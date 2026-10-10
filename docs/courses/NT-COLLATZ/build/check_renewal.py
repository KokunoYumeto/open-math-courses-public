"""Exact finite checks for renewal identities; not proofs of analytic bounds."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def convolution(p, q):
    out = defaultdict(Q)
    for x, a in p.items():
        for y, b in q.items():
            out[add(x, y)] += a*b
    return dict(out)


def first_step(law):
    @lru_cache(None)
    def crossing(s):
        out = defaultdict(Q)
        for v, p in law.items():
            if v[1] > s:
                out[v] += p
            else:
                for x, q in crossing(s-v[1]).items():
                    out[add(v, x)] += p*q
        assert sum(out.values()) == 1
        return dict(out)
    return crossing


def renewal(law, s):
    out = defaultdict(Q, {(0,0):Q(1)})
    pn = {(0,0):Q(1)}
    for _ in range(s):
        pn = {x:p for x,p in convolution(pn, law).items() if x[1] <= s}
        for x,p in pn.items():
            out[x] += p
    assert all(p<=1 for p in out.values())
    return dict(out)


def stopped_words(law, s, word=(), pos=(0,0), mass=Q(1)):
    for v,p in law.items():
        nxt=add(pos,v)
        if nxt[1]>s:
            yield word+(v,),nxt,mass*p
        else:
            yield from stopped_words(law,s,word+(v,),nxt,mass*p)


def main():
    counts=Counter()
    laws=[{(1,1):Q(1,3),(1,2):Q(1,3),(2,2):Q(1,3)},
          {(1,1):Q(1,2),(2,3):Q(1,3),(3,2):Q(1,6)},
          {(1,2):Q(1)}]
    for law in laws:
        crossing=first_step(law)
        alpha=sum(v[0]*p for v,p in law.items())
        beta=sum(v[1]*p for v,p in law.items())
        for s in range(17):
            u=renewal(law,s)
            last=defaultdict(Q)
            for (j,l),a in u.items():
                for v,b in law.items():
                    if l+v[1]>s:
                        last[add((j,l),v)] += a*b
            assert dict(last)==crossing(s)
            counts['last_jump_laws']+=1
            counts['last_jump_points']+=len(last)
            for t in range(9):
                restart=defaultdict(Q)
                for z,p in crossing(s).items():
                    r=z[1]-s
                    if r>t:
                        restart[z]+=p
                    else:
                        for y,q in crossing(t-r).items():
                            restart[add(z,y)]+=p*q
                assert dict(restart)==crossing(s+t)
                counts['nested_threshold_laws']+=1
        for s in range(6):
            stop=defaultdict(Q)
            mean_time=Q(0)
            for word,z,p in stopped_words(law,s):
                stop[z]+=p
                mean_time+=len(word)*p
                assert len(word)<=s+1
                assert sum(v[1] for v in word[:-1])<=s<z[1]
                counts['stopped_words']+=1
            assert dict(stop)==crossing(s)
            assert sum(z[0]*p for z,p in stop.items())==alpha*mean_time
            assert sum(z[1]*p for z,p in stop.items())==beta*mean_time
            counts['bounded_wald_checks']+=2
        # Fixed-length product enumeration checks independence after the random stop.
        for s in range(4):
            joint=defaultdict(Q)
            for word in product(law,repeat=s+3):
                p=Q(1)
                for v in word:
                    p*=law[v]
                z=(0,0)
                for n,v in enumerate(word,1):
                    z=add(z,v)
                    if z[1]>s:
                        break
                joint[z,word[n:n+2]]+=p
            for z,p in crossing(s).items():
                for tail in product(law,repeat=2):
                    assert joint[z,tail]==p*law[tail[0]]*law[tail[1]]
                    counts['unused_tail_cells']+=1
            assert sum(joint.values())==1
    expected={(2,3):Q(6,27),(3,3):Q(7,27),(2,4):Q(3,27),
              (3,4):Q(7,27),(4,4):Q(4,27)}
    assert first_step(laws[0])(2)==expected
    assert sum(z[0]*p for z,p in expected.items())==Q(76,27)
    assert sum(z[1]*p for z,p in expected.items())==Q(95,27)
    # Bounded holding-law coefficients: omitted values cannot reach these endpoints.
    holding={}
    failure={0:Q(1)}
    q=lambda b:Q(b-1,2**b)
    for j in range(1,5):
        for l,p in failure.items():
            if l+3<=20:
                holding[j,l+3]=p/4
        nxt=defaultdict(Q)
        for l,p in failure.items():
            for b in range(2,21-l):
                if b!=3:
                    nxt[l+b]+=p*q(b)
        failure=dict(nxt)
    pair=convolution(holding,holding)
    state={(0,0):Q(1)}  # (sum, number of marks); second mark terminates.
    direct={}
    for j in range(1,5):
        nxt=defaultdict(Q)
        done=defaultdict(Q)
        for (l,marks),p in state.items():
            for b in range(2,21-l):
                m=marks+int(b==3)
                if m==2:
                    done[l+b]+=p*q(b)
                else:
                    nxt[l+b,m]+=p*q(b)
        for l,p in done.items():
            direct[j,l]=p
        state=dict(nxt)
    for j in range(2,5):
        for l in range(6,21):
            assert pair.get((j,l),Q(0))==direct.get((j,l),Q(0))
            counts['marked_block_sum_coefficients']+=1
    assert pair[3,8]==Q(1,32)
    # Algebra in the convolution argument, on exact rational finite grids.
    f=lambda h,x:min(x*x/h,abs(x))
    for h in range(1,13):
        for x in [Q(i,2) for i in range(-16,17)]:
            for y in [Q(i,3) for i in range(-12,13)]:
                assert abs(f(h,x)-f(h,y))<=2*abs(x-y)
                assert f(h,x)<=f(1,x)
                counts['decay_weight_inequalities']+=1
    # Exact tail-sum identity used for exponential overshoot moments.
    for a in [Q(3,2),Q(5,4),Q(2)]:
        for k in range(21):
            assert a**k==1+(a-1)*sum(a**(r-1) for r in range(1,k+1))
            counts['tail_sum_identities']+=1
    print(json.dumps({'passed':True,'arithmetic':'exact integers and fractions',
        'counts':dict(counts),
        'ranges':{'finite_increment_laws':3,'last_jump_thresholds':[0,16],
            'added_thresholds':[0,8],'stopped_word_thresholds':[0,5],
            'unused_tail_thresholds':[0,3],'unused_tail_length':2,
            'marked_total_entries_max':4,'marked_total_height_max':20},
        'scope':'Finite regression checks of exact renewal, last-jump, restart, bounded Wald and block-factorization identities. Bounded holding coefficients include every word reaching the specified endpoints. Infinite analytic probability estimates have written proofs and are not certified by these computations.'},indent=2))


if __name__=='__main__':
    main()

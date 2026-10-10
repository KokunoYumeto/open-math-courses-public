"""Exact finite regressions for geometric words and controlled conditioning.

The concentration theorem is proved analytically in the lesson. Rational
exponential tilts, exact geometric tails, cylinder laws and finite conditional
experiments are checked here; no numerical test is an infinite proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb
import json


def compositions(total, length):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total-length+2):
        for rest in compositions(total-first, length-1):
            yield (first,)+rest


def geometric_tail(k, q):
    return 1-sum((Q(comb(s-1,k-1),2**s) for s in range(k,q)),Q(0))


def valuation_word(m, k):
    word=[]
    for _ in range(k):
        z=3*m+1
        a=(z & -z).bit_length()-1
        word.append(a)
        m=z//2**a
    return tuple(word)


def cylinder(word):
    s=0
    c=0
    for a in word:
        c=3*c+2**s
        s+=a
    modulus=2**(s+1)
    residue=pow(3**len(word),-1,modulus)*(2**s-c)%modulus
    return residue,modulus,c


def law(starts, weights, k):
    out=defaultdict(Q)
    for m,p in zip(starts,weights):
        out[valuation_word(m,k)]+=p
    return dict(out)


def comparison(starts, weights, k, q):
    p=law(starts,weights,k)
    # Outside the finite actual support, all remaining geometric mass contributes.
    gp={w:Q(1,2**sum(w)) for w in p}
    distance=sum(abs(p[w]-gp[w]) for w in p)+1-sum(gp.values())
    residues=defaultdict(Q)
    for m,mass in zip(starts,weights):
        residues[m%2**q]+=mass
    eta=sum(abs(residues[r]-Q(1,2**(q-1))) for r in range(1,2**q,2))
    tail=geometric_tail(k,q)
    assert distance<=eta+2*tail
    return distance,tail,eta


def main():
    counts=Counter()
    for k in range(1,7):
        for s in range(k,13):
            words=list(compositions(s,k))
            assert len(words)==comb(s-1,k-1)
            for p in [Q(1,2),Q(1,3),Q(3,5)]:
                each=p**k*(1-p)**(s-k)
                total=sum((each for _ in words),Q(0))
                assert total==comb(s-1,k-1)*each
                assert each/total==Q(1,len(words))
                counts['fixed_sum_laws']+=1
    for k in range(1,33):
        for q in range(k,4*k+7):
            upper=geometric_tail(k,q)
            lower=1-geometric_tail(k,q+1)
            assert upper<=2**k*Q(3,4)**q
            assert lower<=Q(3,5)**k*Q(4,3)**q
            counts['exact_tilt_tail_pairs']+=1
    for r in [Q(1,2),Q(3,4),Q(1),Q(4,3),Q(3,2)]:
        for cutoff in range(1,21):
            ratio=r/2
            partial=sum((ratio**b for b in range(1,cutoff+1)),Q(0))
            remainder=ratio**(cutoff+1)/(1-ratio)
            assert partial+remainder==r/(2-r)
            counts['generating_function_remainders']+=1
    for z in [Q(3,4)+Q(7*j,120) for j in range(11)]:
        assert Q(3,4)<=z<=Q(4,3)
        assert 6*(2-z)**2-2*z==2*(3*z-4)*(z-3)>=0
        counts['second_derivative_certificate_instances']+=1
    for k in range(1,6):
        for s in range(k,11):
            for w in compositions(s,k):
                r,modulus,c=cylinder(w)
                assert r%2==1 and (3**k*r+c)%modulus==2**s
                for t in range(3):
                    assert valuation_word(r+t*modulus,k)==w
                    counts['cylinder_lifts']+=1
    for q in range(1,12):
        starts=list(range(1,2**q,2))
        for k in range(1,6):
            for weights in [[Q(1,len(starts))]*len(starts),
                            [Q(i+1,len(starts)*(len(starts)+1)//2) for i in range(len(starts))]]:
                comparison(starts,weights,k,q)
                counts['finite_word_law_comparisons']+=1
            p=law(starts,[Q(1,len(starts))]*len(starts),k)
            for s in range(k,q):
                for w in compositions(s,k):
                    assert p[w]==Q(1,2**s)
                    counts['short_cylinder_probabilities']+=1
    for b in [1,3,17,63,100,257]:
        for q in range(1,9):
            starts=list(range(1,2*b,2))
            _,_,eta=comparison(starts,[Q(1,b)]*b,3,q)
            assert eta<=Q(2**(q-1),b)
            counts['incomplete_period_samples']+=1
    for b,c in product(range(2,8),repeat=2):
        pairmass1=(b-1)*Q(1,2**b)
        pairmass2=(c-1)*Q(1,2**c)
        for a,d in product(range(1,b),range(1,c)):
            joint=Q(1,2**(b+c))/(pairmass1*pairmass2)
            assert joint==Q(1,(b-1)*(c-1))
            counts['separate_pair_conditionings']+=1
    # A finite non-geometric test law with probabilities 4/7, 2/7, 1/7.
    # Used only for the event-algebra and independence identities, not tail bounds.
    def regular(w):
        return all(abs(sum(w[i:j])-2*(j-i))<=1 for i in range(len(w)) for j in range(i+1,len(w)+1))
    def probability(w):
        p=Q(1)
        for a in w:
            p*=Q(2**(3-a),7)
        return p
    cells=defaultdict(lambda:defaultdict(Q))
    bad=global_bad=no_cross=Q(0)
    added=Q(0)
    for w in product(range(1,4),repeat=4):
        weight=probability(w)
        sums=[0]
        for a in w:
            sums.append(sums[-1]+a)
        crossing=next((j for j in range(1,5) if sums[j]>4),None)
        whole=regular(w)
        if not whole:
            global_bad+=weight
        if crossing is None:
            no_cross+=weight
        chosen=crossing is not None and regular(w[:crossing])
        if not chosen:
            bad+=weight
        else:
            j=crossing
            cells[j,sums[j]][w[j:]]+=weight
            if not whole:
                added+=weight
        if whole and crossing is not None:
            assert chosen
        counts['prefix_event_words']+=1
    assert bad<=global_bad+no_cross
    assert added<=global_bad
    for (j,l),tail_law in cells.items():
        mass=sum(tail_law.values())
        for tail in product(range(1,4),repeat=4-j):
            assert tail_law[tail]==mass*probability(tail)
            counts['unused_tail_factorizations']+=1
    assert geometric_tail(2,6)==Q(3,16)
    assert cylinder((2,1))==(9,16,7)
    assert valuation_word(1,2)==(2,2)
    w=list(compositions(5,3))
    freq=Counter(a[0] for a in w)
    assert [Q(freq[a],len(w)) for a in [1,2,3]]==[Q(1,2),Q(1,3),Q(1,6)]
    for d in [Q(1,4),Q(1,1000)]:
        assert abs(d)+abs(-d)==2*d
        assert abs(d/d)+abs(-d/d)==2
    print(json.dumps({'passed':True,'arithmetic':'exact integers and fractions',
        'counts':dict(counts),'ranges':{'geometric_sum_lengths':[1,32],'residue_bits':[1,11],
        'cylinder_total_max':10,'prefix_event_word_length':4},
        'scope':'Finite regressions, exact infinite-tail complements and rational exponential tilts. Analytic concentration and general comparison/conditioning theorems are proved in the lesson; no formal certification is claimed.'},indent=2))


if __name__=='__main__':
    main()

"""Exact finite tests for coarsening and scheduled probability transport.
These finite functional graphs and rational laws do not prove the asymptotic
Collatz input. That input and the general inequalities have written proofs.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json

counts=Counter()
def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),Q(0))/2
def push(p,f,m):
    out=[Q(0)]*m
    for a,j in zip(p,f): out[j]+=a
    return tuple(out)
def comps(total,n):
    if n==1:
        yield (total,)
    else:
        for a in range(total+1):
            for b in comps(total-a,n-1): yield (a,)+b

laws=[tuple(Q(a,4) for a in c) for c in comps(4,3)]
for p,q in product(laws,repeat=2):
    u,v=p[0]-q[0],p[2]-q[2]
    merged=2*(tv(p,q)-tv(push(p,(0,1,0),2),push(q,(0,1,0),2)))
    assert merged==abs(u)+abs(v)-abs(u+v)
    assert merged==(2*min(abs(u),abs(v)) if u*v<0 else 0)
    assert tv(p,q)==max(abs(sum((p[i]-q[i] for i in range(3) if mask>>i&1),Q(0))) for mask in range(8))
    counts['merged_pair_and_event_supremum']+=1
    for f in product(range(2),repeat=3):
        out=2*tv(push(p,f,2),push(q,f,2))
        fibre=sum(abs(sum((p[i]-q[i] for i in range(3) if f[i]==z),Q(0))) for z in range(2))
        assert out==fibre and out<=2*tv(p,q)
        counts['observation_fibres']+=1

sets=[{i for i in range(4) if mask>>i&1} for mask in range(1,16)]
for weights in [(Q(1),)*4,tuple(Q(1,2*i+3) for i in range(4)),(Q(2),Q(7),Q(1),Q(3))]:
    for s,t in product(sets,repeat=2):
        ws=sum(weights[i] for i in s); wt=sum(weights[i] for i in t)
        wi=sum((weights[i] for i in s&t),Q(0))
        p=tuple(weights[i]/ws if i in s else Q(0) for i in range(4))
        q=tuple(weights[i]/wt if i in t else Q(0) for i in range(4))
        assert tv(p,q)==1-wi/max(ws,wt)
        assert tv(p,q)==max(ws-wi,wt-wi)/max(ws,wt)
        counts['weighted_overlap']+=1
        for f in product(range(2),repeat=4):
            assert tv(push(p,f,2),push(q,f,2))<=tv(p,q)
            counts['weighted_output_comparison']+=1

# Exhaust all maps of {1,2,3,4} to itself, including maps that move 1,
# cycles, nonmonotone orbits and nonpassage. Infinity is determined by
# an actual repeated state in the finite graph, not by a truncated run.
def passage(mapping,start,q):
    seen=set(); n=start; k=0
    while n>q:
        if n in seen: return None,1
        seen.add(n); n=mapping[n-1]; k+=1
    return k,n
def bad(t,k): return t is None or t>k
law4=[tuple(Q(int(i==j)) for i in range(4)) for j in range(4)]
law4 += [(Q(1,4),)*4, (Q(1,2),Q(0),Q(1,3),Q(1,6))]
for mapping in product(range(1,5),repeat=4):
    pt={(n,q):passage(mapping,n,q) for n in range(1,5) for q in range(1,5)}
    for n,h,q,k,budget in product(range(1,5),range(1,5),range(1,5),range(4),range(4)):
        tq,f=pt[n,q]; th=pt[n,h][0]; tf=pt[f,h][0]
        assert int(bad(tf,k))<=int(bad(th,k))
        assert int(bad(th,k+budget))<=int(bad(tf,k))+int(bad(tq,budget))
        counts['pointwise_time_pair']+=1
    # Every pair of these laws and every auxiliary threshold, with no
    # independence assumption and no required ordering of target and threshold.
    for p,q,threshold in product(law4,law4,range(1,5)):
        f=tuple(pt[n,threshold][1]-1 for n in range(1,5))
        dist=tv(push(p,f,4),push(q,f,4))
        h=2; k=1; budget=2
        prev=sum(p[n-1]*bad(pt[n,h][0],k) for n in range(1,5))
        after=sum(q[n-1]*bad(pt[n,h][0],k+budget) for n in range(1,5))
        fail=sum(q[n-1]*bad(pt[n,threshold][0],budget) for n in range(1,5))
        assert after<=prev+dist+fail
        counts['integrated_one_step']+=1
    # Two steps, including a nontrivial mixed intermediate law.
    for i in range(4):
        chain=[law4[i],law4[4],law4[(i+1)%4]]
        thresholds=(4-i,1+i); budgets=(0,2)
        rhs=sum(chain[0][n-1]*bad(pt[n,1][0],0) for n in range(1,5))
        for j in range(2):
            f=tuple(pt[n,thresholds[j]][1]-1 for n in range(1,5))
            rhs+=tv(push(chain[j],f,4),push(chain[j+1],f,4))
            rhs+=sum(chain[j+1][n-1]*bad(pt[n,thresholds[j]][0],budgets[j]) for n in range(1,5))
        lhs=sum(chain[-1][n-1]*bad(pt[n,1][0],sum(budgets)) for n in range(1,5))
        assert lhs<=rhs
        counts['two_step_recurrence']+=1

# Exact source movement with beta=2, q=3 is a finite illustration of the
# general overlap argument, not a substitute for the fixed alpha theorem.
def odd_interval(lo,hi,left=True,right=True):
    return {n for n in range(1,int(hi)+2,2) if (n>=lo if left else n>lo) and (n<=hi if right else n<hi)}
for b in range(3,13):
    for r in (Q(0),Q(1,4),Q(1,2),Q(3,4)):
        x=b+r
        s=odd_interval(b*b,b**3); t=odd_interval(x*x,x**3)
        assert s-t==odd_interval(b*b,x*x,True,False)
        assert t-s==odd_interval(b**3,x**3,False,True)
        eps=Q(max(len(s-t),len(t-s)),max(len(s),len(t)))
        envelope=((x**3-b**3)/2+1)/(Q(b**3-b*b,2)-1)
        assert eps<=envelope
        if r==0: assert eps==0
        counts['exact_floor_source_sets']+=1

def collatz_step(n):
    m=3*n+1
    while m%2==0: m//=2
    return m
def actual_pass(n,q):
    seen=set(); k=0
    while n>q:
        if n in seen: return None,1
        seen.add(n); n=collatz_step(n); k+=1
    return k,n
for n in range(1,202,2):
    for b in range(1,12):
        for r in (Q(0),Q(1,4),Q(3,4)):
            assert actual_pass(n,b+r)==actual_pass(n,b)
            counts['integer_state_floor_identity']+=1

alpha=Q(1001,1000); eta=Q(5097587,77645938)
assert eta<Q(1,4) and 1/(10*alpha*(alpha-1))==100/alpha
assert 3*(100/alpha)+1==300/alpha+1
for a in (alpha,Q(3,2),Q(2)):
    for j in range(10):
        L=Q(23,7); ell=Q(7,10)
        exact=sum((a**i*L for i in range(j)),Q(0))/(10*ell)
        assert exact==L*(a**j-1)/(10*ell*(a-1))
        log_y0=a*L; log_yj=a**j*log_y0
        assert exact==(log_yj-log_y0)/(10*a*(a-1)*ell)
        counts['exact_geometric_log_coordinates']+=1

p=(Q(1,2),Q(1,3),Q(1,6));q=tuple(reversed(p))
assert tv(p,q)==Q(1,3) and tv(push(p,(0,1,0),2),push(q,(0,1,0),2))==0
assert Q(1,3)+Q(1,5)+Q(1,7)==Q(71,105)
assert Q(1,5)+Q(1,7)+Q(1,9)==Q(143,315)
assert Q(108,143)-Q(36,71)==Q(2520,10153)
assert Q(1,3)/Q(71,105)==Q(35,71)
assert max(100-3,0)==97 and max(100-1,0)==99
assert 2+4==6 and Q(1,4)+Q(1,16)==Q(5,16)
assert Q(1,4)/(1-Q(1,4))==Q(1,3)
counts['solved_exercises']=4
print(json.dumps({'passed':True,'arithmetic':'exact rational and finite integer only','counts':dict(counts),
 'finite_scope':'All 256 endomaps of four states, exact law comparisons and selected finite Collatz paths. Cycle detection establishes nonpassage only for the finite graph being tested.',
 'general_proof':'The general statements and asymptotic Collatz comparison are proved in the lesson and its explicit preceding dependencies, not certified by these tests.'},indent=2))

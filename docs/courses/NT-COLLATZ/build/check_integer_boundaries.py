"""Exact finite regressions for integer fibres and boundary replacement.

General bounds are proved in the lesson, not inferred from these tests.
No floating-point arithmetic, unbounded orbit searches or Lean workers.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, gcd
import json


def compositions(s,r):
    if r==1:
        if s>=1:
            yield (s,)
        return
    for a in range(1,s-r+2):
        for tail in compositions(s-a,r-1):
            yield (a,)+tail


def coordinates(word):
    total=constant=0
    partial=[(0,0)]
    for a in word:
        constant=3*constant+2**total
        total+=a
        partial.append((total,constant))
    return total,constant,partial


def itinerary(n,r):
    vals=[]
    states=[n]
    for _ in range(r):
        k=3*n+1
        a=(k & -k).bit_length()-1
        n=k//2**a
        vals.append(a)
        states.append(n)
    return tuple(vals),states


def pmf(r,s):
    return F(comb(s-1,r-1),2**s) if s>=r else F(0)


def pow_rat(b,s):
    return F(b**s) if s>=0 else F(1,b**(-s))


def main():
    counts=dict(cylinders=0,inverses=0,first_passages=0,reversal_offsets=0,
                residue_tests=0,point_mass_bounds=0,separated_intervals=0,
                boundary_bounds=0,boundary_word_endpoints=0,boundary_disagreements=0,normalizations=0,
                rational_log_enclosures=0)
    for r in range(1,4):
        cache={n:itinerary(n,r) for n in range(1,512,2)}
        for word in product(range(1,5),repeat=r):
            total,c,partial=coordinates(word)
            mod=2**(total+1)
            residue=(2**total-c)*pow(3**r,-1,mod)%mod
            offset=F(c,2**total)
            assert 0<offset<3**r
            rev=word[::-1]
            z=F(0)
            t=0
            for j,a in enumerate(rev):
                t+=a
                z+=F(3**j,2**t)
            assert z==offset
            counts['reversal_offsets']+=1
            for n,(actual,states) in cache.items():
                assert (actual==word)==(n%mod==residue)
                counts['cylinders']+=1
                for x in (10,30,100):
                    lower=max(F(2**aj*x-cj,3**j) for j,(aj,cj) in enumerate(partial[:-1]))
                    upper=F(2**total*x-c,3**r)
                    lhs=actual==word and all(y>x for y in states[:-1]) and states[-1]<=x
                    rhs=n%mod==residue and lower<n<=upper
                    assert lhs==rhs
                    counts['first_passages']+=1
            for m in range(1,204,2):
                n=F(2**total*m-c,3**r)
                exists=m>offset and (2**total*m-c)%3**r==0
                assert exists==(n.denominator==1 and n>0)
                if exists:
                    actual,states=itinerary(n.numerator,r)
                    assert actual==word and states[-1]==m and n.numerator%2==1
                    assert (3**r*n+c)/2**total==m
                counts['inverses']+=1

    words=[(1,3),(2,2),(3,1)]
    pieces=[]
    for word in words:
        piece=[n for n in range(1,501,2) if itinerary(n,2)[0]==word
               and min(itinerary(n,2)[1][:-1])>100 and itinerary(n,2)[1][-1]<=100]
        if piece:
            pieces.append(piece)
    flattened=[n for p in pieces for n in p]
    assert len(flattened)==len(set(flattened))
    for lo,hi in [(F(0),F(500)),(F(201,2),F(301,2)),(F(115),F(147))]:
        selected=[n for n in flattened if lo<=n<=hi]
        for q in (1,3,5,7,9,25):
            for z in range(q):
                assert abs(sum(n%q==z for n in selected)-F(len(selected),q))<=len(pieces)
                counts['residue_tests']+=1
    assert [n for n in range(1,201,2) if itinerary(n,2)[0]==(1,3)
            and min(itinerary(n,2)[1][:-1])>100 and itinerary(n,2)[1][-1]<=100]==[115,147]
    assert F(2)-F(2,3)==F(4,3)>1

    for r in range(1,41):
        mode=pmf(r,2*r-1)
        if r>1:
            assert mode==pmf(r,2*r-2)
        for s in range(r,r+150):
            p=pmf(r,s)
            assert p<=mode and p*p<=F(1,4*r)
            counts['point_mass_bounds']+=1
    for k in range(100):
        assert 4*(k+1)**3-(2*k+1)**2*(k+2)==3*k+2

    for a,b in [(3,2),(2,3),(5,2),(5,3),(4,3)]:
        assert gcd(a,b)==1
        for R in range(1,6):
            M=4*a**(2*R)+1
            intervals=[]
            for r in range(1,R+1):
                for s in range(-3,9):
                    scale=pow_rat(b,s)/a**r
                    intervals.append(((M-a**r)*scale,M*scale,r,s))
            intervals.sort()
            for left,right in zip(intervals,intervals[1:]):
                assert left[1]<right[0],(a,b,R,left,right)
                counts['separated_intervals']+=1
    assert 5-3<=F(9,2)<=5 and 5-3<=F(9,4)<=5
    assert pow_rat(4,1)/pow_rat(2,2)==pow_rat(4,2)/pow_rat(2,4)==1

    cases=[]
    for r0,R,B in [(1,2,401),(1,3,2917),(4,4,26245)]:
        E=list(range(B,B+52,2)) # one interval in the odd progression
        I=tuple(range(r0,R+1))
        for Y,U in [(F(10),F(B)),(F(B,2),F(2*B)),
                    (F(B-4),F(3*B)),(F(1),F(4*B))]:
            cases.append((E,I,Y,U,B,r0,R))
    cases.append((list(range(401,453,2)),(1,2),F(362),F(363),401,1,2))
    for E,I,Y,U,B,r0,R in cases:
        assert B>4*3**(2*R)
        raw=0
        for r in I:
            cap=U*3**r/F(B-3**r)
            top=0
            while 2**(top+1)<=cap:
                top+=1
            for s in range(r,top+1):
                for word in compositions(s,r):
                    _,c,_=coordinates(word)
                    for M in E:
                        if (2**s*M-c)%3**r:
                            continue
                        n=F(2**s*M-c,3**r)
                        n0=F(2**s*M,3**r)
                        diff=int(Y<=n<=U)!=int(Y<n0<=U)
                        if diff:
                            assert any(v*3**r/F(2**s)<=M<=v*3**r/F(2**s)+3**r for v in (Y,U))
                            counts['boundary_disagreements']+=1
                        raw+=diff
                        counts['boundary_word_endpoints']+=1
        delta=2*F(raw)/U
        harmonic=sum((F(1,M) for M in E),F(0))
        error=F(8*3**R*len(I),B)
        coefficient=2*(1+Y/U)*harmonic
        residual=delta-error
        assert residual<=0 or residual*residual*r0<=coefficient*coefficient
        counts['boundary_bounds']+=1
    assert counts['boundary_disagreements']>0

    for lower in range(1,41):
        for upper in range(lower,101):
            h=sum(lower<=n<=upper for n in range(1,102,2))
            assert abs(h-F(upper-lower,2))<=1
            if h and upper>=2*lower+4:
                assert F(upper,2*h)<=2
            counts['normalizations']+=1
    z=F(1,2)
    log3_upper=2*sum((z**(2*j+1)/(2*j+1) for j in range(4)),F(0))+2*z**9/(9*(1-z*z))
    d_lower=F(2,7)+F(2,3*7**3)
    alpha=F(1001,1000)
    assert log3_upper<F(11,10)
    assert d_lower>F(287,1000)
    assert (alpha**3-1)/F(287,1000)<F(11,1000)
    assert F(11,10)*(alpha**3-1)/F(287,1000)<F(29,2500)
    counts['rational_log_enclosures']=4
    result=dict(passed=True,arithmetic='Exact integers and fractions',
                counts=counts,examples={'first_passage_starts':[115,147],
                'first_passage_endpoints':[65,83],
                'true_start':11,'zero_offset_start':'104/9',
                'subset_discrepancy':'4/3'},
                scope='Finite regressions only. The general inverse, separation and boundary bounds are proved in the lesson.',
                lean_certification=False)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()


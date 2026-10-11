"""Exact finite regressions for rational blocks, counts and summation by parts.
The general irrational and asymptotic assertions are proved in the lesson.
"""
from fractions import Fraction as F
from math import gcd,isqrt
import json

def frac(x): return x-x.numerator//x.denominator
def dist(x,y):
    z=frac(x-y)
    return min(z,1-z)
def discrepancy(xs):
    groups={}
    for x in xs: groups[x]=groups.get(x,0)+1
    k=0; values=[F(0)]; n=len(xs)
    for x,m in sorted(groups.items()):
        values.extend([k-n*x,k+m-n*x]); k+=m
    return max(values)-min(values)
def count(xs,a,b): return sum(a<=x<b for x in xs)
def variation(w):
    return sum(abs(b-a) for a,b in zip([F(0)]+w,w+[F(0)]))
def rotation_certificate(M):
    # Test |q sqrt(2)-p|<1/M using rational square comparisons only.
    for q in range(1,M+1):
        k=isqrt(2*q*q)
        for p in [k,k+1]:
            lo=F(p)-F(1,M); hi=F(p)+F(1,M)
            if (lo<0 or lo*lo<2*q*q) and 2*q*q<hi*hi:
                g=gcd(p,q)
                return p//g,q//g
    raise AssertionError(M)
def main():
    blocks=0; arcs=0; maximum=F(0)
    for q in range(1,15):
        for p in range(1,q+1):
            if gcd(p,q)!=1: continue
            for M in [q,2*q+1]:
                for sign in [-1,1]:
                    alpha=F(p,q)+sign*F(1,3*q*M)
                    u=F(7,31)
                    x=[frac(u+i*alpha) for i in range(q)]
                    y=[frac(u+F(i*p,q)) for i in range(q)]
                    assert len(set(y))==q
                    assert discrepancy(y)<=1 and discrepancy(x)<=5
                    maximum=max(maximum,discrepancy(x))
                    delta=(q-1)*abs(alpha-F(p,q))
                    points=sorted(set([F(0),F(1)]+x+y))
                    ends=sorted(set(points+[(a+b)/2 for a,b in zip(points,points[1:])]))
                    # All states of interval membership, including exact boundaries.
                    for i,a in enumerate(ends):
                        for b in ends[i+1:]:
                            changes=[j for j in range(q) if (a<=x[j]<b)!=(a<=y[j]<b)]
                            if q>1:
                                assert len(changes)<=4
                                for j in changes:
                                    assert min(dist(y[j],a),dist(y[j],b))<=delta
                            assert abs(count(x,a,b)-q*(b-a))<=5
                            arcs+=1
                    blocks+=1
    greedy=[]
    for N in list(range(1,65))+[100,127,128,200,511,1000]:
        M=N; covered=0; stages=[]
        while M:
            p,q=rotation_certificate(M); b=M//q; rem=M-b*q
            assert 1<=q<=M and gcd(p,q)==1
            assert 2*rem<M and q>F(M,4)  # c=1/4, nu=1
            stages.append(dict(M=M,p=p,q=q,blocks=b,remainder=rem))
            covered+=b*q; M=rem
        assert covered==N and len(stages)<=N.bit_length()
        assert 5*sum(z['blocks'] for z in stages)<=20*N.bit_length()
        if N in [64,200,1000]: greedy.append(dict(N=N,stages=stages))
    abel=0
    for n in range(1,31):
        a=[F((j*j+3*j)%17-8,13) for j in range(n)]
        for w in [[F((3*j)%11-5,7) for j in range(n)],
                  [F(min(j+1,n-j),n*n) for j in range(n)],
                  [F(1) for _ in range(n)]]:
            S=[]; v=F(0)
            for z in a: v+=z; S.append(v)
            left=sum(x*y for x,y in zip(w,a))
            right=w[-1]*S[-1]+sum((w[j]-w[j+1])*S[j] for j in range(n-1))
            assert left==right
            assert abs(left)<=max(map(abs,S))*variation(w)
            abel+=1
    for R in range(1,101):
        w=[F(R-abs(n),R*R) for n in range(-R+1,R)]
        assert sum(w)==1 and variation(w)==F(2,R) and max(w)==F(1,R)
    # Exact rational enclosures for the picture and exercise.
    assert F(1414,1000)**2<2<F(1415,1000)**2
    expected=[False,True,False,True,False]
    for i in range(5):
        integer=isqrt(2*i*i) if i else 0
        lo=F(1,10)+i*F(1414,1000)
        hi=F(1,10)+i*F(1415,1000)
        k=lo.numerator//lo.denominator
        assert hi<k+1
        lo-=k; hi-=k
        if expected[i]: assert F(8,25)<lo<=hi<F(13,25)
        else: assert hi<F(8,25) or lo>=F(13,25)
    grid=[frac(F(1,10)+F(7*i,5)) for i in range(5)]
    assert count(grid,F(8,25),F(13,25))==1
    return dict(passed=True,counts=dict(rational_blocks=blocks,exact_intervals=arcs,
        abel_identities=abel,triangular_profiles=100,irrational_greedy_decompositions=70),
        maximum_tested_block_discrepancy=str(maximum),sqrt2_greedy=greedy,
        picture_counts=dict(grid=1,rotation=2),
        scope="Exact finite regression only. Theorems4-7 and irrational lower bounds use the written proofs, not these tests.")
if __name__=='__main__': print(json.dumps(main(),indent=2))


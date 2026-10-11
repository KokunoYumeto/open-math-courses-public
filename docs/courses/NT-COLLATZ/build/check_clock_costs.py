"""Exact finite checks for first-entrance costs, clock identities and fibre counts.
The asymptotic density conclusions are proved in the written lesson, not here.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json

def S(m):
    v=3*m+1; a=0
    while v%2==0: v//=2; a+=1
    return v,a
def T(n): return (3*n+1)//2 if n%2 else n//2
def C(n): return 3*n+1 if n%2 else n//2
def iterate(f,n,k):
    for _ in range(k): n=f(n)
    return n

def main():
    checks=Counter()
    for images in product(range(4),repeat=4):
        for mask in range(1,16):
            target={i for i in range(4) if mask>>i&1}
            for start in range(4):
                seen=[]; n=start
                while n not in target and n not in seen:
                    seen.append(n); n=images[n]
                if n in target:
                    assert len(seen)==len(set(seen))
                    assert all(v not in target for v in seen)
                    checks['finite_function_first_entrances']+=1
    for m in range(1,512,2):
        for H in [2,3,5,10,25]:
            n=m; states=[]; A=0
            while n>H and len(states)<200:
                states.append(n); n,a=S(n); A+=a
            assert n<=H, (m,H,'bounded test did not reach target')
            k=len(states)
            assert len(set(states))==k
            P=F(1)
            for v in states: P*=1+F(1,3*v)
            assert 2**A*n==3**k*m*P
            if k:
                r=2*((H+1)//2)+1
                assert r>H and r%2
                ordered=sorted(states)
                assert all(v>=r+2*j for j,v in enumerate(ordered))
                assert sum((F(1,v) for v in states),F()) <= sum((F(1,r+2*j) for j in range(k)),F())
                Pmax=F(1)
                for j in range(k): Pmax*=1+F(1,3*(r+2*j))
                assert P<=Pmax
                checks['distinct_reciprocal_costs']+=1
            for a in [0,1,4]:
                N=2**a*m
                assert iterate(T,N,a+A)==n
                assert iterate(C,N,a+k+A)==n
                checks['exact_common_clock_endpoints']+=1
            checks['exact_valuation_products']+=1
    for b in [2,3,4,6]:
        base=[m for m in range(1,80) if m%b]
        for modulus in [2,3,5,7]:
            E={m for m in base if m%modulus==1}
            for X in [1,2,3,7,20,60,199]:
                counts=0; scale=1
                while scale<=X:
                    counts+=sum(m*scale<=X for m in E);scale*=b
                lifted=[]
                for n in range(1,X+1):
                    m=n
                    while m%b==0:m//=b
                    if m in E:lifted.append(n)
                assert counts==len(lifted)
                eps=max([F(sum(m<=y for m in E),y) for y in range(1,max(X,79)+1)]+[F()])
                assert counts<=F(b,b-1)*eps*X
                checks['exact_base_fibre_counts']+=1
    for X in range(1,501):
        powers=0;t=1
        while t<=X:powers+=1;t*=2
        E={m for m in range(3,X+1,2)}
        lifted=0
        for n in range(1,X+1):
            m=n
            while m%2==0:m//=2
            lifted+=m in E
        assert lifted==X-powers
        assert len(E)<=F(X,2)
        checks['sharp_factor_examples']+=1
    seq=[];n=7;A=0
    while n>2:
        seq.append(n);n,a=S(n);A+=a
    assert seq==[7,11,17,13,5] and n==1 and A==11
    assert iterate(T,56,14)==iterate(C,56,19)==1
    assert F(2**11,3**5*7)==F(2048,1701)
    example=[]
    for n in range(1,61):
        m=n
        while m%3==0:m//=3
        if m in {2,4,5}:example.append(n)
    assert example==[2,4,5,6,12,15,18,36,45,54]
    # Coefficients of log2 and log3 in the two cleared-denominator identities.
    d=(2,-1)
    assert tuple(x+y for x,y in zip((0,1),d))==(2,0)
    assert tuple(x+y for x,y in zip((1,1),d))==(3,0)
    print(json.dumps({'passed':True,'arithmetic':'exact integers and fractions',
      'counts':dict(checks),'example':{'input':56,'odd_prefix':[7,11,17,13,5,1],
      'odd_returns':5,'valuation_sum':11,'shortcut_time':14,'ordinary_time':19,
      'correction_product':'2048/1701'},
      'scope':'Finite function, exact trajectory, reciprocal-cost and fibre-count regressions. '
      'Logarithmic integral bounds, arbitrary input sizes and density conclusions rely on the written proofs. '
      'No infinite-orbit or Lean certification.'},indent=2))

if __name__=='__main__':main()

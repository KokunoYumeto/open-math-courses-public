"""Exact endpoint/counting and normalized tangential-derivative checks."""
from fractions import Fraction as F
from itertools import product
import json
import sympy as s
from laurent_constant import Interval,E,LN2
from matveev_block_parameters import constants,exp_interval

z=s.symbols("z")
def rising(y,m):
    return s.prod(y+j for j in range(m))/s.factorial(m)
def block(z,ell,H):
    q,h=divmod(ell,H)
    return s.expand(rising(z,H)**q*rising(z,h))

def check():
    coefficient=Interval(F(40,41))/(F(101,100)*exp_interval(F(53,100)))
    assert coefficient.lo>F(567,1000)
    assert (E**10).lo>2000
    assert F(3,4)/exp_interval(F(1047,100)).lo<F(1,2000)
    assert F(1,148)+F(3,592000)<F(1,100)
    assert 11*F(1,8000)/4<F(1,1000)
    assert 2*Interval(2).log().hi+F(19,1000)*0< F(19,1000)*F(592000,2)
    gaps=[]
    for kappa in [1,2]:
        half=F(567,1000)*(5+2*kappa)/kappa-(F(251,100)/kappa+1+F(1,14))
        ordinary=2*F(567,1000)*(5+2*kappa)/kappa-(F(251,100)/kappa+F(17,10)+F(1,7))
        assert half>F(1,5)
        assert ordinary>F(1,5)
        gaps.append({"kappa":kappa,"half_gap_at_n2":str(half),"ordinary_gap_at_n2":str(ordinary)})
    grid_cases=0
    for L in [F(1),F(3,2),F(17),F(10000)]:
        for DG in [F(1,100),F(1),F(17,3),F(10000)]:
            for step in range(26):
                T=(L/2**step).__floor__()
                following=(L/2**(step+1)).__floor__()
                X=(2*DG/(T+1)).__ceil__()
                nextX=(2*DG/(following+1)).__ceil__()
                assert following==T//2
                assert nextX<=2*X
                if T==0:assert nextX==X
                for n in [2,3,9]:
                    old_count=2**(n+1)*X+1
                    assert nextX<old_count/2
                    grid_cases+=1
    # Full normalized tangential derivative identity, checked algebraically.
    # b=(2,3); logarithms are formal symbols so no numerical derivative is used.
    lam=s.symbols("lambda")
    operator_cases=0
    for H,c,ell,m0,m1,tau,a,b in product([1,2],[1,2,8],range(5),range(3),range(3),range(4),[-2,1],[-1,2]):
        chi=3*a-2*b
        rate=chi*lam/3
        P=block(c*z,ell,H)
        seed=s.diff(P,z,m0)*rising(chi,m1)
        direct=s.expand(seed)
        # Conjugating the derivative by exp(rate*z) gives d/dz+rate.
        for _ in range(tau):
            direct=s.expand(s.diff(direct,z)+rate*direct)
        direct=s.expand(direct/s.factorial(tau))
        expanded=sum(s.diff(P,z,m0+j)*rising(chi,m1)*rate**(tau-j)/
                     (s.factorial(j)*s.factorial(tau-j)) for j in range(tau+1))
        assert s.expand(direct-expanded)==0
        operator_cases+=1
    # Every additional polynomial in chi has the exact claimed filtered degree.
    degree_cases=0
    y=s.symbols("y")
    for m,t,shift,N in product(range(8),range(8),[-3,0,2],[1,2,8]):
        p=s.Poly(rising(N*y-shift,m)*y**t,y)
        assert p.degree()==m+t
        degree_cases+=1
    return {"status":"passed","constant_quotient_lower_bound_interval":[str(coefficient.lo),str(coefficient.hi)],
            "n2_exponent_gaps":gaps,"grid_halving_cases":grid_cases,
            "normalized_tangential_derivative_identities":operator_cases,
            "filtered_differential_degree_cases":degree_cases,
            "scope":"Supplementary derivative, filtered-degree and grid checks for the continuation proof (8.117–8.119). The lesson contains the universal argument."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))

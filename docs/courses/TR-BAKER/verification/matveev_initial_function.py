"""Exact initial equations and triangular jet changes; finite supplementary check."""
from itertools import product
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json
import sympy as s
from laurent_constant import Interval,E
from matveev_block_parameters import exp_interval,constants

z=s.symbols("z")
def rising(y,m):
    return s.prod(y+j for j in range(m))/s.factorial(m)
def block(z,ell,H):
    q,h=divmod(ell,H)
    return s.expand(rising(z,H)**q*rising(z,h))

def check():
    # K=Q, alpha=(2,3), N=1, A=(1,2), L=6, eta=2.
    # All nineteen points satisfy |u.lambda|<=3 by rational intervals.
    logs=[Interval(2).log(),Interval(3).log()]
    support=[u for u in product(range(-3,4),range(-1,2))
             if u not in [(-3,-1),(3,1)]]
    assert len(support)==19
    for a,b in support:
        val=a*logs[0]+b*logs[1]
        assert max(abs(val.lo),abs(val.hi))<3
    for a,b in [(-3,-1),(3,1)]:
        val=a*logs[0]+b*logs[1]
        assert val.lo>3 or val.hi< -3
    # rho=9 and this explicit coset contains nineteen points.
    assert s.Rational(1,2)*36/2==9
    H=2;c=2;d=2;L0=2;M0=2
    columns=[(ell,u) for ell in range(L0+1) for u in support]
    derivatives=[(m0,m1) for m0 in range(M0+1)
                  for m1 in range(M0+1-m0)]
    rows=[(x,m) for x in [-1,0,1] for m in derivatives]
    old=[];new=[]
    for x,(m0,m1) in rows:
        ordinary=[];normalized=[]
        for ell,(a,b) in columns:
            chi=a-b
            exponential=(s.Rational(2)**a*s.Rational(3)**b)**x
            derivative=s.diff(block(c*z,ell,H),z,m0).subs(z,x)
            ordinary.append(derivative*chi**m1*exponential)
            factor=s.Rational(d**m0,s.factorial(m0)*c**m0)
            polynomial=s.cancel(factor*derivative)
            assert polynomial.q==1
            differential=rising(chi,m1)
            assert differential.q==1
            normalized.append(polynomial*differential*exponential)
        old.append(ordinary);new.append(normalized)
    old=s.Matrix(old);new=s.Matrix(new)
    assert old.rank()==new.rank()==18
    assert old.col_join(new).rank()==18
    witness=new.nullspace()[0]
    common=lcm(*(int(v.q) for v in witness))
    integer=[int(v*common) for v in witness]
    divisor=reduce(gcd,integer)
    integer=[v//divisor for v in integer]
    witness=s.Matrix(integer)
    assert any(integer)
    assert new*witness==s.zeros(18,1)
    assert old*witness==s.zeros(18,1)
    blocks={}
    for coefficient,(ell,u) in zip(integer,columns):
        if coefficient:
            blocks[u]=blocks.get(u,0)+coefficient*block(c*z,ell,H)
    assert any(s.expand(poly)!=0 for poly in blocks.values())
    # The all-dimension proof reduces the hard-case endpoint to n=2,kappa=1.
    endpoint= s.Rational(297,100)*387072*(E**3)/s.Rational(31,5)
    threshold=exp_interval(s.Rational(35,2))/s.Rational(37,2)
    margin=endpoint-threshold
    assert margin.lo>0
    assert (2*E/s.Rational(31,10)).lo>1
    assert (4*E/s.Rational(31,10)).lo>3
    from laurent_constant import PI
    assert ((2*PI).sqrt()*exp_interval(F(1,24))).hi<3
    assert Interval(500).log().lo>F(31,5)
    assert (Interval(F(40,31)).log()+2).lo>F(9,4)
    assert Interval(25).log().hi<F(33,10)
    fixed=4*F(41,20)*F(27,8)*exp_interval(F(253,100))/(2*PI).sqrt()
    assert fixed.hi<exp_interval(F(51,10)).lo
    assert Interval(2).log().hi<F(7,10)
    assert (E/(E-1)).log().hi<1
    assert Interval(2).log().hi<F(1,20)*(F(44,5)+7)
    endpoint_eta,endpoint_xi=constants(2,1)
    assert 9*24<endpoint_xi.lo/F(500)
    endpoint_zeta=F(31,10)**2*2
    assert 8*endpoint_zeta<2*endpoint_xi.lo/F(1000)
    ratios=0
    coefficient_margins=0
    for n in range(2,51):
        for kappa in [1,2]:
            eta,xi=constants(n,kappa)
            zeta=F(31,10)**n*F(n**kappa,kappa)
            previous=F(31,10)**(n-1)*F((n-1)**kappa,kappa)
            assert xi.lo>16*n*(s.Rational(n)+s.Rational(21,10))*zeta
            assert xi.lo>16*s.Rational(31,10)*n*(s.Rational(n)+s.Rational(21,10))*previous
            # xi/(c1*zeta_previous)>60, with c1<2.001(n+1).
            assert xi.lo>60*s.Rational(2001,1000)*(n+1)*previous
            assert 2*xi.lo>s.Rational(2001,1000)*(n+1)*zeta
            ratios+=1
            eps0=Interval(F(3*n**3,1)/xi.hi,F(3*n**3,1)/xi.lo)
            eps1=Interval(zeta/(2*xi.hi),zeta/(2*xi.lo))
            assert ((n+1)**2*eps0).hi<F(1,500)
            assert (n**3*eps1).hi<F(1,1000)
            W=F(37,2)
            beta=F(3,8*(n+1))/W
            powers=(1+eps0)**(n+1)*(1+n*eps1)**n
            actual_margin=(n+F(21,10))*(1-2*eps1)-powers*(1+beta)*(n+2+F(11,10)*n*eps1+n*beta)
            assert actual_margin.lo>F(1,20)
            assert ((n+2)*eps1).hi<F(1,40)/(n+F(21,10))
            coefficient_margins+=1
    # The denominator/scaling identity for all polynomial rows.
    identities=0
    for c,H,ell,m,x in product([1,2,8],[1,2,5],range(9),range(5),[-3,-1,0,2]):
        dh=lcm(*range(1,H+1))
        left=s.cancel(s.Rational(dh**m,s.factorial(m)*c**m)*
                      s.diff(block(c*z,ell,H),z,m).subs(z,x))
        right=s.cancel(s.Rational(dh**m,s.factorial(m))*
                       s.diff(block(z,ell,H),z,m).subs(z,c*x))
        assert left==right
        assert left.q==1
        identities+=1
    return {"status":"passed","support_points":19,"clipped_volume_lower_bound":9,
            "initial_equations":18,"coefficient_columns":57,"ordinary_rank":18,
            "normalized_rank":18,"joint_row_rank":18,
            "primitive_integer_witness_nonzero_entries":sum(v!=0 for v in integer),
            "witness_max_absolute_coefficient":max(map(abs,integer)),
            "witness_nonzero_blocks":len(blocks),
            "chain_rule_integrality_cases":identities,
            "hard_case_threshold_margin_interval":[str(margin.lo),str(margin.hi)],
            "hard_case_threshold_margin_approximation":float(margin.lo),
            "differential_budget_ratio_cases":ratios,
            "initial_coefficient_margin_cases":coefficient_margins,
            "witness":[{"coefficient":v,"ell":ell,"exponent":list(u)}
                       for v,(ell,u) in zip(integer,columns) if v],
            "scope":"Exact basis, jet and parameter examples supplement the all-parameter initial-function proof (8.96–8.108)."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))

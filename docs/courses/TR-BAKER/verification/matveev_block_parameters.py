"""Outward rational checks for the alternative block length and dyadic counts."""
from fractions import Fraction as F
from math import factorial
import json
from laurent_constant import Interval,E,PI,LN2

def exp_interval(x):
    x=Interval.of(x)
    k=x.lo.__floor__()
    assert k>=0
    return E**k*(x-k).exp()

def ceil_interval(x):
    a=x.lo.__ceil__();b=x.hi.__ceil__()
    assert a==b,("rounding not decided",a,b)
    return a

def constants(n,kappa):
    eta=exp_interval(Interval(1)+Interval(F(n,1)+F(53,100))/kappa)
    xi=F(8,factorial(n))*(F(n)+F(21,10))*(2*(n+1))**(n+1)*(n*eta/2)**kappa
    return eta,xi

def check():
    assert Interval(F(353,100)).exp().lo>34
    assert (E**3).hi<21
    assert (E**2).lo>7
    assert Interval(3).log().hi<F(11,10)
    assert Interval(4).log().hi<F(7,5)
    margin=(E**7 -
            F(1001,1000)*F(51,5)*F(3,2)*27*F(41,20)*
            Interval(F(53,50)).exp()/(2*PI).sqrt())
    assert margin.lo>0
    assert 8*F(5001,5000)*F(251,200)+F(2,15)<F(51,5)
    dimensions=0
    for n in range(2,41):
        e1,x1=constants(n,1);e2,x2=constants(n,2)
        assert x1.lo>15000*n**3
        assert x2.lo>15000*n**3
        # Clear the large positive denominator before comparing; otherwise
        # absolute128-bit reciprocal rounding loses all relative precision.
        assert x2.lo>x1.hi
        assert (x2*e2).hi<(x1*e1).lo
        dimensions+=1
    rounding=0
    for t in [F(35,2),F(18),F(20),F(100),F(10000)]+[
            F(10,9)*(k+F(1,2)) for k in range(16,101)]:
        H=(F(9,10)*t).__floor__()
        assert H>=15
        assert (t+1)/H<F(251,200)
        assert H*Interval(3).log().hi<t
        rounding+=1
    growth=0
    for n in [2,5,9]:
      for kappa in [1,2]:
        eta,xi=constants(n,kappa)
        eps=3*n**3/xi
        c1=2*(n+1)*(1+eps)
        for D in [1,19]:
          ell=(E*D).log()
          for N in [1,8]:
            arg=F(1,2)*n*n*xi*N*D*ell/(E**3)
            S=ceil_interval(arg.log()/LN2)
            C0=F(22,5)*n+7+F(11,2)*Interval(n).log()+Interval(N).log()+2*Interval(D).log()+ell.log()
            max_growth=exp_interval(C0)
            for t in [F(35,2),F(100)]:
              W0=t+1;H=(F(9,10)*t).__floor__()
              for L in [F(1),F(500)]:
                G=c1*L*W0
                for s in sorted(set([0,S//2,S])):
                  T=(L/2**s).__floor__()
                  X=ceil_interval(2*D*G/(T+1))
                  for nu in [0,n]:
                    count=(2*X+1 if s==0 else 2*X) if nu==0 else 2**(nu+1)*X+1
                    Z=count*(T+1)
                    assert Interval(Z).lo>=(2**(nu+2)*D*G).hi
                    assert Interval(Z).hi<=(2**nu*(4*D*G+3*T+3)).lo
                    R=2**s*eta*Z/L;K=2**(S-s)
                    actual=E*(1+K*(R+1)/H)
                    assert actual.hi<max_growth.lo
                    growth+=1
    counts=0
    for n in [1,2,9]:
      for eps in [F(0),F(1,10000),F(2)]:
        for L in [F(1),F(3,2),F(17),F(10000)]:
          c=2*(n+1)*(1+eps);A=c*L;M0=A.__floor__();past=0
          for s in range(26):
            T=(L/2**s).__floor__()
            Msn=M0-(n+1)*(past+T)+T
            assert Msn>=eps*A/(1+eps)
            for DG in [F(1,100),F(1),F(17,3),F(10000)]:
              X=(2*DG/(T+1)).__ceil__()
              for nu in range(n+1):
                count=(2*X+1 if s==0 else 2*X) if nu==0 else 2**(nu+1)*X+1
                Z=count*(T+1)
                assert 2**(nu+2)*DG<=Z<=2**nu*(4*DG+3*T+3)
                counts+=1
            past+=T
    return {"status":"passed","fixed_constant_margin_rational_interval":[str(margin.lo),str(margin.hi)],
            "fixed_constant_margin_approximation":float(margin.lo),
            "dimension_cases":dimensions,"block_rounding_cases":rounding,
            "full_growth_examples":growth,"exact_dyadic_count_cases":counts,
            "scope":"Finite examples supplement the all-dimensional block and dyadic proofs (8.90–8.95)."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))

"""Exact checks for Lesson 7's rounded boxes and uniform occupancy proof.

GPT-6.1 Sol (OpenAI), Ultra; October 2026. CC0.
The family adapts N. Gouillon's rounded construction (2003), thesis §§5.1,5.3.2.
The lesson supplies the uniform proof, including the residual rounding terms.
All roots, integer parts and strict margins use integers/rational intervals.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval, decimal_out

g=F(241,1000)
gamma=F(1309,1000)
def power(q,n):
    return (Interval.of(q).log()/n).exp()

rho=power(g/(2*gamma),3)
assert rho.hi<F(452,1000)
assert (rho/3).hi<F(151,1000)
Tcoef=power(2*gamma/g,3)**2/F(765)
Tcoef*=power(F(2701,2700),3)
assert Tcoef.hi<F(642,100000)
small=power(2*gamma/g,3)**2/F(9)*(F(1,1350)+F(1,2700))
assert small.hi<F(7,10000)
C=power(3,3)+1/power(1350,3)
ends={}
for c in (300,5000):
    r=power(c,6)
    value=2*(C+F(452,1000)/r+F(151,1000)/(r**4))**2*(C+F(642,100000)*(r**2))
    assert value.hi<F(1153,125)<F(250,27)
    ends[str(c)]=[decimal_out(value.lo,10),decimal_out(value.hi,10,up=True)]
TKL=F(1,1350)+rho**2/power(300,3)*F(2701,2700)*F(1351,1350)*C
assert TKL.hi<F(1,20)
ln3=Interval(3).log()
assert (F(3*946,20*1000)/ln3).hi<F(1,7)
assert (F(60,2700)/ln3).hi<1
length=F(2701,2700)*(1/power(300,2)+power(2*gamma/(g*300),3)*C)
factorial=F(6,2700)*Interval(1351).log()
coefficient=Interval(F(283,1000)).log()+F(11,3)+ln3+F(161,10000)+Interval(F(1,20)).log()
assert length.hi<F(566,1000)
assert factorial.hi<F(161,10000)
assert coefficient.hi<F(524,1000)

def floor_root(value,n):
    """The exact integer floor of a positive rational nth root."""
    value=F(value)
    assert value>=0
    low,high=0,1
    while high**n*value.denominator<=value.numerator:high*=2
    while high-low>1:
        mid=(low+high)//2
        if mid**n*value.denominator<=value.numerator:low=mid
        else:high=mid
    assert low**n<=value<(low+1)**n
    return low

floor=lambda value:value.numerator//value.denominator
cases=0
branches={'half_K':0,'L':0}
for lam in [F(1),F(7,5),F(2),F(1000)]:
 for D in [1,2,10]:
  for Q in [lam/D,max(F(5),lam/D)]:
   for p1,p2 in [(1,1),(1,100),(100,1)]:
    a1,a2=3*lam*p1,3*lam*p2
    A=a1*a2
    for c0 in [300,5000]:
     for hfactor in [1,100]:
      h=max(265*lam/D,150*Q)*hfactor
      c1=F(51,10)
      k=c0*A*D*Q/lam**3
      K,L=floor(k),floor(c1*D*h/lam)
      assert K>=2700 and L>=1351
      G=min(F(K+1,2),F(L+1))
      branches['half_K' if G==F(K+1,2) else 'L']+=1
      y6=F((K+1)**4)*(2*gamma*D*Q)**2/(g*g*A)
      r6=y6*(a2/a1)**3
      s6=y6*(a1/a2)**3
      Rj=[floor_root((K+1)*a2/a1,2),floor_root(r6/(G*G),6),floor_root(9*r6,6)]
      Sj=[floor_root((K+1)*a1/a2,2),floor_root(s6/(G*G),6),floor_root(9*s6,6)]
      z3=g*g*(L+1)**3*A*(K+1)**2/(2*gamma*D*Q)**2
      Tj=[max((L+1)//(K+1),K),floor_root(z3/G,3),floor_root(3*z3,3)]
      card=[(r+1)*(s+1) for r,s in zip(Rj,Sj)]
      checks=[(Tj[0],K),(card[0],K+1),((Tj[0]+1)*card[0],L+1),
              ((Tj[1]+1)*card[1],2*K*L+1),((Tj[1]+1)*card[1],K*K+1),
              ((Tj[2]+1)*card[2],3*K*K*L+1)]
      assert all(left>=right for left,right in checks)
      R,S,T=sum(Rj),sum(Sj),sum(Tj)
      assert F(R,K)<F(566,1000)*lam/a1
      assert F(S,K)<F(566,1000)*lam/a2
      N=(K+1)*(K+2)*(L+1)//2
      q=(R+1)*(S+1)
      ratio=F(q*(T+1),N)
      assert 1<ratio<F(1153,125)
      assert F(T,K*L)<F(1,20)
      omega=1-F(N,2*q*(T+1))
      omega0=2*ratio
      assert F(1,4)-F(1,12)/ratio<g
      assert omega<F(946,1000) and omega0<20
      U=omega*T+omega0
      bvalue=U/(1+K*ln3/3)
      low,high=floor(bvalue.lo),floor(bvalue.hi)
      assert low==high
      b=low+1
      assert 1<=b<L
      cases+=1
assert cases==288 and all(branches.values())
print(json.dumps({'status':'passed','rounded_parameter_cases':cases,
                 'Gamma_branches':branches,'endpoint_intervals':ends,
                 'TKL_majorant':[decimal_out(TKL.lo,10),decimal_out(TKL.hi,10,up=True)],
                 'length_majorant':[decimal_out(length.lo,12),decimal_out(length.hi,12,up=True)],
                 'factorial_majorant':[decimal_out(factorial.lo,12),decimal_out(factorial.hi,12,up=True)],
                 'coefficient_bracket_constant':[decimal_out(coefficient.lo,12),decimal_out(coefficient.hi,12,up=True)],
                 'arithmetic':'integers,Fraction,128-bit outward intervals',
                 'scope':'Finite cases supplement the written uniform proof. Counts assume the stated injectivity hypotheses; no algebraic bases or complete numerical lower-bound corollaries are certified by these samples.'},indent=2))

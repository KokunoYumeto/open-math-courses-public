"""Exact finite regressions plus separately labelled 70-digit diagnostics.

The general claims are proved in the lesson. These finite checks are not a
formal proof, nor a verification of the complete first-passage theorem.
"""
from fractions import Fraction as F
from math import comb, floor, ceil
import json
import mpmath as mp

mp.mp.dps=70
counts=dict(multiplicity_prefixes=0,exact_profile_families=0,time_ratios=0,
            exact_variation_bounds=0,local_log_diagnostics=0,analytic_diagnostics=0)
def p(n,k):return F(comb(k-1,n-1),2**k) if k>=n else F(0)
def d(A,D,n):return floor(A-D*n)+1
def mf(q):return mp.mpf(q.numerator)/q.denominator if isinstance(q,F) else mp.mpf(q)
for D in [F(1,4),F(2,5),F(1,2),F(2,3),F(3,4)]:
 for shift in [F(0),F(1,7),F(1,2),F(6,7)]:
  A=D*120+shift
  for W in [F(2),F(3),F(9,2),F(6),F(8)]:
   R=ceil(W)-1;n=floor((A-R)/D)+1;m=floor((A+R+1)/D)
   assert n>=8*W
   carrier=[v for v in range(1,m+8) if abs(d(A,D,v))<W]
   assert carrier==list(range(n,m+1))
   pref=F(0)
   for level in range(-R,R+1):
    fibres=[v for v in carrier if d(A,D,v)==level]
    mult=floor((A-level+1)/D)-floor((A-level)/D)
    assert len(fibres)==mult
    assert all((A-level)/D<v<=(A-level+1)/D for v in fibres)
    pref+=mult-1/D
    assert abs(pref)<=1
    counts['multiplicity_prefixes']+=1
   q=[p(v,2*v+d(A,D,v)) for v in carrier]
   Z=sum(q,F(0));V=q[0]+q[-1]+sum(abs(b-a) for a,b in zip(q,q[1:]))
   kap=max(W/(2*n),(W*W+W+2*n)/(4*n*(n-W+1)))
   assert kap<=W/n
   residual=max(F(0),V-kap*Z)
   assert residual*residual*(3*n-2)<=1
   counts['exact_variation_bounds']+=1
   for v,qa,qb in zip(carrier,q,q[1:]):
    L=2*v+d(A,D,v);Ln=2*(v+1)+d(A,D,v+1)
    ratio=F(L,2*v) if Ln-L==1 else F(L*(L+1),4*v*(L+1-v))
    assert Ln-L in [1,2] and qb==ratio*qa and abs(ratio-1)<=kap
    counts['time_ratios']+=1
   counts['exact_profile_families']+=1
for n in range(1,100):
 for k in range(n,3*n+1):
  assert p(n+1,k+1)==p(n,k)*F(k,2*n)
  assert p(n+1,k+2)==p(n,k)*F(k*(k+1),4*n*(k+1-n))
  counts['time_ratios']+=2
for n in [8,17,40,80,128]:
 for dev in range(-(n//2),n//2+1):
  pv=mf(p(n,2*n+dev))
  err=abs(mp.log(pv)+mp.log(4*mp.pi*n)/2+mp.mpf(dev)**2/(4*n))
  bound=mp.mpf(2)/n+mp.mpf(2*abs(dev))/n+mp.mpf(abs(dev)**3)/(n*n)
  assert err<=bound
  counts['local_log_diagnostics']+=1
diagnostics=[]
for S,C in [(512,mp.mpf('0.25')),(2048,mp.mpf('0.5')),(8192,mp.mpf(1)),(8192,mp.mpf(2))]:
 D=2-mp.log(3)/mp.log(2);A=D*S;W=C*mp.sqrt(S*mp.log(S));R=int(mp.ceil(W))-1
 n=int(mp.floor((A-R)/D))+1;m=int(mp.floor((A+R+1)/D));T=(R+1)/D
 assert 1<W<=mp.mpf(n)/8
 def phi(v):return mp.exp(-mp.mpf(v)**2/(4*S))/mp.sqrt(4*mp.pi*S)
 Q=(2+1/D)*phi(0)+4*S/(D*R)*phi(R)
 eta=mp.mpf(2+2*R)/n+mp.mpf(R)**3/n**2+T/(2*n)+mp.mpf(R)**2*T/(4*n*S)
 eps=mp.expm1(eta);H=mp.mpf(0);Z=mp.mpf(0);dist=mp.mpf(0)
 for v in range(n,m+1):
  dev=int(mp.floor(A-D*v))+1;k=2*v+dev
  q=mp.exp(mp.loggamma(k)-mp.loggamma(v)-mp.loggamma(k-v+1)-k*mp.log(2))
  g=phi(dev);H+=g;Z+=q;dist+=abs(q-g)
  assert abs(mp.log(q/g))<=eta
 assert abs(H-1/D)<=Q and dist<=eps*H
 M=eps*(1/D+Q)+Q
 assert abs(Z-1/D)<=M
 diagnostics.append(dict(S=S,C=str(C),n=n,m=m,mass=str(Z),target=str(1/D),
                         mass_error=str(abs(Z-1/D)),proved_upper_bound=str(M),eta=str(eta)))
 counts['analytic_diagnostics']+=1
# Exact examples, including the rational-slope strict-gate counterexample.
assert [sum(d(F(40),F(2,5),v)==z for v in range(96,108)) for z in range(-2,3)]==[2,3,2,3,2]
assert p(41,81)/p(40,80)==1 and p(41,82)/p(40,80)==F(81,82)
for A in range(1,10):
 for v in range(1,30):
  phase=F(A)+F(3,2)*v-floor(F(A)+F(3,2)*v)
  assert phase in [0,F(1,2)] and not phase>F(1,2)
print(json.dumps(dict(passed=True,counts=counts,numerical_precision_digits=70,
    numerical_scope='Gaussian/logarithmic estimates and log-gamma sums are high-precision diagnostics, not exact certificates.',
    exact_scope='Rational cutoffs, carriers, multiplicities, cumulative errors, factorial ratios and squared variation bounds.',
    diagnostic_cases=diagnostics),indent=2))

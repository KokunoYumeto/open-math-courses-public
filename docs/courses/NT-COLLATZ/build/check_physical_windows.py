"""Finite exact regressions; separate high-precision schedule diagnostics."""
from fractions import Fraction as F
from math import floor,ceil,comb
import json
from pathlib import Path
import mpmath as mp
counts=dict(log_certificates=0,scalar_inequalities=0,support_cases=0,translated_indices=0,sampling_intervals=0,numerical_schedule_cases=0)
def log_interval(x,n):
 u=(x-1)/(x+1)
 s=2*sum((u**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
 e=2*u**(2*n+1)/(F(2*n+1)*(1-u*u))
 return s,s+e
el,eu=log_interval(F(2),12);dl,du=log_interval(F(4,3),6)
assert F('.693147')<el<eu<F('.6931471808')
assert F('.287682')<dl<du<F('.2876821')
counts['log_certificates']=2
alpha=F(1001,1000)
inequalities=[
 F('.001')/du>F('.003476'),
 (alpha**3-1)/dl<F('.010439'),
 1/(10*eu)>F('.14426'),1/(10*el)<F('.14427'),
 eu/dl<F('2.41'),(F(4,25)+eu)/dl<F(3707,1250),
 (3-F(3707,1250))*71>F('2.41'),
 (F('.14426')-F('13.74')*F('.010495'))*300000>F('14.74'),
 F('42.44')*F('.0034')>F('.14427'),
 F('.000022')<F('.0034')/8,
 F('.003476')-F('.00001')-F(4,25)*F('.000022')/dl>F('.00345'),
 F('.010439')-F('.00001')+F(4,25)*F('.000022')/dl<F('.010442'),
 F('.00345')>F('.14427')/43,
 (F('.14426')/13-F('.010442'))*300000>1+F(1,13),
 F(4,3)<2*el,16/eu**3>48,
 F(5097587,77645938)<F(1,2),
 F('.010495')+F(1,300000)<F('.0105')]
assert all(inequalities)
counts['scalar_inequalities']=len(inequalities)
def support(A,delta,W,i):
 R=ceil(W)-1
 lo=floor((A+i-R)/delta)+1;hi=floor((A+i+R+1)/delta)
 return list(range(max(1,lo),hi+1))
def p(n,k):
 return F(comb(k-1,n-1),2**k) if k>=n else F(0)
for delta in [F(2,5),F(1,2),F(3,4)]:
 for A in [F(20),F(81,4),F(101,3)]:
  for h in [0,7,11]:
   for W in [F(3),F(9,2),F(5)]:
    for tau in [F(-1),F(0),F(1)]:
     beta=F(3,2);d=delta;t0=A/delta+h+tau/d
     Wpad=(abs(tau)/d+(W+1)/delta)/3
     V=list(range(max(1,ceil(t0-3*Wpad)-h),floor(t0+beta/d+3*Wpad)-h+1))
     I=[support(A,delta,W,i) for i in [0,1]]
     R=ceil(W)-1
     union=list(range(max(1,floor((A-R)/delta)+1),floor((A+R+2)/delta)+1))
     assert sorted(set(I[0])|set(I[1]))==union
     for i in [0,1]:
      for nu in range(1,floor((A+R+3)/delta)+3):
       level=floor(A+(2-delta)*nu)+1
       assert (nu in I[i])==(abs(level+i-2*nu)<W)
      assert set(I[i])<=set(V)
      for nu in I[i]:
       n=nu+h;assert n-h==nu
       assert t0-3*Wpad<=n<=t0+beta/d+3*Wpad
       counts['translated_indices']+=1
      full=sum((p(nu,floor(A+(2-delta)*nu)+1+i) for nu in I[i]),F(0))
      restricted=sum((p(nu,floor(A+(2-delta)*nu)+1+i) for nu in V if nu in I[i]),F(0))
      assert full==restricted
     counts['support_cases']+=1
for z in [F(k,4) for k in range(4,121)]:
 for length in [F(1,4),F(1),F(7,2),F(8)]:
  v=z+length
  odds=[n for n in range(1,ceil(v)+1,2) if z<n<v]
  D=ceil((v-1)/2)-floor((z-1)/2)-1
  assert D==len(odds)
  assert abs(D-length/2)<=1
  H=sum((F(1,n) for n in odds),F(0))
  # Exact interval certificate for log(v/z), no floating logarithm.
  ll,uu=log_interval(v/z,60)
  assert uu/2-H<=1/z and H-ll/2<=1/z
  counts['sampling_intervals']+=1
assert support(F(40),F(2,5),F(5),0)==list(range(91,113))
assert support(F(40),F(2,5),F(5),1)==list(range(93,116))
assert sum((F(1,n) for n in [7,9,11]),F(0))==F(239,693)
mp.mp.dps=80
ell=mp.log(2);d=mp.log(mp.mpf(4)/3);delta=d/ell;alpha=mp.mpf(1001)/1000
diagnostics=[]
for L,C in [(mp.mpf(10)**10,mp.mpf('.5')),(mp.mpf(10)**10,mp.mpf(1)),(mp.mpf(10)**11,mp.mpf(2))]:
 N=int(mp.floor(L/(10*ell)));h=int(mp.floor(L/100000));W=C*mp.sqrt(N*mp.log(N))
 assert 3*W<=mp.mpf(33)/500000*L and W>=142
 for a in [alpha,alpha**2]:
  K=int(mp.floor((alpha-1)*a*L));beta=(alpha-1)*a*L/K
  assert ell<beta<2*ell
  for j in [0,K//2,K-1]:
   t0=((a-1)*L+j*beta)/d
   vmin=int(mp.ceil(t0-3*W))-h
   vmax=int(mp.floor(t0+beta/d+3*W))-h
   assert mp.mpf('.0034')*L<=vmin<=vmax<=mp.mpf('.0105')*L
   assert mp.mpf('13.74')<=mp.mpf(N)/vmax<=mp.mpf(N)/vmin<=mp.mpf('42.44')
   for sign in [-1,0,1]:
    tau=sign*mp.mpf(4)/25*W;S=t0-h-tau/d;A=delta*S;R=int(mp.ceil(W))-1
    assert mp.mpf(N)/43<=S<=mp.mpf(N)/13
    for i in [0,1]:
     lower=int(mp.floor((A+i-R)/delta))+1
     upper=int(mp.floor((A+i+R+1)/delta))
     assert vmin<=lower<=upper<=vmax
     assert W<=mp.mpf(lower)/8
    counts['numerical_schedule_cases']+=1
 diagnostics.append(dict(log_B=str(L),C=str(C),N=N,h=h,W=mp.nstr(W,20)))
print(json.dumps(dict(passed=True,scope='Exact rational finite regressions and separate80-digit diagnostics; no infinite proof or Lean certification',counts=counts,logarithm_certificates=[dict(x='2',terms=12,lower=str(el),upper=str(eu)),dict(x='4/3',terms=6,lower=str(dl),upper=str(du))],numerical_diagnostics=diagnostics),indent=2))

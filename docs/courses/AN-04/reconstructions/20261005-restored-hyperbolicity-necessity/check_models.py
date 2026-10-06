"""Retained full-operator finite diagnostics and a new circle-count check; no general proof certification."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
y,ss,tt,h=s.symbols('y ss tt h',real=True)
phase=s.I*y*y+2*(ss+s.I*tt)+s.I*(ss+s.I*tt)**2
L=lambda f:s.expand(-s.diff(f,ss)-s.I*s.diff(f,tt))
assert L(phase)==0
assert s.simplify(s.im(phase)-(y*y+ss*ss+tt*tt)-2*tt*(1-tt))==0
aa=s.expand(s.diff(phase,tt)+s.I*s.diff(phase,ss));assert L(aa)==0
assert aa.subs({y:0,ss:0,tt:0})==4*s.I
checks.append({'name':'Exact phase, differentiated quotient and positive-side damping','passed':True,
 'scope':'Polynomial phase in three variables; L sign, a(0), La and exact imaginary-part remainder.'})
def covD(f,var):return s.expand(-s.I*s.diff(f,var)+s.diff(phase,var)*f/h)
cases=[]
for iy in range(3):
 for iss in range(3):
  for itt in range(3):
   f=y**iy*ss**iss*tt**itt
   value=h**9*(h**-8*(covD(covD(f,ss),ss)+covD(covD(f,tt),tt))
     +h**-6*(1+h*h*y)*covD(covD(f,ss),y)
     +h**-4*((3-2*s.I)*covD(f,tt)-s.I*covD(f,ss))+(1+h*h*y)*f)
   value=s.expand(value)
   assert all(term.as_powers_dict().get(h,0)>=0 for term in value.as_ordered_terms())
   assert s.expand(value.subs(h,0)-aa*L(f))==0
   cases.append([iy,iss,itt])
checks.append({'name':'Full anisotropic formal adjoint and smooth normalized operator','passed':True,
 'cases':cases,'scope':'Exercise5 operator with c=3+2i, b=1+x1; includes -iDs adjoint coefficient derivative, all full lower terms and27 independent amplitude monomials.'})
q1,q2,qt=s.symbols('q1 q2 qt',real=True)
def cd(f,var):return s.expand(-s.I*s.diff(f,var)+(s.I/h if var==qt else 0)*f)
for i in range(3):
 for j in range(3):
  for k in range(3):
   f=q1**i*q2**j*qt**k
   actual=s.expand(h*(cd(cd(cd(f,qt),q1),q1)+cd(cd(cd(f,q2),q2),q2)))
   expected=s.I*(-s.diff(f,q1,2))+h*(s.I*s.diff(f,q1,2,qt)+s.I*s.diff(f,q2,3))
   assert s.expand(actual-expected)==0
checks.append({'name':'Full constant cone transport with its normal phase factor','passed':True,
 'scope':'Exercise12,27 amplitude monomials; exact R_h=iD1^2+h(D1^2Dt+D2^3), not just a leading symbol.'})
E=-s.Heaviside(q1)*s.Heaviside(q2)
assert -s.diff(E,q1,q2)==s.DiracDelta(q1)*s.DiracDelta(q2)
checks.append({'name':'Nonelliptic tangential fundamental solution','passed':True,
 'scope':'Distributional differentiation for D1D2 and E=-H1H2; smooth convolution transfer is proved in the lesson.'})
B,R,ex=s.symbols('B R ex',positive=True);normal=B*R+ex
assert s.simplify(normal**2-B**2/(1+B**2)*(normal**2+R**2)-ex*(2*B*R+ex)/(1+B**2))==0
checks.append({'name':'Exact positive-cone damping constant','passed':True,
 'scope':'Nonnegative remainder for t>=B|yprime| with B>0; the B=0 counterexample is proved separately.'})
ws,wt,wy=s.symbols('ws wt wy',real=True)
scaled=s.expand(phase.subs({y:h*wy,ss:h*ws,tt:h*wt})/h)
assert s.limit(scaled,h,0)==2*(ws+s.I*wt)
assert s.expand(-s.I*s.conjugate(2*(ws+s.I*wt)))==-2*s.I*ws-2*wt
checks.append({'name':'Hermitian concentrated-pairing signs','passed':True,
 'scope':'Full rescaled polynomial phase, including quadratic terms; the chosen source phase cancels the test conjugate.'})
budget_cases=[]
for n,m,r,nu,N in [(3,2,1,2,2),(2,1,1,2,0),(5,4,3,4,5),(4,3,2,3,3),(7,6,6,7,4)]:
 for cone in [False,True]:
  A0=(m*nu if cone else 2*m*nu)+m-r
  loss=nu*(n+2*N) if cone else nu*(n+2+4*N)
  M=loss+n+N+1;J=A0+N+M
  assert J+1-A0-N==M+1 and M-loss-n-N==1 and nu-r>0
  budget_cases.append({'cone':cone,'n':n,'m':m,'r':r,'nu':nu,'N':N,'A0':A0,'loss':loss,'M':M,'J':J})
checks.append({'name':'Finite derivative and truncation budgets','passed':True,'cases':budget_cases,
 'scope':'Ten concrete order/geometry budgets; the general finite Taylor proof is written separately.'})
w=s.symbols('w',real=True);root_cases=[]
for k in range(2,13):
 for sign in [-1,1]:
  count=int(s.Poly(w**k+sign,w).count_roots(-s.oo,s.oo))
  assert (count==k)==(k==2 and sign==-1)
  root_cases.append({'k':k,'sign':sign,'real_roots':count})
checks.append({'name':'One-sided and two-sided binomial alternatives','passed':True,'cases':root_cases,
 'scope':'Exact counts k=2..12; arbitrary-k root persistence and real-root count are proved in Lemma7.2.'})
t,x,tau,eta=s.symbols('t x tau eta',real=True)
def H(poly,f):return s.expand(s.diff(poly,tau)*s.diff(f,t)+s.diff(poly,eta)*s.diff(f,x)-s.diff(poly,t)*s.diff(f,tau)-s.diff(poly,x)*s.diff(f,eta))
poly=tau**2-t*eta**2
assert H(poly,H(poly,t))==2*eta**2
assert H(s.I*poly,H(s.I*poly,t))==-2*eta**2
cp=(1+t+x)*poly
assert s.expand(H(cp,H(cp,t)).subs({t:0,tau:0})-2*(1+x)**2*eta**2)==0
quartic=tau**4-t*eta**4;squared=poly**2
assert H(quartic,H(quartic,t)).subs({t:0,tau:0})==0
assert all(s.diff(squared,v).subs({t:0,tau:0})==0 for v in [t,x,tau,eta])
checks.append({'name':'Complete Hamilton derivatives and hypothesis guards','passed':True,
 'scope':'Positive double-root model, complex sign reversal, nonconstant real multiplier, quartic and genuine multiple-characteristic examples.'})

centers=np.array([-1+0j,.5+np.sqrt(3)*.5j,.5-np.sqrt(3)*.5j])
lower=s.Rational(1,5)*(s.sqrt(3)-s.Rational(1,5))**2
upper=s.Rational(1,20)*s.Rational(6,5)**4
assert s.simplify(lower-upper)>0
angles=np.linspace(0,2*np.pi,4096,endpoint=False)
cases=[]
for eps in np.linspace(0,.05,21):
 roots=np.roots([eps,1,0,0,1]) if eps else np.roots([1,0,0,1])
 for center in centers:
  assert np.count_nonzero(np.abs(roots-center)<.2)==1
  w=center+.2*np.exp(1j*angles)
  R=w**3+1+eps*w**4
  Rp=3*w**2+4*eps*w**3
  count=np.mean(Rp/R*(w-center))
  assert abs(count-1)<1e-10
  assert np.min(np.abs(R))>float(lower-upper)-1e-12
  cases.append({'epsilon':float(eps),'circle_center':[float(center.real),float(center.imag)],
                'count_real':float(count.real),'count_imag':float(count.imag)})
checks.append({'name':'Complete circle-homotopy example, including degree drop at epsilon zero',
 'passed':True,'cases':cases,'scope':'Exact uniform gap; numerical circle counts and polynomial zeros are supplementary diagnostics.'})
record={'passed':all(c['passed'] for c in checks),'finite_groups':len(checks),'checks':checks,
 'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},'script_sha256':sha(Path(__file__)),
 'retained_original_diagnostic_groups':9,'added_diagnostic_groups':1,
 'finite_checks_are_general_proof_certification':False,'full_course_complete':False,
 'human_review_complete':False,'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'passed':record['passed'],'finite_groups':len(checks),'full_original_solutions':20}))

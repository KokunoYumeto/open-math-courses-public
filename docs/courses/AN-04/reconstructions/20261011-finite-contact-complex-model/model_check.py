"""Exact sign, scaling and threshold checks; the proofs remain in the lesson. CC0."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
x,lam,t,s,d,a,q,eta,tau=S.symbols('x lam t s d a q eta tau',real=True)
checks=[]
def equal(name,left,right):
 assert S.simplify(left-right)==0,name
 checks.append(name)
for k in range(1,7):
 delta=S.Rational(1,k+1)
 equal(f'contact balance k={k}',1-k*delta,delta)
 equal(f'gain and loss k={k}',1-delta,S.Rational(k,k+1))
for k in [1,3,5]:
 w=S.exp(-x**(k+1)/S.Integer(k+1))
 equal(f'decaying opposite-sign mode k={k}',S.diff(w,x)+x**k*w,0)
 equal(f'good-sign residual k={k}',S.diff(w,x)-x**k*w,-2*x**k*w)
delta=S.symbols('delta',positive=True)
equal('full Fourier norm exponent',2*(a-delta-d/2)+delta+d/2,2*a-delta-d/2)
alpha=-s-S.Rational(1,2)+delta/2+d/4
equal('exact Sobolev threshold',2*alpha-delta-d/2+2*t,2*(t-s)-1)
equal('cubic example alpha',alpha.subs({s:2,delta:S.Rational(1,4),d:2}),-S.Rational(15,8))
equal('cubic order-two gain',2-1+S.Rational(1,4),S.Rational(5,4))
equal('cubic Sobolev integrand',2*(-S.Rational(15,8))-S.Rational(1,4)-1+2*t,2*t-5)
for k in [1,2,3,4]:
 ell=eta+S.I*x**k*tau
 equal(f'Hamilton normal derivative k={k}',S.diff(ell,eta),1)
 equal(f'Hamilton frequency derivative k={k}',-S.diff(ell,x),-S.I*k*x**(k-1)*tau)
equal('constant leading jet sign',-S.I*S.diff(S.exp(-S.I*q*x),x)+q*S.exp(-S.I*q*x),0)
equal('nearby cubic root', (x**3-a**3).subs(x,a),0)
equal('nearby simple derivative',S.diff(x**3-a**3,x).subs(x,a),3*a**2)
equal('central cubic derivative',S.diff(x**3,x,3),6)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(root/'finite-contact-complex-models-and-regularity.md'),'script_sha256':sha(Path(__file__)),'scope':'Exact finite identities only; full classical summation, compactness, microlocal bootstrapping and distributional wavefront proofs are in the lesson.'}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps(result))

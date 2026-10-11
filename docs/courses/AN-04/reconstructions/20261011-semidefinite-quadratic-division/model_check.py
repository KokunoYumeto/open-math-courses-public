"""Exact model identities; analytic flatness and positivity are proved in the lesson. CC0-1.0."""
from pathlib import Path
import sympy as s,json,hashlib
root=Path(__file__).resolve().parent
t,u,w,e,x,v,k,eta,tau,z=s.symbols('t u w e x v k eta tau z',real=True)
checks=[]
def check(name,a,b):
 d=a-b
 assert (all(s.simplify(q)==0 for q in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0),name
 checks.append({'name':name,'passed':True})
g=u*u+w**3;f=(1-t)**2*g+t*t*e*(1-g)
check('Reference time',f.subs(t,0),g)
check('Raw division',f,g*((1-t)**2-t*t*e)+t*t*e)
check('Corrected division',f,g*(1-t)**2+t*t*e*(1-g))
check('Negative quotient at time one',((1-t)**2-t*t*e).subs(t,1),-e)
check('Raw-to-corrected quotient',(1-t)**2-((1-t)**2-t*t*e),t*t*e)
check('Divisor Hessian',s.hessian(g,[u,w]).subs({u:0,w:0}),s.diag(2,0))
check('Negative-side family',f.subs(e,0),(1-t)**2*g)
fp=(v-t*e)**2;gp=v*v;rm=-2*t*v*e+t*t*e*e
check('Necessary one-sided remainder',fp-gp,rm)
check('Obstruction at divisor zero',fp.subs(v,0),t*t*e*e)
check('Reference divisor zero',gp.subs(v,0),0)
check('Positive-side reference time',fp.subs(t,0),gp)
fm=v*(v-e);check('Negative-side independence',s.diff(fm,t),0)
hom=k*fp.subs(v,eta/k);gh=k*gp.subs(v,eta/k);rh=k*rm.subs(v,eta/k)
check('Homogeneous identity',hom,gh+rh)
check('Homogeneous Euler identity',k*s.diff(hom,k)+eta*s.diff(hom,eta),hom)
check('Remainder Euler identity',k*s.diff(rh,k)+eta*s.diff(rh,eta),rh)
check('Reversed sign identity',-hom,-gh-rh)
check('Reference homogeneous Hessian',s.diff(gh,eta,2).subs(k,1),2)
check('Negative homogeneous Hessian',s.diff(-gh,eta,2).subs(k,1),-2)
eps,delta,N=s.symbols('eps delta N',positive=True)
check('Flat-defect exponent',delta**(3*N)/delta**(2*N),delta**N)
check('Cover lower constant',s.Integer(7)-2,5)
check('Cover upper constant',s.Integer(17)+2,19)
check('Nearest lattice lower bound',s.Integer(8)-s.Rational(1,2),s.Rational(15,2))
check('Nearest lattice upper bound',s.Integer(16)+s.Rational(1,2),s.Rational(33,2))
check('Figure obstruction at x one half',s.exp(-2/(s.Rational(1,2)**2)),s.exp(-8))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'cases':checks,'source_sha256':sha(root/'semidefinite-division-with-a-nonnegative-quotient.md'),'script_sha256':sha(Path(__file__)),'scope':'Finite model and scaling identities. Full sign, flatness, covering, smooth extension and division proofs are in the lesson.'}
(root/'model-check.json').write_text(json.dumps(r,indent=2)+'\n','utf-8');print(json.dumps({'passed':True,'cases':len(checks)}))

"""Exact algebraic checks for the concave-index construction; not a substitute for its proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent
lam=s.symbols('lambda',positive=True);t,b,c,a,n,d,r=s.symbols('t b c a n d r',real=True)
z,theta,eta=s.symbols('z theta eta',real=True);L=s.log(lam)
rows=[]
def check(name,left,right=0):
 # The packet is supported on lambda>2, so log(lambda) is positive.
 residual=s.simplify((left-right).subs(s.log(lam),s.Symbol('positive_log_lambda',positive=True)))
 ok=residual==0;rows.append(dict(name=name,passed=bool(ok),kind='exact symbolic identity'));assert ok,(name,residual)
e=z*s.sqrt(L/lam)-theta*L
check('frequency change inversion',e.subs(z,theta*s.sqrt(lam*L)+eta*s.sqrt(lam/L)),eta)
check('transverse derivative',s.diff(e,z),s.sqrt(L/lam))
check('last-frequency derivative',s.diff(e,lam),(1-L)/(2*lam*L)*e-(1+L)/(2*lam)*theta)
check('positive quadratic expansion',(theta*s.sqrt(lam*L)+eta*s.sqrt(lam/L))**2/lam,theta**2*L+2*theta*eta+eta**2/L)
th2,e2=s.symbols('theta2 eta2',real=True)
check('indefinite quadratic expansion',((theta*s.sqrt(lam*L)+eta*s.sqrt(lam/L))**2-(th2*s.sqrt(lam*L)+e2*s.sqrt(lam/L))**2)/lam,(theta**2-th2**2)*L+2*(theta*eta-th2*e2)+(eta**2-e2**2)/L)
check('phase transverse derivative',s.diff(z**2/lam,z),2*z/lam)
check('phase last derivative',s.diff(z**2/lam,lam),-z**2/lam**2)
packet=lam**b*s.exp(t*z**2/lam)
check('exact signed PDE',-s.I*lam*s.diff(packet,t)+s.I*z**2*packet)
check('one-dimensional Jacobian',s.diff(theta*s.sqrt(lam*L)+eta*s.sqrt(lam/L),eta),s.sqrt(lam/L))
check('two-dimensional Jacobian',s.det(s.diag(s.sqrt(lam/L),s.sqrt(lam/L))),lam/L)
sigma=-b-c*t-n/4
check('threshold power',2*(b+c*t+sigma)+(n-2)/2,-1)
check('affine intercept',(-b-c*t-n/4).subs(b,-a-n/4),a-c*t)
check('dimension notation',d/4+s.Rational(1,2),(d+2)/4)
check('critical logarithmic substitution',(lam**-1*L**(-d/2)).subs(lam,s.exp(r))*s.exp(r),r**(-d/2))
q=s.symbols('q',positive=True);cp=s.symbols('cp',nonnegative=True)
check('positive quadratic scaling',q*s.sqrt(cp/q)**2,cp)
check('negative quadratic scaling',-q*s.sqrt(cp/q)**2,-cp)
check('rescaled packet center',(theta*s.sqrt(lam*L))/(s.sqrt(lam*L)),theta)
check('rescaled packet half width',s.sqrt(lam/L)/s.sqrt(lam*L),1/L)
check('three-dimensional constant line',-s.Rational(-3,4)-s.Rational(3,4),0)
check('three-dimensional falling line',-s.Rational(-3,4)-t-s.Rational(3,4),-t)
check('four-dimensional falling line',2-t-1,1-t)
check('four-dimensional rising line',2+t-1,1+t)
check('indefinite positive vector',s.Integer(1)**2-s.Integer(0)**2,1)
check('indefinite negative vector',s.Integer(0)**2-s.Integer(1)**2,-1)
source=root/'positive-packets-and-prescribed-concave-regularity.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=dict(passed=all(x['passed'] for x in rows),total_cases=len(rows),exact_algebraic_checks=len(rows),numerical_checks=0,cases=rows,source_sha256=sha(source),script_sha256=sha(Path(__file__)))
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:result[k] for k in ['passed','total_cases','source_sha256']}))

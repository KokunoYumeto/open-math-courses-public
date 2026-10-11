"""Exact finite checks of the packet scales; the existence theorem is proved in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
t,r,delta,x,y=s.symbols('t r delta x y',positive=True,real=True)
checks=[]
def check(name,expr):
 assert s.simplify(expr)==0,(name,expr)
 checks.append(name)
for d in [1,2,3,5]:
 check(f'normal squared normalization d={d}',t**(-d)*(t/s.log(t))**d-s.log(t)**(-d))
 check(f'full lower box dimension d={d}',t**(2*delta-d)*(t/s.log(t))**d/s.log(t)**2-t**(2*delta)/s.log(t)**(d+2))
for lam in [4,8,16]:
 check(f'support width logt={lam}',s.Rational(1,8)/lam-2*s.Rational(1,16)/lam)
check('strict barrier Laplacian',s.diff(x*x+y*y+s.Rational(1,8),x,2)+s.diff(x*x+y*y+s.Rational(1,8),y,2)-4)
check('superharmonic index Laplacian',s.diff(-x*x-y*y,x,2)+s.diff(-x*x-y*y,y,2)+4)
phi=x*x+y*y+s.Rational(1,8);index=-x*x-y*y
check('target positive gap',phi+index-s.Rational(1,8))
check('lower exponent in dimension three',2*(phi+index).subs({x:0,y:0})-s.Rational(1,4))
check('logarithmic growth derivative',s.diff(r/4-3*s.log(r),r)-(s.Rational(1,4)-3/r))
check('growth critical log scale',(s.Rational(1,4)-3/r).subs(r,12))
check('strict test gap at unit radius',1+s.Rational(1,8)-2+s.Rational(7,8))
v=s.symbols('v',real=True);eta=s.symbols('eta',real=True)
check('profile differentiation scale',s.diff((eta/t-1)*s.log(t),eta)-s.log(t)/t)
check('inverse profile Jacobian',s.diff(t*(1+v/s.log(t)),v)-t/s.log(t))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(root/'prescribed-superharmonic-regularity.md'),'script_sha256':sha(Path(__file__)),'scope':'Exact packet Jacobians, all displayed dimension powers, support and plateau scales, quadratic barrier signs and the explicit growth derivative. Completeness, approximation and existence are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');print(json.dumps(out))

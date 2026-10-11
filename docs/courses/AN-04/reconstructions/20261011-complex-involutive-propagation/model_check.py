"""Exact checks of signs and explicit comparison identities; not a substitute for proofs."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent
x,y,c,alpha,beta,t,rho,R,r0=s.symbols('x y c alpha beta t rho R r0',real=True,positive=True)
z=x+s.I*y;zb=x-s.I*y
L=lambda f:-s.I*s.diff(f,x)+s.diff(f,y)
checks=[]
def check(name,value):
 assert s.simplify(value)==0,(name,value)
 checks.append(name)
check('L z',L(z));check('L conjugate z',L(zb)+2*s.I)
v=-s.I*c*zb/2
check('gauge exponent sign',L(v)+c)
check('exact scalar gauge',L(s.exp(v))+c*s.exp(v))
for k in range(5):check('holomorphic polynomial '+str(k),L(z**k))
check('affine holomorphic variable weight',L(t**(alpha+beta*z)))
check('nonholomorphic variable weight',L(t**(x*x+y*y))+2*s.I*z*s.log(t)*t**(x*x+y*y))
h=s.log(R/rho)/s.log(R/r0)
check('annular harmonic radial equation',s.diff(h,rho,2)+s.diff(h,rho)/rho)
check('inner coefficient',h.subs(rho,r0)-1);check('outer coefficient',h.subs(rho,R))
check('exact midpoint coefficient',h.subs({R:1,r0:s.Rational(1,4),rho:s.Rational(1,2)})-s.Rational(1,2))
check('truncated fundamental absolute mass',s.integrate(1,(rho,0,R))-R)
for k in range(1,4):check('harmonic real part '+str(k),s.diff(s.re(z**k),x,2)+s.diff(s.re(z**k),y,2))
source=r/'complex-involutive-normal-form-and-regularity-propagation.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'scope':'Exact scalar signs, holomorphic and nonholomorphic commutators, harmonic polynomial and annular identities, and local kernel mass. The infinite-order, microlocal and propagation arguments are in the lesson.'}
(r/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(out))

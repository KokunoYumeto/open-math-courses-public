"""Exact finite checks for the constants and examples; not a substitute for the analytic proof."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
x,y,a,r,t,lam=s.symbols('x y a r t lam',real=True,positive=True)
z=x+s.I*y
dz=lambda f:(s.diff(f,x)-s.I*s.diff(f,y))/2
db=lambda f:(s.diff(f,x)+s.I*s.diff(f,y))/2
checks=[]
def equal(name,lhs,rhs):
 assert s.simplify(lhs-rhs)==0,name
 checks.append({'name':name,'passed':True})
equal('bar derivative of z',db(z),0)
equal('bar derivative of conjugate z',db(s.conjugate(z)),1)
phi=x*x+2*y*y+x*y+x*x*x*y
w=1+x+y*y+s.I*x*y
delta=lambda f:dz(f)-dz(phi)*f
equal('full weighted derivative commutator',db(delta(w))-delta(db(w)),-db(dz(phi))*w)
equal('Laplacian curvature factor',4*db(dz(phi)),s.diff(phi,x,2)+s.diff(phi,y,2))
equal('Gaussian curvature',4*db(dz(a*(x*x+y*y))),4*a)
equal('Gaussian radial mass',2*s.pi*s.integrate(r*s.exp(-a*r*r),(r,0,s.oo)),s.pi/a)
equal('Gaussian minimal solution norm',2*s.pi*s.integrate(r**3*s.exp(-a*r*r),(r,0,s.oo)),s.pi/a**2)
equal('sharp weighted right side',4/(4*a)*s.pi/a,s.pi/a**2)
equal('quadratic peak polynomial',s.Rational(1,4)+z-s.Rational(1,2),z-s.Rational(1,4))
equal('quadratic peak gap',x*x+y*y-s.re(z-s.Rational(1,4)),(x-s.Rational(1,2))**2+y*y)
equal('anisotropic quadratic holomorphic part',s.re(-z*z/2),(-x*x+y*y)/2)
equal('anisotropic quadratic curvature gap',x*x+2*y*y-s.re(-z*z/2),s.Rational(3,2)*(x*x+y*y))
equal('cutoff inner gap',s.Rational(1,2)**2/4,s.Rational(1,16))
equal('cutoff outer gap',s.Rational(1,2)**2,s.Rational(1,4))
equal('rescaled weighted estimate factor',4/(2*lam),2/lam)
for k in [1,2,3]:
 equal('exact peak derivative '+str(k),s.diff(s.exp(lam*(z-s.Rational(1,4))),x,k),lam**k*s.exp(lam*(z-s.Rational(1,4))))
equal('small scale weight comparison exponent',lam*(2/lam),2)
equal('profile e4 at inner annulus',4*s.Rational(1,4)**2,s.Rational(1,4))
equal('profile e16 at inner annulus',16*s.Rational(1,4)**2,1)
source=ROOT/'weighted-cauchy-riemann-estimates-and-holomorphic-peaks.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'source':source.name,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'scope':'Wirtinger signs, full commutator, curvature factor, Gaussian sharpness, Taylor gaps, cutoff margins and logarithmic derivatives. Functional existence, local regularity and uniform bounds are proved in the lesson.',
 'checks':checks}
(ROOT/'model-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps({k:report[k] for k in ['passed','total_cases','exact_algebraic_checks','source_sha256','script_sha256']}))

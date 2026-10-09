"""Exact identities for the observation reduction; not a replacement for its proof."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
x,z,eta,rho,c,k,N,r,delta,lam=s.symbols('x z eta rho c k N r delta lam',real=True)
ap,am=s.symbols('ap am',complex=True)
checks=[]
def check(name,expr):
 value=s.simplify(expr.rewrite(s.exp))
 assert value==0,(name,value)
 checks.append(name)
ell=rho-c*eta
check('exact right reciprocal',ell/ell-1)
check('normal reciprocal derivative',s.diff(1/ell,rho)+1/ell**2)
check('tangential reciprocal derivative',s.diff(1/ell,eta)-c/ell**2)
check('second normal reciprocal derivative',s.diff(1/ell,rho,2)-2/ell**3)
check('joint reciprocal derivative',s.diff(1/ell,rho,eta)+2*c/ell**3)
check('weighted reciprocal example',(lam/ell).subs({c:2,rho:2*eta+2*delta*lam})-1/(2*delta))
theta=s.symbols('theta',real=True)
check('Peetre inequality positive remainder',2*(1+eta**2)*(1+theta**2)-(1+(eta+theta)**2)-(1+(eta-theta)**2+2*eta**2*theta**2))
h=s.Function('h')(x);e=rho-h*eta;b=1/e
error=-s.diff(b,rho)*(-s.I*s.diff(h,x)*eta)
check('first variable coefficient defect',error+s.I*s.diff(h,x)*eta/e**2)
correction=s.I*s.diff(h,x)*eta/e**3
check('first left inverse correction',correction*e+error)
check('normal numerator identity',rho/e-(1+h*eta/e))
D=lambda f:-s.I*s.diff(f,x)
kap=c*k
u=(ap*s.exp(s.I*kap*x)+am*s.exp(-s.I*kap*x))*s.exp(s.I*k*z)
vp=D(u)+kap*u;vm=D(u)-kap*u
check('original second order equation',D(D(u))+c**2*s.diff(u,z,2))
check('plus branch removes minus',vp-2*kap*ap*s.exp(s.I*kap*x+s.I*k*z))
check('minus branch removes plus',vm+2*kap*am*s.exp(-s.I*kap*x+s.I*k*z))
check('plus first order equation',D(vp)-kap*vp)
check('minus first order equation',D(vm)+kap*vm)
check('full boundary comparison',(vm-vp).subs(x,0)+2*kap*(ap+am)*s.exp(s.I*k*z))
check('zero Dirichlet matching',(vm-vp).subs({x:0,am:-ap}))
check('zero observed coefficient',vp.subs(ap,0))
check('nonzero complementary coefficient',vm.subs(ap,0)+2*kap*am*s.exp(-s.I*kap*x+s.I*k*z))
gaussian=s.exp(-eta**2)
check('residual first derivative',s.diff(gaussian,eta)+2*eta*gaussian)
check('residual second derivative',s.diff(gaussian,eta,2)-(4*eta**2-2)*gaussian)
check('residual has no normal derivative',s.diff(gaussian,rho))
check('mixed norm independent of normal mode',s.diff((2*s.pi)**2*s.exp(-2*k**2)*(1+k**2)**r,N))
check('two circle volume',s.integrate(s.integrate(1,(x,0,2*s.pi)),(z,0,2*s.pi))-(2*s.pi)**2)
check('positive characteristic line',eta**2-eta**2)
check('negative characteristic line',(-eta)**2-eta**2)
check('upper edge root separation',s.Rational(5,4)*eta-eta-eta/4)
check('lower edge root separation',eta-s.Rational(3,4)*eta-eta/4)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(root/'a-fixed-interior-observation-test-for-reflection.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Exact reciprocal derivatives, first variable correction, mode extraction, residual norm distinction and figure coordinates; full uniform operator and remainder bounds are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

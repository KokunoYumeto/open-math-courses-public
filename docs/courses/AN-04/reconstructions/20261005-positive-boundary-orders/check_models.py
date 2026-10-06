"""Finite supporting checks; the complete proofs are in the companion."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import mpmath as mp
HERE=Path(__file__).resolve().parent
mp.mp.dps=40
checks=[]
def record(name,detail):checks.append({'name':name,'passed':True,'detail':detail})
x,y=S.symbols('x y',real=True)
L=S.log(x*x+y*y)/2+S.I*S.atan(y/x)
assert S.simplify(S.diff(L,x)-1/(x+S.I*y))==0
assert S.simplify(S.diff(L,y)-S.I/(x+S.I*y))==0
for h in [mp.mpf(1),mp.mpf('1.5'),mp.mpf(4)]:
 for tau in [-6,-1,0,2,7]:
  ell=mp.mpc(h,tau)
  for z in [mp.mpc('0.25','-2'),mp.mpc('-1.5','0.3'),mp.mpc(2,0)]:
   value=mp.exp(z*mp.log(ell))
   expected=abs(ell)**z.real*mp.exp(-z.imag*mp.arg(ell))
   assert abs(abs(value)/expected-1)<mp.mpf('1e-36')
record('right-half-plane-branch','Both exact derivatives and 45 complex modulus/real-isometry cases')
laplace_cases=0
for q in [mp.mpc('0.7','0.4'),mp.mpc('1.5','-0.6'),mp.mpc(3,2)]:
 for h,tau in [(1,0),(2,1),(2,-2),(4,3)]:
  numerical=mp.quad(lambda t:t**(q-1)*mp.exp(-(h+mp.j*tau)*t),[0,1,mp.inf])
  exact=mp.gamma(q)*mp.exp(-q*mp.log(h+mp.j*tau))
  assert abs(numerical-exact)<mp.mpf('1e-26')*max(1,abs(exact))
  derivative=mp.quad(lambda t:-mp.j*t**q*mp.exp(-(h+mp.j*tau)*t),[0,1,mp.inf])
  assert abs(derivative+mp.j*q*exact/(h+mp.j*tau))<mp.mpf('1e-26')
  laplace_cases+=1
record('complex-Laplace-and-ODE',f'{laplace_cases} independent complex quadratures and differentiated identities')
for q in [mp.mpc('0.7','0.4'),mp.mpc('1.5','-0.6'),mp.mpc(3,2)]:
 for n in [1,3,7]:
  integral=mp.quad(lambda u:u**(q-1)*(1-u)**n,[0,1])
  product=mp.factorial(n)/mp.fprod(q+k for k in range(n+1))
  assert abs(integral-product)<mp.mpf('1e-26')
 n=5000
 logarithm=q*mp.log(n)-mp.fsum(mp.log(1+q/k) for k in range(1,n+1))-mp.log(q)
 approximation=mp.exp(logarithm)
 assert abs(approximation/mp.gamma(q)-1)<mp.mpf('.003')
record('nonzero-gamma-product','Nine beta quadratures and three convergent complex finite products')
xi,eta=S.symbols('xi eta',real=True);den=1+xi**2+eta**2
A=S.Matrix([[1+xi,eta+S.I],[xi*eta,eta**2+2]])
E1=S.Matrix([[1,eta],[0,xi]]);E2=S.Matrix([[eta,0],[S.I,1]])
W1=xi*A/den;W2=eta*A/den
A1=W1-E1;A2=W2-E2;A0=A/den+xi*E1+eta*E2
assert S.simplify(A0+xi*A1+eta*A2-A)==S.zeros(2)
record('full-integer-residual-decomposition','Exact ordered 2-by-2 identity retains both arbitrary residual terms')
t,h,tau=S.symbols('t h tau',positive=True)
for k in range(1,6):
 kernel=t**(k-1)*S.exp(-h*t)/S.factorial(k-1)
 transformed=S.integrate(kernel*S.exp(-S.I*tau*t),(t,0,S.oo))
 assert S.simplify(transformed-(h+S.I*tau)**(-k))==0
record('one-sided-kernel-constants','Five exact normal Fourier transforms, including the unit delta normalization')
z=x+S.I*y
for f in [z,1+z**2,(2-S.I)*z**3+z+S.I]:
 u=S.re(S.expand_complex(f));v=S.im(S.expand_complex(f));norm=S.expand(u*u+v*v)
 lap=S.diff(norm,x,2)+S.diff(norm,y,2)
 expected=4*(S.diff(u,x)**2+S.diff(u,y)**2)
 assert S.simplify(lap-expected)==0
 assert S.simplify(S.diff(norm+x*x+y*y,x,2)+S.diff(norm+x*x+y*y,y,2)-lap)==4
record('rectangle-maximum-identity','Three nonconstant holomorphic polynomials and strict real quadratic perturbation')
M=mp.mpf(3);m=mp.mpf('1.3');eps=mp.mpf('.5')
# This family has precisely the vertical exponential growth permitted in PS14.
F=lambda z:mp.exp(mp.mpc('.4','.7')*z)
def damped(z):return F(z)*mp.exp(eps*(z-m)**2)
C=[]
for a in [mp.mpf(0),M]:
 tau_star=-mp.mpf('.7')/(2*eps)
 C.append(abs(damped(mp.mpc(a,tau_star))))
bound=C[0]**(1-m/M)*C[1]**(m/M)
assert abs(F(m))<=bound
for a in [0,m,M]:
 assert abs(damped(mp.mpc(a,30)))<mp.mpf('1e-180')
record('Gaussian-strip-normalization','Exact vertical maximizers, geometric endpoint constant and horizontal decay')
sources={p.relative_to(HERE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
 for p in [HERE/'positive-order-halfspace-bounds.md',HERE/'figures/positive_order_halfspace.py',
           HERE/'figures/positive_order_halfspace.png',HERE/'figures/positive_order_halfspace.svg']}
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':len(checks),
 'checks':checks,'source_hashes':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'complete_proof_not_inferred_from_models':True}
(HERE/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

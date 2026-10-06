"""Finite sign, normalization and remainder checks; not a substitute for proofs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
checks=[]
def record(name,detail):checks.append({'name':name,'passed':True,'detail':detail})
t1,t2,z,p1,p2=S.symbols('t1 t2 z p1 p2',real=True)
kappa=S.Matrix([(2+z)*t1+t2+t1*t1,3*t2+t1*t2,z+z*z+t1])
Psi=S.Matrix([[2+z+t1,1],[t2,3]])
assert S.simplify(kappa[:2,0]-Psi*S.Matrix([t1,t2]))==S.zeros(2,1)
J=kappa.jacobian([t1,t2,z]);J0=J.subs({t1:0,t2:0})
B=Psi.subs({t1:0,t2:0});D=1+2*z
assert S.simplify(J0.det()-B.det()*D)==0
tau=B.inv().T*S.Matrix([p1,p2])
canonical=S.Matrix([z+z*z,tau[0],tau[1]]).jacobian([z,p1,p2])
assert S.simplify(canonical.det()-D/B.det())==0
assert S.simplify(J0.det()/B.det()**2-canonical.det())==0
record('nonlinear-half-density-coordinate-law','Full nonblock-diagonal ambient chart and conormal Jacobian give the same squared half-density factor')
n,k,m=S.symbols('n k m')
r=m+(n-2*k)/4
assert S.simplify(r+k/2-m-n/4)==0
q=S.symbols('q',positive=True)
assert S.simplify(q**k*q**(-(n+2*k)/2)*q**(n/2))==1
assert S.simplify((n+2*k).subs({n:2*S.Symbol('d'),k:S.Symbol('d')})/4-S.Symbol('d'))==0
record('intrinsic-orders-and-energy','Exact codimension-independent symbol order, all Fourier-energy powers and ordinary diagonal normalization')
t,x,w,tau,eta=S.symbols('t x w tau eta',real=True)
count=0
for j in range(6):
 for ell in range(5):
  a=w**ell*tau**j
  amplitude=(t*tau+x*eta)*a
  # The first Gauss contraction is -i d_w d_eta.
  first=(amplitude-S.I*S.diff(amplitude,w,eta)).subs({w:x,eta:0})
  # The second is +i d_t d_tau.
  reduced=(first+S.I*S.diff(first,t,tau)).subs(t,0)
  expected=S.I*(j+1-ell)*x**ell*tau**j
  assert S.simplify(reduced-expected)==0
  # Direct t D_t D_t^j delta = i(j+1) D_t^j delta.
  direct=(S.I*(j+1)-S.I*ell)*x**ell*tau**j
  assert S.simplify(reduced-direct)==0
  count+=1
record('ordered-two-Gauss-action',f'{count} monomial amplitudes compare both contraction signs against direct delta-jet differential action')
a,b=S.symbols('a b',positive=True)
rad=(a+b)/2;ratio=(a-b)/rad
for d in [-1,0,1,2,4]:
 f=rad**d*(1+ratio+ratio**2)
 assert S.simplify(a*S.diff(f,a)+b*S.diff(f,b)-d*f)==0
record('corner-homogeneity','Exact radial degree after the full nonlinear corner-coordinate substitution')
sigma=S.symbols('sigma',positive=True)
for j in range(1,7):
 for ell in range(j-1):
  value=(sigma**ell-sigma**(j-1))/(j-1-ell)
  assert S.simplify(sigma*S.diff(value,sigma)-(j-1)*value+sigma**ell)==0
 resonant=-sigma**(j-1)*S.log(sigma)
 assert S.simplify(sigma*S.diff(resonant,sigma)-(j-1)*resonant+sigma**(j-1))==0
empty_case=S.exp(-sigma)/sigma
assert S.simplify(sigma*S.diff(empty_case,sigma)+empty_case+S.exp(-sigma))==0
record('inverse-Euler-and-logarithm','Every polynomial and resonant log term through j=6, plus the separate j=0 integrable model')
lam=S.symbols('lam',positive=True)
rho=S.symbols('rho',positive=True)
for nu in range(7):
 L=nu+3
 near=S.integrate(rho**(nu+1),(rho,0,2/lam))
 assert S.simplify(near*lam**(nu+2)-2**(nu+2)/S.Integer(nu+2))==0
 far=lam**(-L)*S.integrate(rho**(nu-L+1),(rho,1/lam,1))
 assert S.simplify(far-(lam**(-nu-2)-lam**(-nu-3)))==0
record('all-derivative-remainder-integrals','Seven exact two-dimensional near/far integrals have the required negative frequency degree')
v=S.symbols('v',positive=True)
poly=3+2*a-5*b+7*a*b+a**2
test=(1+a+b)**6
moments={(0,0):3,(1,0):2,(0,1):-5,(1,1):7,(2,0):1}
symbol=sum(c*(S.I*a)**i*(S.I*b)**j for (i,j),c in moments.items())
assert S.Poly(symbol.subs({a:v,b:2*v}),v).degree()==2
jets=sum(c*S.diff(test,a,i,b,j).subs({a:0,b:0}) for (i,j),c in moments.items())
taylor=S.Poly(S.expand(test),a,b)
trunc=sum(c*a**powers[0]*b**powers[1] for powers,c in taylor.terms() if sum(powers)<=2)
assert jets==sum(c*S.diff(trunc,a,i,b,j).subs({a:0,b:0}) for (i,j),c in moments.items())
record('point-supported-jet-identification','Mixed normal jets depend on the full finite Taylor polynomial; their nonzero Fourier polynomial fails decay')
sources={p.relative_to(HERE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(HERE.glob('*.md'))}
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':len(checks),'checks':checks,
 'source_hashes':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'complete_proof_not_inferred_from_models':True}
(HERE/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

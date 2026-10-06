"""Finite checks for the exact profile and diagram; these do not replace proofs."""
from pathlib import Path
import hashlib,json,math,re
import sympy as S
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
k,g,r=S.symbols('k g r',real=True)
beta=(k+2)/4
assert S.simplify(-2*beta+k/2+1)==0
assert S.simplify(k/2-beta-(beta-1))==0
assert S.simplify((2*r-2*g+k/2).subs(r,g-(k+2)/4)+1)==0
checks.append('Exact Gaussian norm exponent, inverse-profile exponent and logarithmic threshold')
errs=[]
for lam in [2.,5.,11.]:
 for y in [0.,.25,.6]:
  val=quad(lambda nu:math.exp(-nu*nu/(4*lam))*math.cos(y*nu),-math.inf,math.inf,
           epsabs=1e-10,epsrel=1e-10)[0]
  exact=math.sqrt(4*math.pi*lam)*math.exp(-lam*y*y)
  errs.append(abs(val-exact))
assert max(errs)<1e-8
checks.append('Independent numerical Gaussian Fourier normalization at nine probes')
lam,y,a,u=S.symbols('lam y a u',positive=True)
poly=S.Integer(1)
for m in range(5):
 direct=S.diff(lam**a*S.exp(-lam*y*y),lam,m)
 expected=lam**(a-m)*S.exp(-lam*y*y)*poly.subs(u,lam*y*y)
 assert S.simplify(direct-expected)==0
 poly=S.expand((a-m-u)*poly+u*S.diff(poly,u))
checks.append('Full lambda derivative recurrence through order four before polynomial-Gaussian bounds')
def bump(x):return math.exp(-1/(1-x*x)) if abs(x)<1 else 0.
for t in [.001,.02,.25,.5,.73,.98,.999]:
 T=1/(1-t)-1/t
 assert 1/(1-t)**2+1/t**2>0
 ids=range(math.floor(T)-2,math.ceil(T)+3)
 terms=[bump(T-j) for j in ids]
 total=sum(terms)
 assert total>0 and abs(sum(x/total for x in terms)-1)<1e-14
 assert sum(x>0 for x in terms)<=2
checks.append('Positive rational time coordinate and actual locally finite partition at endpoint and interior probes')
for tau in [-80.,-30.,30.,80.]:
 b=lambda t:math.exp(1-1/(1-t*t)) if t<1 else 0.
 val=quad(lambda t:b(t)*math.cos(tau*t),0,1,epsabs=1e-11)[0]-1j*quad(
  lambda t:b(t)*math.sin(tau*t),0,1,epsabs=1e-11)[0]
 assert abs(val-1/(1j*tau))<10/(tau*tau)
checks.append('Both temporal signs retain the nonzero endpoint Fourier term for a smooth cutoff')
svg=(ROOT/'figures/prescribed-singular-ray.svg').read_text('utf8')
for q,left,right in [(1,82.,338.),(3,167.3333,252.6667),(6,188.6667,231.3333)]:
 assert abs((210-left)/32-4/q)<2e-6
 assert abs((right-210)/32-4/q)<2e-6
 assert abs((730-490)/60-4)<1e-14
 lf=str(left).removesuffix('.0');rf=str(right).removesuffix('.0')
 assert f'L{lf} 490 H{rf}' in svg
assert '<path d="M185 162 H335"' in svg
for yy in [162,242]:
 for xx in [185,335]:assert f'cx="{xx}" cy="{yy}"' in svg
checks.append('Original SVG uses exact segment endpoints and cone axes r=(x-210)/32, lambda=(730-y)/60')
out={'passed':True,'finite_groups':len(checks),'checks':checks,
 'largest_gaussian_quadrature_error':max(errs),'script_sha256':sha(Path(__file__)),
 'source_hashes':{p:sha(ROOT/p) for p in ['prescribed-finite-singular-rays.md','figures/prescribed-singular-ray.svg']},
 'scope':'Finite formula and diagram checks only; complete proof review is separately required.',
 'full_course_complete':False}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks),'gaussian_error':max(errs)}))

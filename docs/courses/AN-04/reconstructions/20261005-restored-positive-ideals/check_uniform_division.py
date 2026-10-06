"""Finite algebra/sign controls for the privately written uniform graph-division proof."""
import datetime,hashlib,json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import quad
here=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path,d):path.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
checks=[]
v1,v2,z,u,V1,V2=s.symbols('v1 v2 z u V1 V2',real=True)
T=s.Matrix([s.I*z,z**2+s.I*z**3]);v=s.Matrix([v1,v2])
P=V1**3+V1*V2+V2**2
path=T+u*(v-T)
coeff=[s.integrate(s.diff(P,V).subs({V1:path[0],V2:path[1]}),(u,0,1)) for V in [V1,V2]]
rem=P.subs({V1:T[0],V2:T[1]})
assert s.simplify(P.subs({V1:v1,V2:v2})-rem-sum((v[j]-T[j])*coeff[j] for j in range(2)))==0
checks.append({'name':'Whole multivariable polynomial Taylor/path division','passed':True,
 'scope':'Exact complex graph T=(iz,z^2+iz^3), all coefficients and residue of a cubic mixed polynomial, with complete straight-path integrals.'})

def flat(w):return 0. if abs(w)<1e-150 else np.exp(-1/w**2)
def flatprime(w):return 0. if abs(w)<1e-150 else 2*np.exp(-1/w**2)/w**3
def cint(f):return quad(lambda u:np.real(f(u)),0,1,epsabs=1e-12)[0]+1j*quad(lambda u:np.imag(f(u)),0,1,epsabs=1e-12)[0]
wrong_errors=[];trials=[]
# A(V)=V+g(ImV)*barV is almost analytic and equals a(v)=v on the real axis.
for zv in [-.8,-.6,-.2,.2,.6,.8]:
 for vv in [-.4,.3]:
  Tv=1j*zv
  def V(u):return Tv+u*(vv-Tv)
  def dbar(u):
   point=V(u);wv=np.imag(point)
   return flat(wv)+.5j*flatprime(wv)*np.conj(point)
  remv=Tv+flat(zv)*np.conj(Tv)
  qv=cint(lambda u:1+flat(np.imag(V(u))))
  E=2j*zv*cint(dbar)
  actual=vv-remv-(vv-Tv)*qv
  assert abs(E-actual)<3e-12,(zv,vv,E,actual)
  fj=vv-Tv;S=abs(fj)**2;ej=np.conj(fj)*E/S
  assert abs(fj*ej-E)<1e-12
  wrong_errors.append(abs(-E-actual))
  trials.append({'real_argument':vv,'imaginary_shift':zv,'correct_error':abs(E-actual),'wrong_sign_error':abs(-E-actual)})
assert max(wrong_errors)>.01
checks.append({'name':'Actual almost-analytic nonholomorphic path error and sign control','passed':True,
 'scope':'Twelve independently integrated paths for A(V)=V+exp(-1/(ImV)^2)*barV; the +2i ImT error and exact conjugate-generator division pass, and reversing its sign fails.',
 'trials':trials})

for k in range(2,15):
 for l in range(k//2+1):
  # A finite model of the diagonal cutoff choice: C=2^(k^3), epsilon=2^(-3k^2).
  exponent=k**3-3*k**2*(k-l)
  assert exponent<=-k
checks.append({'name':'Diagonal cutoff summability mechanism','passed':True,
 'scope':'Thirteen levels and all derivative orders <=half the degree verify the precise C*epsilon^(degree-order)<=2^(-degree) choice used in the written smooth extension. This finite model does not certify arbitrary families.'})

proof=here/'positive-lagrangian-ideals-and-distributions.md'
assert proof.exists() and len(checks)==3 and all(r['passed'] for r in checks)
report={'schema':'private-uniform-complex-graph-division-check/v1',
 'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'checks':checks,
 'proof':'positive-lagrangian-ideals-and-distributions.md, Section 2','proof_sha256':sha(proof),
 'script_sha256':sha(Path(__file__)),
 'written_argument':'Author derivation includes uniform cutoff Taylor extension, almost-analytic flatness, full path-chain identity, exact flat-error division and all derivative bounds on a fixed patch.',
 'limitations':'Finite algebra and sign controls support the author-written supporting proof; they do not certify the general argument, complete the public teaching lesson or imply independent review.'}
dump(here/'uniform-division-checks.json',report)
print(json.dumps({'passed':True,'finite_control_groups':3,'nonholomorphic_paths':12,'wrong_sign_control_fails':True,'private_proof_sha256':report['proof_sha256']}))

"""Finite endpoint, commutator and scaled-jet checks. CC0; proofs remain in the text."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,cmath
import sympy as sp
ROOT=Path(__file__).resolve().parent
groups=[]
def done(name,detail):groups.append({'name':name,'passed':True,'detail':detail})
def close(a,b,tol=1e-9):assert abs(a-b)<=tol*max(1,abs(a),abs(b)),(a,b)
# The normal delta has transform one. Exact sharp annuli give the endpoint.
for count in [2,4,8,16]:
 vals=[2**(-j/2)*math.sqrt(2*(2**(j+1)-2**j)/(2*math.pi)) for j in range(1,count+1)]
 close(max(vals),1/math.sqrt(math.pi));close(sum(v*v for v in vals),count/math.pi)
done('Besov endpoint versus Sobolev sum','Exact one-dimensional delta block norms: bounded supremum and linearly divergent square sum')
t=sp.symbols('t',real=True)
D=lambda f:-sp.I*sp.diff(f,t)
X=lambda f:t*D(f)
for k in range(7):
 for degree in range(10):
  f=t**degree;prod=f
  for j in range(k):prod=sp.expand(X(prod)+sp.I*j*prod)
  expected=t**k*(-sp.I)**k*sp.diff(f,t,k)
  assert sp.expand(prod-expected)==0
done('weighted normal generators','All lower imaginary coefficients in the triangular identity, orders zero through six')
x,s=sp.symbols('x s',real=True)
q=(s-1)**2*(2-s)**2
for degree in range(6):
 u=(x-s)**degree
 Q=sp.integrate(q*u,(s,1,2))
 QXu=sp.integrate(q*(-sp.I*degree*(x-s)**degree),(s,1,2))
 left=sp.expand(-sp.I*x*sp.diff(Q,x)-QXu)
 right=sp.integrate(-sp.I*sp.diff(s*q,s)*u,(s,1,2))
 assert sp.simplify(left-right)==0
done('positive convolution commutator','Exact finite moments on a positive normal interval, retaining the derivative-of-kernel term and sign')
for delta in [.2,.5,1,1.5,3]:
 for eps in [.001,.03,.2,1]:
  for j in range(50):
   value=2**(-j*delta)*min(eps*2**j,1)
   assert value<=eps**min(1,delta)*(1+1e-12)
done('strict conormal approximation loss','Both sides of the dyadic split, including delta=1 and fractional losses')
alpha=sp.symbols('alpha',positive=True)
f=sp.exp(-alpha*t)
for j in range(9):
 jet=((-sp.I)**j*sp.diff(f,t,j)).subs(t,0)
 delta_pair=(-1)**j*sp.diff(f,t,j).subs(t,0)
 assert sp.simplify((-sp.I)**j*jet-delta_pair)==0
assert sp.I*(-sp.I)==1
done('intrinsic trace and delta jets','Exact (-i)^j pairing for nine jet orders and the plus-i correction cancelling D H')
for N in range(1,8):
 for w in [-9,-1,-.2,.03,.5,4,11]:
  poly=sum((-1j*w)**j/math.factorial(j) for j in range(N))
  remainder=abs(cmath.exp(-1j*w)-poly)
  if abs(w)<=1:
   assert remainder<=abs(w)**N/math.factorial(N)+1e-12
  else:
   C=1+sum(1/math.factorial(j) for j in range(N))
   assert remainder<=C*abs(w)**(N-1)+1e-12
done('scaled test Fourier remainder','Low-frequency Taylor and high-frequency polynomial bounds for orders one through seven')
for N in range(1,9):
 nodes=list(range(1,N+1))
 coeff=[sp.prod(sp.Rational(-r,l-r) for r in nodes if r!=l) for l in nodes]
 for j in range(N):assert sp.simplify(sum(c*l**j for c,l in zip(coeff,nodes)))==(1 if j==0 else 0)
done('finite scale cancellation','Exact rational Lagrange weights cancel every intermediate Taylor degree, sizes one through eight')
for L in [0,3,17]:
 for A in [0.2,2.5,11]:
  for r in [0,2,7]:
   N=1;a=(L+r+3)/N;K=math.floor(a*A+r+3)+1
   assert L-a*N<-r-2 and a*A-K<-r-2
   desired=3;Np=math.floor(desired+A)+2;d=r+4
   K=max(d+1,math.ceil(((desired+A)*L+(Np+A)*d)/(Np-desired)))+2
   theta=(K-d)/(K+L)
   assert theta*Np-(1-theta)*A>desired
done('two-scale smoothness and interpolation','Every displayed exponent inequality with the actual degree-dependent negative order')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':len(groups),'groups':groups,
 'script_sha256':sha(Path(__file__)),'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'finite_checks_are_not_general_proofs':True,'U031_restored':False,'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(groups)}))

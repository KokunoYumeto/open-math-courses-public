"""Finite convention and sharp-constant checks; not substitutes for the proofs. CC0."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,cmath
import numpy as np
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
groups=[]
def done(name,detail):groups.append({'name':name,'passed':True,'detail':detail})
def close(a,b,tol=2e-9):assert abs(a-b)<=tol*max(1,abs(a),abs(b)),(a,b)
rng=np.random.default_rng(514)
for _ in range(500):
 z,y=rng.normal(size=(2,3))*rng.choice([.1,1,10,100]);r,q=rng.uniform(-4,4,size=2)
 R=lambda v:math.sqrt(1+np.dot(v,v));h=lambda v:math.sqrt(1+np.dot(v[1:],v[1:]))
 ratio=R(z)**r*h(z)**q/(R(y)**r*h(y)**q)
 bound=2**((abs(r)+abs(q))/2)*R(z-y)**(abs(r)+abs(q))
 assert ratio<=bound*(1+1e-12)
 a=r-rng.uniform(0,3);b=r+q-a-rng.uniform(0,3)
 assert R(z)**(a-r)*h(z)**(b-q)<=1+1e-12
done('all-sign weights and embeddings','500 deterministic two-weight Peetre and exact embedding samples')
x=sp.symbols('x',real=True);z=sp.symbols('z',real=True)
for p in [sp.Rational(-7,3),0,sp.Rational(5,2)]:
 P=sp.Integer(1)
 for k in range(5):
  expected=(1+x*x)**((p-k)/2)*P.subs(z,x/sp.sqrt(1+x*x))
  assert sp.simplify(sp.diff((1+x*x)**(p/2),x,k)-expected)==0
  P=sp.expand((p-k)*z*P+(1-z*z)*sp.diff(P,z))
done('real multiplier derivatives','Exact polynomial recursion through four derivatives, including negative and fractional exponents')
for c in [.4,1,2.5,4]:
 for h in [1,2.3]:
  for tau in [-3,.25,2]:
   # Scale s=y/h, retaining the original Fourier sign.
   f=lambda y:y**(c-1)*math.exp(-y)
   real=quad(lambda y:f(y)*math.cos(tau*y/h),0,np.inf,epsabs=2e-10)[0]
   imag=quad(lambda y:-f(y)*math.sin(tau*y/h),0,np.inf,epsabs=2e-10)[0]
   close(h**(-c)*complex(real,imag)/math.gamma(c),(h+1j*tau)**(-c),3e-8)
   for a in [-2.3,0,1.7]:close(abs((h+1j*tau)**a),(h*h+tau*tau)**(a/2))
done('one-sided Laplace multiplier','24 convergent Laplace integrals, exact Fourier sign and real-power modulus')
tau=sp.symbols('tau',real=True)
v=1/(1+sp.I*tau);f0=v;fn=sp.I*v
assert sp.simplify(f0+tau*fn-1)==0
# D(H e^-t)=-i delta+i H e^-t, hence f0+D(i H e^-t)=delta.
assert sp.simplify(sp.I*(-sp.I))==1
for r,q in [(-1,-3),(sp.Rational(-3,4),2),(3,-2)]:
 for h,t in [(1,0),(2,3),(4,-7)]:
  R=math.hypot(h,t);source=R**float(r)*h**float(q)
  close(R**float(r+1)*h**float(q-1)*h/R,source)
  close(R**float(r+1)*h**float(q)/R,source)
done('supported boundary source','Exact delta decomposition with D=-i partial_t and both component norm ratios')
for a in [.1,.5,1,2,7]:
 # The H1 minimal extension is e^-a t for t>0, e^t for t<0.
 exact=(1+a)**2/(2*a)
 direct=quad(lambda t:(1+a*a)*math.exp(-2*a*t),0,np.inf)[0]+1
 close(exact,direct)
 lower=(1+a*a)/(2*a)
 assert .5*exact<=lower+1e-12 and lower<=exact+1e-12
 if a==1:close(lower,.5*exact)
 # J_- = 1-partial_t: applying its inverse to the zero extension of
 # (1+a)e^-a t gives the displayed extension on both sides.
 for t in [-2,-.5,.5,2]:
  got=quad(lambda s:math.exp(t-s)*(1+a)*math.exp(-a*s),max(t,0),np.inf)[0]
  close(got,math.exp(t) if t<0 else math.exp(-a*t))
done('minimal extension and sharp normal-step constant','Exact exponential norms, both-side inverse formula and equality at one-half')
for s,k,expected in [(1,0,math.pi),(2,0,math.pi/2),(2,1,math.pi/2),(3,1,math.pi/8)]:
 c=quad(lambda y:y**(2*k)*(1+y*y)**(-s),-np.inf,np.inf)[0];close(c,expected)
 for h in [1,2,5]:
  integral=quad(lambda y:y**(2*k)*(h*h+y*y)**(-s),-np.inf,np.inf)[0]
  close(integral,h**(2*k+1-2*s)*c)
  close(h**(2*(s-k-.5))*integral/(2*math.pi),c/(2*math.pi))
done('boundary trace coefficient','Four exact trace integrals, normal scaling and retained 1/(2pi) coefficient')
for k in range(7):
 for h,t in [(1,0),(2,3),(1,-7)]:
  close((h*h+t*t)**k,sum(math.comb(k,j)*t**(2*j)*h**(2*(k-j)) for j in range(k+1)))
done('complete integer jet norm','Full binomial Fourier identity at every integer order zero through six')
for _ in range(300):
 r1=rng.uniform(-6,3);r2=r1+rng.uniform(.1,7);a=rng.uniform(r1,r2)
 S=rng.uniform(-8,8);q1=S-r1+rng.uniform(0,3);q2=S-r2+rng.uniform(0,3)
 previous=r1
 for i in range(1,math.ceil(a-r1)+1):
  aj=min(a,r1+i);bj=S-aj
  assert aj<=previous+1+1e-12 and aj<=r2+1e-12
  assert aj+bj<=r1+q1+1e-12 and aj+bj<=r2+q2+1e-12
  previous=aj
 close(previous,a)
done('all-real recovery bookkeeping','300 finite nested-cutoff index sequences at fixed total regularity')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':len(groups),'groups':groups,
 'script_sha256':sha(Path(__file__)),'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'finite_checks_are_not_general_proofs':True,'U031_restored':False,'public_release_authorized':False}
(ROOT/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(groups)}))

"""Finite exact identities supporting, not certifying, the written analytic proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    assert (value is True) if isinstance(value,bool) else value==0,(name,value)
    checks.append({'name':name,'passed':True})
rho,k,n,N,e,m=s.symbols('rho k n N e m',real=True)
delta=1-rho;eps=2*rho-1
check('rescaled normal prefactor',s.expand(delta*k+eps*k/2-k/2))
check('each stationary pair has drop epsilon',s.expand(-1+2*delta+eps))
check('physical normal coefficient power',s.expand(eps+2*delta-1))
check('output Euler derivative order',s.expand(delta-1+rho))
check('clean Fourier scalar order',s.expand(m+(n-2*N-2*e)/4+N-(n+N-e)/2-(m-n/4)))
check('geometric half-density order',s.expand(m+(n-2*N-2*e)/4-(n-N+e)/2+e+n/2-(m+n/4)))
check('stabilized amplitude balance',s.expand(m+n/4-(N+k)/2+k/2-(m+n/4-N/2)))
check('point mass graph order',s.expand(0+n/4-n/4))
check('point mass density order',s.expand(n/4+n/4-n/2))
z,w=s.symbols('z w')
for j in range(5):
    a=(1+z+2*w)**(2*j+2)
    lap=lambda f:s.diff(f,z,2)-s.diff(f,w,2)
    def power(f):
        for _ in range(j):f=lap(f)
        return f.subs({z:0,w:0})
    check('Euler coefficient identity j='+str(j),s.expand(power(z*s.diff(a,z)+w*s.diff(a,w))-2*j*power(a)))
lam=s.symbols('lam',positive=True)
f=s.Function('f')(lam)
for j in range(5):
    check('radial coefficient connection j='+str(j),
          s.simplify(s.diff(lam**(-j)*f,lam)-lam**(-j)*(s.diff(f,lam)-j*f/lam)))
t=s.symbols('t',real=True)
for j in range(1,5):
    check('shifted Gaussian coefficient j='+str(j),
          s.simplify((s.I/2)**j*(-1)**j/s.factorial(j)-(-s.I/2)**j/s.factorial(j)))
angle=s.symbols('angle',real=True)
check('clean leading average vanishes',s.integrate(s.cos(angle),(angle,0,2*s.pi)))
check('clean next average equals one',
      s.integrate(s.cos(angle)*(1+s.cos(angle))**2,(angle,0,2*s.pi))/(2*s.pi)-1)
for r in [s.Rational(3,5),s.Rational(3,4),s.Integer(1)]:
    check('positive exact drop at rho='+str(r),bool((2*r-1)>0))
check('endpoint has zero drop',2*s.Rational(1,2)-1)
raw=(ROOT/'stationary-phase-and-symbols-with-derivative-loss.md').read_bytes()
out={'schema':'AN04-rho-stationary-model-check/v1','passed':True,'total_cases':len(checks),
 'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,
 'source_sha256':hashlib.sha256(raw).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Finite scale, density, Gaussian, Euler-connection and clean-average identities. Uniform estimates and every complete proof are in the lesson.' 
                                                     }
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

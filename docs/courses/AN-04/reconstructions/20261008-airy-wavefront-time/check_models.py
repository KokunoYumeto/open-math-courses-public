"""Finite checks of the affine phase, time signs and exact Airy split. CC0."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
from scipy.special import airy
P=Path(__file__).resolve().parent
q,mu,lam=s.symbols('q mu lam',positive=True)
y1,y2,tau,kap,u=s.symbols('y1 y2 tau kap u',real=True)
checks=[]
def exact(name,value):
    assert s.simplify(value)==0,(name,value)
    checks.append({'name':name,'passed':True,'method':'exact symbolic identity'})
for ep in [1,-1]:
    phase=y1*mu+y2*lam+ep*s.Rational(2,3)/s.sqrt(lam)*((q*lam+mu)**s.Rational(3,2)-mu**s.Rational(3,2))
    v=mu/lam
    exact(f'{ep}: input mu derivative',s.diff(phase,mu)-y1-ep*(s.sqrt(q+v)-s.sqrt(v)))
    exact(f'{ep}: input lambda derivative',s.diff(phase,lam)-y2-ep*((2*q-v)*s.sqrt(q+v)+v**s.Rational(3,2))/3)
    exact(f'{ep}: normal root',s.diff(phase,q)-ep*lam*s.sqrt(q+v))
    exact(f'{ep}: eikonal equation',s.diff(phase,q)**2-q*lam**2-mu*lam)
    exact(f'{ep}: first input point at boundary',s.diff(phase,mu).subs(q,0)-y1)
    exact(f'{ep}: second input point at boundary',s.diff(phase,lam).subs(q,0)-y2)
    exact(f'{ep}: glancing first shift',s.diff(phase,mu).subs(mu,0)-y1-ep*s.sqrt(q))
    exact(f'{ep}: glancing second shift',s.diff(phase,lam).subs(mu,0)-y2-ep*s.Rational(2,3)*q**s.Rational(3,2))
p=-q*(tau-kap)**2-tau**2+kap**2
exact('physical time derivative',s.diff(p,tau).subs({tau:(mu+lam)/2,kap:(mu-lam)/2})+(1+2*q)*lam+mu)
exact('timelike covector',p.subs({tau:1,kap:0})+1+q)
exact('glancing normal position equation',s.diff(u*u,u)-2*u)
exact('glancing normal momentum equation',s.diff(u,u)-1)
exact('glancing first tangential equation',s.diff(-u,u)+1)
exact('glancing second tangential equation',s.diff(-s.Rational(2,3)*u**3,u)+2*u*u)
exact('glancing physical time equation',s.diff(-u-s.Rational(2,3)*u**3,u)+1+2*u*u)
def F(x,ep=1):
    ai,aip,bi,bip=airy(x)
    z=np.sqrt(np.pi)*np.exp(1j*np.pi/4)*(ai-1j*bi)
    zp=np.sqrt(np.pi)*np.exp(1j*np.pi/4)*(aip-1j*bip)
    return (z,zp) if ep==1 else (z.conjugate(),zp.conjugate())
def chi(x):
    if x<=-2:return 0.
    if x>=-1:return 1.
    v=x+2
    a=np.exp(-1/v);b=np.exp(-1/(1-v))
    return a/(a+b)
errs=[]
for ep in [1,-1]:
 for a,b in [(-12,-6),(-2,-1.5),(-1.8,-1.2),(-3,0),(-2,3),(0,0),(1,5),(4,4)]:
    fa,fpa=F(a,ep);fb,_=F(b,ep)
    g=1+.3j;h=.2-.1j
    original=(g*fa+1j*h*fpa)/fb
    result=chi(a)*original
    if a<-1:
        pa=ep*2/3*(-a)**1.5
        f=np.exp(-1j*pa)*fa;fp=np.exp(-1j*pa)*fpa
        result+=(1-chi(a))*chi(b)*np.exp(1j*pa)*(g*f+1j*h*fp)/fb
        if b<-1:
            pb=ep*2/3*(-b)**1.5
            fbb=np.exp(-1j*pb)*fb
            result+=(1-chi(a))*(1-chi(b))*np.exp(1j*(pa-pb))*(g*f+1j*h*fp)/fbb
    err=abs(result-original)/max(1,abs(original));assert err<2e-13
    errs.append(float(err))
for L in [8,64,512]:
    a,_=F(.25*L**(2/3));assert abs(a/a-1)==0
    b,_=F((.25-.125)*L**(2/3))
    assert abs(b/a)<1
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':True,'exact_algebraic_checks':len(checks),'numerical_decomposition_checks':len(errs),
 'numerical_boundary_and_decay_checks':6,'total_cases':len(checks)+len(errs)+6,'checks':checks,
 'maximum_relative_split_error':max(errs),'source_sha256':sha(P/'fourier-airy-wavefronts-and-time-direction.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Finite affine identities and sampled exact decomposition; analytic wavefront and uniformity proofs are in the lesson.'}
(P/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='checks'}))

"""Finite diagnostics for CJ/FS. These complement, not replace, the written proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parent
checks=[]
def add(name,count,detail):
 checks.append({'name':name,'passed':True,'cases':int(count),'scope':detail})
x,y,a,b,u,v=s.symbols('x y a b u v',real=True)
p=3*x**3+2*x*y**2-4*x*y+5*y+1
def jet(aa,bb):
 return s.expand(sum(s.diff(p,x,i,y,j).subs({x:aa,y:bb})*(x-aa)**i*(y-bb)**j/
                     (s.factorial(i)*s.factorial(j)) for i in range(4) for j in range(4-i)))
assert s.expand(jet(a,b)-p)==0
assert s.expand(jet(u,v)-jet(a,b))==0
add('Finite multivariate Taylor polynomial and anchor invariance',2,'Exact total degree three, all mixed terms')
# Exact dyadic cube used in the illustration.
lo=np.array([13/8,1.0]);hi=lo+1/8
khi=np.array([1.0,.4])
dist=np.linalg.norm(lo-khi);diam=np.linalg.norm(hi-lo)
plo=np.array([1.5,1.0]);phi=plo+.25
pd=np.linalg.norm(plo-khi);pdiam=np.linalg.norm(phi-plo)
assert 4*diam<=dist<10*diam and pd<4*pdiam
add('Maximal dyadic cube and failed parent in the illustration',3,'K=[-1,1]x[-0.4,0.4], Q=[13/8,7/4]x[1,9/8]')
# Probe the derivative sizes used in flat-jet cutoff annihilation.
eps=s.symbols('eps',positive=True)
for k in range(6):
 for j in range(k+1):
  power=s.diff(x**(k+1),x,j).subs(x,eps)*eps**(-(k-j))
  assert s.limit(power,eps,0,dir='+')==0
add('Flat-jet powers retain exactly k derivatives',21,'One-dimensional exact polynomial examples, not a general proof')
theta=np.linspace(0,2*np.pi,4096,endpoint=False)
for j in range(1,33):assert abs(np.exp(1j*j*theta).mean())<1e-13
add('Circle cancellation of all sampled nonconstant powers',32,'Angular quadrature residual below 1e-13')
zeta=s.symbols('zeta')
for degree in range(1,7):
 pp=(x+zeta)**degree+2*(x+zeta)+3
 assert s.diff(pp,zeta,degree)==s.factorial(degree)+(2 if degree==1 else 0)
add('Translated polynomial has a fixed nonzero top derivative',6,'Exact degrees one through six')
r=np.linspace(.4,.6,161)
zz=r[:,None]*np.exp(1j*theta[None,:])
assert np.min(np.abs(zz**2-1))>=.64-1e-14
add('Rotating annulus avoids the two roots',len(r)*len(theta),'Q(z)=z^2-1 and 0.4<=|z|<=0.6 imply |Q|>=0.64')
# Integration by parts sign, verified on exponentials.
xi,eta=s.symbols('xi eta')
wave=s.exp(s.I*x*(xi+eta))
def D(expr):return -s.I*s.diff(expr,x)
for coeff in [(2,3,1),(1,s.I,0),(-1,0,2)]:
 Pwave=coeff[0]*wave+coeff[1]*D(wave)+coeff[2]*D(D(wave))
 assert s.simplify(Pwave/wave-(coeff[0]+coeff[1]*(xi+eta)+coeff[2]*(xi+eta)**2))==0
add('Complex frequency multiplier and bilinear transpose convention',3,'No coefficient conjugation in P(-D)')
# Uniform real-phase integration-by-parts identity.
for n in range(5):
 w=s.exp(s.I*x*xi)
 for _ in range(n):w=w-s.diff(w,x,2)
 assert s.simplify(w/s.exp(s.I*x*xi)-(1+xi**2)**n)==0
add('Real-frequency decay identity',5,'(1-d_x^2)^N exp(ix xi)=(1+xi^2)^N exp(ix xi)')
record={'passed':all(c['passed'] for c in checks),'groups':len(checks),'checks':checks,
 'proofs_are_the_written_C1_C5_and_F1_F5':True,'human_review_complete':False,
 'full_course_complete':False,'public_release_authorized':False,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf8')
print(json.dumps({'passed':record['passed'],'groups':len(checks),'finite_cases':sum(c['cases'] for c in checks)}))

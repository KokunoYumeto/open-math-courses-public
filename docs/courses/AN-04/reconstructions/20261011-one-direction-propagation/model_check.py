"""Finite exact sign, remainder and model identities. CC0-1.0."""
from pathlib import Path
import sympy as s,json,hashlib
root=Path(__file__).resolve().parent;checks=[]
def check(name,a,b):
 d=a-b
 assert (all(s.simplify(q)==0 for q in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0),name
 checks.append({'name':name,'passed':True})
t,lam,beta,eta,delta,x,k,tau=s.symbols('t lam beta eta delta x k tau',real=True)
chi=s.Function('chi')(t);z=s.Function('z')(t);q=s.exp(-lam*t)*chi*z
check('Time commutator sign',q*(-s.I*s.diff(z,t)/z)+s.I*s.diff(q,t),s.I*s.exp(-lam*t)*(s.diff(chi,t)-lam*chi)*z)
chi0,minus,plus,zr,zi=s.symbols('chi0 minus plus zr zi',real=True)
v=zr+s.I*zi
check('Outgoing square real part',s.re(s.exp(-2*lam*t)*plus*chi0*v*s.conjugate(v)),s.exp(-2*lam*t)*plus*chi0*(zr*zr+zi*zi))
q0,br=s.symbols('q0 br',real=True)
check('Imaginary leading commutator',s.re(-s.I*q0*br),0)
check('First regularizer composition cancellation',-s.I*q0*br+s.I*q0*br,0)
r=1/(1+delta*eta**2)
check('First regularizer derivative',s.diff(r,eta),-2*delta*eta/(1+delta*eta**2)**2)
check('Second regularizer derivative',s.diff(r,eta,2),-2*delta/(1+delta*eta**2)**2+8*delta**2*eta**2/(1+delta*eta**2)**3)
check('Regularizer limit',s.limit(r,delta,0),1)
v=s.exp(-beta*t)
check('Scalar damping equation',s.diff(v,t)+beta*v,0)
check('Operator sign check',-s.I*s.diff(v,t)-s.I*beta*v,0)
check('Weighted derivative identity',s.diff(s.exp(-2*lam*t)*v*v,t),-2*(lam+beta)*s.exp(-2*lam*t)*v*v)
A=s.exp(-1/t**2);a=s.diff(A,t)
check('Flat damping coefficient',a,2*t**-3*s.exp(-1/t**2))
u=s.exp(-A*eta)
check('Fourier damping equation',s.diff(u,t),-a*eta*u)
check('Homogeneous solution operator',-s.I*s.diff(u,t)-s.I*a*eta*u,0)
p=tau-s.I*t*t*k*x*x
check('Model real principal part',s.re(p),tau)
check('Model imaginary sign',s.im(p),-t*t*k*x*x)
check('Model homogeneous Euler',tau*s.diff(p,tau)+k*s.diff(p,k),p)
check('Model central value',p.subs({tau:0,x:0,k:1}),0)
check('Model central time Hamilton component',s.diff(p,tau),1)
check('Model central transverse gradient',s.diff(p,x).subs(x,0),0)
check('Model Hessian',s.diff(s.im(p),x,2).subs(k,1),-2*t*t)
check('Model isolated zero Hessian',s.diff(s.im(p),x,2).subs({k:1,t:0}),0)
th=s.symbols('th',real=True)
check('Cubic integral Taylor coefficient',3/s.factorial(3)*s.integrate((1-th)**2*6,(th,0,1)),1)
u1,u2=s.symbols('u1 u2',real=True);F=u1*u1*u2
rhs=0
for aa in range(4):
 bb=3-aa
 rhs+=u1**aa*u2**bb*3/(s.factorial(aa)*s.factorial(bb))*s.integrate((1-th)**2*s.diff(F,u1,aa,u2,bb).subs({u1:th*u1,u2:th*u2}),(th,0,1))
check('Mixed cubic Taylor identity',rhs,F)
sigma,b0=s.symbols('sigma b0',real=True)
check('Sobolev threshold exponent',(2*sigma-2*b0).subs(sigma,b0-s.Rational(1,2)),-1)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'cases':checks,'source_sha256':sha(root/'one-direction-propagation-and-characteristic-strata.md'),'script_sha256':sha(Path(__file__)),'scope':'Finite exact signs, Taylor identities, symbol homogeneity and solution equations. The full analytic estimates, weak limits and geometric statements are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(d,indent=2)+'\n','utf-8');print(json.dumps({'passed':True,'cases':len(checks)}))

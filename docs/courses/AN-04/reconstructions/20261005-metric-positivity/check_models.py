"""Finite checks support, but do not replace, MP's analytic proofs. CC0."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x,xi,lam=s.symbols('x xi lam',real=True)
def bracket(a,b):return s.diff(a,xi)*s.diff(b,x)-s.diff(a,x)*s.diff(b,xi)
def product(a,b,N):
 return s.expand(sum((s.I/2)**k/s.factorial(k)*sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,xi,j)*s.diff(b,x,j,xi,k-j) for j in range(k+1)) for k in range(N)))
checks=[]
a=(1+x*x)*(1+xi*xi);phi=x+x*xi;cs=x*xi
assert s.expand(bracket(phi,a)*phi+bracket(phi*a,phi))==0
checks.append('Scalar triple-product first correction cancels exactly')
assert product(cs,cs,5)==x*x*xi*xi+s.Rational(1,4)
checks.append('Exact scalar square correction has sign +1/4')
u=s.Function('u')(x)
A=lambda v:-s.I*(x*s.diff(v,x)+v/2)
assert s.expand(A(A(u))-u/4-(-x*x*s.diff(u,x,2)-2*x*s.diff(u,x)-u/2))==0
checks.append('Differential operator has constant term -1/2')
L=s.symbols('L',positive=True);t=s.symbols('t',real=True)
v=s.pi**(-s.Rational(1,4))*L**(-s.Rational(1,2))*s.exp(-t*t/(2*L*L))
assert s.integrate(v*v,(t,-s.oo,s.oo))==1
assert s.simplify(s.integrate(s.diff(v,t)**2,(t,-s.oo,s.oo))-1/(2*L*L))==0
checks.append('Gaussian norm and derivative energy agree with exact logarithmic test')
for value in [.5,1,np.sqrt(2),2,5]:
 value=float(value)
 energy=quad(lambda t:t*t*np.exp(-t*t/value**2)/(np.sqrt(np.pi)*value**5),-np.inf,np.inf)[0]-.25
 assert abs(energy-(1/(2*value**2)-.25))<1e-10
checks.append('Independent quadrature confirms zero, negative value and asymptotic approach')
rng=np.random.default_rng(418)
J=np.array([[0.,-1.],[1.,0.]])
for _ in range(40):
 shear=rng.uniform(-3,3);scale=np.exp(rng.uniform(-2,2))
 T=np.array([[scale,0],[shear*scale,1/scale]])
 nu=rng.uniform(.01,1);G=np.linalg.inv(T).T@(nu*np.eye(2))@np.linalg.inv(T)
 Q=J@np.linalg.inv(G)@J.T
 assert np.allclose(T.T@J@T,J)
 assert np.allclose(T.T@G@T,nu*np.eye(2))
 assert np.allclose(np.linalg.eigvals(np.linalg.solve(Q,G)),nu*nu)
checks.append('Symplectic covariance preserves the exact positive-form Planck parameter')
for delta,rho in [(0,1),(.3,.8),(.9,.95)]:
 for _ in range(1000):
  eta=rng.uniform(-100,100);xi0=rng.uniform(-100,100)
  wy=np.hypot(1,eta);wx=np.hypot(1,xi0);d=abs(xi0-eta)/wy**delta
  ratio=max(wx/wy,wy/wx)
  assert np.log(ratio)<=np.log(2)/(1-delta)+np.log1p(d)/(1-delta)+1e-12
checks.append('Classical metric ratio estimate checked at both small and separated frequencies')
# A noncommuting family verifies both actual interaction matrices and conclusion.
ops=[np.array([[1,0],[0,0]],complex),np.array([[0,.2],[.1,0]],complex),np.array([[0,0],[0,.4]],complex)]
left=np.array([[np.linalg.norm(a.conj().T@b,2)**.5 for b in ops] for a in ops])
right=np.array([[np.linalg.norm(a@b.conj().T,2)**.5 for b in ops] for a in ops])
M=max(left.sum(axis=1).max(),right.sum(axis=1).max())
assert np.linalg.norm(sum(ops),2)<=M
for _ in range(20):
 vec=rng.normal(size=2)+1j*rng.normal(size=2)
 total=sum(abs(np.vdot(a@vec,b@vec)) for a in ops for b in ops)
 assert total<=M*M*np.vdot(vec,vec).real+1e-12
checks.append('Both Cotlar interaction matrices checked on a noncommuting finite family')
out={'passed':True,'finite_groups':len(checks),'checks':checks,'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in sorted(ROOT.glob('*.md'))},
 'limitations':'Finite algebra and numerical model checks; analytic completeness is reviewed separately.',
 'general_metric_L2_theorem_included':True,'Fefferman_Phong_operator_theorem_included':True,'U033_restored':False}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

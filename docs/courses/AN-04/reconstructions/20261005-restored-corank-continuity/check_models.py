"""Exact tangent/form checks and independent finite parameter operators."""
import hashlib,json
from pathlib import Path
import sympy as s
import numpy as np
here=Path(__file__).resolve().parent;checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def omega(n):return s.zeros(n).row_join(-s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
def symplectic_change(n):
 P=s.Matrix(n,n,lambda i,j:i+j+1)
 Q=s.diag(*range(1,n+1))
 return s.eye(n).row_join(Q).col_join(s.zeros(n).row_join(s.eye(n)))*s.eye(n).row_join(s.zeros(n)).col_join(P.row_join(s.eye(n)))
splittings=[]
for n1,n2,n in [(3,2,1),(2,2,2),(2,3,1),(1,1,0)]:
 cols=[]
 for j in range(n):
  v=s.zeros(2*n1+2*n2,1);v[j]=v[2*n1+j]=1;cols.append(v)
 for j in range(n):
  v=s.zeros(2*n1+2*n2,1);v[n1+j]=v[2*n1+n2+j]=1;cols.append(v)
 for j in range(n,n1):
  v=s.zeros(2*n1+2*n2,1);v[j]=1;cols.append(v)
 for j in range(n,n2):
  v=s.zeros(2*n1+2*n2,1);v[2*n1+j]=1;cols.append(v)
 G=s.Matrix.hstack(*cols);O1=omega(n1);O2=omega(n2)
 S1=symplectic_change(n1);S2=symplectic_change(n2)
 assert S1.T*O1*S1==O1 and S2.T*O2*S2==O2
 G=s.diag(S1,S2)*G;P1=G[:2*n1,:];P2=G[2*n1:,:]
 assert G.rank()==n1+n2 and G.T*s.diag(O1,-O2)*G==s.zeros(n1+n2)
 sigma=P1.T*O1*P1
 assert sigma==P2.T*O2*P2 and sigma.rank()==2*n
 K1=s.Matrix.hstack(*[P1*v for v in P2.nullspace()]) if P2.nullspace() else s.zeros(2*n1,0)
 K2=s.Matrix.hstack(*[P2*v for v in P1.nullspace()]) if P1.nullspace() else s.zeros(2*n2,0)
 assert K1.rank()==n1-n and K2.rank()==n2-n
 assert K1.T*O1*P1==s.zeros(n1-n,n1+n2)
 assert K2.T*O2*P2==s.zeros(n2-n,n1+n2)
 assert n1+n2-sigma.rank()==K1.rank()+K2.rank()
 splittings.append({'n1':n1,'n2':n2,'shared_n':n,'kernel_dimensions':[K1.rank(),K2.rank()],
  'rank':sigma.rank(),'corank':n1+n2-sigma.rank()})
checks.append({'name':'linear relation splitting after independent symplectic changes',
 'kind':'exact full relation matrices, quotient dimensions and orthogonals',
 'models':splittings,'passed':True})

# Actual pullback of the changing-rank nonlinear canonical relation.
x,z,t,eta=s.symbols('x z t eta',real=True)
output=s.Matrix([x,z,eta,t*t*eta]);input_=s.Matrix([x+z*t*t,t,eta,-2*z*t*eta])
J1=output.jacobian([x,z,t,eta]);J2=input_.jacobian([x,z,t,eta])
sigma=s.simplify(J1.T*omega(2)*J1)
assert s.simplify(sigma-J2.T*omega(2)*J2)==s.zeros(4)
assert sigma.subs({t:0,eta:1}).rank()==2
assert sigma.subs({t:1,eta:1}).rank()==4
R=s.Matrix([0,0,0,eta]);alpha=-sigma*R
assert alpha==s.Matrix([eta,t*t*eta,0,0])
phase=(x+z*t*t)*eta
assert s.diff(phase,x,eta)==1
h=phase-x*eta
assert all(s.diff(h,a,b).subs({x:0,z:0,t:0,eta:1})==0 for a in [x,z,t,eta] for b in [x,z,t,eta])
checks.append({'name':'changing-rank nonlinear relation and partial phase',
 'kind':'exact two independent cotangent pullbacks and full Hessian',
 'ranks_at_t_0_and_1':[2,4],'coranks':[2,0],
 'radial_one_form':'eta dx + t^2 eta dz','zero_two_jet':True,'passed':True})

# Verify the primitive correction and actual Moser flow by differentiating
# the whole coordinate map, not just checking the displayed vector field.
x1,x2,xi1,xi2,eps,tau=s.symbols('x1 x2 xi1 xi2 eps tau',real=True)
u=s.Matrix([x1,x2,xi1,xi2]);O0=omega(2)
beta=s.zeros(4);beta[2,1]=eps*x2;beta[1,2]=-eps*x2
radial=s.Matrix([0,0,xi1,xi2]);alpha=-beta*radial
f=eps*xi1*x2*x2/2;df=s.Matrix([s.diff(f,v) for v in u])
gamma=s.simplify(alpha-df)
assert gamma==s.Matrix([0,0,-eps*x2*x2/2,0])
V=s.Matrix([-eps*x2*x2/2,0,0,0]);Ot=O0+tau*beta
assert s.simplify(-Ot*V+gamma)==s.zeros(4,1)
flow=s.Matrix([x1-tau*eps*x2*x2/2,x2,xi1,xi2]);J=flow.jacobian(u)
assert s.simplify(J.T*Ot*J-O0)==s.zeros(4)
marked={x1:0,x2:0,xi1:1,xi2:0}
assert J.subs(marked)==s.eye(4)
assert gamma.jacobian(u).subs(marked)==s.zeros(4)
assert alpha.jacobian(u).subs(marked)!=s.zeros(4)
checks.append({'name':'homogeneous Moser correction preserves the marked tangent map',
 'kind':'exact primitive jets, contraction and full flow pullback',
 'uncorrected_primitive_first_jet_nonzero':True,
 'corrected_primitive_first_jet_zero':True,'flow_differential_identity':True,'passed':True})

# Normalization/order in actual lifting dimensions, including odd corank.
normalizations=[]
for n1,n2,n in [(2,1,1),(3,2,1),(2,2,2)]:
 k=n1+n2-2*n;m=-s.Rational(k,4)
 amplitude_order=m+s.Rational(n1+n2,4)-s.Rational(n,2)
 assert amplitude_order==0
 kernel_exponent=-s.Rational(n1+n2+2*n,4)
 assert kernel_exponent+n==-s.Rational(k,4)
 normalizations.append({'dimensions':[n1,n2,n],'corank':k,'critical_order':str(m),
  'graph_amplitude_order':str(amplitude_order),'extra_2pi_exponent':str(kernel_exponent+n)})
checks.append({'name':'partial Fourier order and normalization in unequal dimensions',
 'kind':'exact rational density/order calculation','models':normalizations,'passed':True})

# Direct weighted finite operator with a variable family of unitary circle
# rotations. Its norm is compared with the parameter-volume bound.
size=16;wx=np.array([.2,.3,.5]);wy=np.array([.1,.25,.65])
blocks=[]
for i,a in enumerate(wx):
 row=[]
 for j,b in enumerate(wy):
  T=np.roll(np.eye(size),(i+2*j)%size,axis=0)
  row.append(np.sqrt(a*b)*T)
 blocks.append(row)
A=np.block(blocks);actual=np.linalg.norm(A,2);bound=np.sqrt(wx.sum()*wy.sum())
assert actual<=bound+2e-14
constant=np.kron(np.sqrt(wx)[:,None]*np.sqrt(wy)[None,:],np.eye(size))
assert abs(np.linalg.norm(constant,2)-bound)<2e-14
checks.append({'name':'uniform graph family integrated over parameters',
 'kind':'independent weighted rotation matrices and constant-family saturation',
 'actual_norm':float(actual),'volume_bound':float(bound),
 'constant_family_norm':float(np.linalg.norm(constant,2)),'passed':True})

# Actual flat tensor multiplier: identical canonical geometry and distinct
# amplitude orders. Fourier-mode norms expose growth without FIO calculus.
spectral=[];h_norm=2.;ell_norm=3.;k=2
constant=(2*np.pi)**(-k/4)*h_norm*ell_norm
for mu in [0.,1.]:
 norms=[constant*(1+N*N)**(mu/2) for N in [1,4,16,64]]
 if mu==0:assert max(norms)==min(norms)
 else:assert all(norms[j+1]>norms[j] for j in range(len(norms)-1))
 spectral.append({'amplitude_order':mu,'fio_order':mu-k/4,'mode_norms':norms})
checks.append({'name':'flat tensor Fourier model order obstruction',
 'kind':'exact diagonal-mode action','models':spectral,'passed':True})

report={'schema':'corank-finite-check/v1','passed':True,
 'lesson':'corank-geometry-and-sufficient-continuity.md',
 'lesson_sha256':sha(here/'corank-geometry-and-sufficient-continuity.md'),
 'script_sha256':sha(Path(__file__)),'checks':checks,
 'scope':'Bounded exact tangent/phase/flow models and independent finite parameter operators. Not certification of general homogeneous Darboux, FIO continuity or constant-rank sharpness.',
 'independent_mathematical_review':False}
(here/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'finite_checks':len(checks),'lesson_sha256':report['lesson_sha256']}))

"""Finite exact identities for the written clean composition/transport proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 if isinstance(value,bool):assert value,(name,value)
 else:assert s.simplify(value)==0,(name,value)
 checks.append({'name':name,'passed':True})
nx,ny,nz,N1,N2,e,m1,m2,rho=s.symbols('nx ny nz N1 N2 e m1 m2 rho',real=True)
delta=1-rho;eps=2*rho-1;d=nx+nz;N=N1+N2+ny;M=m1+m2+e/2
mu1=m1+(nx+ny-2*N1)/4;mu2=m2+(ny+nz-2*N2)/4
check('joint amplitude/order balance',mu1+mu2-ny-(M+(d-2*N-2*e)/4))
oldpower=-(nx+ny+2*N1)/4-(ny+nz+2*N2)/4
newpower=-(d+2*N-2*e)/4
check('sole Gaussian factor exponent',oldpower-newpower+e/2)
check('intrinsic density degree',
      m1+(nx+ny)/4+m2+(ny+nz)/4+(e-ny)/2-(M+d/4))
check('unequal-frequency integration gain',delta-1+rho)
check('middle auxiliary derivative gain',delta-1+rho)
check('normal stationary derivative loss',-1+2*delta+eps)
for r in [s.Rational(3,5),s.Rational(3,4),s.Integer(1)]:
 check('positive gain at rho='+str(r),bool(2*r-1>0))
 check('subprincipal restriction remainder at rho='+str(r),bool(r-1<=0))
 check('second ordinary term remainder at rho='+str(r),bool(2*r-2<=0))
 check('subprincipal representative error at rho='+str(r),bool(2-r-(2*r-1)>=0))
x1,x2,z1,z2=s.symbols('x1 x2 z1 z2',real=True)
R=s.sqrt(z1*z1+z2*z2);h1=s.diff(R,z1);h2=s.diff(R,z2)
p=x1*x1-h1*h1;pj=x1+h1
S=s.diff(pj,z1);T=s.diff(pj,x1)*s.diff(R,z1,2)
trace=s.diff(p,x1,z1)+s.diff(p,x2,z2)
div=s.diff(2*h1,z1)
check('nonlinear graph vanishing',p.subs(x1,h1))
check('fixed-base derivative versus Hessian',S-T-trace)
check('total graph divergence',S+T-div)
check('half-divergence multiplication coefficient',s.I*S-s.I*trace/2-s.I*div/2)
z=s.symbols('z',positive=True);b=s.Function('b')(z)
actual=s.I*s.diff(z*b,z)
lie=s.I*z*s.diff(b,z)+s.I*b/2
sub=s.I*b/2
check('xDx full transport coefficient',actual-lie-sub)
u=s.symbols('u',positive=True)
check('composition correction exponent',delta-rho+eps)
check('Taylor remainder exponent gap',3*delta-2+2*eps+delta)
check('circle excess output order',-s.Rational(1,4)-s.Rational(1,4)+s.Rational(1,2))
E12=s.Matrix([[0,1],[0,0]]);E21=s.Matrix([[0,0],[1,0]])
t=s.symbols('t',real=True)
UV=s.integrate(s.cos(2*s.pi*t)**2,(t,0,1))*(E12*E21)
for i in range(2):
 for j in range(2):check('ordered compact-fiber entry '+str(i)+str(j),UV[i,j]-(s.Rational(1,2) if i==0 and j==0 else 0))
check('reversed factors give a different entry',bool(E12*E21!=E21*E12))
A=s.Matrix([[1,s.I],[2,-s.I]]);B=s.Matrix([[s.I,3],[1,2]])
for i in range(2):
 for j in range(2):check('finite antidual product entry '+str(i)+str(j),((A*B).conjugate().T-B.conjugate().T*A.conjugate().T)[i,j])
source=HERE/'clean-fourier-integral-composition-and-rho-transport.md'
out={'schema':'AN04-rho-fio-composition-model-check/v1','passed':True,'total_cases':len(checks),
 'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact dimension, Gaussian, derivative-budget, nonlinear graph/divergence, matrix-adjoint, circle-fiber and order identities. Full analytic and distributional proofs are in the lesson.',
 'proof_completeness_certified_by_these_checks':False}
(HERE/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

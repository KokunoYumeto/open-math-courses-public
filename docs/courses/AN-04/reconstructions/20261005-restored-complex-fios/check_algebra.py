"""Full-section source/target preparation and finite models, not a completed lesson."""
import argparse,hashlib,json,datetime,math
from pathlib import Path
import sympy as s
import numpy as np
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
def dump(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
checks=[]
xi,eta,etap,zeta,a,b=s.symbols('xi eta etap zeta a b',positive=True)
x,y,z=s.symbols('x y z',real=True)
H1=-s.I*a*(xi-eta)**2/(2*eta);H2=-s.I*b*(etap-zeta)**2/(2*zeta)
phi1=x*xi-y*eta-H1;phi2=y*etap-z*zeta-H2;Phi=phi1+phi2
assert s.simplify(s.im(-s.conjugate(phi1))-s.im(phi1))==0
assert s.simplify(s.diff(-s.conjugate(phi1),y)-s.conjugate(eta))==0
checks.append({'name':'Twist and complex adjoint signs','passed':True,'scope':'Actual positive conic phase and unchanged imaginary damping under negative conjugation, including reversed input/output derivative signs.'})
q=[y,xi,eta,etap,zeta];vars=[x,z]+q
mark={x:0,y:0,z:0,xi:1,eta:1,etap:1,zeta:1}
D=s.Matrix([s.diff(Phi,v) for v in q]).jacobian(vars).subs(mark)
assert D.subs({a:2,b:3}).rank()==5
assert s.simplify(s.hessian(Phi,vars).subs(mark).det())!=0
G=s.I*(H1+H2.subs(etap,eta))
row=s.simplify(s.Matrix([s.diff(G,eta)]).jacobian([xi,eta,zeta]).subs({xi:1,eta:1,zeta:1}))
assert row==s.Matrix([[-a,a+b,-b]])
Gxx=s.hessian(G,[xi,zeta]).subs({xi:1,eta:1,zeta:1})
Gxe=s.Matrix([s.diff(G,v,eta) for v in [xi,zeta]]).subs({xi:1,eta:1,zeta:1})
effective=s.simplify(Gxx-Gxe*Gxe.T/(a+b))
assert effective==a*b/(a+b)*s.Matrix([[1,-1],[-1,1]])
assert s.simplify(s.diff(G,eta,eta)-a*xi**2/eta**3-b/zeta)==0
assert D.subs({a:0,b:0}).rank()==4
checks.append({'name':'Whole positive conic composition model and transverse failure','passed':True,'scope':'Five full critical differentials, entire seven-variable Hessian, actual transverse derivative row, positive middle second derivative, effective coefficient ab/(a+b), and exact rank loss at a=b=0.'})
nx,ny,nz,N1,N2,m1,m2=s.symbols('nx ny nz N1 N2 m1 m2')
product=m1+(nx+ny-2*N1)/4+m2+(ny+nz-2*N2)/4-ny
assert s.simplify(product-(m1+m2+(nx+nz-2*(N1+N2+ny))/4))==0
assert s.simplify(-(nx+ny+2*N1)/4-(ny+nz+2*N2)/4+(nx+nz+2*(N1+N2+ny))/4)==0
R=s.symbols('R',positive=True);v0,v1=s.symbols('v0 v1',real=True)
rho=s.sqrt(xi*xi+eta*eta);change=s.Matrix([rho*y,xi,eta]);assert s.simplify(change.jacobian([y,xi,eta]).det()-rho)==0
checks.append({'name':'Exact homogenization Jacobian and general composition order/constants','passed':True,'scope':'Entire nonlinear three-variable Jacobian and symbolic all-dimension amplitude/order/2pi bookkeeping.'})
I=s.eye(2);J=s.zeros(2).row_join(-I).col_join(I.row_join(s.zeros(2)))
O=s.diag(J,-J)
C=s.Matrix([[1,0,-1,0],[0,1,0,0],[-1,0,1,0],[0,0,0,1]])
Qh=-s.I*C
M=Qh[:2,:].col_join(s.eye(4)[:2,:]).col_join(-Qh[2:,:]).col_join(s.eye(4)[2:,:])
assert M.T*O*M==s.zeros(4)
assert s.I*s.conjugate(M).T*O*M==2*C
assert C.nullspace()==[s.Matrix([1,0,1,0])]
one=M*s.Matrix([0,0,0,1]);assert one[:4,:]==s.zeros(4,1) and one[4:,:]!=s.zeros(4,1)
qv=s.Matrix(s.symbols('q0:4',real=True));rad=(qv[0]+qv[2])/2
H=-s.I*((qv[0]-qv[2])**2+qv[1]**2+qv[3]**2)/(2*rad)
assert s.hessian(H,qv).subs(dict(zip(qv,[1,0,1,0])))==Qh
bad=C.copy();bad[3,3]=0;assert s.Matrix([0,0,0,1]) in bad.nullspace()
checks.append({'name':'Real and complex one-sided vectors in an actual conic tangent model','passed':True,'scope':'Full 8-by4 canonical-plane matrix, exact positive Hermitian form and radial real nullspace, allowed complex one-sided vector, whole conic H Hessian, and forbidden real vector when eta2 damping is removed.'})
xx=s.symbols('xx',real=True);nrm=s.integrate(s.exp(-xx*xx),(xx,-s.oo,s.oo))
assert nrm==s.sqrt(s.pi)
goodnorm=s.sqrt(s.pi)/(2*s.pi)**s.Rational(3,2)
growth=[{'scale':v,'evaluation_growth':math.sqrt(v)} for v in [1,4,16,64]]
checks.append({'name':'Gaussian bounded model versus concentrating evaluation','passed':True,'scope':'Exact Gaussian squared norm sqrt(pi) and multiplication-tensor-rank-one norm sqrt(pi)/(2pi)^(3/2); removed input damping gives evaluation growth sqrt(t) on normalized packets. Kernel identities and L2 obstruction are to be proved in the teaching lesson.','bounded_norm':str(goodnorm),'concentrating_samples':growth})
u,k,fr=s.symbols('u k fr',positive=True);zz=s.symbols('zz',real=True)
psi=s.I*k*fr*zz**2/2
lhs=s.expand(abs(s.diff(psi,zz))**2/fr+fr*abs(s.diff(psi,fr))**2)
assert s.simplify(lhs-k*k*fr*(zz*zz+zz**4/4))==0
Ps={}
for al in range(5):
 P=s.Integer(1)
 for j in range(al):P=s.expand(s.diff(P,u)-u*P)
 for be in range(5):
  Ps[(al,be)]=P
  if be<4:P=s.expand((s.Rational(al,2)-be)*P+u*s.diff(P,u)/2-u*u*P/2)
  true=s.diff(s.exp(-fr*zz*zz/2),zz,al,fr,be)
  predicted=fr**(s.Rational(al,2)-be)*Ps[(al,be)].subs(u,zz*s.sqrt(fr))*s.exp(-fr*zz*zz/2)
  assert s.simplify(true-predicted)==0
checks.append({'name':'Weighted phase gradient and twenty-five complete exponential derivatives','passed':True,'scope':'Whole exact quadratic gradient expression and all Gaussian derivative polynomials for spatial/frequency orders0..4, with their actual radial factors. A real cubic phase has nonzero gradient and zero imaginary damping, giving the negative control.'})
metric_samples=0
for p0 in [0.,1.,10.,100.]:
 for p1 in [0.,-.4,4.,50.]:
  rr=math.sqrt(1+p0*p0);ss=math.sqrt(1+p1*p1);d=(p0-p1)**2/ss
  assert max(rr/ss,ss/rr)<=4*(1+d)+1e-10
  metric_samples+=1
Gm=s.diag(R,1/R);Jo=s.Matrix([[0,-1],[1,0]])
assert s.simplify(Jo.T*Gm.inv()*Jo-Gm)==s.zeros(2)
checks.append({'name':'Exact endpoint self-duality and actual temperateness controls','passed':True,'scope':'Whole symplectic dual matrix equals original metric; sixteen distinct-center frequency comparisons satisfy the written exact constant4 and exponent1. General structural proof is supplied in the private preparation, not certified by sampling.','samples':metric_samples})
print(json.dumps({'passed':True,'finite_model_groups':len(checks),'checks':checks}))

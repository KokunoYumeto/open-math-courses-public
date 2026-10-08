"""Exact diagnostic models for time mixing, density transport and window scales."""
from pathlib import Path
import hashlib,json,sympy as s
r=Path(__file__).resolve().parent;p=r
x,t,v,rho,theta,eta,xi,tau,zeta=s.symbols('x t v rho theta eta xi tau zeta',real=True)
groups=[]
def zero(expr):assert s.simplify(expr)==0,expr
for lam in [0,1]:
    M=1+lam*x*x;Y=M*v+t*x*x/2;Yx=s.diff(Y,x);Yt=s.diff(Y,t)
    # Old covectors evaluated at F and expressed in the new ones.
    zz=eta/M;tt=theta-Yt*zz;xx=rho-Yx*zz
    old=s.Matrix([x,t,Y,xx,tt,zz]);new=s.Matrix([x,t,v,rho,theta,eta])
    A=old.jacobian(new)
    Omega=s.zeros(6)
    for i in range(3):Omega[i,i+3]=-1;Omega[i+3,i]=1
    error=A.T*Omega*A-Omega
    for entry in error:zero(entry)
    pF=tt*tt-(xx+Yx*zz)**2-zz*zz
    R=(theta-Yt*eta/M)**2-(eta/M)**2
    zero(pF+rho*rho-R)
    zero(R.subs(x,0)-(theta*theta-eta*eta))
    zero(s.diff(R,x).subs(x,0))
groups.append({'name':'full symplectic time-dependent cotangent maps and exact normal symbols',
    'cases':2,'matrix_entries_checked_per_case':36,'passed':True})

# Nonconstant tangential Jacobian: dropping it changes the dual conjugate.
J=1+x*x*v;h=v**3+t*v+1
B=lambda f:-s.I*s.diff(f,v)/J
C=lambda f:J*B(f/J)
zero(C(h)-(B(h)+s.I*s.diff(J,v)*h/J**2))
# C*=B follows from (J^-1 D_v)*=D_v J^-1 and conjugation of the zero-order term.
formal_Cstar=-s.I*s.diff(h/J,v)-s.I*s.diff(J,v)*h/J**2
zero(formal_Cstar-B(h))
assert s.simplify(C(h)-B(h))!=0
groups.append({'name':'variable-density natural-dual action and actual formal adjoint',
    'nontrivial_jacobian':str(J),'cases':3,'passed':True})

cases=0
for sign in [-1,1]:
 for xv in [s.Rational(0),s.Rational(1,8),s.Rational(1,2)]:
  for tv in [-1,0,1]:
   for ratio in [-s.Rational(1,2),s.Rational(1,2)]:
    ta=s.Integer(sign);ze=ta*ratio;th=ta+xv*xv*ze/2
    assert s.sign(th)==sign
    assert abs(th)>=abs(ta)/2 and abs(th)<=3*abs(ta)/2
    assert abs(ze/th-ze/ta)<=xv*xv
    for root_sign in [-1,1]:
     xx=-xv*tv*ze+root_sign*s.sqrt(ta*ta-ze*ze)
     rr=xx+xv*tv*ze
     zero(ta*ta-(xx+xv*tv*ze)**2-ze*ze)
     zero(rr*rr-((th-xv*xv*ze/2)**2-ze*ze))
     assert abs((xv*rr)/abs(th)-(xv*xx)/abs(ta))<=2*xv*xv
     cases+=1
groups.append({'name':'both frequency signs and both characteristic roots under normalization',
    'cases':cases,'passed':True})

cases=0
for D in [s.Rational(1,2),s.Integer(1),s.Integer(2)]:
 for sign in [-1,1]:
  for sv in [s.Rational(1,2),s.Rational(1,4),s.Rational(1,32)]:
   step=sign*sv;analytic_step=-D*step
   assert s.sign(analytic_step)==-sign
   normal=3*D**2*step**2
   tangent=(3*D**2+5)*step**2+7*9*D**4*step**4
   assert normal<=269*step**2 and tangent<=269*step**2
   cases+=1
groups.append({'name':'uniform reversing-clock window constants with quartic coordinate error',
    'cases':cases,'passed':True})

figure=json.loads((p/'figure-check.json').read_text(encoding='utf8'))
u=s.symbols('u',real=True)
for row in figure['exact_model_curves']:
    q=row['bezier_control'];point=s.Matrix(q[0])*(1-u)**2+2*s.Matrix(q[1])*u*(1-u)+s.Matrix(q[2])*u**2
    zero(point[0]-(70+170*(row['v']+u*u/2)))
    zero(point[1]-(306-190*u))
groups.append({'name':'rendered quadratic Bezier paths equal the exact collar graphs',
    'cases':2,'passed':True})
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
record={'schema':'an04-normal-window-models/v1','passed':True,'groups':groups,
    'source_sha256':sha(p/'boundary-normal-coordinates-and-window-transfer.md'),
    'script_sha256':sha(Path(__file__)),'figure_svg_sha256':figure['svg_sha256'],
    'sympy_version':s.__version__,'general_theorem_certificate':False,
    'scope':'Exact finite diagnostic models; the variable-coefficient proof is the complete receiving chapter.'}
(p/'model-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'cases':sum(a['cases'] for a in groups),
    'general_theorem_certificate':False})

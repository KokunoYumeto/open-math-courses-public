"""Exact identities supporting division and affine normal transport. CC0-1.0."""
from pathlib import Path
import sympy as s
import hashlib,json
root=Path(__file__).resolve().parent
t,u,v,w,b,A=s.symbols('t u v w b A',real=True);checks=[]
def check(name,actual,expected=0):
    d=actual-expected
    ok=all(s.simplify(z)==0 for z in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0
    assert ok,(name,d);checks.append(name)
J=s.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
Q=s.diag(2,-2,0,0);F=J*Q;I=s.eye(4);U=I+s.I*A*F
check('Hamilton matrix is symplectic',F.T*J+J*F,s.zeros(4))
check('Quadratic form is preserved infinitesimally',F.T*Q+Q*F,s.zeros(4))
check('Nilpotent transverse matrix',F*F,s.zeros(4))
check('Exact inverse transport',U*(I-s.I*A*F),I)
check('Finite transport preserves quadratic form',U.T*Q*U,Q)
check('Finite transport preserves symplectic form',U.T*J*U,J)
check('Polynomial quadratic division',u**5-(u*u+b)*(u**3-b*u),b*b*u)
check('Opposite quadratic Hessian determinant',s.hessian(u*u-v*v+w**3,[u,v]).det(),-4)
x1,x2,x3,k1,k2,k3=s.symbols('x1 x2 x3 k1 k2 k3',real=True)
z=[x1,x2,x3,k1,k2,k3];p=k1*(x1+s.I*(x2*x2-x3*x3))
hp=s.Matrix([s.diff(p,k) for k in z[3:]]+[-s.diff(p,x) for x in z[:3]])
want=s.Matrix([x1+s.I*(x2*x2-x3*x3),0,0,-k1,-2*s.I*k1*x2,2*s.I*k1*x3])
for j in range(6):check('Radial Hamilton component '+str(j),hp[j],want[j])
gamma={x1:0,x2:0,x3:0,k1:s.exp(-t),k2:0,k3:0}
for j in range(6):check('Radial curve component '+str(j),hp[j].subs(gamma),-s.exp(-t) if j==3 else 0)
qt=s.hessian(s.im(p),[x2,x3,k2,k3]).subs(gamma)
check('Radial Hessian',qt,s.exp(-t)*Q)
check('Radial affine derivative',s.diff(-s.exp(-t),t),s.exp(-t))
check('Reparameterized primitive',s.diff(t+4*t**3/3,t),1+4*t*t)
check('Normalized affine scaling',(2*t)+(2*t)**3/3,2*(t+4*t**3/3))
q=2+s.I+(1+2*s.I)*x2
qm=s.hessian(s.im(s.expand(q*p/(2+s.I))),[x2,x3,k2,k3]).subs(gamma)
check('Complex multiplier Hessian invariance',qm,qt)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'cases':checks,
 'source_sha256':sha(root/'indefinite-quadratic-division-and-affine-parameters.md'),'script_sha256':sha(Path(__file__)),
 'scope':'Finite algebraic identities. The smooth gluing, sign positivity, invariant transport and quotient topology are proved in the lesson.'}
(root/'model-check.json').write_text(json.dumps(r,indent=2)+'\n','utf-8');print(json.dumps({'passed':True,'cases':len(checks)}))

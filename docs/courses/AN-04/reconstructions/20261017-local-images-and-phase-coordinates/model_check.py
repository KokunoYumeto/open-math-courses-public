"""Exact algebra checks for the written projection and reduction examples."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,expression):
    if isinstance(expression,s.MatrixBase):ok=all(s.simplify(v)==0 for v in expression)
    else:ok=s.simplify(expression)==0
    assert ok,(name,expression)
    checks.append(name)
a,u,v,r,t,q,p=s.symbols('a u v r t q p',real=True)
rho,theta1=s.symbols('rho theta1',positive=True)
theta2=s.symbols('theta2',real=True)
J=s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
frame=s.Matrix([[a,0],[1,0],[0,1],[0,-a]])
check('full Lagrangian-plane pairing',frame.T*J*frame)
check('a-independent full frame minor',frame[[1,2],:].det()-1)
check('nonzero-parameter matching constraint',frame[3,1]+a)
check('zero-parameter reduction is vertical',frame.subs(a,0)[0,:])
check('reduced line projection jump norm squared',(s.diag(1,-1).T*s.diag(1,-1))-s.eye(2))
cusp=s.Matrix([3*t**2,-2*t**3,t*rho,rho])
check('cusp exact primitive',cusp[2]*s.diff(cusp[0],t)+cusp[3]*s.diff(cusp[1],t))
check('semicubical base equation',(cusp[0]/3)**3-(cusp[1]/2)**2)
check('cusp lifted frequency Jacobian',cusp.jacobian([t,rho])[[2,3],:].det()-rho)
check('cusp base differential at zero',cusp[:2,0].jacobian([t]).subs(t,0))
mixed=s.Matrix([-s.Rational(3,4)*t**4,t**3,rho,t*rho])
check('mixed example exact primitive',mixed[2]*s.diff(mixed[0],t)+mixed[3]*s.diff(mixed[1],t))
check('mixed lift embedding minor',mixed.jacobian([t,rho])[[2,3],:].det()+rho)
check('mixed projection Jacobian',mixed[[1,2],:].jacobian([t,rho]).det()-3*t**2)
H=theta2**4/(4*theta1**3)
check('full frequency first derivative',s.diff(H,theta1)+3*theta2**4/(4*theta1**4))
check('full frequency second derivative',s.diff(H,theta2)-theta2**3/theta1**3)
check('frequency Euler identity',theta1*s.diff(H,theta1)+theta2*s.diff(H,theta2)-H)
check('frequency Hessian at the marked ray',s.hessian(H,(theta1,theta2)).subs(theta2,0))
phase=q*theta1+p*theta2-H
check('two-variable phase has independent critical equations',s.Matrix([s.diff(phase,theta1),s.diff(phase,theta2)]).jacobian([q,p])-s.eye(2))
hp=s.exp(-1/q)
DF=s.Matrix([[1,0],[s.diff(hp,q),1]])
J2=s.Matrix([[0,-1],[1,0]])
check('ordinary graph shift is symplectic',DF.T*J2*DF-J2)
check('ordinary graph shift determinant',DF.det()-1)
check('positive-side flat-function derivative',s.diff(hp,q)-s.exp(-1/q)/q**2)
out={'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256((ROOT/'local-images-compact-fibers-and-phase-coordinates.md').read_bytes()).hexdigest(),
 'scope':'Exact finite algebra for the written examples. Smoothness at the flat endpoint, properness, topology and the bundle theorem are proved in the text.'}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

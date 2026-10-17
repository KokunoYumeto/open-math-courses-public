"""Exact finite checks of noninjective frames and partial-isometry identities."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).parent;checks=[]
def check(name,ok):
 assert bool(ok),name
 checks.append(name)
J=s.Matrix([[1,0,0],[0,s.Rational(1,2),0]])
D=s.diag(s.Rational(3,5),s.Rational(4,5))
theta2=s.diag(1,s.Rational(1,4),0)
T=J.T*D**2*J;SY=s.diag(s.Rational(3,5),s.Rational(2,5),0)
V=s.Matrix([[1,0,0],[0,1,0]]);P=s.diag(1,1,0)
check('cutoff frame has the actual squared multiplier',J.T*J==theta2)
check('cutoff frame is noninjective',J*s.Matrix([0,0,1])==s.zeros(2,1))
check('noninjective root has the correct square',SY**2==T)
check('partial isometry keeps only the correct domain',V.T*V==P and V.T*V!=s.eye(3))
check('actual polar factor survives the kernel',V*SY==D*J)
R=s.Matrix([[2,0,0],[-3,0,0]]);B=R*J.T*D.inv()
check('input cutoff gives exact complete right cancellation',B*D*J==R and R*theta2==R)
alpha=s.diag(1,1,s.Rational(1,2))
check('larger support frame reconstructs the root',alpha*SY*alpha==SY)
check('original cutoff frame would not reconstruct the root',theta2*SY*theta2!=SY)
B1=s.Matrix([[2,1,0]]);B2=s.Matrix([[0,1,3]])
Q=B1.T*B1+B2.T*B2;f=s.Matrix(s.symbols('a b c',real=True))
check('positive global test keeps the full quadratic identity',s.expand((f.T*Q*f)[0]-(B1*f)[0]**2-(B2*f)[0]**2)==0)
d=s.symbols('d',positive=True)
check('squaring loses the controlling norm',s.simplify(d/(d*d))==1/d)
source=root/'global-finite-order-families-and-residual-tests.md'
(root/'model-check.json').write_text(json.dumps({'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Finite supporting identities and false-shortcut checks; the analytic proof is in the lesson.'},indent=2)+'\n','utf-8')
print({'passed':True,'exact_checks':len(checks)})

"""Finite exact checks of atlas division, polar factor and reciprocal algebra.

These checks support examples and identities; the infinite-dimensional proof
and the full-kernel estimates are in the lesson.
"""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).parent
checks=[]
def check(name,ok):
 assert bool(ok),name
 checks.append(name)
J=s.Matrix([[1,0],[0,1],[1,0],[0,1]])/s.sqrt(2)
D=s.diag(1,2,3,4)/4
T=J.T*D**2*J
S=s.diag(s.sqrt(5)/4,s.sqrt(10)/4)
V=D*J*S.inv()
R=s.Matrix([[2,-3],[5,7]])
B=R*J.T*D.inv()
check('overlapping frame isometry',s.simplify(J.T*J)==s.eye(2))
check('adjoint has a kernel',J.T*s.Matrix([1,0,-1,0])==s.zeros(2,1))
check('positive square root has correct square',s.simplify(S**2-T)==s.zeros(2))
check('auxiliary polar factor is isometric',s.simplify(V.T*V)==s.eye(2))
check('complete rectangular right division',s.simplify(B*D*J)==R)
check('scalar root retains exact factorization',s.simplify(B*V*S)==R)
z=s.symbols('z');F=1
for n in range(1,13):
 c0=s.binomial(2*n-2,n-1)/4**(n-1);c1=s.binomial(2*n,n)/4**n
 F-=(c0-c1)*z**n
check('all root product coefficients through degree twelve',s.series(F**2-(1-z),z,0,13).removeO()==0)
n=s.symbols('n',integer=True,nonnegative=True)
check('central binomial induction margin',s.expand(4*(n+1)**3-(2*n+1)**2*(n+2))==3*n+2)
x=s.symbols('x');p=s.Function('p')(x)
check('second reciprocal derivative',s.simplify(s.diff(1/p,x,2)-(2*s.diff(p,x)**2/p**3-s.diff(p,x,2)/p**2))==0)
check('ratio R=log2',s.exp(s.log(2))==2 and s.exp(-s.log(2))==s.Rational(1,2))
source=root/'global-scalar-factors-for-boundary-residuals.md'
(root/'model-check.json').write_text(json.dumps({'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Finite exact supporting identities only; no numerical certification of the analytic theorem.'},indent=2)+'\n','utf-8')
print({'passed':True,'exact_checks':len(checks)})

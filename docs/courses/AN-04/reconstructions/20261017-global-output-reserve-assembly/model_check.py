"""Exact norm, density and cancellation checks supporting the scalar proof."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).parent;checks=[]
def check(name,ok):
 assert bool(ok),name
 checks.append(name)
L=s.zeros(3,7);L[0,0]=1/s.sqrt(2);L[1,0]=1/s.sqrt(2);L[2,1]=1
V=s.zeros(7,3);V[4,0]=1;V[5,1]=1;V[6,2]=1
W=V*L;alpha=s.diag(1,1,0,0,0,0,0)
S=s.diag(2,3,0,0,0,0,0);Q=s.diag(5,7,11,0,0,0,0)
A=Q+W*S
check('disjoint box isometries retain all frame components',V.T*V==s.eye(3))
check('overlapping source frame has exact cutoff norm',s.simplify(L.T*L)==alpha)
check('encoding recovers the complete residual range',s.simplify(W.T*W*S)==S)
check('full output supports are orthogonal',Q.T*W*S==s.zeros(7))
check('one scalar matrix recovers both norm squares',s.simplify(A.T*A-Q.T*Q-S.T*S)==s.zeros(7))
check('decoded full residual is unchanged',s.simplify(W.T*(W*S))==S)
aa,ll,fp=s.symbols('a ell Fprime',positive=True)
check('density and affine Jacobian cancel',s.simplify((aa**s.Rational(-1,2)*ll**s.Rational(-1,2)*s.sqrt(fp))**2*aa*ll)==fp)
bb,cc=s.symbols('b c',positive=True)
check('flat constant mode normalization',s.simplify(s.sqrt(2*s.pi/cc)*bb/s.sqrt(2*s.pi))==bb/s.sqrt(cc))
q=s.diag(1,0);ss=s.diag(0,1);ww=s.Matrix([[0,-1],[0,0]]);f=s.Matrix([1,1])
check('range isometry alone allows exact cancellation',(ww*ss).T*(ww*ss)==ss.T*ss and (q+ww*ss)*f==s.zeros(2,1))
check('example boxes are separated',s.Rational(1,3)<s.Rational(2,3) and s.Rational(1,6)>0 and s.Rational(5,6)<1)
source=root/'one-scalar-test-with-a-global-boundary-output-reserve.md'
(root/'model-check.json').write_text(json.dumps({'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Finite exact supporting norm, density and false-shortcut checks; full class membership and analytic proof are in the lesson.'},indent=2)+'\n','utf-8')
print({'passed':True,'exact_checks':len(checks)})

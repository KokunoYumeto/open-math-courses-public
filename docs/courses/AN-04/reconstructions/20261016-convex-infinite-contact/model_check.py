"""Exact identities supporting, but not replacing, the convex billiard proof."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,expr):
    assert s.simplify(expr)==0,(label,expr)
    checks.append(label)
j=s.symbols('j',positive=True,integer=True)
m,b,c,theta,d=s.symbols('m b c theta d',real=True)
check('exact interval length',1/j-1/(j+1)-1/(j*(j+1)))
check('prescribed interpolation mean',c+(b-c)*(m-c)/(b-c)-m)
alpha,beta=s.symbols('alpha beta',real=True)
v=s.Matrix([s.cos(alpha),s.sin(alpha)])
T=s.Matrix([s.cos(beta),s.sin(beta)])
w=2*(v.dot(T))*T-v
for k,val in enumerate([s.cos(2*beta-alpha),s.sin(2*beta-alpha)]):
    check('reflected unit vector component '+str(k),s.trigsimp(s.expand_trig(w[k]-val)))
check('equal tangential covector',s.trigsimp(w.dot(T)-v.dot(T)))
check('opposite unit normal component',s.trigsimp(s.expand_trig(
    (w[1]+v[1])*s.cos(beta)-(w[0]+v[0])*s.sin(beta))))
h,k=s.symbols('h k',real=True)
xi=(1+h*h)**s.Rational(-1,2);eta=h*xi
check('gliding characteristic energy',xi*xi+eta*eta-1)
check('gliding tangency',eta-h*xi)
check('gliding xi derivative',s.diff(xi,h)*k*xi+k*h/(1+h*h)**2)
check('gliding eta derivative',s.diff(eta,h)*k*xi-k/(1+h*h)**2)
# The second constraint is eta-h*xi=0, hence eta'-h*xi'-k*xi^2=0.
check('full differentiated gliding constraint',k/(1+h*h)**2+h*k*h/(1+h*h)**2-k*xi*xi)
check('one-third limiting interpolation mean',(1-s.Rational(3,4))/(s.Rational(3,2)-s.Rational(3,4))-s.Rational(1,3))
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256((ROOT/'convex-billiards-at-infinite-contact.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Finite exact algebra only; smooth flatness, convergence and existence are proved in the lesson.'}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

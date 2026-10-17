"""Exact algebra supporting the analytic proofs; not a replacement for them."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
x,t,v,N,M,q=s.symbols('x t v N M q',positive=True)
c=s.Function('c');checks=[]
def check(name,value):
 assert value,name
 checks.append(name)
check('Two output log derivatives: x Cx + x^2 Cxx',
 s.simplify(s.diff(c(s.exp(v)),v,2).subs(v,s.log(x))-(x*s.diff(c(x),x)+x**2*s.diff(c(x),x,2)))==0)
check('Both Schur marginals have finite majorant integral',s.integrate(1/(1+t**2),(t,-s.oo,s.oo))==s.pi)
w0,w1=s.symbols('w0 w1',positive=True)
check('Forward and inverse log density factors cancel',s.simplify(s.sqrt(t*w0/w1)*s.sqrt(w1/w0)/s.sqrt(t))==1)
k=s.Function('k');xp=s.symbols('xp',positive=True)
check('Two input ratio derivatives cost exactly two powers',s.simplify(s.diff(x**-1*k(xp/x),xp,2)-x**-3*s.Subs(s.diff(k(t),t,2),t,xp/x))==0)
check('Chosen residual weight leaves output exponent one',s.simplify((N-1-M-q).subs(N,M+q+2))==1)
a,b,d=s.symbols('a b d');p=a+b*x+d*x**2
check('Front coefficient factorials recover all polynomial coefficients',[s.diff(p,x,j).subs(x,0)/s.factorial(j) for j in range(3)]==[a,b,d])
check('Taylor integral gives the exact quadratic error',s.integrate((1-t)*s.diff(p,x,2),(t,0,1))*x**2==d*x**2)
e=s.symbols('e',positive=True)
check('Weighted differential scaling relative to input L2',s.simplify(e**N*e**-1*s.sqrt(e)/s.sqrt(e)-e**(N-1))==0)
y=s.symbols('y',real=True)
check('Circle constant mode has exact norm one',s.integrate(1/(2*s.pi),(y,0,2*s.pi))==1)
source=HERE/'normal-fiber-bounds-and-finite-front-jets.md'
result={'passed':True,'exact_checks':len(checks),'checks':checks,
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'analytic_proofs_in_lesson':True,'analytic_theorem_proved_by_finite_checks':False}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps(result))

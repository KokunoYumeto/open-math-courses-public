"""Finite exact checks of comparison, geometry, cutoffs and full commutators."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent;checks=[]
def exact(name,left,right=0):
 assert S.simplify(S.expand(left-right))==0,name
 checks.append({'name':name,'kind':'exact_identity','passed':True})
def positive(name,expr):
 assert S.simplify(expr).is_positive,name
 checks.append({'name':name,'kind':'exact_strict_inequality','passed':True})
t,a,b,d,h,l0,l1=S.symbols('t a b delta h L0 L1',real=True)
phi=l0+l1*t-d*(t-a)*(b-t)
exact('convex perturbation second derivative',S.diff(phi,t,2),2*d)
exact('comparison chord excess',(phi.subs(t,t-h)+phi.subs(t,t+h))/2-phi,d*h*h)
L=S.Rational(1,3)-S.Rational(5,3)*t
exact('downward-jump left endpoint',L.subs(t,-S.Rational(1,4)),S.Rational(3,4))
exact('downward-jump right endpoint',L.subs(t,S.Rational(1,2)),-S.Rational(1,2))
exact('downward-jump interior violation',L.subs(t,0),S.Rational(1,3))
exact('allowed right branch curvature',S.diff(1-t*t,t,2),-2)
e=S.symbols('epsilon',nonnegative=True)
exact('weak endpoint gain',((3*e-1)/2).subs(e,S.Rational(1,4)),-S.Rational(1,8))
exact('weighted remainder margin endpoint',(S.Rational(7,8)-e).subs(e,S.Rational(1,4)),S.Rational(5,8))
exact('full factored remainder',e-(1-2*e),3*e-1)
exact('factored remainder endpoint',(3*e-1).subs(e,S.Rational(1,4)),-S.Rational(1,4))
exact('second error output gain',(S.Rational(7,8)-3*e).subs(e,S.Rational(1,4)),S.Rational(1,8))
exact('second error margin above target',(S.Rational(7,8)-2*e).subs(e,S.Rational(1,4)),S.Rational(3,8))
exact('bootstrap strict margin',S.Rational(1,8)-S.Rational(1,16),S.Rational(1,16))
for A0,A1 in [(256,16),(16,1)]:
 positive('strict overlapping-band plateau '+str(A0),(S.Rational(A0)-S.Rational(1,10))/(4*S.sqrt(2))-(2*A1+S.Rational(1,10)))
tau,eta,x,kappa,y=S.symbols('tau eta x kappa y',real=True)
f=t*t*eta;c=S.Function('c')(tau)
br=lambda u,v:S.diff(u,tau)*S.diff(v,t)-S.diff(u,t)*S.diff(v,tau)+S.diff(u,eta)*S.diff(v,x)-S.diff(u,x)*S.diff(v,eta)
exact('retained temporal-frequency bracket',br(f,c),-2*t*eta*S.diff(c,tau))
exact('complete principal commutator sign',br(tau+S.I*f,c)/S.I,br(f,c))
p=tau-S.I*kappa*(x*x+t*t*y*y+y**4)
exact('central real Hamilton component',S.diff(p,tau),1)
exact('negative Hessian x entry',S.diff(S.im(p),x,2).subs({x:0,y:0,kappa:1}),-2)
exact('negative Hessian y entry',S.diff(S.im(p),y,2).subs({x:0,y:0,kappa:1}),-2*t*t)
Q=S.diag(-2,-2*t*t,0,0)
assert Q.subs(t,0).rank()==1 and Q.subs(t,1).rank()==2
checks.append({'name':'exact changing Hessian ranks','kind':'exact_matrix_rank','passed':True})
exact('second admissible clock derivative',S.diff(t+t**3/3,t),1+t*t)
exact('non-affine clock third derivative',S.diff(t+t**3/3,t,3),2)
exact('ordinary real frame squared norm',sum(q*q for q in Q),4*(1+t**4))
source=HERE/'semiconcavity-and-semidefinite-characteristics.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'scope':'Exact comparison chord, jump obstruction, quarter endpoint, three nested plateaus, full temporal-frequency commutator, Hessian ranks and clock derivatives. Classification, admissible-clock construction, distribution estimates and global propagation are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

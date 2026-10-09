"""Exact checks of the normal jets, commutator coefficients and source substitution. CC0."""
from pathlib import Path
import hashlib,json
import sympy as s
PTH=Path(__file__).resolve().parent
checks=[]
def ck(name,expr):
 if isinstance(expr,s.MatrixBase):ok=all(s.simplify(x)==0 for x in expr)
 else:ok=s.simplify(expr)==0
 assert ok,(name,expr)
 checks.append({'name':name,'passed':True})
q,t,eta,sigma=s.symbols('q t eta sigma',real=True)
D=lambda f:-s.I*s.diff(f,q)
Dt=lambda f:-s.I*s.diff(f,t)
def T(a,f):
 p=s.Poly(s.expand(a),sigma);out=0
 for (j,),coef in p.terms():out+=coef*q**j*(-s.I)**j*s.diff(f,q,j)
 return s.expand(out)
a=1+q+q**3+(2-q+q**2)*sigma+(1+q**2)*sigma**2
u=s.Function('u')(q)
e=-s.I*s.diff(a,q);n=-s.I*s.diff(a,sigma)
e0=-s.I*s.diff(e,q);em=-s.I*s.diff(e,sigma)
nm=-s.I*s.diff(n,q);nmm=-s.I*s.diff(n,sigma)
ck('full first normal commutator',D(T(a,u))-T(a,D(u))-T(e,u)-T(n,D(u)))
M=2*n+nmm
ck('full second normal commutator',D(D(T(a,u)))-T(a,D(D(u)))-T(M,D(D(u)))-T(2*e+em+nm,D(u))-T(e0,u))
ck('minus-two correction retained',nmm+2*(1+q**2))
u0,u1,u2,u3=s.symbols('u0 u1 u2 u3')
poly=u0+q*u1+q**2*u2+q**3*u3
for k in range(3):
 rhs=0
 for j in range(k+1):
  akj=sum(s.binomial(j,i)*(-s.I)**(k-j+i)*s.diff(a,q,k-j,sigma,i) for i in range(j+1))
  rhs+=s.binomial(k,j)*akj.subs({q:0,sigma:0})*((-s.I)**j*s.diff(poly,q,j)).subs(q,0)
 ck('exact compressed jet order '+str(k),((-s.I)**k*s.diff(T(a,poly),q,k)).subs(q,0)-rhs)
aflat=1+2*sigma+sigma**2
ck('constant normal input stays Neumann for flat normal symbol',D(T(aflat,1+q**2)).subs(q,0))
ck('normal symbol derivative creates the forbidden value term',D(T(a,1+q**2)).subs(q,0)+s.I)
ck('boundary velocity multiplier includes D_sigma term',(aflat-s.I*s.diff(aflat,sigma)).subs(sigma,0)-(1-2*s.I))
v=s.exp(-q**2)*s.cos(t)
L=lambda f:s.diff(f,t,2)-s.diff(f,q,2)
for chi,label,wanted in [(1+q**2,'flat boundary jet',0),(1+q,'nonzero boundary jet',s.cos(t))]:
 ck(label,s.diff(chi*v,q).subs(q,0)-wanted)
ck('quadratic multiplier full bulk error',L((1+q**2)*v)-(1+q**2)*L(v)-(8*q**2-2)*v)
ck('linear multiplier full bulk error',L((1+q)*v)-(1+q)*L(v)-4*q*v)
Pc=lambda f:D(D(f))-(1+q)*Dt(Dt(f))
B=lambda f:q*s.diff(f,q)
vv=s.Function('v')(q,t)
ck('dilation commutator',Pc(B(vv))-B(Pc(vv))-2*D(D(vv))-q*Dt(Dt(vv)))
ck('equation substitution in dilation model',Pc(B(vv))-B(Pc(vv))-2*Pc(vv)-(2+3*q)*Dt(Dt(vv)))
x,y=s.symbols('x y',real=True);lam2=1+x*x+y*y
ck('Y-minus-one decomposition',1/lam2+x*x/lam2+y*y/lam2-1)
ck('exact sum of representation norm weights',1/lam2**2+x*x/lam2**2+y*y/lam2**2-1/lam2)
# A noncommuting matrix source multiplication keeps the displayed derivative order.
A=s.Matrix([[0,1],[0,0]]);C=s.Matrix([[0,0],[1,0]])
Sinv=s.eye(2)-t*A;F=s.Matrix([1+t**2,2-t])
ck('matrix source divergence transfer',Sinv*Dt(F)-(Dt(Sinv*F)-Dt(Sinv)*F))
ck('test matrices do not commute',A*C-C*A-s.diag(1,-1))
ck('normal kernel upper support endpoint',2*s.Rational(1,3)-s.Rational(2,3))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(PTH/'boundary-preserving-localization-of-weak-sources.md'),'script_sha256':sha(Path(__file__)),
 'checks':checks,'polynomial_symbols_check_algebra_only_not_order_zero_bounds':True,'finite_checks_are_not_the_analytic_proof':True}
(PTH/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))

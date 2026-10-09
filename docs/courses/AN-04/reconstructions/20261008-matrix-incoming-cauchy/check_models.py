"""Exact checks of signs, matrix order, interface terms and energy extensions. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s
P=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
 if isinstance(expr,s.MatrixBase):ok=all(s.simplify(v)==0 for v in expr)
 else:ok=s.simplify(expr)==0
 assert ok,(name,expr)
 checks.append({'name':name,'passed':True})
t,q,z=s.symbols('t q z',real=True)
A=s.Matrix([[0,1],[0,0]]);B=s.Matrix([[0,0],[1,0]]);I=s.eye(2)
cs=[I]
for k in range(3):cs.append((-A*cs[k]-(B*cs[k-1] if k else s.zeros(2)))/(k+1))
V=sum((c*t**k for k,c in enumerate(cs)),s.zeros(2))
check('ordered cubic recurrence',cs[3]-(-A**3+A*B+2*B*A)/6)
check('noncommuting exponential error',cs[3]-(-A**3/6+(A*B+B*A)/4)-(B*A-A*B)/12)
check('commutator is nonzero diagonal',B*A-A*B-s.diag(-1,1))
for k in range(3):check('ODE residual degree '+str(k),(V.diff(t)+(A+t*B)*V).applyfunc(lambda v:s.expand(v).coeff(t,k)))
a=s.Integer(2);beta=s.Matrix([0,s.Rational(1,3)]);Asp=s.diag(1,s.Rational(5,4));xi=s.Matrix([q,z]);Gsp=a*beta*beta.T-Asp
G=s.zeros(3);G[0,0]=a;G[0,1:]=a*beta.T;G[1:,0]=a*beta;G[1:,1:]=Gsp
for ep in [-1,1]:
 lam=-(beta.dot(xi))+ep*s.sqrt((xi.dot(Asp*xi))/a)
 v=s.Matrix([lam,q,z]);check('principal characteristic root '+str(ep),(v.T*G*v)[0])
T=s.eye(3);T[0,1:]=-beta.T
check('full time-square congruence',T.T*G*T-s.diag(a,-1,-s.Rational(5,4)))
check('fixed normalized q blocks',s.Matrix([G[1,1]+1,G[0,1],G[1,2]]))
j=s.symbols('j',integer=True,positive=True);c=s.symbols('c',positive=True)
check('ordered simplex induction',s.integrate(c*(c*t)**(j-1)/s.factorial(j-1),(t,0,1))-c**j/s.factorial(j))
# Test the interface identity against nonconstant coefficients and a compact-test jet.
# The test may be replaced by any compact smooth function with these jets at zero.
h0=1+q**2;h1=2-q;aa=3+t+t**2;gg=1+q+t;bb=2-t
phi=1+2*t+3*t**2
direct=-h0*s.diff(aa*phi,t).subs(t,0)+h1*(aa*phi).subs(t,0)+2*gg.subs(t,0)*s.diff(h0,q)*phi.subs(t,0)+bb.subs(t,0)*h0*phi.subs(t,0)
pred=-aa.subs(t,0)*h0*s.diff(phi,t).subs(t,0)+(aa.subs(t,0)*h1+2*gg.subs(t,0)*s.diff(h0,q)+(bb.subs(t,0)-s.diff(aa,t).subs(t,0))*h0)*phi.subs(t,0)
check('variable coefficient delta-prime pairing',direct-pred)
# Nilpotent time-dependent gauge: exact matrix inverse and actual derivative.
S=I+t*A;Si=I-t*A;U=s.Matrix([1+t+t**2,2-t+t**3]);u=Si*U
check('gauge inverse',Si*S-I)
check('gauge initial velocity with mandatory lower term',u.diff(t).subs(t,0)-(Si*U.diff(t)-Si*S.diff(t)*Si*U).subs(t,0))
check('normalization time square includes cross term',(s.Matrix([t,q,z]).T*G*s.Matrix([t,q,z]))[0]-(a*(t+beta.dot(xi))**2-xi.dot(Asp*xi)))
check('half-space energy norm',s.integrate(2*s.exp(-2*q),(q,0,s.oo))-1)
check('even extension energy norm',2*s.integrate(2*s.exp(-2*q),(q,0,s.oo))-2)
# For e^{-t}, direct convergent integration gives <d^2 t_+,phi>=1,
# and <d^2 t_+^2,phi>=2 integral_0^infty phi=2.
check('value-only matching leaves unit delta',s.integrate(t*s.exp(-t),(t,0,s.oo))-1)
check('two jets matched: ordinary Heaviside source',s.integrate(t**2*s.exp(-t),(t,0,s.oo))-2)
check('conormal Dq factor',(-s.I)*s.I-1)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(P/'matrix-cauchy-evolution-and-causal-boundary-split.md'),'script_sha256':sha(Path(__file__)),
 'checks':checks,'finite_checks_are_not_the_analytic_proof':True}
(P/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))

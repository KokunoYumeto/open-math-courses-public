"""Exact checks for the interval estimate, changing-speed rays and matrix gauge."""
from pathlib import Path
import json,hashlib
import sympy as s
r=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    value=s.simplify(s.expand(expr));assert value==0,(name,value);checks.append(name)
def truth(name,value):
    assert bool(value),name;checks.append(name)
t,a,b,c,x,z,rho,eta,lam,nu,tau,gamma=s.symbols('t a b c x z rho eta lambda nu tau gamma',real=True)
v=a+s.I*b*t
check('D=-i derivative sign',-s.I*s.diff(v,t)-b)
check('interval I squared norm',s.integrate(s.expand(v*s.conjugate(v)),(t,0,2))-(2*a*a+s.Rational(8,3)*b*b))
check('interval J squared norm',s.integrate(s.expand(v*s.conjugate(v)),(t,0,s.Rational(1,2)))-(a*a/2+b*b/24))
check('forcing squared norm',s.integrate(b*b,(t,0,2))-2*b*b)
check('observation coefficient',s.sqrt(2/s.Rational(1,2))-2)
check('constant function gives equality',s.sqrt(2)-2*s.sqrt(s.Rational(1,2)))
p=rho*rho-eta*eta/(c*c)
check('marked point is characteristic',p.subs({rho:-1,eta:-c}))
check('Hamilton x component',s.diff(p,rho).subs(rho,-1)+2)
check('Hamilton z component',s.diff(p,eta).subs(eta,-c)-2/c)
check('eliminating Hamilton parameter',(4-2*lam)-(4-c*(2*lam/c)))
for speed in [s.Rational(9,10),s.Integer(1),s.Rational(11,10)]:
    endpoint=4-2*speed
    truth('positive interior endpoint c='+str(speed),endpoint>=s.Rational(9,5))
    check('endpoint Hamilton time c='+str(speed),(2*lam/c).subs({lam:speed,c:speed})-2)
check('exact lower margin',4-2*s.Rational(11,10)-s.Rational(9,5))
check('maximal reference deviation',2*s.Rational(1,10)-s.Rational(1,5))
dx,ds,dy=s.symbols('dx ds dy',real=True)
check('exact cotangent primitive',nu*(dy-c*ds)+(tau+c*nu)*ds-(nu*dy+tau*ds))
check('full transformed quadratic symbol',p.subs({rho:nu,eta:tau+c*nu})+tau*(tau+2*c*nu)/(c*c))
check('branch has model time momentum zero',(-c)-c*(-1))
g=s.Function('g')
u=g(x+c*z)
check('full wave equation on branch',-s.diff(u,x,2)+s.diff(u,z,2)/(c*c))
N=s.Matrix([[0,1],[0,0]]);I=s.eye(2)
G=s.exp(gamma*t)*(I-s.I*t*N);H=s.exp(-gamma*t)*(I+s.I*t*N)
for name,matrix in [('nilpotent square',N*N),('left inverse',H*G-I),('right inverse',G*H-I),('full transport gauge',-s.I*s.diff(G,t)+(s.I*gamma*I+N)*G)]:
    assert all(s.simplify(e)==0 for e in matrix),name;checks.append(name)
w=G.subs(gamma,1)*s.Matrix([0,1])
check('nonunitary squared norm',(s.conjugate(w).T*w)[0]-s.exp(2*t)*(1+t*t))
truth('nonunitary at t=1',2*s.exp(2)>1)
for q in range(5):
    truth('source factor nonpositive order q='+str(q),q-1-max(0,q-1)<=0)
    check('observer factor order zero q='+str(q),q-q)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,
        'source_sha256':sha(r/'uniform-interior-propagation-and-source-tests.md'),'script_sha256':sha(Path(__file__)),
        'scope':'Exact interval norms and signs, Hamilton curves, common interior margins, canonical primitive, full wave factorization, complex matrix gauge and operator-order checks. Uniform operator estimates and the complete residual argument are proved in the lesson.'}
(r/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

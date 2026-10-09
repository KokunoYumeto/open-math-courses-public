"""Exact checks for the incoming boundary trace models; CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent
q,u,r,rho,lam,C,j=s.symbols('q u r rho lam C j',positive=True)
sigma=s.symbols('sigma',real=True)
I=s.I
checks=[]
def check(name,actual,expected=0):
    difference=actual-expected
    ok=all(s.simplify(x)==0 for x in difference) if isinstance(difference,s.MatrixBase) else s.simplify(difference)==0
    assert ok,(name,difference)
    checks.append({'name':name,'exact':True,'passed':True})

kminus=s.exp(lam*q)/(2*lam)
kplus=s.exp(-lam*q)/(2*lam)
check('Green equation on negative half-line',-s.diff(kminus,q,2)+lam**2*kminus)
check('Green equation on positive half-line',-s.diff(kplus,q,2)+lam**2*kplus)
check('Green continuity',kminus.subs(q,0),kplus.subs(q,0))
check('Green derivative jump',s.diff(kplus,q).subs(q,0)-s.diff(kminus,q).subs(q,0),-1)
k0=s.exp(-lam*u)/(2*lam);k1=-I*s.exp(-lam*u)/2
check('Boundary value kernel',kminus.subs(q,-u),k0)
check('Boundary normal derivative sign',(-I*s.diff(kminus,q)).subs(q,-u),k1)
check('Value profile squared norm',s.integrate(k0**2,(u,0,s.oo)),1/(8*lam**3))
check('Normal profile squared norm',s.integrate(s.conjugate(k1)*k1,(u,0,s.oo)),1/(8*lam))
check('Normal ratio density',s.diff(u*r,r)/(u*r),1/r)
check('Exact rescaled phase derivative',s.diff((1-1/r)*sigma,r),sigma/r**2)
check('Profile Euler multiplier sign',-s.diff(rho/(lam**2+rho**2),rho),(rho**2-lam**2)/(lam**2+rho**2)**2)
for order in [1,2,3]:
    a=k0
    for _ in range(order):a=u*s.diff(a,u)
    b=k0.subs(u,u*r)
    for _ in range(order):b=r*s.diff(b,r)
    check('Euler rescaling order '+str(order),b,a.subs(u,u*r))
primitive=rho-lam*s.atan(rho/lam)
check('Finite-cone integral primitive',s.diff(primitive,rho),rho**2/(lam**2+rho**2))
check('Finite-cone integral endpoints',primitive.subs(rho,C*lam)-primitive.subs(rho,-C*lam),2*lam*(C-s.atan(C)))
check('Graph norm multiplier difference',C**2*rho**2-rho**4/lam**2,rho**2*(C**2-rho**2/lam**2))
check('H1 example value scaling',(j**(-s.Rational(1,2)))**2/j,j**-2)
check('H1 example derivative scaling',(j**s.Rational(1,2))**2/j,1)
check('Normal-cap ellipticity remainder',rho**2-lam**2-s.Rational(3,5)*(rho**2+lam**2),s.Rational(2,5)*(rho**2-4*lam**2))
M=s.Matrix([[0,1],[1,0]]);B=s.Matrix([[0,1],[0,0]])
check('Gauge matrix square',M*M,s.eye(2))
S=s.cos(q)*s.eye(2)-I*s.sin(q)*M
Sinv=s.cos(q)*s.eye(2)+I*s.sin(q)*M
check('Actual gauge inverse',Sinv*S,s.eye(2))
check('Gauge face value',S.subs(q,0),s.eye(2))
check('Robin Dq sign',(-I*S.diff(q)).subs(q,0),-M)
check('Ordered commutator',M*B-B*M,s.diag(-1,1))
check('Ordered transformed coefficient derivative',(Sinv*B*S).diff(q).subs(q,0),I*(M*B-B*M))
check('Physical derivative conversion',-I*(I*sigma),sigma)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'source':'incoming-field-boundary-traces.md','source_sha256':sha(HERE/'incoming-field-boundary-traces.md'),
        'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'passed':True,'checks':checks,
        'scope':'Finite exact model identities only. The general profile, microlocal estimates, operator limits and graph trace identification are proved in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_algebraic_checks':len(checks)}))

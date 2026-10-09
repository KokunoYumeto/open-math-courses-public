"""CC0-1.0. Exact checks of the proof's phases, bounds and solved examples."""
from pathlib import Path
import hashlib, json
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def equal(name,a,b):
    assert S.simplify(a-b)==0,(name,S.simplify(a-b))
    checks.append({'name':name,'passed':True,'kind':'exact_identity'})
def bound(name,value):
    assert bool(value),name
    checks.append({'name':name,'passed':True,'kind':'exact_finite_inequality'})
x,y,t,r,nu,sigma,rho=S.symbols('x y t r nu sigma rho', positive=True)
phase=(1-t)*nu+(x*t-y*r)*rho+(1-1/r)*sigma
V=lambda f:y/x*S.diff(f,t)+S.diff(f,r)
equal('full canceling phase derivative',V(phase),sigma/r**2-y/x*nu)
equal('ordinary normal phase canceled',V(x*t-y*r),0)
k=S.Function('k')
equal('moving profile center canceled',V(k(x*t,y*r-x*t)),y*S.Subs(S.Derivative(k(S.Symbol('a'),y*r-x*t),S.Symbol('a')),S.Symbol('a'),x*t))
equal('first compressed density',S.diff(x*t,t)/x,1)
equal('second compressed density',S.diff(y*r,r)/(y*r),1/r)
equal('far normal phase derivative',S.diff((1-t)*nu+(1-1/r)*sigma,r),sigma/r**2)
equal('far support lower bound at 64',S.Rational(1,4)-S.Rational(4,64),S.Rational(3,16))
equal('comparable lower bound at 128',S.Rational(1,16)-S.Rational(128,8192),S.Rational(3,64))
bound('retained phase gap is weaker',S.Rational(3,64)>S.Rational(1,32))
for q in [1,16,64,96,128]:
    bound('phase gap at ratio '+str(q),S.Rational(1,16)-S.Rational(q,8192)>=S.Rational(3,64))
for q in [64,96,128,160]:
    bound('separation at ratio '+str(q),S.Rational(1,4)-S.Rational(4,q)>=S.Rational(3,16))
s,lam=S.symbols('s lambda',positive=True)
f=S.Function('f')(s)
for j in range(1,5):
    value=f
    for h in range(j):value=s*S.diff(value,s)-h*value
    equal('Euler falling product '+str(j),value,s**j*S.diff(f,s,j))
profile=S.exp(-lam*s)/(2*lam)
equal('inverse profile squared norm',2*S.integrate(profile**2,(s,0,S.oo)),1/(4*lam**3))
equal('normal derivative profile squared norm',2*S.integrate(S.diff(profile,s)**2,(s,0,S.oo)),1/(4*lam))
z=S.symbols('z',real=True)
u=S.Function('u')(x,z)
D=lambda f,v:-S.I*S.diff(f,v)
Vx=lambda f:x*D(f,x)
equal('formal dilation adjoint differential action',D(x*u,x),Vx(u)-S.I*u)
equal('boundary square first value',(x*x).subs(x,0),0)
equal('boundary square normal value',D(x*x,x).subs(x,0),0)
c=S.symbols('c',positive=True)
equal('counterexample collar norm factor',S.integrate(x**4,(x,0,c)),c**5/5)
result={'passed':True,'source_sha256':sha(ROOT/'elliptic-corrections-in-the-original-energy-norm.md'),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'scope':'Exact phases, Jacobians, overlap constants, Euler identities and solved profile norms. The full microlocal estimates and actual L2 limits are proved in the lesson, not certified by these finite checks.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

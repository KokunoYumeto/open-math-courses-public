"""Exact finite checks for the frequency-dependent trace proof."""
from pathlib import Path
import hashlib,json
import sympy as s
checks=[]
def eq(name,a,b=0):
 r=s.simplify(a-b)
 assert r==0,(name,r)
 checks.append({'name':name,'passed':True,'exact_residual':str(r)})
t,x=s.symbols('t x',real=True)
psi=4-6*t;rem=t*(1-t)**2
eq('zeroth trace moment',s.integrate(psi,(t,0,1)),1)
eq('first trace moment',s.integrate(t*psi,(t,0,1)))
eq('integrated Taylor kernel',s.integrate((4-6*t)*(t-x),(t,x,1)),-x*(1-x)**2)
eq('value kernel squared norm',s.integrate(psi**2,(t,0,1)),4)
eq('second derivative kernel squared norm',s.integrate(rem**2,(t,0,1)),s.Rational(1,105))
for n in range(7):
 v=t**n
 eq('trace identity on degree '+str(n),s.integrate(psi*v+rem*s.diff(v,t,2),(t,0,1)),1 if n==0 else 0)
ell,kappa,tau=s.symbols('ell kappa tau',positive=True)
h=tau/kappa;L=ell**2/kappa
eq('first weighted trace coefficient',L*8/h,8*ell**2/tau)
eq('second weighted trace coefficient',L*s.Rational(2,105)*h**3,s.Rational(2,105)*tau**3*ell**2/kappa**4)
b=s.symbols('b',real=True)
kap=ell**s.Rational(2,3)*(1+b*b)**s.Rational(1,4)
eq('normal scale squared',kap**2,ell**s.Rational(4,3)*s.sqrt(1+b*b))
eq('normal scale cubed',kap**3,ell**2*(1+b*b)**s.Rational(3,4))
eq('layer weight',ell**2/kap,ell**s.Rational(4,3)*(1+b*b)**(-s.Rational(1,4)))
eq('global moderation power',s.Rational(4,3)+s.Rational(1,2),s.Rational(11,6))
eq('square-root moderation power',s.Rational(11,6)/2,s.Rational(11,12))
eq('energy-only trace counterexample exponent',s.Rational(4,3)-1,s.Rational(1,3))
q,w1,w2=s.symbols('q w1 w2',real=True)
rho,eta1,eta2=s.symbols('rho eta1 eta2')
oldrho=rho-q*eta1
eq('principal cross-block removal',oldrho**2+2*q*oldrho*eta1+eta1**2-(1+q)*eta2**2,
 rho**2+(1-q*q)*eta1**2-(1+q)*eta2**2)
u=s.Function('u')(q,w1,w2)
Dq=lambda z:-s.I*s.diff(z,q)
D1=lambda z:-s.I*s.diff(z,w1)
D2=lambda z:-s.I*s.diff(z,w2)
oldD=lambda z:Dq(z)-q*D1(z)
actual=oldD(oldD(u))+2*q*oldD(D1(u))+D1(D1(u))-(1+q)*D2(D2(u))
claimed=Dq(Dq(u))+(1-q*q)*D1(D1(u))-(1+q)*D2(D2(u))+s.I*D1(u)
eq('full pulled-back differential operator',actual,claimed)
eq('normal derivative of tangential symbol at boundary',
 s.diff((1-q*q)*eta1**2-(1+q)*eta2**2,q).subs(q,0),-eta2**2)
eq('scaled remainder kernel maximum',(s.Rational(27,4)*rem).subs(t,s.Rational(1,3)),1)
eq('value kernel sign-change',psi.subs(t,s.Rational(2,3)))
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(HERE/'frequency-dependent-boundary-trace-estimate.md'),'script_sha256':sha(Path(__file__)),
 'checks':checks,'scope':'Finite exact trace moments, constants, frequency exponents and full differential-coordinate calculation. The all-frequency Schur bounds and weak-domain trace theorem are proved in the lesson.'}
(HERE/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))

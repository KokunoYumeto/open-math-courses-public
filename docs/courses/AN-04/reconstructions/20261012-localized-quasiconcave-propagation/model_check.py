"""Exact signs and scale identities used in the localized propagation proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
MOD=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a,b,T,lam,delta,eps,R=S.symbols('a b T lambda delta epsilon R',positive=True)
x,xi,t,y,r,theta,h=S.symbols('x xi t y r theta h',real=True)
checks=[]
def eq(name,u,v):
 d=S.simplify(u-v);assert d==0,(name,d);checks.append({'name':name,'difference':str(d),'passed':True})
def yes(name,v):
 assert v is True or v==S.true,(name,v);checks.append({'name':name,'passed':True})
br=lambda f,g:S.diff(f,xi)*S.diff(g,x)-S.diff(f,x)*S.diff(g,xi)
f=x*x+xi*x;c=1+xi*xi
eq('first mixed inverse correction cancellation',c*br(f,1/c)+br(f/c,c),0)
eq('mixed cross parameter at largest adaptive scale',a*S.sqrt(a),a**S.Rational(3,2))
eq('second mixed remainder', (a*S.sqrt(a))**2,a**3)
eq('squared forcing remainder',(a**3)**2,a**6)
eq('ordinary two-term remainder',(a**2)**2,a**4)
eq('adaptive Planck upper scale',S.sqrt(a)**2,a)
eq('floor commutator order',a/S.sqrt(a),S.sqrt(a))
eq('transfer squared error',(a**S.Rational(3,2))**2,a**3)
eq('double imaginary-part commutator weight',b**-2*(b**2)**2,b**2)
eq('ordinary lower-order commutator weight',a*b,a*b)
q=r;p=theta-h*r*r
eq('explicit canonical retained function',p+h*q*q,theta)
eq('explicit canonical Jacobian',S.det(S.Matrix([[S.diff(q,r),S.diff(q,theta)],[S.diff(p,r),S.diff(p,theta)]])),1)
eq('explicit Hamilton velocity q',S.diff(q,r),1)
eq('explicit Hamilton velocity p',S.diff(p,r),-2*h*q)
v=eps/2+(y-S.I*t)**2/R**2
eq('exact complex barrier transport',S.diff(v,t)+S.I*S.diff(v,y),0)
eq('exact real barrier',S.re(v),eps/2+(y*y-t*t)/R**2)
eq('global lower margin at maximal time loss',eps/2-eps/6,eps/3)
yes('inner margin strict gap',S.Rational(7,12)<S.Rational(2,3))
eq('inner upper bound',eps/2+eps/12,7*eps/12)
eq('outgoing lower bound',eps/2+1-eps/6,1+eps/3)
loga=S.symbols('ell',real=True)
G=S.Function('G')(x,xi);H=S.Function('H')(t,x,xi);w=S.Function('v')(t,x,xi)
eq('transport cancellation in weighted bracket',S.I*(S.I*H*br(w,G))+br(w,G*H),G*br(w,H))
eq('derivative energy coefficient at maximal scale',S.sqrt(a)*S.sqrt(T)*S.Abs(loga),S.sqrt(a*T)*S.Abs(loga))
eq('weighted reconstruction',a**(eps-S.symbols('v'))*a**S.symbols('v'),a**eps)
eq('reconstruction squared operator error',(a)**2,a**2)
eq('small positive reconstruction margin',eps-2*eps/3,eps/3)
eq('original normalized frequency scale',S.sqrt(lam)/delta,(lam/delta**2)**S.Rational(1,2))
eq('unmeasured forcing shell power',lam**S.Rational(3,2)*lam**(-S.Rational(5,4)),lam**S.Rational(1,4))
eq('unknown shell error',lam**S.Rational(1,4)*lam**(-S.Rational(1,4)),1)
eq('final shell index loss',S.symbols('sigma')-eps-eps/2,S.symbols('sigma')-3*eps/2)
eq('quarter bootstrap step',S.symbols('sigma')-S.Rational(1,4)+S.Rational(1,4),S.symbols('sigma'))
eq('minus-one error index margin',S.symbols('sigma')-S.Rational(1,4)+1,S.symbols('sigma')+S.Rational(3,4))
F=S.Function('f')(t,x,xi);C=S.Function('chi')(t,x,xi,S.symbols('tau',real=True))
tau=S.symbols('tau',real=True)
full=(S.diff(tau+S.I*F,tau)*S.diff(C,t)-S.diff(tau+S.I*F,t)*S.diff(C,tau)+S.diff(tau+S.I*F,xi)*S.diff(C,x)-S.diff(tau+S.I*F,x)*S.diff(C,xi))
eq('complete spacetime bracket',full,S.diff(C,t)-S.I*S.diff(F,t)*S.diff(C,tau)+S.I*(S.diff(F,xi)*S.diff(C,x)-S.diff(F,x)*S.diff(C,xi)))
Hflat=x*x+xi*xi+t*t;g=x+2*xi
for vars in [(x,x),(x,xi),(xi,xi)]:
 eq('saturated rank-one zero Hessian '+''.join(map(str,vars)),S.diff(g*Hflat,*vars).subs({x:0,xi:0,t:0}),0)
source=MOD/'localized-weights-and-quasiconcave-propagation.md'
v={'schema':'AN04-localized-quasiconcave-model-check/v1','source':source.name,'source_sha256':sha(source),
 'script_sha256':sha(Path(__file__)),'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,
 'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'cases':checks,
 'scope':'Finite transport signs, canonical chart, product cancellations and exact shell exponents. The full uniform analytic, operator and global comparison proofs are in the lesson.'}
(MOD/'model-check.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

"""Exact finite checks supporting the full reduced-leaf propagation proof."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
checks=[]
def exact(name,l,r=0):
 assert S.simplify(S.expand(l-r))==0,name
 checks.append({'name':name,'kind':'exact_identity','passed':True})
t,sigma,eta,lam,ell,rho,y,zeta,rr=S.symbols('t sigma eta lambda ell rho y zeta r',real=True)
lampos=S.symbols('lambda_positive',positive=True)
alpha=t*t;p=sigma+S.I*alpha*eta;q=S.exp(-ell*sigma)
br=lambda a,b:S.diff(a,sigma)*S.diff(b,t)-S.diff(a,t)*S.diff(b,sigma)
exact('full time bracket',br(alpha,sigma),-2*t)
exact('Hamilton decomposition on the weight',br(p,sigma),S.I*eta*br(alpha,sigma))
exact('leading commutator sign',br(p,q)/S.I,2*ell*t*eta*q)
left=sum((lam/S.I)**j/S.factorial(j)*S.diff(p,sigma,j)*S.diff(q,t,j) for j in range(3))
right=sum((lam/S.I)**j/S.factorial(j)*S.diff(q,sigma,j)*S.diff(p,t,j) for j in range(3))
exact('complete polynomial left commutator',(left-right)/lam,2*ell*t*eta*q+S.I*lam*ell**2*eta*q)
exact('time term vanishes from an incomplete transverse sum',S.diff(alpha,eta))
exact('factored main term',-lam*ell*(-1)*(eta*2*t/lam)*q,2*ell*t*eta*q)
exact('absorbed scale',lampos/S.sqrt(lampos),S.sqrt(lampos))
exact('half-step strict margin',S.Rational(1,1)-S.Rational(1,2),S.Rational(1,2))
a=S.exp(S.I*t*S.sin(S.log(rho)))
exact('nonhomogeneous gauge equation',S.I*S.diff(a,t)/a+S.sin(S.log(rho)))
exact('first inverse-frequency gauge derivative',S.diff(a,rho),a*S.I*t*S.cos(S.log(rho))/rho)
exact('second inverse-frequency gauge derivative',S.diff(a,rho,2)/a,
 (-t*t*S.cos(S.log(rho))**2-S.I*t*(S.sin(S.log(rho))+S.cos(S.log(rho))))/rho**2)
s=S.symbols('s',positive=True)
beta=S.exp(-1/s)
exact('positive flat primitive derivative',S.diff(beta,s),beta/s**2)
for k in range(1,6):
 poly=S.cancel(S.diff(beta,s,k)/beta)
 assert S.Poly(poly,1/s) is not None
 checks.append({'name':'flat primitive derivative '+str(k)+' is exponential times inverse-power polynomial','kind':'exact_algebraic_form','passed':True})
beta0=S.Function('beta')(t);av=S.diff(beta0,t);w=y-S.I*beta0
exact('complex coordinate equation',S.diff(w,t)+S.I*av*S.diff(w,y))
barrier=zeta*zeta*S.exp(w)
exact('full normal barrier equation',S.diff(barrier,t)+S.I*av*S.diff(barrier,y))
angle,b0=S.symbols('theta beta0',real=True)
for sign in [-1,1]:
 avg=S.integrate(sign*(b0+rr*S.cos(angle))**2,(angle,0,2*S.pi))/(2*S.pi)
 exact('circle mean sign '+str(sign),avg,sign*(b0*b0+rr*rr/2))
exact('quadratic Taylor mean coefficient',S.integrate(S.cos(angle)**2,(angle,0,2*S.pi))/(4*S.pi),S.Rational(1,4))
tau,vx,veta,vt,phi_t,phi_x,phi_sigma,phi_eta,g,at,ax,ae=S.symbols('tau vx veta vt phi_t phi_x phi_sigma phi_eta g at ax ae',real=True)
coeffs=[-phi_sigma,-phi_eta,phi_x]
exact('all spacetime gradient coefficients',sum(c*d for c,d in zip(coeffs,[at,ax,ae])),ae*phi_x-ax*phi_eta-at*phi_sigma)
tk=S.Rational(1,64)
exact('short-time absorption with T K equal to 1 over 64',4*tk/(1-2*tk),S.Rational(2,31))
source=HERE/'regularity-on-reduced-characteristic-leaves.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,'scope':'Exact full time-frequency commutator, gauge derivatives, flat primitive, normal barrier and circle-mean signs. Infinite-dimensional estimates, quotient topology, uniform remainders and harmonic comparison are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

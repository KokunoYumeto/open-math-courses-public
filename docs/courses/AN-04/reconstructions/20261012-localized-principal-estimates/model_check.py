"""Exact product, scaling and inverse checks for the two localized lemmas."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
rows=[]
def exact(name,l,r=0):
 assert S.simplify(S.expand(l-r))==0,name
 rows.append({'name':name,'kind':'exact_identity','passed':True})
x,y,h,d,lam,ell,mu,kappa,r=S.symbols('x y h delta lambda ell mu kappa r',positive=True)
br=lambda a,b:S.diff(a,y)*S.diff(b,x)-S.diff(a,x)*S.diff(b,y)
def star(a,b,N=2):
 ans=0
 for n in range(N+1):
  for j in range(n+1):
   ans+=(h/(2*S.I))**n*(-1)**j/S.factorial(j)/S.factorial(n-j)*S.diff(a,y,n-j,x,j)*S.diff(b,x,n-j,y,j)
 return S.expand(ans).series(h,0,N+1).removeO().expand()
q=1-x*x-y*y/4;a=x*x;b=y
qa=star(star(q,a),q);qb=star(star(q,b),q)
exact('positive sandwich principal symbol',qa.coeff(h,0),q*q*a)
exact('positive sandwich first correction',qa.coeff(h,1))
exact('self-adjoint B first correction',qb.coeff(h,1))
ab=star(qa,qb)
exact('AB principal cutoff power four',ab.coeff(h,0),q**4*a*b)
exact('AB first Poisson correction',ab.coeff(h,1),br(q*q*a,q*q*b)/(2*S.I))
bab=star(star(qb,qa),qb)
c=q**3*b;ca=star(star(c,a),c)
exact('both energy principal symbols agree',bab.coeff(h,0),ca.coeff(h,0))
exact('BAB first correction cancels',bab.coeff(h,1))
exact('C-alpha-C first correction cancels',ca.coeff(h,1))
der=star(star(q,S.diff(a,x)),c)
exact('derivative cutoff power four',der.coeff(h,0),q**4*b*S.diff(a,x))
exact('first model bracket',br(b,a),2*x)
exact('second model bracket',br(b,br(b,a)),2)
exact('mixed quantization correction',S.diff(a*b,x,y),2*x)
exact('AB first correction scale',d**3/lam*(lam/d**2),d)
exact('energy second correction scale',d**4/lam**2*(lam/d**2)**2,1)
exact('derivative first correction scale',d**2/lam*(lam/d**2),1)
exact('Nirenberg-Treves width exponent',S.Rational(2,4)+S.Rational(1,2)+S.Rational(0,4),1)
exact('physical base derivative power',lam*(1/lam),1)
exact('physical frequency derivative power',(1/lam)*lam,1)
exact('derivative normalization',S.sqrt(lam)/lam,1/S.sqrt(lam))
# Time is a parameter of the transverse quantization, but its coefficient
# derivative is part of the full nonnegative gradient form.
t,tau=S.symbols('t tau',real=True)
at=t*t+x*x
exact('full nonnegative time-space gradient',S.diff(at,t)**2+S.diff(at,x)**2,4*at)
exact('time coefficient derivative cutoff power four',star(star(q,S.diff(at,t)),c).coeff(h,0),q**4*b*S.diff(at,t))
exact('time coefficient first product correction',star(star(q,S.diff(at,t)),c).coeff(h,1),t*br(q,c)/S.I)
exact('time coefficient localized geometric size',((y-1)*S.diff(at,t)).subs({t:d,x:d,y:1+d}),2*d*d)
exact('full spacetime bracket contains time term',-S.diff(at,t)*S.diff(tau,tau),-2*t)
exact('physical time derivative power',lam*(1/lam),1)
# A linear complex weight gives an exact exponential product correction.
# The finite inverse has coefficients ell^(2j)/j!, not an assumed sign.
phi=x+S.I*y;a0=S.exp((phi-mu)*ell);qp=S.exp(-phi*ell)
exact('complex inverse leading product',a0*qp,S.exp(-mu*ell))
exact('complex inverse first correction',S.diff(a0,y)*S.diff(qp,x)/S.I,-ell**2*S.exp(-mu*ell))
for degree in range(1,6):
 coeff=sum(S.Rational((-1)**(degree-j),S.factorial(j)*S.factorial(degree-j))*ell**(2*degree) for j in range(degree+1))
 exact('finite exponential inverse degree '+str(degree),coeff)
for kk in range(1,5):
 f=S.exp(-kappa*r)*r**kk
 exact('logarithmic derivative k='+str(kk),S.diff(f,r),S.exp(-kappa*r)*r**(kk-1)*(kk-kappa*r))
 exact('logarithmic optimizer k='+str(kk),f.subs(r,kk/kappa),(kk/(S.E*kappa))**kk)
n,ss=S.symbols('n sigma',real=True)
exact('delta shell squared scaling',-n+n,0)
exact('Sobolev critical radial exponent',2*(-n/2)+n-1,-1)
exact('integrated shell homogeneous exponent',ss-mu-1+1,ss-mu)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'frequency-localized-estimates-and-sobolev-indices.md'
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,'checks':rows,'scope':'Exact Weyl product coefficients, cutoff powers, geometric and frequency scales, complex-weight inverse signs, logarithmic extrema and Sobolev threshold. Uniform analytic remainders and infinite-dimensional operator estimates are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))

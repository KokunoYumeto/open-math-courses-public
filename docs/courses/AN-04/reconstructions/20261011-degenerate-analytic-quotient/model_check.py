"""Exact signs, coordinate identities and barrier margins from the written proof."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
source=HERE/'boundary-barriers-and-degenerate-analytic-quotients.md'
x,t,y,b,A,C=S.symbols('x t y b A C',real=True)
p,a,r,delta,ep,M,rho,lam=S.symbols('p a r delta ep M rho lambda',positive=True)
q=S.symbols('q',real=True)
rows=[]
def exact(name,left,right=0):
 assert S.simplify(S.expand(left-right))==0,name
 rows.append({'name':name,'kind':'exact_identity','passed':True})
def strict(name,left,right):
 assert bool(left<right),name
 rows.append({'name':name,'kind':'exact_inequality','passed':True})
z=x-S.I*t
F=4*delta*(1/(delta+z+r)+1/(delta+r-z))
exact('rational barrier real part',S.re(F),4*delta*((delta+x+r)/((delta+x+r)**2+t**2)+(delta+r-x)/((delta+r-x)**2+t**2)))
exact('constant real-coordinate derivative',a*q+p*(-a*q/p))
exact('monotone imaginary-coordinate derivative',-a*p+q*(-a*q/p),-a*(p*p+q*q)/p)
exact('positive real Jacobian',S.det(S.Matrix([[a*q,p],[-a*p,q]])),a*(p*p+q*q))
exact('homogeneous coordinate chain coefficient',a*q-S.I*a*p+S.I*a*(p+S.I*q))
exact('conjugate coordinate chain coefficient',a*q+S.I*a*p+S.I*a*(p-S.I*q),2*S.I*a*(p-S.I*q))
exact('endpoint reciprocal real part',S.re(4/(1+x+S.I*y)),4*(1+x)/((1+x)**2+y*y))
exact('endpoint universal lower bound',4*S.Rational(3,4)/S.Rational(5,4)**2,S.Rational(48,25))
strict('endpoint margin exceeds one',S.Integer(1),S.Rational(48,25))
exact('tube perturbation bound',M*(delta/(64*M)+2*delta/(64*M)),3*delta/64)
exact('complete endpoint perturbation bound',M*(delta/(16*M)+delta/(64*M)+2*delta/(64*M)),7*delta/64)
strict('complete endpoint inside quarter tube',S.Rational(7,64),S.Rational(1,4))
exact('central rational bound with chosen strict subscale',(32*delta/r).subs(delta,ep*r/256),ep/8)
strict('central bound below one quarter',S.Rational(1,8),S.Rational(1,4))
exact('inactive parameter contribution at inner radius',2*(S.sqrt(ep)/4)**2,ep/8)
strict('combined inner margin',S.Rational(1,4)+S.Rational(1,8),S.Integer(1))
exact('positive primitive derivative',S.diff((t-S.Rational(1,3))**2/2,t),t-S.Rational(1,3))
exact('negative primitive derivative',S.diff(-(t+S.Rational(1,3))**2/2,t),-t-S.Rational(1,3))
exact('positive primitive endpoint',((t-S.Rational(1,3))**2/2).subs(t,S.Rational(1,3)))
exact('negative primitive endpoint',(-(t+S.Rational(1,3))**2/2).subs(t,-S.Rational(1,3)))
exact('continuous coefficient coordinate sign',S.diff(x-S.I*t**3/3,t)+S.I*t*t*S.diff(x-S.I*t**3/3,x))
conic=b*t+S.I*S.log(rho)
exact('conic homogeneous coordinate',S.diff(conic,t)+S.I*b*rho*S.diff(conic,rho))
exact('radial-invariant real part',rho*S.diff(S.re(conic),rho))
exact('dilation is imaginary translation',conic.subs(rho,lam*rho)-conic,S.I*S.log(lam))
exact('wrong conic sign is detected',S.diff(-b*t+S.I*S.log(rho),t)+S.I*b*rho*S.diff(-b*t+S.I*S.log(rho),rho),-2*b)
exact('affine real transition',S.re(A*(x+S.I*y)+C),A*x+C)
exact('complex and affine example coordinates',-S.I*(-t+S.I*S.log(rho)),S.log(rho)+S.I*t)
exact('example central bound',32*S.Rational(1,512),S.Rational(1,16))
strict('example delta satisfies required scale',S.Rational(1,512),S.Rational(1,2)/128)
exact('example endpoint time distance',S.Rational(1,16)+S.Rational(1,64),S.Rational(5,64))
strict('example endpoint inside tube',S.Rational(5,64),S.Rational(1,4))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,'checks':rows,'scope':'Exact chain-rule and Hamilton signs, rational barrier identities and strict rational margins. The complete topology, uniform bounds and holomorphic limit are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))

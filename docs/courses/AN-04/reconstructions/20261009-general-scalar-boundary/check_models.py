"""Exact model checks supplement, but do not replace, the analytic proof."""
from pathlib import Path
import hashlib,json
import sympy as S
P=Path(__file__).resolve().parent
x,z1,z2,z3,rho,e1,e2,e3,k=S.symbols('x z1 z2 z3 rho eta1 eta2 eta3 kappa',real=True)
ep,de,A,M,lam=S.symbols('epsilon delta A M lambda',positive=True)
coords=(x,z1,z2,z3);mom=(rho,e1,e2,e3)
def pb(f,g):return sum(S.diff(f,p)*S.diff(g,q)-S.diff(f,q)*S.diff(g,p) for q,p in zip(coords,mom))
checks=[]
def eq(name,actual,expected=0):
 residual=S.simplify(actual-expected)
 assert residual==0,(name,residual)
 checks.append({'name':name,'kind':'exact_identity','passed':True})
def positive(name,expression):
 assert expression.is_positive,(name,expression)
 checks.append({'name':name,'kind':'exact_positive_margin','passed':True})
r=e1**2+e2**2-e3**2+k*x*e3**2;p=rho**2-r;r0=r.subs(x,0)
N=-z3/2;a=e1/e3;b=e2/e3
v1=z1+a*z3;v2=z2+b*z3
omega=v1**2+v2**2+(a-1)**2+b**2
eq('boundary clock',pb(r0,N),e3)
for j,f in enumerate([v1,v2,a-1,b],1):eq('boundary transverse invariant '+str(j),pb(r0,f))
eq('boundary transverse quadratic',pb(r0,omega))
eq('full clock',pb(r,N),(1-k*x)*e3)
eq('full transverse error',pb(r,omega),4*k*x*e3*(a*v1+b*v2))
eq('characteristic transverse defining function',r0/e3**2,2*(a-1)+(a-1)**2+b**2)
aa,bb=S.symbols('a b',real=True)
section=S.Matrix([-z3/2,z1+aa*z3,z2+bb*z3,aa-1,bb])
eq('flow-coordinate Jacobian',section.jacobian([z1,z2,z3,aa,bb]).det(),-S.Rational(1,2))
for j,want in enumerate([1,-1,-1,1]):
 eq('ultrahyperbolic diagonal '+str(j),S.diff(p,mom[j],2).subs(x,0)/2,want)
phi=-N+x/ep+omega/(de*ep**2)
eq('full escape derivative',pb(p,phi),(1-k*x)*e3+2*rho/ep-4*k*x*e3*(a*v1+b*v2)/(de*ep**2))
eq('escape support identity',phi/de+N/de,x/(ep*de)+omega/(ep**2*de**2))
eq('normal Hamilton speed',pb(p,x),2*rho)
eq('normal Hamilton force',pb(p,rho),k*e3**2)
eq('gliding clock orientation',pb(p,N).subs({x:0,rho:0}),-e3)
q,dq,b2,e2s,psi2,kk,zz=S.symbols('q Hpq b2 e2s psi2 k z',real=True)
eq('full anti-Hermitian cancellation',dq-2*q*(kk+zz)+(M*lam+2*(kk+zz))*q+b2-e2s,dq+M*lam*q+b2-e2s)
cv,cp,ch,chp,Hphi,HrN,v=S.symbols('chi0 chi0prime chi1 chi1prime Hphi HrN v',real=True)
Hpq=-cp*ch*Hphi/(A*de)+cv*chp*HrN/(ep*de)
bs=lam*cp*ch/(4*A*de);es=cv*chp*HrN/(ep*de)
psis=cp*ch*(Hphi/(A*de)-M*lam*v**2-lam/(4*A*de))
eq('characteristic square identity',(Hpq+M*lam*cv*ch+psis+bs-es).subs(cv,v**2*cp))
vv=S.symbols('v',positive=True)
eq('flat cutoff quotient',S.exp(-1/vv),vv**2*S.diff(S.exp(-1/vv),vv))
h=S.symbols('h',real=True)
u,w,up,wp=S.symbols('u w up wp',positive=True)
eq('step derivative quotient',((up*(u+w)-u*(up-wp))/(u+w)**2),(up*w+u*wp)/(u+w)**2)
eq('damping at threshold',S.Rational(1,4)-16*M*de/(128*M*de),S.Rational(1,8))
positive('threshold damping margin',S.Rational(1,8))
eq('exercise damping parameter',128*10000*S.Rational(1,64),20000)
eq('exercise damping margin',S.Rational(1,4)-16*10000*S.Rational(1,64)/20000,S.Rational(1,8))
j=S.symbols('j',integer=True)
eq('twenty half steps',1-S.Rational(20,40),S.Rational(1,2))
eq('Sobolev total gain',S.Rational(20,2),10)
rr,ll=S.symbols('normal_frequency tangent_frequency',real=True)
eq('normal interpolation polynomial',ll**4+rr**4-2*rr**2*ll**2,(rr**2-ll**2)**2)
eq('extension value jets',3-2,1)
eq('extension first jets',-3+4,1)
y,eta,eta0,s=S.symbols('y eta eta0 s',real=True)
pr=rho**2-y*eta**2
radial=[S.diff(pr,rho),S.diff(pr,eta),-S.diff(pr,x),-S.diff(pr,y)]
for i,(actual,expected) in enumerate(zip(radial,[2*rho,-2*y*eta,0,eta**2])):eq('radial Hamilton component '+str(i),actual,expected)
orbit=eta0/(1-eta0*s)
eq('radial orbit equation',S.diff(orbit,s),orbit**2)
eq('radial characteristic constraint',pr.subs({rho:0,y:0}))
for degree in range(6):
 test=y**degree
 eq('distributional equation test degree '+str(degree),S.diff(y*test,y,2).subs(y,0)-2*S.diff(test,y).subs(y,0))
eq('normal factor second derivative',S.diff(x,x,2))
eq('normal value trace',x.subs(x,0))
eq('normal derivative trace multiplier',-S.I*S.diff(x,x),-S.I)
d=S.Rational(1,64);eps=S.Rational(1,8)
eq('normal and transverse figure scale',d*eps,S.Rational(1,512))
eq('parabolic width factor',eps,8*d)
eq('outer incoming edge',1+eps,S.Rational(9,8))
eq('inner incoming edge',1+eps/2,S.Rational(17,16))
eq('outer normal cap',d*eps*(2+1+eps),S.Rational(25,4096))
eq('incoming omitted z3',-2*d,-S.Rational(1,32))
eq('incoming omitted z1',2*d,S.Rational(1,32))
report={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':hashlib.sha256((P/'scalar-boundary-propagation-through-general-glancing.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
 'scope':'Exact ultrahyperbolic clock and escape identities, ordered leading cancellation, damping margin, interpolation weights, radial distributional example and figure coordinates. These checks do not replace the analytic proof.'}
(P/'model-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

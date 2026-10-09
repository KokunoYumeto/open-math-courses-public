"""CC0-1.0. Exact Hamilton paths, cap limits, Sobolev indices and support gaps."""
from pathlib import Path
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def equal(name,a,b):
 assert S.simplify(a-b)==0,(name,S.simplify(a-b))
 checks.append({'name':name,'passed':True,'kind':'exact_identity'})
def bound(name,v):
 assert bool(v),name
 checks.append({'name':name,'passed':True,'kind':'exact_inequality'})
x,rho,tau,zeta,mu=S.symbols('x rho tau zeta mu',real=True)
p=rho**2-x*zeta**2-tau**2+zeta**2
equal('normal velocity',S.diff(p,rho),2*rho)
equal('normal covector velocity',-S.diff(p,x),zeta**2)
equal('time coordinate velocity',S.diff(p,tau),-2*tau)
equal('second tangential velocity',S.diff(p,zeta),2*(1-x)*zeta)
path_x=mu+rho**2
path_t=-2*tau*rho
path_y=2*(1-mu)*rho-S.Rational(2,3)*rho**3
equal('characteristic path',p.subs({x:path_x,zeta:1}).subs(mu,1-tau**2),0)
equal('normal path derivative',S.diff(path_x,rho),2*rho)
equal('time path derivative',S.diff(path_t,rho),-2*tau)
equal('second tangential path derivative',S.diff(path_y,rho),2*(1-path_x))
equal('strict convexity',S.diff(path_x,rho,2),2)
h=S.Rational(1,16)
a=S.sqrt(h-mu)
equal('slice height at both roots',path_x.subs(rho,a),h)
equal('unreflected time increment',path_t.subs(rho,a)-path_t.subs(rho,-a),-4*tau*a)
equal('unreflected second coordinate increment',path_y.subs(rho,a)-path_y.subs(rho,-a),4*(1-mu)*a-S.Rational(4,3)*a**3)
b=S.symbols('b',nonnegative=True)
equal('reflected time increment',path_t.subs(rho,-b)-path_t.subs(rho,-a)+path_t.subs(rho,a)-path_t.subs(rho,b),-4*tau*(a-b))
equal('reflected second coordinate increment',path_y.subs(rho,-b)-path_y.subs(rho,-a)+path_y.subs(rho,a)-path_y.subs(rho,b),4*(1-mu)*(a-b)-S.Rational(4,3)*(a**3-b**3))
e=S.symbols('e',positive=True)
negative=-4*S.sqrt(1+e)*(S.sqrt(h+e)-S.sqrt(e))
positive=-4*S.sqrt(1-e)*S.sqrt(h-e)
equal('negative-side cap limit',S.limit(negative,e,0),-1)
equal('positive-side cap limit',S.limit(positive,e,0),-1)
equal('negative-side square-root coefficient',S.limit((negative+1)/S.sqrt(e),e,0),4)
for v in [-S.Rational(1,100),0,S.Rational(1,100)]:
 bound('plotted minimum below cap '+str(v),v<h)
 equal('plotted endpoint at cap '+str(v),v+(h-v),h)
indices=[-S.Integer(1)]
target=S.Rational(5,4)
while indices[-1]<target:indices.append(min(indices[-1]+1,target))
equal('three finite elliptic steps',len(indices)-1,3)
equal('last tangential elliptic index',indices[-1],S.Rational(5,4))
equal('elliptic mixed target order',indices[-1]+2,S.Rational(13,4))
equal('global half-step target',S.Rational(9,4)+S.Rational(1,2),S.Rational(11,4))
for n in range(1,7):
 center=S.Rational(1,2)**n;radius=center/8
 next_center=center/2;next_radius=next_center/8
 bound('disjoint neighboring bump intervals '+str(n),next_center+next_radius<center-radius)
 equal('exact gap between bump supports '+str(n),center-radius-next_center-next_radius,5*center/16)
result={'passed':True,'source_sha256':sha(ROOT/'dirichlet-diffraction-on-one-open-region.md'),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'checks':checks,
 'scope':'Exact Hamilton coordinates, reflected cap increments and limits, finite Sobolev index iteration and disjoint supports. The complete analytic bootstrap and energy-front statement are proved in the lesson, not certified by these finite checks.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

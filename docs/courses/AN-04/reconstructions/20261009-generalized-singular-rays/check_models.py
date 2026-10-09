"""CC0-1.0. Exact equations, compression, clock and change-of-speed checks."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
checks=[]
def eq(label,a,b):
 assert S.simplify(a-b)==0,(label,a,b)
 checks.append(label)
x,t,y,rho,tau,eta,k=S.symbols('x t y rho tau eta k',real=True)
positions=[x,t,y];momenta=[rho,tau,eta]
def H(p,f):
 return S.expand(sum(S.diff(p,m)*S.diff(f,z)-S.diff(p,z)*S.diff(f,m) for z,m in zip(positions,momenta)))
p=tau**2-rho**2-(1+k*x)*eta**2
eq('physical time Hamilton derivative',H(p,t),2*tau)
eq('normal Hamilton acceleration',H(p,H(p,x)),-2*k*eta**2)
eq('noncharacteristic double normal coefficient',H(x,H(x,p)),-2)
for name,kv,et,xv,rv,yv in [
 ('incoming reflection',0,S.Rational(3,5),-4*t/5,S.Rational(4,5),-3*t/5),
 ('outgoing reflection',0,S.Rational(3,5),4*t/5,-S.Rational(4,5),-3*t/5),
 ('strict diffraction',-1,1,t*t/4,-t/2,-t+t**3/12)]:
 vals={x:xv,rho:rv,tau:1,eta:et,k:kv}
 eq(name+' characteristic equation',p.subs(vals),0)
 for var,actual in [(x,xv),(rho,rv),(y,yv)]:
  eq(name+' equation for '+str(var),S.diff(actual,t),(H(p,var)/2).subs(vals))
eq('compressed incoming root product',(-4*t/5)*S.Rational(4,5),-16*t/25)
eq('compressed outgoing root product',(4*t/5)*(-S.Rational(4,5)),-16*t/25)
glance={x:0,rho:0,tau:1,eta:1}
ratio=H(p,H(p,x))/H(x,H(x,p))
for var,expected in [(x,0),(rho,0),(t,2),(y,-2)]:
 eq('gliding component '+str(var),(H(p,var)+ratio*H(x,var)).subs(glance),expected)
c=-(2+x+t)
q=c*p
eq('scaled second normal derivative',H(q,H(q,x)).subs(glance),(c*c*H(p,H(p,x))).subs(glance))
eq('scaled transverse Hessian',H(x,H(x,q)).subs(glance),(c*H(x,H(x,p))).subs(glance))
for var in [x,t,y,rho]:
 gq=H(q,var)+H(q,H(q,x))/H(x,H(x,q))*H(x,var)
 gp=H(p,var)+ratio*H(x,var)
 eq('full scaled gliding component '+str(var),(gq-c*gp).subs(glance),0)
for sign in [-1,1]:
 eq('normalized physical clock sign '+str(sign),(H(p,sign*t)/(2*S.Abs(tau))).subs(tau,sign),1)
z=2*(S.exp(t)-1)
eq('rescaled line flow equation',S.diff(z,t),2+z)
eq('rescaled flow initial point',z.subs(t,0),0)
eq('matching first velocity',S.diff(z,t).subs(t,0),2)
eq('quadratic witness error coefficient',3*2**2,12)
eq('coordinate Lipschitz factor',2*(12+S.exp(S.Rational(1,4))),24+2*S.exp(S.Rational(1,4)))
eq('figure reflected endpoint',S.Rational(4,5)*S.Rational(3,5),S.Rational(12,25))
eq('figure diffractive endpoint',S.Rational(3,5)**2/4,S.Rational(9,100))
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(ROOT/'generalized-singular-rays-for-the-weak-wave-problem.md'),
 'script_sha256':sha(Path(__file__)),'scope':'Exact local model equations, compression, full gliding-field scaling and clock identities. The analytic propagation and maximal-extension proofs are in the lesson.',
 'internal_export_proof_closure_claimed':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

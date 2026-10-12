"""Finite exact checks for the tensor descent and affine geometry."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
checks=[]
def exact(name,left,right=0):
 assert S.simplify(S.expand(left-right))==0,name
 checks.append({'name':name,'kind':'exact_identity','passed':True})
t,y,tau,eta,rho,x2,x3=S.symbols('t y tau eta rho x2 x3',real=True)
beta=S.Function('beta')(t);h=S.diff(beta,t)
w=beta+S.I*y
exact('lifted complex coordinate',S.diff(w,t)+S.I*h*S.diff(w,y))
g=rho*(x2*x2-x3*x3)
q=tau+S.I*h*(eta+g)
exact('temporal principal derivative',S.diff(q,tau),1)
exact('new regular defining differential',S.diff(eta+g,eta),1)
exact('extra Hamilton component',S.diff(q,eta),S.I*h)
exact('original g vanishes on central mark',g.subs({x2:0,x3:0}))
for var in [rho,x2,x3]:
 exact('original g differential '+str(var),S.diff(g,var).subs({x2:0,x3:0}))
exact('positive transverse Hessian',S.diff(g,x2,2),2*rho)
exact('negative transverse Hessian',S.diff(g,x3,2),-2*rho)
a=S.symbols('a',positive=True)
flat=S.exp(-1/a)
exact('flat derivative',S.diff(flat,a),flat/a**2)
for k in range(1,6):
 assert S.Poly(S.cancel(S.diff(flat,a,k)/flat),1/a) is not None
 checks.append({'name':'flat derivative '+str(k)+' is exponential times inverse-power polynomial','kind':'exact_algebraic_form','passed':True})
exact('endpoint coefficient',(flat/a**2).subs(a,1),S.exp(-1))
angle,b0,r=S.symbols('angle b0 r',real=True)
for sign in [-1,1]:
 mean=S.integrate(sign*(b0+r*S.cos(angle))**2,(angle,0,2*S.pi))/(2*S.pi)
 exact('circle mean '+str(sign),mean,sign*(b0*b0+r*r/2))
xi,x1=S.symbols('xi x1',real=True)
p=xi*(x1+S.I*(x2*x2-x3*x3))
exact('radial Hamilton momentum component',-S.diff(p,x1),-xi)
exact('radial base component',S.diff(p,xi).subs({x1:0,x2:0,x3:0}))
exact('radial affine derivative',S.diff(-S.exp(-t),t),S.exp(-t))
rr,ss=S.symbols('r s',positive=True)
exact('delta critical integrand exponent',2*S.Rational(-1,2),-1)
exact('delta endpoint logarithmic primitive',S.diff(S.log(rr),rr),1/rr)
z,e=S.symbols('z e',real=True)
exact('tensor weight product bound identity',(1+z*z)*(1+e*e)-(1+z*z+e*e),z*z*e*e)
source=HERE/'one-dimensional-descent-and-affine-concavity.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(HERE/'model-check.json').write_text(json.dumps({'passed':True,'source_sha256':sha(source),
 'script_sha256':sha(Path(__file__)),'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,
 'scope':'Exact lifted Hamilton components, defining differential, indefinite Hessian, flat derivative formulas, circle means, radial affine parameter and tensor weight algebra. Distribution estimates, compact-fiber geometry and global concavity are proved in the lesson.'},indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

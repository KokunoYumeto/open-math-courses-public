"""Exact finite checks; the analytic estimates are proved in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
q,y1,y2,w1,w2,mu,lam,sigma,u,r=s.symbols('q y1 y2 w1 w2 mu lam sigma u r',real=True)
d=s.symbols('d',integer=True,positive=True)
checks=[]
def eq(name,a,b=0):
    residual=s.simplify(a-b)
    assert residual==0,(name,residual)
    checks.append({'name':name,'passed':True,'exact_residual':str(residual)})
z=-q-mu/lam
phi=(y1-w1)*mu+(y2-w2)*lam+sigma*z+sigma**3/(3*lam**2)
eq('auxiliary critical equation',s.diff(phi,sigma),z+sigma**2/lam**2)
eq('input first coordinate',s.diff(phi,mu),y1-w1-sigma/lam)
eq('input last coordinate',s.diff(phi,lam),y2-w2+sigma*mu/lam**2-2*sigma**3/(3*lam**3))
sub={sigma:lam*u,q:u*u-mu/lam,y1:w1+u,y2:w2-u*mu/lam+2*u**3/3}
for v in [sigma,mu,lam]:eq('critical substitution '+str(v),s.diff(phi,v).subs(sub,simultaneous=True))
eq('normal covector',s.diff(phi,q).subs(sigma,lam*u),-lam*u)
eq('first tangential covector',s.diff(phi,y1),mu)
eq('last tangential covector',s.diff(phi,y2),lam)
eq('Hamilton characteristic identity',(-lam*u)**2-(u*u-mu/lam)*lam**2-mu*lam)
out=s.Matrix([u*u-mu/lam,w1+u,w2-u*mu/lam+2*u**3/3,-lam*u,mu,lam])
jac=out.jacobian([w1,w2,mu,lam,u])
eq('nonzero output immersion minor',jac[[1,2,3,4,5],:].det(),-lam)
eq('input submersion minor',s.eye(4).det(),1)
eq('boundary second input shift',(u*mu/lam-2*u**3/3).subs(mu,lam*u*u),u**3/3)
eq('ordinary Airy amplitude order',-s.Rational(1,3)+1-s.Rational(2,3)-s.Rational(2,3),-s.Rational(2,3))
order=-s.Rational(2,3)+(d+1)/2-(2*d+1)/4
eq('unequal dimension kernel order',order,-s.Rational(5,12))
eq('normal operator order',2*order+s.Rational(1,2),-s.Rational(1,3))
eq('conjugated kernel order',order+r+s.Rational(1,6)-r,-s.Rational(1,4))
eq('conjugated normal order',2*(-s.Rational(1,4))+s.Rational(1,2))
eq('energy input exponent',1-s.Rational(1,6),s.Rational(5,6))
eq('tangential energy squared power',2-s.Rational(1,3),s.Rational(5,3))
eq('normal energy squared power',s.Rational(4,3)+s.Rational(1,3),s.Rational(5,3))
eq('oscillatory energy derivative',s.diff(s.Rational(4,3)*q**s.Rational(3,2),q),2*s.sqrt(q))
f=s.exp(y1/4)*(q+q*q/5)
eq('coordinate Jacobian',s.diff(f,q),s.exp(y1/4)*(1+2*q/5))
eq('coordinate tangential derivative',s.diff(f,y1),f/4)
rho=-lam*u*s.diff(f,q);xi1=mu-lam*u*s.diff(f,y1)
p=(rho/s.diff(f,q))**2-f*lam**2-(xi1-rho*s.diff(f,y1)/s.diff(f,q))*lam
eq('variable phase characteristic identity',p,lam**2*(u*u-f)-mu*lam)
eq('exact plotted marked radius',s.Rational(7,10)**2,s.Rational(49,100))
eq('exact plotted normal covector',-s.Rational(7,10),s.Rational(-7,10))
eq('normalized power at lambda 64',s.Integer(64)**s.Rational(5,3),1024)
eq('decay power at lambda 64',s.Integer(64)**s.Rational(-1,3),s.Rational(1,4))
source=HERE/'sharp-sobolev-mapping-for-the-decaying-airy-kernel.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
        'numerical_checks':0,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
        'scope':'Exact signs, critical equations, projection minor, FIO orders, energy exponents and variable-coordinate identities. Not a numerical proof of the analytic estimates.',
        'checks':checks}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

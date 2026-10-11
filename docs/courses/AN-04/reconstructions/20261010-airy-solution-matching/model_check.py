"""Exact algebra checks accompanying AM; analytic estimates are proved in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def check(name,expression):
    assert s.simplify(expression)==0,(name,expression)
    checks.append(name)
q,mu,lam=s.symbols('q mu lam',positive=True)
phase=s.Rational(2,3)*lam*(q+mu/lam)**s.Rational(3,2)
rho=s.diff(phase,q)
check('positive root',rho**2-(mu*lam+q*lam**2))
check('negative root',(-rho)**2-(mu*lam+q*lam**2))
check('mu displacement',s.diff(phase,mu)-s.sqrt(q+mu/lam))
check('lambda displacement',s.diff(phase,lam)-(2*q-mu/lam)*s.sqrt(q+mu/lam)/3)
check('central s plus',-s.diff(phase,mu).subs({mu:0,q:s.Rational(1,4),lam:1})+s.Rational(1,2))
check('central t plus',-s.diff(phase,lam).subs({mu:0,q:s.Rational(1,4),lam:1})+s.Rational(1,12))
check('central rho plus',rho.subs({mu:0,q:s.Rational(1,4),lam:1})-s.Rational(1,2))
check('Cauchy inverse order',-s.Rational(1,2)+s.Rational(5,6)-s.Rational(1,3))
check('initial field order',s.Rational(1,3)+s.Rational(1,6)-s.Rational(1,2))
check('bounded extraction order',1-s.Rational(1,6)-s.Rational(5,6))
A,B,Ap,a,c,k,u,d=s.symbols('A B Ap a c k u d',nonzero=True)
Bp=(s.Rational(1,1)/s.pi+Ap*B)/A
uv=a*A+c*B;dv=-k*(a*Ap+c*Bp)
check('value recovers Ai coefficient',s.pi*(Bp*uv+B*dv/k)-a)
check('derivative recovers Bi coefficient',-s.pi*(Ap*uv+A*dv/k)-c)
alpha=a-s.I*c
v=c*(B+s.I*A)
check('actual value matching',A*alpha+v-uv)
check('normalized multiplier constant',v/(A-s.I*B)-s.I*c)
Ai,Bi=s.symbols('Ai Bi')
check('exact stable representation',Ai*alpha+(Ai-s.I*Bi)*v/(A-s.I*B)-(a*Ai+c*Bi))
check('incoming half coefficient',(alpha/2)-((a-s.I*c)/2))
check('layer series exponent',s.Rational(4,3)-s.Rational(3,2)+s.Rational(1,6))
check('oscillating series exponent',s.Rational(5,3)-s.Rational(3,2)-s.Rational(1,6))
check('second normal derivative',s.diff(q**s.Rational(9,4),q,2)-s.Rational(45,16)*q**s.Rational(1,4))
check('third normal derivative',s.diff(q**s.Rational(9,4),q,3)-s.Rational(45,64)*q**s.Rational(-3,4))
source=root/'matching-an-energy-solution-to-airy-kernels.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
     'numerical_checks':0,'checks':checks,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
     'scope':'Finite signs, orders, affine Cauchy algebra, norm-series exponents and exact figure coordinates; analytic assertions are proved in AM.'}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps(out))

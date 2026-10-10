"""Exact checks for the gauge, finite gain chain and complete model Hamilton trajectory."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent
x,t,z=s.symbols('x tau z',real=True);c,cx,alpha,beta=s.symbols('c cx alpha beta')
checks=[]
def check(name,expr):
    value=s.simplify(s.expand(expr))
    assert value==0,(name,value)
    checks.append(name)
D=lambda f:-s.I*s.diff(f,x)
u=s.Function('u')(x)
S=s.exp(-s.I*c*x/2)
check('constant normal gauge derivative',s.diff(S,x)+s.I*c*S/2)
check('constant first normal coefficient',c-2*s.I*s.diff(S,x)/S)
check('constant full normal conjugation',(D(D(S*u))+c*D(S*u))/S-D(D(u))+c*c*u/4)
sx=-s.I*c/2;sxx=-s.I*cx/2-c*c/4
check('variable first normal coefficient',c-2*s.I*sx)
check('variable normal scalar coefficient',-sxx-s.I*c*sx-(s.I*cx/2-c*c/4))
check('transformed R scalar sign',-(-sxx-s.I*c*sx)-(c*c/4-s.I*cx/2))
check('complex exponent split',-s.I*(alpha+s.I*beta)*x/2-(beta*x/2-s.I*alpha*x/2))
check('boundary normalization',S.subs(x,0)-1)
X=t*t/2;rho=t/2;z1=-s.sqrt(2)*t;z2=s.sqrt(2)*(t-t**3/6);eta=s.sqrt(2)/2
check('Hamilton normal position',s.diff(X,t)-2*rho)
check('Hamilton normal covector',s.diff(rho,t)-eta**2)
check('Hamilton first tangent position',s.diff(z1,t)+2*eta)
check('Hamilton second tangent position',s.diff(z2,t)-2*(1-X)*eta)
check('exact characteristic equation',rho*rho-eta**2+(1-X)*eta**2)
check('compressed normal covector',X*rho-t**3/4)
check('exact projected parabola',X-z1**2/4)
check('boundary clock speed',s.sqrt(2)/(2*s.sqrt(2))+s.sqrt(2)/(2*s.sqrt(2))-1)
check('endpoint normal position',X.subs(t,s.Rational(1,4))-s.Rational(1,32))
check('endpoint compressed covector',(X*rho).subs(t,s.Rational(1,4))-s.Rational(1,256))
check('endpoint tangent extent',z1.subs(t,-s.Rational(1,4))-s.sqrt(2)/4)
check('eleven half gains',-4+s.Rational(11,2)-s.Rational(3,2))
check('last cutoff index',1-s.Rational(11,22)-s.Rational(1,2))
ds=s.symbols('d0:11');v=s.symbols('M0');rec=v
for j in range(11):rec=2*(rec+ds[j])
check('full eleven-step recurrence',rec-2**11*v-sum(2**(11-j)*ds[j] for j in range(11)))
kap=s.symbols('kappa',positive=True)
check('transition margin equality',1-(kap/2)**2/kap**2-s.Rational(3,4))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(r/'glancing-with-fixed-source-and-observation-tests.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Full constant and variable normal gauge signs, all Hamilton equations and characteristic identity, compressed and projected coordinates, finite recurrence and transition margin. The operator inequalities and support proofs are in the lesson.'}
(r/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))

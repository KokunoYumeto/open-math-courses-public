"""Exact finite checks of the two-root transformation and signs. CC0-1.0."""
from pathlib import Path
import json,hashlib
import sympy as s
PTH=Path(__file__).resolve().parent
checks=[]
def ck(name,value):
    parts=list(value) if isinstance(value,s.MatrixBase) else [value]
    assert all(s.simplify(x)==0 for x in parts),(name,value)
    checks.append({'name':name,'passed':True})
beta,c,xi,t,rho=s.symbols('beta c xi t rho',positive=True)
lp=(-beta+c)*xi;lm=(-beta-c)*xi
T=s.Matrix([[1,1],[lp/xi,lm/xi]])
M=s.Matrix([[0,xi],[-(beta**2-c**2)*xi,-2*beta*xi]])
ck('both principal eigenvectors',M*T-T*s.diag(lp,lm))
ck('normalized determinant is the negative gap',T.det()+2*c)
ck('principal inverse on both sides',T.inv()*T-s.eye(2))
ct=s.Function('c')(t)
Tv=s.Matrix([[1,1],[ct,-ct]])
H=s.I*Tv.inv()*s.diff(Tv,t)
ck('full time derivative term',H-s.I*s.diff(ct,t)/(2*ct)*s.Matrix([[1,-1],[-1,1]]))
kp=s.I*s.diff(ct,t)/(4*ct**2*xi)
km=-kp
ck('plus-minus Sylvester sign',H[0,1]+2*ct*xi*kp)
ck('minus-plus Sylvester sign',H[1,0]-2*ct*xi*km)
amp=ct**s.Rational(-1,2)
ck('scalar density transport',s.diff(amp,t)+s.diff(ct,t)/(2*ct)*amp)
A=s.Matrix([[0,1],[0,0]]);B=s.Matrix([[0,0],[1,0]])
I=s.eye(2);O=s.zeros(2)
D=s.BlockMatrix([[rho*I,O],[O,-rho*I]]).as_explicit()
E=s.BlockMatrix([[O,A],[B,O]]).as_explicit()
K=s.BlockMatrix([[O,-A/(2*rho)],[B/(2*rho),O]]).as_explicit()
D1=s.BlockMatrix([[A*B/(2*rho),O],[O,-B*A/(2*rho)]]).as_explicit()
ck('matrix off-diagonal cancellation',D*K-K*D+E)
ck('ordered diagonal correction',E*K-D1)
ck('complete corrected intertwining residual',(D+E)*(s.eye(4)+K)-(s.eye(4)+K)*(D+D1)+K*D1)
ck('noncommuting products are distinct',A*B-B*A-s.diag(1,-1))
x,tau=s.symbols('x tau',real=True)
be=s.Function('b')(t,x);cc=s.Function('v')(t,x)
rp=(-be+cc)*xi;rm=(-be-cc)*xi
p=(tau-rp)*(tau-rm)
for root,name in [(rp,'plus'),(rm,'minus')]:
    den=s.diff(p,tau).subs(tau,root)
    ck(name+' Hamilton spatial sign',s.diff(p,xi).subs(tau,root)/den+s.diff(root,xi))
    ck(name+' Hamilton frequency sign',-s.diff(p,x).subs(tau,root)/den-s.diff(root,x))
    ck(name+' time covector sign',-s.diff(p,t).subs(tau,root)/den-s.diff(root,t))
    ck(name+' root derivative along flow',s.diff(root,t)-s.diff(root,x)*s.diff(root,xi)+s.diff(root,xi)*s.diff(root,x)-s.diff(root,t))
ck('figure plus ray velocity',-s.diff(lp,xi).subs({beta:s.Rational(1,4),c:1})+s.Rational(3,4))
ck('figure minus ray velocity',-s.diff(lm,xi).subs({beta:s.Rational(1,4),c:1})-s.Rational(5,4))
f=s.Function('f')
u=(f(x+t)-f(x-t))/2
ck('travelling profiles solve wave equation',s.diff(u,t,2)-s.diff(u,x,2))
ck('two initial positions cancel',u.subs(t,0))
ck('initial velocity is profile derivative',s.diff(u,t).subs(t,0)-s.diff(f(x),x))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),
 'numerical_checks':0,'checks':checks,'source_sha256':sha(PTH/'two-branch-matrix-cauchy-wavefronts.md'),
 'script_sha256':sha(Path(__file__)),'finite_checks_are_not_the_analytic_proof':True}
(PTH/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='checks'}))

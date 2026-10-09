"""Exact identities; the analytic uniform estimates are proved in the lesson."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
cases=[]
def check(name,expression):
    assert S.simplify(expression)==0,(name,expression)
    cases.append({'name':name,'passed':True})
a,x,z1,z2,z3,e1,e2,e3=S.symbols('a x z1 z2 z3 e1 e2 e3',real=True)
lam=S.sqrt(e1**2+e2**2+e3**2)
r=(1+a)*e1**2+e2**2-e3**2+x*e3**2
N=z1*lam/(2*(1+a)*e1)
v2=z2-e2*z1/((1+a)*e1)
v3=z3+e3*z1/((1+a)*e1)
def H(f):return sum(S.diff(r,e)*S.diff(f,z) for e,z in zip([e1,e2,e3],[z1,z2,z3]))
check('exact homogeneous clock',H(N)-lam)
check('second boundary-flow invariant',H(v2))
check('third invariant full normal error',H(v3)-2*x*e3)
anchor={e1:1/S.sqrt(2+a),e2:0,e3:S.sqrt(1+a)/S.sqrt(2+a)}
check('anchor characteristic',r.subs(x,0).subs(anchor))
check('anchor normalization',(lam**2).subs(anchor)-1)
check('first clock-coordinate speed',S.diff(r,e1).subs(anchor)-2*(1+a)/S.sqrt(2+a))
check('third clock-coordinate speed',S.diff(r,e3).subs(x,0).subs(anchor)+2*S.sqrt(1+a)/S.sqrt(2+a))
scale=S.symbols('scale',positive=True)
check('clock degree zero',N.subs({e1:scale*e1,e2:scale*e2,e3:scale*e3},simultaneous=True)-N)
check('second invariant degree zero',v2.subs({e1:scale*e1,e2:scale*e2,e3:scale*e3},simultaneous=True)-v2)
check('third invariant degree zero',v3.subs({e1:scale*e1,e2:scale*e2,e3:scale*e3},simultaneous=True)-v3)
nu=S.symbols('nu',positive=True);c0=S.exp(-1/nu)
check('flat cutoff derivative identity',c0-nu**2*S.diff(c0,nu))
A,delta,eps,M,L,hp,hr,k,chi1,chi1p=S.symbols('A delta eps M L hp hr k chi1 chi1p',positive=True)
hpq=-S.diff(c0,nu)*chi1*hp/(A*delta)+c0*chi1p*hr/(eps*delta)
b2=L*S.diff(c0,nu)*chi1/(4*A*delta)
e2square=c0*chi1p*hr/(eps*delta)
psi2=S.diff(c0,nu)*chi1*(hp/(A*delta)-M*L*nu**2-L/(4*A*delta))
check('complete characteristic square',hpq+M*L*c0*chi1+psi2+b2-e2square)
q,Hq,psq,bsq,esq=S.symbols('q Hq psq bsq esq',real=True)
check('anti-Hermitian leading cancellation',(Hq-2*k*q+(M*L+2*k)*q+bsq-esq)-(Hq+M*L*q+bsq-esq))
check('damping margin at exact threshold',(1/(4*A*delta)-16*M/A**2-1/(8*A*delta)).subs(A,128*M*delta))
s=S.symbols('s',real=True);Ms=2*s**2+3;As=8*Ms
check('exercise damping threshold',128*Ms*S.Rational(1,16)-As)
check('exercise positive margin',(1/(4*A*delta)-16*M/A**2-1/(8*A*delta)).subs({A:As,delta:S.Rational(1,16),M:Ms}))
X=S.symbols('X',real=True);profile=S.exp(-A/(S.Rational(3,2)-X))
check('normal-slice midpoint',profile.subs(X,S.Rational(3,4))-S.exp(-4*A/3))
count=S.symbols('count',positive=True,integer=True);j=S.symbols('j',integer=True)
theta=lambda i:1-i/(2*count)
check('first nested index',theta(0)-1)
check('fixed last nested index',theta(count)-S.Rational(1,2))
check('strict consecutive gap',theta(j)-theta(j+1)-1/(2*count))
check('total half-order gain',sum([S.Rational(1,2)]*12)-6)
check('normal interpolation midpoint',(s+S.Rational(1,2)+s-S.Rational(3,2))/2-(s-S.Rational(1,2)))
check('first trace index',((s)+(s-1))/2-(s-S.Rational(1,2)))
check('normal trace index',((s-1)+(s-2))/2-(s-S.Rational(3,2)))
n=S.symbols('n',positive=True,integer=True);y=S.symbols('y',real=True)
check('periodic derivative',-S.I*S.diff(S.exp(S.I*n*y),y)-n*S.exp(S.I*n*y))
for parameter in [-S.Rational(1,4),S.Integer(0),S.Rational(1,4)]:
    speed=2*(1+parameter)/S.sqrt(2+parameter)
    assert speed>0
    cases.append({'name':'positive clock speed at a='+str(parameter),'passed':True})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,
 'source_sha256':sha(ROOT/'uniform-half-order-gain-at-glancing.md'),'script_sha256':sha(Path(__file__)),
 'scope':'Exact clock, invariant, characteristic-completion, damping, trace-index and fixed-support identities. These checks do not prove operator bounds or uniform PDE propagation.',
 'cases':cases}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))

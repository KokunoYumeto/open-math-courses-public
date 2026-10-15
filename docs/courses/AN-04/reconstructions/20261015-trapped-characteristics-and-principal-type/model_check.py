"""Exact normalization, stationary-symbol and turn checks; not a geometry verifier."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
source=root/'trapped-characteristics-and-the-escape-criterion.md'
cases=[]
def check(name,condition):
 assert condition,name
 cases.append({'name':name,'kind':'exact_algebra','passed':True})
for i,(a,b) in enumerate([(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)),(F(2),F(3)),(F(-3),F(4))]):
 for sign in (-1,1):
  den=a*a+b*b;cr=sign*a/den;ci=-sign*b/den
  check(f'oriented-real-component-{i}-{sign}',cr*a-ci*b==sign)
  check(f'oriented-imaginary-component-{i}-{sign}',cr*b+ci*a==0)
  check(f'exact-multiplier-norm-{i}-{sign}',(cr*cr+ci*ci)*den==1)
t,tau,theta=s.symbols('t tau theta',real=True)
p=s.exp(s.I*t)*tau
check('rotating-time-Hamilton-component',s.simplify(s.diff(p,tau)*s.exp(-s.I*t))==1)
check('rotating-radial-correction-zero-on-char',s.simplify(s.diff(p,t).subs(tau,0))==0)
check('stationary-symbol-gradient',s.diff(tau**2,tau).subs(tau,0)==0)
check('stationary-Hamilton-field',2*tau.subs(tau,0)==0)
aa,bb=s.symbols('aa bb',positive=True)
check('flat-angle-reflection',s.simplify(s.pi*aa/(aa+bb)+s.pi*bb/(aa+bb)-s.pi)==0)
check('turn-speed-square',s.trigsimp((-s.cos(theta))**2+s.sin(theta)**2)==1)
for eps,S0 in [(F(1,10),F(1,3)),(F(1,7),F(2,5)),(F(1,20),F(1,2))]:
 lam=eps/S0
 check(f'turn-positive-speed-{eps}',lam>0 and lam*S0==eps)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'schema':'AN04-trapped-characteristics-finite-checks/v1','source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,
 'cases':cases,'scope':'Exact oriented multiplier, rotating homogeneous symbol, stationary characteristic gradient, reflection and turn-speed identities.',
 'not_established_by_finite_checks':['compact_limiting_curve','active_leaf_connectedness','embedded_admissible_corridors','full_trapping_equivalence','full_course_completion']}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','total_cases','exact_algebraic_checks')}))

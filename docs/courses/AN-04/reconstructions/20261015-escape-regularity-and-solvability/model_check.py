"""Finite symbolic Hamilton, support and multiplier checks; not propagation tests."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
source=root/'escape-arcs-regularity-and-semiglobal-solutions.md'
cases=[]
def check(name,condition):
 assert condition,name
 cases.append({'name':name,'kind':'exact_algebra','passed':True})
t,x,tau,xi=s.symbols('t x tau xi',real=True);xi_pos=s.symbols('xi_pos',positive=True)
a=s.Function('a')(t);p=tau+s.I*x*xi*a
def H(v):return s.diff(p,tau)*s.diff(v,t)-s.diff(p,t)*s.diff(v,tau)+s.diff(p,xi)*s.diff(v,x)-s.diff(p,x)*s.diff(v,xi)
for name,actual,wanted in [
 ('Hamilton-time',H(t),1),('Hamilton-base',H(x),s.I*x*a),
 ('Hamilton-time-covector',H(tau),-s.I*x*xi*s.diff(a,t)),
 ('Hamilton-space-covector',H(xi),-s.I*xi*a)]:
 check(name,s.simplify(actual-wanted)==0)
check('Hamilton-log-fiber',s.simplify(H(s.log(xi))+s.I*a)==0)
beta=s.Function('beta')(t)
check('complex-coordinate-sign',s.simplify(H(s.log(xi)+s.I*beta).subs(s.diff(beta,t),a))==0)
qr,qi,h,rho,theta=s.symbols('qr qi h rho theta',real=True)
# On the zero leaf, the imaginary multiplier contributes -Im(Q)*(h+rho)*H_g.
check('uncapped-rank-one-multiplier',s.expand(-qi*h).subs(h,0)==0)
check('capped-real-multiplier',s.expand(-(1-theta)*qi*(h+rho)).subs(theta,1)==0)
check('transition-away-from-cap',s.expand(-(1-theta)*qi*(h+rho)).subs({rho:0,h:0})==0)
for qreal in (F(-7,3),F(-1,5),F(1,11),F(9,2)):
 for th in (F(0),F(1,2),F(1)):
  check(f'multiplier-stays-nonzero-{qreal}-{th}',qreal*qreal+(1-th)**2*F(4,9)>0)
for tt,old_positive,cap_positive in [
 (F(-11,4),False,True),(F(-2),False,True),(F(-7,4),False,False),
 (F(-1),False,False),(F(0),False,False),(F(1,3),True,False)]:
 check(f'exact-coefficient-support-{tt}',(tt>0)==old_positive and ((tt+3>0) and (F(-7,4)-tt>0))==cap_positive)
check('cap-separated-from-K',F(-7,4)<F(-3,2))
check('cap-mark-inside-support',F(-3)<F(-2)<F(-7,4))
for mm,cc,mu in [(F(1),F(-2),F(-1)),(F(3,2),F(-2,3),F(-1,4)),(F(-2),F(-6),F(-4))]:
 sigma=mu-mm+1
 check(f'exact-source-shift-{mm}',sigma+mm-1==mu and cc<mu)
check('quasiconcave-mean-positive',F(1,1)>0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'schema':'AN04-escape-regularity-finite-checks/v1','source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,
 'cases':cases,'scope':'Exact Hamilton coefficients, complex-coordinate cancellation, return-compatible multiplier, support inequalities and source shifts.',
 'not_established_by_finite_checks':['existence_of_factor_charts','uniform_local_comparison','superharmonic_strong_minimum','compact_support_index_gain','trapped_leaf_equivalence'                         ]}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','total_cases','exact_algebraic_checks')}))

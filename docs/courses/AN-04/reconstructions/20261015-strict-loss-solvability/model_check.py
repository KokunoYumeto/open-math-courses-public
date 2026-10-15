"""Exact finite order and sequence checks; analytic proofs are in the lesson."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
root=Path(__file__).resolve().parent
source=root/'strict-sobolev-loss-and-compact-solvability.md'
cases=[]
def check(name,condition):
 assert condition,name
 cases.append({'name':name,'passed':True,'kind':'exact_algebra'})
triples=[(F(3,2),F(-2,3),F(-5,12)),(F(0),F(0),F(-2)),
 (F(-3,2),F(7,3),F(-2,3)),(F(4,3),F(1,7),F(1,8)),
 (F(-2),F(-3),F(-7)),(F(2),F(3),F(7,2)),
 (F(1),F(-1,2),F(-3,4)),(F(7,4),F(-4),F(-7,2))]
for i,(m,s,t) in enumerate(triples):
 eps=s+m-1-t;r=-t;q=r+m-1-eps
 check(f'positive-target-gap-{i}',eps>0)
 check(f'reciprocal-test-order-{i}',q==-s)
 check(f'solution-order-{i}',-r==t)
for j in range(1,7):
 m=F(j,3);r=F(-j,4);eps=F(1,j)
 q=r+m-1-eps
 check(f'graph-output-order-{j}',q-1-m==r-2-eps)
for j in range(4,11):
 check(f'second-derivative-summable-tail-{j}',F(-j*j+2*j)<=F(-j*j,2)<=-j)
for j in range(1,6):
 check(f'fourier-derivative-obstruction-{j}',F(2**(2*j))*F(1,2**(j+1))==F(2**(j-1)))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'schema':'AN04-strict-loss-solvability-finite-checks/v1',
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),
 'numerical_checks':0,'cases':cases,
 'scope':'Finite reciprocal-order identities, full lower graph order, selected exact derivative tails and Fourier coefficients.',
 'not_established_by_finite_checks':['adjoint_gain_hypothesis','characteristic_escape_equivalence','geometric_regularity_theorem','uniform_operator_estimates','full_course_completion']}
(root/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','total_cases','exact_algebraic_checks')}))

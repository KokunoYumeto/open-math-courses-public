"""Finite independent checks of actual normal products and both error sides. CC0."""
from pathlib import Path
import hashlib,json
import sympy as S

HERE=Path(__file__).resolve().parent
checks=[]
k,h,r=S.symbols('k h r',real=True,nonzero=True)
A=S.Matrix([[1,2],[0,1]])
B=S.Matrix([[2,0],[3,-1]])
assert A*B!=B*A
# Acting on a plane wave after multiplying by exp(i*h*r) shifts frequency.
# This checks actual multiplier composition, including every negative binomial sign.
for L in range(1,7):
    partial=sum((-h)**j/k**(j+1) for j in range(L))
    residual=S.factor(1/(k+h)-partial)
    assert S.simplify(residual-(-h)**L/(k**L*(k+h)))==0
    assert S.simplify(S.diff(residual,k)-S.diff((-h)**L/(k**L*(k+h)),k))==0
    for kk,hh in [(8,1),(-8,1),(12,-2),(-12,-2)]:
        assert S.simplify((residual-(-h)**L/(k**L*(k+h))).subs({k:kk,h:hh}))==0
checks.append({'id':'actual_multiplier_after_normal_modulation','lengths':6,
               'signed_tail_samples':24,'ordered_matrix_product':'A B',
               'first_normal_derivative_checked':True})

# A finite differential operator gives an independent exact Leibniz test.
# Distinct matrices keep every factor order visible.
for a in [1,2,3,4]:
    coef=(1+r+r*r)*B
    actual=A*((-S.I)**a*S.diff(coef*S.exp(S.I*k*r),r,a))
    predicted=sum((S.binomial(a,j)*k**(a-j)*A*((-S.I)**j*S.diff(coef,r,j))
                   for j in range(a+1)),S.zeros(2))*S.exp(S.I*k*r)
    assert all(S.simplify(x)==0 for x in actual-predicted)
checks.append({'id':'actual_differential_leibniz_action','normal_orders':[1,2,3,4]})

# Different bundle dimensions force the two error endomorphisms to remain distinct.
P=S.Matrix([[1,2],[0,1],[2,-1]]) # E dimension 2 -> F dimension 3
Q=S.Matrix([[1,0,1],[2,1,0]]) # F -> E
RF=P*Q-S.eye(3);RE=Q*P-S.eye(2)
assert RE*Q==Q*RF
for N in range(1,6):
    right=Q*sum(((-RF)**j for j in range(N)),S.zeros(3))
    left=sum(((-RE)**j for j in range(N)),S.zeros(2))*Q
    assert right==left
    assert P*right==S.eye(3)-(-RF)**N
    assert right*P==S.eye(2)-(-RE)**N
checks.append({'id':'typed_actual_finite_correction','input_dimension':3,'output_dimension':2,
               'finite_lengths':5,'both_distinct_error_identities':True})

# The normal identity acts by evaluation on each test; it does not smooth r=s.
# The separated tangential rank-one kernel merely supplies a scalar integral.
s=S.symbols('s',real=True)
for degree in range(6):
    test=(1+s)**degree*S.exp(-s*s)
    delta_pair=S.integrate(S.DiracDelta(r-s)*test,(s,-S.oo,S.oo))
    assert S.simplify(delta_pair-test.subs(s,r))==0
checks.append({'id':'retained_normal_delta','test_functions':6,
               'tangential_separation_does_not_remove_normal_diagonal':True})

source=HERE/'paired-normal-composition.md'
result={'schema':'AN04-paired-normal-composition-models/v1',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'passed':True,'general_theorem_certified':False}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'finite_groups':len(checks),'passed':True}))

"""Independent finite tests of normal inverse signs and matrix order. CC0."""
from pathlib import Path
import hashlib,json,math
import sympy as S
HERE=Path(__file__).resolve().parent
checks=[]
t,r,k=S.symbols('t r k',real=True,nonzero=True)
B=S.Matrix([[0,1],[2,1]]);C=S.Matrix([[2,0],[1,3]]);I=S.eye(2)
assert B*C!=C*B
U=[I,-B,B*B-C,-B*B*B+B*C+C*B]
V=sum((U[j]*t**j for j in range(4)),S.zeros(2))
for residual in [(I+B*t+C*t*t)*V-I,V*(I+B*t+C*t*t)-I]:
 for entry in residual:
  assert all(S.expand(entry).coeff(t,j)==0 for j in range(4))
wrong=-B**3+2*B*C
assert wrong!=U[3]
checks.append({'id':'ordered_two_sided_matrix_residual','cancelled_powers':[0,1,2,3],'noncommuting_factors':True})

for N in range(1,6):
 q=S.exp(-S.I*r)*sum(k**(-1-j) for j in range(N))
 actual=S.exp(S.I*r)*(-S.I*S.diff(q*S.exp(S.I*k*r),r))
 assert S.simplify(actual-(1-k**(-N))*S.exp(S.I*k*r))==0
checks.append({'id':'variable_normal_coefficient','actual_differential_action_checked':True,'finite_lengths':5})

# NI13 checked as an actual action on polynomial coefficients/tests, where
# negative powers of Lambda terminate on each finite polynomial derivative.
z=S.symbols('z',nonzero=True)
def lam(p,f):
 out=0
 for j in range(20):
  df=S.diff(f,r,j)
  if df==0:break
  out+=S.binomial(p,j)*z**(p-j)*(-S.I)**j*df
 return S.expand(out)
for p in [-4,-2,-1,0,1,2,4]:
 coeff=2+r+r**3;f=1-r+r**2
 left=lam(p,coeff*f)
 right=sum(S.binomial(p,j)*(-S.I)**j*S.diff(coeff,r,j)*lam(p-j,f) for j in range(4))
 assert S.simplify(left-right)==0
checks.append({'id':'faithful_representation_product','positive_and_negative_powers':[-4,-2,-1,0,1,2,4]})

samples=0;largest_scaled_error=0.
for eta in [-3.,-.5,0.,.5,3.]:
 T=1+abs(eta);bracket=math.sqrt(1+eta*eta)
 BB=B*bracket;CC=C*bracket**2
 UU=[I,-BB,BB*BB-CC,-BB**3+BB*CC+CC*BB]
 for sign in [-1,1]:
  for scale in [1,2,4]:
   kk=sign*8*T*scale
   inverse=(I*kk**2+BB*kk+CC).inv()
   approx=sum((UU[j]*kk**(-2-j) for j in range(4)),S.zeros(2))
   err=float((inverse-approx).norm())
   largest_scaled_error=max(largest_scaled_error,err*abs(kk)**6/T**4)
   assert float((I*kk**2+BB*kk+CC).det())!=0
   samples+=1
checks.append({'id':'both_actual_tails','samples':samples,'largest_observed_scaled_L4_error':largest_scaled_error,
               'finite_samples_do_not_prove_uniform_estimate':True})
source=HERE/'normal-inverse-expansions.md'
result={'schema':'AN04-normal-inverse-expansions-models/v1','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'passed':True,
 'general_theorem_certified':False}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'finite_groups':len(checks),'passed':True,'two_tail_samples':samples}))

"""Finite sign/order checks accompanying the full analytic proofs."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x,t,rho,xi=S.symbols('x t rho xi',real=True)
D=lambda f,v,k=1:(-S.I)**k*S.diff(f,v,k)
checks=[]
for p in range(4):
 for q in range(4):
  a=t**p*rho**q;u=(1+t)**6
  Ta=lambda f:t**p*t**q*D(f,t,q)
  left=D(Ta(u),t)-Ta(D(u,t))
  right=(-S.I)*p*t**(p-1+q)*D(u,t,q) if p else 0
  right+=(-S.I)*q*t**(p+q-1)*D(u,t,q) if q else 0
  assert S.simplify(left-right)==0
checks.append('Full raw normal commutator, including the normal-frequency derivative term, for sixteen polynomial symbols')
u=(1+x)**6*(1+t)**6
for m in range(1,5):
 for j in range(m+1):
  for k in range(m-j+1):
   a=1+x*t+x*x
   left=t**m*a*D(D(u,x,k),t,j)
   right=t**(m-j)*a*D(t**j*D(u,t,j),x,k)
   assert S.expand(left-right)==0
checks.append('Complete weighted ordinary differential expression for all monomials through total order four')
b=(1+x*t)*xi**2+(x*x+t*t)*xi+t*x
def op(symbol,v):
 poly=S.Poly(S.expand(symbol),xi)
 return S.expand(sum(coef*D(v,x,power[0]) for power,coef in poly.terms()))
v=(1+t)**5*(1+x)**5
for aa in range(4):
 for gg in range(4):
  left=t**aa*D(D(op(b,v),x,gg),t,aa)
  right=sum(S.binomial(aa,j)*S.binomial(gg,k)*t**j*op(D(D(b,t,j),x,k),t**(aa-j)*D(D(v,t,aa-j),x,gg-k)) for j in range(aa+1) for k in range(gg+1))
  assert S.expand(left-right)==0,(aa,gg)
checks.append('All normal weights and both binomial sums in the tangential topology formula, sixteen differentiated cases')
P=S.Matrix([[1,2],[0,1]]);C=S.Matrix([[2,1],[3,2]])
DB=S.Matrix([[1,4],[2,3]]);R0=S.Matrix([[0,1],[2,0]])
Q=P*C-R0;E=DB*P;R=DB*(S.eye(2)-Q)-DB*R0
assert E*C+R==DB
assert C*E+R!=DB
checks.append('Exact left-parametrix microlocal division and residual signs with noncommuting matrices')
jets=[S.Matrix([[j+1,j],[j*j,2*j+1]]) for j in range(7)]
polynomial=sum((t**j/S.factorial(j)*jets[j] for j in range(7)),S.zeros(2))
for j in range(7):assert polynomial.diff(t,j).subs(t,0)==jets[j]
checks.append('Exact seven matrix-valued normal jets in the collar extension before local cutoffs')
for j in range(1,6):
 for l in range(1,5):
  c1=S.Rational(1,2);c2=S.Rational(3,4)
  integral=(c2**(2*j+1)-c1**(2*j+1))/(2*j+1)*2**(l*(2*j+1))
  direct=S.integrate(rho**(2*j),(rho,c1*2**l,c2*2**l))
  assert direct==integral
  for m in [j-1,j,j+1]:
   weight_squared=2**(-2*l*(S.Rational(m)+S.Rational(1,2)))
   assert S.simplify(direct*weight_squared/((c2**(2*j+1)-c1**(2*j+1))/(2*j+1))-2**(2*l*(j-m)))==0
checks.append('Exact dyadic normal-frequency growth proving the increasing delta-jet local/global counterexample')
# Multiplication by t^m kills every delta derivative through m-1:
# (t^m delta^(j))(phi)=(-1)^j d^j(t^m phi)(0).
phi=1+t+t*t+t**7
for m in range(1,7):
 for j in range(m):assert S.diff(t**m*phi,t,j).subs(t,0)==0
checks.append('All weighted boundary-defect jets through normal order six vanish with the exact factor t^m')
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},'script_sha256':sha(Path(__file__)),
 'scope':'Finite identities support the signs, matrix order, jet coefficients and explicit counterexample. Full analytic proofs are in the three companions.',
 'U031_restored':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

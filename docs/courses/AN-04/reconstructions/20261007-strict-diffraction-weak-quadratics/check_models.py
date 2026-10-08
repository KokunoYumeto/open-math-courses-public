"""Exact sign, order and matrix checks; these do not replace the proofs."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
groups=[]
count=0
for a in [s.Integer(1),s.Integer(2),s.Integer(3)]:
 for b in [s.Integer(0),s.Integer(1),s.Integer(2)]:
  for gamma in [s.Rational(1,2),s.Integer(1)]:
   for r in [s.Integer(-2),s.Integer(0),s.Integer(3)]:
    integral=1/(2*a+b)
    weak=(a*(a+b)-r)*gamma*integral
    interior=-(a*a+r)*gamma*integral
    boundary=a*gamma
    normal_energy=a*a*gamma*integral
    commutator=a*b*gamma*integral
    tangential=-r*gamma*integral
    assert s.simplify(weak-interior-boundary)==0
    assert s.simplify(weak-normal_energy-commutator-tangential)==0
    count+=1
groups.append({'name':'Actual normal Green term and parameter commutator, WQ14/WQ34','cases':count})
L=s.Matrix([[0,1],[0,0]]);M=s.Matrix([[s.I,1],[0,-2]]);v=s.Matrix([1,1])
inner=lambda a,b:(b.conjugate().T*a)[0]
count=0
for gamma in [s.Rational(1,8),s.Rational(1,4),s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(3)]:
 z=(inner(L*s.I*v,gamma*v)+inner(M*v,s.I*gamma*v))/2
 assert s.simplify(z-gamma*(1+2*s.I)/2)==0
 magnitude=s.sqrt(s.expand_complex(z*s.conjugate(z)))
 bound=s.sqrt(5)*(1+gamma**2)/4
 assert s.simplify(bound-magnitude-s.sqrt(5)*(gamma-1)**2/4)==0
 count+=1
groups.append({'name':'Both non-Hermitian lower factors and exact mean-order balance, WQ36/WQ37','cases':count})
a0,a1,a2,b0,b1,g,r,t=s.symbols('a0 a1 a2 b0 b1 g r t',real=True)
B=s.Matrix([[a0+b0*b0+g*r,a1/2+b0*b1],[a1/2+b0*b1,a2+b1*b1-g]])
v=s.Matrix([1,t])
assert s.expand((v.T*B*v)[0]-(a0+a1*t+a2*t*t+(b0+b1*t)**2-g*(t*t-r)))==0
groups.append({'name':'The full ordered-array principal polynomial has the GR and G signs in WQ25','cases':1})
count=0
for j in range(2):
 for k in range(2):
  order=s.Rational(2*j-1,2)+(1-j-k)+s.Rational(2*k-1,2)
  assert order==0
  assert s.Rational(-1,2)+s.Rational(1,2)-j==-j
  count+=1
groups.append({'name':'Mixed order-zero conjugation and exact lower weights, WQ10/WQ11','cases':count})
a=s.Rational(528,31);b=s.Rational(2080,63);d=b-a
B=s.Matrix([[1,a],[1,b]]);inverse=s.Matrix([[b,-a],[-1,1]])/d
assert d==s.Rational(31216,1953) and B*inverse==s.eye(2) and inverse*B==s.eye(2)
groups.append({'name':'Two-sided exact inverse of the normalized commutant rows, WQ38','cases':1})
result={'passed':True,'groups':groups,'total_cases':sum(x['cases'] for x in groups),
 'source_sha256':hashlib.sha256((ROOT/'weak-characteristic-quadratic-estimates.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'finite_checks_do_not_replace_proofs':True,'strict_diffraction_propagation_proved':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

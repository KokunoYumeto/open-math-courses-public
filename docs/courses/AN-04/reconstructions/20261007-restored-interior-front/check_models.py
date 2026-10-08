"""Finite diagnostics for order bookkeeping and noncommuting algebra; not proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
groups=[];count=0
for k in [s.Integer(0),s.Rational(1,2),s.Integer(1),s.Integer(3)]:
 for radius in [1,2,4,8]:
  w=s.sqrt(1+radius**2)
  assert s.simplify((w**k)**2*w**2-w**(2*(k+1)))==0
  assert s.simplify((w**(k+1))**2/w**2-w**(2*k))==0
  assert s.simplify((w**k)**2/w**2-w**(2*k))!=0
  count+=1
groups.append(dict(name='opposite Sobolev baseline shifts and missing forcing order',cases=count,passed=True))
N1=s.Matrix([[0,1],[0,0]]);N2=s.Matrix([[0,0],[1,0]]);I=s.eye(2);count=0
for a in [-2,0,1]:
 for b in [-1,0,3]:
  M=(I+b*N2)*(I+a*N1);H=s.Matrix([[1+a*b,-a],[-b,1]])
  assert M==s.Matrix([[1,a],[b,1+a*b]]) and M.det()==1 and M*H==H*M==I
  assert M*s.Matrix([0,1])==s.Matrix([a,1+a*b])
  if a*b:assert (I+a*N1)*(I+b*N2)!=M
  count+=1
fig=json.loads((root/'figure-check.json').read_text())
states=[s.Matrix(x) for x in fig['states']]
assert (I+N1)*states[0]==states[1] and (I+N2)*states[1]==states[2]
assert fig['exact_orders']=={'solution_b':3,'solution_ordinary':4,'source_b':4,'source_ordinary':3}
groups.append(dict(name='ordered nilpotent pulse matrices, both inverses and exact figure states',cases=count+1,passed=True))
D,A,B,Q,L=s.symbols('D A B Q L',commutative=False)
assert s.expand(D*B-((D-B*Q*L*A)*B+B*Q*L*(A*B-1)+B*Q*L))==0
groups.append(dict(name='complete three-term conjugation defect with noncommuting factors',cases=1,passed=True))
t=s.symbols('t',real=True)
for length in [s.Rational(1,2),s.Integer(1),s.Integer(3)]:
 norm_g=5*length
 norm_primitive=s.integrate(5*(t-length/2)**2,(t,0,length))
 assert norm_primitive==5*length**3/12 and norm_primitive<=length**2*norm_g
groups.append(dict(name='actual vector primitive centered inside the interval and squared L2 bound',cases=3,passed=True))
record=dict(schema='AN04-interior-front-models/v1',passed=True,groups=groups,
 source_sha256=sha(root/'interior-energy-fronts-and-matrix-propagation.md'),script_sha256=sha(Path(__file__)),
 figure_svg_sha256=fig['svg_sha256'],sympy_version=s.__version__,general_theorem_certificate=False,
 scope='Exact finite order and matrix diagnostics. Complete variable-coefficient, distributional and all-order proofs are in the lesson and linked programme providers.')
(root/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'groups':len(groups),'cases':sum(x['cases'] for x in groups),'general_theorem_certificate':False}))

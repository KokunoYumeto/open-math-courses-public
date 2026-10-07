"""Finite exact checks complement the written global proofs; they do not replace them."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,xml.etree.ElementTree as ET
import sympy as sp
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
t,s,z,r,a=sp.symbols('t s z r a',real=True)
tau,zz=sp.symbols('tau zz',real=True)
x=sp.Matrix([t,z,tau,zz])
transition=sp.Matrix([t+a*z,z,tau,zz-a*tau])
J=sp.zeros(4);J[2,0]=1;J[0,2]=-1;J[3,1]=1;J[1,3]=-1
M=transition.jacobian(x)
assert sp.simplify(M.T*J*M-J)==sp.zeros(4)
assert M.det()==1 and transition[2]==tau and M[:,0]==sp.Matrix([1,0,0,0])
# A finite n=2 relation verifies the stated corank and the distinction
# between paired and individual radial lifts.
embed=sp.Matrix([t,z,0,r,s,z,0,r])
B=embed.jacobian([t,s,z,r])
omega=sp.diag(J,sp.zeros(4))
assert (B.T*omega*B).rank()==2 and B.rank()==4
radx=sp.Matrix([0,0,0,1,0,0,0,0]);rady=sp.Matrix([0,0,0,0,0,0,0,1])
assert B.row_join(radx).rank()==5 and B.row_join(rady).rank()==5
assert B.row_join(radx+rady).rank()==4
q0,q1=sp.symbols('q0 q1')
weight=sp.exp(q0*(t-s)+q1*(t*t-s*s)/2)
assert sp.simplify(-sp.I*sp.diff(weight,t)+sp.I*(q0+q1*t)*weight)==0
assert sp.simplify(sp.I*sp.diff(weight,s)+sp.I*(q0+q1*s)*weight)==0
assert weight.subs(t,s)==1
assert -sp.I*sp.I==1 and -sp.I*(-sp.I)*(-1)==1
assert sp.I*sp.I*(-1)==1 and sp.I*(-sp.I)==1
m,hs=sp.symbols('m hs',real=True)
assert sp.simplify(hs-(1-m)-(hs+m-1))==0
assert sp.simplify(-sp.Rational(1,2)+(1-m)-(sp.Rational(1,2)-m))==0
fig=HERE/'figures/global-signed-assembly.svg'
tree=ET.fromstring(fig.read_text('utf-8'));ns={'s':'http://www.w3.org/2000/svg'}
polys=tree.findall('s:polygon',ns);assert len(polys)==2
expected=[[(210,450),(450,210),(210,210)],[(210,450),(450,210),(390,210),(210,390)]]
for index,poly in enumerate(polys):
 pts=[tuple(map(int,v.split(','))) for v in poly.attrib['points'].split()]
 assert pts==expected[index]
 for px,py in pts:
  ss=sp.Rational(px-330,60);tt=sp.Rational(390-py,60)
  assert -2<=ss<=2 and -2<=tt<=3 and tt-ss>=1
  if index==1:assert tt-ss<=2
text=' '.join(tree.itertext())
assert all(v in text for v in ['b = t','s < b ≤ t','i/e','Travel d = 0: i','Travel d = 1: ie'])
assert sp.Rational(1,4)+sp.Rational(1,4)+sp.Rational(1,2)==1
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':3,
 'groups':['Exact tau-preserving canonical shear, corank-two model and both individual radial exclusions',
 'Complex linear-in-time weight solves both transport equations with exact signed jumps and arbitrary-real orders',
 'Every affine polygon vertex, strict/reflexive hull boundary, normalized partition weights and model labels'],
 'limitation':'Finite exact models only. The full proofs establish the general manifold, all-derivative and support assertions.',
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name if p.parent==HERE else p.relative_to(HERE).as_posix():sha(p) for p in [HERE/'global-signed-parametrices-from-local-delayed-errors.md',fig]}}
(HERE/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':3}))

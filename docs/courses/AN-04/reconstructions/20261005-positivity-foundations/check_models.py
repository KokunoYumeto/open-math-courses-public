"""Finite exact diagnostics; the companion text supplies the general proofs."""
from pathlib import Path
import json,hashlib,itertools
import sympy as s
P=Path(__file__).parent;checks={}
L,T=s.symbols('L T')
assert s.expand((2*L+8*T)-2*(L+T))==6*T
assert s.Rational(11,3)+2*s.Rational(37,24)==s.Rational(27,4)<7
assert s.expand(2*(L+T)-(2*L+8*T)/4)==s.Rational(3,2)*L
assert 2*s.Rational(37,24)+s.Rational(11,12)==4
checks['normalized_jet_constants']=True
assert s.Rational(1,16)-s.Rational(1,8)+s.Rational(1,384)<0
checks['negative_Hessian_contradiction']=True
x,y,r,t=s.symbols('x y r t',real=True)
f=(x-y*y)**2+y**4
assert s.diff(f,x).subs(x,y*y)==0 and s.diff(f,x,2)==2
assert s.expand(f-y**4-(x-y*y)**2)==0
assert s.integrate((1-t)*s.diff(f,x,2),(t,0,1))==1
assert s.expand(f.subs(x,r+y*y)-r*r-y**4)==0
checks['curved_graph_residual_and_exact_integral']=True
for k in range(1,6):
 v=s.symbols('v:'+str(k));pol=0
 for signs in itertools.product([-1,1],repeat=k):
  pol+=s.prod(signs)*sum(a*b for a,b in zip(signs,v))**k
 assert s.expand(pol/(2**k*s.factorial(k))-s.prod(v))==0
checks['polarization_degrees_one_through_five']=True
h=s.symbols('h',positive=True);J=s.Matrix([[0,-1],[1,0]])
G=h*s.eye(2)
assert J.T*G.inv()*J==s.eye(2)/h
assert G.det()==h*h
checks['adaptive_symplectic_dual']=True
a,b,u,v,e=s.symbols('a b u v e',real=True);z=a+s.I*b
A=s.Matrix([[1,z],[s.conjugate(z),a*a+b*b+e]])
w=s.Matrix([u,v])
assert s.expand((w.conjugate().T*A*w)[0]-s.expand_complex((u+z*v)*s.conjugate(u+z*v))-e*v*v)==0
assert s.simplify(A.det())==e
checks['nondiagonal_matrix_positivity']=True
theta=s.Matrix([s.Rational(1,2),s.Rational(1,3),s.Rational(1,4)])
den=(theta.T*theta)[0]
assert sum(v*v/den for v in theta)==1
checks['squared_partition_normalization']=True
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'scope':'Exact finite algebra diagnostics only; full general proofs and exact dependencies are in the companions and proof map.',
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in P.glob('*.md')},
 'figure_source_sha256':sha(P/'figures/scalar_splitting.py'),
 'Fefferman_Phong_operator_theorem_included':False,'U033_restored':False}
(P/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf8')
print(json.dumps(result))

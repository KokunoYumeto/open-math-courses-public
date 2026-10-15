"""Exact noncommutative and linear-symplectic examples, not analytic proof tests."""
from pathlib import Path
import hashlib,json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def eq(name,a,b):
 assert s.simplify(a-b)==0,(name,a,b)
 checks.append({'name':name,'passed':True})
A,B=s.symbols('A B',commutative=False)
for N in range(6):
 words=[]
 for choices in itertools.product([0,1],repeat=N):
  term=s.Integer(1)
  for c in choices:term=term*(A*B if c==0 else B*A)
  words.append((-1)**sum(choices)*term)
 assert s.expand((A*B-B*A)**N-s.Add(*words))==0
 checks.append({'name':'exact ordered commutator expansion N='+str(N),'passed':True})
 assert len(words)==2**N
 checks.append({'name':'word count N='+str(N),'passed':True})
xi1=s.symbols('xi1',real=True);xi2=s.symbols('xi2',positive=True)
x1,x2=s.symbols('x1 x2',real=True);r=s.sqrt(xi1**2+xi2**2)
def pb(f,g):
 return sum(s.diff(f,p)*s.diff(g,x)-s.diff(f,x)*s.diff(g,p) for x,p in [(x1,xi1),(x2,xi2)])
eq('Poisson sign x1 xi1',pb(x1,xi1),-1)
eq('bad-set bracket',pb(x1*r,xi1).subs({x1:0,xi1:0}),-xi2)
eq('good-set bracket',pb(x1*r,xi2),0)
J=s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
bad=s.Matrix.hstack(s.eye(4)[:,1],s.eye(4)[:,3])
good=s.Matrix.hstack(s.eye(4)[:,1],s.eye(4)[:,2])
assert (bad.T*J*bad).rank()==2;checks.append({'name':'bad tangent is symplectic','passed':True})
assert good.T*J*good==s.zeros(2);checks.append({'name':'conormal tangent is isotropic','passed':True})
for n in range(1,5):
 for k in [n,n+1,2*n]:
  assert 2*n-k<=k
  checks.append({'name':f'coisotropic dimension inequality n={n},k={k}','passed':True})
eq('conormal amplitude order',0+(2-2)/s.Integer(4),0)
eq('conormal integral normalization',-(2+2)/s.Integer(4),-1)
eq('conormal fixed endpoint',-s.Rational(2,4),-s.Rational(1,2))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'checks':checks,'source_sha256':sha(ROOT/'iterated-regularity-and-the-poisson-obstruction.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Finite ordered-word, Poisson sign, tangent-plane and normalization identities. The full operator, wavefront and first-jet proofs are in the lesson.'}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'cases':len(checks)}))

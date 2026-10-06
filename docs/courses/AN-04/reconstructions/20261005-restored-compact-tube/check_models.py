"""Exact finite identities; distinct from the full geometric/operator proof."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def passed(name):checks.append({'name':name,'passed':True})
t,z,tau,eta=s.symbols('t z tau eta',real=True)
v=s.Matrix([t,z,tau,eta])
f=s.Matrix([s.tan(t),z,tau*s.cos(t)**2,eta]);df=f.jacobian(v)
J=s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
assert (df.T*J*df-J).applyfunc(s.trigsimp)==s.zeros(4)
passed('Full four-dimensional symplectic Jacobian including mixed time components')
primitive=s.Matrix([[f[2],f[3]]])*df[:2,:]
assert (primitive-s.Matrix([[tau,eta,0,0]])).applyfunc(s.trigsimp)==s.zeros(1,4)
passed('Exact primitive equality without a discarded exact one-form')
H=s.Matrix([1+f[0]**2,0,-2*f[0]*f[2],0])
assert (s.diff(f,t)-H).applyfunc(s.trigsimp)==s.zeros(4,1)
assert s.trigsimp((1+f[0]**2)*f[2]-tau)==0
passed('Actual Hamilton transport and p composed with chart equals tau')
A,B,P,D,L,R=s.symbols('A B P D L R',commutative=False)
assert s.expand(A*(D-B*P*A)*B+(A*B-1)*P*A*B+P*(A*B-1)-(A*D*B-P))==0
assert s.expand((1-A*B)*P*A+A*(B*P*A-D)-(P*A-A*D))==0
assert s.expand(L*(1-A*R)+(L*A-1)*R-(L-R))==0
passed('All three ordered inverse and intertwining defect identities')
x,xi=s.symbols('x xi',real=True)
rad=s.Matrix([0,s.exp(-t)])
assert s.diff(rad,t)==s.Matrix([rad[0],-rad[1]])
passed('Radial example has H_p=-R on its exact exponential curve')
c=s.symbols('c',real=True)
assert s.expand((tau*c)**2+eta**2-c**2*(tau**2+eta**2)-eta**2*(1-c**2))==0
assert s.expand((tau**2+eta**2)-((tau*c)**2+eta**2)-tau**2*(1-c**2))==0
passed('Both full covector norm bounds for 0<c<=1')
result={'passed':True,'finite_groups':len(checks),'checks':checks,
 'script_sha256':sha(Path(__file__)),'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'analytic_proof_certification_by_these_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

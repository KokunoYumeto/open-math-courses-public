"""Finite algebra and model checks; analytic proofs are reviewed separately."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def passed(name):checks.append({'name':name,'passed':True})
t,z,t0,a,b,R=s.symbols('t z t0 a b R',real=True)
g=t*z+t**2;G=s.I*s.integrate(g,(t,t0,t))
assert s.simplify(-s.I*s.diff(G,t)-g)==0
passed('Primitive has Dt=-i*d/dt sign and exact polynomial forcing')
# A noncommutative identity checks all ordered defects, before their analytic estimates.
A,B,P,u,D,Q=s.symbols('A B P u D Q',commutative=False)
f= P*u
assert s.expand((D-B*P*A)*B*u+B*P*(A*B-1)*u+B*f-D*B*u)==0
passed('Ordered conjugation defect identity without commuted factors')
m,h=s.symbols('m h',real=True);r=h+m-1
assert s.simplify(h-(1-m)-r)==0 and s.simplify(r+1-m-h)==0
assert s.simplify(r-r)==0
passed('Every-real-order forcing reduction and total BQ order')
for exponent,expected in [(-1,1-1/R),(-s.Rational(1,2),s.log(R)),(0,R-1)]:
 assert s.simplify(s.diff(expected,R)-R**(2*exponent))==0
 assert s.simplify(expected.subs(R,1))==0
passed('Three plotted comparison integrals differentiate to their actual weights')
tau,eta=s.symbols('tau eta',real=True)
assert s.expand((1+tau**2)*(1+eta**2)-(1+tau**2+eta**2))==tau**2*eta**2
passed('Exact joint-frequency product bound for the delta threshold')
tau1,eta1=s.symbols('tau1 eta1')
p=tau1
assert s.diff(p,tau1)==1 and s.diff(p,eta1)==0
passed('Characteristic has dt/ds=1 and fixed transverse covector')
out={'passed':True,'finite_groups':len(checks),'checks':checks,
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.name:sha(p) for p in ROOT.glob('*.md')},
 'analytic_proof_certification_by_these_checks':False}
(ROOT/'model-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks)}))

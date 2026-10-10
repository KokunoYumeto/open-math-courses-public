"""Exact checks of the series examples and flat-wave geometric bounds."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent;rows=[]
def check(name,a,b=0):
 assert s.simplify(a-b)==0,(name,a,b)
 rows.append({'name':name,'passed':True,'kind':'exact algebra'})
j=s.symbols('j',integer=True,positive=True)
for n in range(1,7):
 check(f'CO22 geometric tail n={n}',s.summation(s.Rational(1,4)**j,(j,n,s.oo)),s.Rational(4)**(1-n)/3)
for n,want in [(1,s.Rational(1,3)),(2,s.Rational(13,12)),(3,s.Rational(3121,48))]:
 check(f'CO22 complete column n={n}',sum(k**(2*n) for k in range(1,n))+s.Rational(4)**(1-n)/3,want)
for J in [1,4,8,16]:
 check(f'CO23 full partial sum J={J}',sum((s.Integer(k)*s.Rational(1,k))**2 for k in range(1,J+1)),J)
 for m in [4,8]:
  check(f'CO23 truncated partial sum J={J},m={m}',sum((s.Integer(k)*s.Rational(1,k) if k<=m else 0)**2 for k in range(1,J+1)),min(J,m))
check('CO23 telescoping majorant',1/(j*(j+1)),1/j-1/(j+1))
check('CO23 majorant difference for index j+1',1/(j*(j+1))-1/(j+1)**2,1/(j*(j+1)**2))
xi,eta,tau=s.symbols('xi eta tau',real=True)
p=xi**2+eta**2-tau**2
check('CO24 reflection preserves p',p.subs(xi,-xi),p)
check('CO24 characteristic normalization',p/tau**2,(xi/tau)**2+(eta/tau)**2-1)
for sign in [-1,1]:
 check(f'CO24 normalized physical time sign={sign}',s.diff(p,tau).subs(tau,sign),-2*sign)
 for t0 in [-s.Rational(1,4),s.Integer(0),s.Rational(1,4)]:
  duration=(s.Rational(5,8)+sign*t0)/2
  check(f'CO25 exact observed time sign={sign},t0={t0}',t0-2*sign*duration,-sign*s.Rational(5,8))
  assert s.Rational(3,16)<=duration<=s.Rational(7,16)
check('CO25 maximum spatial displacement',2*s.Rational(7,16),s.Rational(7,8))
source=ROOT/'compact-generalized-rays-and-uniform-observation.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'scope':'Exact series columns, dense-test partial sums, telescoping bound, normalized flat-wave signs and compact access bounds. These checks do not replace the analytic proof.',
 'checks':rows}
(ROOT/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(rows)}))

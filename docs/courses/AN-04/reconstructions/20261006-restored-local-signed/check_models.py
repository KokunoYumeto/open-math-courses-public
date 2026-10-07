"""Finite algebra and exact coordinate checks; the complete proofs are in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
d=s.symbols('d',real=True);chi=s.Function('chi')(d)
# On each open time half-line; the zero-time jump has chi(0)=1.
for sign in [1,-1]:
 f=sign*s.I*chi
 g=sign*s.I*(chi-1)
 residual=sign*s.diff(chi,d)
 assert s.simplify(-s.I*s.diff(f,d)-residual)==0
 assert s.simplify(-s.I*s.diff(g,d)-residual)==0
 assert s.simplify(f-g-sign*s.I)==0
 # Jump is right minus left; backward coefficient occurs on the left.
 jump=sign*s.I if sign==1 else -sign*s.I
 assert -s.I*jump==1
n,mu,a=s.symbols('n mu a',real=True)
assert s.simplify((n-1)/2-2*n/4)==-s.Rational(1,2)
assert s.simplify(-(n-1)+(2*n+2*(n-1))/4)==s.Rational(1,2)
assert s.simplify(mu-s.Rational(1,2)-mu)==-s.Rational(1,2)
assert s.simplify((a+mu)-mu)==a
svg=ET.fromstring((ROOT/'figures/local-signed-cutoff-errors.svg').read_bytes())
polygons=svg.findall('.//{http://www.w3.org/2000/svg}polygon')
expected=[{s.Rational(0),s.Rational(1)},{s.Rational(-1),s.Rational(0)},
          {s.Rational(1),s.Rational(2)},{s.Rational(-2),s.Rational(-1)}]
for p,values in zip(polygons,expected):
 points=[[s.Rational(x) for x in item.split(',')] for item in p.attrib['points'].split()]
 times={(300-y)/80-(x-420)/80 for x,y in points}
 assert times==values,(times,values)
assert len(polygons)==4
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'finite_groups':3,'scope':['Signed derivatives and jump coefficients for both cutoff kernels and their exact flat corrections',
 'Exact conormal normalization and arbitrary real graph-order/Sobolev cancellation',
 'All polygon vertices under the actual affine diagram map and both signed residual bands'],
 'does_not_replace_general_proofs':True,'script_sha256':sha(Path(__file__)),
 'source_hashes':{p:sha(ROOT/p) for p in ['local-signed-parametrices-and-delayed-errors.md','figures/local-signed-cutoff-errors.svg']}}
(ROOT/'model-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps(out,ensure_ascii=False))

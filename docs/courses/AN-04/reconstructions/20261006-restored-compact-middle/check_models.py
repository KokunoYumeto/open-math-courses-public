"""Exact finite algebra, Gaussian normalization and figure coordinates; full proofs are in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
# Transpose of the actual linear embedding (x,y,z)->(x,y,y,z).
J=s.Matrix([[1,0,0],[0,1,0],[0,1,0],[0,0,1]])
xi,e1,e2,zeta,theta=s.symbols('xi e1 e2 zeta theta')
assert J.T*s.Matrix([xi,e1,e2,zeta])==s.Matrix([xi,e1+e2,zeta])
assert J.T*s.Matrix([0,theta,-theta,0])==s.zeros(3,1)
# Exact compact-middle commutator formula for a forward pair t>s and t<s.
fs,ft=s.symbols('phi_s phi_t',real=True)
for H in [0,1]:
 triple=-s.I*H*(ft-fs)+fs
 outside=(s.I*H+1)*fs-ft*s.I*H
 assert s.simplify(triple-outside)==0
 assert s.simplify(triple.subs({fs:1,ft:1}))==1
eps=s.symbols('epsilon',positive=True);y=s.symbols('y',real=True)
g=(4*s.pi*eps)**(-s.Rational(1,2))*s.exp(-y*y/(4*eps))
mass=s.integrate(g*g,(y,-s.oo,s.oo))
assert s.simplify(mass-(8*s.pi*eps)**(-s.Rational(1,2)))==0
svg=ET.fromstring((ROOT/'figures/compact-middle-return-cutoff.svg').read_bytes())
ns={'s':'http://www.w3.org/2000/svg'}
rects=[r for r in svg.findall('.//s:rect',ns) if r.get('y') in ['175','225','278']]
intervals=[((s.Rational(r.get('x'))-500)/130,(s.Rational(r.get('x'))+s.Rational(r.get('width'))-500)/130) for r in rects]
assert intervals==[(-3,-2),(2,3),(-2,2),(-1,1)]
circles=svg.findall('.//s:circle',ns)
assert [(s.Rational(c.get('cx'))-500)/130 for c in circles]==[-s.Rational(1,2),s.Rational(1,4),s.Rational(3,4)]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'finite_groups':3,'scope':['Actual normal transpose and exact compact-middle commutator on both time regions',
 'Exact Gaussian square integral and divergent coefficient','All return-cutoff diagram interval endpoints and marked times'],
 'does_not_replace_general_proofs':True,'script_sha256':sha(Path(__file__)),
 'source_hashes':{p:sha(ROOT/p) for p in ['comparing-global-parametrices-through-a-compact-middle.md','figures/compact-middle-return-cutoff.svg']}}
(ROOT/'model-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps(out,ensure_ascii=False))

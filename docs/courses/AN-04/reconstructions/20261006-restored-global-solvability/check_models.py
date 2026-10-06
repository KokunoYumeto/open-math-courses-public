"""Finite checks for the exact slit drawing and the complex duality convention."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
import sympy as s
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
R=s.Rational
fig=ROOT/'figures/global-solvability-slit-domain.svg'
svg=ET.parse(fig).getroot();ns={'s':'http://www.w3.org/2000/svg'}
assert (svg.attrib['width'],svg.attrib['height'])==('430','500')
paths=[p.attrib['d'] for p in svg.findall('.//s:path',ns)]
assert 'M85 150V410M345 150V410' in paths
assert 'M215 150L215 73' in paths
circles={(R(c.attrib['cx']),R(c.attrib['cy'])) for c in svg.findall('.//s:circle',ns)}
for j in [1,2,4]:
 y=-R(1,j);px=215;py=150-260*y
 assert (px,py) in circles
 assert f'M85 {py}H315' in paths and f'M315 {py}H345' in paths
 assert s.simplify((85-215)/s.Integer(130))==-1
 assert s.simplify((345-215)/s.Integer(130))==1
 assert y<0 and -y==R(1,j)
x,y,xi,eta=s.symbols('x y xi eta',real=True);p=xi
Hp=s.Matrix([s.diff(p,xi),s.diff(p,eta),-s.diff(p,x),-s.diff(p,y)])
assert Hp==s.Matrix([1,0,0,0]) and p.subs({xi:0,eta:1})==0
I=s.I
P=s.Matrix([[1+2*I,3-I],[-2+I,4]])
u=s.Matrix([2-I,1+3*I]);v=s.Matrix([1+I,-3+2*I])
psi=[s.Matrix([1,2+I]),s.Matrix([I,1-I])];a=[2+3*I,-1+2*I]
pair=lambda b,c:s.expand((c.conjugate().T*b)[0])
f=P*u+sum((ar*pr for ar,pr in zip(a,psi)),s.zeros(2,1))
z=[pair(v,pr) for pr in psi]
ell=sum(ar*s.conjugate(zr) for ar,zr in zip(a,z))
assert s.simplify(pair(f,v)-pair(u,P.conjugate().T*v)-ell)==0
assert s.simplify(ell-sum(ar*zr for ar,zr in zip(a,z)))!=0
lam=2-I
assert all(s.simplify(pair(lam*v,pr)-lam*zr)==0 for pr,zr in zip(psi,z))
assert s.simplify(pair(f,lam*v)-s.conjugate(lam)*pair(f,v))==0
result={'passed':True,'finite_groups':2,
 'groups':['Exact SVG affine coordinates, endpoints, positive covectors and Hamilton flow on the slit domain',
           'Nonreal matrix adjoint and residual pairing, image-map linearity and mandatory functional conjugation'],
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in [ROOT/'global-solvability-modulo-smooth.md',fig]},
 'proof_of_infinite_dimensional_theorem':False}
(ROOT/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':2}))

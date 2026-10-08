"""Exact affine coefficient curves from NE7-NE8, not solution-energy samples."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
X=lambda h:100+480*float(h*8)
Y=lambda v:290-256*float(v)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="780" height="390" viewBox="0 0 780 390" role="img" aria-labelledby="title desc">',
'<title id="title">Cone and collar costs in the normal-energy estimate</title>',
'<desc id="desc">Exact lines theta equals one eighth plus twice h and two theta equals one quarter plus four h, for h from zero to one eighth. The source term remains separate.</desc>',
'<rect width="780" height="390" fill="white"/>',
'<g font-family="Arial,sans-serif" font-size="16" fill="#18334a">',
'<text x="30" y="30" font-size="21" font-weight="bold">Both localization widths enter the coefficient</text>',
'<text x="30" y="56">a₀ = b₀ = C = 1,  ω = 1/8,  γ = θ</text>']
for val,label in [(F(0),'0'),(F(1,8),'1/8'),(F(1,4),'1/4'),(F(1,2),'1/2'),(F(3,4),'3/4')]:
 y=Y(val);parts.append(f'<path d="M100 {y} H580" stroke="#dce4ea"/><text x="88" y="{y+5}" text-anchor="end">{label}</text>')
parts.append('<path d="M100 85 V290 H590" fill="none" stroke="#18334a" stroke-width="2"/>')
for h,label in [(F(0),'0'),(F(1,16),'1/16'),(F(1,8),'1/8')]:
 x=X(h);parts.append(f'<path d="M{x} 290 v6" stroke="#18334a"/><text x="{x}" y="318" text-anchor="middle">{label}</text>')
for factor,color in [(1,'#167497'),(2,'#b8560a')]:
 v0=factor*F(1,8);v1=factor*F(3,8)
 parts.append(f'<path d="M100 {Y(v0)} L580 {Y(v1)}" stroke="{color}" stroke-width="4" fill="none"/>')
 parts.append(f'<circle cx="100" cy="{Y(v0)}" r="5" fill="white" stroke="{color}" stroke-width="2"/>')
parts+=['<text x="597" y="102" fill="#b8560a">2θ = 1/4 + 4h</text>',
'<text x="597" y="198" fill="#167497">θ = 1/8 + 2h</text>',
'<text x="390" y="345">normal collar width h</text>',
'<text x="30" y="378">Exact coefficients only. Source norm remains; h = 0 is a limit.</text></g></svg>']
asset=ROOT/'figures/normal-energy-budget.svg';asset.write_text('\n'.join(parts)+'\n',encoding='utf-8')
checks=[]
for i in range(17):
 h=F(i,128);theta=F(1,8)+2*h;coefficient=2*theta
 assert coefficient==F(1,4)+4*h
 checks.append({'h':str(h),'theta':str(theta),'coefficient':str(coefficient)})
record={'asset':'figures/normal-energy-budget.svg','sha256':sha(asset),'source_sha256':sha(ROOT/'glancing-normal-energy-model.md'),'script_sha256':sha(Path(__file__)),'exact_coordinate_checks':checks,'curves':'Exact straight lines; no numerical approximation.','solution_energies_depicted':False,'source_term_retained':True,'actually_inspected':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print({'exact_coordinate_checks':len(checks),'figure':asset.name})

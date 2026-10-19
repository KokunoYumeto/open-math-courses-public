"""Exact affine envelope and rescaled logarithmic support/plateau windows."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="900" viewBox="0 0 1100 900"><rect width="1100" height="900" fill="#f5f7fa"/>']
def text(x,y,txt,size=18,color='#21374d',anchor='start'):
 p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{txt}</text>')
def line(x1,y1,x2,y2,color='#cbd4df',width=1):p.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"/>')
text(40,42,'A positive sum realizes the concave envelope',25)
text(40,75,'Exact example: h(t) = min(0, −t), with Q(ζ) = ζ² and n = 3.',18)
X=lambda t:570+215*t
Y=lambda h:285-67.5*h
for q in [-2,-1,0,1,2]:
 line(X(q),150,X(q),420);text(X(q),446,str(q),16,anchor='middle')
 line(140,Y(q),1000,Y(q));text(124,Y(q)+5,str(q),16,anchor='end')
line(140,Y(0),1000,Y(0),'#21374d',1.5);line(X(0),140,X(0),426,'#21374d',1.5)
line(X(-2),Y(0),X(2),Y(0),'#8b718e',2)
line(X(-2),Y(2),X(2),Y(-2),'#c26b29',2)
p.append(f'<path d="M{X(-2)},{Y(0)} L{X(0)},{Y(0)} L{X(2)},{Y(-2)}" fill="none" stroke="#087684" stroke-width="5"/>')
text(1020,292,'t',18);text(584,137,'index',17)
text(195,225,'ℓ₁(t) = −t',18,'#a7551b');text(770,266,'ℓ₀(t) = 0',18,'#7a557e')
text(695,372,'h(t)',20,'#087684');text(140,480,'Below both lines: finite norms. Above either line: positivity prevents cancellation.',18)
text(40,527,'Actual frequency windows in the rescaled coordinate z = ζ / √(λ log λ)',22)
text(40,558,'Light bar: |η| ≤ 1. Dark bar: |η| ≤ 1/2. Centers θ = 0 and θ = 1.',18)
Z=lambda z:300+500*z
for ll,y in [(4,620),(8,700),(16,780)]:
 text(40,y+6,f'log λ = {ll}',18)
 line(150,y,970,y)
 for center in [0,1]:
  p.append(f'<rect x="{Z(center-1/ll)}" y="{y-12}" width="{1000/ll}" height="24" fill="#abd5d8"/>')
  p.append(f'<rect x="{Z(center-1/(2*ll))}" y="{y-6}" width="{500/ll}" height="12" fill="#087684"/>')
  line(Z(center),y-21,Z(center),y+21,'#21374d',1.5)
text(Z(0),827,'0',18,anchor='middle');text(Z(1),827,'1',18,anchor='middle');text(985,808,'z',18)
text(40,869,'In the original conic coordinate ζ/λ, both windows tend to zero; only the positive λ ray remains.',17)
p.append('</svg>');svg=root/'figures/prescribed-concave-packets.svg';svg.write_text('\n'.join(p),'utf-8')
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps(dict(svg='figures/prescribed-concave-packets.svg',svg_sha256=sha(svg),generator_sha256=sha(Path(__file__)),coordinate_formulas=['h(t)=min(0,-t)','rescaled center=theta','support half width=1/log(lambda)','plateau half width=1/(2log(lambda))'],scope='The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                       ),indent=2)+'\n','utf-8')
print(svg)

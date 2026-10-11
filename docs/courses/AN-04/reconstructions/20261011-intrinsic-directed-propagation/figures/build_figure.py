"""Exact zero regions and increasing-time orientation for the two flat models."""
from pathlib import Path
import math,json,hashlib
root=Path(__file__).resolve().parents[1]
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="810" viewBox="0 0 1100 810"><rect width="1100" height="810" fill="#f5f7fa"/><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#263d55"/></marker></defs>']
def text(x,y,s,size=18,color='#22364c',anchor='start'):
 p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>')
def line(x1,y1,x2,y2,color='#9caabb',width=1,arrow=False):
 p.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
text(40,42,'The accessible endpoint fixes the propagation direction',25)
text(40,74,'p = τ − i a(t)η on η &gt; 0; both models point toward increasing t.',18)
for y,title,left,right in [(125,'Exiting geometry: a(t) = A′(t)','Characteristic: t ≤ 0','Noncharacteristic: t &gt; 0'),(320,'Entering geometry: a(t) = A′(−t)','Noncharacteristic: t &lt; 0','Characteristic: t ≥ 0')]:
 text(50,y,title,21)
 lc,rc=('#d5dfef','#d0e9e3') if y==125 else ('#d0e9e3','#d5dfef')
 p.append(f'<rect x="120" y="{y+24}" width="430" height="64" fill="{lc}"/><rect x="550" y="{y+24}" width="430" height="64" fill="{rc}"/>')
 text(330,y+63,left,19,anchor='middle');text(767,y+63,right,19,anchor='middle')
 line(120,y+106,980,y+106,'#263d55',2,True);line(550,y+20,550,y+116,'#263d55',2)
 text(550,y+140,'t = 0',16,anchor='middle');text(985,y+128,'t',18)
 text(110,y+160,'Imaginary value is zero on the blue region and strictly negative on the green region.',17)
text(50,523,'The actual flat coefficients',22)
X=lambda t:550+210*t
Y=lambda a:733-100*a
for t in [-2,-1,0,1,2]:line(X(t),553,X(t),733,'#d5dce4');text(X(t),756,str(t),15,anchor='middle')
for a in [0,.5,1,1.5]:line(130,Y(a),970,Y(a),'#d5dce4');text(117,Y(a)+5,str(a),15,anchor='end')
def coeff(t):return 2*t**-3*math.exp(-1/t**2) if t>0 else 0
for sign,color in [(1,'#096b77'),(-1,'#ad5720')]:
 pts=[(X(t),Y(coeff(sign*t))) for t in [i/200 for i in range(-400,401)]]
 p.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="3"/>')
text(215,569,'A′(−t)',18,'#ad5720');text(798,569,'A′(t)',18,'#096b77');text(990,739,'t',18)
text(50,796,'A(t) = exp(−1/t²) for t &gt; 0, and 0 for t ≤ 0. Zero sets and arrows are exact.',17)
p.append('</svg>');svg=root/'figures/intrinsic-directed-propagation.svg';svg.write_text('\n'.join(p),'utf-8')
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps({'svg':'figures/intrinsic-directed-propagation.svg','svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),'coordinate_formulas':['outgoing coefficient = 2t^(-3)exp(-1/t^2) for t>0, zero otherwise','incoming coefficient = outgoing(-t)','both orientation arrows point toward increasing t'],'actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')
print(svg)

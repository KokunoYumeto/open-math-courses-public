"""Draw exact exponent lines and support-bound curves without external assets."""
from pathlib import Path
import math,hashlib,json
root=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="630" viewBox="0 0 1100 630"><rect width="1100" height="630" fill="#f5f7fa"/>']
def text(x,y,s,size=17,color='#22364c',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>')
def line(x1,y1,x2,y2,c='#9caabb',width=1):parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{c}" stroke-width="{width}" fill="none"/>')
def path(points,c,width=3):parts.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="{width}"/>')
text(40,40,'Shrinking cutoffs: the endpoint and the sign region',25)
text(40,73,'Exact formulas; curves sampled only for drawing.',17)
text(55,119,'Orders in the energy estimate',21)
X=lambda v:85+420*v/.25
Y=lambda v:175+270*(-v)
for v in [-1,-.5,-.125,0]:
 line(85,Y(v),505,Y(v),'#d5dce4');text(76,Y(v)+5,str(v),14,anchor='end')
for v in [0,.125,.25]:
 line(X(v),175,X(v),445,'#e0e5eb');text(X(v),469,str(v),14,anchor='middle')
line(85,175,85,445);line(85,445,505,445)
path([(X(v/800),Y(-1+4*v/800)) for v in range(201)],'#096b77')
path([(X(v/800),Y((3*v/800-1)/2)) for v in range(201)],'#ad5720')
text(105,158,'0 = bounded positivity error',16,'#096b77')
text(320,410,'−1 + 4e',19,'#096b77')
text(105,230,'weak shift (3e − 1)/2',18,'#ad5720')
text(490,500,'e',18)
text(75,532,'At e = 1/4: positivity order 0;',17)
text(75,557,'the weak input order is s − 1/8.',17)
text(590,119,'Positive-side support strips at e = 1/4',21)
XX=lambda q:635+400*q/4
YY=lambda y:450-220*y/4
parts.append('<rect x="635" y="450" width="400" height="38" fill="#f4dad8"/>')
for q in [0,1,2,3,4]:
 line(XX(q),210,XX(q),488,'#e0e5eb');text(XX(q),508,str(q),14,anchor='middle')
for y in [0,1,2,3,4]:
 line(635,YY(y),1035,YY(y),'#d5dce4');text(624,YY(y)+5,str(y),14,anchor='end')
qs=[i/50 for i in range(201)]
def poly(a,b,fill):
 ps=[(XX(q),YY(a*10**(-q/4))) for q in qs]+[(XX(q),YY(b*10**(-q/4))) for q in reversed(qs)]
 parts.append('<polygon points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in ps)+f'" fill="{fill}"/>')
poly(1,4,'#d4e9e6');poly(2,3,'#75b5ab')
for a in [1,4]:path([(XX(q),YY(a*10**(-q/4))) for q in qs],'#357e7a',2)
for a in [2,3]:path([(XX(q),YY(a*10**(-q/4))) for q in qs],'#205d55',2)
line(635,450,1035,450,'#263c53',2)
text(610,188,'y',19);text(830,540,'log₁₀ η',18,anchor='middle')
text(760,477,'y &lt; 0: f &gt; 0',16,'#8f3632')
text(655,578,'Inner: 2η⁻¹⁄⁴ &lt; y &lt; 3η⁻¹⁄⁴',17,'#205d55')
text(655,604,'Outer: η⁻¹⁄⁴ &lt; y &lt; 4η⁻¹⁄⁴',17,'#357e7a')
parts.append('</svg>');svg=root/'figures/shrinking-cutoff-energy.svg';svg.write_text('\n'.join(parts),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps({'svg':'figures/shrinking-cutoff-energy.svg','svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),'coordinate_formulas':['positivity order = -1+4e','weak shift = (3e-1)/2','outer bounds = eta^(-1/4),4eta^(-1/4)','inner bounds = 2eta^(-1/4),3eta^(-1/4)'],'horizontal_frequency_axis':'log10 eta, from 0 to 4','actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')
print(svg)

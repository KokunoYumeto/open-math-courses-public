"""Two explicit derivative-bound shapes and the exact sharp phase coefficient."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="740" viewBox="0 0 1100 740"><rect width="1100" height="740" fill="#f5f7fa"/>']
def text(x,y,t,size=18,color='#22384c',anchor='start'):p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{t}</text>')
def line(x1,y1,x2,y2,color='#cbd4df',width=1):p.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"/>')
def curve(points,color,width=3):p.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
text(40,42,'Local sign geometry controls the complex phase',26)
text(40,76,'The pointwise remainder has the exact weak order 2β = 2s − 1 + 3e.',19)
text(100,137,'Two derivative regimes',22);text(660,137,'Exact sharp coefficient',22)
text(100,171,'1 + 4z',17,'#b66426');text(235,171,'4/z',17,'#8b668a');text(330,171,'minimum',17,'#087684')
text(660,171,'k − 2k²',18,'#b66426')
X=lambda z:100+(z-.25)*400/3.75;Y=lambda v:610-v*400/18
for z in [.25,1,2,3,4]:line(X(z),210,X(z),610);text(X(z),636,str(z),15,anchor='middle')
for v in [0,4,8,12,16]:line(100,Y(v),500,Y(v));text(88,Y(v)+5,str(v),15,anchor='end')
zs=[.25+3.75*j/600 for j in range(601)]
curve([(X(z),Y(1+4*z)) for z in zs],'#b66426',2)
curve([(X(z),Y(4/z)) for z in zs],'#8b668a',2)
curve([(X(z),Y(min(1+4*z,4/z))) for z in zs],'#087684',4)
line(100,Y(8),500,Y(8),'#68778a',1.5);text(310,Y(8)-10,'2wᵉ = 8',16,'#526579')
text(300,668,'z = g / w¹⁻ᵉ, with wᵉ = 4',17,anchor='middle')
U=lambda k:660+760*k;V=lambda a:610-a*400/.15
for k in [0,.125,.25,.375,.5]:line(U(k),210,U(k),610);text(U(k),636,str(k),15,anchor='middle')
for v in [0,.0625,.125]:line(660,V(v),1040,V(v));text(649,V(v)+5,str(v),15,anchor='end')
curve([(U(j/1200),V(j/1200-2*(j/1200)**2)) for j in range(601)],'#b66426',4)
p.append(f'<circle cx="{U(.25)}" cy="{V(.125)}" r="6" fill="#087684"/>')
text(850,245,'(1/4, 1/8)',18,'#087684',anchor='middle');text(850,668,'k',18,anchor='middle')
text(40,714,'Left: bound shapes with fixed constants suppressed. Right: the exact coefficient of R²ᵝ in the example.',17)
p.append('</svg>');svg=root/'figures/local-sign-phase.svg';svg.write_text('\n'.join(p),'utf-8');sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
(root/'figure-check.json').write_text(json.dumps(dict(svg='figures/local-sign-phase.svg',svg_sha256=sha(svg),generator_sha256=sha(Path(__file__)),coordinate_formulas=['left shapes 1+4z and 4/z, z in [1/4,4]','right exact k-2k^2, k in [0,1/2]','maximum 1/8 at k=1/4'],actually_inspected=False,exact_coordinate_review_complete=False),indent=2)+'\n','utf-8');print(svg)

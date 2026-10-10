"""Exact-coordinate SVG for USD:X1-X2; only the curves are sampled."""
from pathlib import Path
from math import sqrt
from html import escape
out=Path(__file__).resolve().parent/'strict-diffraction.svg'
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="560" viewBox="0 0 1040 560" role="img" aria-labelledby="title desc">',
 '<title id="title">Strict diffraction with a stationary projected boundary field</title>',
 '<desc id="desc">Left: the exact tangent base projection x=t squared, z=-2t cubed/3. Right: continuous cap-travel time across interior turning, tangency and reflection.</desc>',
 '<rect width="1040" height="560" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b;font-size:16px}.head{font-size:20px;font-weight:bold}.small{font-size:14px}.axis{stroke:#435668;stroke-width:1.5}.grid{stroke:#dce4e9;stroke-width:1}</style>']
def text(x,y,s,cls='',anchor='start'):
 svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#435668',width=1.5,dash=''):
 svg.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def curve(points,color):
 svg.append('<polyline fill="none" stroke="'+color+'" stroke-width="3.2" points="'+' '.join(f'{x:.4f},{y:.4f}' for x,y in points)+'"/>')
def dot(x,y,color):svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')
text(35,33,'A strict tangent ray, although H(r₀) = 0','head')
text(555,33,'The cap-hitting map is continuous','head')
text(35,63,'p = ξ² − xη²,  η = 1,  z₀ = 0')
text(555,63,'rβ = (x + β)η²,  h = 1/16')
left=lambda z,x:(265+z*18000,410-x*4400)
for x,label in [(0,'0'),(1/32,'1/32'),(1/16,'1/16')]:
 a,b=left(-.0115,x);c,d=left(.0115,x);line(a,b,c,d,'#dce4e9');text(45,b+5,label,'small','end')
line(*left(-.012,0),*left(.012,0));line(*left(0,0),*left(0,.068))
text(494,414,'z');text(273,102,'x')
for z,label in [(-1/96,'−1/96'),(0,'0'),(1/96,'1/96')]:
 a,b=left(z,0);line(a,b,a,b+5);text(a,435,label,'small','middle')
for lo,hi,color in [(-.25,0,'#087e8b'),(0,.25,'#b64736')]:
 ts=[lo+(hi-lo)*i/150 for i in range(151)]
 curve([left(-2*t**3/3,t*t) for t in ts],color)
 for t in [lo,hi]:dot(*left(-2*t**3/3,t*t),color)
text(76,112,'outgoing  t = 1/4','small');text(318,112,'incoming  t = −1/4','small')
text(318,195,'t increases ↙','small');text(89,255,'↖ t increases','small')
text(277,387,'t = 0','small');text(265,468,'x = t²,  z = −2t³/3','', 'middle')
right=lambda b,t:(775+b*11200,410-(t-.28)*750)
for t,label in [(.3,'0.3'),(.4,'0.4'),(.5,'0.5')]:
 a,c=right(-1/64,t);b,d=right(1/64,t);line(a,c,b,d,'#dce4e9');text(585,c+5,label,'small','end')
line(*right(-1/64,.28),*right(1/64,.28));line(*right(-1/64,.28),*right(-1/64,.565))
line(*right(0,.28),*right(0,.54),'#9aa8b1',1,'4 4')
for b,label in [(-1/64,'−1/64'),(0,'0'),(1/64,'1/64')]:
 a,c=right(b,.28);line(a,c,a,c+5);text(a,c+25,label,'small','middle')
text(970,416,'β');text(562,177,'T')
for lo,hi,color in [(-1/64,0,'#087e8b'),(0,1/64,'#b64736')]:
 bs=[lo+(hi-lo)*i/200 for i in range(201)]
 curve([right(b,2*(sqrt(1/16+b)-sqrt(max(b,0)))) for b in bs],color)
dot(*right(0,.5),'#182a3b');text(786,226,'T(0) = 1/2','small')
text(651,145,'interior turn','small','middle');text(884,145,'reflection','small','middle')
text(775,468,'T(β) = 2[√(h + β) − √max(β, 0)]','','middle')
text(35,516,'Left: exact base projection; ξ = t and compressed ζ = t³ are given in USD:X1.','small')
text(35,542,'Right: a reflected covector jump consumes no time. Exact cap displacement is in USD:X2, equation UD30.','small')
svg.append('</svg>');out.write_text('\n'.join(svg)+'\n','utf-8');print(out)

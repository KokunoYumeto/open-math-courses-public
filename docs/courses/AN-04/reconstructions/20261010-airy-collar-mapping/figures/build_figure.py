"""Reproduce the exact affine relation slice and normalized squared powers."""
from pathlib import Path
from math import log10
import html
W,H=1040,520
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="1040" height="520" fill="#f5f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#203347}.title{font-size:20px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}.axis{stroke:#8394a3;stroke-width:1.3}</style>']
def text(x,y,t,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#8394a3',width=1.3):
    parts.append(f'<path d="M{x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def path(points,color,width=3):
    parts.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(points))+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
def dot(x,y,c):
    parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="5" fill="{c}"/>')
text(26,34,'A smooth relation through the Airy caustic', 'title')
for left,lab,sign,col in [(45,'Base projection (q, y₁)',1,'#126a8a'),(380,'Cotangent projection (q, ρ)',-1,'#ac5526')]:
    text(left,78,lab)
    x=lambda q:left+35+220*q
    y=lambda v:248-116*v
    line(x(0),y(-1.05),x(0),y(1.05))
    line(x(0),y(0),x(1.1),y(0))
    for a in [0,.5,1]:
        line(x(a),y(0)-4,x(a),y(0)+4);text(x(a),y(0)+23,str(a),'small','middle')
    for a in [-1,1]:
        line(x(0)-4,y(a),x(0)+4,y(a));text(x(0)-10,y(a)+5,str(a),'small','end')
    path([(x(t*t),y(sign*t)) for t in [-1+i/200 for i in range(401)]],col)
    dot(x(.49),y(sign*.7),col)
    text(x(.49)-10 if sign==1 else x(.49)+10,y(sign*.7)-24 if sign==1 else y(sign*.7)-9,'u = 0.7','small','end' if sign==1 else 'start')
    dot(x(0),y(0),'#203347')
    text(x(.9),y(0)-12,'q','label')
    text(left,400,'q = u²;  '+('y₁ = u' if sign==1 else 'ρ = −u'),'label')
    text(left,425,'Marked point: (0.49, '+('0.7)' if sign==1 else '−0.7)'),'small')
left=740;top=120;bottom=365
text(left-5,78,'Squared norm powers')
x=lambda v:left+220*log10(v)/log10(64)
y=lambda v:bottom-245*(log10(v)+1)/5
line(left,top-10,left,bottom);line(left,bottom,left+230,bottom)
for v in [1,4,16,64]:
    line(x(v),bottom-4,x(v),bottom+4);text(x(v),bottom+24,str(v),'small','middle')
for v in [.1,1,10,100,1000,10000]:
    yy=y(v)
    if top-3<=yy<=bottom+1:
        line(left-4,yy,left+225,yy,'#dbe2e8');text(left-9,yy+4,f'{v:g}','small','end')
vals=[64**(i/200) for i in range(201)]
path([(x(v),y(v**(-1/3))) for v in vals],'#126a8a')
path([(x(v),y(v**(5/3))) for v in vals],'#ac5526')
text(left+65,150,'λ⁵ᐟ³ (energy)','small')
text(left+50,359,'λ⁻¹ᐟ³ (L²)','small')
text(left+225,bottom+47,'λ','label','end')
text(left-5,425,'Both axes logarithmic.','small')
text(26,468,'Exact affine slice: λ = 1, μ = 0, w₁ = 0; omitted y₂ = w₂ + 2u³/3.', 'label')
text(26,496,'AC23–AC25: the powers show scaling, not fitted constants. Only projection onto q alone folds.', 'small')
parts.append('</svg>')
Path(__file__).with_name('airy-collar-relation.svg').write_text('\n'.join(parts)+'\n','utf-8')

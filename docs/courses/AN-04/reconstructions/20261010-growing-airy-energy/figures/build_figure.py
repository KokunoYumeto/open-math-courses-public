"""Exact cutoff boundaries and normalized column densities; no Airy numerics."""
from pathlib import Path
from math import sqrt,exp
import html
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="560" viewBox="0 0 1040 560">',
 '<rect width="1040" height="560" fill="#f4f8fb"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#203347}.title{font-size:21px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>']
def txt(x,y,t,cls='label',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#8a9aa8',width=1):
 parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def curve(points,color,width=3):
 parts.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(points))+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
def polygon(points,color):
 parts.append('<polygon points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="{color}"/>')
txt(28,34,'One input coefficient, two different normal scales','title')
txt(48,76,'Airy regions: ζ = b − t;  K = 8')
lx=lambda b:78+120*b
ly=lambda t:405-5.5*t
bs=[3*i/200 for i in range(201)]
polygon([(lx(b),ly(8*sqrt(1+b*b))) for b in bs]+[(lx(b),ly(16*sqrt(1+b*b))) for b in reversed(bs)],'#dcebdc')
polygon([(lx(b),ly(0)) for b in bs]+[(lx(b),ly(b)) for b in reversed(bs)],'#fae4c8')
for v in [0,10,20,30,40,50]:
 line(lx(0),ly(v),lx(3.05),ly(v),'#dae3eb');txt(lx(0)-10,ly(v)+5,str(v),'small','end')
for v in [0,1,2,3]:
 line(lx(v),ly(0),lx(v),ly(0)+5);txt(lx(v),ly(0)+23,str(v),'small','middle')
line(lx(0),ly(0),lx(0),ly(53));line(lx(0),ly(0),lx(3.1),ly(0))
curve([(lx(b),ly(b)) for b in bs],'#b3671f')
curve([(lx(b),ly(8*sqrt(1+b*b))) for b in bs],'#257951')
curve([(lx(b),ly(16*sqrt(1+b*b))) for b in bs],'#126a8a')
txt(375,111,'t = 2K⟨b⟩','small')
txt(335,252,'t = K⟨b⟩','small')
txt(238,352,'layer estimate','small')
txt(214,295,'overlap','small')
txt(180,145,'oscillatory estimate','small')
txt(307,390,'ζ > 0','small')
txt(440,440,'b','label')
txt(53,111,'t','label')
txt(52,469,'Orange: 0 < t < b.  Green: both estimates apply.','small')
txt(570,76,'Unit normal mass at every scale')
rx=lambda q:605+355*q/.5
ry=lambda density:405-2.1*density
for v in [0,32,64,96,128]:
 line(rx(0),ry(v),rx(.5),ry(v),'#dae3eb');txt(rx(0)-10,ry(v)+5,str(v),'small','end')
for v in [0,.1,.2,.3,.4,.5]:
 line(rx(v),405,rx(v),410);txt(rx(v),428,f'{v:g}','small','middle')
line(rx(0),ry(0),rx(0),ry(135));line(rx(0),405,rx(.51),405)
for m,col in [(4,'#126a8a'),(16,'#ac5526'),(64,'#7a4aa0')]:
 curve([(rx(q),ry(2*m*exp(-2*m*q))) for q in [i/2000 for i in range(1001)]],col)
txt(642,160,'m = 64','small');txt(650,330,'m = 16','small');txt(800,369,'m = 4','small')
txt(967,444,'q','label')
txt(590,469,'Density = 2m exp(−2mq); half-line integral = 1.','small')
txt(28,513,'GE11–GE13: exact cutoff boundaries. GE36: integrate each normal column before taking a frequency supremum.','small')
txt(28,540,'The right panel illustrates the estimate mechanism; these exponential curves are not Airy solutions.','small')
parts.append('</svg>')
Path(__file__).with_name('growing-airy-regions.svg').write_text('\n'.join(parts)+'\n','utf-8')

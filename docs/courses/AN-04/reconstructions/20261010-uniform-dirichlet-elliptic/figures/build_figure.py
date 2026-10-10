"""Exact symbol level sets and rescaled normal profiles; no external assets."""
from pathlib import Path
import math,html
OUT=Path(__file__).with_name('dirichlet-elliptic.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="620" viewBox="0 0 1040 620" role="img" aria-label="Compressed elliptic level sets and exact Dirichlet profiles">',
'<rect width="1040" height="620" fill="#f6f8fa"/>',
'<style>text{font-family:Arial,sans-serif;fill:#172f42}.label{font-size:16px}.small{font-size:14px}.title{font-size:22px;font-weight:bold}.grid{stroke:#d9e2e9;stroke-width:1}</style>']
def line(x1,y1,x2,y2,c='#8196a5',w=1):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>')
def text(x,y,s,cl='label',c=None):
 parts.append(f'<text x="{x}" y="{y}" class="{cl}"'+(f' style="fill:{c}"' if c else '')+'>'+html.escape(s)+'</text>')
def curve(points,color):
 parts.append('<polyline fill="none" stroke="'+color+'" stroke-width="3" points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+'"/>')
text(34,38,'An elliptic boundary point still needs its boundary condition','title')
for x in [24,526]:parts.append(f'<rect x="{x}" y="65" width="490" height="495" rx="12" fill="white" stroke="#ccd9e2"/>')
text(45,98,'Compressed principal level sets','title')
text(45,124,'s² + (1 + a)x² = 1,   s = ζ / |η|')
ox,oy,sx,sy=92,321,280,150
line(ox,155,ox,487,w=2);line(ox,oy,453,oy,w=2)
for value in [-1,1]:
 y=oy-sy*value;line(ox,y,445,y);text(58,y+5,str(value))
text(77,150,'s');text(457,326,'x');text(74,344,'0')
for a,color,label in [(-.25,'#186a90','a = −1/4'),(0,'#9d4e83','a = 0'),(.25,'#be6322','a = 1/4')]:
 pts=[]
 for k in range(301):
  theta=-math.pi/2+math.pi*k/300
  pts.append((ox+sx*math.cos(theta)/math.sqrt(1+a),oy-sy*math.sin(theta)))
 curve(pts,color)
 yy=508+[ -.25,0,.25].index(a)*19
 line(52,yy-5,76,yy-5,color,3);text(84,yy,label,'small')
parts.append(f'<circle cx="{ox}" cy="{oy}" r="6" fill="#b2383e"/>')
text(114,355,'At (0,0): compressed p = 0','small','#b2383e')
text(114,376,'Ordinary p > 0 when η ≠ 0','small')
line(ox+sx,oy-4,ox+sx,oy+4,w=2);text(ox+sx-18,oy+23,'1','small')
text(547,98,'Exact normal profiles','title');text(547,124,'t = nx; tangential factor eⁱⁿᶻ suppressed')
px,py,tx,ty=582,460,82,265
line(px,168,px,py,w=2);line(px,py,985,py,w=2)
for t in [1,2,3,4]:
 x=px+tx*t;line(x,182,x,py,'#e7edf1');text(x-4,483,str(t),'small')
text(565,483,'0','small');text(990,464,'t')
for val in [.5,1]:
 y=py-ty*val;line(px,y,980,y,'#e7edf1');text(550,y+5,str(val),'small')
curve([(px+tx*t/60,py-ty*math.exp(-t/60)) for t in range(289)],'#be6322')
curve([(px+tx*t/60,py-ty*(t/60)*math.exp(-t/60)) for t in range(289)],'#186a90')
text(657,205,'e⁻ᵗ: boundary value 1','label','#be6322')
text(688,337,'te⁻ᵗ: boundary value 0','label','#186a90')
parts.append(f'<circle cx="{px}" cy="{py-ty}" r="5" fill="#be6322"/><circle cx="{px}" cy="{py}" r="5" fill="#186a90"/>')
text(550,520,'Zero value removes the normal endpoint term.','small')
text(550,542,'Equations DE27–DE30 give the exact energies.','small')
text(34,590,'Left: symbol level sets, not rays.  Right: normalized profiles from the solved exercises.','label')
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT.name)

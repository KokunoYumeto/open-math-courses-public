"""Sample the exact scalar trace formulas; retain both one-sided endpoints."""
from pathlib import Path
from html import escape
import math
OUT=Path(__file__).with_name('one-sided-trace.svg')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="610" viewBox="0 0 1120 610" role="img" aria-labelledby="title desc">',
 '<title id="title">The positive trace differs from the symmetric principal value</title>',
 '<desc id="desc">At lambda one, kappa divided by one plus kappa squared is odd. The model-subtracted imaginary integrand is one over one plus kappa squared with full integral pi. The actual inverse kernel has imaginary limits plus one half from positive r and minus one half from negative r. No value is assigned at zero.</desc>',
 '<rect width="1120" height="610" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#153047}.title{font-size:22px;font-weight:700}.label{font-size:17px}.small{font-size:15px}</style>']
def text(x,y,s,cls='label',anchor='start',color=None):
 svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"'+(f' style="fill:{color}"' if color else '')+'>'+escape(s)+'</text>')
def line(x1,y1,x2,y2,color='#cad6df',dash=None,width=1):
 svg.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def path(points,color):
 svg.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="2.6"/>')
lx=lambda k:70+(k+4)*440/8
ly=lambda f:415-(f+.6)*315/1.8
rx=lambda r:655+(r+3)*400/6
ry=lambda f:415-(f+.7)*315/1.4
blue='#21679c';orange='#b55412'
text(65,42,'Subtract before integrating','title')
text(650,42,'Take the actual positive limit','title')
for v in [-4,-2,0,2,4]:
 line(lx(v),100,lx(v),415);text(lx(v),441,str(v),'small','middle')
for v in [-.5,0,.5,1]:
 line(70,ly(v),510,ly(v));text(58,ly(v)+5,str(v),'small','end')
line(lx(0),100,lx(0),415,'#617b8c');line(70,ly(0),510,ly(0),'#617b8c')
ks=[-4+8*j/640 for j in range(641)]
path([(lx(k),ly(k/(1+k*k))) for k in ks],blue)
path([(lx(k),ly(1/(1+k*k))) for k in ks],orange)
text(290,471,'normal frequency κ','label','middle')
text(75,81,'λ = 1; frequency window [−4, 4]','small')
text(75,505,'Blue: h(κ) = κ / (1+κ²); symmetric PV = 0','small',color=blue)
text(75,530,'Orange: Im(h − (κ+i)⁻¹) = 1 / (1+κ²)','small',color=orange)
text(75,558,'Full integral J₊(h) = iπ, including both tails.','small')
for v in [-3,-2,-1,0,1,2,3]:
 line(rx(v),100,rx(v),415);text(rx(v),441,str(v),'small','middle')
for v in [-.5,0,.5]:
 line(655,ry(v),1055,ry(v));text(644,ry(v)+5,str(v),'small','end')
line(rx(0),100,rx(0),415,'#617b8c','4 4');line(655,ry(0),1055,ry(0),'#617b8c')
for sign in [-1,1]:
 rr=[sign*3*j/300 for j in range(301)]
 path([(rx(r),ry(sign*.5*math.exp(-abs(r)))) for r in rr],blue)
 svg.append(f'<circle cx="{rx(0):.3f}" cy="{ry(sign*.5):.3f}" r="5" fill="white" stroke="{blue}" stroke-width="2.6"/>')
text(866,ry(.5)-12,'0+ : +½','small',color=blue)
text(760,ry(-.5)+28,'0− : −½','small',color=blue)
text(855,471,'output normal r','label','middle')
text(660,81,'Imaginary part of the inverse kernel','small')
text(660,505,'Im Kₕ(r) = ½ sgn(r) exp(−|r|), r ≠ 0','small',color=blue)
text(660,530,'Open endpoints mark limits, not point values.','small')
text(660,558,'Positive trace: (2π)⁻¹ J₊(h) = i/2.','small')
text(560,594,'Exact formulas and Fourier constants: TS5–TS11 and Example 1 (TS27). Curves are sampled.','small','middle')
svg.append('</svg>');OUT.write_text('\n'.join(svg)+'\n',encoding='utf-8')
print(OUT.name)

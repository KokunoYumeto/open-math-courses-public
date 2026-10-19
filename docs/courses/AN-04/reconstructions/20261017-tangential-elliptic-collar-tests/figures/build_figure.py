"""Reproduce the exact circle cone and Gaussian full-tail factor."""
from pathlib import Path
import math
from html import escape
HERE=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="750" viewBox="0 0 1100 750" role="img" aria-labelledby="title desc">',
 '<title id="title">Tangentially elliptic scalar collar tests</title>',
 '<desc id="desc">One normalized circle covector fiber with allowed cone abs kappa less than three abs eta and target region abs kappa at most abs eta. Normal directions are omitted, tangential directions retained. The exact Gaussian kernel factor and proof maps describe one scalar collar test with the original Banach remainder.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#334155"/></marker></defs>',
 '<rect width="1100" height="750" fill="#f8fafc"/>',
 '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#172c43;font-size:19px}.title{font-size:25px;font-weight:600}.small{font-size:17px}.box{fill:white;stroke:#607b91;stroke-width:2}.axis{stroke:#64748b;stroke-width:1.5}.arrow{stroke:#334155;stroke-width:2;marker-end:url(#arrow)}</style>']
def text(x,y,value,cls=''):out.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(value)}</text>')
def line(x,y,xx,yy,cls='axis'):out.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" class="{cls}"/>')
def point(theta):return 210+135*math.cos(theta),230-135*math.sin(theta)
def arc(a,b,color,width):
 pts=[point(a+(b-a)*i/150) for i in range(151)]
 out.append('<polyline points="'+' '.join(f'{x:.5f},{y:.5f}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
text(30,38,'One boundary covector fiber','title');text(30,67,'κ² + η² = 1;  every boundary base point')
line(48,230,380,230);line(210,390,210,77)
out.append('<circle cx="210" cy="230" r="135" fill="none" stroke="#cbd5e1" stroke-width="2"/>')
alpha=math.atan(1/3)
for a,b in [(alpha,math.pi-alpha),(math.pi+alpha,2*math.pi-alpha)]:
 arc(a,b,'#1c8992',15)
 for theta in [a,b]:
  x,y=point(theta);out.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#1c8992" stroke-width="2"/>')
for a,b in [(math.pi/4,3*math.pi/4),(5*math.pi/4,7*math.pi/4)]:
 arc(a,b,'#c66b22',7)
 for theta in [a,b]:
  x,y=point(theta);out.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#c66b22"/>')
text(386,237,'κ');text(223,91,'η');text(35,422,'Allowed: |κ| &lt; 3|η|'.replace('&lt;','<'));text(35,451,'Target: |κ| ≤ |η|')
text(488,38,'The exact Gaussian factor','title');text(488,67,'g(h) = exp(−h²/4) / (2√π)')
left,top,width,height=520,100,520,270
line(left,top+height,left+width+15,top+height);line(left,top+height,left,top)
for val in [0,.1,.2]:
 y=top+height-val*height/.3;line(left-5,y,left,y);text(left-36,y+6,f'{val:g}','small')
text(left-12,top-9,'g(h)','small')
pts=[]
for i in range(301):
 h=-5+10*i/300;val=math.exp(-h*h/4)/(2*math.sqrt(math.pi))
 pts.append((left+(h+5)*width/10,top+height-val*height/.3))
out.append('<polyline points="'+' '.join(f'{x:.5f},{y:.5f}' for x,y in pts)+'" fill="none" stroke="#2563a6" stroke-width="3"/>')
for h in [-4,-2,0,2,4]:
 x=left+(h+5)*width/10;line(x,top+height,x,top+height+6);text(x-8,top+height+26,str(h),'small')
text(1060,377,'h');text(488,422,'s⁰(h) = g(h) Σ cₙ exp(inh) J*PₙJ')
text(488,451,'All derivatives have every exponential tail.','small')
def box(x,y,w,lines):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="10" class="box"/>')
 for i,v in enumerate(lines):text(x+14,y+30+29*i,v)
box(30,505,305,['0 ≤ Sκ ≤ p(κ) I','⟨Sκf,f⟩ ≥ c* p ‖ΠκJf‖²','Entire weak band retained'])
box(395,505,305,['Aκ = Qκ + iSκ','‖Qκf‖ + ‖Sκf‖ ≤ C‖Aκf‖','Every residual jet controlled'])
box(760,505,310,['A = U⁻¹ β A₀ Uχ','Separated output → ‖u‖ℬ','One scalar collar-input test'])
line(339,560,390,560,'arrow');line(704,560,755,560,'arrow')
text(30,670,'β = 1 below 3a; input χ supported below 2a; omitted output has h ≥ log(3/2).','small')
text(30,708,'Proof locators: Q0–Q1, F0, G0–G2, E0–E1, A0–A1, T0.  Whole-manifold gluing uses the tangential-equator construction.','small')
out.append('</svg>');(HERE/'tangential-elliptic-collar.svg').write_text('\n'.join(out)+'\n','utf-8');print(HERE/'tangential-elliptic-collar.svg')

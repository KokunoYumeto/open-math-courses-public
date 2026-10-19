"""Exact lifted reflected ray and the global full-test proof mechanism."""
from pathlib import Path
from html import escape
import math
HERE=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="800" viewBox="0 0 1100 800" role="img" aria-labelledby="title desc">',
 '<title id="title">Global finite-test observation</title>',
 '<desc id="desc">An exact lifted wave ray starts at time minus pi, normal position one quarter, reflects at zero and one, and meets the observation section at time zero. The adjoining flow describes full local estimates, residual observation tests and the closed-defect ray contradiction. Scalar consequences retain their exact scopes.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#334155"/></marker></defs>',
 '<rect width="1100" height="800" fill="#f8fafc"/>',
 '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#172c43;font-size:19px}.title{font-size:25px;font-weight:600}.small{font-size:17px}.box{fill:white;stroke:#607b91;stroke-width:2}.axis{stroke:#64748b;stroke-width:1.5}.arrow{stroke:#334155;stroke-width:2;marker-end:url(#arrow)}</style>']
def text(x,y,v,cls=''):out.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(v)}</text>')
def line(x,y,xx,yy,cls='axis'):out.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" class="{cls}"/>')
def box(x,y,w,h,rows):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="box"/>')
 for i,row in enumerate(rows):text(x+15,y+31+i*27,row)
text(30,40,'A compact cylinder with two boundary circles','title')
text(30,72,'p = ξ² − τ²;  τ = −1;  one lifted time interval','small')
left,top,width,height=70,120,570,230
tx=lambda t:left+(t+math.pi)*width/(2*math.pi)
xy=lambda x:top+(1-x)*height
eps=math.pi/8
out.append(f'<rect x="{tx(-eps)}" y="{top}" width="{tx(eps)-tx(-eps)}" height="{height}" fill="#a4ded9" opacity=".7"/>')
line(left,top,left+width,top);line(left,top+height,left+width,top+height);line(left,top,left,top+height)
for t,label in [(-math.pi,'−π'),(0,'0'),(math.pi,'π')]:
 line(tx(t),top+height,tx(t),top+height+7);text(tx(t)-8,top+height+29,label,'small')
text(left-29,top+7,'1');text(left-29,top+height+6,'0');text(left-31,top-15,'x')
out.append(f'<line x1="{tx(0)}" y1="{top}" x2="{tx(0)}" y2="{top+height}" stroke="#1c8992" stroke-dasharray="5 4"/>')
events=[(-math.pi,.25)]+[(-math.pi+m-.25,1 if m%2 else 0) for m in range(1,7)]+[(math.pi,1-abs(1-((.25+2*math.pi)%2)))]
out.append('<polyline points="'+' '.join(f'{tx(t):.6f},{xy(x):.6f}' for t,x in events)+'" fill="none" stroke="#c66b22" stroke-width="3"/>')
for t,x in events[1:-1]:out.append(f'<circle cx="{tx(t)}" cy="{xy(x)}" r="3.5" fill="#c66b22"/>')
x0=15/4-math.pi
out.append(f'<circle cx="{tx(0)}" cy="{xy(x0)}" r="5" fill="#2563a6"/>')
text(tx(0)+10,xy(x0)-14,'(0, 15/4 − π)','small')
text(286,105,'|t| &lt; π/8'.replace('&lt;','<'),'small')
text(70,410,'t is lifted; its coordinate on X is t mod 2π.','small')
text(70,438,'Reflections reverse ξ; the time component stays −1.','small')
text(70,466,'The section t = 0 is reached at normalized time π/2.','small')
for y,rows in [(95,['Full local estimates','and exact input margins']),
 (195,['Fixed source / observation tests','Residuals remain observations']),
 (295,['Closed characteristic defect F','All permitted joining laws']),
 (395,['Maximal ray meets K₂','Contradiction to the defect'])]:
 box(720,y,350,67,rows)
 if y<395:line(895,y+71,895,y+94,'arrow')
box(30,510,1040,105,[
 'Global estimate: Nₐ(u) ≤ C(‖u‖ℬ + Σ ‖Fᵢ Pₐu‖₂ + Σ ‖Oⱼu‖₂)',
 'Full kernels, cross-chart residuals and the original Banach remainder are retained.',
 'One geometric parameter ball is fixed before every target order.'])
box(30,640,1040,100,[
 'Scalar consequences: noncompact boundary; dimension one; no boundary; mixed proved assemblies.',
 'The compact example uses full-cone source assembly and an unused-point observation assembly.',
 'Restricted-cone scalar assembly uses the angular output-reserve theorem.'])
text(30,777,'Proof locators: G0, C0, R0–R1, L0–L2, D0–D3, P0–P1, S0, T0, X2.','small')
out.append('</svg>');(HERE/'global-finite-test-observation.svg').write_text('\n'.join(out)+'\n','utf-8');print(HERE/'global-finite-test-observation.svg')

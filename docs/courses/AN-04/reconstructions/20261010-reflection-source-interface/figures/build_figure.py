"""Exact scalar transition geometry and proof-dependency diagram. CC0-1.0."""
from pathlib import Path
from html import escape
r=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590">',
'<rect width="1040" height="590" fill="#fff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#172c3e} .small{font-size:15px} .label{font-size:18px} .title{font-size:21px;font-weight:bold}</style>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#536c80"/></marker></defs>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def line(x1,y1,x2,y2,color='#536c80',width=2,dash='',arrow=False):
    extra=(' stroke-dasharray="6 5"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>')
def box(x,y,w,h,color):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{color}" stroke="#b4c4ce"/>')
X=lambda x:88+320*x/(1/8)
Y=lambda q:294-174*q
text(42,38,'Where the localization errors live','title')
text(570,38,'How the full estimate closes','title')
for low,high,color in [(-1,-.5,'#fff0d0'),(-.5,.5,'#eaf3fb'),(.5,1,'#fff0d0')]:
    parts.append(f'<rect x="88" y="{Y(high)}" width="320" height="{Y(low)-Y(high)}" fill="{color}"/>')
for q0 in [-1,-.5,0,.5,1]:
    line(88,Y(q0),408,Y(q0),dash=q0!=0)
    text(76,Y(q0)+6,{1:'1',.5:'1/2',0:'0',-.5:'−1/2',-1:'−1'}[q0],'small','end')
line(88,490,88,92,arrow=True)
line(77,Y(0),438,Y(0),arrow=True)
for sign in [-1,1]:
    line(X(0),Y(0),X(1/8),Y(sign/4),'#ad3556',3)
line(408,112,408,480,'#8c9daa',1)
text(45,82,'q = ζ / η','label')
text(444,300,'x','label')
text(87,509,'0','small','middle')
text(408,509,'1/8','small','middle')
text(153,148,'elliptic transition','small')
text(153,445,'elliptic transition','small')
text(237,263,'q = 2x','small')
text(237,361,'q = −2x','small')
text(116,227,'H = I modulo full residuals','small')
text(92,543,'p / ζ² ≥ 3/4 on 1/2 ≤ |q| ≤ 1','small')
text(92,568,'Smooth cutoffs; their support bands are shown.','small')
box(554,74,449,80,'#eaf3fb')
text(575,105,'v = Hu, with zero Dirichlet value')
text(575,132,'Negative-order regularization gives Xₛ.','small')
line(778,155,778,183,arrow=True)
box(554,185,449,94,'#fff0d0')
text(575,218,'Pv = (Θ²H)f + V Dₓu + Wu')
text(575,245,'Tested errors: elliptic transition + residuals.','small')
text(575,268,'Move Dₓ outside; use the actual H² estimate.','small')
line(778,280,778,308,arrow=True)
box(554,310,449,90,'#eaf4ef')
text(575,341,'Reflection controls T₀Hu, then Cu.')
text(575,368,'One fixed observation: Aobs = A₂,t H.','small')
text(575,390,'Retain every residual source list.','small')
line(778,401,778,429,arrow=True)
box(554,432,449,99,'#f0edf9')
text(575,463,'One common input patch, one source test.')
text(575,490,'All finite families: Tf = Bₜ,a Af exactly.','small')
text(575,517,'‖Cu‖ ≤ C (‖Af‖ + ‖Aobs u‖ + ‖u‖ℬ)','small')
text(574,565,'Geometry is fixed before the target order.','small')
parts.append('</svg>')
(r/'reflection-source-interface.svg').write_text('\n'.join(parts)+'\n','utf-8')
print('Wrote the exact transition and dependency figure.')

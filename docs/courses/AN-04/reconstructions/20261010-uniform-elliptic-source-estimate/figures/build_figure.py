"""Exact compressed normal-cap geometry and the actual source graph decomposition."""
from pathlib import Path
import hashlib,json,math
here=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="620" viewBox="0 0 1040 620">',
 '<rect width="1040" height="620" fill="#f7fafc"/>',
 '<defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#235470"/></marker></defs>',
 '<style>text{font-family:Arial,sans-serif;fill:#18354a;font-size:17px}.small{font-size:15px}.title{font-size:21px;font-weight:bold}.box{fill:white;stroke:#8aa6b7;stroke-width:1.5}</style>']
def text(x,y,t,cls='',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{t}</text>')
def line(x1,y1,x2,y2,color='#235470',width=2,arrow=False,dashed=False):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arr)"' if arrow else '')+(' stroke-dasharray="6 5"' if dashed else '')+'/>')
X=lambda x:75+1100*x
Y=lambda s:305-220*s
h=1/(4*math.sqrt(3));edge=1/math.sqrt(3)
text(28,34,'A cap separated from both roots','title')
text(28,62,'p = ζ² − 4x²η²; vertical coordinate s = ζ / |η|','small')
parts.append(f'<rect x="{X(0)}" y="{Y(.9)}" width="{X(h)-X(0)}" height="{Y(-.9)-Y(.9)}" fill="#eaf0f5"/>')
for a,b in [(edge,.9),(-.9,-edge)]:
 parts.append(f'<rect x="{X(0)}" y="{Y(b)}" width="{X(.34)-X(0)}" height="{Y(a)-Y(b)}" fill="#d5eade"/>')
line(X(0),Y(0),X(.36),Y(0),arrow=True)
line(X(0),Y(-.94),X(0),Y(.97),arrow=True)
text(X(.36)+4,Y(0)+25,'x');text(X(0)+10,Y(.97)-5,'s')
for a in [-edge,edge]:
 line(X(0),Y(a),X(.34),Y(a),color='#5f9777')
 text(X(.035),Y(a)-10 if a>0 else Y(a)+23,('1/√3' if a>0 else '−1/√3'),'small')
for a in [-1,1]:
 line(X(0),Y(0),X(.34),Y(a*.68),color='#8c6655',width=3)
 text(X(.31),Y(a*.62)+(-22 if a>0 else 35),'s = '+('2x' if a>0 else '−2x'),'small')
line(X(h),Y(-.9),X(h),Y(.9),color='#567d9c',dashed=True)
line(X(h)-5,Y(0),X(h)+5,Y(0))
text(X(h),Y(0)+30,'1/(4√3)','small',anchor='middle')
for a in [-1,1]:
 parts.append(f'<circle cx="{X(h)}" cy="{Y(a*2*h)}" r="4" fill="#8c6655"/>')
text(28,551,'Within the collar and shaded cap:','small')
text(28,578,'ζ² − 4x²η² ≥ 3ζ²/4. Pure normal directions','small')
text(28,602,'continue beyond this finite slope window.','small')
text(548,34,'Keep both actual terms','title')
boxes=[
 (84,'C u = x² Θ²H f + R u','f = Pₐu; H is the complete elliptic parametrix.'),
 (196,'Differentiate the weighted source part','Dₓ²(x²v) = (Q² − 3iQ − 2I)v,  Q = xDₓ'),
 (308,'Control R u by its residual source tree','The full boundary remainder has an H² bound.'),
 (420,'One fixed scalar source test A','‖C u‖H² + equation + traces ≤ C (‖A f‖ + ‖u‖B)')]
for i,(y,title,sub) in enumerate(boxes):
 parts.append(f'<rect x="534" y="{y}" width="487" height="88" rx="7" class="box"/>')
 text(549,y+31,title);text(549,y+61,sub,'small')
 if i<3:line(775,y+89,775,y+109,arrow=True)
text(548,551,'All coefficients and residual kernels are retained.','small')
text(548,578,'The source test is fixed across the parameter family.','small')
text(548,602,'The characteristic and global estimates remain open.','small')
parts.append('</svg>')
svg=here/'elliptic-cap-and-source-graph.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(here.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/'+svg.name,'svg_sha256':sha(svg),
 'generator_sha256':sha(Path(__file__)),'coordinates':{'characteristic_slopes':['2*x','-2*x'],'cap_edges':['1/sqrt(3)','-1/sqrt(3)'],'collar_edge':'1/(4*sqrt(3))','exact_lower_bound':'3*zeta**2/4'},
 'not_a_discontinuous_cutoff_symbol':True,'source_residual_decomposition_exact':True,
 'actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')
print(json.dumps({'figure':svg.name,'coordinate_model':'NE27; exact weighted-source identity NE13–NE16'}))

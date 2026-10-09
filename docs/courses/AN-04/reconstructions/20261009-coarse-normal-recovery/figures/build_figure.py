"""Exact index lattice and logarithmic derivative norms; CC0-1.0."""
from pathlib import Path
import hashlib,json,math,html
root=Path(__file__).resolve().parents[1]; out=Path(__file__).parent/'normal-recovery-and-boundary-layer.svg'
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="560" viewBox="0 0 1040 560" role="img" aria-labelledby="title desc">',
 '<title id="title">Finite normal recovery and a boundary layer</title>',
 '<desc id="desc">Four steps preserve total mixed order minus two. An exact sourced boundary layer has bounded second normal derivative but an unbounded third.</desc>',
 '<rect width="1040" height="560" fill="#f7f9fc"/>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 Z" fill="#147b89"/></marker></defs>']
def text(x,y,value,size=14,anchor='start',color='#18334c',weight='normal'):
 parts.append(f'<text x="{x:.3f}" y="{y:.3f}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{html.escape(value)}</text>')
def line(x1,y1,x2,y2,color='#d8e2eb',width=1,arrow=False):
 parts.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
text(24,29,'Weak input → finite normal graph, with the actual source retained',20,weight='bold')
text(24,55,'Left: mixed Sobolev indices. Right: exact L² norms for uₖ(x) = k⁻³ᐟ²(kx)e⁻ᵏˣ.',15)
for left in [24,540]:
 parts.append(f'<rect x="{left}" y="78" width="476" height="386" rx="8" fill="white" stroke="#d3e0ea"/>')
text(38,104,'N = 2: four normal steps',17,weight='bold')
text(554,104,'One boundary layer, four normal derivatives',17,weight='bold')
X=lambda r:86+(r+2)*87
Y=lambda t:148-t*54
for r in range(-2,3):
 line(X(r),132,X(r),374);text(X(r),394,str(r),13,'middle')
for t in range(-4,1):
 line(75,Y(t),451,Y(t));text(67,Y(t)+4,str(t),13,'end')
text(85,128,'t',14);text(270,418,'normal index r',14,'middle')
nodes=[(-2+i,-i) for i in range(5)]
for (r,t),(rr,tt) in zip(nodes,nodes[1:]):line(X(r)+8,Y(t)+5,X(rr)-10,Y(tt)-6,'#147b89',2.5,True)
for r,t in nodes:
 parts.append(f'<circle cx="{X(r)}" cy="{Y(t)}" r="5" fill="#147b89"/>')
 text(X(r)+9,Y(t)-12,f'({r}, {t})',13)
text(270,445,'r + t = −2 throughout; source: L² H⁻⁴',14,'middle')
RX=lambda logk:596+logk*92
RY=lambda v:374-(v+9)*15
for lg in range(5):
 line(RX(lg),134,RX(lg),374);text(RX(lg),394,str(2**lg),13,'middle')
for value in [-8,-4,0,4]:
 line(586,RY(value),971,RY(value));text(580,RY(value)+4,str(value),13,'end')
text(595,126,'log₂ norm',13);text(780,418,'k (logarithmic scale)',14,'middle')
colors=['#147b89','#b75821','#7652b7','#ab3650'];data=[]
for m,color in enumerate(colors):
 intercept=.5*math.log2((2*m*m-2*m+1)/4)
 y0=intercept;y1=intercept+4*(m-2)
 line(RX(0),RY(y0),RX(4),RY(y1),color,2.3)
 text(596+(m%2)*186,439+(m//2)*18,'j = '+str(m),13,color=color)
 data.append({'normal_derivative':m,'slope':m-2,'intercept_log2':intercept,'k_range':[1,16],'exact_squared_norm_factor':f'{2*m*m-2*m+1}/4'})
text(24,495,'The index gain uses restriction norms; no boundary value is assumed in the normal step.',15)
text(24,519,'P = Dₓ²,  uₖ(0) = 0,  ‖Puₖ‖² = 5/4.  The third derivative has squared norm 13k²/4.',15)
text(24,543,'Proofs: B1–B8 and Exercises 1–3. Lines and lattice arrows encode exact formulas, not numerical PDE solutions.',14)
parts.append('</svg>');out.write_text('\n'.join(parts)+'\n','utf-8')
check={'svg':out.relative_to(root).as_posix(),'svg_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_index_nodes':nodes,
 'logarithmic_norm_lines':data,'actually_inspected':False,'exact_coordinate_review_complete':False}
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8')
print(json.dumps({'figure':str(out),'exact_lines':4,'exact_index_steps':4}))

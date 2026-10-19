"""Reproducible sampled plots of the exact maps in X3 and X4."""
from pathlib import Path
import math,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1220" height="560" viewBox="0 0 1220 560">',
 '<rect width="1220" height="560" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#123047;font-size:18px}.title{font-size:23px;font-weight:bold}.small{font-size:16px}.axis{stroke:#526b7e;stroke-width:1.4}.curve{fill:none;stroke-width:3}</style>']
def text(x,y,label,cls=''):parts.append(f'<text x="{x}" y="{y}" class="{cls}">{label}</text>')
def line(x1,y1,x2,y2,style='axis'):parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{style}"/>')
def poly(points,color,dash=''):
    coords=' '.join(f'{x:.4f},{y:.4f}' for x,y in points)
    parts.append(f'<polyline points="{coords}" class="curve" stroke="{color}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
text(30,35,'Exact projection tests: image branches and coordinate inverses','title')
parts.append('<rect x="20" y="60" width="574" height="460" rx="8" fill="#f6fafc" stroke="#a8c0cf"/>')
parts.append('<rect x="612" y="60" width="588" height="460" rx="8" fill="#fcfaf6" stroke="#c9c0ad"/>')
text(40,95,'Proper matching with two input copies','title')
text(632,95,'A bijective mixed projection','title')
lx=lambda q:105+(q+1)*140
ly=lambda p:390-p*330
line(85,390,560,390);line(lx(0),410,lx(0),145)
for q in [-1,0,1,2]:
    line(lx(q),385,lx(q),395);text(lx(q)-7,420,str(q))
for p in [.3,.6]:
    line(lx(0)-5,ly(p),lx(0)+5,ly(p));text(lx(0)-40,ly(p)+5,str(p))
text(565,390,'q');text(lx(0)+10,150,'p')
poly([(lx(q),ly(0)) for q in [-1,2]],'#156a9e')
poly([(lx(-1),ly(0)),(lx(0),ly(0))],'#b62935','7 5')
poly([(lx(q),ly(math.exp(-1/q))) for q in [i/150 for i in range(1,301)]],'#b62935')
parts.append(f'<circle cx="{lx(0)}" cy="{ly(0)}" r="5" fill="white" stroke="#123047"/>')
text(380,175,'p = h(q)','#')
text(450,375,'p = 0')
text(45,458,'q ≤ 0: two preimages; q &gt; 0: one on each branch.','small')
text(45,489,'Three local arms at the origin. Ordinary symplectic example.','small')
rx=lambda t:905+205*t
ry=lambda u:285-140*u
line(677,285,1140,285);line(905,440,905,125)
for t in [-1,0,1]:
    line(rx(t),280,rx(t),290);text(rx(t)-8,312,str(t))
for u in [-1,1]:
    line(900,ry(u),910,ry(u));text(873,ry(u)+6,str(u))
text(1145,285,'t');text(915,130,'u')
poly([(rx(t),ry(t**3)) for t in [i/200 for i in range(-200,201)]],'#7b438b')
parts.append('<circle cx="905" cy="285" r="4" fill="#7b438b"/>')
text(1000,220,'u = t³')
text(635,458,'At t = 0: du/dt = 0; the cube-root inverse is not differentiable.','small')
text(635,489,'The smooth Lagrangian lift and its full phase remain regular.','small')
text(30,548,'X4 and X3 give the full proofs. Curves are sampled exact formulas; these are not ray trajectories.','small')
parts.append('</svg>')
out=ROOT/'figures/local-image-projection-tests.svg'
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
(ROOT/'figure-check.json').write_text(json.dumps({'figure':'figures/'+out.name,
 'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source':'figures/build_figure.py',
 'left':'Exact ordinary branch graphs p=0 and p=h(q), -1<=q<=2; input multiplicity retained.',
 'right':'Exact mixed projection u=t^3, -1<=t<=1; cube-root inverse and singular Jacobian distinguished.' 
                           },indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':out.name,'bytes':out.stat().st_size}))

"""Exact coordinate sets; only smooth graph traces are sampled. CC0-1.0."""
from pathlib import Path
import math,html,json,hashlib
ROOT=Path(__file__).resolve().parent.parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="930" viewBox="0 0 1100 930">','<rect width="1100" height="930" fill="white"/>']
def text(x,y,t,size=20,color='#193247'):
    parts.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#6a7988',width=1):
    parts.append(f'<path d="M{x1:.3f},{y1:.3f} L{x2:.3f},{y2:.3f}" stroke="{color}" stroke-width="{width}" fill="none"/>')
X=lambda t:110+(t+3)*145
def graph(fn,base,scale,color):
    pts=[(X(-3+6*i/600),base-scale*fn(-3+6*i/600)) for i in range(601)]
    d='M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in pts)
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3"/>')
def ticks(base):
    line(X(-3),base,X(3),base)
    for t in [-3,-2,-1,0,1,2,3]:
        line(X(t),base-5,X(t),base+5);text(X(t)-8,base+28,str(t),17)
    text(X(3)+24,base+7,'t',20)
def E(s):return math.exp(-1/s**2) if s>0 else 0.0
text(45,38,'A. Flat coefficient: h(t) = E(t − 1) + E(−t − 1)',23)
ticks(222);line(X(-3),75,X(-3),222)
graph(lambda t:E(t-1)+E(-t-1),222,165,'#166a8b')
line(X(-1),222,X(1),222,'#b03b54',5)
text(447,194,'h = 0 exactly',19,'#b03b54');text(74,84,'h',20)
text(45,298,'B. Characteristic set in the slice τ = 0, ξ = 1',23)
parts.append(f'<rect x="{X(-1)}" y="334" width="{X(1)-X(-1)}" height="200" fill="#eef0f3"/>')
line(X(-1),334,X(-1),534,'#8895a2');line(X(1),334,X(1),534,'#8895a2')
line(X(-3),434,X(-1),434,'#166a8b',5);line(X(1),434,X(3),434,'#166a8b',5)
line(X(-1),434,X(1),434,'#b03b54',5)
line(X(-3),334,X(-3),534)
text(71,345,'x',20);text(75,440,'0',18)
text(190,414,'N₂',22,'#166a8b');text(834,414,'N₂',22,'#166a8b')
text(470,412,'rank one',19,'#b03b54');text(433,370,'N₁₁: x ≠ 0',19)
text(434,512,'N₁₁: x ≠ 0',19)
ticks(547)
text(122,602,'The whole colored line is S. The gray strip also contains zeros outside S.',20)
text(45,656,'C. Semidefinite transverse Hessian: eigenvalues 2 and 2t²',23)
ticks(855);line(X(-3),685,X(-3),855)
graph(lambda t:2,855,9,'#166a8b');graph(lambda t:2*t*t,855,9,'#b03b54')
text(128,808,'2',18,'#166a8b');text(888,716,'2t²',18,'#b03b54')
parts.append(f'<circle cx="{X(0)}" cy="855" r="5" fill="#b03b54"/>')
text(339,914,'Rank 1 at t = 0; rank 2 for every t ≠ 0.',20)
parts.append('</svg>')
svg=ROOT/'figures/condition-p-geometry.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'coordinate_range':{'t':[-3,3],'x':[-1,1]},'sample_count_per_curve':601,
 'exact_sets':'Plateau [-1,1], saturation x=0, rank-two pieces |t|>1; all drawn from exact coordinates.',
 'sampled_curves':'h(t), 2, 2t^2; samples illustrate exact lesson formulas, not proofs.',
 'source_proof_locators':['CPG:X1','CPG:X3','CPG:V0'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure_sha256':record['svg_sha256']}))

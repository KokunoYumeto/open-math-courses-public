"""Original exact frequency cone and the actual observation/source decomposition."""
from pathlib import Path
import json,hashlib
here=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="600" viewBox="0 0 1040 600">',
 '<rect width="1040" height="600" fill="#f7fafc"/>',
 '<defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#235470"/></marker></defs>',
 '<style>text{font-family:Arial,sans-serif;fill:#18354a;font-size:17px}.small{font-size:15px}.title{font-size:21px;font-weight:bold}.box{fill:white;stroke:#8aa6b7;stroke-width:1.5}</style>']
def text(x,y,t,cls='',anchor='start'):parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{t}</text>')
def line(x1,y1,x2,y2,color='#235470',width=2,arrow=False):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arr)"' if arrow else '')+'/>')
X=lambda e:65+135*e
Y=lambda r:300-52*r
text(32,37,'Select the observed characteristic graph','title')
text(32,64,'Flat model: p = ρ² − η²; η > 0','small')
pts=[(s,f*s) for s,f in [(.4,.75),(3,.75),(3,1.25),(.4,1.25)]]
parts.append('<polygon points="'+' '.join(f'{X(e)},{Y(r)}' for e,r in pts)+'" fill="#d9ece1"/>')
line(45,300,495,300,arrow=True);line(65,510,65,82,arrow=True)
text(498,326,'η');text(79,89,'ρ')
for k in [1,2,3]:
 line(X(k),295,X(k),305);text(X(k),329,str(k),anchor='middle')
for k in [-3,-2,-1,1,2,3]:
 line(60,Y(k),70,Y(k));text(51,Y(k)+6,str(k),anchor='end')
line(X(0),Y(0),X(3),Y(3),width=3)
line(X(0),Y(0),X(3),Y(-3),color='#8b6d62',width=3)
line(X(.4),Y(.3),X(3),Y(2.25),color='#73a48b')
line(X(.4),Y(.5),X(3),Y(3.75),color='#73a48b')
text(342,90,'ρ = 5η/4','small')
text(379,133,'ρ = η','small')
text(365,207,'ρ = 3η/4','small')
text(371,479,'ρ = −η','small')
text(32,547,'Shaded edges guide a smooth cutoff;','small')
text(32,571,'unbounded normal frequencies remain in the proof.','small')
text(563,37,'Keep both parts of the estimate','title')
boxes=[
 (92,'Near the positive graph','Ordinary test Θχ₀ΨQ₊(Dₓ − A₋)u'),
 (206,'Complementary normal frequencies','C v₊ = B F₊ + R v₊'),
 (320,'The residual is tangential','R is bounded by the actual coarse mixed norm.'),
 (434,'One fixed observation A₂,ₜ','Full ordinary parametrix; uniform in parameter a.')]
for i,(y,title,sub) in enumerate(boxes):
 parts.append(f'<rect x="549" y="{y}" width="465" height="78" rx="7" class="box"/>')
 text(567,y+28,title);text(567,y+56,sub,'small')
 if i<3:line(780,y+79,780,y+108,arrow=True)
text(563,553,'Source norms and the Banach-domain conversion','small')
text(563,577,'remain explicit in the global task.','small')
parts.append('</svg>')
svg=here/'reflection-observation-interface.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(here.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/'+svg.name,
 'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'exact_model':'p=rho^2-eta^2, eta>0; roots rho=+eta,-eta; guide edges rho=3eta/4,5eta/4.',
 'projection':'Frequency plane; guide edges are not a discontinuous symbol.',
 'actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')

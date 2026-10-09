"""Original exact flat ray projection and reflection estimate diagram."""
from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590">',
 '<rect width="1040" height="590" fill="#f7fafc"/>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#255777"/></marker></defs>',
 '<style>text{font-family:Arial,sans-serif;fill:#18354a;font-size:17px}.small{font-size:15px}.title{font-size:21px;font-weight:bold}.box{fill:white;stroke:#89a4b6;stroke-width:1.5}</style>']
def text(x,y,t,cls='',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{t}</text>')
def line(x1,y1,x2,y2,color='#255777',width=2,arrow=False):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
text(34,38,'Exact transverse reflection','title')
text(34,65,'p = ξ² − η²; η = 1','small')
text(567,38,'From one strip to both branches','title')
text(567,65,'Every source and residual norm is retained.','small')
zx=lambda z:265+100*z
xy=lambda x:440-150*x
parts.append(f'<rect x="55" y="{xy(1)}" width="420" height="{xy(.5)-xy(1)}" fill="#e0efe5"/>')
line(45,440,490,440,arrow=True);line(265,458,265,103,arrow=True)
text(491,467,'z');text(281,112,'x')
for z in [-2,-1,1,2]:
 line(zx(z),435,zx(z),445);text(zx(z),468,str(z),anchor='middle')
for x in [.5,1,2]:
 line(260,xy(x),270,xy(x));text(253,xy(x)-7,str(x),anchor='end')
line(zx(2),xy(2),zx(0),xy(0),width=4)
line(zx(0),xy(0),zx(-2),xy(2),width=4)
line(zx(1.4),xy(1.4),zx(1),xy(1),width=4,arrow=True)
line(zx(-.9),xy(.9),zx(-1.3),xy(1.3),width=4,arrow=True)
text(365,132,'ξ = −1')
text(52,132,'ξ = +1')
text(353,355,'J = [½, 1]','small')
text(278,421,'(0, 0)','small')
text(50,513,'Incoming: (z, x) = (−2τ, −2τ), τ ≤ 0','small')
text(50,540,'Outgoing: (z, x) = (−2τ, 2τ), τ ≥ 0','small')
text(50,568,'Arrows: increasing Hamilton parameter τ.','small')
boxes=[
 (94,'Observe v₊ on J','Average gives a slice; cost |J|⁻½.'),
 (189,'Propagate v₊ to x = 0','Two-sided energy; complex lower terms kept.'),
 (284,'v₋(0) − v₊(0) = β b','The full common Q₀ cancels Dₓu(0).'),
 (379,'Propagate v₋ through the collar','For b = 0 the two initial outputs agree.'),
 (474,'Recover u and Dₓ(T₀u)','Subtract full roots; elliptic gap = 2|η|.')]
for i,(y,title,sub) in enumerate(boxes):
 parts.append(f'<rect x="559" y="{y}" width="450" height="69" rx="7" class="box"/>')
 text(579,y+26,title);text(579,y+51,sub,'small')
 if i<4:line(780,y+70,780,y+91,arrow=True)
parts.append('</svg>')
svg=here/'uniform-transverse-reflection.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(here.parent/'figure-check.json').write_text(json.dumps({
 'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'exact_model':'p=xi^2-eta^2; eta=1; incoming (z,x)=(-2tau,-2tau), outgoing (-2tau,2tau); J=[1/2,1].',
 'projection':'Base coordinates only; arrows follow Hamilton parameter.',
 'actually_inspected':False,'exact_coordinate_review_complete':False},indent=2)+'\n','utf-8')

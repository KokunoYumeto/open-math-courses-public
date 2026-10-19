"""Exact oblique versus orthogonal reconstruction, not characteristic geometry. CC0."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
p=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="630" viewBox="0 0 1100 630" role="img" aria-labelledby="title desc"><title id="title">Different complements solve the same equation</title><desc id="desc">For P(x,y)=(x+y,0), the input (2,1), oblique reconstruction (3,0) and orthogonal reconstruction (1.5,1.5) have the same image. The kernel is x+y=0; its perpendicular is y=x.</desc><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="context-stroke"/></marker></defs><rect width="1100" height="630" fill="#f7fafb"/><g fill="#183344" font-family="sans-serif"><text x="30" y="42" font-size="25" font-weight="bold">Same equation, different choices of solution</text><text x="40" y="84" font-size="18">X1 and V0: exact finite-dimensional projection algebra</text>''']
px=lambda x:164+91*x
py=lambda y:434-91*y
def line(x1,y1,x2,y2,color,width=2,dash='',arrow=False):
 p.append(f'<line x1="{px(x1)}" y1="{py(y1)}" x2="{px(x2)}" y2="{py(y2)}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
for t in [-1,0,1,2,3]:
 line(t,-1,t,3.3,'#dbe5e9',1);line(-1,t,3.3,t,'#dbe5e9',1)
 if t!=0:p.append(f'<text x="{px(t)-5}" y="{py(0)+22}" font-size="15">{t}</text><text x="{px(0)-24}" y="{py(t)+5}" font-size="15">{t}</text>')
line(-1,0,3.4,0,'#183344');line(0,-1,0,3.4,'#183344')
line(-1,1,1,-1,'#704495',2,'5 4');line(-.8,-.8,3.15,3.15,'#669e9d',2,'5 4')
line(-.2,3.2,3.2,-.2,'#8b969c',2,'3 5')
for x,y,color in [(2,1,'#183344'),(3,0,'#b3592b'),(1.5,1.5,'#166e80')]:
 line(0,0,x,y,color,3,arrow=True)
 p.append(f'<circle cx="{px(x)}" cy="{py(y)}" r="4" fill="{color}"/>')
p.append(f'<text x="{px(2)+12}" y="{py(1)-9}" font-size="17">v=(2,1)</text><text x="{px(3)-94}" y="{py(0)+44}" font-size="17" fill="#b3592b">E₀Pv=(3,0)</text><text x="{px(1.5)-82}" y="{py(1.5)-19}" font-size="17" fill="#166e80">EPv=(3/2,3/2)</text>')
p.append('''<text x="480" y="448" font-size="18">x</text><text x="145" y="117" font-size="18">y</text><text x="43" y="561" font-size="17" fill="#704495">Kernel: x+y=0</text><text x="256" y="561" font-size="17" fill="#669e9d">Perpendicular: y=x</text><rect x="575" y="130" width="482" height="354" rx="10" fill="#e4eff2"/><text x="603" y="170" font-size="22" font-weight="bold">P(x,y) = (x+y,0)</text><text x="603" y="217" font-size="19">All three displayed points satisfy x+y=3.</text><text x="603" y="264" font-size="19" fill="#b3592b">E₀ chooses the horizontal complement.</text><text x="603" y="309" font-size="19" fill="#166e80">E chooses the perpendicular complement.</text><text x="603" y="356" font-size="19">P E = I − Π₊</text><text x="603" y="394" font-size="19">E P = I − Π₋</text><text x="603" y="451" font-size="18">Π₋ is the orthogonal kernel projection.</text><text x="575" y="528" font-size="17">The dotted fiber is x+y=3.</text><text x="30" y="606" font-size="17">Coordinates are exact. This illustrates the normalization algebra, not a physical characteristic manifold.</text></g></svg>''')
out=root/'figures/orthogonalized-parametrix.svg';out.write_text(''.join(p),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'exact_parameters':{'a':1,'input':[2,1],'oblique_reconstruction':[3,0],'orthogonal_reconstruction':['3/2','3/2'],'kernel':'x+y=0','orthogonal_complement':'y=x','equation_fiber':'x+y=3'},'proof_locators':['N0','N1','X1','V0'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                         }
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8');print(json.dumps(check))

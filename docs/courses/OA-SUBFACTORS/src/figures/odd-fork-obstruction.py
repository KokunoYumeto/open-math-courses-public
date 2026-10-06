"""Typed odd-fork fusion obstruction, Theorem 28.4. CC0."""
from pathlib import Path
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="700" viewBox="0 0 540 700" role="img" aria-labelledby="title desc">',
       '<title id="title">An odd fork forces a half multiplicity</title>',
       '<desc id="desc">A hypothetical D7 graph has even vertices Y0, Y1 and Y2 along its long arm and odd vertices W0, W1 and tips U and V. The general D(2n+3) proof forms N-N products A=U fusion conjugate U and B=U fusion conjugate V. The dual tip rules imply their difference Delta has right-fusion eigenvalue minus one for Y=Y1. The even fusion matrix F has determinant det(F+I)=2, forcing Delta=0. Their sum contains each even class once, so A=B would force unit multiplicity one half, which is impossible.</desc>',
       '<rect width="540" height="700" fill="#fbfcff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.label{font-size:17px}.small{font-size:14px}.heading{font-size:18px;font-weight:bold}.edge{stroke:#426987;stroke-width:2.5}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
text(24,34,'An odd fork contradicts fusion integrality','title')
text(24,65,'Hypothetical D₇, n = 2; root Y₀; general proof below')
nodes=[(50,160,'Y₀',True),(140,160,'W₀',False),(230,160,'Y₁',True),(320,160,'W₁',False),(410,160,'Y₂',True),(480,95,'U',False),(480,225,'V',False)]
for i,j in [(0,1),(1,2),(2,3),(3,4),(4,5),(4,6)]:
    x,y,_,_=nodes[i];xx,yy,_,_=nodes[j]
    parts.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" class="edge"/>')
for x,y,label,even in nodes:
    parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{"#172c45" if even else "#fff"}" stroke="#426987" stroke-width="2.5"/>')
    text(x,y-20 if label!='V' else y+31,label,'label','middle')
text(24,270,'Filled: N–N modules.  Open: N–M modules.','small')
def box(y,title,line1,line2):
    parts.append(f'<rect x="24" y="{y}" width="492" height="97" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+28,title,'heading','middle')
    text(270,y+57,line1,'label','middle')
    text(270,y+82,line2,'small','middle')
box(292,'The dual tips exchange the products','A·Y = T + B;   B·Y = T + A','A = U ⊗_M Ū;  B = U ⊗_M V̄;  T = Y₁ + ⋯ + Yₙ.')
box(409,'The even matrix excludes eigenvalue −1','Δ = A − B;   Δ·Y = −Δ;   det(F + I) = 2','Lemma 28.3: injectivity forces Δ = 0, hence A = B.')
box(526,'Their sum contains the unit exactly once','A + B = Y₀ + Y₁ + ⋯ + Yₙ','A = B would give unit multiplicity 1/2: impossible.')
text(24,661,'Lemma 28.1 keeps the original and dual roots separate.','small')
text(24,687,'Theorem 28.4 excludes every D₂ₙ₊₃, n ≥ 1.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

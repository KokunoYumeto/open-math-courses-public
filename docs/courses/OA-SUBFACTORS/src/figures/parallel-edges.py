"""The exact two-class graph of the M2 amplification example in lesson 19. CC0."""
from pathlib import Path
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="470" viewBox="0 0 500 470" role="img" aria-labelledby="title desc">',
       '<title id="title">Two edges count two copies</title>',
       '<desc id="desc">The principal graph for P tensor one inside P tensor M2 has two vertices and two parallel edges. The root is the N-N unit and the other class is Y. At levels zero to four, the multiplicity is 1,2,4,8,16, yielding one matrix endomorphism block of that size. Its adjacency norm is two and its index is four.</desc>',
       '<rect width="500" height="470" fill="#fbfcff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:19px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
text(24,32,'Two edges count two copies','title')
text(24,61,'N = P ⊗ 1  ⊂  M = P ⊗ M₂','label')
parts.append('<path d="M85,144 Q250,70 415,144" fill="none" stroke="#2b6fbd" stroke-width="3"/>')
parts.append('<path d="M85,144 Q250,218 415,144" fill="none" stroke="#2b9383" stroke-width="3"/>')
for x,fill in [(85,'#1e5c9d'),(415,'white')]:
    parts.append(f'<circle cx="{x}" cy="144" r="9" fill="{fill}" stroke="#172c45" stroke-width="1.5"/>')
text(85,119,'1_N','label','middle');text(415,119,'Y','label','middle')
text(85,196,'N–N','small','middle');text(415,196,'N–M','small','middle')
text(250,225,'X = Y ⊕ Y','label','middle')
text(28,267,'Level n','small');text(143,267,'Class','small');text(258,267,'Copies','small');text(350,267,'End(Hₙ)','small')
for n,y in enumerate(range(298,423,29)):
    text(47,y,str(n));text(151,y,'1_N' if n%2==0 else 'Y');text(279,y,str(2**n))
    text(365,y,'ℂ' if n==0 else {1:'M₂',2:'M₄',3:'M₈',4:'M₁₆'}[n])
parts.append('<line x1="24" y1="433" x2="476" y2="433" stroke="#a4b4c8"/>')
text(24,458,'Adjacency norm 2; index 4. The root fixes the parity.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

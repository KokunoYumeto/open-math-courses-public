"""Cyclic charge blocks and structure maps in Theorem 27.2. CC0."""
from pathlib import Path
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="650" viewBox="0 0 540 650" role="img" aria-labelledby="title desc">',
       '<title id="title">Charge blocks determine the cyclic invariant</title>',
       '<desc id="desc">Nine two-letter words split into three charge classes modulo three, each of size three. The equal-charge entry blocks give A3 equal to three copies of M3. At the next level all nine by nine scalar coefficients give A4 equal to M9, represented with entry power u to column charge minus row charge. Odd-to-even embeddings keep supported scalar coefficients. Even-to-odd embeddings expand an entry u to power g as the cyclic shift matrix S to power g, appending coordinates i and j with i equals j plus g. Both rows are recovered by simultaneous shift of the first coordinate. Traces and Jones projections have universal formulas in Theorem 27.2.</desc>',
       '<rect width="540" height="650" fill="#fbfcff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.label{font-size:17px}.small{font-size:14px}.heading{font-size:18px;font-weight:bold}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
text(24,34,'The cyclic invariant uses only charges','title')
text(24,66,'c(a) = sum of word coordinates modulo 3')
groups=[['00','12','21'],['01','10','22'],['02','11','20']]
colors=['#d6e7f7','#e0efdb','#f5e3cf']
for q,words in enumerate(groups):
    y=91+q*47
    parts.append(f'<rect x="24" y="{y}" width="492" height="39" rx="5" fill="{colors[q]}" stroke="#8a9eaf"/>')
    text(42,y+26,f'charge {q}:    '+',  '.join(words)+'     → one M₃ block')
text(270,258,'A₃ = M₃ ⊕ M₃ ⊕ M₃;   A₄ = M₉','label','middle')
parts.append('<rect x="24" y="285" width="492" height="104" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
text(270,315,'Odd → even: retain the coefficients','heading','middle')
text(270,348,'zₐᵦ  ↦  zₐᵦ uᶜ⁽ᵇ⁾⁻ᶜ⁽ᵃ⁾','label','middle')
text(270,375,'Existing supported entries have equal charges, so u⁰ = 1.','small','middle')
parts.append('<rect x="24" y="412" width="492" height="104" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
text(270,442,'Even → odd: append a cyclic shift','heading','middle')
text(270,475,'zₐᵦ uᵍ ↦ zₐᵦ Sᵍ;   i = j + g  (mod 3)','label','middle')
text(270,502,'New charges agree: c(a) + i = c(b) + j.  Equation (27.14).','small','middle')
text(270,551,'B row: simultaneous first-coordinate shift','label','middle')
text(270,580,'zₐ₊ε,ᵦ₊ε = zₐᵦ;   ε = (1, 0, …, 0)','label','middle')
text(24,625,'Theorem 27.2: embeddings, traces and projections are universal.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

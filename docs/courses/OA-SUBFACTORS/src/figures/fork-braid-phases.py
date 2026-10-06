"""Exact terminal-character phase and commutator. CC0."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="800" viewBox="0 0 540 800" role="img" aria-labelledby="title desc">',
 '<title id="title">Real and imaginary terminal phases</title>',
 '<desc id="desc">At every even endpoint x from zero to two r, the phase b_x=(-1)^(x/2) i^r is real plus or minus one for even r and imaginary plus or minus i for odd r. In the two cup-free root channels, P has diagonal entries one half and off-diagonal minus one half. Q has off-diagonal minus b_x/2 and minus its conjugate/2. Their commutator is i Im(b_x)/2 times diagonal minus one,plus one. Even r gives zero commutator and realizes D_(r+2). Odd r gives norm one half. Exact examples r=4 and r=3 are shown on the complex unit circle. Theorem35.4 and Corollary35.5 prove the family result.</desc>',
 '<rect width="540" height="800" fill="#fbfcff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']
def text(x,y,s,cls='label',anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def box(y,title,lines,height=119):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+29,title,'heading')
    for j,line in enumerate(lines):text(270,y+60+25*j,line,'label')
text(24,32,'A phase decides the fork','title','start')
box(53,'Cup-free endpoint channel: x = 0, 2, …, 2r',[
    'Basis: ξL ψₓ, ξR ψₓ; crossing S is diagonal.',
    'bₓ = conj(λₓ) λ₂ᵣ₋ₓ = (−1)^(x/2) iʳ'])
for cx,title in [(140,'Even r: real phases'),(400,'Odd r: imaginary phases')]:
    text(cx,210,title,'heading')
    parts.append(f'<circle cx="{cx}" cy="312" r="69" fill="none" stroke="#adbacb"/>')
    parts.append(f'<path d="M{cx-92} 312 H{cx+92} M{cx} 225 V399" stroke="#7c9bbd" fill="none"/>')
    text(cx+91,337,'Re','small');text(cx+18,235,'Im','small')
for x,y,label,tx,ty in [(71,312,'−1',71,293),(209,312,'+1',209,293),
                          (400,243,'+i',427,258),(400,381,'−i',427,385)]:
    parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#276a89"/>')
    text(tx,ty,label,'small')
text(270,425,'r = 4: b₀,b₂,b₄,… = +1,−1,+1,…','small')
text(270,452,'r = 3: b₀,b₂,b₄,… = −i,+i,−i,…','small')
box(478,'Two rank-one projections',[
    'P = ½ [ 1  −1 ; −1  1 ]',
    'Qₓ = ½ [ 1  −bₓ ; −conjugate(bₓ)  1 ]'])
box(615,'The exact commutator',[
    '[P,Qₓ] = ½ i Im(bₓ) diag(−1,+1)',
    'Even r: 0.   Odd r: norm ½.'])
text(270,755,'Even r ⇒ actual principal graph Dᵣ₊₂, index δ².','heading')
text(270,778,'Theorem 35.4 and Corollary 35.5.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

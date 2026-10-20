"""Draw the exact Koszul support and Spencer indices of Example 4.31.

GPT-6.1 Sol (OpenAI), CC0 1.0.
"""
from pathlib import Path
from html import escape

support = [(0, 0, '1'), (2, 1, 't₁e₁'), (3, 1, 't₂²e₂'),
           (5, 2, 't₁t₂²e₁₂')]
parts = []

def text(x, y, value, size=18, **attrs):
    attributes = ' '.join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"'
                          for k, v in attrs.items())
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {attributes}>{escape(value)}</text>')

parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="830" viewBox="0 0 1200 830" role="img" aria-labelledby="title desc">
<title id="title">Koszul support and Spencer bidegrees</title>
<desc id="desc">For Q=F[t1,t2]/(t1 squared,t2 cubed), all nonzero Koszul homology classes occur at internal and exterior degrees (0,0), (2,1), (3,1), and (5,2). Subtracting exterior degree gives Spencer bidegrees (0,0), (1,1), (2,1), and (3,2). The degree-five class has symmetric degree three. The lower complex and homotopy explain finite support; one coefficient localization is needed to preserve homology under specialization.</desc>
<rect width="1200" height="830" fill="#f6f8fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
<rect x="25" y="106" width="555" height="412" rx="12" fill="white" stroke="#c5d0df"/>
<rect x="620" y="106" width="555" height="412" rx="12" fill="white" stroke="#c5d0df"/>
<rect x="25" y="541" width="1150" height="262" rx="12" fill="white" stroke="#c5d0df"/>
''')
text(30, 39, 'Koszul support and Spencer bidegrees', 27, font_weight=650)
text(30, 74, 'Q = F[t₁,t₂]/(t₁²,t₂³);  exterior vectors have internal degree one.', 20)
text(46, 143, 'Koszul indices (a,j)', 23, font_weight=600)
text(642, 143, 'Spencer indices (i,j),  i = a − j', 23, font_weight=600)

for panel, left, step, xmax in [('Koszul', 100, 78, 5), ('Spencer', 700, 122, 3)]:
    bottom, rise = 443, 115
    for j in range(3):
        y = bottom - j*rise
        parts.append(f'<path d="M{left} {y}H{left+xmax*step}" stroke="#dbe2ed"/>')
        text(left-28, y+6, str(j), 17, text_anchor='middle')
    for x in range(xmax+1):
        px = left + x*step
        parts.append(f'<path d="M{px} {bottom}V{bottom-2*rise}" stroke="#dbe2ed"/>')
        text(px, bottom+27, str(x), 17, text_anchor='middle')
    text(left-38, bottom-2*rise-25, 'j', 20)
    text(left+xmax*step+25, bottom+27, 'a' if panel=='Koszul' else 'i', 20)
    for a, j, label in support:
        x = a if panel=='Koszul' else a-j
        px, py = left+x*step, bottom-j*rise
        parts.append(f'<circle cx="{px}" cy="{py}" r="7" fill="#265ba8"/>')
        # Labels at exact support points; opposing labels leave room at degree two.
        dx, dy = (0, -18)
        text(px+dx, py+dy, label, 19, text_anchor='middle', fill='#174880')
text(46, 500, 'All unmarked lattice positions have zero homology.', 17)
text(642, 500, 'The top class has i = 5 − 2 = 3.', 18, fill='#174880')

text(48, 580, 'Proof mechanism: Theorem 4.30 and Example 4.31', 22, font_weight=600)
text(65, 624, '0  →  Qe₁₂  →  Qe₁ ⊕ Qe₂  →  Q  →  0', 25)
text(65, 661, 'd(ce₁₂) = t₁ce₂ − t₂ce₁;    d(ae₁ + be₂) = t₁a + t₂b.', 21)
text(65, 705, 'dεᵣ + εᵣd = tᵣ id  ⇒  tᵣHⱼ = 0  ⇒  finite internal-degree support.', 22, fill='#174880')
text(65, 746, 'For a coefficient family: split the differential cokernels after one localization.', 20)
text(65, 779, 'Then specialized homology equals the field specialization of homology.', 20)
parts.append('</g></svg>')
svg = '\n'.join(parts) + '\n'

if __name__ == '__main__':
    Path(__file__).with_suffix('.svg').write_text(svg, encoding='utf-8', newline='\n')

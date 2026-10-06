"""Exact D4 graph, Fourier blocks and trace weights, lesson 26. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="630" viewBox="0 0 540 630" role="img" aria-labelledby="title desc">',
         '<title id="title">A cyclic action realizes the rooted D4 graph</title>',
         '<desc id="desc">The root is one of three even leaves, each of Perron value one. Each leaf joins the odd central vertex, of Perron value square root three. Three Fourier projections p0, p1 and p2 form the depth-two algebra C cubed, each with trace one third; p0 is the Jones projection. The sole length-three endpoint has multiplicity three and gives the matrix algebra M3. The graph norm is square root three, index three and depth two.</desc>',
         '<rect width="540" height="630" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.label{font-size:17px}.small{font-size:14px}.edge{stroke:#426987;stroke-width:3}.leaf{fill:#fff;stroke:#426987;stroke-width:3}.odd{fill:#bcd2e8;stroke:#426987;stroke-width:3}</style>']

def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

text(24,34,'Three Fourier blocks give D₄','title')
text(24,66,'Outer cyclic action: Rᴳ ⊂ R ⊂ R ⋊ G,  |G| = 3')
centre=(270,210)
leaves=[(95,210),(405,115),(405,305)]
for x,y in leaves:
    parts.append(f'<line x1="270" y1="210" x2="{x}" y2="{y}" class="edge"/>')
parts.append('<circle cx="270" cy="210" r="12" class="odd"/>')
for i,(x,y) in enumerate(leaves):
    fill='#172c45' if i==0 else '#fff'
    parts.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{fill}" stroke="#426987" stroke-width="3"/>')
text(95,180,'root: μ = 1','label','middle')
text(270,245,'μ = √3','label','middle')
text(405,90,'μ = 1','label','middle')
text(405,338,'μ = 1','label','middle')
text(270,382,'δ = √3;  index δ² = 3;  depth = 2','label','middle')
parts.append('<rect x="24" y="410" width="492" height="142" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
text(270,439,'A₁ = ℂ³:  p₀, p₁, p₂;  τ(pⱼ) = 1/3','label','middle')
text(270,472,'p₀ = e_P = (1 + U + U²)/3','label','middle')
text(270,507,'A₂ = M₃:  three length-three paths','label','middle')
text(270,536,'Minimal matrix-projection trace at this level: 1/3','small','middle')
text(24,588,'Lemma 26.1 and Theorem 26.2 identify the rooted graph.','small')
text(24,613,'Theorem 26.4: every D₄ pair is a cyclic crossed product.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

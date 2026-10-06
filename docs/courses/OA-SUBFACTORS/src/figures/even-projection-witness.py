"""Reproduce the tensor-position diagram for the commuting-projection example."""
from pathlib import Path

lines=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="490" viewBox="0 0 1000 490" role="img" aria-label="Five tensor positions, even projections and a noncommuting commutant witness">',
'<rect width="1000" height="490" fill="#ffffff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#142b3e} .title{font-size:26px;font-weight:700}.label{font-size:22px}.small{font-size:19px}.math{font-size:25px} .blue{stroke:#236aa1;stroke-width:4}.orange{stroke:#bd5c19;stroke-width:5}</style>',
'<text x="45" y="44" class="title">Five tensor factors and a commutant witness</text>',
'<text x="45" y="76" class="small">Each position carries V = C²; eᵢ projects positions i and i+1 onto (|01⟩ − |10⟩)/√2.</text>']
xs=[100,290,480,670,860]
for i,x in enumerate(xs,1):
    lines.extend([f'<circle cx="{x}" cy="230" r="25" fill="#eef3f7" stroke="#45657e" stroke-width="2"/>',f'<text x="{x}" y="237" text-anchor="middle" class="label">{i}</text>'])
for i,(a,b) in enumerate(zip(xs,xs[1:]),1):
    y=140 if i%2 else 188
    cls='blue' if i%2 else 'orange'
    lines.extend([f'<path d="M {a} 202 V {y} H {b} V 202" fill="none" class="{cls}"/>',f'<text x="{(a+b)/2}" y="{y-13}" text-anchor="middle" class="label">e{i}</text>'])
lines.extend(['<text x="45" y="295" class="math">q = (1 − e₂)(1 − e₄),    X = qe₁q,    Y = qe₃q</text>',
'<text x="45" y="331" class="small">X and Y commute with e₂ and e₄ because q is orthogonal to both projections.</text>',
'<text x="45" y="361" class="small">They commute with every later even projection by the distant-commutation relation.</text>',
'<rect x="45" y="389" width="910" height="62" rx="6" fill="#edf6fb" stroke="#236aa1"/>',
'<text x="500" y="429" text-anchor="middle" class="math">⟨00001 | [X,Y] | 00100⟩ = 1/32 ≠ 0</text>',
'<text x="45" y="478" class="small">Exact witness for Theorem 5.2. The abelian even-generator algebra has a noncommutative commutant.</text>','</svg>'])
Path(__file__).with_suffix('.svg').write_text('\n'.join(lines),encoding='utf-8')

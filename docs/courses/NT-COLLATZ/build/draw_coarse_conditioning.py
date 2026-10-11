"""Reproducible exact finite diagram for uniform compositions of eight."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations

root=Path(__file__).resolve().parents[1]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="735" viewBox="0 0 440 735" role="img" aria-labelledby="title desc">',
     '<title id="title">Fixed-total clocks and the law of a prefix</title>',
     '<desc id="desc">All thirty-five compositions of eight into four positive parts give centered clocks returning to zero. The lower panel compares the exact conditional and independent distributions of the first two coordinates summed, including the whole tail above six.</desc>',
     '<rect width="440" height="735" fill="white"/>',
     '<g font-family="sans-serif" fill="#172c38">',
     '<text x="220" y="26" font-size="19" text-anchor="middle">The clock has fixed endpoints</text>']
def path_y(z): return 164-28*float(z)
for value in range(-3,4):
    y=path_y(value)
    out += [f'<line x1="52" x2="388" y1="{y}" y2="{y}" stroke="#d8e2e8"/>',
            f'<text x="43" y="{y+5}" font-size="14" text-anchor="end">{value}</text>']
for cuts in combinations(range(1,8),3):
    partial=(0,)+cuts+(8,)
    points=' '.join(f'{52+84*k},{path_y(F(s)-2*k)}' for k,s in enumerate(partial))
    out.append(f'<polyline points="{points}" fill="none" stroke="#307f9f" stroke-width="1.2" opacity=".35"/>')
for k in range(5):
    out.append(f'<text x="{52+84*k}" y="276" font-size="15" text-anchor="middle">{k}</text>')
out += ['<text x="220" y="301" font-size="15" text-anchor="middle">Prefix length k</text>',
        '<text x="220" y="324" font-size="14" text-anchor="middle">Vertical coordinate: Sₖ − 2k · n = 4, s = 8</text>',
        '<text x="220" y="376" font-size="19" text-anchor="middle">The prefix laws differ</text>',
        '<text x="220" y="400" font-size="14" text-anchor="middle">Mass of S₂ = t, with the full tail grouped</text>']
q=[F(v,35) for v in (5,8,9,8,5)]+[F(0)]
p=[F(1,4),F(1,4),F(3,16),F(1,8),F(5,64),F(7,64)]
for level in (F(0),F(1,8),F(1,4)):
    y=626-600*float(level)
    out += [f'<line x1="50" x2="409" y1="{y}" y2="{y}" stroke="#d8e2e8"/>',
            f'<text x="44" y="{y+5}" font-size="13" text-anchor="end">{level}</text>']
for j,label in enumerate(('2','3','4','5','6','> 6')):
    x=73+61*j
    for dx,mass,color in ((-10,q[j],'#125567'),(10,p[j],'#b45309')):
        h=600*float(mass)
        out.append(f'<rect x="{x+dx-8}" y="{626-h}" width="16" height="{h}" fill="{color}"/>')
    out.append(f'<text x="{x}" y="650" font-size="15" text-anchor="middle">{label}</text>')
out += ['<rect x="47" y="674" width="14" height="14" fill="#125567"/>',
        '<text x="67" y="686" font-size="14">Conditioned on S₄ = 8</text>',
        '<rect x="259" y="674" width="14" height="14" fill="#b45309"/>',
        '<text x="279" y="686" font-size="14">Independent</text>',
        '<text x="220" y="717" font-size="14" text-anchor="middle">Exact ℓ¹ distance: 533/1120</text>',
        '</g></svg>']
(root/'figures/conditioned-prefix.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')

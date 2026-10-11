"""Reproducible schematic of an actual first-entrance path and its cost bound."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
xs=[80,210,340,470,600,730]
orbit=[7,11,17,13,5,1]
sorted_states=[5,7,11,13,17]
ranks=[3,5,7,9,11]
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="565" viewBox="0 0 820 565" role="img" aria-labelledby="title desc">
<title id="title">Distinct states before the first entrance</title>
<desc id="desc">The actual odd orbit 7,11,17,13,5,1 first reaches at most two at its fifth return. Its previous five states are distinct. Sorting only to bound the sum gives 5,7,11,13,17, at least 3,5,7,9,11 respectively.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#25645f"/></marker></defs>
<rect width="820" height="565" rx="16" fill="#f8fafc"/>
<g font-family="Arial,sans-serif" fill="#183147">
<text x="30" y="42" font-size="23" font-weight="bold">First entrance controls an accumulated cost</text>
<text x="30" y="77" font-size="18">Actual odd-return orbit, with target H = 2</text>''']
for i in range(5):
    parts.append(f'<path d="M{xs[i]+25} 135H{xs[i+1]-25}" stroke="#25645f" stroke-width="2" marker-end="url(#arrow)"/>')
for i,v in enumerate(orbit):
    col="#dfede9" if i<5 else "#ecddea"
    parts.append(f'<circle cx="{xs[i]}" cy="135" r="23" fill="{col}"/><text x="{xs[i]}" y="142" text-anchor="middle" font-size="21">{v}</text>')
parts.append('''<text x="30" y="197" font-size="18">The five states before entrance are distinct, but not monotone.</text>
<rect x="25" y="229" width="770" height="188" rx="10" fill="#e4efed"/>
<text x="45" y="261" font-size="18" font-weight="bold">Reorder only for the reciprocal sum</text>''')
for i,(v,r) in enumerate(zip(sorted_states,ranks)):
    x=xs[i]+45
    parts.append(f'<text x="{x}" y="304" text-anchor="middle" font-size="22">{v}</text><text x="{x}" y="341" text-anchor="middle" font-size="21">≥</text><text x="{x}" y="378" text-anchor="middle" font-size="22">{r}</text>')
parts.append('''<text x="45" y="402" font-size="16">Lower row: the five smallest odd integers strictly above H.</text>
<text x="30" y="460" font-size="19">Σ 1/Mᵢ ≤ 1/3 + 1/5 + 1/7 + 1/9 + 1/11</text>
<text x="30" y="499" font-size="18">An integral bounds this sum logarithmically in the number of returns.</text>
<text x="30" y="533" font-size="17">This is a bound on an orbit cost, not a change to the trajectory.</text>
</g></svg>''')
(ROOT/'figures/first-entrance-cost.svg').write_text('\n'.join(parts),encoding='utf-8')
print('Wrote figures/first-entrance-cost.svg')

"""Exact dyadic-level diagram: three strict intervals of length 3/2."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="850" height="440" viewBox="0 0 850 440" role="img" aria-labelledby="title desc">',
 '<title id="title">A successor enters only after the strict phase threshold</title>',
 '<desc id="desc">Intervals (1/4,7/4), (1/2,2) and (3/4,9/4). The first integer is one. Integer two is excluded in the first two intervals and included in the third.</desc>',
 '<rect width="850" height="440" fill="#fbfaf7"/>',
 '<g font-family="Georgia,serif" fill="#152b39">',
 '<text x="35" y="36" font-size="23">A band of length 3/2 in integer-level coordinates</text>',
 '<text x="35" y="65" font-size="17">Threshold θ = 1/2. Both interval endpoints are strict.</text>']
def X(v):return 290+180*v
for phase,y,label in [(0.25,138,'x = 1/4'),(0.5,246,'x = 1/2'),(0.75,354,'x = 3/4')]:
    right=phase+1.5
    parts.extend([f'<text x="35" y="{y+6}" font-size="21">{label}</text>',
      f'<line x1="{X(0)}" y1="{y}" x2="{X(2.6)}" y2="{y}" stroke="#b9c4ca" stroke-width="2"/>',
      f'<line x1="{X(phase)}" y1="{y}" x2="{X(right)}" y2="{y}" stroke="#16736b" stroke-width="6"/>'])
    for k in [0,1,2]:
        parts.append(f'<line x1="{X(k)}" y1="{y-12}" x2="{X(k)}" y2="{y+12}" stroke="#536774"/>')
        parts.append(f'<text x="{X(k)-5}" y="{y+38}" font-size="17">{k}</text>')
    for endpoint in [phase,right]:
        parts.append(f'<circle cx="{X(endpoint)}" cy="{y}" r="7" fill="#fbfaf7" stroke="#16736b" stroke-width="3"/>')
    for k in [1,2]:
        if phase<k<right:
            parts.append(f'<circle cx="{X(k)}" cy="{y}" r="7" fill="#204d81"/>')
    note='Only the first level' if phase<0.5 else ('Successor at endpoint: excluded' if phase==0.5 else 'Both levels admitted')
    parts.append(f'<text x="290" y="{y-27}" font-size="17">{note}</text>')
parts.extend(['<text x="35" y="421" font-size="16">Integer one carries q₀; integer two, when admitted, carries its own weight q₁.</text>','</g></svg>'])
(ROOT/'figures/strict-phase.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('figures/strict-phase.svg')

"""Reproduce the exact countdown example in the scheduled-transport lesson."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
q,h,budget=3,1,2
starts=(3,100)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="614" viewBox="0 0 440 614" role="img" aria-labelledby="title desc">',
'<title id="title">Equal landing laws, different travel times</title>',
'<desc id="desc">Countdown map D(n)=max(n-1,1). Inputs 3 and 100 both first land at 3, taking 0 and 97 steps. Both then take two more steps to reach 1. With a first-leg budget of 2 the second input fails the schedule.</desc>',
'<rect width="440" height="614" rx="10" fill="#f4f8fa"/>',
'<g font-family="system-ui,sans-serif" fill="#172c38">',
'<text x="22" y="34" font-size="21" font-weight="650">Same landing. Different times.</text>',
'<text x="22" y="66" font-size="18">Countdown D(n) = max(n − 1, 1)</text>',
'<text x="22" y="93" font-size="16">An example map, not the Collatz map</text>']
for row,n in enumerate(starts):
    y=116+row*204
    first=max(n-q,0); remaining=q-h; total=first+remaining
    color="#16645a" if first<=budget else "#9d4327"
    label="Meets the first-leg budget" if first<=budget else "Misses the first-leg budget"
    parts.extend([
        f'<rect x="16" y="{y}" width="408" height="187" rx="8" fill="#fff" stroke="#b7cbd5"/>',
        f'<text x="32" y="{y+29}" font-size="19" font-weight="650">Start {n} · first threshold 3</text>',
        f'<text x="32" y="{y+61}" font-size="19">{n} → 3: {first} steps</text>',
        f'<text x="32" y="{y+91}" font-size="19">3 → 2 → 1: {remaining} more steps</text>',
        f'<text x="32" y="{y+123}" font-size="19" font-weight="650">Total time to 1: {total} steps</text>',
        f'<text x="32" y="{y+159}" font-size="17" fill="{color}">{escape(label)} of {budget}</text>'
    ])
parts.extend([
'<text x="22" y="550" font-size="18">Both landing laws are the point mass at 3.</text>',
'<text x="22" y="579" font-size="18">Their event distance is exactly zero.</text>',
'</g></svg>'])
(ROOT/'figures/scheduled-transport.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Wrote exact countdown figure: first legs 0,97; totals 2,99.')

"""Reproduce Figure 17.1. Original CC0 diagram; no third-party graphics."""
from pathlib import Path
from html import escape

parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="990" viewBox="0 0 1000 990" role="img" aria-labelledby="title desc">
<title id="title">Sea patterns and the finite graph corner</title>
<desc id="desc">Four orthogonal sea patterns with exact excitation energy and trace weights, followed by four levels of the A4 corner rooted at odd vertex 1.</desc>
<rect width="1000" height="990" rx="18" fill="#f6f7fb"/>
<style>text{font-family:Arial,sans-serif;fill:#17233b}.title{font-size:28px;font-weight:bold}.label{font-size:22px}.small{font-size:19px}.mono{font-family:Consolas,monospace;font-size:22px}</style>
<text x="36" y="49" class="title">One finite corner inside an infinite thermal factor</text>
<text x="36" y="86" class="small">Theorem 17.2 • modes outside the window continue the indicated sea pattern</text>
<rect x="25" y="108" width="950" height="365" rx="12" fill="white" stroke="#bcc8da"/>
<text x="44" y="146" class="label">Pattern</text>
<text x="706" y="146" class="label">Energy</text>
<text x="822" y="146" class="label">Trace / u₀</text>''']
xs=[187+70*k for k in range(7)]
for n,x in zip(range(-3,4),xs):
    parts.append(f'<text x="{x}" y="178" text-anchor="middle" class="small">{n}</text>')
for row,j in enumerate([-1,0,1,2]):
    y=219+58*row
    parts.append(f'<text x="54" y="{y+7}" class="mono">p_{j}</text>')
    parts.append(f'<text x="139" y="{y+7}" class="label">⋯</text>')
    for n,x in zip(range(-3,4),xs):
        fill='#345dcc' if n<j else 'white'
        parts.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{fill}" stroke="#345dcc" stroke-width="3"/>')
    parts.append(f'<text x="657" y="{y+7}" class="label">⋯</text>')
    energy=j*(j-1)//2
    trace={-1:'λ',0:'1',1:'λ⁻¹',2:'λ⁻²'}[j]
    parts.append(f'<text x="733" y="{y+7}" text-anchor="middle" class="mono">{energy}</text>')
    parts.append(f'<text x="871" y="{y+7}" text-anchor="middle" class="label">{trace}</text>')
parts.append('''<text x="44" y="455" class="small">Filled: fₙ = 1 • hollow: fₙ = 0 • distinct rows impose incompatible occupations</text>
<rect x="25" y="493" width="950" height="368" rx="12" fill="white" stroke="#bcc8da"/>
<text x="44" y="532" class="label">Sea corner q = p₀ for A₄, root r = 1</text>
<text x="44" y="570" class="small">Negative pieces: rank one, root fixed • nonnegative pieces: transfer B = [[1,1],[1,0]]</text>
<text x="71" y="613" class="label">L = m+1</text>
<text x="255" y="613" class="label">Endpoint 1</text>
<text x="443" y="613" class="label">Endpoint 3</text>
<text x="643" y="613" class="label">Normalized minimal traces</text>''')
for row,(a,b) in enumerate([(1,1),(2,1),(3,2),(5,3)]):
    y=653+48*row
    parts.append(f'<text x="119" y="{y}" text-anchor="middle" class="mono">{row+1}</text>')
    parts.append(f'<text x="302" y="{y}" text-anchor="middle" class="mono">M_{a}</text>')
    parts.append(f'<text x="490" y="{y}" text-anchor="middle" class="mono">M_{b}</text>')
    parts.append(f'<text x="655" y="{y}" class="label">φ⁻{row+1}, φ⁻{row+2}</text>')
parts.append('''<text x="44" y="847" class="small">Each block count × its minimal trace sums to 1 • φ = (1+√5)/2</text>
<text x="36" y="905" class="label">λ &gt; 1: unbounded corner matrix sizes ⇒ qMq is II₁</text>
<text x="36" y="943" class="label">Orthogonal pⱼ, j ≤ 0: trace sums diverge ⇒ M is II∞</text>
<text x="36" y="975" class="small">Exact locators: (17.5)–(17.7), (17.10) • original CC0 figure</text>
</svg>''')
output=Path(__file__).with_suffix('.svg')
output.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(output.name)

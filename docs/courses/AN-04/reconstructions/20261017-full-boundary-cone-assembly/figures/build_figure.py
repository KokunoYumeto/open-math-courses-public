"""Exact cutoff ratios and scalar norm-recovery diagram, not kernel samples."""
from pathlib import Path
import xml.etree.ElementTree as ET
p=Path(__file__).with_name('full-boundary-cone-assembly.svg')
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650" role="img" aria-labelledby="title desc">
<title id="title">Coercive collar test and positive interior gluing</title><desc id="desc">The normal axis is x/a. Deep alpha is supported below one half, while the interior term has all output above one. Collar ellipticity through two overlaps the guaranteed interior ellipticity from three halves to three. The whole collar norm is recovered from one scalar test plus the original Banach norm.</desc>
<rect width="1100" height="650" rx="12" fill="#f3f7f8"/>
<g font-family="Arial,sans-serif" fill="#152d3a"><text x="35" y="42" font-size="25">The whole boundary cosphere is allowed</text>
<text x="35" y="76" font-size="18">Exact relative cutoff bands; the boundary Y may have arbitrary compact geometry.</text>
<path d="M220 118 H1000" stroke="#526b76"/>
''']
scale=lambda x:220+190*x
for x,label in [(0,'0'),(.25,'1/4'),(.5,'1/2'),(1,'1'),(1.5,'3/2'),(2,'2'),(3,'3'),(4,'4')]:
 xx=scale(x);parts.append(f'<path d="M{xx} 112 V124" stroke="#526b76"/><text x="{xx}" y="144" font-size="15" text-anchor="middle">{label}</text>')
parts.append('<text x="1020" y="123" font-size="17">x/a</text>')
rows=[('deep α',175,.5,.25),('input χ₀',220,1,.5),('χ and β',265,3,2)]
for label,y,supp,one in rows:
 parts.append(f'<text x="45" y="{y+22}" font-size="20">{label}</text><rect x="220" y="{y}" width="{190*supp}" height="29" fill="#d3e5ee"/><rect x="220" y="{y}" width="{190*one}" height="29" fill="#548ca5"/>')
parts.append('''<text x="45" y="342" font-size="20">ellipticity</text>''')
parts.append(f'<rect x="220" y="320" width="380" height="30" fill="#548ca5"/><rect x="{scale(1.5)}" y="359" width="285" height="30" fill="#d9aa5c"/>')
parts.append('''<text x="618" y="342" font-size="17">collar A_b: χ = 1</text>
<text x="813" y="381" font-size="17">interior Q_I</text>
<text x="45" y="425" font-size="17">Dark: cutoff = 1. Light: possible cutoff support. Orange: guaranteed interior ellipticity.</text>
<text x="45" y="461" font-size="18">The whole output of Q_I lies in x/a &gt; 1; hence α Q_I = 0 exactly.</text>
<text x="45" y="505" font-size="21">G_M(U χ f) ≤ C ‖A_b f‖₂;   ‖A_b Dₐu‖₂ ≤ C (‖A Dₐu‖₂ + ‖u‖_ℬ)</text>
<text x="45" y="549" font-size="20">A = A_b + Q_I;   every full collar tail remains in the cylinder estimate.</text>
<text x="45" y="590" font-size="17">Support and norm schematic. Proof: C0, H1–H3, L0–L1, A0–A2, T0; FC9–FC19.</text>
<text x="45" y="624" font-size="16">The interior term also covers the remaining prescribed interior microsupport, outside this axis.</text></g></svg>''')
p.write_text(''.join(parts),'utf-8');ET.parse(p);print(p.name)

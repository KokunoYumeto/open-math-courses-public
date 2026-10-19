"""Exact real sections of the two-root principal energy; original SVG, no raster inputs."""
from pathlib import Path
from math import sin,cos,pi,sqrt
from html import escape
out=Path(__file__).with_name('uniform-sobolev-cauchy-energy.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1125" height="590" viewBox="0 0 1125 590" role="img" aria-labelledby="title desc">',
 '<title id="title">A Sobolev-independent energy with a fixed root gap</title>',
 '<desc id="desc">Three exact real sections of z0 squared over2 plus z1 squared over2 epsilon squared equals1. Blue and rust points are unit-energy branch eigenvectors. A fixed epsilon gives norm comparison independent of the Sobolev exponent. The ellipses flatten when epsilon tends to zero. The full operator energy also includes an H minus1 term to control its lower-order remainder.</desc>',
 '<rect width="1125" height="590" fill="#fff"/>',
 '<style>text{font-family:Georgia,serif;fill:#183247}.heading{font-family:Arial,sans-serif;font-weight:bold}.axis{stroke:#667987;stroke-width:1.2}.ellipse{stroke:#176b78;fill:#e7f4f5;stroke-width:2.4}.minus{fill:#2458a6}.plus{fill:#ac491e}</style>',
 '<text x="30" y="34" font-size="25" class="heading">The principal energy does not depend on the Sobolev weight</text>',
 '<text x="30" y="65" font-size="20">Pε = Dₜ² − ε²Dₓ², ξ &gt; 0:  Eε(z) = z₀²/2 + z₁²/(2ε²),  Eε = 1</text>']
for k,(epsilon,label) in enumerate([(1,'1'),(.5,'1/2'),(.25,'1/4')]):
    left=375*k;cx=left+180;cy=235;scale=78
    parts.append(f'<text x="{left+35}" y="111" font-size="23" class="heading">ε = {label}</text>')
    pts=' '.join(f'{cx+sqrt(2)*scale*cos(i*pi/150):.5f},{cy-sqrt(2)*epsilon*scale*sin(i*pi/150):.5f}' for i in range(301))
    parts.append(f'<polygon class="ellipse" points="{pts}"/>')
    parts.append(f'<path class="axis" d="M {left+35} {cy} H {left+330} M {cx} 119 V 357"/>')
    parts.append(f'<text x="{left+332}" y="{cy+7}" font-size="19">z₀</text><text x="{cx+9}" y="135" font-size="19">z₁</text>')
    parts.append(f'<text x="{cx-16}" y="{cy+20}" font-size="16">0</text>')
    for sign,color,sub in [(-1,'minus','−'),(1,'plus','+')]:
        px=cx+scale;py=cy-sign*epsilon*scale
        parts.append(f'<path d="M {cx} {cy} L {px} {py}" stroke="{("#2458a6" if sign<0 else "#ac491e")}" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{px}" cy="{py}" r="4.5" class="{color}"/>')
        ly=py+(23 if sign<0 else -12)
        parts.append(f'<text x="{px+8}" y="{ly}" font-size="19" class="{color}">v{sub}</text>')
    parts.append(f'<text x="{left+35}" y="391" font-size="18">v− = (1, −ε),  v+ = (1, ε)</text>')
parts+=['<text x="30" y="431" font-size="20">½‖z‖² ≤ Eε(z) ≤ (2ε²)⁻¹‖z‖²: fixed ε gives constants independent of s.</text>',
 '<text x="30" y="462" font-size="20">As ε → 0 the roots merge; the comparison constant is not uniform in ε.</text>',
 '<path d="M30 483 H1090" stroke="#bed0d5"/>',
 '<text x="30" y="515" font-size="20">Full operator:  JK = I + R₋₁  ⇒  ‖Uₛ‖² ≲ ‖KUₛ‖² + ‖Uₛ‖²H⁻¹.</text>',
 '<text x="30" y="547" font-size="18">Real fibre sections shown. Homogeneous jets are used away from zero frequency.</text>',
 '<text x="30" y="575" font-size="18">Exact proof: §3.1 U1–U4 and Exercise 24. Mathematical antecedent: Hörmander III, §23.2.</text>',
 '</svg>']
out.write_text('\n'.join(parts)+'\n','utf-8')
print(out.name)

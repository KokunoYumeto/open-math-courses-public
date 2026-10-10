"""Editable exact path diagram for the last-jump decomposition."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
points=[(0,0),(1,3),(3,8),(4,11)]
x=lambda j:90+125*j
y=lambda l:440-29*l
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="530" viewBox="0 0 820 530" role="img" aria-labelledby="title desc">
<title id="title">Separating the last jump</title>
<desc id="desc">Path (0,0), (1,3), (3,8), (4,11). The boundary is height 6. The first crossing is (3,8), with deficit 3 before the final jump and overshoot 2 after it.</desc>
<style>text{font-family:Georgia,serif;fill:#163044;font-size:19px}.title{font-size:25px}.small{font-size:16px}.axis{stroke:#526879;stroke-width:1.5;fill:none}.path{stroke:#08677c;stroke-width:3;fill:none}.boundary{stroke:#b36114;stroke-width:2;stroke-dasharray:8 5;fill:none}.guide{stroke:#71838c;stroke-dasharray:4 4;fill:none}.bracket{stroke:#b36114;stroke-width:2;fill:none}</style>
<rect width="820" height="530" fill="white"/>
<text x="410" y="31" text-anchor="middle" class="title">Separating the last jump</text>
<path class="axis" d="M90 75 V440 H650"/>
<text x="69" y="77">l</text><text x="660" y="448">j</text>''']
for j in range(5):
    parts.append(f'<path class="axis" d="M{x(j)} 440 v5"/><text x="{x(j)}" y="468" text-anchor="middle">{j}</text>')
for l in [0,3,6,8,11]:
    parts.append(f'<path class="axis" d="M85 {y(l)} h5"/><text x="76" y="{y(l)+6}" text-anchor="end">{l}</text>')
parts.append(f'<path class="boundary" d="M90 {y(6)} H650"/><text x="100" y="{y(6)-12}">s = 6</text>')
parts.append('<polyline class="path" points="'+' '.join(f'{x(j)},{y(l)}' for j,l in points)+'"/>')
for j,l in points:
    color='#b36114' if (j,l)==(3,8) else '#08677c'
    parts.append(f'<circle cx="{x(j)}" cy="{y(l)}" r="5" fill="{color}"/>')
parts.extend([
    f'<text x="{x(1)-15}" y="{y(3)+31}">(1,3)</text>',
    f'<text x="{x(3)-210}" y="{y(8)-17}">(3,8): first crossing</text>',
    f'<text x="{x(4)+13}" y="{y(11)+5}">(4,11)</text>',
    f'<path class="guide" d="M{x(1)} {y(3)} H700 M{x(3)} {y(8)} H700"/>',
    f'<path class="bracket" d="M685 {y(8)} h12 M691 {y(8)} V{y(6)} M685 {y(6)} h12"/>',
    f'<text x="707" y="{(y(8)+y(6))/2+6}">r = 2</text>',
    f'<path class="bracket" d="M685 {y(6)} h12 M691 {y(6)} V{y(3)} M685 {y(3)} h12"/>',
    f'<text x="707" y="{(y(6)+y(3))/2+6}">v = 3</text>',
    '<text x="275" y="345" class="small">Last jump: (u, r + v) = (2,5)</text>',
    '<text x="410" y="507" text-anchor="middle" class="small">Renewal paths and first-crossing locations · Proposition 1</text></svg>'
])
(ROOT/'figures/renewal-crossing.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

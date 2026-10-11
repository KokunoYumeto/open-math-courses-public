"""Draw the exact finite example of weighted absorption in Lesson 32."""
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
rows=[(F(1,5),F(1,45),F(1,90),F(1,30)),
      (F(3,10),F(1,30),F(1,90),F(2,45)),
      (F(1,2),F(1,18),F(1,90),F(1,15))]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="460" viewBox="0 0 440 460" role="img" aria-labelledby="title desc">',
'<title id="title">Summing errors against actual mass</title>',
'<desc id="desc">Three time slices have actual masses one fifth, three tenths, and one half. At relative coefficient one tenth and absolute remainder one hundredth per time, the absorbed errors are one thirtieth, two forty-fifths, and one fifteenth. Their sum is thirteen ninetieths.</desc>',
'<rect width="440" height="460" fill="#f5f8fa"/>',
'<g font-family="Arial, sans-serif" fill="#172c38">',
'<text x="24" y="32" font-size="20" font-weight="bold">Errors follow their actual masses</text>',
'<text x="24" y="59" font-size="15">Relative coefficient 1/10; remainder 1/100 per time</text>']
for i,(Y,rel,absolute,total) in enumerate(rows):
    y=96+98*i
    w1=float(rel*4800);w2=float(absolute*4800)
    parts += [f'<text x="24" y="{y}" font-size="17">Time {i+1}: actual mass {Y}</text>',
              f'<rect x="24" y="{y+12}" width="{w1}" height="32" fill="#276e87"/>',
              f'<rect x="{24+w1}" y="{y+12}" width="{w2}" height="32" fill="#a85917"/>',
              f'<text x="{24+w1/2}" y="{y+34}" text-anchor="middle" fill="white" font-size="15">{rel}</text>',
              f'<text x="{24+w1+w2/2}" y="{y+34}" text-anchor="middle" fill="white" font-size="15">{absolute}</text>',
              f'<text x="24" y="{y+66}" font-size="16">Total error = {total}</text>']
parts += ['<rect x="24" y="373" width="14" height="14" fill="#276e87"/>',
'<text x="47" y="385" font-size="15">Relative part: actual mass / 9</text>',
'<rect x="24" y="399" width="14" height="14" fill="#a85917"/>',
'<text x="47" y="411" font-size="15">Absolute part: 1/90 at each time</text>',
'<text x="24" y="443" font-size="18" font-weight="bold">Sum = 1/9 + 1/30 = 13/90</text>','</g></svg>']
(ROOT/'figures/mass-weighted-assembly.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Exact mass-weighted assembly diagram written.')

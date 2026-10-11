"""Draw the exact n=2,m=1,total=3 example; generated SVG uses no external fonts."""
from pathlib import Path
from fractions import Fraction as F

root=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="390" viewBox="0 0 1000 390" role="img" aria-labelledby="title desc">',
       '<title id="title">Uniform lifting preserves the total and coarse residue masses</title>',
       '<desc id="desc">At total three, the joint law puts mass one eighth at residues two and four modulo nine. Lifting from modulo three puts mass one twenty-fourth at residues one, two, four, five, seven and eight. Both panels have total mass one quarter.</desc>',
       '<rect width="1000" height="390" fill="white"/>',
       '<g font-family="sans-serif" fill="#172033">']
original={2:F(1,8),4:F(1,8)}
lifted={y:F(1,24) for y in (1,2,4,5,7,8)}
for index,(data,title) in enumerate(((original,'Original joint masses at S₂ = 3'),(lifted,'Uniform lift from residues modulo 3'))):
    x0=70+500*index
    parts.append(f'<text x="{x0+190}" y="35" font-size="20" text-anchor="middle">{title}</text>')
    for level in (F(0),F(1,24),F(1,12),F(1,8)):
        y=295-float(level)*1600
        parts.extend([f'<line x1="{x0-5}" x2="{x0+360}" y1="{y}" y2="{y}" stroke="#d9e1eb"/>',
                      f'<text x="{x0-12}" y="{y+5}" font-size="14" text-anchor="end">{level}</text>'])
    for residue in range(9):
        x=x0+residue*41
        mass=data.get(residue,F(0))
        height=float(mass)*1600
        color={0:'#94a3b8',1:'#1d4ed8',2:'#b45309'}[residue%3]
        if mass:
            parts.append(f'<rect x="{x-11}" y="{295-height}" width="22" height="{height}" fill="{color}"/>')
            parts.append(f'<text x="{x}" y="{285-height}" font-size="14" text-anchor="middle">{mass}</text>')
        parts.append(f'<text x="{x}" y="318" font-size="15" text-anchor="middle">{residue}</text>')
    parts.append(f'<text x="{x0+170}" y="344" font-size="16" text-anchor="middle">Offset residue modulo 9</text>')
parts.extend(['<text x="500" y="378" font-size="16" text-anchor="middle">Blue: residue 1 modulo 3 · Ochre: residue 2 modulo 3 · Total mass in each panel: 1/4</text>', '</g></svg>'])
(root/'figures/joint-total-mixing.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

"""Draw the exact 9 -> 7 inverse example with rational interval coordinates."""
from fractions import Fraction as Q
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
left, right = Q(35,4), Q(49,4)
def x(v):
    return float(150+560*(v-left)/(right-left))

pieces = ['''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="530" viewBox="0 0 840 530" role="img" aria-labelledby="title desc">
<title id="title">Changing a weight and changing the support</title>
<desc id="desc">The true source is 9 and the offset-free comparison point is 28/3. The three exact bands are [9,10), [37/4,12), and [9,28/3). Their selectors respectively include both points, only the comparison point, and only the actual source. Each band contains a positive odd integer.</desc>
<rect width="840" height="530" fill="#faf9f6"/>
<g font-family="Georgia,serif" fill="#172b3a">
<text x="30" y="36" font-size="24">One return: (3 × 9 + 1) / 4 = 7</text>
<text x="30" y="66" font-size="18">Actual N = 9; comparison N⁰ = 28/3; relative defect α = 1/28.</text>
''']
rows = [
    (135,Q(9),Q(10),'[9, 10)','Both included: only the reciprocal weight changes.',True,True),
    (265,Q(37,4),Q(12),'[37/4, 12)','Comparison only: the source lies below the lower boundary.',False,True),
    (395,Q(9),Q(28,3),'[9, 28/3)','Actual only: the comparison point is at the excluded upper end.',True,False)]
for y,l,u,label,meaning,actual,nominal in rows:
    pieces.append(f'<text x="30" y="{y-35}" font-size="20">{escape(label)}</text>')
    pieces.append(f'<line x1="150" x2="710" y1="{y}" y2="{y}" stroke="#93a0aa" stroke-width="2"/>')
    pieces.append(f'<line x1="{x(l)}" x2="{x(u)}" y1="{y}" y2="{y}" stroke="#b9d7df" stroke-width="16"/>')
    pieces.append(f'<circle cx="{x(l)}" cy="{y}" r="7" fill="#38768a"/>')
    pieces.append(f'<circle cx="{x(u)}" cy="{y}" r="7" fill="#faf9f6" stroke="#38768a" stroke-width="3"/>')
    # The band endpoints are shown on the axis; points sit above it to avoid overlap.
    for val,text,colour,included in [(Q(9),'N = 9','#254e70',actual),(Q(28,3),'N⁰ = 28/3','#9b4a24',nominal)]:
        pieces.append(f'<line x1="{x(val)}" x2="{x(val)}" y1="{y-17}" y2="{y+13}" stroke="{colour}" stroke-width="2"/>')
        pieces.append(f'<circle cx="{x(val)}" cy="{y-17}" r="5" fill="{colour if included else "#faf9f6"}" stroke="{colour}" stroke-width="2"/>')
        anchor, dx = ('end',-8) if val == 9 else ('start',8)
        pieces.append(f'<text x="{x(val)+dx}" y="{y+36}" text-anchor="{anchor}" font-size="17" fill="{colour}">{text}</text>')
    pieces.append(f'<text x="30" y="{y+69}" font-size="18">{escape(meaning)}</text>')
pieces.append('<text x="30" y="511" font-size="16">Filled band endpoint: included. Open band endpoint: excluded. Points use the same convention.</text></g></svg>')
(ROOT/'figures/affine-support.svg').write_text('\n'.join(pieces)+'\n',encoding='utf-8')

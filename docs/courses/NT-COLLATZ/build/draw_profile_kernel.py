"""Generate the exact horizontal-layer diagram for w=(1,2,3,2,1)/9."""
from pathlib import Path
from fractions import Fraction
import html
ROOT=Path(__file__).resolve().parents[1]
w=[1,2,3,2,1]
assert sum(w)==9 and max(w)==3
assert [sum(x>k for x in w) for k in range(3)]==[5,3,1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="title desc">',
'<title id="title">The mass of a unimodal sequence as horizontal interval layers</title>',
'<desc id="desc">Weights one, two, three, two, one divided by nine. Each of the three horizontal layers has height one ninth and respective lengths five, three, one. Their total mass is one and their maximum height is one third.</desc>',
'<rect width="760" height="360" fill="#fff"/>',
'<g font-family="Arial, sans-serif" fill="#17324d" font-size="18">']
def text(x,y,s,size=18,anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}">{html.escape(s)}</text>')
text(30,35,'A profile is a stack of interval layers',23)
x0,dx,base,dy=90,65,282,60
colors=['#c6def1','#8db7db','#4d83b3']
for lev in range(3):
    active=[i for i,v in enumerate(w) if v>lev]
    x=x0+min(active)*dx
    y=base-(lev+1)*dy
    parts.append(f'<rect x="{x}" y="{y}" width="{len(active)*dx}" height="{dy}" fill="{colors[lev]}" stroke="#fff" stroke-width="2"/>')
for i,v in enumerate(w):
    x=x0+i*dx
    parts.append(f'<path d="M {x} {base} v {-dy*v} h {dx} v {dy*v}" fill="none" stroke="#17324d" stroke-width="1.5"/>')
    text(x+dx/2,base+25,str(i+1),18,'middle')
    text(x+dx/2,base-v*dy-10,f'{v}/9',17,'middle')
parts.append(f'<path d="M 77 75 V {base} H 430" stroke="#17324d" fill="none"/>')
text(27,90,'w(n)',19)
for lev in range(4):
    text(69,base-lev*dy+6,str(Fraction(lev,9)),16,'end')
text(422,base+25,'n',19)
text(478,110,'0 ≤ t < 1/9: length 5')
text(478,150,'1/9 ≤ t < 2/9: length 3')
text(478,190,'2/9 ≤ t < 1/3: length 1')
text(478,243,'Mass = (5 + 3 + 1)/9 = 1')
text(478,279,'Maximum = 3/9 = 1/3')
text(30,337,'Strict superlevel sets {n : w(n) > t}; endpoint heights do not affect the integrals.',16)
parts.append('</g></svg>')
(ROOT/'figures/profile-levels.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Generated exact profile-levels.svg')


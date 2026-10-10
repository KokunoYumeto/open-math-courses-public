"""Reproduce the exact sections and output intervals of Exercises 1 and 3."""
from pathlib import Path
from html import escape
r=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590">',
 '<rect width="1040" height="590" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#183044;font-size:19px}.small{font-size:16px}.title{font-size:23px;font-weight:600}</style>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#536c80"/></marker></defs>']
def text(x,y,t,cls='',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(t)}</text>')
def line(x1,y1,x2,y2,color='#536c80',width=2,arrow=False):
 extra=' marker-end="url(#arrow)"' if arrow else ''
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>')
def rect(x,y,w,h,fill):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
zx=lambda z:388+120*z
text(34,36,'Two patches need no common base-frequency rectangle','title')
text(35,66,'Section ζ = 0, |η| = 1; the normal base coordinate is fixed.','small')
line(67,185,728,185,arrow=True);text(742,191,'z')
line(388,272,388,83,arrow=True);text(399,97,'η')
for sign,y in [(1,126),(-1,244)]:
 text(374,y+6,'+1' if sign==1 else '−1','small','end')
 for base in [-1.5,1.5]:
  if (sign==1 and base<0) or (sign==-1 and base>0):
   rect(zx(base-.5),y-14,120,28,'#cfeadd')
   parts.append(f'<circle cx="{zx(base)}" cy="{y}" r="5" fill="#17694d"/>')
   for endpoint in [base-.5,base+.5]:parts.append(f'<circle cx="{zx(endpoint)}" cy="{y}" r="5" fill="white" stroke="#17694d" stroke-width="2"/>')
  else:
   xx=zx(base);line(xx-7,y-7,xx+7,y+7,'#ad3556',3);line(xx-7,y+7,xx+7,y-7,'#ad3556',3)
for z in [-2,-1,0,1,2]:
 line(zx(z),180,zx(z),190);text(zx(z),210,str(z),'small','middle')
text(794,118,'Green: open intervals','small');text(794,145,'Red crosses: excluded','small')
text(794,194,'A rectangle containing','small');text(794,220,'both green points also','small');text(794,246,'contains both crosses.','small')
text(35,323,'One scalar test has two disjoint output channels','title')
zx2=lambda z:100+110*(z+2)
line(62,424,963,424,arrow=True);text(975,431,'z')
rect(zx2(-2),367,zx2(2)-zx2(-2),37,'#dbeaf8')
rect(zx2(4),367,zx2(5)-zx2(4),37,'#ecdff4')
text((zx2(-2)+zx2(2))/2,392,'Qf: output in [−2, 2]','','middle')
text((zx2(4)+zx2(5))/2,392,'USf','','middle')
for z in [-2,0,2,4,5]:
 line(zx2(z),419,zx2(z),429);text(zx2(z),451,str(z),'small','middle')
text((zx2(2)+zx2(4))/2,394,'gap = 2','small','middle')
text(34,498,'U: [−3, 3] → [4, 5],   z = 9/2 + Z/6,   amplitude = √6')
text(34,532,'A = Q + US;     ‖Af‖² = ‖Qf‖² + ‖Sf‖²')
text(34,565,'Only the residual output moves. Normal and input coordinates stay unchanged.','small')
parts.append('</svg>')
(r/'boundary-chart-scalar-assembly.svg').write_text('\n'.join(parts)+'\n','utf-8')
print('Wrote exact crossed-patch section and disjoint output intervals.')

"""Exact vector coordinate diagrams; no raster or source-book images."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 460" role="img" aria-labelledby="title desc">',
'<title id="title">A folded Lagrangian and two characteristic exchanges</title>',
'<desc id="desc">Left: r=t squared and xi=t, with the two covector branches over r positive. Right: coordinates y,p on q=0,rho=p squared, and the two distinct exchange endpoints from y=-one half,p=one half.</desc>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#53677b"/></marker></defs>',
'<rect width="1100" height="460" fill="#fff"/>']
def line(x1,y1,x2,y2,color='#53677b',width=1.5,arrow=False,dash=False):
 out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="6 4"' if dash else '')+'/>')
def text(x,y,s,size=17,color='#142b42',anchor='start'):
 out.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')
def path(points,color):
 out.append('<path d="'+' '.join(('M' if i==0 else 'L')+f' {x:.4f} {y:.4f}' for i,(x,y) in enumerate(points))+f'" fill="none" stroke="{color}" stroke-width="3"/>')
def point(x,y,color='#b34b2d'):
 out.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>')
text(45,34,'Folding Lagrangian: r=t², ξ=t',22)
text(595,34,'Glancing intersection: q=0, ρ=p²',22)
out.append('<rect x="65" y="64" width="84" height="344" fill="#e6edf3"/>')
line(65,228,505,228,arrow=True);line(150,410,150,62,arrow=True)
text(510,233,'r');text(131,66,'ξ')
text(77,395,'r<0',15);text(224,395,'attained side r≥0',16)
for lo,hi,col in [(0,1.05,'#136e8a'),(-1.05,0,'#a24f26')]:
 pts=[]
 for i in range(101):
  t=lo+(hi-lo)*i/100;pts.append((150+285*t*t,228-143*t))
 path(pts,col)
for t in [-.75,.75]:point(150+285*t*t,228-143*t)
line(150+285*.75**2,228-143*.75,150+285*.75**2,228+143*.75,dash=True)
text(315,103,'ξ=+√r',17,'#136e8a');text(315,310,'ξ=−√r',17,'#a24f26')
text(64,438,'Potentials: ±(2/3)r^(3/2); spectators fixed',16)
# Right panel: the arrows denote endpoint identifications, never orbits.
def coord(y,p):return 814+220*y,225-190*p
line(*coord(-.93,0),*coord(1.0,0),arrow=True)
line(*coord(0,-.87),*coord(0,.86),arrow=True)
text(1044,232,'y');text(795,63,'p')
A=coord(-.5,.5);B=coord(-.5,-.5);C=coord(.5,-.5)
line(*A,*B,color='#136e8a',width=2,arrow=True)
line(*A,*C,color='#a24f26',width=2,arrow=True)
for P in [A,B,C]:point(*P)
text(641,110,'(−1/2, 1/2)',16)
text(591,348,'i_F: (−1/2, −1/2)',16,'#136e8a')
text(884,348,'i_G: (1/2, −1/2)',16,'#a24f26')
text(631,188,'i_F',17,'#136e8a')
text(867,189,'i_G',17,'#a24f26')
text(604,387,'i_F(y,p)=(y,−p)',17)
text(604,413,'i_G(y,p)=(y+2p,−p)',17)
text(604,438,'Arrows join exchange endpoints; ρ=1/4 here',16)
out.append('</svg>')
(ROOT/'folded-lagrangian-and-glancing-exchanges.svg').write_text('\n'.join(out)+'\n','utf-8')
print({'panels':2,'exact_marked_points':5,'raster_inputs':0})

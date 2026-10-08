"""Draw the proved index sequence, redundant scalar data and fixed support collar."""
from pathlib import Path
from html import escape
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="500" viewBox="0 0 1120 500" role="img" aria-labelledby="title desc">',
 '<title id="title">Two regularity gains on a fixed collar</title>',
 '<desc id="desc">Six diagonal steps preserve s+t and reach s=5/2. Seven horizontal steps at t=-6 reach s=19/2. The scalar redundant boundary map is reduced by retaining its first output coordinate. All finite cutoff families fit between the same outer and inner normal collars.</desc>',
 '<rect width="1120" height="500" fill="white"/><style>text{font-family:Arial,sans-serif;font-size:17px;fill:#182a3b}.title{font-size:21px;font-weight:bold}.small{font-size:15px}</style>',
 '<defs><marker id="blue" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#2364b1"/></marker><marker id="green" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#087c65"/></marker></defs>']
def txt(x,y,t,c=''):out.append(f'<text x="{x}" y="{y}" class="{c}">'+escape(t)+'</text>')
def line(x,y,xx,yy,col='#d7e0e5',w=1,arrow=None):out.append(f'<path d="M{x:.2f} {y:.2f} L{xx:.2f} {yy:.2f}" fill="none" stroke="{col}" stroke-width="{w}"'+(f' marker-end="url(#{arrow})"' if arrow else '')+'/>')
txt(30,34,'The two gains (EW16, EW19)','title');txt(30,63,'m = 2; the exact sequence in Exercise 4')
x=lambda s:65+(s+4)*33;y=lambda t:110-t*40
for ss in [-4,-2,0,2,4,6,8,10]:
 line(x(ss),100,x(ss),375);txt(x(ss)-8,397,str(ss),'small')
for tt in [0,-2,-4,-6]:
 line(65,y(tt),527,y(tt));txt(31,y(tt)+5,str(tt),'small')
txt(540,397,'s');txt(34,93,'t')
pts=[(-3.5+j,-j) for j in range(7)]+[(2.5+j,-6) for j in range(1,8)]
for j,(p,q) in enumerate(zip(pts,pts[1:])):
 line(x(p[0]),y(p[1]),x(q[0])-3,y(q[1]),'#2364b1' if j<6 else '#087c65',2,'blue' if j<6 else 'green')
for p in pts:out.append(f'<circle cx="{x(p[0]):.2f}" cy="{y(p[1]):.2f}" r="3.2" fill="#182a3b"/>')
txt(83,94,'(−7/2, 0)','small');txt(245,329,'(5/2, −6)','small');txt(448,329,'(19/2, −6)','small')
txt(33,439,'Blue: (s,t) → (s+1,t−1), six steps.')
txt(33,470,'Green: (s,t) → (s+1,t), seven steps.')
line(580,20,580,480,'#c8d5dc')
txt(605,34,'The boundary map and the fixed collar','title')
out.append('<rect x="602" y="77" width="485" height="126" rx="8" fill="#f2f6f8" stroke="#b8ccd5"/>')
txt(621,106,'Stable scalar solution: v(r) = c exp(−ar)')
txt(621,140,'Original data: c ↦ (c, ia c), rank one')
txt(621,177,'Retained first coordinate: c ↦ c, invertible')
txt(610,242,'The normal coordinate and final collar stay fixed.')
line(642,292,1054,292,'#b8cad6',13)
line(642,332,891,332,'#548bae',13)
line(642,372,758,372,'#087c65',13)
line(642,265,642,402,'#586e7b',2)
txt(624,427,'0');txt(1042,319,'δ');txt(1071,292,'r')
txt(682,280,'Common input collar','small')
txt(909,338,'Intermediate cutoffs','small')
txt(776,378,'Fixed inner collar','small')
txt(610,460,'More steps insert more cutoffs between these bounds.','small')
out.append('</svg>')
(Path(__file__).parent/'elliptic-boundary-wavefront.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')

"""Draw exact base projections and interval lengths using native SVG primitives."""
from pathlib import Path
from html import escape
W,H=1040,810
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Changing-speed interior rays and the observed interval</title>',
 '<desc>Exact rays x=4-c z for c from 0.9 to 1.1 and 0 to 2 in z, with constant covectors rho=-1, eta=-c. The lowest endpoint is x=1.8 above the boundary. The observed interval has length one half within an interval of length two.</desc>',
 '<rect width="1040" height="810" fill="#ffffff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#173044}.title{font-size:26px;font-weight:700}.label{font-size:20px}.small{font-size:18px}.ray{fill:none;stroke-width:3}.axis{stroke:#506575;stroke-width:1.6}</style>']
def text(x,y,value,cls='label',anchor='start',fill=None):
 extra=f' fill="{fill}"' if fill else ''
 svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{extra}>{escape(value)}</text>')
def line(x1,y1,x2,y2,color='#506575',width=2,dash=None):
 extra=f' stroke-dasharray="{dash}"' if dash else ''
 svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>')
def point(x,y,color):svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')
def X(z):return 105+330*z
def Y(x):return 450-76*x
text(40,42,'Interior rays with changing speed','title')
text(40,75,'x = 4 − c z,   9/10 ≤ c ≤ 11/10;   (ρ, η) = (−1, −c)','label')
svg.append(f'<rect x="{X(0)}" y="110" width="{X(.5)-X(0)}" height="340" fill="#eee8f7"/>')
coords=[(X(0),Y(4)),(X(2),Y(2.2)),(X(2),Y(1.8))]
svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in coords)+'" fill="#cce8e7"/>')
line(X(0),Y(0),X(2.15),Y(0));line(X(0),Y(0),X(0),Y(4.4))
for x in [0,1,2,3,4]:
 line(X(0)-5,Y(x),X(0),Y(x));text(X(0)-16,Y(x)+6,str(x),'small','end')
for z,label in [(0,'0'),(.5,'1/2'),(1,'1'),(1.5,'3/2'),(2,'2')]:
 line(X(z),Y(0),X(z),Y(0)+6);text(X(z),Y(0)+28,label,'small','middle')
text(X(2.15)+12,Y(0)+6,'z');text(X(0)-26,Y(4.4)-10,'x')
for c,color,label in [(.9,'#246c82','c = 9/10'),(1,'#164653','c = 1'),(1.1,'#ad5a35','c = 11/10')]:
 line(X(0),Y(4),X(2),Y(4-2*c),color,3)
 point(X(2),Y(4-2*c),color)
 endy=Y(4-2*c)
 targety={.9:244,1:277,1.1:310}[c]
 line(X(2)+6,endy,820,targety-6,color,1.4)
 text(832,targety,label,'small')
point(X(0),Y(4),'#173044')
text(150,130,'observed strip','small')
line(X(2),Y(1.8),X(2),Y(0),'#ad5a35',1.7,'5 5')
text(790,393,'x ≥ 9/5 > 0','label')
text(400,437,'physical boundary x = 0','small')
text(105,514,'The shaded band is a base projection; its full covectors are specified above.','small')
line(40,540,1000,540,'#cad6df',1)
text(40,580,'Observation by an interval average','title')
line(X(0),631,X(2),631,'#246c82',7)
line(X(0),631,X(.5),631,'#7a53a2',10)
for z,label in [(0,'0'),(.5,'1/2'),(2,'2')]:
 line(X(z),618,X(z),644,'#173044',1.5);text(X(z),671,label,'small','middle')
text(300,620,'I = [0, 2],  length 2','label')
text(105,707,'J = [0, 1/2],  length 1/2','label')
text(105,747,'‖v‖ on I  ≤  2 ‖v‖ on J  +  2 ‖Dₜv‖ on I','label')
text(105,782,'The first coefficient is sharp for constant v; no derivative sharpness is claimed.','small')
svg.append('</svg>')
p=Path(__file__).resolve().parent/'uniform-interior-observation.svg'
p.write_text('\n'.join(svg)+'\n',encoding='utf-8')
print(p)

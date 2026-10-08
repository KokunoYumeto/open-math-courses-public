"""Two labelled exact model sections; sampled curves are explicitly identified."""
from pathlib import Path
import math

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="610" viewBox="0 0 1120 610">',
         '<rect width="1120" height="610" fill="white"/>',
         '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#555"/></marker></defs>']

def text(x, y, value, size=14, color='#17324d', anchor='start', weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{value}</text>')

def line(x1, y1, x2, y2, color='#ced9e5', width=1, extra=''):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>')

def dot(x,y,color='#196eaa'):
    parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')

text(60,35,'Projection of Laplace jets',23,weight='bold')
text(635,35,'A stable solution with a repeated root',23,weight='bold')
text(60,66,'|η| = 1; exact real section (Re x₀, Im x₁)')
text(635,66,'η = 1, initial value e₂; t ∈ [0, 3]')
x=lambda a: 250+95*a
y=lambda b: 260-95*b
for a in [-1,0,1,2]:
    line(x(a),90,x(a),430)
    text(x(a),451,str(a),anchor='middle')
for b in [-1,0,1]:
    line(110,y(b),487,y(b))
    text(98,y(b)+5,str(b),anchor='end')
line(x(-1.35),y(0),x(2.5),y(0),'#8095aa')
line(x(0),y(-1.75),x(0),y(1.75),'#8095aa')
line(x(-1.3),y(-1.3),x(1.65),y(1.65),'#196eaa',2.5)
line(x(-1.3),y(1.3),x(1.65),y(-1.65),'#bc5700',2.5)
line(x(2),y(0),x(1),y(1),'#555',2,'marker-end="url(#arrow)"')
line(x(0),y(0),x(1),y(-1),'#bc5700',2,'stroke-dasharray="5 4"')
for a,b,c in [(2,0,'#555'),(1,1,'#196eaa'),(1,-1,'#bc5700')]:dot(x(a),y(b),c)
text(x(2)+8,y(0)-12,'x = (2, 0)')
text(x(1)+10,y(1)+8,'qx = (1, 1)',color='#196eaa')
text(x(1)+10,y(-1)+6,'x − qx = (1, −1)',color='#bc5700')
text(240,478,'Re x₀')
text(85,87,'Im x₁')
text(60,514,'Blue: stable line C(1, i); orange: unstable line C(1, −i).',13)
text(60,539,'Arrow: projection along the unstable line, not time evolution.',13)

xx=lambda a: 665+130*a
yy=lambda b: 380-255*b
for a in [0,1,2,3]:
    line(xx(a),99,xx(a),438)
    text(xx(a),459,str(a),anchor='middle')
for b in [-0.2,0,0.5,1]:
    line(665,yy(b),1055,yy(b))
    text(650,yy(b)+5,str(b),anchor='end')
line(665,yy(0),1055,yy(0),'#8095aa')
for fun,col in [(lambda a:-a*math.exp(-2*a),'#bc5700'),(lambda a:math.exp(-2*a),'#196eaa')]:
    points=[(xx(3*k/300),yy(fun(3*k/300))) for k in range(301)]
    path='M'+' L'.join(f'{a:.3f},{b:.3f}' for a,b in points)
    parts.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="2.5"/>')
text(858,486,'normal time t')
text(635,514,'Blue: u₂(t) = exp(−2t).',13,color='#196eaa')
text(635,539,'Orange: u₁(t) = −t exp(−2t), the nilpotent term.',13,color='#bc5700')
text(560,581,'NP7–NP9 and Examples 1–2. Left: exact section. Right: sampled exact formulas.',14,anchor='middle')
parts.append('</svg>')
Path(__file__).with_name('stable-normal-projection.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

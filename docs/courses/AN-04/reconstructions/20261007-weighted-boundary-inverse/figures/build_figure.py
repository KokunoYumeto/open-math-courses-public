"""Exact oblique projection and samples of the two surviving error multipliers."""
from pathlib import Path
import math
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="610" viewBox="0 0 1120 610">','<rect width="1120" height="610" fill="white"/>','<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#555"/></marker></defs>']
def text(x,y,s,size=14,color='#17324d',anchor='start',weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
def line(x1,y1,x2,y2,color='#d7e0e7',width=1,extra=''):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>')
def curve(fun,xx,yy,color):
    pts=[(xx(1+19*k/400),yy(fun(1+19*k/400))) for k in range(401)]
    d='M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in pts)
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"/>')
text(60,35,'Both retained errors have order minus one',22,weight='bold')
text(635,35,'Projection supplies the stable inverse',22,weight='bold')
text(60,67,'ε(x) = 1 / (2√(1 + x²)); integer samples are circle modes')
text(635,67,'Exact real plane section of the matrices in Example 2')
xx=lambda x:90+(x-1)*21.3
yy=lambda y:420-820*y
for x in [1,5,10,15,20]:
    line(xx(x),95,xx(x),420);text(xx(x),444,str(x),anchor='middle')
for y in [0,.1,.2,.3,.4]:
    line(90,yy(y),495,yy(y));text(78,yy(y)+5,str(y),anchor='end')
eps=lambda x:1/(2*math.sqrt(1+x*x))
curve(eps,xx,yy,'#196eaa');curve(lambda x:eps(x)/(1+eps(x)),xx,yy,'#bc5700')
text(290,475,'frequency magnitude x',anchor='middle')
text(60,512,'Blue: ε(x). Orange: ε(x)/(1 + ε(x)).',13)
text(60,539,'Both satisfy x × error → 1/2; neither is smoothing.',13)
xx=lambda x:780+150*x
yy=lambda y:275-175*y
for x in [-.5,0,.5,1,1.5]:
    line(xx(x),100,xx(x),423);text(xx(x),446,str(x),anchor='middle')
for y in [-.5,0,.5,1]:
    line(682,yy(y),1045,yy(y));text(672,yy(y)+5,str(y),anchor='end')
line(xx(-.65),yy(0),xx(1.75),yy(0),'#196eaa',2.5)
line(xx(-.65),yy(-.325),xx(1.7),yy(.85),'#bc5700',2.5)
line(xx(.2),yy(-.4),xx(1),yy(0),'#555',2,'marker-end="url(#arrow)"')
for x,y in [(.2,-.4),(1,0)]:parts.append(f'<circle cx="{xx(x)}" cy="{yy(y)}" r="4" fill="#555"/>')
text(xx(.2)-35,yy(-.4)+28,'t = (1/5, −2/5)',13)
text(xx(1)-13,yy(0)-18,'s = qt = (1, 0)',13)
text(882,475,'first coordinate',anchor='middle')
text(635,512,'Blue: ran q = R(1, 0). Orange: ker q = R(2, 1).',13)
text(635,539,'The arrow is parallel to ker q; bqt = 1, but bt = −1.',13)
text(560,581,'WB24–WB27. Left: sampled exact functions. Right: exact vectors and subspaces.',14,anchor='middle')
parts.append('</svg>')
Path(__file__).with_name('weighted-boundary-inverse.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

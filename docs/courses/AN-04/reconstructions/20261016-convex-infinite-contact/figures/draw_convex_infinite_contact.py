"""Draw exact polygon data and numerical samples of its smooth interpolation."""
from pathlib import Path
import math
OUT=Path(__file__).with_name('convex-infinite-contact.svg')
a=1/32
N=2048
u=[-a+2*a*i/N for i in range(N+1)]
bump=[math.exp(-1/(1-(v/a)**2)) if abs(v)<a else 0 for v in u]
mass=[0.]
for i in range(N):mass.append(mass[-1]+(u[i+1]-u[i])*(bump[i]+bump[i+1])/2)
mass=[v/mass[-1] for v in mass]
ints=[0.]
for i in range(N):ints.append(ints[-1]+(u[i+1]-u[i])*(mass[i]+mass[i+1])/2)
def L(v):
    if v<=-a:return 0.
    if v>=a:return v # even bump has zero first moment
    t=(v+a)/(2*a)*N;i=min(int(t),N-1);s=t-i;h=2*a/N
    return ints[i]+h*(mass[i]*s+(mass[i+1]-mass[i])*s*s/2)
def data(j):
    m=2.**-j
    b=math.tan((math.atan(2*m)+math.atan(m))/2)
    c=math.tan((math.atan(m)+math.atan(m/2))/2)
    return m,b,c,(m-c)/(b-c)
def y(j):return sum(2.**-k/(k*(k+1)) for k in range(j,160))
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="450" viewBox="0 0 1100 450"><rect width="1100" height="450" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#193248;font-size:16px}.head{font-weight:bold;font-size:18px}.note{font-size:14px}.axis{stroke:#8094a3;stroke-width:1}.curve{fill:none;stroke:#148080;stroke-width:3}.chord{fill:none;stroke:#4857b4;stroke-width:2}</style>']
def text(x,y,t,cls=''):svg.append(f'<text x="{x}" y="{y}" class="{cls}">{t}</text>')
def line(x1,y1,x2,y2,style):svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {style}/>')
def poly(points,cls):svg.append('<polyline class="'+cls+'" points="'+' '.join(f'{x:.4f},{y:.4f}' for x,y in points)+'"/>')
text(28,30,'One smooth convex obstacle; exact reflected chords','head')
text(28,65,'Actual boundary and chords (j ≥ 2)','head')
text(28,88,'x unchanged; vertical scale: 20y','note')
X=lambda x:55+560*x
Y=lambda v:310-160*20*v
line(45,310,350,310,'class="axis"');line(55,315,55,110,'class="axis"')
pts=[(X(0),Y(0))]
for j in range(60,1,-1):
    d=1/(j*(j+1));m,b,c,theta=data(j)
    for i in range(41):
        s=i/40;x=1/(j+1)+d*s
        f=y(j+1)+d*(c*s+(b-c)*L(s-(1-theta)))
        pts.append((X(x),Y(f)))
poly(pts,'curve')
poly([(X(0),Y(0))]+[(X(1/j),Y(y(j))) for j in range(60,1,-1)],'chord')
for j in [2,3,4,6]:
    x1,y1=X(1/j),Y(y(j))
    svg.append(f'<circle cx="{x1}" cy="{y1}" r="3" fill="#4857b4"/>')
    text(x1+4,y1-10,f'P{j}','note')
text(55,334,'0');text(319,334,'x');text(28,116,'20y','note')
text(28,368,'Every open chord lies above f.','note')
text(28,390,'Vertices accumulate at the flat origin.','note')
text(390,65,'One interval, with its tangent removed','head')
text(390,88,'j = 5; S = (x − x₆)/d₅','note')
m,b,c,theta=data(5);xx=lambda s:415+255*s;yy=lambda v:310-205*v
line(410,310,690,310,'class="axis"');line(415,315,415,120,'class="axis"')
poly([(xx(i/200),yy(L(i/200-(1-theta)))) for i in range(201)],'curve')
poly([(xx(0),yy(0)),(xx(1),yy(theta))],'chord')
text(460,195,'chord: θ₅ S','note');text(470,290,'graph: L(S − c₅)','note')
text(415,334,'0');text(665,334,'1');text(690,334,'S')
text(390,368,'Y = [f − y₆ − b₆(x − x₆)]','note')
text(419,390,'/ [d₅(b₅ − b₆)]','note')
text(760,65,'Exact equal-angle reflection at P₂','head')
text(760,88,'Orthonormal tangent frame','note')
ox,oy=905,225
line(765,oy,1070,oy,'stroke="#8094a3" stroke-width="2"')
delta=(math.atan(.5)-math.atan(.25))/2
dx,dy=135*math.cos(delta),135*math.sin(delta)
line(ox-dx,oy-dy,ox,oy,'stroke="#4857b4" stroke-width="3"')
line(ox,oy,ox+dx,oy-dy,'stroke="#4857b4" stroke-width="3"')
svg.append(f'<circle cx="{ox}" cy="{oy}" r="4" fill="#193248"/>')
text(778,180,'incoming −δ₂','note');text(953,180,'outgoing +δ₂','note')
text(790,259,'tangent (angle β₂)','note')
text(760,307,'δ₂ = (arctan ½ − arctan ¼)/2','note')
text(760,329,f'δ₂ ≈ {delta*180/math.pi:.3f}°; directions have unit norm','note')
text(760,368,'The picture shows spatial geometry.','note')
text(760,390,'The text gives time and all covectors.','note')
text(28,432,'Teal: smooth boundary. Indigo: straight chords. Fixed-profile integrals are sampled numerically for drawing only.','note')
svg.append('</svg>')
OUT.write_text('\n'.join(svg)+'\n','utf-8')
print(OUT.name)

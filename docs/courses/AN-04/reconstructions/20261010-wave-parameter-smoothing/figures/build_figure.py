"""Reproducible coordinate plots for WS19, WS27 and the common support bound."""
from pathlib import Path
from math import sqrt
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="620" viewBox="0 0 1040 620">',
       '<rect width="1040" height="620" fill="#fff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#183347} .small{font-size:15px} .label{font-size:17px} .title{font-size:21px;font-weight:bold}</style>']
def text(x,y,value,cls='small',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def line(x1,y1,x2,y2,color='#d9e1e5',width=1,dash=''):
    extra=f' stroke-dasharray="{dash}"' if dash else ''
    parts.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"{extra}/>')
def dot(x,y,color='#156a83'):
    parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="4.5" fill="{color}"/>')
def panel(left,right,vmax,title,ylabel):
    top,bottom=100,448
    def xy(t,v): return (left+(t+1.3)/3.5*(right-left),bottom-v/vmax*(bottom-top))
    for tt in [-1,0,1,2]:
        x,_=xy(tt,0);line(x,top,x,bottom);text(x,bottom+25,str(tt),anchor='middle')
    for vv in [i/2 for i in range(int(vmax*2)+1)]:
        _,y=xy(0,vv);line(left,y,right,y);text(left-9,y+5,str(vv).removesuffix('.0'),anchor='end')
    line(left,top,left,bottom,'#183347',1.5);line(left,bottom,right,bottom,'#183347',1.5)
    text(left,60,title,'title');text(left,84,ylabel,'label');text(right,bottom+25,'t','label')
    return xy
def curve(xy,fun,color,width=3,dash='',start=-1.2,end=2.1):
    points=[xy(start+(end-start)*i/500,fun(start+(end-start)*i/500)) for i in range(501)]
    data='M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in points)
    extra=f' stroke-dasharray="{dash}"' if dash else ''
    parts.append(f'<path d="{data}" fill="none" stroke="{color}" stroke-width="{width}"{extra}/>')
radius=lambda t:sqrt((.2+.6*(t-1.5))**2+(.1+.8*(t-1.5))**2)
normal=lambda t:abs(.2+.6*(t-1.5))
left=panel(64,492,3,'Spatial radius and the zero region','ρ = √(r² + y²)')
x1,y1=left(.99,.42);x2,y2=left(2.01,0)
parts.append(f'<rect x="{x1:.3f}" y="{y1:.3f}" width="{x2-x1:.3f}" height="{y2-y1:.3f}" fill="#d5ecf5" opacity=".9"/>')
text(x1+7,y1-7,'target M')
curve(left,lambda t:1.01*(.4+abs(t))+.01,'#c47a1a',2.5)
curve(left,lambda t:abs(t)+.5,'#646b79',2,'6 5')
curve(left,radius,'#156a83',3.5,end=1.5)
x,y=left(-1.1,radius(-1.1));dot(x,y);text(x+13,y-11,'ρ² = 577/100')
x,y=left(1.5,radius(1.5));dot(x,y)
line(72,494,108,494,'#156a83',3);text(118,500,'radius of the exact reflected ray')
line(72,524,108,524,'#c47a1a',3);text(118,530,'common support envelope')
line(72,554,108,554,'#646b79',2,'6 5');text(118,560,'observation boundary: ρ = |t| + 1/2')
right=panel(579,995,2,'Normal projection of the same ray','r ≥ 0; boundary r = 0')
curve(right,normal,'#156a83',3.5,end=1.5)
hx,hy=right(7/6,0);dot(hx,hy);line(hx,hy-8,hx+25,hy-143,'#156a83',1)
text(hx-110,hy-185,'reflection at t = 7/6')
text(hx-110,hy-160,'y = −1/6')
x,y=right(-1.1,normal(-1.1));dot(x,y);text(x+12,y-10,'r = 34/25')
text(586,500,'r(t) = |1/5 + 3(t − 3/2)/5|')
text(586,530,'Omitted coordinate: y(t) = 1/10 + 4(t − 3/2)/5')
text(586,560,'Target: t₀ = 3/2, (r₀, y₀) = (1/5, 1/10)')
text(64,600,'Exact formulas: WS14, WS19, WS21 and WS27. Curves are sampled coordinate plots; see V0 for their scope.')
parts.append('</svg>')
Path(__file__).with_name('wave-observation-and-reflection.svg').write_text('\n'.join(parts)+'\n','utf-8')
print('Wrote wave-observation-and-reflection.svg')

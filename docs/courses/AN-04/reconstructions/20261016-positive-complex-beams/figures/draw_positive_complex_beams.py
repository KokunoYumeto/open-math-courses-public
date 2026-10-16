"""Exact scientific coordinate plots, standard library, CC0-1.0."""
from pathlib import Path
import math,html
out=Path(__file__).with_name('positive-complex-beams.svg')
items=['<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="600" viewBox="0 0 1160 600" role="img" aria-labelledby="title desc">',
'<title id="title">Positive complex graphs through a focusing time</title>',
'<desc id="desc">Exact plots for b=one half: the complex Q ellipse, the Gaussian width coefficient from time zero to pi, and the leading boundary logarithm on a separate initial-plane slice.</desc>',
'<rect width="1160" height="600" fill="white"/>',
'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke"/></marker></defs>',
'<style>text{font-family:system-ui,sans-serif;font-size:15px;fill:#182d40}.head{font-size:18px;font-weight:650}.small{font-size:13px}</style>']
def txt(x,y,t,cl='',anchor='start'):
    items.append(f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{html.escape(t)}</text>')
def line(x,y,X,Y,color='#8195a4',dash='',arr=False):
    items.append(f'<line x1="{x:.3f}" y1="{y:.3f}" x2="{X:.3f}" y2="{Y:.3f}" stroke="{color}" stroke-width="1.8"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arr)"' if arr else '')+'/>')
def curve(points,color):
    items.append('<path d="M '+' L '.join(f'{x:.4f},{y:.4f}' for x,y in points)+f'" stroke="{color}" stroke-width="2.6" fill="none"/>')
for x in [385,775]:line(x,67,x,575,'#d8e2ea')
txt(25,34,'Positive complex beams: graph, width and boundary trace','head')
txt(25,76,'1. Complex graph block Q','head')
txt(405,76,'2. Gaussian width coefficient','head')
txt(795,76,'3. Leading boundary logarithm','head')
# Q-plane, exactly equal scale in real and imaginary coordinates.
cx,cy,scale=190,260,115
qp=lambda a,b:(cx+scale*a,cy-scale*b)
line(*qp(-1.28,0),*qp(1.35,0),arr=True);line(*qp(0,-.75),*qp(0,.95),arr=True)
curve([qp(math.cos(2*math.pi*j/600),.5*math.sin(2*math.pi*j/600)) for j in range(601)],'#156b88')
for a,b,label,dx,dy in [(1,0,'s=0',-15,25),(0,.5,'s=π/2',12,-12),(-1,0,'s=π',-10,25)]:
    x,y=qp(a,b);items.append(f'<circle cx="{x}" cy="{y}" r="3.6" fill="#ac402e"/>');txt(x+dx,y+dy,label,'small')
txt(318,286,'Re Q','small');txt(201,149,'Im Q','small')
txt(25,403,'Q=cos s + (i/2) sin s')
txt(25,437,'|Q|²=cos²s + (1/4)sin²s ≥ 1/4','small')
txt(25,471,'Q never reaches the origin.')
txt(25,514,'The real graph Qℝ=cos s fails','small')
txt(25,536,'at π/2; the complex graph does not.','small')
# Width on interval [0,pi].
ox,oy,w,h=435,342,300,185
width=lambda s:math.sqrt(2*math.cos(s)**2+.5*math.sin(s)**2)
wp=lambda s,v:(ox+w*s/math.pi,oy-h*v/1.6)
line(*wp(0,0),*wp(math.pi*1.05,0),arr=True);line(*wp(0,0),*wp(0,1.73),arr=True)
line(*wp(math.pi/2,0),*wp(math.pi/2,1.62),'#ac402e','5 4')
curve([wp(math.pi*j/500,width(math.pi*j/500)) for j in range(501)],'#236b4b')
for s,label in [(0,'0'),(math.pi/2,'π/2'),(math.pi,'π')]:
    x,y=wp(s,0);txt(x,y+23,label,'small','middle')
txt(739,371,'s','small');txt(441,130,'(Im M)⁻¹ᐟ²','small')
txt(405,403,'Width = λ⁻¹ᐟ²√(2cos²s + ½sin²s)','small')
txt(405,437,'Im M ∈ [1/2, 2]')
txt(405,471,'At π/2: width = 1/√(2λ)')
txt(405,514,'This plots a transverse quadratic jet,','small')
txt(405,536,'not the full nonlinear wave.','small')
# Leading log along v=0, 0.04<=w<=0.8, exact parameter bounds.
lx,ly,lw,lh=831,342,284,194
lp=lambda w,v:(lx+lw*w/.8,ly-lh*v/8)
line(*lp(0,0),*lp(.85,0),arr=True);line(*lp(0,0),*lp(0,8.5),arr=True)
curve([lp(.04+.76*j/500,-math.log((.04+.76*j/500)**2/2)) for j in range(501)],'#ac402e')
for w in [.2,.4,.6,.8]:
    x,y=lp(w,0);txt(x,y+24,f'{w:.1f}','small','middle')
for v in [2,4,6]:
    x,y=lp(0,v);txt(x-9,y+5,str(v),'small','end')
txt(1119,381,'w','small')
txt(795,403,'φ₀(v,w)=v + i(v²+w²)/2','small')
txt(795,437,'−log|φ₀(0,w)| = −log(w²/2)','small')
txt(795,471,'Trace / (2√R) has this leading part.','small')
txt(795,514,'The complete trace also has a bounded','small')
txt(795,536,'remainder, proved in the lesson.','small')
items.append('</svg>')
out.write_text('\n'.join(items)+'\n','utf-8')
print(out.name)

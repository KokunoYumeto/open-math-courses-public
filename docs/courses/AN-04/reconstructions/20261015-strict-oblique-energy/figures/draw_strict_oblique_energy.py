"""Original exact coordinate diagram; Python standard library only. CC0-1.0."""
from pathlib import Path
import math,html
out=Path(__file__).with_name('strict-oblique-energy.svg')
items=['<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="635" viewBox="0 0 1160 635" role="img" aria-labelledby="title desc">',
 '<title id="title">Strict complex oblique boundary energy</title>',
 '<desc id="desc">Three separate planes: physical normal and time with the outward future multiplier; a real slice of the positive complex derivative form; exact neutral and growing boundary-layer magnitudes at r=1 and k=1.</desc>',
 '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke"/></marker></defs>',
 '<rect width="1160" height="635" fill="#fff"/>',
 '<style>text{font-family:system-ui,sans-serif;font-size:15px;fill:#172c40}.head{font-size:19px;font-weight:650}.small{font-size:13px}.blue{fill:#136f8a}.red{fill:#ae3f28}.green{fill:#236847}</style>']
def line(x,y,X,Y,color='#668091',dash='',arrow=False):
    items.append(f'<line x1="{x:.4f}" y1="{y:.4f}" x2="{X:.4f}" y2="{Y:.4f}" stroke="{color}" stroke-width="2"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arr)"' if arrow else '')+'/>')
def txt(x,y,s,cl='',anchor='start'):
    items.append(f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{html.escape(s)}</text>')
def path(points,color,width=2.5):
    d='M '+' L '.join(f'{x:.4f},{y:.4f}' for x,y in points)
    items.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>')
for x in [385,775]:line(x,65,x,610,'#d9e2e9')
txt(25,36,'Strict complex oblique boundary energy','head')
txt(25,72,'1. Physical (r,t) plane','head')
txt(405,72,'2. Complex derivative slice','head')
txt(795,72,'3. Exact modes before cutoffs','head')
# One physical coordinate scale for all vectors and null directions.
ox,oy,scale=147,343,105
xy=lambda r,t:(ox+scale*r,oy-scale*t)
items.append('<rect x="147" y="140" width="207" height="255" fill="#eef6fa"/>')
line(*xy(-.85,0),*xy(1.8,0),arrow=True);line(*xy(0,-.42),*xy(0,1.8),arrow=True)
line(*xy(0,0),*xy(1.45,1.45),'#79909d','5 4')
line(*xy(0,0),*xy(-.85,.85),'#79909d','5 4')
line(*xy(0,0),*xy(1,0),'#236847',arrow=True)
line(*xy(0,0),*xy(0,1),'#136f8a',arrow=True)
line(*xy(0,0),*xy(-.25,1),'#ae3f28',arrow=True)
txt(336,368,'r');txt(156,157,'t')
txt(257,332,'N=(1,0)','green')
txt(159,226,'V=(0,1)','blue')
txt(26,211,'Z=(-1/4,1)','red')
txt(275,178,'r ≥ 0','small')
txt(267,207,'null','small')
txt(25,431,'g(Z,Z)=15/16 > 0')
txt(25,462,'Z has an outward normal component.')
txt(25,501,'Boundary form on (u_y,u_t):')
txt(25,529,'K = [ 3/16    -i/8 ]')
txt(25,553,'      [  i/8      3/2 ]')
txt(25,585,'On B₀u=0: flux ≥ (17/324)|du|²','small')
# Slice z=(a,ib) of H = I-iA_sp, e_Z=2/sqrt(15).
eps=2/math.sqrt(15);cx,cy,sc=584,300,81
ab=lambda a,b:(cx+sc*a,cy-sc*b)
line(*ab(-1.65,0),*ab(1.65,0),arrow=True);line(*ab(0,-1.65),*ab(0,1.65),arrow=True)
points=[]
for j in range(481):
    t=2*math.pi*j/480
    u=math.cos(t)/math.sqrt(1+eps);v=math.sin(t)/math.sqrt(1-eps)
    points.append(ab((u+v)/math.sqrt(2),(u-v)/math.sqrt(2)))
path(points,'#136f8a')
for a,b in [(1,1),(1,-1)]:
    norm=math.sqrt(a*a+b*b);s=1.5
    line(*ab(-s*a/norm,-s*b/norm),*ab(s*a/norm,s*b/norm),'#b7c6d1','3 4')
txt(725,323,'a');txt(596,158,'b')
txt(408,445,'z=(a,ib), a,b real; unit-Z frame','small')
txt(408,477,'a²+b²+2(2/√15)ab = 1')
txt(408,509,'Principal values: 1 ± 2/√15')
txt(408,542,'Both are positive.')
txt(408,577,'This is a derivative-space slice,','small')
txt(408,598,'not physical space.','small')
# Actual magnitudes for r=k=1, t between 0 and 3.
px,py,w,h=827,375,285,210
plot=lambda t,v:(px+w*t/3,py-h*v/1.3)
line(*plot(0,0),*plot(3.15,0),arrow=True);line(*plot(0,0),*plot(0,1.4),arrow=True)
for t in [0,1,2,3]:
    x,y=plot(t,0);line(x,y,x,y+5);txt(x,y+24,str(t),'small','middle')
for v in [.5,1]:
    x,y=plot(0,v);line(x-4,y,x,y);txt(x-10,y+5,str(v),'small','end')
path([plot(j/100,math.exp(-1)) for j in range(301)],'#136f8a')
path([plot(j/100,math.exp(5*(j/100)/12-13/12)) for j in range(301)],'#ae3f28')
txt(1120,405,'t');txt(830,132,'|w₁(1,t)|','small')
txt(909,233,'e=3/2','red');txt(963,300,'e=1','blue')
txt(795,445,'Neutral: e⁻¹','blue')
txt(795,477,'Growing: exp(5t/12 − 13/12)','red')
txt(795,509,'α²−σ²=1,  α+σ=e')
txt(795,542,'Exact Lwₖ=Bₑwₖ=0.')
txt(795,577,'The normalized cutoff tests are','small')
txt(795,598,'proved separately in the lesson.','small')
items.append('</svg>')
out.write_text('\n'.join(items)+'\n','utf-8')
print(out.name)

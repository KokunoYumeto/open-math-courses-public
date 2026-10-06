"""Actual circle-flow samples, compact suspension maps and exact integer cutoffs."""
from pathlib import Path
import argparse, math, os, tempfile
HERE=Path(__file__).resolve().parent
CACHE=tempfile.TemporaryDirectory(prefix='compact-holonomy-')
os.environ['MPLCONFIGDIR']=CACHE.name
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle
matplotlib.rcParams.update({'svg.hashsalt':'compact-holonomy-map-20261006','svg.fonttype':'path','font.family':'DejaVu Sans','axes.unicode_minus':False})
FONT_ROOT=HERE/'fonts'; FONT=FONT_ROOT/'DejaVuSans.ttf'
assert FONT.is_file()
fm.fontManager.addfont(str(FONT))
original_find=fm.fontManager.findfont
def local_find(*args,**kwargs):
    p=Path(original_find(*args,**kwargs)); local=FONT_ROOT/p.name
    if not local.is_file():raise RuntimeError('Unbound font '+p.name)
    return str(local)
fm.fontManager.findfont=local_find; fm.findfont=local_find
FP=fm.FontProperties(fname=str(FONT))
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--output-dir',type=Path,default=HERE.parents[1]/'figures')
OUT=ap.parse_args().output_dir.resolve(); OUT.mkdir(parents=True,exist_ok=True)
ink='#193348'; teal='#187b79'; purple='#8053a0'; gold='#e69a28'; muted='#63788b'
fig,axes=plt.subplots(2,2,figsize=(18,12),dpi=150)
fig.patch.set_facecolor('#f6f8fb')
def text(ax,x,y,s,size=12,color=ink,ha='left'):
    return ax.text(x,y,s,fontproperties=FP,fontsize=size,color=color,ha=ha,va='center')
def arrow(ax,a,b,color=ink,curve=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.6,color=color,connectionstyle=f'arc3,rad={curve}'))
def panel(ax,title):
    ax.set_xlim(0,10); ax.set_ylim(0,7); ax.set_aspect('equal'); ax.axis('off')
    text(ax,.15,6.65,title,17)
def flow(theta,t):
    return 2*math.atan2(math.exp(t)*math.sin(theta/2),math.cos(theta/2))

ax=axes[0,0]; panel(ax,'A. Actual normal germs on N = S¹ × S²')
cx,cy,r=2.5,3.9,1.3
ax.add_patch(Circle((cx,cy),r,fill=False,edgecolor=muted,lw=1.6))
for theta in [.35,.95,1.7,4.5,5.2,5.9]:
    phi=flow(theta,.7)
    start=(cx+r*math.cos(theta),cy+r*math.sin(theta))
    end=(cx+r*math.cos(phi),cy+r*math.sin(phi))
    ax.add_patch(Circle(start,.035,color=teal)); arrow(ax,start,end,teal,.10 if theta<math.pi else -.10)
for theta,label,off in [(0,'θ = 0: derivative e',.52),(math.pi,'θ = π: derivative 1/e',-.52)]:
    x,y=cx+r*math.cos(theta),cy+r*math.sin(theta)
    ax.add_patch(Circle((x,y),.075,color=gold))
    text(ax,x,y-1.70,label,11,ha='center')
text(ax,cx,5.65,'Time-one flow of sin(θ) d/dθ',12,ha='center')
sx,sy,sr=7.5,3.9,1.30
ax.add_patch(Circle((sx,sy),sr,facecolor='#edf5fa',edgecolor=muted,lw=1.5))
ax.add_patch(Ellipse((sx,sy),2*sr,.58,fill=False,edgecolor=purple,lw=1.3))
ax.plot([sx,sx],[sy-sr,sy+sr],color=muted,lw=.8,linestyle='--')
ax.add_patch(Circle((sx,sy+sr),.075,color=gold))
arrow(ax,(sx-.75,sy-.03),(sx+.75,sy-.03),purple,.4)
text(ax,sx,5.65,'Rotation R by 2π/s',12,ha='center')
text(ax,sx,1.97,'Nonidentity rotations retain nonidentity germs',10,ha='center')
text(ax,.2,.96,'p fixed; distinct quotient labels give distinct holonomy germs.',12)
text(ax,.2,.38,'Identity germs: source 0 × sZ; target 0 × Z.',12)

ax=axes[0,1]; panel(ax,'B. Compact suspensions and smooth foliated maps')
for x,title,xlabel,ylabel in [(1.05,'Mₛ → T²','f','R'),(6.10,'M∞ → T²','f','id')]:
    ax.add_patch(Rectangle((x,2.62),2.35,2.35,facecolor='#eef3f7',edgecolor=ink,lw=1.4))
    arrow(ax,(x+.23,2.35),(x+2.10,2.35),teal)
    text(ax,x+1.18,1.98,'u-loop: '+xlabel,11,ha='center')
    arrow(ax,(x-.28,2.83),(x-.28,4.75),purple)
    text(ax,x+1.18,5.34,title,13,ha='center')
    text(ax,x+1.18,3.78,'Opposite edges\nidentified',11,ha='center')
    text(ax,x+1.18,1.52,'v-loop: '+ylabel,11,ha='center')
arrow(ax,(3.66,3.75),(5.84,3.75),gold)
text(ax,4.75,4.30,'Aₘ',15,ha='center')
text(ax,4.75,3.18,'base (u,v) ↦ (mu,v)',10,ha='center')
text(ax,.2,.88,'Aₘ[u,v,q] = [mu,v,p]; all source leaves reach the same target torus.',11)
text(ax,.2,.35,'Full holonomy: (Z × Cₛ) ⋉ N  →  Z ⋉ N;  (n,c,q) ↦ (mn,p).',11)

ax=axes[1,0]; panel(ax,'C. Infinite induced action; displayed window, s = 2')
for y,m in [(4.75,1),(2.55,2)]:
    ax.plot([.7,9.3],[y,y],color=muted,lw=.9)
    for r in range(-4,5):
        x=5+.93*r; color=teal if r%m==0 else purple
        ax.add_patch(Circle((x,y),.09,color=color)); text(ax,x,y-.32,str(r),10,ha='center')
        if 0<=r<m:
            ax.add_patch(Circle((x,y),.18,fill=False,edgecolor=gold,lw=2))
            text(ax,x,y+.40,'1/2',11,ha='center')
    text(ax,.42,y,'…',17,ha='center'); text(ax,9.60,y,'…',17,ha='center')
    text(ax,.16,y+.90,'m = '+str(m)+':  r ↦ r + '+str(m)+'n',12)
    arrow(ax,(1.28,y+.46),(1.28+.93*m,y+.46),ink)
    text(ax,7.72,y+.88,'Σ w = '+('1/2' if m==1 else '1'),12,ha='center')
text(ax,.2,1.05,'At p, every transporter has two rotation labels.',12)
text(ax,.2,.48,'Cw = 2 × (1/2) = 1; off the finite support w = 0.',12)

ax=axes[1,1]; panel(ax,'D. Same coarse map; two different full images')
for x,y in [(1.1,4.9),(1.4,3.8),(.9,2.7)]:
    ax.add_patch(Ellipse((x,y),.85,.25,fill=False,edgecolor=teal,lw=1.4))
    arrow(ax,(x+.5,y),(5.0,3.8),muted)
ax.add_patch(Ellipse((5.6,3.8),1.0,.3,fill=False,edgecolor=purple,lw=1.8))
text(ax,.3,5.66,'Leaf classes of M₂',12)
text(ax,4.25,5.66,'One target torus leaf',12)
text(ax,2.82,2.20,'Coarse h is constant for both A₁ and A₂.',12,ha='center')
text(ax,7.28,4.90,'F₁:  aδₚ ↦ (a/2)δₚ',12,ha='center')
text(ax,7.28,3.06,'F₂:  aδₚ ↦ aδₚ',12,ha='center')
text(ax,.2,1.10,'Kernel order 2; target coset counts 1 and 2.',12)
text(ax,.2,.48,'The full arrow maps are not naturally isomorphic.',12)

fig.suptitle('Compact foliation holonomy retains the m/s image factor',fontproperties=FP,fontsize=24,color=ink,y=.985)
fig.text(.5,.025,'Exact proof: Theorem 5.29, equations (5.29.4)–(5.29.10). Circle arrows use actual time-0.7 samples; sphere/base drawings are schematics. Original CC0 diagram.',ha='center',fontproperties=FP,fontsize=11,color=ink)
fig.subplots_adjust(left=.025,right=.985,top=.93,bottom=.07,wspace=.13,hspace=.12)
fig.savefig(OUT/'compact-holonomy-map.png',metadata={'Software':'Original CC0 diagram; Matplotlib'})
notice=(FONT_ROOT/'LICENSE_DEJAVU.txt').read_text(encoding='utf-8')
fig.savefig(OUT/'compact-holonomy-map.svg',metadata={'Date':None,'Creator':'Original CC0 diagram','Description':'Unmodified DejaVu Sans; complete font terms:\n'+notice})
plt.close(fig)
print('Rendered compact-holonomy-map.png and compact-holonomy-map.svg')
CACHE.cleanup()

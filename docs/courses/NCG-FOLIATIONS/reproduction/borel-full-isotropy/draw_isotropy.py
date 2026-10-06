"""Four exact infinite-group action diagrams; displayed integers are only a window."""
from pathlib import Path
import os, argparse, tempfile
HERE=Path(__file__).resolve().parent
CACHE=tempfile.TemporaryDirectory(prefix='isotropy-figure-')
os.environ['MPLCONFIGDIR']=CACHE.name
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyArrowPatch, Circle
matplotlib.rcParams.update({'svg.hashsalt':'borel-full-isotropy-20261006','svg.fonttype':'path','font.family':'DejaVu Sans','font.size':12,'axes.unicode_minus':False})
FONT_ROOT=HERE/'fonts';FONT=FONT_ROOT/'DejaVuSans.ttf'
assert FONT.is_file()
fm.fontManager.addfont(str(FONT))
original_find=fm.fontManager.findfont
def local_find(*args,**kwargs):
    selected=Path(original_find(*args,**kwargs)); local=FONT_ROOT/selected.name
    if not local.is_file():raise RuntimeError('Unbound font '+selected.name)
    return str(local)
fm.fontManager.findfont=local_find;fm.findfont=local_find
FP=fm.FontProperties(fname=str(FONT))
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=HERE.parents[1]/'figures')
OUT=parser.parse_args().output_dir.resolve();OUT.mkdir(parents=True,exist_ok=True)
fig,axs=plt.subplots(2,2,figsize=(16,10),dpi=150)
fig.patch.set_facecolor('#f6f8fb')
colors=['#247a73','#9554a5']
def text(ax,x,y,s,size=12,color='#182a3c',ha='left'):
    ax.text(x,y,s,fontsize=size,fontproperties=FP,color=color,ha=ha,va='center')
def panel(ax,title,subtitle):
    ax.set_xlim(-5,6);ax.set_ylim(-2.1,3.1);ax.axis('off')
    ax.set_facecolor('white')
    text(ax,-4.8,2.85,title,17)
    text(ax,-4.8,2.3,subtitle,12)
def lattice(ax,m,s):
    ax.plot([-4.6,5.6],[.3,.3],color='#8193a3',lw=1)
    for z in range(-4,6):
        fill=colors[z%m] if m>1 else colors[0]
        ax.add_patch(Circle((z,.3),.16,color=fill))
        text(ax,z,-.12,str(z),11,ha='center')
        if 0<=z<m:
            text(ax,z,.82,'1' if s==1 else '1/2',12,ha='center')
            ax.add_patch(Circle((z,.3),.24,fill=False,edgecolor='#e79727',lw=2))
    text(ax,-4.7,.3,'…',15,ha='center');text(ax,5.8,.3,'…',15,ha='center')
    arrow=FancyArrowPatch((-3,1.25),(-3+m,1.25),arrowstyle='-|>',mutation_scale=15,lw=1.8,color='#182a3c')
    ax.add_patch(arrow);text(ax,-3+m/2,1.64,'n = 1: z ↦ z + '+str(m),11,ha='center')
panel(axs[0,0],'A. F₁,₁ : Z → Z','F(n) = n; kernel size 1; one action orbit')
lattice(axs[0,0],1,1)
text(axs[0,0],-4.8,-.83,'Cutoff: f(0) = 1, zero elsewhere')
text(axs[0,0],-4.8,-1.45,'Cf = 1;   Σ f = 1;   image Λₐ → Λₐ',14)
panel(axs[0,1],'B. F₂,₁ : Z → Z','F(n) = 2n; kernel size 1; two action orbits')
lattice(axs[0,1],2,1)
text(axs[0,1],-4.8,-.83,'Cutoff: f(0) = f(1) = 1, zero elsewhere')
text(axs[0,1],-4.8,-1.45,'Cf = 1;   Σ f = 2;   image Λₐ → Λ₂ₐ',14)
panel(axs[1,0],'C. F₂,₂ : Z × C₂ → Z','F(n,u) = 2n; kernel size 2; two action orbits')
lattice(axs[1,0],2,2)
text(axs[1,0],-4.8,-.83,'Each transporter occurs twice; f(0) = f(1) = 1/2')
text(axs[1,0],-4.8,-1.45,'Cf = 2 × (1/2) = 1;   Σ f = 1;   Λₐ → Λₐ',13)
panel(axs[1,1],'D. F₀ : Z → Z','F(n) = 0; infinite kernel; singleton action orbits')
ax=axs[1,1]
ax.plot([-4.6,5.6],[.3,.3],color='#8193a3',lw=1)
for z in range(-4,6):
    ax.add_patch(Circle((z,.3),.15,color='#ae4646'));text(ax,z,-.12,str(z),11,ha='center')
text(ax,-4.7,.3,'…',15,ha='center');text(ax,5.8,.3,'…',15,ha='center')
ax.add_patch(FancyArrowPatch((-.1,.55),(.1,.55),connectionstyle='arc3,rad=-4',arrowstyle='-|>',mutation_scale=15,color='#ae4646',lw=1.8))
text(ax,0,1.64,'Every n fixes z; infinitely many transporters',11,ha='center')
text(ax,-4.8,-.83,'Cf(z) = 0 if f(z) = 0; infinity if f(z) > 0')
text(ax,-4.8,-1.45,'No normalized cutoff; supremum integral = 0',13)
fig.suptitle('Full arrows determine normalization and image scale',fontproperties=FP,fontsize=23,y=.985,color='#182a3c')
fig.text(.5,.015,'Integer windows in infinite action spaces. Exact proofs: (5.26.4), (5.28.3)–(5.28.4).  a > 0.  Original diagram: CC0.',ha='center',fontproperties=FP,fontsize=11,color='#182a3c')
fig.subplots_adjust(left=.035,right=.985,bottom=.07,top=.92,wspace=.16,hspace=.20)
fig.savefig(OUT/'borel-full-isotropy.png',dpi=150,metadata={'Software':'Original CC0 diagram; Matplotlib'})
notice=(FONT_ROOT/'LICENSE_DEJAVU.txt').read_text(encoding='utf-8')
fig.savefig(OUT/'borel-full-isotropy.svg',metadata={'Date':None,'Creator':'Original CC0 diagram','Description':'Unmodified DejaVu Sans glyph terms:\n'+notice})
plt.close(fig)
print('Rendered borel-full-isotropy.png and borel-full-isotropy.svg')
CACHE.cleanup()

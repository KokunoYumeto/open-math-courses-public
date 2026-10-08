"""Support-corner inclusions and an exact finite coefficient mass model."""
from pathlib import Path
from fractions import Fraction
import argparse, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=HERE.parent / 'typeiii-zero-decomposition')
args = parser.parse_args()
for name in ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf']:
    fontManager.addfont(str(args.font_dir / name))
font = FontProperties(fname=str(args.font_dir / 'DejaVuSans.ttf'))
plt.rcParams.update({'font.family':font.get_name(),'font.size':10,
                     'svg.hashsalt':'oa-flow-centralizer-consequences-v1','svg.fonttype':'path'})
data=json.loads((HERE/'data.json').read_text()); m=data['finite_model']
lam=Fraction(m['lambda0']);a=list(map(Fraction,m['a']));h=list(map(Fraction,m['h']))
mass=Fraction(m['normalized_trace_mass']);normalized=list(map(Fraction,m['normalized_h']))
assert h==[lam+(1-lam)*(1+x)/3 for x in a]
assert sum(h)/2==mass and normalized==[x/mass for x in h] and sum(normalized)/2==1

fig=plt.figure(figsize=(12,7.1),facecolor='#fbfcff')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.2],width_ratios=[1.2,1],
                    left=.08,right=.95,bottom=.16,top=.85,wspace=.40,hspace=.60)
ax=fig.add_subplot(gs[0,:]);ax.set(xlim=(0,12),ylim=(-.55,4.0));ax.axis('off')
labels=[r'$Dp$',r'$C=Z(P)$',r'$P$',r'$pNp$',r'$pMp$']
for j,label in enumerate(labels):
    x=.3+2.4*j
    ax.add_patch(FancyBboxPatch((x,1.2),1.7,.8,boxstyle='round,pad=.03,rounding_size=.10',
                              facecolor='#e7eff9',edgecolor='#5e7695',linewidth=1))
    ax.text(x+.85,1.6,label,ha='center',va='center',fontsize=14)
    if j<4:ax.text(x+2.05,1.6,r'$\subseteq$',ha='center',va='center',fontsize=15)
ax.add_patch(FancyArrowPatch((3.55,2.12),(5.95,2.12),arrowstyle='-|>',mutation_scale=13,
                             connectionstyle='arc3,rad=-.55',color='#397b70',lw=1.4))
ax.text(4.75,3.60,r'$C^{\prime}\cap pMp=P$',ha='center',fontsize=12,color='#275f56',
        bbox={'facecolor':'#fbfcff','edgecolor':'none','pad':1.5})
ax.add_patch(FancyArrowPatch((5.95,1.04),(3.55,1.04),arrowstyle='-|>',mutation_scale=13,
                             connectionstyle='arc3,rad=-.50',color='#976b35',lw=1.4))
ax.text(4.75,-.32,r'$P^{\prime}\cap pMp=C$',ha='center',fontsize=12,color='#805625',
        bbox={'facecolor':'#fbfcff','edgecolor':'none','pad':1.5})
ax.text(9.9,.25,'All commutants in pMp\nInclusions need not be strict',
        ha='center',fontsize=9,color='#45566d')
ax.text(.3,3.25,'The actual support corner\nMC16–20',fontsize=10,color='#45566d')

bx=fig.add_subplot(gs[1,0]);xs=[0,1];width=.30
bx.bar([x-width/2 for x in xs],[float(x) for x in h],width,color='#6485b6',label='original h')
bx.bar([x+width/2 for x in xs],[float(x) for x in normalized],width,color='#d3a354',label='h / m')
for j in xs:
    bx.text(j-width/2,float(h[j])+.035,str(h[j]),ha='center',fontsize=10)
    bx.text(j+width/2,float(normalized[j])+.035,str(normalized[j]),ha='center',fontsize=10)
bx.axhline(1,color='#8f9aaa',lw=.8,ls='--')
bx.set(xticks=xs,xticklabels=['coordinate 1','coordinate 2'],ylim=(0,1.30),
       ylabel='density eigenvalue')
bx.spines[['top','right']].set_visible(False)
bx.legend(loc='upper left',frameon=False,fontsize=9)
bx.set_title('The mass must be divided out',loc='left',fontweight='bold',fontsize=12,pad=14)
bx.text(.5,-.23,r'$\operatorname{tr}_2(h)=25/36\quad\longrightarrow\quad\operatorname{tr}_2(h/m)=1$',
        transform=bx.transAxes,ha='center',fontsize=11)

cx=fig.add_subplot(gs[1,1]);cx.axis('off')
cx.text(0,.94,'The two commutant steps',fontsize=12,fontweight='bold',va='top')
cx.text(0,.70,r'$x\in (Dp)^{\prime}\cap pMp\ \Longrightarrow\ x\in pNp$',fontsize=12)
cx.text(0,.55,'All nonzero Fourier degrees vanish.',fontsize=10,color='#45566d')
cx.text(0,.34,r'$x\in C^{\prime}\cap pNp\ \Longrightarrow\ xh=hx$',fontsize=12)
cx.text(0,.19,'The spectral projections of h lie in C.',fontsize=10,color='#45566d')
cx.text(0,.02,'Together they give x ∈ P.  MC18–19',fontsize=10,color='#45566d')
fig.suptitle('Centralizers: support, commutants and normalization',x=.08,ha='left',
             fontsize=17,fontweight='bold',color='#1e304a')
fig.text(.08,.025,'Exact matrix density calculation MC21; the matrix algebra illustrates mass normalization, not type III. Original diagrams of the stated proofs.',
         fontsize=8.8,color='#43536a')
fig.savefig(HERE/'centralizer-consequences.svg',metadata={'Date':None,'Creator':'OA-FLOW course project'})
fig.savefig(HERE/'centralizer-consequences.png',dpi=180,metadata={'Software':'OA-FLOW course project'})
plt.close(fig)

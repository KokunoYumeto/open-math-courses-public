"""Draw exact projected normal contraction and signed contact slices."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams.update({'font.family':'DejaVu Sans','font.size':20,'mathtext.fontset':'stix','svg.fonttype':'path'})
here=Path(__file__).resolve().parent
dest=here/'weighted-contraction-and-contact-signs.svg'
fig,axes=plt.subplots(3,1,figsize=(10,13),gridspec_kw={'height_ratios':[1.3,1,1]})
fig.subplots_adjust(top=0.95,bottom=0.115,left=0.15,right=0.95,hspace=0.65)
ax=axes[0]
times=np.linspace(0,6,1001)
for p0,q0,color in [(1,1,'#176880'),(-1,1,'#98561e'),(-1,-1,'#176880'),(1,-1,'#98561e')]:
    pp=p0*np.exp(-2*times/3)
    qq=q0*np.exp(-times/3)
    ax.plot(pp,qq,color=color,lw=3)
    ax.plot([p0],[q0],'o',color=color,ms=8)
    for tt in [0.8,2.6]:
        start=(p0*np.exp(-2*tt/3),q0*np.exp(-tt/3))
        end=(p0*np.exp(-2*(tt+0.35)/3),q0*np.exp(-(tt+0.35)/3))
        ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','color':color,'lw':2,'mutation_scale':23})
ax.axhline(0,color='#b7b7b7',lw=1)
ax.axvline(0,color='#b7b7b7',lw=1)
ax.plot([0],[0],'o',color='#262626',ms=7)
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),xlabel=r'$p$',ylabel=r'$q$')
ax.set_title(r'$p_s=e^{-2s/3}p_0,\quad q_s=e^{-s/3}q_0$',fontsize=22,pad=18)
ax.text(0.5,-0.38,r'projection; $0\leq s\leq6$, limit $(0,0)$',ha='center',transform=ax.transAxes,fontsize=19)
xx=np.linspace(-1.1,1.1,1001)
for ax,k in zip(axes[1:],[2,3]):
    ax.plot(xx,xx**k,color='#176880',lw=3,label=r'$+x_1^'+str(k)+'$')
    ax.plot(xx,-xx**k,color='#98561e',lw=3,ls='--',label=r'$-x_1^'+str(k)+'$')
    ax.axhline(0,color='#b7b7b7',lw=1)
    ax.axvline(0,color='#b7b7b7',lw=1)
    ax.plot([0],[0],'o',color='#262626',ms=6)
    ax.set(xlim=(-1.1,1.1),ylim=(-1.4,1.4),xlabel=r'$x_1$',ylabel=r'$\mathrm{Im}\,p$')
    ax.set_title(r'$k='+str(k)+r'$; slice $\xi_1=0,\ \xi_n=1$',fontsize=21,pad=13)
    ax.legend(loc='upper center',ncol=2,fontsize=18,framealpha=0.95)
    note='Even negative contact: positive mark' if k==2 else r'Odd negative contact: mark $(0,-e_n)$'
    ax.text(0.5,-0.43,note,ha='center',transform=ax.transAxes,fontsize=19)
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=16)
fig.savefig(dest,format='svg',metadata={'Title':'Projected weighted contraction and signed contact profiles','Description':'Exact normal-flow projection for weights2/3,1/3 and the xi_n=1 contact slices of orders2,3. The tangential flow is not pictured.','Creator':'Original AN-04 mathematical drawing','Date':None})
png=here/'weighted-contraction-and-contact-signs.png'
fig.savefig(png,dpi=130)
plt.close(fig)
print('Drawn 1001 samples per exact curve; original SVG and inspection PNG saved.')

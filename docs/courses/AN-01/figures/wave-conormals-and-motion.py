"""Full wave characteristic conormals and base motion. GPT-6 Astra; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['svg.hashsalt']='AN01-wave-conormals-and-motion'
out=Path(__file__).parent
fig,axes=plt.subplots(1,2,figsize=(10.6,5.5),layout='constrained')
fig.patch.set_facecolor('#f8fafc')
for ax in axes:
    ax.set_facecolor('#f8fafc');ax.grid(alpha=.15);ax.set_axisbelow(True)
    ax.spines[['top','right']].set_visible(False)
    ax.set(xlim=(-1.45,1.45),ylim=(-2.9,2.9),aspect='equal')
z=np.linspace(-1.25,1.25,251)
for sign,col in [(1,'#176689'),(-1,'#ac5525')]:
    axes[0].plot(z,-2*sign*z,lw=2.3,color=col)
    axes[1].plot(z,2*sign*z,lw=2.3,color=col)
    for lam in [-1,1]:
        p=np.array([.25*lam,-.5*sign*lam])
        q=np.array([.7*lam,-1.4*sign*lam])
        axes[0].annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=col,lw=2,mutation_scale=15))
        # Positive Hamilton time with conormal lambda*(-2sign,1).
        base=np.array([-.65*sign*lam,-1.3*lam])
        end=base+np.array([-.18*sign*lam,-.36*lam])
        axes[1].annotate('',xy=end,xytext=base,arrowprops=dict(arrowstyle='->',color=col,lw=2,mutation_scale=15))
axes[0].scatter([0],[0],s=55,facecolor='#f8fafc',edgecolor='#243549',zorder=5,lw=1.3)
axes[0].set(title='Covector fiber: all four rays',xlabel=r'$\xi$',ylabel=r'$\tau$')
axes[1].set(title='Base: opposite conormals reverse motion',xlabel='t',ylabel='x')
axes[0].text(-1.3,2.6,r'$\tau=-2\xi$',color='#176689',fontsize=12)
axes[0].text(.22,2.6,r'$\tau=2\xi$',color='#ac5525',fontsize=12)
axes[1].text(-1.3,2.6,r'$x=-2t$',color='#ac5525',fontsize=12)
axes[1].text(.32,2.6,r'$x=2t$',color='#176689',fontsize=12)
fig.suptitle(r'$p=\tau^2-4\xi^2,\qquad H_p=(2\tau,-8\xi;0,0)$',fontsize=15)
for ext in ['png','svg']:
    fig.savefig(out/('wave-conormals-and-motion.'+ext),dpi=175,
                metadata={'Date':'2026-10-20'} if ext=='svg' else None)
svg=out/'wave-conormals-and-motion.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)

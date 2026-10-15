"""Finite-window samples of the exact functions in IK1.1 and IK5.2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'oa-mod-ik8-v1','font.size':11})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(11,4.8),constrained_layout=True)
t=np.linspace(-3,3,2401)
for phi,color,label in [(-np.pi/2,'#1f5f99',r'$\phi=-\pi/2,\ \int k_\phi=1/\sqrt{2}$'),(0,'#444444',r'$\phi=0,\ \int k_0=1/2$'),(np.pi/2,'#ac5726',r'$\phi=\pi/2,\ \int k_\phi=1/\sqrt{2}$')]:
    axes[0].plot(t,np.exp(-phi*t)/(2*np.cosh(np.pi*t)),color=color,lw=2,label=label)
axes[0].set_title(r'Strip kernels $k_\phi(t)$')
axes[0].set_xlabel(r'$t$');axes[0].set_ylabel('Kernel value')
axes[0].set_xlim(-3,3);axes[0].set_ylim(0,.66);axes[0].legend(loc='upper right',fontsize=9)
x=np.linspace(-1.6,1.6,2401)
for eps,color,label in [(1,'#1f5f99',r'$\varepsilon=1$'),(.5,'#267a4a',r'$\varepsilon=1/2$'),(.25,'#8b449a',r'$\varepsilon=1/4$')]:
    axes[1].plot(x,1/(eps*np.cosh(np.pi*x/eps)),color=color,lw=2,label=label)
axes[1].set_title(r'Approximate identities $p_\varepsilon(x)$')
axes[1].set_xlabel(r'$x$');axes[1].set_ylabel('Density')
axes[1].set_xlim(-1.6,1.6);axes[1].set_ylim(0,4.4);axes[1].legend(loc='upper right')
axes[1].text(-1.48,3.5,r'$\int p_\varepsilon=1$'+'\n'+r'$p_\varepsilon(0)=1/\varepsilon$',fontsize=11)
for ax in axes:
    ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'bounded-modular-kernels.svg',metadata={'Date':None})
fig.savefig(out/'bounded-modular-kernels.png',dpi=150)
plt.close(fig)

"""Smooth boundary approaches and exact critical concentration profiles. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
eps=np.linspace(0,.4,401)
for s,color in [(-.5,'#176db0'),(0,'#c95a12'),(.5,'#703fa0')]:
    axes[0].plot(s+eps,eps**2,color=color,label=rf'$s={s:g}$')
    axes[0].scatter([s],[0],color=color,s=25,zorder=4)
    j=220
    axes[0].annotate('',xy=(s+eps[j-35],eps[j-35]**2),xytext=(s+eps[j],eps[j]**2),arrowprops=dict(arrowstyle='->',color=color,lw=1.5))
axes[0].axhline(0,color='.5',lw=.8)
axes[0].set(xlabel=r'$\operatorname{Re}F_\varepsilon$',ylabel=r'$\operatorname{Im}F_\varepsilon$',title=r'$F_\varepsilon(s)=s+\varepsilon+i\varepsilon^2,\quad g^\prime(s)=1$',ylim=(-.015,.18),xlim=(-.62,1.3))
axes[0].legend(loc='center right',frameon=False)
x=np.linspace(-.8,.8,1601)
for e,color in [(.16,'#176db0'),(.04,'#c95a12'),(.01,'#703fa0')]:
    axes[1].plot(x,e/(x**4+e**2),color=color,label=rf'$\varepsilon={e:g}$')
axes[1].set(xlabel=r'$x$',ylabel=r'$-\operatorname{Im}(x^2+i\varepsilon)^{-1}$',title='A critical singular level',ylim=(0,108))
axes[1].text(.03,.93,r'height $=\varepsilon^{-1}$'+'\n'+r'core: $|x|\leq\sqrt{\varepsilon}$'+'\n'+r'core mass $\geq\varepsilon^{-1/2}$',transform=axes[1].transAxes,va='top')
axes[1].legend(loc='upper right',frameon=False)
for ax in axes:
    ax.grid(alpha=.15)
    ax.spines[['top','right']].set_visible(False)
fig.savefig(root/'moving-boundary-and-critical-concentration.png',dpi=180)
fig.savefig(root/'moving-boundary-and-critical-concentration.svg')
svg=root/'moving-boundary-and-critical-concentration.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)

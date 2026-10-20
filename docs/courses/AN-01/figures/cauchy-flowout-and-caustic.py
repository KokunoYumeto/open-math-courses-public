"""Exact characteristic curves for the Hamilton-Jacobi example, CC0.
Programme figure: GPT-6 Astra (OpenAI). See AN01-U037, Solution 26.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':
    out=out/'advanced-U183-20261020/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13,
                     'svg.hashsalt':'AN01-cauchy-flowout-and-caustic'})
fig,axs=plt.subplots(1,2,figsize=(13,5.7),layout='constrained')
ts=np.linspace(-.25,1.35,160)
cols=['#305d9b','#a24e20','#16816a','#9b3f7d','#756721']
for y,c in zip([-1,-.5,0,.5,1],cols):
    axs[0].plot(ts,(1-ts)*y,color=c,lw=2,label=rf'$y={y:g}$')
axs[0].axvline(1,color='#444444',ls='--',lw=1.2)
axs[0].plot([1],[0],'o',color='#111111')
axs[0].annotate('Base projection loses rank',xy=(1,0),xytext=(.12,1.17),
                arrowprops=dict(arrowstyle='->',color='#333333'),fontsize=11)
axs[0].set(xlabel=r'$t$',ylabel=r'$x$',title=r'Base: $x=(1-t)y$',xlim=(-.3,1.4),ylim=(-1.45,1.45))
axs[0].legend(ncol=3,loc='lower left',fontsize=10)
ys=np.linspace(-1,1,160)
for t,c in zip([0,.5,1,1.25],['#305d9b','#16816a','#9b3f7d','#a24e20']):
    axs[1].plot((1-t)*ys,-ys,color=c,lw=2.4,label=rf'$t={t:g}$')
axs[1].set(xlabel=r'$x$',ylabel=r'$\xi$',title=r'Phase curves: $\xi=-y$, $\tau=-\xi^2/2$',xlim=(-1.3,1.3),ylim=(-1.2,1.2))
axs[1].legend(loc='lower right',fontsize=10)
for ax in axs:
    ax.axhline(0,color='#777777',lw=.6,zorder=0)
    ax.axvline(0,color='#777777',lw=.6,zorder=0)
    ax.grid(alpha=.18)
fig.suptitle(r'$p=\tau+\xi^2/2,\quad \phi(0,x)=-x^2/2$'+'\nA smooth phase-space surface can cease to be a base graph',fontsize=16)
for ext in ['png','svg']:
    target=out/('cauchy-flowout-and-caustic.'+ext)
    fig.savefig(target,dpi=170,metadata={'Date':None} if ext=='svg' else None)
    if ext=='svg':
        target.write_text('\n'.join(line.rstrip() for line in target.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)

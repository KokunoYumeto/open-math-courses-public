"""Original schematic of proved and conjectured zeta growth exponents. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':14,'axes.titlesize':17,'axes.labelsize':16})
x=np.linspace(-.35,1.35,681)
conv=np.where(x<=0,.5-x,np.where(x<1,(1-x)/2,0))
lh=np.maximum(0,.5-x)
fig,axes=plt.subplots(1,2,figsize=(11.8,4.8),sharey=True)
for ax in axes:
    ax.axhline(0,color='#61746a',lw=.7)
    ax.axvline(.5,color='#9b9989',lw=1,ls=':')
    ax.set_xlim(-.35,1.35);ax.set_ylim(-.05,.95)
    ax.set_xticks([0,.5,1]);ax.set_xlabel(r'$\sigma$')
    ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
axes[0].plot(x,conv,color='#1b635a',lw=3,label='Proved upper envelope')
axes[0].plot(x,lh,color='#9a6640',lw=1.8,ls='--',label='Proved lower envelope')
axes[0].fill_between(x,lh,conv,color='#1b635a',alpha=.11)
axes[0].scatter([.5],[.25],color='#1b635a',zorder=3)
axes[0].annotate(r'$\mu(1/2)\leq 1/4$',(.5,.25),xytext=(.64,.4),arrowprops={'arrowstyle':'->','color':'#1b635a'})
axes[0].set_title('Convexity bounds');axes[0].set_ylabel(r'Growth exponent $\mu(\sigma)$')
axes[0].legend(loc='upper right',fontsize=11)
axes[1].plot(x,lh,color='#9a6640',lw=3,label='Conditional exact value under LH')
axes[1].scatter([.5],[0],color='#9a6640',zorder=3)
axes[1].annotate(r'$\mu(1/2)=0$',(.5,0),xytext=(.6,.18),arrowprops={'arrowstyle':'->','color':'#9a6640'})
axes[1].set_title('The Lindelöf hypothesis');axes[1].legend(loc='upper right',fontsize=11)
fig.tight_layout(pad=1.1)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=160)

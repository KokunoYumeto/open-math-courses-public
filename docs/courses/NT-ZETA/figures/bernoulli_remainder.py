"""Bernoulli sawtooth and its exact periodic primitive; original figure, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes=plt.subplots(2,1,figsize=(7.4,5.2),sharex=True,layout='constrained')
blue='#22718a'; green='#386b46'
for k in range(3):
    u=np.linspace(k,k+1,401)
    v=u-k
    axes[0].plot(u,v-.5,color=blue,lw=2.5)
    axes[0].scatter([k],[ -.5],color=blue,s=45,zorder=4)
    axes[0].scatter([k+1],[.5],facecolors='white',edgecolors=blue,s=45,zorder=4)
    axes[1].plot(u,(v*v-v)/2,color=green,lw=2.5)
    axes[1].fill_between(u,(v*v-v)/2,0,color=green,alpha=.15)
axes[0].scatter([3],[-.5],color=blue,s=45,zorder=4)
axes[0].set_title(r'$b(u)=\{u\}-1/2$: zero mean on each period',fontsize=17)
axes[1].set_title(r'$F(u)=(\{u\}^2-\{u\})/2$: bounded primitive',fontsize=17)
axes[0].set_ylim(-.62,.62);axes[0].set_yticks([-.5,0,.5],['−1/2','0','1/2'])
axes[1].set_ylim(-.15,.03);axes[1].set_yticks([-.125,0],['−1/8','0'])
axes[1].axhline(-.125,color=green,ls='--',lw=1.2)
axes[1].set_xlabel('u',fontsize=19)
for ax in axes:
    ax.set_xlim(0,3);ax.set_xticks([0,.5,1,1.5,2,2.5,3])
    ax.tick_params(labelsize=17);ax.axhline(0,color='#555555',lw=1)
    ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180,metadata={'Software':None})

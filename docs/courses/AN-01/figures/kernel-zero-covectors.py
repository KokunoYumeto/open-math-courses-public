"""Exact cotangent examples from AN01-U084, Exercises 5 and 6. CC0.

The left panel shows zeta=-2*xi. The right shows sampled directions
of the full punctured outer cotangent plane; every middle covector is 0.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(12.8,5.7),layout='constrained')
for ax in axes:
    ax.set_aspect('equal');ax.set_xlim(-1.55,1.55);ax.set_ylim(-1.55,1.55)
    ax.axhline(0,color='#a5b1c2',lw=.8);ax.axvline(0,color='#a5b1c2',lw=.8)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.15)
    ax.set_xlabel(r'outer covector $\xi$');ax.set_ylabel(r'outer covector $\zeta$')
    ax.spines[['top','right']].set_visible(False)
x=np.linspace(-.72,.72,200)
axes[0].plot(x,-2*x,color='#1565a6',lw=2.6)
axes[0].scatter([.5,-.5],[-1,1],color='#1565a6',s=45,zorder=4)
axes[0].annotate(r'$(1/2,-1)$',(.5,-1),xytext=(.66,-.75),fontsize=11)
axes[0].set_title('Linear kernels: $a=2$, $b=-1$\n'+r'$\eta=2\xi,\quad\zeta=-\eta=-2\xi$',pad=14)
for k in range(12):
    angle=2*np.pi*k/12
    v=1.15*np.array([np.cos(angle),np.sin(angle)])
    axes[1].annotate('',xy=v,xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#a33263',lw=1.7))
axes[1].set_title('Point-mass composition\n'+r'full outer fiber $\setminus\{0\}$; middle $\eta=0$',pad=14)
for ax in axes:
    ax.scatter([0],[0],s=48,facecolor='white',edgecolor='#25354b',linewidth=1.4,zorder=6)
fig.suptitle('The matched covector can be zero',fontsize=19,fontweight='bold')
fig.text(.5,-.10,'At the outer base point (x,z)=(0,0). Open circles exclude the joint zero covector.\nRight-hand arrows sample directions; every nonzero direction belongs.',ha='center',fontsize=11)
fig.savefig(out/'kernel-zero-covectors.png',dpi=210,bbox_inches='tight',facecolor='white')
fig.savefig(out/'kernel-zero-covectors.svg',bbox_inches='tight',facecolor='white')
p=out/'kernel-zero-covectors.svg';p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines()).rstrip()+'\n',encoding='utf-8')

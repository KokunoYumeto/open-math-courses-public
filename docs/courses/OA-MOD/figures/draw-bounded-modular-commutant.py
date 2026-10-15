from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

D=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'oa-mod-commutant-mc8-v1'})
fig=plt.figure(figsize=(14,4.8),layout='constrained')
grid=fig.add_gridspec(1,3,width_ratios=[1.5,1,1])
ax=fig.add_subplot(grid[0,0])
ax.set(xlim=(-.55,2.8),ylim=(-.55,2.55));ax.axis('off')
nodes={'a':(0,2),'b':(2,2),'c':(2,0),'d':(0,0)}
labels={'a':r'$E_{12}$','b':r'$E_{21}$','c':r'$E_{11}$','d':r'$E_{11}$'}
for key,xy in nodes.items():
    ax.text(*xy,labels[key],ha='center',va='center',fontsize=17,
            bbox={'boxstyle':'round,pad=.4','facecolor':'#f0f4f8','edgecolor':'#a0aec0'})
def edge(a,b,label,xy,color):
    ax.add_patch(FancyArrowPatch(nodes[a],nodes[b],arrowstyle='-|>',mutation_scale=16,
                                shrinkA=28,shrinkB=28,lw=2,color=color))
    ax.text(*xy,label,ha='center',va='center',fontsize=13,color=color,
            bbox={'facecolor':'white','edgecolor':'none','pad':2})
edge('a','b',r'$J$',(1,2.25),'#235a92')
edge('b','c',r'$\ell_{E_{12}}$',(2.43,1),'#235a92')
edge('c','d',r'$J$',(1,-.25),'#235a92')
edge('a','d',r'$r_{E_{21}}$',(-.37,1),'#9c3d10')
ax.set_title(r'(a) $J\ell_{E_{12}}J=r_{E_{21}}$',pad=15,fontsize=14)
ax.text(1,-.53,r'$H=M_2(\mathbb{C}),\quad \langle X,Y\rangle=\mathrm{Tr}(Y^*X)$',
        ha='center',va='top',fontsize=10)
for col,sgn,title,color in [(1,1,r'(b) $E_{12}$ coefficient','#146b8a'),
                           (2,-1,r'(c) $E_{21}$ coefficient','#a44920')]:
    ar=fig.add_subplot(grid[0,col]);ar.set_aspect('equal')
    ar.set(xlim=(-1.38,1.38),ylim=(-1.38,1.38))
    theta=np.linspace(0,2*np.pi,361)
    ar.plot(np.cos(theta),np.sin(theta),color='#b7c3cb',lw=1.2)
    ar.axhline(0,color='#d3d9de',lw=.8);ar.axvline(0,color='#d3d9de',lw=.8)
    ar.plot([0,1],[0,0],color='#708090',lw=1.6)
    ar.annotate('',xy=(0,sgn),xytext=(0,0),
                arrowprops={'arrowstyle':'-|>','lw':2.2,'color':color})
    arc=np.linspace(0,sgn*np.pi/2,61)
    ar.plot(.65*np.cos(arc),.65*np.sin(arc),color=color,lw=2)
    ar.annotate('',xy=(.65*np.cos(arc[-1]),.65*np.sin(arc[-1])),
                xytext=(.65*np.cos(arc[-5]),.65*np.sin(arc[-5])),
                arrowprops={'arrowstyle':'-|>','lw':2,'color':color})
    ar.scatter([1,0],[0,sgn],color=['#708090',color],s=35,zorder=4)
    ar.text(1.09,-.1,'1',fontsize=13)
    ar.text(.11,sgn*1.08,r'$i$' if sgn==1 else r'$-i$',color=color,fontsize=15,va='center')
    ar.text(.4,sgn*.4,r'$+\pi/2$' if sgn==1 else r'$-\pi/2$',color=color,fontsize=11)
    ar.set_title(title,pad=15,fontsize=13)
    ar.set_xticks([]);ar.set_yticks([])
    for spine in ar.spines.values():spine.set_visible(False)
    ar.text(0,-1.4,r'$4^{it_*}=i$' if sgn==1 else r'$4^{-it_*}=-i$',
            ha='center',va='top',fontsize=13,color=color)
fig.suptitle(r'Exact matrix model: $\rho=\mathrm{diag}(4,1)$ and $t_*=\pi/(2\log4)$',fontsize=16)
fig.savefig(D/'bounded-modular-commutant.svg',metadata={'Date':None,'Creator':'OpenAI Codex; exact MC8 model'})
fig.savefig(D/'bounded-modular-commutant.png',dpi=160,metadata={'Software':'OpenAI Codex; exact MC8 model'})


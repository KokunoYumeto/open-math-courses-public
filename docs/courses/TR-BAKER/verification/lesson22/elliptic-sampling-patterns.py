"""Symbolic index-set diagram for the two interpolation arguments."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch

plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans',
                     'axes.spines.top':False,'axes.spines.right':False})
fig, axes=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
dark='#126e7c'; pale='#dcecf0'; boundary='#176579'
for ax in axes:
    ax.set_xlim(-.025,1.06);ax.set_ylim(-.025,1.10)
    ax.set_xlabel('Integer node index s',labelpad=12)
    ax.grid(False)

ax=axes[0]
ax.add_patch(Rectangle((0,0),.65,.5,facecolor=pale,edgecolor=boundary,lw=1.5))
ax.add_patch(Rectangle((0,0),.17,1,facecolor=dark,alpha=.9))
ax.set_xticks([0,.17,.65,1],['0',r'$S_0-1$',r'$nS$',r'$2nS$'])
ax.set_yticks([0,.5,1],['0',r'$nT$',r'$2nT$'])
ax.set_ylabel(r'Total order $|\alpha|$')
ax.set_title('No positive sampled multiple in the subgroup',pad=18)
ax.annotate('Interpolate each jet\nalong the line z w',xy=(.47,.36),
            xytext=(.48,.74),ha='center',va='center',
            arrowprops={'arrowstyle':'->','color':boundary,'lw':1.7})

ax=axes[1]
ax.add_patch(Rectangle((0,0),.65,.76,facecolor=pale,edgecolor=boundary,lw=1.5))
ax.add_patch(Rectangle((0,0),1,.19,facecolor=dark,alpha=.9))
ax.set_xticks([0,.65,1],['0',r'$nS$',r'$2nS$'])
ax.set_yticks([0,.19,.76],['0',r'$T_0-1$',r'$nT$'])
ax.set_ylabel(r'Last-direction order $m$ (other exponents zero)')
ax.set_title('A sampled multiple lies in the subgroup',pad=18)
ax.annotate('Interpolate in w;\nthen apply Cauchy',xy=(.42,.49),
            xytext=(.52,.97),ha='center',va='center',
            arrowprops={'arrowstyle':'->','color':boundary,'lw':1.7})

fig.legend(handles=[Patch(facecolor=dark,label='Prescribed small jets'),
                    Patch(facecolor=pale,edgecolor=boundary,label='Jets bounded after interpolation')],
           loc='outside lower center',ncol=2,frameon=False)
fig.suptitle('Two sampling patterns — symbolic axes, not to scale',fontsize=16)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=160)
plt.close(fig)

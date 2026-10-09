"""Exact coordinate regions of NS-FLUID-10; no solution or energy is sampled."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Patch
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(14.5,6.6),layout='constrained')
gray='#b5bec9';green='#4baf91';blue='#bfd5f3';ink='#243649'
ax=axes[0]
ax.set_xscale('log');ax.set_xlim(2.6,133);ax.set_ylim(-.045,1.07)
ax.add_patch(Rectangle((3,0),117,1,fill=False,edgecolor=ink,linewidth=1.5))
ax.add_patch(Rectangle((3,.5),117,.5,color=blue,alpha=.65))
for lo,hi in [(3,6),(60,120)]:ax.add_patch(Rectangle((lo,0),hi-lo,1,color=gray,alpha=.6))
ax.add_patch(Rectangle((30,0),30,.25,color=green,alpha=.9))
ax.hlines(.75,3,120,linestyle=':',color=ink,linewidth=2)
ax.text(13,.785,r'Shown slice $T_0=3/4$',ha='center',fontsize=10)
ax.text(42.4,.12,'Target',ha='center',color='white',weight='bold')
ax.text(14,.36,r'Unchanged field: $6\leq |x|\leq60$',ha='center',fontsize=10)
ax.set_xticks([3,6,30,60,120],['3','6','30','60','120'])
ax.set_yticks([0,.25,.5,.75,1],['0','1/4','1/2','3/4','1'])
ax.set_xlabel(r'Original radius $|x|$ (logarithmic scale)');ax.set_ylabel(r'Original time $t$')
ax.set_title('Annular estimate (5.4)\n'+r'$\nu=T=1,\ C_0=2,\ r_-=3,\ r_+=120$',fontsize=12,pad=14)
ax=axes[1]
ax.set_xlim(-2,67);ax.set_yscale('symlog',linthresh=2,linscale=.8);ax.set_ylim(-.1,2450)
ax.add_patch(Rectangle((0,0),64,2000,fill=False,edgecolor=ink,linewidth=1.5))
ax.add_patch(Rectangle((0,50),64,50,color=blue,alpha=.75))
ax.add_patch(Rectangle((32,0),32,2000,color=gray,alpha=.6))
ax.add_patch(Rectangle((0,1),32,1,color=green,alpha=.9))
ax.hlines(80,0,64,linestyle=':',color=ink,linewidth=2)
ax.text(15,115,r'Shown slice $T_0=1/25$',ha='center',fontsize=10)
ax.text(16,1.48,'Target',ha='center',color='white',weight='bold')
ax.text(48,5,'Cutoff\nderivatives',ha='center',fontsize=10)
ax.set_xticks([0,32,64]);ax.set_yticks([0,1,2,50,100,2000],['0','1','2','50','100','2000'])
ax.set_xlabel(r'Original radius $|x|$');ax.set_ylabel(r'$t/\tau$ (linear to 2, logarithmic above 2)')
ax.set_title('Gaussian estimate (6.5)\n'+r'$\nu=T=1,\ r=64,\ \tau=1/2000,\ \varepsilon=1/4000$',fontsize=12,pad=14)
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
 ax.grid(alpha=.15)
fig.legend(handles=[Patch(color=green,label='Target integral'),Patch(color=gray,label='Spatial cutoff derivatives'),Patch(color=blue,label='Time-slice selection interval'),Line2D([0],[0],color=ink,linestyle=':',label='Example admissible time slice')],loc='outside lower center',ncol=2,frameon=False)
fig.suptitle('Where the weighted estimates receive their data',fontsize=17,weight='bold')
fig.savefig(ROOT/'weighted-heat-regions.png',dpi=155)
fig.savefig(ROOT/'weighted-heat-regions.svg')
print('Saved exact annular and Gaussian region diagrams.')

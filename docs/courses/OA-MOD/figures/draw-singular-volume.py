"""Reproduce the exact two-dimensional example accompanying GV5. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from fractions import Fraction

OUT=Path(__file__).resolve().parent
epsilon=Fraction(1,4)
width=1+epsilon
height=epsilon
assert width*height==Fraction(5,16)
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','svg.hashsalt':'oa-mod-gv5-singular-volume-v1','font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,3,figsize=(11.4,4),constrained_layout=True)
titles=[r'Source $E=[0,1]^2$',r'$T(x,y)=(x,0)$',r'$\phi_{1/4}(x,y)=(5x/4,y/4)$']
for ax,title in zip(axes,titles):
 ax.set_aspect('equal');ax.set_xlim(-.12,1.4);ax.set_ylim(-.15,1.2)
 ax.set_xticks([0,1,1.25],['0','1','5/4']);ax.set_yticks([0,.25,1],['0','1/4','1'])
 ax.spines[['top','right']].set_visible(False)
 ax.set_title(title,pad=15);ax.set_xlabel('First coordinate');ax.set_ylabel('Second coordinate')
 ax.grid(alpha=.15,zorder=0)
axes[0].add_patch(Rectangle((0,0),1,1,facecolor='#cae6f1',edgecolor='#145a75',linewidth=2,zorder=2))
axes[0].text(.5,.5,'Area = 1',ha='center',va='center')
axes[1].plot([0,1],[0,0],color='#145a75',linewidth=4,zorder=3)
axes[1].scatter([0,1],[0,0],s=24,color='#145a75',zorder=4)
axes[1].text(.5,.55,'Area = 0\nDeterminant = 0',ha='center',va='center')
axes[2].add_patch(Rectangle((0,0),float(width),float(height),facecolor='#cdebd7',edgecolor='#237145',linewidth=2,zorder=2))
axes[2].text(.625,.6,'Area = 5/16\nDeterminant = 5/16',ha='center',va='center')
fig.savefig(OUT/'singular-volume-example.svg',metadata={'Date':None,'Creator':'OA-MOD programme proof illustration'})
fig.savefig(OUT/'singular-volume-example.png',dpi=160,metadata={'Software':'OA-MOD programme proof illustration'})
plt.close(fig)

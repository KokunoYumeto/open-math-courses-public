"""Exact phase-congruence support illustration; original TR-BAKER-10 figure, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

folder=Path(__file__).resolve().parent
destination=folder.parent/'figures' if folder.name=='figure_sources' else folder
destination.mkdir(exist_ok=True)
support=[(x,y) for x in range(-2,3) for y in range(-2,3) if (x+y+1)%3==0]
red=[p for p in support if (sum(p)+1)%6==0]
blue=[p for p in support if (sum(p)-2)%6==0]
assert len(support)==8 and len(red)==len(blue)==4
assert all((2*sum(p)+2)%6==0 for p in support)
fig,axes=plt.subplots(1,2,figsize=(13.2,6.4),gridspec_kw={'width_ratios':[1,1.35]})
fig.subplots_adjust(left=.07,right=.975,bottom=.30,top=.73,wspace=.26)
fig.suptitle('The divided support splits into two phase classes over the original field',fontsize=21,y=.97)
ax=axes[0]
ax.scatter([p[0] for p in red],[p[1] for p in red],s=115,color='#c04b27',label='b = 0: sum = -1')
ax.scatter([p[0] for p in blue],[p[1] for p in blue],s=115,color='#2c71a7',label='b = 1: sum = 2 mod 6')
ax.scatter([-1],[0],s=210,facecolors='none',edgecolors='black',linewidths=1.5)
ax.annotate(r'$\lambda_0=(-1,0)$',xy=(-1,0),xytext=(-.76,.32),fontsize=17)
ax.set_aspect('equal');ax.set_xlim(-2.6,2.6);ax.set_ylim(-2.6,2.6)
ax.set_xticks(range(-2,3));ax.set_yticks(range(-2,3))
ax.set_xlabel(r'$\lambda_1$',fontsize=18);ax.set_ylabel(r'$\lambda_2$',fontsize=18)
ax.tick_params(labelsize=16);ax.grid(alpha=.18);ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.set_title(r'$2(\lambda_1+\lambda_2)+2=0\ (\mathrm{mod}\ 6)$',fontsize=18,pad=15)
handles,labels=ax.get_legend_handles_labels()
fig.legend(handles,labels,loc='upper center',bbox_to_anchor=(.5,.90),ncol=2,fontsize=14)
right=axes[1];right.axis('off')
def box(y,height,color):
 right.add_patch(FancyBboxPatch((.035,y),.91,height,boxstyle='round,pad=.018',
                               transform=right.transAxes,facecolor=color,edgecolor='#75828e',linewidth=1))
box(.72,.20,'#f0f2f4')
right.text(.49,.86,r'$q=2,\ G_0=6,\ a_*=2,\ H=3$',ha='center',fontsize=18)
right.text(.49,.765,r'$u=-1+3b\ (\mathrm{mod}\ 6),\quad b=0,1$',ha='center',fontsize=18)
box(.36,.25,'#edf2f7')
right.text(.49,.54,r'$\beta=\zeta^3=i,\quad \beta^2=-1\in\mathbb{Q}$',ha='center',fontsize=18)
right.text(.49,.43,r'$\zeta^s\Sigma=Z_0+i^s Z_1=0,\quad Z_b\in\mathbb{Q}$',ha='center',fontsize=18)
box(.025,.21,'#f4efe6')
right.text(.49,.17,r'$s$ odd: $1,i^s$ independent over $\mathbb{Q}$',ha='center',fontsize=17)
right.text(.49,.075,r'$Z_0=0,\qquad Z_1=0$',ha='center',fontsize=20)
fig.text(.57,.13,'Retain the class containing a coefficient of minimum local valuation.',ha='center',fontsize=17)
fig.text(.57,.065,r'Its normalized phase is $\zeta^{s(u-u_0)}\in\{\pm1\}\subset\mathbb{Q}$.',ha='center',fontsize=18)
fig.savefig(destination/'phase-congruence-split.png',dpi=200)
plt.close(fig)

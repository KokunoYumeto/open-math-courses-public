"""Original diagram of the sign-action invariant monoid. Requires matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
out=Path(__file__).resolve().parent/'figures'
out.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(6.4,5.1),layout='constrained')
for a in range(7):
 for b in range(7):
  invariant=(a+b)%2==0
  ax.scatter(a,b,s=42 if invariant else 15,color='#156b9b' if invariant else '#c5cbd1',zorder=2)
for a,b,color,label,offset in [(2,0,'#ad401f','x²: (2,0)',(1.9,-.45)),(1,1,'#11794b','xy: (1,1)',(.65,1.42)),(0,2,'#7b4896','y²: (0,2)',(-.15,2.35))]:
 ax.annotate('',xy=(a,b),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.2,'color':color},zorder=3)
 ax.text(*offset,label,color=color,fontsize=11)
ax.set(xlim=(-.6,6.4),ylim=(-.6,6.65),xlabel='Exponent a in xᵃyᵇ',ylabel='Exponent b in xᵃyᵇ',xticks=range(7),yticks=range(7))
ax.set_aspect('equal')
ax.spines[['top','right']].set_visible(False)
ax.grid(color='#eef0f2',linewidth=.7)
ax.legend(handles=[Line2D([],[],color='#156b9b',marker='o',ls='',label='Invariant: a + b even'),Line2D([],[],color='#c5cbd1',marker='o',ls='',label='Changes sign: a + b odd')],loc='lower center',bbox_to_anchor=(.5,1.02),frameon=False,fontsize=10)
fig.savefig(out/'sign-monomials.png',dpi=170,metadata={'Software':None})
fig.savefig(out/'sign-monomials.svg',metadata={'Date':None,'Creator':None})
plt.close(fig)

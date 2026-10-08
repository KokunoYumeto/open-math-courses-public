from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'snc-laurent-pole-filtration.png'
OUT.parent.mkdir(parents=True,exist_ok=True)
fig,ax=plt.subplots(figsize=(8.8,5.8),dpi=180)
fig.patch.set_facecolor('#fbfaf4');ax.set_facecolor('#fbfaf4')
colors=['#203d4c','#177e89','#df7c35','#d3d4ce']
for n1 in range(-4,4):
    for n2 in range(-4,4):
        deficit=max(-n1-1,0)+max(-n2-1,0)
        ax.scatter(n1,n2,s=74,color=colors[min(deficit,3)],zorder=3)
ax.axvline(-1,color='#a6aca8',linestyle='--',linewidth=1)
ax.axhline(-1,color='#a6aca8',linestyle='--',linewidth=1)
ax.annotate('',xy=(-2,-1),xytext=(-1,-1),arrowprops={'arrowstyle':'->','color':'#bd382f','lw':2.2,'connectionstyle':'arc3,rad=-0.27'},zorder=5)
ax.annotate('',xy=(-1,-1),xytext=(-2,-1),arrowprops={'arrowstyle':'->','color':'#4c6db0','lw':2.2,'connectionstyle':'arc3,rad=-0.27'},zorder=5)
ax.text(-1.56,-0.62,r'$\partial_1:\ A_1-I$',fontsize=11,color='#98302a',ha='center')
ax.text(-1.54,-1.53,r'$z_1:\ F_1\to F_0$',fontsize=11,color='#36528c',ha='center')
ax.set(xlim=(-4.45,3.45),ylim=(-4.45,3.45),xticks=range(-4,4),yticks=range(-4,4),xlabel=r'Laurent exponent $n_1$',ylabel=r'Laurent exponent $n_2$')
ax.set_aspect('equal');ax.grid(alpha=.18)
ax.set_title(r'Pole filtration at a two-component boundary'+'\n'+r'$\nu(n)=\max(-n_1-1,0)+\max(-n_2-1,0)$',fontsize=14,pad=16)
handles=[Patch(color=colors[0],label=r'$\nu=0$ (in $F_0$)'),Patch(color=colors[1],label=r'$\nu=1$ (added in $F_1$)'),Patch(color=colors[2],label=r'$\nu=2$ (added in $F_2$)'),Patch(color=colors[3],label=r'$\nu>2$ (outside $F_2$)')]
ax.legend(handles=handles,loc='upper left',bbox_to_anchor=(1.02,1),frameon=False,fontsize=10)
fig.text(.07,.03,'Shown exponent window: -4 to 3. The admitted region continues to the right and upward.\nAfter the derivative raises filtration degree, multiplication by z₁ lowers it; its symbol product is zero.',fontsize=9,color='#253944')
fig.subplots_adjust(left=.09,right=.72,bottom=.18,top=.84)
fig.savefig(OUT,facecolor=fig.get_facecolor())
plt.close(fig)
print(str(OUT))

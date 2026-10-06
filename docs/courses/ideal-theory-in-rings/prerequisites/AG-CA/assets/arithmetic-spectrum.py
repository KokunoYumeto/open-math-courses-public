"""Original schematic of arithmetic fibres; run beside the generated PNG."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(13, 6.8), dpi=160)
ax.set(xlim=(0,13), ylim=(0,7))
ax.axis('off')
fig.patch.set_facecolor('#fafaf7')
ax.text(.5,6.55,'One ring, fibres over different fields',fontsize=19,weight='bold',color='#173a45')
ax.text(.5,6.12,'Selected points of Spec Z[x]: colored arrows specialize; gray arrows project.',fontsize=12,color='#43545a')
cols=[(2.3,r'Generic fibre: $\mathrm{Spec}\,\mathbb{Q}[x]$',r'$(0)$',r'$(x)$'),
      (6.6,r'Closed fibre: $\mathrm{Spec}\,\mathbb{F}_2[x]$',r'$(2)$',r'$(2,x)$'),
      (10.6,r'Closed fibre: $\mathrm{Spec}\,\mathbb{F}_3[x]$',r'$(3)$',r'$(3,x)$')]
for x,title,top,bottom in cols:
    ax.add_patch(plt.Rectangle((x-1.8,2.5),3.6,3.2,facecolor='#eaf0ef',edgecolor='#89a5ac',lw=1.2))
    ax.text(x,5.32,title,fontsize=12,ha='center',color='#173a45')
    for y,label in [(4.65,top),(3.1,bottom)]:
        ax.plot(x,y,'o',color='#173a45',ms=7)
        ax.text(x+.18,y,label,fontsize=16,va='center')
    ax.annotate('',xy=(x,3.25),xytext=(x,4.48),arrowprops={'arrowstyle':'->','color':'#247f80','lw':2})
    ax.annotate('',xy=(x,1.45),xytext=(x,2.33),arrowprops={'arrowstyle':'->','color':'#64747a','lw':1.4})
    ax.text(x,1.12,[r'$(0)$',r'$(2)$',r'$(3)$'][cols.index((x,title,top,bottom))],fontsize=16,ha='center')
ax.text(.5,1.55,r'Projection to $\mathrm{Spec}\,\mathbb{Z}$',fontsize=12,color='#43545a')
ax.annotate('',xy=(6.43,2.97),xytext=(2.3,2.95),arrowprops={'arrowstyle':'->','color':'#af6237','lw':1.5,'connectionstyle':'arc3,rad=.19'})
ax.annotate('',xy=(10.42,2.97),xytext=(2.3,2.91),arrowprops={'arrowstyle':'->','color':'#af6237','lw':1.5,'connectionstyle':'arc3,rad=.13'})
ax.text(.5,.42,'Only selected points and specializations are drawn. No Euclidean geometry or exhaustive list is asserted.',fontsize=11,color='#43545a')
fig.tight_layout(pad=.4)
fig.savefig(Path(__file__).with_suffix('.png'),facecolor=fig.get_facecolor(),metadata={'Software':None})
plt.close(fig)

"""Original CC0 exact tensor-site schematic for the reindexing proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
matplotlib.rcParams['svg.hashsalt']='oa-classify-relative-reindexing-v1'
fig,ax=plt.subplots(figsize=(6.3,7));fig.patch.set_facecolor('#faf8f4')
ax.set_facecolor('#faf8f4');ax.set_xlim(0,6.3);ax.set_ylim(0,7);ax.axis('off')
ax.text(3.15,6.55,'Move the partition;\nkeep the prescribed coefficient fixed',
 ha='center',fontsize=14)
positions=[1.05,3.7,5.25];labels=[r'$n$',r'$2n$',r'$2n+1$']
for y in [4.8,2.65]:
 for x,label in zip(positions,labels):
  ax.add_patch(Rectangle((x-.48,y-.32),.96,.64,facecolor='#e5e8e8',edgecolor='#475e68'))
  ax.text(x,y-.62,label,ha='center',fontsize=14)
ax.text(.3,5.5,'Before',fontsize=14,weight='bold')
ax.text(.3,3.35,'After',fontsize=14,weight='bold')
ax.text(1.05,4.8,r'$p_n,\ x_n$',ha='center',fontsize=14)
ax.text(1.05,2.65,r'$x_n$',ha='center',fontsize=14)
ax.text(3.7,2.65,r'$p_{2n}$',ha='center',fontsize=14)
ax.text(5.25,2.65,r'$p_{2n+1}$',ha='center',fontsize=14)
ax.annotate('',xy=(3.7,3.12),xytext=(1.45,4.4),
 arrowprops={'arrowstyle':'->','color':'#af5e15','lw':2})
ax.text(2.8,4.05,r'$k(n)=2n$',color='#af5e15',ha='center',fontsize=14)
ax.annotate('',xy=(5.2,3.02),xytext=(3.85,3.02),
 arrowprops={'arrowstyle':'->','color':'#11647d','lw':1.8})
ax.text(4.55,3.21,r'$\beta$',color='#11647d',ha='center',fontsize=14)
ax.text(3.15,1.3,r'$[p_{2n},x_n]=0,\qquad \tau(p_{2n})=1/2$',
 ha='center',fontsize=14)
ax.text(3.15,.85,r'$\|\beta(p_{2n})-p_{2n}\|_2=1/\sqrt{2}$',
 ha='center',fontsize=14)
ax.text(3.15,.3,'The shift defect remains positive.',
 ha='center',fontsize=12)
fig.tight_layout(pad=.6)
out=Path(__file__).resolve().parent
fig.savefig(out/'relative-tower-reindexing.svg',metadata={'Date':'2026-10-02','Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 diagram'})
fig.savefig(out/'relative-tower-reindexing.png',dpi=160,metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 diagram'})

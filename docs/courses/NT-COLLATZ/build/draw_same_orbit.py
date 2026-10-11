"""Exact marked visits from Lemma7. Schematic spacing, not elapsed distance."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(9,4.2));ax.set_xlim(-.4,5.4);ax.set_ylim(-1.3,2.9);ax.axis('off')
positions=[0,1,2,3,4,5];states=[56,7,11,17,13,5]
for i in range(5):
    ax.add_patch(FancyArrowPatch((i+.17,1.2),(i+1-.17,1.2),arrowstyle='->',mutation_scale=14,
      color='#b26420' if i>=3 else '#21647a',linewidth=2))
for x,state in zip(positions,states):
    ax.text(x,1.2,str(state),ha='center',va='center',fontsize=15,
       bbox=dict(boxstyle='round,pad=.3',facecolor='#fff4e9' if x>=3 else '#eef6fa',edgecolor='#52636d'))
ax.text(0,2.55,'One orbit, two possible first targets',fontsize=17,weight='bold')
ax.text(0,2.05,'The marked odd visit is 17. Continue to target 5, or truncate at target 7.',fontsize=10.5)
for x,odd,st,ct in [(1,0,3,3),(2,1,4,5),(3,2,5,7),(4,3,7,10),(5,4,10,14)]:
    ax.text(x,.65,'odd index '+str(odd),ha='center',fontsize=9)
    ax.text(x,.24,'T time '+str(st),ha='center',fontsize=9)
    ax.text(x,-.14,'C time '+str(ct),ha='center',fontsize=9)
ax.text(.5,1.61,'3 halvings',ha='center',fontsize=9)
ax.text(3,1.70,'mark',ha='center',color='#8d4e18',fontsize=11,weight='bold')
ax.text(1,-.73,'target 7: stop here',ha='center',color='#21647a',fontsize=10)
ax.text(4.15,-.73,'target 5: 2 more odd returns',ha='center',color='#8d4e18',fontsize=10)
ax.text(0,-1.12,'Continuation: 5 shortcut steps, 7 ordinary steps; maximum 52, bounded by 136.',fontsize=10.5)
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1]/'figures/same-orbit-joining.svg',bbox_inches='tight')
plt.close(fig)


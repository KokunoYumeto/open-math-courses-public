from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'svg.hashsalt':'oa-classify-unitary-two-cocycle-tower','font.family':'DejaVu Sans'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,9.4));fig.subplots_adjust(0,0,1,1);ax.set_xlim(0,6.5);ax.set_ylim(0,9.4);ax.axis('off')
ax.text(.3,9.1,'Where the two-cocycle cancels',fontsize=21,weight='bold',va='top')
ax.text(.3,8.55,'R = {0, 1, 2, 3, 4},   g = 1',fontsize=17)
ax.text(.3,8.1,'Target s uses source g⁻¹s = s − 1.',fontsize=14)
ys=[7.1,6.15,5.2,4.25,3.3]
for s,y in enumerate(ys):
 color='#f9e4e1' if s==0 else '#e3f1eb'
 ax.add_patch(FancyBboxPatch((1.3,y-.27),4.6,.6,boxstyle='round,pad=.04',facecolor=color,edgecolor='#465d71',linewidth=1.2))
 ax.text(1.5,y+.04,f'Target {s}',fontsize=16,weight='bold',va='center')
 ax.text(3.35,y+.04,'bad: source −1' if s==0 else f'good: source {s-1}',fontsize=13,va='center')
 if s>0:ax.annotate('',xy=(.86,y+.04),xytext=(.86,ys[s-1]+.04),arrowprops={'arrowstyle':'->','color':'#3b6c91','lw':1.8})
ax.text(.3,5.2,'g',fontsize=17,color='#3b6c91')
ax.add_patch(FancyBboxPatch((1.3,1.95),4.6,.6,boxstyle='round,pad=.04',facecolor='#f9e4e1',edgecolor='#465d71',linewidth=1.2))
ax.text(1.5,2.28,'Uncovered E*',fontsize=16,weight='bold',va='center')
ax.text(.3,1.52,'Six equal weights: δ = 1/6, boundary = 1/6.',fontsize=13.7)
ax.text(.3,.98,r'$\|U_g\sigma_g(U_h)c(g,h)-U_{gh}\|_2$'+'\n'+r'$\leq 2\sqrt{\delta+B_g^{\mathrm{R}}}=2\sqrt{1/3}$',fontsize=18,va='center',linespacing=1.7)
ax.text(.3,.12,'Proved upper bound; working proof (5.1)–(5.5).',fontsize=12)
fig.savefig(out/'unitary-two-cocycle-tower.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI'})
fig.savefig(out/'unitary-two-cocycle-tower.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI'})
plt.close(fig)

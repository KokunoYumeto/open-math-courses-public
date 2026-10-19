from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'svg.hashsalt':'oa-classify-controlled-cohomology-tower','font.family':'DejaVu Sans'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,9.4));fig.subplots_adjust(0,0,1,1);ax.set_xlim(0,6.5);ax.set_ylim(0,9.4);ax.axis('off')
ax.text(.3,9.1,'Correct a normalizer cocycle',fontsize=21,weight='bold',va='top')
ax.text(.3,8.5,'R = {0, 1, 2, 3, 4},   g = 1',fontsize=16)
for s,y in enumerate([7.6,6.78,5.96,5.14,4.32]):
 color='#f9e4e1' if s==0 else '#e3f1eb'
 ax.add_patch(FancyBboxPatch((.45,y-.45),5.55,.65,boxstyle='round,pad=.03',facecolor=color,edgecolor='#465d71'))
 ax.text(.7,y-.13,f'Target {s}',fontsize=16,weight='bold',va='center')
 ax.text(3.35,y-.13,'bad: source −1' if s==0 else f'source {s-1} → coefficient C{s}',fontsize=12.5,va='center')
ax.add_patch(FancyBboxPatch((.45,3.05),5.55,.65,boxstyle='round,pad=.03',facecolor='#f9e4e1',edgecolor='#465d71'))
ax.text(.7,3.38,'Uncovered E*',fontsize=16,weight='bold',va='center')
ax.text(.3,2.6,r'$Z=E_*+\sum_s C_s E_s$',fontsize=21)
ax.text(.3,2.04,r'$C_1\beta_1(C_{s-1})=C_s$',fontsize=21)
ax.text(.3,1.48,'Six equal weights: bad mass = 1/3.',fontsize=14)
ax.text(.3,.88,r'$\|C_1-Z\beta_1(Z^*)\|_\varphi^{\sharp\,2}\leq 8/3$',fontsize=20)
ax.text(.3,.35,'Upper bound; projection scheme, not a free',fontsize=12)
ax.text(.3,.10,'Z-action on six points. Proof (3.3)–(3.6).',fontsize=12)
fig.savefig(out/'controlled-cohomology-tower.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI'})
fig.savefig(out/'controlled-cohomology-tower.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI'});plt.close(fig)

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-classify-two-sided-convergence-learner-v1'})
dest=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,13.5));fig.patch.set_facecolor('white');ax.set_xlim(0,6.5);ax.set_ylim(0,13.5);ax.axis('off')
ax.text(.2,13.05,'Both convergence\ndirections matter',fontsize=20,weight='bold',va='top')
ax.text(.2,11.85,'Finite cycle, n = 5',fontsize=15,weight='bold')
positions=[.65,1.85,3.05,4.25,5.45]
def arrow(x1,y1,x2,y2,color='#42749d',curve=0):
 ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='->',mutation_scale=15,color=color,lw=1.8,connectionstyle=f'arc3,rad={curve}'))
for j,x in enumerate(positions,1):
 ax.plot(x,10.85,'o',color='#254861');ax.text(x,10.5,fr'$e_{j}$',ha='center',fontsize=16)
 if j<5:arrow(x+.12,10.85,positions[j]-.12,10.85)
arrow(5.45,10.95,.65,10.95,color='#af574e',curve=.22)
ax.text(.2,10.,'The closing arrow moves outward\nas n grows.',fontsize=13,color='#913f36',va='top')
ax.text(.2,9.15,'Shift limit',fontsize=15,weight='bold')
for j,x in enumerate(positions,1):
 ax.plot(x,8.55,'o',color='#254861');ax.text(x,8.2,fr'$e_{j}$',ha='center',fontsize=16)
 if j<5:arrow(x+.12,8.55,positions[j]-.12,8.55)
arrow(5.58,8.55,6.05,8.55);ax.text(6.16,8.5,'…',fontsize=16)
ax.add_patch(Rectangle((.3,8.1),.7,.85,fill=False,ec='#af574e',lw=1.5))
ax.text(.2,7.6,r'$S e_j=e_{j+1},\quad S^*S=1$',fontsize=16)
ax.text(.2,7.12,r'$SS^*=1-e_{11}$',fontsize=16)
ax.text(.2,6.45,'Forward predual tests converge:',fontsize=14,weight='bold')
ax.text(.3,5.88,r'$q_n t q_n^*\longrightarrow S t S^*$',fontsize=17)
ax.text(.3,5.45,'in trace norm',fontsize=14)
ax.text(.2,4.78,'Inverse predual tests fail:',fontsize=14,weight='bold')
ax.text(.3,4.22,r'$q_n^*e_{11}q_n=e_{nn}$',fontsize=17)
ax.text(.3,3.67,r'$\|e_{nn}-e_{mm}\|_1=2\quad(n\ne m)$',fontsize=16)
ax.text(.2,2.95,'Compression loses multiplication:',fontsize=14,weight='bold')
ax.text(.3,2.38,r'$S^*e_{12}S=0$',fontsize=17)
ax.text(.3,1.83,r'$S^*e_{12}^*e_{12}S=e_{11}\ne0$',fontsize=16)
ax.text(.2,.85,'Proof (6.1)–(6.3). Basis-arrow schematic.\nNo infinite numerical convergence claim.',fontsize=11,va='top')
fig.savefig(dest/'two-sided-convergence-obstruction.svg',bbox_inches='tight',metadata={'Date':None})
fig.savefig(dest/'two-sided-convergence-obstruction.png',dpi=160,bbox_inches='tight',metadata={'Software':'OA-CLASSIFY reproducible figure'})
plt.close(fig)

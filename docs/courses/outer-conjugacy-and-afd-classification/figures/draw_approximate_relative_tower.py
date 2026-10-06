"""CC0: exact finite-corner geometry and unequal boundary trace weights."""
from pathlib import Path
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
matplotlib.rcParams.update({'svg.hashsalt':'oa-classify-approximate-relative-tower','font.size':12,'font.family':'DejaVu Sans'})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(6,9.5),facecolor='#faf8f4',gridspec_kw={'height_ratios':[1.1,1]})
a=axes[0];a.set_aspect('equal');a.set_xlim(-.2,1.6);a.set_ylim(-.22,1.25)
a.axhline(0,color='#52616a',lw=1);a.axvline(0,color='#52616a',lw=1)
point=(.5,np.sqrt(3)/2)
for endpoint,color in [((1,0),'#24556d'),(point,'#a75c16')]:
 a.annotate('',xy=endpoint,xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':color})
a.plot([1,.5],[0,0],color='#376d84',lw=5,alpha=.55)
a.plot([.5,.5],[0,point[1]],color='#d19045',lw=4,alpha=.7)
a.plot([.5],[0],'o',color='#24556d');a.plot([.5],[point[1]],'o',color='#a75c16')
a.text(1.03,-.11,r'$u=e:\ (1,0)$');a.text(.54,.94,r'$ve:\ (1/2,\sqrt{3}/2)$')
a.text(.61,.36,r'$(1-e)ve$');a.text(.29,-.13,r'$a=eve$')
a.set_title('Complete the compressed corner',pad=20);a.set_xticks([]);a.set_yticks([])
a.text(.5,-.31,r'$\|ve-u\|_2^2=1/2\ \leq\ 3/4=\|[v,e]\|_2^2$',ha='center',transform=a.transAxes)
for spine in a.spines.values():spine.set_visible(False)
b=axes[1];b.set_xlim(-.5,3.5);b.set_ylim(-.95,2.35);b.set_aspect('equal');b.axis('off')
for j in range(3):
 b.add_patch(Rectangle((j,1),.9,.75,facecolor='#7fbbca' if j==0 else '#e5a04b',edgecolor='#3c5965'))
 b.text(j+.45,1.38,r'$P_'+str(j)+'$',ha='center',va='center')
b.text(.45,.75,r'$E_{1,0}$',ha='center');b.text(1.95,.75,r'$E_{1,1}=P_1+P_2$',ha='center')
b.annotate('',xy=(1.45,1.98),xytext=(.45,1.98),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#3c5965'})
b.text(.95,2.13,r'$\gamma_1$',ha='center')
b.text(1.5,.33,r'$\tau(P_j)=1/3,\quad\delta=0$',ha='center')
b.text(1.5,-.04,r'$B_1^{\mathrm{L}}=2/3,\quad B_1^{\mathrm{R}}=1/3$',ha='center')
b.text(1.5,-.42,r'$\eta_1=\|P_1-(P_1+P_2)\|_2=1/\sqrt{3}$',ha='center')
b.set_title('Equal boundary counts; unequal trace weights',pad=18)
fig.subplots_adjust(hspace=.48,top=.95,bottom=.07,left=.08,right=.94)
metadata={'Creator':'OA-CLASSIFY Writing AI','Date':'2026-10-01','Description':'Lemma 1.1 at rotation pi/3; Lemma 3.2 for unequal levels in the three-cycle.'}
fig.savefig(out/'approximate-corner-and-weighted-boundaries.svg',metadata=metadata)
fig.savefig(out/'approximate-corner-and-weighted-boundaries.png',dpi=150,metadata={'Software':'OA-CLASSIFY Writing AI','Description':metadata['Description']})
plt.close(fig)

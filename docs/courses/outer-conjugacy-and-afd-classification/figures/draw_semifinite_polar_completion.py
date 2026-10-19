from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams.update({'svg.hashsalt':'oa-classify-semifinite-polar-completion','font.family':'DejaVu Sans'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,9.4));fig.subplots_adjust(0,0,1,1);ax.set_xlim(0,6.5);ax.set_ylim(0,9.4);ax.axis('off')
ax.text(.3,9.1,'Complete the polar part',fontsize=23,weight='bold',va='top')
ax.text(.3,8.5,'Semifinite projection supports',fontsize=16)
def box(x,y,w,h,label,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03',facecolor=color,edgecolor='#465d71',linewidth=1.2))
 ax.text(x+w/2,y+h/2,label,fontsize=19,ha='center',va='center')
box(.45,6.4,2.15,1.15,r'$p$', '#e6edf5');box(3.9,6.4,2.15,1.15,r'$r=vpv^*$', '#e6edf5')
ax.annotate('',xy=(3.75,6.98),xytext=(2.75,6.98),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#3b6c91'});ax.text(3.25,7.32,r'$v$',fontsize=20,ha='center')
ax.text(.3,5.95,'Remove a tail with small state mass:',fontsize=14)
box(.45,4.9,2.15,.65,r'$t$', '#f9e4e1');box(3.9,4.9,2.15,.65,r'$vtv^*$', '#f9e4e1')
ax.text(3.25,4.38,r'$\varphi(t)+\varphi(vtv^*)<1/k$',fontsize=20,ha='center')
box(.45,2.85,2.15,1.05,r'$P=p-t$', '#e3f1eb');box(3.9,2.85,2.15,1.05,r'$Q=r-vtv^*$', '#e3f1eb')
ax.annotate('',xy=(3.75,3.4),xytext=(2.75,3.4),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#285e47'});ax.text(3.25,3.74,r'$vP$',fontsize=19,ha='center')
ax.text(.3,2.34,'Match the infinite-trace complements:',fontsize=14)
ax.text(3.25,1.84,r'$b^*b=1-P,\quad bb^*=1-Q$',fontsize=20,ha='center')
ax.text(3.25,1.17,r'$u=vP+b\quad\mathrm{unitary}$',fontsize=23,ha='center')
ax.text(.3,.58,'Error supported on 1 − P and 1 − Q.',fontsize=14)
ax.text(.3,.18,'Support scheme; proof (2.3)–(2.5).',fontsize=12)
fig.savefig(out/'semifinite-polar-completion.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI'})
fig.savefig(out/'semifinite-polar-completion.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI'});plt.close(fig)

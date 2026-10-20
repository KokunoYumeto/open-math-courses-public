"""Original exact diagrams for root orbits, nullcone matching and straightening."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Arc
out=Path(__file__).resolve().parent/'figures';out.mkdir(exist_ok=True)
def save(fig,name):
 fig.savefig(out/(name+'.png'),dpi=170,metadata={'Software':None})
 fig.savefig(out/(name+'.svg'),metadata={'Date':None,'Creator':None})
 plt.close(fig)

fig,ax=plt.subplots(figsize=(10,4.2),layout='constrained')
ax.set(xlim=(-.4,9.4),ylim=(-.4,4));ax.axis('off')
ax.text(4.5,3.65,'One unordered set of four roots, six cross-ratios',ha='center',fontsize=15,color='#173c4d')
entries=[(r'$\lambda$',r'$3$'),(r'$1/\lambda$',r'$1/3$'),(r'$1-\lambda$',r'$-2$'),(r'$1/(1-\lambda)$',r'$-1/2$'),(r'$\lambda/(\lambda-1)$',r'$3/2$'),(r'$(\lambda-1)/\lambda$',r'$2/3$')]
for i,(formula,value) in enumerate(entries):
 x=(i%3)*3.2;y=2.15-(i//3)*1.22
 ax.add_patch(FancyBboxPatch((x,y),2.6,.84,boxstyle='round,pad=.1',facecolor='#edf5f8',edgecolor='#356277'))
 ax.text(x+1.3,y+.55,formula,ha='center',fontsize=13)
 ax.text(x+1.3,y+.19,value,ha='center',fontsize=12,color='#a13c23')
ax.text(4.5,.3,r'Every displayed value gives $J=\frac{4}{27}\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}=\frac{343}{243}$.',ha='center',fontsize=13)
ax.text(4.5,-.15,'Example: roots 0, 1, 3 and infinity. Changing their order gives the six values.',ha='center',fontsize=10)
save(fig,'cross-ratio-orbit')

fig,ax=plt.subplots(figsize=(10,4.4),layout='constrained')
ax.set(xlim=(.1,6.9),ylim=(-.4,3.9));ax.axis('off')
ax.text(3.5,3.55,'Two copies of each factor, paired six positions apart',ha='center',fontsize=15,color='#173c4d')
colors=['#297a97']*6+['#bd5a26']*4+['#578246']*2
slots=[1,1,2,2,3,3,4,4,5,5,6,6]
for r in range(6):
 x=r+1
 ax.plot([x,x],[1.05,2.5],color='#5d6870',lw=1.4)
 for position,y in [(r,2.5),(r+6,1.05)]:
  ax.scatter([x],[y],s=560,color=colors[position],zorder=3)
  ax.text(x,y,r'$\ell_'+str(slots[position])+'$',ha='center',va='center',color='white',fontsize=13)
  ax.text(x,y+(.35 if position<6 else -.37),'position '+str(position+1),ha='center',fontsize=9,color='#333333')
ax.text(3.5,3.03,'Root line A: 3 factors, 6 copies',ha='center',fontsize=11,color='#297a97')
ax.text(2.5,.33,'Root line B: 2 factors, 4 copies',ha='center',fontsize=10,color='#bd5a26')
ax.text(5.5,.33,'Root line C: 1 factor, 2 copies',ha='center',fontsize=10,color='#578246')
ax.text(3.5,-.12,r'$M=[14]^2[25]^2[36]^2\ne0$: every factor slot has degree two.',ha='center',fontsize=13)
save(fig,'root-matching')

fig,axes=plt.subplots(1,3,figsize=(11,3.8),layout='constrained')
panels=[([(1,4),(2,3)],r'$[14][23]$','Nonstandard columns'),([(1,3),(2,4)],r'$[13][24]$','Standard columns'),([(1,2),(3,4)],r'$[12][34]$','Standard columns')]
for ax,(pairs,label,title) in zip(axes,panels):
 ax.set(xlim=(.65,4.35),ylim=(-.55,2.65));ax.axis('off')
 for j,(a,b) in enumerate(pairs):
  width=b-a
  ax.add_patch(Arc(((a+b)/2,.3),width,width,theta1=0,theta2=180,lw=2,color=['#297a97','#bd5a26'][j]))
 ax.plot([1,4],[.3,.3],color='#a3adb4',lw=.9)
 for j in range(1,5):
  ax.scatter(j,.3,color='#173c4d',s=28,zorder=3)
  ax.text(j,.04,str(j),ha='center',fontsize=11)
 ax.text(2.5,2.38,title,ha='center',fontsize=12,color='#173c4d')
 ax.text(2.5,-.27,label,ha='center',fontsize=15)
fig.suptitle(r'Integral straightening: $[14][23]=[13][24]-[12][34]$',fontsize=16,color='#173c4d')
save(fig,'bracket-straightening')

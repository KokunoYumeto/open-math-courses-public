"""Original course figures. CC0 for code and geometry; rendered font glyphs retain their licences."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
out=Path(__file__).resolve().parent;out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','savefig.facecolor':'white'})
fig,axs=plt.subplots(1,3,figsize=(12,4),layout='constrained')
titles=[r'Standard monomials of $I$',r'Box for $(x^2,y^3)$',r'Box for $(x,y^4)$']
for j,ax in enumerate(axs):
 for a in range(3):
  for b in range(5):
   keep=(a<2 and b<3) or (a==0 and b<4) if j==0 else ((a<2 and b<3) if j==1 else (a==0 and b<4))
   ax.add_patch(Rectangle((a-.42,b-.42),.84,.84,facecolor=('#276a92' if keep else '#e7ecef'),edgecolor='white'))
   if keep: ax.text(a,b,'1' if a==b==0 else (('x' if a==1 else ('' if a==0 else f'x^{a}'))+('y' if b==1 else ('' if b==0 else f'y^{b}'))),ha='center',va='center',color='white',fontsize=11)
 ax.set(xlim=(-.6,2.6),ylim=(-.6,4.6),xticks=range(3),yticks=range(5),xlabel='exponent of x',ylabel='exponent of y',title=titles[j]);ax.set_aspect('equal')
fig.savefig(out/'monomial-boxes.png',dpi=180);fig.savefig(out/'monomial-boxes.svg');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
ax=axs[0]; pts=[(-1,0),(0,1),(1,0)]
labels=[r'$(x)$',r'$(x,y)$',r'$(y)$']
for a,b in [(0,1),(1,2)]: ax.plot([pts[a][0],pts[b][0]],[pts[a][1],pts[b][1]],color='#276a92',lw=3)
for p,l in zip(pts,labels): ax.scatter(*p,s=180,color='#276a92');ax.text(p[0],p[1]+.16,l,ha='center')
ax.set(xlim=(-1.6,1.6),ylim=(-.4,1.6),title='Comparable primes join into one group');ax.axis('off')
ax=axs[1];ax.plot([-1.5,1.5],[0,0],lw=3,color='#276a92');ax.plot([0,0],[-1.3,1.3],lw=3,color='#ad5833');ax.scatter(1,1,s=130,color='#477b48');ax.text(1.05,1.1,'(1,1)',fontsize=12)
ax.text(-1.4,.17,'axes: one connected piece');ax.text(.35,-.7,'point: second piece');ax.set(xlim=(-1.7,1.7),ylim=(-1.4,1.5),title='Incomparable axes can still meet');ax.set_aspect('equal');ax.axis('off')
fig.savefig(out/'two-kinds-of-separation.png',dpi=180);fig.savefig(out/'two-kinds-of-separation.svg');plt.close(fig)

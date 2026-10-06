"""Exact boundary model and zero-count circles, with explicitly numerical sample zeros. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,'svg.fonttype':'none'})
fig,axs=plt.subplots(2,1,figsize=(7.5,11.5),layout='constrained')
ax=axs[0];t=np.linspace(0,1,801)
ax.plot(t,np.sqrt(t),color='#176785',lw=2.5,label=r'$\tau=+\sqrt{t}$')
ax.plot(t,-np.sqrt(t),color='#a34c22',lw=2.5,label=r'$\tau=-\sqrt{t}$')
ax.plot(0,0,'o',color='#263442',ms=7)
ax.axvline(0,color='#909aa1',lw=1);ax.axhline(0,color='#ddd',lw=1)
ax.annotate('Double root at the boundary',(0,0),xytext=(.2,.08),
            arrowprops={'arrowstyle':'->'},fontsize=13)
ax.text(.58,-.15,r'$p=\tau^2-t,\quad H_p^2t=2$',ha='center',va='top',fontsize=14)
ax.set(xlim=(-.055,1.04),ylim=(-1.12,1.12),xlabel=r'$t$',ylabel=r'$\tau$',
       title='A noncharacteristic surface with a double root')
ax.legend(loc='upper left',frameon=False,fontsize=13);ax.spines[['top','right']].set_visible(False)
ax=axs[1];centers=np.array([-1+0j,.5+np.sqrt(3)*.5j,.5-np.sqrt(3)*.5j])
zeros=np.roots([.05,1,0,0,1])
for c in centers:
 ax.add_patch(Circle((c.real,c.imag),.2,fc='#dcebf6',ec='#34799e',lw=1.7))
ax.scatter(centers.real,centers.imag,c='#263442',marker='x',s=65,lw=2,zorder=3,label=r'$w^3+1=0$')
shown=zeros[np.abs(zeros)<2]
ax.scatter(shown.real,shown.imag,c='#b95521',s=24,zorder=4,label=r'$w^3+1+w^4/20=0$ (numerical)')
ax.axhline(0,color='#b6c0c6',lw=.8)
ax.axvline(0,color='#ddd',lw=.8)
ax.annotate('Each circle retains one zero',(.66,.86),xytext=(-1.18,1.29),
            arrowprops={'arrowstyle':'->'},fontsize=13)
ax.text(-1.16,-1.25,'Radius = 1/5.  The fourth perturbed zero is off-frame.',fontsize=11.5)
ax.set(xlim=(-1.3,1.28),ylim=(-1.36,1.45),xlabel=r'$\operatorname{Re}w$',ylabel=r'$\operatorname{Im}w$',
       title='Root counts persist without choosing branches')
ax.set_aspect('equal');ax.legend(loc='center',fontsize=10.5,frameon=False,bbox_to_anchor=(.56,.62))
ax.spines[['top','right']].set_visible(False)
for suffix in ['png','svg']:fig.savefig(HERE/f'boundary_roots_and_counts.{suffix}',dpi=170)
plt.close(fig)

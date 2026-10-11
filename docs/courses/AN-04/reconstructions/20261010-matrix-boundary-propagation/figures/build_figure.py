"""Exact principal rays, fiber polarization samples, and matrix Rayleigh energy."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'svg.fonttype':'none','axes.titlesize':14})
fig=plt.figure(figsize=(12.8,5.5),facecolor='#fafbfe')
grid=GridSpec(1,3,figure=fig,width_ratios=[1.1,.60,1.65],
              left=.055,right=.975,bottom=.19,top=.83,wspace=.35)
ax=fig.add_subplot(grid[0,0])
ax.set_title('Principal rays: physical time increases',loc='left',pad=16)
ax.axvline(0,color='#30384a',linewidth=2)
ax.plot([1,0],[-1,0],color='#295fc3',lw=3)
ax.plot([0,1],[0,1],color='#bd4d32',lw=3)
ax.annotate('',xy=(.36,-.36),xytext=(.70,-.70),
            arrowprops=dict(arrowstyle='->',color='#295fc3',lw=2))
ax.annotate('',xy=(.73,.73),xytext=(.37,.37),
            arrowprops=dict(arrowstyle='->',color='#bd4d32',lw=2))
ax.scatter([0],[0],s=45,color='#30384a',zorder=5)
ax.text(.44,-1.14,r'incoming: $t+x=0$',color='#295fc3',fontsize=11)
ax.text(.42,1.12,r'outgoing: $t-x=0$',color='#bd4d32',fontsize=11)
ax.text(.08,-.10,'value: out − in = 0',fontsize=10,va='top')
ax.set(xlim=(-.12,1.25),ylim=(-1.38,1.38),xlabel='normal position x',ylabel='time t')
ax.set_xticks([0,.5,1]);ax.set_yticks([-1,0,1])
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16)

fiber=fig.add_subplot(grid[0,1]);fiber.set_axis_off()
fiber.set_title('Fiber coordinates',fontsize=12,pad=16)
for t,yc in [(1,.83),(0,.50),(-1,.17)]:
    sub=fiber.inset_axes([.12,yc-.12,.62,.24])
    tt=np.linspace(0,2*np.pi,150)
    sub.plot(np.cos(tt),np.sin(tt),color='#b2bace',lw=1)
    sub.axhline(0,color='#d9deea',lw=.7);sub.axvline(0,color='#d9deea',lw=.7)
    sub.annotate('',xy=(np.cos(t),np.sin(t)),xytext=(0,0),
                 arrowprops=dict(arrowstyle='-|>',lw=2,color='#286b57'))
    sub.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),aspect='equal')
    sub.set_axis_off()
    fiber.text(.81,yc,f't = {t}',va='center',fontsize=10)
fiber.text(.50,-.06,r'$(\cos t,\sin t)$',ha='center',fontsize=12)
fiber.text(.50,-.14,'polarization, not velocity',ha='center',fontsize=10,color='#526078')

en=fig.add_subplot(grid[0,2])
angles=np.linspace(0,np.pi/2,400)
en.plot(angles,8+3*np.cos(2*angles),color='#6b45a1',lw=3)
en.axhline(5,color='#286b57',ls='--',lw=1.6)
en.scatter([0,np.pi/2],[11,5],color='#6b45a1',s=40,zorder=5)
en.set_title('Matrix damping on a unit complex vector',loc='left',pad=16)
en.set(xlim=(-.035,np.pi/2+.04),ylim=(4.5,11.6),ylabel=r'$a(\theta)^*h\,a(\theta)$',
       xlabel=r'$\theta$: mixing the orthonormal eigenvectors')
en.set_xticks([0,np.pi/4,np.pi/2],['0',r'$\pi/4$',r'$\pi/2$'])
en.set_yticks([5,8,11]);en.grid(alpha=.18)
en.text(.54,10.55,r'$8+3\cos(2\theta)$',fontsize=14,color='#6b45a1')
en.text(.13,5.23,'positive lower bound = 5',color='#286b57',fontsize=11)
en.spines[['top','right']].set_visible(False)
fig.suptitle('Coupling changes polarization; the scalar principal symbol fixes the rays',
             x=.055,y=.98,ha='left',fontsize=16,color='#24314a')
fig.text(.055,.055,'Exact examples: MP27–MP32. The matrix commutator and all operator remainders are retained in the proof.',
         fontsize=11,color='#526078')
out=Path(__file__).with_name('matrix-boundary-propagation.svg')
fig.savefig(out,metadata={'Date':None,'Creator':'AN-04 independent CC0 figure source'})
plt.close(fig)
print(out)

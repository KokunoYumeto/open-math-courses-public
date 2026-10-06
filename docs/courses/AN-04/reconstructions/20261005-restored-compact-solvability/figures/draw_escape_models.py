"""Exact base projections and coordinate covectors for the lesson's two models."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Wedge,Circle
plt.rcParams.update({'svg.fonttype':'path','font.size':12})
ROOT=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(6.5,10),layout='constrained')
ax=axes[0]
ax.add_patch(Rectangle((-1,-.75),2,1.5,facecolor='#dce7eb',edgecolor='#7a8e99',label='Compact set K'))
t=np.linspace(-1.6,1.6,300)
ax.plot(t,0*t,color='#147f86',lw=2.5,label='Characteristic base')
ax.annotate('',xy=(1.48,0),xytext=(1.16,0),arrowprops={'arrowstyle':'->','color':'#147f86','lw':2})
ax.quiver([0],[0],[0],[.3],angles='xy',scale_units='xy',scale=1,color='#b55831',width=.012)
ax.text(.08,.36,r'$\xi=(0,1)$',color='#954624')
ax.set(xlim=(-1.7,1.7),ylim=(-1.1,1.1),xlabel='x',ylabel='z',title=r'$p=\xi_x$: every line leaves K')
ax.legend(loc='lower left',fontsize=10)
ax=axes[1]
ax.add_patch(Wedge((0,0),1.75,0,360,width=.5,facecolor='#dce7eb',edgecolor='#7a8e99'))
for rr in [1,2]:ax.add_patch(Circle((0,0),rr,fill=False,ls=':',edgecolor='#9da9ae'))
th=np.linspace(0,2*np.pi,500)
ax.plot(1.5*np.cos(th),1.5*np.sin(th),color='#147f86',lw=2.5)
tt=np.array([0,2*np.pi/3,4*np.pi/3])
ax.quiver(1.5*np.cos(tt),1.5*np.sin(tt),.3*np.cos(tt),.3*np.sin(tt),
 angles='xy',scale_units='xy',scale=1,color='#b55831',width=.008)
ax.annotate('',xy=(1.5*np.cos(.58),1.5*np.sin(.58)),
 xytext=(1.5*np.cos(.38),1.5*np.sin(.38)),
 arrowprops={'arrowstyle':'->','color':'#147f86','lw':2,'connectionstyle':'arc3,rad=.12'})
ax.text(0,0,r'$r=3/2$'+'\n'+r'$P=D_\theta-ic$'+'\n'+r'$c\ne0$',ha='center',va='center')
ax.set(xlim=(-2.2,2.2),ylim=(-2.2,2.2),xlabel='x',ylabel='y',
 title=r'$p=x\eta_y-y\eta_x$: a trapped circle')
for ax in axes:
 ax.set_aspect('equal');ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Escape and a trapped characteristic',fontsize=16)
fig.supxlabel('Orange: covectors, scale 0.3 coordinate units per unit.\nTeal: flow direction.',fontsize=10)
fig.savefig(ROOT/'escape-and-circular-characteristic.svg')
fig.savefig(ROOT/'escape-and-circular-characteristic.png',dpi=150)
plt.close(fig)

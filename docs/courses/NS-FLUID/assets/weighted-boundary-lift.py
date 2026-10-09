"""Exact coordinate sections for NS-FLUID-11 equations 4.10–4.12."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
a,h=2.,1.
y=np.linspace(-1.5,1.5,600)
angle=np.linspace(0,2*np.pi,600)
levels=[.25,.5,.75,1.]
colors=['#2a9d8f','#267f9b','#435bab','#963d85']
fig,axes=plt.subplots(1,2,figsize=(12.5,5.8),layout='constrained')
for s,col in zip(levels,colors):
    axes[0].plot((a+s)*y/a,(a+s)*np.sqrt(1-y*y/a/a),color=col,
                 label=fr'$s={s:g}$')
    axes[1].plot(s*np.cos(angle),s*np.sin(angle),color=col)
axes[0].plot(y,a*np.sqrt(1-y*y/a/a),'k--',lw=1,label=r'$s=0$')
axes[0].set(xlabel=r'Original $x_1$',ylabel=r'Original $x_3$',
            title=r'Inner cap: $x_2=0$, $a=2$, $h=1$')
axes[0].legend(loc='lower center',ncols=3,fontsize=10)
axes[0].set_aspect('equal');axes[0].set_ylim(0,3.3)
axes[1].set(xlabel=r'Lift coordinate $z_1$',ylabel=r'Lift coordinate $z_2$',
            title=r'Four-dimensional lift: section $y=(0,0)$')
axes[1].set_aspect('equal')
axes[1].text(0,0,r'$s=\sqrt{z_1^2+z_2^2}$',ha='center',va='center',
             bbox={'facecolor':'white','edgecolor':'none','alpha':.9},fontsize=12)
for ax in axes:
    ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Distance to the physical boundary becomes a radial coordinate in the lift',fontsize=14)
fig.savefig(ROOT/'weighted-boundary-lift.png',dpi=170)
fig.savefig(ROOT/'weighted-boundary-lift.svg')
print('Saved exact coordinate sections; no solution field is simulated.')

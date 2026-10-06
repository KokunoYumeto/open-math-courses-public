"""Original CC0 illustration of exact Nyman–Beurling generators."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':22,'axes.titlesize':26,'axes.labelsize':24,'legend.fontsize':22})
fig,axes=plt.subplots(1,2,figsize=(12,5.3),layout='constrained')
colors=['#176b9a','#a34240']
for theta,color in zip([.5,.75],colors):
    breaks=sorted({.08,1.5}|{1/k for k in range(1,14) if .08<1/k<1.5}|{theta/k for k in range(1,14) if .08<theta/k<1.5})
    for i,(a,b) in enumerate(zip(breaks,breaks[1:])):
        midpoint=(a+b)/2
        value=theta*np.floor(1/midpoint)-np.floor(theta/midpoint)
        axes[0].plot([a,b],[value,value],color=color,lw=2.3,label=rf'$\theta={theta:g}$' if i==0 else None)
    x=np.linspace(1.001,3,350)
    axes[1].plot(x,theta/x,color=color,lw=2.3,label=rf'$\theta={theta:g}$')
axes[0].axvline(1,color='#777777',ls=':',lw=1.4)
axes[0].set(xlabel='$x$',ylabel=r'$f_\theta(x)$',title='Constrained generators',xlim=(.08,1.5),ylim=(-.85,.85))
axes[0].legend(loc='lower right')
axes[1].plot([1,3],[0,0],color='#222222',lw=2.3,label=r'$f_\theta=0$')
axes[1].set(xlabel='$x$',ylabel='Function value',title='Tail cancellation',xlim=(1,3),ylim=(-.08,.85))
axes[1].legend(loc='upper right')
for ax in axes:
    ax.grid(alpha=.18)
    ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)

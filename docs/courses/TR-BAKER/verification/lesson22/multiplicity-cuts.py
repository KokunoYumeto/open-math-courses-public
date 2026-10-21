"""Exact chart equations from Example 22.34; reproducible illustrative real slices."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
blue='#2563a6'; orange='#c45c16'; green='#39805c'
x=np.linspace(-.72,1.15,500)
ax=axes[0]
ax.plot(x,1+x,color=blue,lw=2.5,label=r'$F=y-1-x=0$')
ax.axhline(1,color=orange,lw=2.2,label=r'$\Delta F=y-1=0$')
ax.plot(x,np.exp(x),color=green,lw=1.9,ls='--',label=r'Flow $(t,e^t)$')
ax.scatter([0],[1],color='black',zorder=6,s=40)
ax.annotate('$(0,1)$\nlength 1',(0,1),xytext=(.25,.35),arrowprops={'arrowstyle':'->','color':'black'})
ax.set(xlabel='$x$',ylabel='$y$',xlim=(-.75,1.2),ylim=(.1,3.3),title='The point retained on the group')
ax.legend(loc='upper left',frameon=False,fontsize=11)
p=np.linspace(-.3,.3,500)
ax=axes[1]
ax.plot(p,p/(1-p),color=blue,lw=2.5,label=r'$F_h=q-pq-p=0$')
ax.axhline(0,color=orange,lw=2.2,label=r'$H_h=q-pq=0$ near $(0,0)$')
ax.scatter([0],[0],color='black',s=40,zorder=6)
ax.annotate('Boundary point\nlength 1',(0,0),xytext=(.06,-.24),arrowprops={'arrowstyle':'->','color':'black'})
ax.set(xlabel=r'$p=X_1/X_3$',ylabel=r'$q=X_2/X_3$',xlim=(-.31,.31),ylim=(-.32,.46),title='The second point in the boundary chart')
ax.legend(loc='upper left',frameon=False,fontsize=10)
fig.suptitle('Segre quadric: total intersection degree 2 = 1 + 1',fontsize=16)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=175)
plt.close(fig)

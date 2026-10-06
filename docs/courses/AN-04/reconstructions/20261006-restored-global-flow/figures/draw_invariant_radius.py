"""Exact model M=(-1,1)xR+, v=dt+log(2)r dr, invariant R=r*2**(-t)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'svg.fonttype':'path','font.size':12,'svg.hashsalt':'AN04-U040-invariant-radius'})
ROOT=Path(__file__).resolve().parent
fig,axes=plt.subplots(2,1,figsize=(6.5,8.5),layout='constrained')
t=np.linspace(-1,1,401);radii=[.5,1.,2.]
colors=['#20748a','#b75e26','#62599c']
for ax in axes:
 for x in [-1,0,1]:ax.axvline(x,color='#adb9bf',ls=':',lw=1)
 ax.spines[['top','right']].set_visible(False)
 ax.set(xlim=(-1.18,1.18),xlabel='Time t',xticks=[-1,-.5,0,.5,1])
 ax.grid(axis='y',alpha=.14)
for R,color in zip(radii,colors):
 r=R*2**t
 axes[0].plot(t,r,color=color,lw=2,label=f'R = {R:g}')
 axes[1].plot(t,0*t+R,color=color,lw=2,label=f'R = {R:g}')
 for ax,yy in [(axes[0],[R/2,2*R]),(axes[1],[R,R])]:
  ax.plot([-1,1],yy,'o',mec=color,mfc='white',ms=7,mew=1.8)
 axes[0].annotate('',xy=(.25,R*2**.25),xytext=(.02,R*2**.02),
                  arrowprops={'arrowstyle':'->','color':color,'lw':2})
 axes[1].annotate('',xy=(.25,R),xytext=(.02,R),
                  arrowprops={'arrowstyle':'->','color':color,'lw':2})
axes[0].set(ylim=(0,4.25),ylabel='Original radius r',title=r'Radial drift: $r(t)=R\,2^t$')
axes[1].set(ylim=(0,2.35),ylabel='Invariant radius R',title=r'New coordinates: $R=r\,2^{-t}$')
axes[0].legend(loc='upper left',fontsize=10)
axes[1].text(0,2.16,'Section t = 0',ha='center',fontsize=10)
fig.suptitle('Straightening the radial drift',fontsize=16)
fig.supxlabel('Open circles: endpoints outside M. Arrows: increasing time.\nProof: FG6–FG7 and the exact-model paragraph.',fontsize=10)
fig.savefig(ROOT/'invariant-radius-flow.svg',metadata={'Date':None})
fig.savefig(ROOT/'invariant-radius-flow.png',dpi=150,metadata={'Software':'AN04 exact mathematical model'})
plt.close(fig)

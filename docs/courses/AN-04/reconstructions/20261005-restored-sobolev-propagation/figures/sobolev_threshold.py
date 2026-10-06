"""Exact figure for SPA1 and unchanged Exercise 6.2; no source-book assets."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':16,'svg.fonttype':'none'})
fig,axes=plt.subplots(2,1,figsize=(7,8.4),layout='constrained')
ax=axes[0];ax.axhspan(-1.5,-.5,color='#d6e5cc')
ax.axhline(-.5,color='#ad4d39',ls='--',lw=2.2)
ax.text(0,-1.05,r'$1\otimes\delta_0\in H^r$ microlocally',ha='center')
ax.text(0,-.25,'Critical order excluded',ha='center',color='#8c3828')
ax.set(xlim=(-2,2),ylim=(-1.5,.15),xlabel='Time t along (t, 0; 0, 1)',ylabel='Sobolev order r',
 title='The same membership at every time')
ax.set_yticks([-1.5,-1,-.5,0]);ax.grid(alpha=.18)
ax=axes[1];R=np.geomspace(1,100,400)
for r,c in [(-1,'#176777'),(-.5,'#ad4d39'),(0,'#7355a3')]:
 y=np.log(R) if r==-.5 else np.expm1((2*r+1)*np.log(R))/(2*r+1)
 ax.plot(R,y,color=c,lw=2.5,label=f'r = {r:g}')
ax.set_yscale('symlog',linthresh=1)
ax.set(xscale='log',xlim=(1,100),ylim=(0,110),
 xlabel='Frequency radius R',ylabel=r'$J_r(R)$',
 title='Exact high-frequency comparison integrals')
ax.legend(loc='upper left');ax.grid(alpha=.2)
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'sobolev-propagation-threshold.svg',metadata={'Creator':'AN-04 course project'})
fig.savefig(out/'sobolev-propagation-threshold.png',dpi=170)
print('Saved exact characteristic membership and radial integrals.')

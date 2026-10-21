"""Reproduce Figure22.14: coordinate upper factors, not function samples."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r=np.logspace(-2,2,501)
first=.0176*r**3
second=.309*r
third=np.full_like(r,3.33)
envelope=np.maximum.reduce([first,second,third])
coarse=3.33*np.maximum(1,r**3)
assert np.all(envelope<=coarse)
fig,ax=plt.subplots(figsize=(9.6,5.5),layout='constrained')
ax.loglog(r,first,label=r'First coordinate: $0.0176r^3$',color='#4e79a7',linewidth=1.8)
ax.loglog(r,second,label=r'Second coordinate: $0.309r$',color='#59a14f',linewidth=1.8)
ax.loglog(r,third,label=r'Third coordinate: $3.33$',color='#b07aa1',linewidth=1.8)
ax.loglog(r,coarse,label=r'Common factor: $3.33\max\{1,r^3\}$',color='#d76a25',linestyle='--',linewidth=2)
ax.loglog(r,envelope,label='Maximum of the three coordinate factors',color='#252525',linewidth=2.4)
ax.set(xlabel=r'Lattice scale $r=|\omega_1|$',ylabel='Upper prefactor (Gaussian factor omitted)',
       title='Retaining the separate coordinate scaling factors',xlim=(.01,100),ylim=(1e-8,1e7))
ax.grid(which='major',alpha=.2)
ax.legend(loc='upper left',fontsize=10,framealpha=.97)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=170,bbox_inches='tight')
plt.close(fig)
print('Figure22.14 saved: elliptic-scaled-growth.png')

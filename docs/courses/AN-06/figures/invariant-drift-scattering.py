"""Reproduce Example 4.4, c=1, one transverse coordinate; exact formulas."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN06-invariant-drift-v1'})
y=np.linspace(-8,8,1001);phase=-np.pi/np.sqrt(1+y*y)
radius=np.concatenate(([0.],np.geomspace(.001,1000,1600)))
values=np.exp(-1j*np.pi/np.sqrt(1+radius*radius))
fig,ax=plt.subplots(1,2,figsize=(12,5.2),constrained_layout=True)
ax[0].plot(y,phase,color='#175d98',lw=2.5)
ax[0].axhline(0,color='#777777',ls='--',lw=1)
ax[0].set(xlabel='transverse coordinate y',ylabel='phase of S(y) (radians)',ylim=(-3.5,.3))
ax[0].set_yticks([-np.pi,-np.pi/2,0],['−π','−π/2','0'])
ax[0].set_title('Exact phase: −π / √(1 + y²)')
ax[0].annotate('S(0) = −1',xy=(0,-np.pi),xytext=(2,-2.8),arrowprops={'arrowstyle':'->'})
ax[0].text(-7.5,-.5,'phase → 0 as |y| → ∞',fontsize=11)
ax[0].grid(alpha=.18)
theta=np.linspace(0,2*np.pi,501)
ax[1].plot(np.cos(theta),np.sin(theta),color='#b0b0b0',ls='--',lw=1)
ax[1].plot(values.real,values.imag,color='#ae5030',lw=3)
ax[1].scatter([-1],[0],color='#ae5030',s=45,zorder=4)
ax[1].scatter([1],[0],facecolors='white',edgecolors='#ae5030',s=65,zorder=4)
ax[1].annotate('y = 0',xy=(-1,0),xytext=(-.85,.32))
ax[1].annotate('limit |y| → ∞',xy=(1,0),xytext=(.02,.33),arrowprops={'arrowstyle':'->'})
ax[1].set(xlabel='Re S(y)',ylabel='Im S(y)',xlim=(-1.2,1.2),ylim=(-1.2,.65),aspect='equal')
ax[1].set_title('Exact scattering values: |S(y)| = 1')
ax[1].grid(alpha=.18)
fig.suptitle('Complete ordinary drift scattering with transverse invariant directions',fontsize=15)
out=Path(__file__).resolve().parent
fig.savefig(out/'invariant-drift-scattering.png',dpi=180,metadata={'Software':'Matplotlib'})
fig.savefig(out/'invariant-drift-scattering.svg',metadata={'Date':None,'Creator':'Matplotlib'})

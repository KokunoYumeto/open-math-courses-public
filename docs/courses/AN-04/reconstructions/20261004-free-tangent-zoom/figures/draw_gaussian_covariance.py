"""Reproduce the exact Z7 coordinate example; original CC0 illustration."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(2,1,figsize=(6.4,9.2),layout='constrained')
q=np.linspace(-1.4,1.4,501)
ax[0].plot(-q*q/2,q,label=r'$x=(-q^2/2,q)$',color='#12677b',lw=2)
ax[0].plot(q*q/2,q,label=r'$y=(q^2/2,q)$',color='#984ba0',lw=2,ls='--')
ax[0].scatter([0],[0],color='black',s=25,zorder=3)
ax[0].axvline(0,color='#aaa',lw=.6);ax[0].axhline(0,color='#aaa',lw=.6)
ax[0].set(xlabel='First base coordinate',ylabel='Second base coordinate',
 title=r'One Lagrangian in two charts: $x=(y_1-y_2^2,y_2)$')
ax[0].legend(loc='upper center',fontsize=11)
ax[0].set_aspect('equal');ax[0].grid(alpha=.2)
v=np.linspace(-3,3,601);w=np.exp(1j*(v*v/2-np.pi/4))
ax[1].plot(v,w.real,label=r'$\mathrm{Re}\,w$',color='#12677b',lw=2)
ax[1].plot(v,w.imag,label=r'$\mathrm{Im}\,w$',color='#984ba0',lw=2,ls='--')
ax[1].set(xlabel=r'$v_2$ on the support $v_1=0$',ylabel='Coefficient',
 title=r'$w(v_2)\delta_0(v_1)$,  $w=e^{i(v_2^2/2-\pi/4)}$',
 ylim=(-1.15,1.15))
ax[1].legend(loc='lower center',ncol=2,fontsize=11);ax[1].grid(alpha=.2)
fig.suptitle('The phase correction and fourth root agree',fontsize=15)
fig.text(.5,-.012,
 r'$A_x=\mathrm{diag}(0,1),\ B_x=0,\ \beta_x=1$'+'\n'+
 r'$A_y=\mathrm{diag}(0,-1),\ B_y=\mathrm{diag}(0,-2),\ \beta_y=-i$'+'\n'+
 'Bottom: the common coefficient, not values of the delta distribution.\n'+
 'Exact proof: Gaussian-symbol companion, Z7 (Z20–Z21).',
 ha='center',va='top',fontsize=11)
for ext in ['svg','png']:
 fig.savefig(out/f'gaussian-covariance.{ext}',dpi=170,bbox_inches='tight')
plt.close(fig)

"""Exact CT21/CT22 coordinate plot; proof remains in the lesson."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':16,'svg.fonttype':'path'})
t=np.linspace(-1,1,501)
fig,axs=plt.subplots(2,1,figsize=(7,8),layout='constrained')
axs[0].plot(t,np.tan(t),color='#176777',lw=2.5)
axs[0].scatter([-1,1],[-np.tan(1),np.tan(1)],color='#176777')
axs[0].set(xlabel='Flow time t',ylabel=r'Base coordinate $x=\tan t$',
 title='One injective base interval',xlim=(-1.08,1.08))
axs[1].plot(t,np.cos(t)**2,color='#176777',lw=2.5,label=r'$\xi_x/\tau=\cos^2 t$')
axs[1].axhline(1,color='#77608d',ls=':',lw=2,label=r'$\xi_z/\eta=1$')
axs[1].axhline(np.cos(1)**2,color='#ad4d39',ls='--',lw=2,label=r'Lower bound $\cos^2(1)$')
axs[1].set(xlabel='Flow time t',ylabel='Cotangent multiplier',title='Covectors retain a positive scale',
 xlim=(-1.08,1.08),ylim=(0,1.14))
axs[1].legend(loc='lower center',fontsize=13)
for ax in axs:
 ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'compact-tube-coordinates.svg',metadata={'Creator':'AN-04 course project'})
fig.savefig(out/'compact-tube-coordinates.png',dpi=170)
print('Saved exact finite tube coordinate illustration.')

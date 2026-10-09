"""Plot the original smooth cutoff and the proved full two-band estimate."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def bump(x):
    out=np.zeros_like(x);mask=x>0;out[mask]=np.exp(-1/x[mask]);return out
tau=np.linspace(.25,1,1601)
h=bump(1-tau)/(bump(1-tau)+bump(tau-.25))
weight=(4*(1-h)**2+h*h)/tau
fig,axs=plt.subplots(1,2,figsize=(13,5.8),layout='constrained')
ax=axs[0];ax.plot(tau,h,lw=2.4,color='#246b89',label=r'$h=\chi(\tau)$')
ax.axvline(5/8,color='#777',ls=':',lw=1);ax.axhline(.5,color='#777',ls=':',lw=1)
ax.scatter([5/8],[.5],color='#246b89',zorder=4)
ax.set_xticks([1/4,5/8,1],['1/4','5/8','1']);ax.set_yticks([0,.5,1],['0','1/2','1'])
ax.set_xlabel(r'Original cutoff argument $\tau=(2|\xi|/N)^2$',fontsize=12)
ax.set_ylabel('Original projection weight',fontsize=12)
ax.set_title('Both weights stay explicit',fontsize=16,weight='bold')
ax.legend(loc='lower left',fontsize=13);ax.grid(alpha=.15)
ax=axs[1];ax.plot(tau,weight,color='#197554',lw=2.4,label=r'$[4(1-h)^2+h^2]/\tau$')
ax.plot([.25,.625],[5,5],color='#b26720',lw=2)
ax.plot([.625,1],[32/5,32/5],color='#b26720',lw=2,label='Proved two-piece bound')
ax.axhline(16,color='#959ba5',ls='--',lw=1.5,label='Earlier support bound: 16')
ax.set_xticks([1/4,5/8,1],['1/4','5/8','1']);ax.set_yticks([0,4,5,32/5,16],['0','4','5','32/5','16'])
ax.set_ylim(0,17);ax.set_xlabel(r'Original cutoff argument $\tau$',fontsize=12)
ax.set_ylabel(r'Full weighted sum divided by $|\xi|^2$',fontsize=12)
ax.set_title('The exact pair gives a smaller bound',fontsize=16,weight='bold')
ax.legend(loc='upper center',bbox_to_anchor=(.5,.85),fontsize=11);ax.grid(alpha=.15)
fig.suptitle('The original two-band projection and retained dissipation',fontsize=19,weight='bold')
fig.supxlabel('Proof: Exercise 4, (13.12)–(13.16). The curve samples the exact cutoff; the analytical bound proves the estimate.\nThe complete Fourier gradient factor gives 8/(5π²) times D. No fluid solution is sampled.',fontsize=11)
out=Path(__file__).with_suffix('');fig.savefig(out.with_suffix('.png'),dpi=160);fig.savefig(out.with_suffix('.svg'));plt.close(fig)


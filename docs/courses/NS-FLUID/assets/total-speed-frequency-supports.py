"""Exact radial symbols from NS-FLUID-12 equations 3.1–3.3."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
def b(s):
 s=np.asarray(s);out=np.zeros_like(s);inside=s>0
 out[inside]=np.exp(-1/s[inside]);return out
def phi(r):
 s=r*r;left=b(1-s);right=b(s-.25)
 return left/(left+right)
def p(r):return phi(r)-phi(2*r)
def companion(r):return phi(r/2)-phi(4*r)
radius=np.geomspace(.04,10,4000)
fig,axes=plt.subplots(1,2,figsize=(12.5,5.2),layout='constrained')
for N,col in zip([.5,1,2,4],['#238b7b','#287eb1','#6b58a7','#b26a30']):
 axes[0].plot(radius,p(radius/N),label=fr'$N={N:g}$',color=col,lw=2)
axes[0].set(title='Actual dyadic symbols; four members shown',xlabel=r'Original frequency radius $|\xi|$',ylabel=r'$p(\xi/N)$')
axes[0].legend()
N=2.
axes[1].plot(radius,companion(radius/N),color='#267f9b',lw=2,label=r'$\widetilde p(\xi/2)$')
axes[1].plot(radius,p(radius/N),color='#c27339',lw=2,label=r'$p(\xi/2)$')
axes[1].axvspan(N/4,N,color='#267f9b',alpha=.09)
axes[1].set(title=r'Companion equals one on $1/2\leq|\xi|\leq2$',xlabel=r'Original frequency radius $|\xi|$',ylabel='Symbol value')
axes[1].legend()
for ax in axes:
 ax.set_xscale('log',base=2);ax.set_xlim(.0625,8);ax.set_ylim(-.04,1.08)
 ax.set_xticks([.0625,.125,.25,.5,1,2,4,8],['1/16','1/8','1/4','1/2','1','2','4','8'])
 ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
fig.suptitle(r'Exact cutoff family, $N_*=1$; the full lattice continues in both directions',fontsize=13)
fig.savefig(ROOT/'total-speed-frequency-supports.png',dpi=170)
fig.savefig(ROOT/'total-speed-frequency-supports.svg')
print('Saved exact radial symbols and companion plateau.')

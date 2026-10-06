"""Render the exact Fourier sequence of BC24--BC28."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parent
n=np.arange(1,21,dtype=float)
bracket=np.sqrt(1+n*n)
fig,axes=plt.subplots(1,2,figsize=(11,4.4),layout='constrained')
axes[0].plot(n,bracket**0.5,'o-',label=r'input coefficient $\langle n\rangle^{1/2}$')
axes[0].plot(n,bracket**-0.5,'s-',label=r'output coefficient $\langle n\rangle^{-1/2}$')
axes[0].set(xlabel=r'Fourier index $n$',ylabel='Coefficient magnitude',
    title=r'Original sequence: $u_n\mapsto Ru_n$')
axes[1].plot(n,np.ones_like(n),'o-',label=r'output in $H^{1/2}$: norm $1$')
axes[1].plot(n,bracket**-1,'s-',label=r'output in $H^{-1/2}$: norm $\langle n\rangle^{-1}$')
axes[1].set(xlabel=r'Fourier index $n$',ylabel='Output norm',
    title='Same output, two specified target spaces',ylim=(-0.04,1.16))
for ax in axes:
    ax.grid(alpha=.25);ax.legend(loc='best',fontsize=9);ax.set_xticks([1,5,10,15,20])
fig.suptitle(r'$R_{11}=R_{12}=R_{22}=0,\ R_{21}=\Lambda^{-1}$'
             r', $\Lambda e_n=(1+n^2)^{1/2}e_n$',fontsize=14)
fig.savefig(root/'calderon-mixed-orders.png',dpi=160)
fig.savefig(root/'calderon-mixed-orders.svg')
plt.close(fig)

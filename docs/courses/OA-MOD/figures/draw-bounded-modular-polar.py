from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'oa-mod-polar-mp8-v1'})
n=np.arange(1,65);q=n+1
xnorm=np.cumsum(q.astype(float)**-4)
snorm=np.cumsum(q.astype(float)**-2)
delta_norm=n.astype(float)
assert np.all(xnorm<snorm) and np.all(snorm<1)
fig,axes=plt.subplots(1,2,figsize=(12.6,4.7),layout='constrained')
ax=axes[0]
ax.plot(n,snorm,color='#1a6b8b',lw=2.4,label=r'$\|Sx^{(N)}\|^2=\sum_{n\leq N}(n+1)^{-2}$')
ax.plot(n,xnorm,color='#7061a6',lw=2.4,label=r'$\|x^{(N)}\|^2=\sum_{n\leq N}(n+1)^{-4}$')
ax.axhline(1,color='#687782',ls='--',lw=1.5,label='Proved upper bound 1')
ax.set(xlim=(1,64),ylim=(0,1.08),xlabel='Truncation length N',ylabel='Squared norm')
ax.set_title(r'(a) Convergence in the graph norm of $S$',pad=12)
ax.legend(loc='center right',bbox_to_anchor=(.99,.38),fontsize=10,frameon=True)
ax.grid(alpha=.18)
ax=axes[1]
ax.plot(n,delta_norm,color='#a74818',lw=2.5)
ax.set(xlim=(1,64),ylim=(0,68),xlabel='Truncation length N',ylabel='Squared norm')
ax.set_title(r'(b) $\|\Delta x^{(N)}\|^2=N$',pad=12)
ax.annotate(r'Exactly linear growth: $x\notin D(\Delta)$',xy=(48,48),xytext=(7,59),
            arrowprops={'arrowstyle':'->','color':'#a74818'},color='#a74818',fontsize=11)
ax.grid(alpha=.18)
fig.suptitle(r'Exact domain example: $H=\ell^2(\mathbb{N};\mathbb{C}^2)$, $q_n=n+1$, $x_n=(q_n^{-2},0)$',fontsize=15)
fig.savefig(D/'bounded-modular-polar.svg',metadata={'Date':None,'Creator':'OpenAI Codex; exact MP8 partial sums'})
fig.savefig(D/'bounded-modular-polar.png',dpi=160,metadata={'Software':'OpenAI Codex; exact MP8 partial sums'})

"""Reproduce the two error-bound components in Example 4.1, CC0.

OpenAI GPT-6.1 Sol in Codex, Ultra setting, October 2026.
These are normalized analytic envelopes, not measured arithmetic errors.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

L=1e8
a=1/4000
u=np.linspace(40,400,1500)
zero_log=2*np.log(u)-a*L/u
contour_log=2*np.log(L+u)-u
left,right=40.,400.
for _ in range(70):
    mid=(left+right)/2
    if 2*math.log(mid)-a*L/mid < 2*math.log(L+mid)-mid:
        left=mid
    else:
        right=mid
crossing=(left+right)/2
value=math.exp(2*math.log(crossing)-a*L/crossing)

plt.rcParams.update({'font.size':12})
fig,ax=plt.subplots(figsize=(9.5,6.3),constrained_layout=True)
ax.semilogy(u,np.exp(zero_log),color='#244766',linewidth=2.2,
            label=r'Zero term: $u^2\exp(-aL/u)$')
ax.semilogy(u,np.exp(contour_log),color='#c25523',linewidth=2.2,
            label=r'Contour term: $(L+u)^2\exp(-u)$')
ax.axvline(math.sqrt(a*L),color='#777777',linestyle=':',linewidth=1.6,
           label=r'Exponential balance $u=\sqrt{aL}$')
ax.scatter([crossing],[value],color='#2f6742',s=60,zorder=5)
ax.annotate(f'Prefactor crossing\nu = {crossing:.2f}',(crossing,value),
            xytext=(33,45),textcoords='offset points',color='#2f6742',
            arrowprops={'arrowstyle':'->','color':'#2f6742'})
ax.set_ylim(1e-180,1e4)
ax.set_xlim(40,400)
ax.set_xlabel(r'$u=\log T$')
ax.set_ylabel('Normalized relative error component (log scale)')
ax.set_title(r'The cutoff balance: $L=\log x=10^8$, $a=1/4000$',pad=12)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.15),fontsize=11,ncol=1)
ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)
plt.close(fig)
print(f'Crossing {crossing:.12f}; relative model value {value:.12e}')

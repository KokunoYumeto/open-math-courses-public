"""Reproduce the exact coordinate window and HM06 finite domain sums."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig, (ax, bx)=plt.subplots(2,1,figsize=(9,10.5),dpi=100)
fig.patch.set_facecolor('#fafbfc')
ratios=np.array([[2.0**(j-i) for j in range(4)] for i in range(4)])
ax.imshow(np.log2(ratios),cmap='PuOr_r',vmin=-3,vmax=3)
for i in range(4):
    for j in range(4):
        k=j-i
        label=str(2**k) if k>=0 else '1/'+str(2**(-k))
        ax.text(j,i,label,ha='center',va='center',fontsize=18,
                color='white' if abs(k)>=2 else '#102333')
ax.set_xticks(range(4));ax.set_yticks(range(4))
ax.set_xlabel('column j');ax.set_ylabel('row i')
ax.set_title('Exact multipliers on a finite coordinate window\n'
             r'$\Delta E_{ij}=2^{j-i}E_{ij}$',pad=13)
ax.set_xticks(np.arange(-.5,4,1),minor=True)
ax.set_yticks(np.arange(-.5,4,1),minor=True)
ax.grid(which='minor',color='white',linewidth=2)
ax.tick_params(which='minor',bottom=False,left=False)
N=np.arange(1,13)
quarter=np.array([sum(2**(-n/2) for n in range(1,int(k)+1)) for k in N])
bx.plot(N,N,'s-',color='#923c15',linewidth=2,label=r'half-power sum: $N$')
bx.plot(N,quarter,'o-',color='#076f82',linewidth=2,label=r'quarter-power sum: $\sum_{n=1}^N2^{-n/2}$')
bx.axhline(1+math.sqrt(2),color='#076f82',linestyle='--',linewidth=1)
bx.annotate(r'$1+\sqrt{2}$',(11,1+math.sqrt(2)),xytext=(9.5,3.8),
            arrowprops={'arrowstyle':'->','color':'#076f82'},color='#076f82',fontsize=14)
bx.set(xlim=(.6,12.4),ylim=(0,13),xlabel='truncation N',ylabel='squared graph-image norm')
bx.set_title(r'$Z_N=\sum_{n=1}^N2^{-n/2}E_{0n}$: the two domain tests',pad=14)
bx.grid(alpha=.2);bx.legend(loc='upper left',frameon=False)
fig.subplots_adjust(top=.93,bottom=.11,hspace=.49,left=.12,right=.95)
fig.text(.5,.035,'HM04–06: the infinite limit belongs to the quarter-power domain,\n'
         'but not the half-power domain. The sixteen entries above are only a window.',
         ha='center',va='center',fontsize=11,color='#253746')
out=Path(__file__).with_name('hilbert-schmidt-modular-domains.png')
fig.savefig(out,dpi=100,metadata={'Software':'OA-MOD original figure','Title':'Hilbert-Schmidt modular domains'})
plt.close(fig)

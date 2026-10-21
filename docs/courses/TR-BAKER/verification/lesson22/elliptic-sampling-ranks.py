"""Figure22.18: exact normal-jet index sets for22.211 and22.217."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base=Path(__file__).resolve().parent
points=[(a,b) for a in range(13) for b in range(13-a)]
selected=[(a,b) for a,b in points if b<3]
assert len(points)==91 and len(selected)==36
fig,axes=plt.subplots(1,2,figsize=(10.6,5),constrained_layout=True)
for ax in axes:
    ax.scatter(*zip(*points),s=26,color='#d2dce2',zorder=2)
    ax.plot([0,12],[12,0],'--',lw=1.1,color='#647886')
    ax.set(xlim=(-.6,12.7),ylim=(-.6,12.7),xlabel=r'First normal exponent $\alpha_1$',ylabel=r'Second normal exponent $\alpha_2$')
    ax.set_xticks(range(0,13,2));ax.set_yticks(range(0,13,2));ax.set_aspect('equal');ax.grid(alpha=.13)
axes[0].scatter(*zip(*points),s=26,color='#287a9d',zorder=3)
axes[0].set_title('All normal jets: 91 indices',fontsize=12)
axes[1].scatter(*zip(*selected),s=29,color='#b35c32',zorder=3)
axes[1].axhline(3,color='#b35c32',lw=1,ls=':')
axes[1].text(6,3.4,r'$\alpha_2<3$',color='#994622',fontsize=12)
axes[1].set_title('Truncated normal jets: 36 indices',fontsize=12)
fig.suptitle(r'$\alpha_1+\alpha_2\leq12$: the index sets in (22.624)–(22.625)',fontsize=14)
fig.savefig(base/'elliptic-sampling-ranks.png',dpi=170)
plt.close(fig)
print('Figure22.18 saved; exact counts91 and36.')

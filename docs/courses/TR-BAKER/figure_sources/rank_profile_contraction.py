"""Original rank-profile margins in Theorem10.102 and Corollary10.103. CC0."""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
ms=list(range(1,9))
bounds=[F(675,2048)*F(25,6144)**m for m in ms]
assert bounds[0]==F(5625,4194304)<F(1,700)
fig,axes=plt.subplots(2,1,figsize=(10.8,8.3),constrained_layout=True)
ax=axes[0]
ax.semilogy(ms,[float(b) for b in bounds],marker='o',color='#267a81',lw=2.4)
ax.axhline(1/700,color='#b75435',ls='--',label='Uniform allowance factor 1/700')
ax.set_xticks(ms);ax.set_xlabel('New rank m (the proof holds for every m >= 1)')
ax.set_ylabel('Certified normalized product upper bound')
ax.set_title('The original residue-index profile has a uniform strict margin',pad=13)
ax.grid(alpha=.2);ax.legend(loc='upper right',framealpha=1)
ax.text(.04,.17,'C_m = (675/2048) (25/6144)^m\nC_1 = 5625/4194304 < 1/700',transform=ax.transAxes,
        fontsize=11,bbox={'facecolor':'white','edgecolor':'none','alpha':1})
ax=axes[1]
values=[F(672,5),F(511,3)]
labels=['Original rank-one allowance','Every rank-one representation needs']
ax.barh(labels,[float(v) for v in values],color=['#487ca0','#ac8240'],height=.48)
ax.invert_yaxis();ax.set_xlim(0,210);ax.set_xlabel('Weight (strict bounds from elementary logarithm estimates)')
for i,v in enumerate(values):ax.text(float(v)+3,i,('< 672/5' if i==0 else '> 511/3'),va='center',fontsize=11)
ax.set_title('A proved rank-two example: K = Q, p = 3, bases 2 and 5\nL = 101 z_1 + 103 z_2',pad=12)
ax.grid(axis='x',alpha=.2)
for a in axes:
    a.spines[['top','right']].set_visible(False)
fig.suptitle('Geometric stopping preserves the original minimum-rank budget',fontsize=15)
fig.savefig(HERE/'rank-profile-contraction.png',dpi=165)
plt.close(fig)

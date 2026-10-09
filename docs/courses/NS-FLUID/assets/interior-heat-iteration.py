"""Physical ball radii, cutoff bands and time margins in NS-FLUID-14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
ROOT=Path(__file__).resolve().parent
rho=1.;eps=rho/32;t1=2.;t2=4.;T=t2-t1;tau=T/16
R=lambda k:rho-2*k*eps
S=lambda k:t1+k*tau
assert R(10)==.375 and S(9)==3.125
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13})
fig,axs=plt.subplots(1,2,figsize=(14,8),layout='constrained',gridspec_kw={'width_ratios':[1,1.3]})
ax=axs[0]
for k in range(1,10):
    y=10-k
    ax.broken_barh([(0,R(k))],(y-.15,.3),facecolors='#2d7196')
    ax.broken_barh([(R(k),eps)],(y-.15,.3),facecolors='#a8cddd')
    ax.broken_barh([(R(k-1)-eps,eps)],(y-.15,.3),facecolors='#e3a063')
    ax.text(R(k-1)+.016,y,f'R{k} = {R(k):.4f}',va='center',fontsize=10)
ax.set_xlim(0,1.24);ax.set_ylim(.4,9.7);ax.set_yticks(range(1,10),labels=[f'k = {k}' for k in range(9,0,-1)])
ax.set_xlabel('Original distance |x − x₀|, with ρᵦ = 1')
ax.set_title('Nested balls and their exact cutoff bands',loc='left')
ax.grid(axis='x',alpha=.17)
ax.legend(handles=[Patch(color='#2d7196',label='Target ball Bₖ'),
                   Patch(color='#a8cddd',label='Additional region where ψₖ = 1'),
                   Patch(color='#e3a063',label='Smooth transition band of ψₖ')],loc='lower right',bbox_to_anchor=(1,-.23),fontsize=10)
ax=axs[1];labels=['2 → 12/5','12/5 → 3','3 → 4','4 → 6','6 → 12','12 → ∞','Hölder vorticity','Newton velocity / gradient','Vorticity gradient']
for k,label in enumerate(labels,1):
    y=10-k
    start=S(k-1);ready=S(k)
    if k==8:
        start=ready=S(7)
        ax.plot([ready,t2],[y,y],lw=9,color='#478266',solid_capstyle='butt')
    else:
        ax.plot([start,ready],[y,y],lw=9,color='#e3a063',solid_capstyle='butt')
        ax.plot([ready,t2],[y,y],lw=9,color='#2d7196',solid_capstyle='butt')
    ax.text(t1-.06,y,label,va='center',ha='right',fontsize=10)
    ax.text(ready,y+.18,f'{ready:g}',va='bottom',ha='center',fontsize=9)
ax.axvline(S(9),ls=':',color='#88482e',lw=1.3)
ax.set_xlim(t1-.1,t2+.08);ax.set_ylim(.4,9.7);ax.set_yticks([])
ax.set_xlabel('Original time, with t₁ = 2 and t₂ = 4')
ax.set_title('Exact time cutoffs and proved receiving intervals',loc='left')
ax.set_xticks([2,2.25,2.5,2.75,3,3.125,3.5,3.75,4],labels=['2','2.25','2.5','2.75','3','3.125','3.5','3.75','4'],rotation=30)
ax.grid(axis='x',alpha=.17)
ax.legend(handles=[Patch(color='#e3a063',label='Time cutoff changes from 0 to 1'),
                   Patch(color='#2d7196',label='Target estimate applies'),
                   Patch(color='#478266',label='Newton map: same time s₇, smaller ball B₈')],loc='lower right',bbox_to_anchor=(1,-.23),fontsize=10)
fig.suptitle('The complete interior iteration retains its physical margins',fontsize=16)
for ext in ['png','svg']:fig.savefig(ROOT/f'interior-heat-iteration.{ext}',dpi=170)
print({'radii':[R(k) for k in range(11)],'times':[S(k) for k in range(10)],'newton_time':S(7),'final_time':S(9)})

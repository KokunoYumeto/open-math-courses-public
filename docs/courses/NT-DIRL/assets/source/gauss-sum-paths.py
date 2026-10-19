"""Original CC0 diagram of ordered sums e(n^2/p), with exact endpoints.

The plotted coordinates are numerical samples of the explicit roots of unity;
endpoint labels state the exact evaluations proved in Gauss sums, Theorem 4.1.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['svg.hashsalt']='quadratic-gauss-sum-paths'
fig,axes=plt.subplots(2,1,figsize=(5.7,8.7),constrained_layout=True)
for ax,p,label in zip(axes,[5,7],[r'$\sqrt{5}$',r'$i\sqrt{7}$']):
    terms=np.exp(2j*np.pi*(np.arange(p)**2%p)/p)
    points=np.r_[0,np.cumsum(terms)]
    ax.axhline(0,color='#cbd5e1',lw=.8); ax.axvline(0,color='#cbd5e1',lw=.8)
    for n,(a,b) in enumerate(zip(points[:-1],points[1:])):
        ax.annotate('',(b.real,b.imag),(a.real,a.imag),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#164e63'})
        midpoint=(a+b)/2; normal=1j*(b-a)/abs(b-a)
        at=midpoint+.10*normal
        if p==5 and n==3: at=midpoint-.25-.20j
        if p==5 and n==4: at=midpoint+.22-.12j
        if p==7 and n==1: at=midpoint+.12-.18j
        if p==7 and n==2: at=midpoint-.08+.20j
        ax.text(at.real,at.imag,f'n={n}',fontsize=10,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':.7})
    ax.scatter(points.real,points.imag,s=17,color='#164e63')
    ax.scatter([points[-1].real],[points[-1].imag],s=65,color='#b45309',zorder=5)
    ax.annotate('Start: 0',(0,0),xytext=(-.5,-.3),fontsize=12)
    ax.annotate('End: '+label,(points[-1].real,points[-1].imag),xytext=(points[-1].real+.10,points[-1].imag+.18),fontsize=12,color='#92400e')
    ax.set_title(f'p = {p}: add the unit vectors in order n = 0, ..., {p-1}',fontsize=12,pad=12)
    ax.set_aspect('equal'); ax.set_xlabel('Real part',fontsize=12); ax.set_ylabel('Imaginary part',fontsize=12)
    ax.set_xlim(-1.0,3.4 if p==5 else 2.1); ax.set_ylim(-1.45,1.6 if p==5 else 3.35)
    for spine in ax.spines.values(): spine.set_visible(False)
out=Path(__file__).resolve().parent.parent
fig.savefig(out/'gauss-sum-paths.png',dpi=160,metadata={'Software':None})
fig.savefig(out/'gauss-sum-paths.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Codex, Ultra; original CC0 diagram'})
plt.close(fig)

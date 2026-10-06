"""Original numerical illustration of U004 Proposition4.4 / Example4.5; CC0.

Requires Python3, NumPy, SciPy and Matplotlib. The displayed samples have c=1.
The sine integral is evaluated numerically with scipy.special.sici. The exact
tail bound2/a and failure of absolute integrability are proved in the lesson,
not inferred from the plot. No numerical sample certifies an endpoint value.
"""
from pathlib import Path
import numpy as np
from scipy.special import sici
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN06-conditional-drift-phase-v1'})
root=Path(__file__).resolve().parent
x=np.linspace(-32,32,16001)
potential=np.sinc(x/np.pi)
primitive=sici(x)[0]
fig,axes=plt.subplots(1,2,figsize=(13,5.4),constrained_layout=True)
color='#126783';accent='#b94c29'
axes[0].plot(x,potential,color=color,lw=1.8,label=r'$V(x)=\sin(x)/x,\quad V(0)=1$')
for sign in [-1,1]:
    tail=np.linspace(1,32,400)
    axes[0].plot(sign*tail,1/tail,color=accent,lw=1,ls='--')
    axes[0].plot(sign*tail,-1/tail,color=accent,lw=1,ls='--')
axes[0].set(xlabel='position x',ylabel='potential V(x)',title='Decay permits cancellation',ylim=(-.35,1.1))
axes[0].text(.04,.06,r'$\int |V|=\infty$ by the disjoint-interval proof',transform=axes[0].transAxes,fontsize=11)
axes[0].legend(loc='upper right',fontsize=11)
axes[1].plot(x,primitive,color=color,lw=1.8,label=r'$F(x)=\int_0^x V(s)\,ds$ (numerical samples)')
reference=float(sici(1000)[0])
for sign in [-1,1]:
    tail=np.linspace(2,32,400)
    center=sign*reference
    err=2/tail+2/1000
    axes[1].fill_between(sign*tail,center-err,center+err,color=accent,alpha=.12)
    axes[1].plot(sign*tail,np.full(tail.shape,center),color=accent,ls='--',lw=1)
axes[1].set(xlabel='position x',ylabel='primitive F(x), speed c=1',title='Finite phase endpoints give ordinary waves',ylim=(-2.5,2.5))
axes[1].text(.03,.04,r'$|F(x)-F(\pm\infty)|\leq 2/|x|$ for $|x|\geq1$',transform=axes[1].transAxes,fontsize=11)
axes[1].legend(loc='upper left',fontsize=10)
for ax in axes:
    ax.axhline(0,color='#777777',lw=.7)
    ax.grid(alpha=.18)
fig.suptitle('Conditional integrability in the exact drift model',fontsize=17)
fig.text(.5,-.01,'Shading: separate proven tail bounds around the numerical reference F(±1000); no endpoint evaluation is assumed.',ha='center',fontsize=10)
fig.savefig(root/'conditional-drift-phase.png',dpi=160,bbox_inches='tight')
fig.savefig(root/'conditional-drift-phase.svg',bbox_inches='tight',metadata={'Date':None})
plt.close(fig)

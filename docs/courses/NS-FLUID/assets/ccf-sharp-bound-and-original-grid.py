"""Reproduce the sharp original velocity bound and actual nonuniform cubic grid."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'legend.fontsize':9,'figure.facecolor':'#f7f9fc','axes.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
blue='#176699';orange='#c95b20';green='#16775b';purple='#7447a7'
fig,ax=plt.subplots(1,3,figsize=(15.2,4.9));fig.suptitle('The joint error bound and the original nonuniform grid',fontweight='bold',y=1.03)
A=np.linspace(0,6,601);phi=np.where(A<=2,A*A/2,2*A-2);old=np.minimum(A*A/2,2*A)
ax[0].plot(A,old,'--',color=orange,label=r'CM6: $\min\{A^2/2,2A\}$')
ax[0].plot(A,phi,color=blue,lw=2,label=r'Sharp $\Phi(A;1,1)$, SC6')
ax[0].set_xlabel('Actual receiving radius A');ax[0].set_ylabel(r'Bound on $|E-y\Delta|$ with $\gamma_0=0$')
ax[0].set_title(r'Both constraints: $d_0=d_1=1$');ax[0].legend()
y=np.linspace(-4,4,1001);q=lambda r:np.clip(np.abs(r)-2,-1,1)
eta=.12;nodes,weights=np.polynomial.legendre.leggauss(180)
rho=np.exp(-1/(1-nodes*nodes));weights=weights*rho;weights=weights/weights.sum()
smooth=np.array([np.sum(weights*q(r-eta*nodes)) for r in y])
ax[1].plot(y,q(y),'--',color=orange,label=r'Limiting even $q^{\rm even}$, SC16')
ax[1].plot(y,smooth,color=green,lw=2,label=r'Mollified $q_\eta$, $\eta=0.12$ (numerical evaluation)')
ax[1].axvline(3,color='#667586',lw=.8);ax[1].axvline(-3,color='#667586',lw=.8)
ax[1].set_xlabel('Original coordinate y');ax[1].set_ylabel('Even compatibility error');ax[1].set_title(r'Approach the sharp coefficient at $A=3$');ax[1].legend(loc='lower right')
xs=np.array([-63/16,-15/8,-3/4,0,3/4,15/8,63/16]);ws=np.array([9979/14784,855551/295680,-5515/10752,47413/26880,-5515/10752,855551/295680,9979/14784])
for xx,ww in zip(xs,ws):
    col=blue if ww>=0 else orange
    ax[2].plot([xx,xx],[0,ww],color=col,lw=2);ax[2].scatter([xx],[ww],color=col,s=36)
    ax[2].annotate(f'{ww:.3f}',(xx,ww),xytext=(0,6 if ww>=0 else -16),textcoords='offset points',ha='center',fontsize=8)
ax[2].set_xticks(xs,['−63/16','−15/8','−3/4','0','3/4','15/8','63/16'],rotation=30)
ax[2].set_ylim(-.9,3.3);ax[2].set_xlabel(r'Original nodes $x_j=\sinh[(j-3)\log2]$');ax[2].set_ylabel('Complete effective cubic weight')
ax[2].set_title('EX13–EX20 retain every negative weight')
for a in ax:a.grid(alpha=.18);a.axhline(0,color='#9da9b7',lw=.6)
fig.text(.5,-.035,'SC1–SC17 prove the bound and smooth sharpness construction. EX13–EX22 give the exact rational nodes, weights and errors; decimal labels are for display.',ha='center',fontsize=10)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(R/('ccf-sharp-bound-and-original-grid.'+ext),dpi=180,bbox_inches='tight')
plt.close(fig)
print('Reproduced sharp-bound and original-grid figure.')

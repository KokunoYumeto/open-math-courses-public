"""Exact coordinate weights for OA-MOD-TC-11; no numerical approximation to domains."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14,6.4),gridspec_kw={'width_ratios':[1,1.15]})
i,j=np.mgrid[1:9,1:9];exponent=j-i
ax.imshow(exponent,cmap='coolwarm',norm=TwoSlopeNorm(vmin=-7,vcenter=0,vmax=7),origin='upper')
for row in range(8):
 for col in range(8):
  k=col-row; label=str(2**k) if k>=0 else '1/'+str(2**(-k))
  ax.text(col,row,label,ha='center',va='center',fontsize=10,color='white' if abs(k)>4 else '#17212b')
ax.set_xticks(range(8),range(1,9));ax.set_yticks(range(8),range(1,9))
ax.set_xlabel('column j');ax.set_ylabel('row i')
ax.set_title(r'Exact weights of $\Delta$: $2^{j-i}$',pad=15,fontweight='bold')
n=np.arange(1,9)
bx.plot(n,2.**(-n),'o-',label=r'$H$: $2^{-n}$',color='#167d8d')
bx.plot(n,np.full(8,.5),'s-',label=r'$D(S)$: $1/2$',color='#b84030')
bx.plot(n,2.**(1-2*n),'^-',label=r'$D(F)$: $2^{1-2n}$',color='#6846a0')
bx.set_yscale('log',base=2);bx.set_xticks(n);bx.set_ylim(2**-16,1)
bx.set_xlabel('coordinate n');bx.set_ylabel('term in the squared-norm test')
bx.set_title(r'For $X=\sum_{n\geq1}2^{-n/2}E_{1n}$',pad=15,fontweight='bold')
bx.grid(alpha=.2);bx.legend(loc='lower left',fontsize=11)
fig.suptitle('The same matrix has different adjoint-domain tests',fontsize=19,fontweight='bold',y=.98)
fig.text(.26,.065,r'$JX=X^*$ exchanges the two indices.'+'\nOnly the first 8 × 8 coordinates are drawn.',ha='center',fontsize=12)
fig.text(.755,.065,r'$X\in D(F)\setminus D(S)$'+'\nThe constant terms have an infinite sum.',ha='center',fontsize=12)
fig.subplots_adjust(top=.82,bottom=.22,wspace=.34,left=.06,right=.98)
fig.savefig(Path(__file__).with_name('tomita-domain-weights.png'),dpi=150)
plt.close(fig)


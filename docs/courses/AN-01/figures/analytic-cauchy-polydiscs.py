"""Exact domain slice and proved remainder bound for AN01-U107. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','svg.hashsalt':'AN01-U107'})
fig,axes=plt.subplots(1,2,figsize=(12.4,5.1),layout='constrained')
ax=axes[0]
ax.add_patch(Rectangle((-1,-.25),2,.5,facecolor='#dbeafe',edgecolor='#245a9c',lw=2))
ax.add_patch(Rectangle((-.5,-.125),1,.25,facecolor='#bbf7d0',edgecolor='#167047',lw=2))
ax.axhline(0,color='#354152',lw=.7)
ax.axvline(0,color='#354152',lw=.7)
ax.set(xlim=(-1.2,1.2),ylim=(-.33,.33),xlabel=r'Tangential coordinate $x$',ylabel=r'Normal coordinate $t$',
       xticks=[-1,-.5,0,.5,1],yticks=[-.25,-.125,0,.125,.25])
ax.set_yticklabels([r'$-1/4$',r'$-1/8$','0',r'$1/8$',r'$1/4$'])
ax.text(0,.285,r'Input: $\Omega_{1,\,1/4}$',ha='center',color='#245a9c')
ax.text(0,.075,r'Output: $\Omega_{1/2,\,1/4}$',ha='center',color='#115a36',fontsize=12)
ax.set_title('Both radii are halved\nReal slice of the complex polydiscs',fontsize=14)
ax=axes[1]
N=np.arange(0,11)
bound=2.0**(1-N)
ax.semilogy(N,bound,'o-',base=2,color='#7c3e9e',lw=2)
ax.set(xlim=(-.3,10.3),xticks=np.arange(0,11,2),xlabel=r'Number of iterates $N$',
       ylabel=r'Certified remainder divided by $M$')
ax.grid(True,which='major',alpha=.22)
ax.set_title(r'$A=1/2$: bound $2^{1-N}$'+'\nNot a measured solution error',fontsize=14)
fig.savefig(out/'analytic-cauchy-polydiscs.png',dpi=170)
svg=out/'analytic-cauchy-polydiscs.svg'
fig.savefig(svg,metadata={'Date':None})
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
plt.close(fig)

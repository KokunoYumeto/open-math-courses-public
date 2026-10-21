"""Figure22.17: exact monomial counts underlying the multiplicity bound."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base=Path(__file__).resolve().parent
fig,ax=plt.subplots(1,2,figsize=(11.8,4.7),constrained_layout=True)
for m,color,size in [(4,'#2c7599',13),(1,'#b55225',48)]:
    pts=np.array([(i/m,j/m) for i in range(4*m) for j in range(4*m-i)])
    ax[0].scatter(pts[:,0],pts[:,1],s=size,c=color,label=fr'$m={m}$: {len(pts)} monomials',zorder=m==1 and 3 or 2)
ax[0].plot([0,4],[4,0],'--',color='#555',lw=1.3,label=r'Boundary $x+y=4$')
ax[0].set(xlim=(-.15,4.2),ylim=(-.15,4.2),xlabel=r'Exponent of $x$, divided by $m$',ylabel=r'Exponent of $y$, divided by $m$',title=r'Monomials outside $I^m$, scaled by $m$')
ax[0].set_aspect('equal');ax[0].legend(loc='upper right',fontsize=9)
m=np.arange(1,25)
scaled=16+4/m
ax[1].plot(m,scaled,'o-',color='#2c7599',ms=4,label=r'$2\,\mathrm{length}(R/I^m)/m^2=16+4/m$')
ax[1].axhline(16,color='#b55225',ls='--',label=r'Intersection bound $(T+1)^2=16$')
ax[1].set(xlabel=r'Power $m$',ylabel='Normalized colength',ylim=(15.6,20.4),title='The leading count of powers')
ax[1].legend(fontsize=9)
for a in ax:a.grid(alpha=.15)
fig.suptitle(r'$I=(x,y)^4$: ordinary colength $10$, power-count bound $16$ — (22.621)',fontsize=14)
fig.savefig(base/'elliptic-parameter-region.png',dpi=170);plt.close(fig)
print('Saved Figure22.17')

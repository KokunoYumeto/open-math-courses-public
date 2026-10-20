"""Original numerical illustration of regularized point kernels; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U001-regularized-kernels'})
out=Path(__file__).resolve().parent
def bump(x):
    a=np.zeros_like(x,dtype=float);mask=np.abs(x)<1
    a[mask]=np.exp(-1/(1-x[mask]**2))
    return a
# Numerical quadrature sets the color values; normalization in the text is exact.
grid=np.linspace(-1,1,20001)
c=1/np.trapezoid(bump(grid),grid)
fig,axes=plt.subplots(1,3,figsize=(15,5.2),layout='constrained',
                      gridspec_kw={'width_ratios':[1,1,1.15]})
x=np.linspace(-1.1,1.1,701)
norm=Normalize(0,4*(c*np.exp(-1))**2)
for ax,e in zip(axes[:2],[1,.5]):
    rho=c/e*bump(x/e)
    a=ax.imshow(np.outer(rho,rho),extent=[x[0],x[-1],x[0],x[-1]],
                origin='lower',cmap='magma',norm=norm)
    ax.set(xlabel='$x$',ylabel='$y$',title=rf'$\varepsilon={e:g}$')
    ax.text(.5,-.23,'Numerical sample; exact mass 1',ha='center',
            transform=ax.transAxes,fontsize=10)
fig.colorbar(a,ax=list(axes[:2]),shrink=.75,label=r'$K_\varepsilon(x,y)$')
eps=np.geomspace(1e-5,.5,800)
axes[2].loglog(eps,eps*np.log(1/eps),lw=2.5,color='#11768a',
               label=r'$\varepsilon\log(1/\varepsilon)$')
axes[2].loglog(eps,eps,'--',lw=1.8,color='#b34e2d',label=r'$\varepsilon$')
axes[2].set(xlabel=r'$\varepsilon$',ylabel='scalar coefficient',
            title='Logarithmic error coefficient')
axes[2].legend(loc='upper left',fontsize=11)
axes[2].grid(alpha=.17);axes[2].spines[['top','right']].set_visible(False)
name='regularized-point-kernels'
fig.savefig(out/(name+'.png'),dpi=170)
fig.savefig(out/(name+'.svg'),metadata={'Date':None})
p=out/(name+'.svg')
p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')

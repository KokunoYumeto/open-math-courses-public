"""Original illustration of signed cancellation under composition; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U037-openness'})
out=Path(__file__).resolve().parent
def bump(x):
    a=np.zeros_like(x,dtype=float);mask=np.abs(x)<1
    a[mask]=np.exp(-1/(1-x[mask]**2))
    return a
g=np.linspace(-1,1,20001)
c=1/np.trapezoid(bump(g),g)
fig,axes=plt.subplots(1,2,figsize=(12.5,5.3),layout='constrained')
y=np.linspace(-1.35,.6,2401);x=np.linspace(-.8,.8,1601)
for e,col in [(.4,'#b34e2d'),(.15,'#11768a')]:
    v=c/e*(bump(y/e)-bump(y/e+2))
    composition=c/e*bump(x*x/e)
    axes[0].plot(y,v,color=col,lw=2,label=rf'$\varepsilon={e:g}$')
    axes[1].plot(x,composition,color=col,lw=2,label=rf'$\varepsilon={e:g}$')
axes[0].set(xlabel='$y$',ylabel=r'$v_\varepsilon(y)$',
            title='Equal opposite masses in the target')
axes[0].axvspan(y[0],0,color='#ced4d8',alpha=.2)
axes[0].text(-.76,4.5,r'$x^2$ never reaches $y<0$',ha='center',fontsize=11)
axes[1].set(xlabel='$x$',ylabel=r'$v_\varepsilon(x^2)$',
            title='Only the positive packet remains')
axes[1].text(0,4.55,r'Mass $=C_\rho\,\varepsilon^{-1/2}$',
             ha='center',fontsize=12)
for ax in axes:
    ax.axhline(0,color='#606a74',lw=.8)
    ax.grid(alpha=.15);ax.legend(loc='upper right',fontsize=10)
    ax.spines[['top','right']].set_visible(False)
fig.suptitle('Numerical samples of compact smooth profiles',fontsize=12)
name='openness-and-composition'
fig.savefig(out/(name+'.png'),dpi=170)
fig.savefig(out/(name+'.svg'),metadata={'Date':None})
p=out/(name+'.svg')
p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')

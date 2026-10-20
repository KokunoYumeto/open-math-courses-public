"""Tangent and cotangent shear, with both conormal signs. GPT-6 Astra; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['svg.hashsalt']='AN01-tangent-cotangent-shear'
out=Path(__file__).parent
out.mkdir(exist_ok=True,parents=True)
fig,axes=plt.subplots(1,2,figsize=(10.6,5.2),layout='constrained')
fig.patch.set_facecolor('#f8fafc')
x=np.linspace(-1.15,1.15,300)
axes[0].plot(x,0*x,color='#176689',lw=2.6)
axes[1].plot(x,x*x,color='#176689',lw=2.6)
for ax,curved in zip(axes,[False,True]):
    for a in [-.8,0,.8]:
        base=np.array([a,a*a if curved else 0.])
        for lam in [-.3,.3]:
            delta=np.array([-2*a*lam if curved else 0.,lam])
            ax.annotate('',xy=base+delta,xytext=base,
                        arrowprops=dict(arrowstyle='->',lw=2,color='#7d3f92',mutation_scale=13,shrinkA=0,shrinkB=0))
        ax.scatter(*base,s=26,color='#176689',zorder=4)
    a=.8;base=np.array([a,a*a if curved else 0.])
    tangent=.24*np.array([1.,2*a if curved else 0.])
    ax.annotate('',xy=base+tangent,xytext=base,
                arrowprops=dict(arrowstyle='->',lw=2.2,color='#b45025',mutation_scale=13,shrinkA=0,shrinkB=0))
    ax.set(xlim=(-1.55,1.55),ylim=(-.6,1.65),aspect='equal')
    ax.set_facecolor('#f8fafc');ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.16);ax.set_axisbelow(True)
axes[0].set(title='Straight constraint: z = 0',xlabel='x',ylabel='z')
axes[1].set(title='Sheared constraint: w = y²',xlabel='y',ylabel='w')
axes[0].text(-1.4,1.32,r'conormal $(0,\lambda)$',fontsize=12,color='#7d3f92')
axes[0].text(-1.4,.98,r'tangent $(1,0)$',fontsize=12,color='#b45025')
axes[1].text(-1.4,1.45,r'conormal $(-2y\lambda,\lambda)$',fontsize=11.5,color='#7d3f92')
axes[1].text(-.65,1.12,r'tangent $(1,2y)$',fontsize=11.5,color='#b45025')
fig.suptitle(r'$h(x,z)=(x,z+x^2)$'+'\n'+r'$\widehat h(x,z;\xi,\zeta)=(x,z+x^2;\xi-2x\zeta,\zeta)$',fontsize=14)
for ext in ['png','svg']:
    fig.savefig(out/('tangent-cotangent-shear.'+ext),dpi=175,
                metadata={'Date':'2026-10-20'} if ext=='svg' else None)
svg=out/'tangent-cotangent-shear.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)

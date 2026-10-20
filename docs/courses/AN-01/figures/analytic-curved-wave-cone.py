"""Exact curves and covector sections for Exercises 10–11. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':15})
fig,axes=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
r=np.linspace(0,1.6,600)
ax=axes[0]
ax.fill_between(r,-r-r*r,r-r*r,color='#e0f2f0')
for eps,col in [(1,'#176b87'),(-1,'#8c326f')]:
    ax.plot(r,eps*r-r*r,color=col,lw=2,label=fr'$z={eps:+d}r-r^2$')
    for t in [.3,.7,1.15]:
        z=eps*t-t*t
        cov=np.array([2*t-4*eps*t*t,-2*eps*t])
        cov=.19*cov/np.linalg.norm(cov)
        for sign in [-1,1]:
            ax.annotate('',xy=(t+sign*cov[0],z+sign*cov[1]),xytext=(t,z),
                arrowprops=dict(arrowstyle='->',color=col,lw=1.5))
ax.scatter([0],[0],s=40,color='#173c54',zorder=5)
ax.set(xlabel='$r$ (time coordinate)',ylabel='$z$',xlim=(-.28,1.85),ylim=(-4.35,.65),
       title='Curved forward support\nand both conormal signs')
ax.set_aspect('equal');ax.legend(loc='lower left',fontsize=10)
ax=axes[1];theta=np.linspace(0,2*np.pi,600)
ax.plot(np.cos(theta),np.sin(theta),color='#176b87',lw=3,label='All unit vertex covectors')
null=np.array([(a,b) for a in [-1,1] for b in [-1,1]])/np.sqrt(2)
ax.scatter(null[:,0],null[:,1],color='#a93852',s=65,zorder=5,label='Limits of nonvertex conormals')
ax.scatter([1],[0],s=80,facecolors='white',edgecolors='#176b87',lw=2,zorder=6)
ax.annotate('$(1,0)$: supplied by the point source',xy=(1,0),xytext=(-1.28,1.31),
            arrowprops=dict(arrowstyle='->',color='#173c54'),fontsize=10)
ax.axhline(0,color='#b6bdc4',lw=.7);ax.axvline(0,color='#b6bdc4',lw=.7)
ax.set(xlabel=r'$\tau$',ylabel=r'$\xi$',xlim=(-1.5,1.5),ylim=(-1.45,1.6),
       title='The same full vertex fiber\nin all three regularity scales')
ax.set_aspect('equal');ax.legend(loc='lower center',fontsize=9)
for a in axes:a.spines[['top','right']].set_visible(False)
out=Path(__file__).resolve().parent
fig.savefig(out/'analytic-curved-wave-cone.svg')
fig.savefig(out/'analytic-curved-wave-cone.png',dpi=170)
svg=out/'analytic-curved-wave-cone.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')

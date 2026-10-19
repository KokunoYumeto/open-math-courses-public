"""Original illustration of S-unit height and its three local logarithms."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

out=Path(__file__).resolve().parents[1] / 'figures/sunit-place-geometry.png'
log2,log3=np.log(2),np.log(3);H=np.log(9)
fig,axes=plt.subplots(1,2,figsize=(12.4,5.0),layout='constrained')
ax=axes[0]
vertices=np.array([[H,0],[H,-H],[0,-H],[-H,0],[-H,H],[0,H]])
ax.add_patch(Polygon(vertices,facecolor='#dceef3',edgecolor='#21677b',lw=1.6))
for a in range(-4,5):
    for b in range(-3,4):
        u,v=a*log2,b*log3
        if max(abs(u),abs(v),abs(u+v))<=H+1e-12:
            ax.plot(u,v,'.',color='#6f8991',ms=6)
samples=[(3,-2,r'$8/9$','#b65336'),(-3,2,r'$9/8$','#6554a4'),(0,-2,r'$1/9$','#258261')]
offsets=[(-42,13),(12,-20),(10,14)]
for (a,b,label,color),offset in zip(samples,offsets):
    ax.scatter(a*log2,b*log3,s=42,color=color,zorder=4)
    ax.annotate(label,(a*log2,b*log3),xytext=offset,textcoords='offset points',color=color,fontsize=12)
ax.axhline(0,lw=.6,color='#aaa');ax.axvline(0,lw=.6,color='#aaa')
ax.set(xlabel=r'$u=a\log 2$',ylabel=r'$v=b\log 3$',
       xlim=(-2.6,2.6),ylim=(-2.6,2.6),aspect='equal',
       title=r'$h(\pm2^a3^b)=\max(|u|,|v|,|u+v|)$')
ax.text(0,2.35,r'Height region: $h\leq\log9$',ha='center',fontsize=10)
ax=axes[1];places=[r'$\infty$',r'$2$',r'$3$'];base=np.arange(3)
for k,(a,b,label,color) in enumerate(samples):
    vals=[a*log2+b*log3,-a*log2,-b*log3]
    assert abs(sum(vals))<1e-12
    ax.bar(base+(k-1)*.23,vals,width=.21,label=label,color=color)
ax.axhline(0,color='#444',lw=.8)
ax.axhline(-H/3,color='#555',ls=':',lw=1.2,label=r'$-h(x)/3=-\log9/3$')
ax.set(xticks=base,xticklabels=places,ylabel=r'Unscaled local logarithm $\lambda_v(x)$',
       title='The smallest place can be finite',ylim=(-2.6,3.4))
ax.legend(frameon=False,fontsize=10,loc='upper right',ncol=2)
ax.text(.5,.025,r'$\lambda_\infty+\lambda_2+\lambda_3=0$',transform=ax.transAxes,ha='center',fontsize=11)
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.12);ax.set_axisbelow(True)
fig.suptitle('S-unit geometry for '+r'$S=\{\infty,2,3\}$'+
             '\nLattice points illustrate a height bound; they are not all solutions of '+r'$x+y=1$.',fontsize=12)
fig.savefig(out,dpi=165)
plt.close(fig)
print(out)

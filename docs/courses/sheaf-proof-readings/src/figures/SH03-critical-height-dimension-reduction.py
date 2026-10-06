"""Exact critical-height model on T^2; original diagram, CC0.

GPT-6 Astra (OpenAI), Ultra, October 2026.
The square is a parameter domain with opposite edges identified, not an
embedded square model of the torus. No numerical approximation enters the
rank-drop set or the displayed fibre/image coordinates.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                    'svg.fonttype':'none','svg.hashsalt':'SH03-critical-height-dimension-reduction-v1','axes.spines.top':False,
                    'axes.spines.right':False})
fig=plt.figure(figsize=(11.4,6.1),layout='constrained')
grid=fig.add_gridspec(2,2,width_ratios=[1.2,1],height_ratios=[1,.12])
ax=fig.add_subplot(grid[0,0]);image=fig.add_subplot(grid[0,1])
blue='#2466a2';gold='#a45b00';green='#087b5b'
pi=np.pi
for value in [0,pi,2*pi]:
    ax.plot([value,value],[0,2*pi],color=blue,lw=2)
    ax.plot([0,2*pi],[value,value],color=blue,lw=2)
ax.plot([0,2*pi],[pi,pi],color=gold,lw=4,zorder=3)
for theta in [pi/3,5*pi/3]:
    ax.plot([theta,theta],[0,2*pi],color=green,lw=2,ls=(0,(4,3)))
    ax.scatter([theta],[pi],s=58,color=green,edgecolor='white',zorder=5)
ax.set(xlim=(-.08,2*pi+.08),ylim=(-.08,2*pi+.08),aspect='equal',
       xlabel=r'$\theta$',ylabel=r'$\phi$')
ax.set_xticks([0,pi/3,pi,5*pi/3,2*pi],['0',r'$\pi/3$',r'$\pi$',r'$5\pi/3$',r'$2\pi$'])
ax.set_yticks([0,pi,2*pi],['0',r'$\pi$',r'$2\pi$'])
ax.set_title('Source torus: opposite square edges identified',fontsize=12,pad=16)
ax.annotate(r'$h=-1$ on the entire gold circle',xy=(pi*.8,pi),
            xytext=(pi*.26,pi*1.48),fontsize=10,color=gold,
            arrowprops={'arrowstyle':'->','color':gold})

image.axis('off');image.set(xlim=(-1.3,1.3),ylim=(-1,1.6))
image.text(0,1.43,r'$f(\theta,\phi)=\cos\theta,\quad h(\theta,\phi)=\cos\phi$',ha='center',fontsize=13)
image.text(0,1.04,r'$g=(\det d(f,h))^2=\sin^2\theta\,\sin^2\phi$',ha='center',fontsize=13)
image.text(0,.70,r'$Z=\{g=0\}$ meets every fibre of $f$.',ha='center',fontsize=12)
image.plot([-1,1],[0,0],color=gold,lw=5,solid_capstyle='round')
image.scatter([-1,1],[0,0],color=blue,s=60,zorder=4)
image.scatter([.5],[0],color=green,s=65,edgecolor='white',zorder=5)
for x,label in [(-1,r'$-1$'),(.5,r'$1/2$'),(1,r'$1$')]:image.text(x,-.21,label,ha='center',fontsize=12)
image.text(0,-.49,r'$f(Z)=f(T^2)=[-1,1]$',ha='center',fontsize=14)
image.text(0,-.79,'The minimizing circle already covers the whole interval;\nits map is two-to-one over the open interval.',ha='center',fontsize=10)

legend=fig.add_subplot(grid[1,:]);legend.axis('off')
legend.legend(handles=[Line2D([0],[0],color=blue,lw=2,label=r'Rank-drop set $Z$'),
                       Line2D([0],[0],color=gold,lw=4,label=r'Minimizing circle $\phi=\pi$'),
                       Line2D([0],[0],color=green,lw=2,ls='--',label=r'The two circles in $f^{-1}(1/2)$')],
              loc='center',ncol=3,frameon=False,fontsize=11)
fig.suptitle('Reducing a compact source while keeping its entire image',fontsize=15)
root=Path(__file__).resolve().parents[2];out=root/'figures/SH03-critical-height-dimension-reduction.svg';out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,metadata={'Title':'Critical-height dimension reduction on the torus',
                         'Creator':'GPT-6 Astra (OpenAI), Ultra',
                         'Description':'Exact parameter-domain diagram for f=cos(theta), h=cos(phi) and the squared Jacobian determinant; CC0 original programme diagram.',
                         'Date':None})
plt.close(fig)
print(out)

"""Two exact coordinate projections of a fixed radial slice, numerically sampled."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
here=Path(__file__).resolve().parent;dest=here/'isotropic-cusp-and-covector-direction.svg'
plt.rcParams.update({'svg.fonttype':'path','font.size':17,'axes.labelsize':17,'axes.titlesize':18,'xtick.labelsize':13,'ytick.labelsize':13})
fig,axs=plt.subplots(2,1,figsize=(6.6,8.8))
def points(r):return r*r,-2*r**3/3-r**4/2,r+r*r
for sign,color in [(-1,'#175e8f'),(1,'#b55a17')]:
    r=np.linspace(0,.24*sign,501);x1,x2,u=points(r)
    axs[0].plot(x1,x2,color=color,lw=2.4)
    axs[1].plot(u,x1,color=color,lw=2.4,label='r < 0' if sign<0 else 'r > 0')
for ax in axs:
    ax.axhline(0,color='#999',lw=.7);ax.axvline(0,color='#999',lw=.7)
    ax.grid(alpha=.15);ax.plot(0,0,'o',color='#222',markersize=5)
axs[0].set_title('The base projection has a cusp',pad=14)
axs[0].set_xlabel(r'$x_1=r^2$')
axs[0].set_ylabel(r'$x_2=-2r^3/3-r^4/2$')
axs[1].set_title('Covector direction detects a smooth lift',pad=14)
axs[1].set_xlabel(r'$\xi_1/\xi_2=r+r^2$')
axs[1].set_ylabel(r'$x_1=r^2$')
axs[1].legend(loc='upper left',fontsize=14)
axs[1].annotate('',(.075,0),(0,0),arrowprops={'arrowstyle':'->','color':'#444','lw':1.5})
axs[1].text(.02,.039,r'$(1,0)$ tangent at $r=0$',ha='center',fontsize=12)
for rr in [-.2,.2]:
    xx,yy,uu=points(rr)
    axs[0].plot(xx,yy,'o',color='#555',ms=4)
    axs[0].annotate('r = '+str(rr),(xx,yy),xytext=(-25,13 if rr<0 else -22),textcoords='offset points',fontsize=13)
fig.text(.5,.023,'Two projections of the slice ρ = 1.\nExact relation and immersion: (5.3)–(5.5).',ha='center',fontsize=14)
fig.subplots_adjust(left=.2,right=.96,top=.945,bottom=.13,hspace=.47)
fig.savefig(dest)
fig.savefig(here/'isotropic-cusp-and-covector-direction.png',dpi=160)
print(dest.name)

"""Reproduce the exact C1, C3 and C4 exercise models. Original figure, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-clean-composition',
                           'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(3,1,figsize=(8,12),layout='constrained')
blue,red,green='#12647b','#a4412b','#286542'
q=np.linspace(-1.15,1.15,1001)
h=np.zeros_like(q);inside=np.abs(q)<1
h[inside]=np.exp(-2/(1-q[inside]**2))
ax=axes[0];ax.plot(q,h,color=blue,lw=2.4);ax.fill_between(q,h,color=blue,alpha=.2)
ax.set(xlabel=r'$q$ on the fibre $F=E=\mathbb{R}$',ylabel=r'coefficient $a(q)b(q)$',
       title='1. Excess produces a density to integrate (Exercise C1)')
ax.text(.02,.87,r'$a=b=e^{-1/(1-q^2)}$ for $|q|<1$; zero outside',transform=ax.transAxes)
ax.text(.02,.72,r'$a|dq|^{1/2}\otimes b|dq|^{1/2}\mapsto ab|dq|$',transform=ax.transAxes)
ax.text(.02,.57,r'Composed image: one point; excess $e=1$',transform=ax.transAxes)
ax.set_ylim(0,.30);ax.grid(alpha=.16)
ax=axes[1];ax.plot(q,q*q,color=red,lw=2.4,label=r'$p=q^2$')
ax.axhline(0,color=blue,lw=2.4,label=r'$p=0$');ax.scatter([0],[0],s=55,color=green,zorder=5)
ax.set(xlabel='$q$',ylabel='$p$',title='2. A smooth intersection can fail to be clean (Exercise C3)')
ax.text(.20,.87,r'Intersection: $\{(0,0)\}$, tangent dimension $0$',transform=ax.transAxes)
ax.text(.20,.76,r'Common tangent: $q$-axis, dimension $1$',transform=ax.transAxes)
ax.set_ylim(-.25,1.6);ax.legend(loc='lower right');ax.grid(alpha=.16)
t=np.linspace(0,2*np.pi,1401);ax=axes[2]
ax.plot(np.sin(t),np.sin(2*t),color=blue,lw=2.4)
s=np.linspace(-.32,.32,40)
ax.plot(s,2*s,'--',color=red,label=r'$t=0$: tangent $\mathbb{R}(1,2)$')
ax.plot(-s,2*s,':',color=green,lw=2.4,label=r'$t=\pi$: tangent $\mathbb{R}(-1,2)$')
ax.scatter([0],[0],color='black',s=35,zorder=5)
ax.set(xlabel='$x$',ylabel='$y$',title='3. Proper immersion, disconnected crossing fibre (Exercise C4)')
ax.text(.02,.97,r'$t\mapsto(\sin t,\sin 2t)$ on the circle',transform=ax.transAxes,va='top')
ax.set_xlim(-1.2,1.2);ax.set_ylim(-1.5,1.35);ax.legend(loc='lower left',fontsize=10)
ax.grid(alpha=.16)
fig.savefig(out/'composition-geometry.svg',metadata={'Date':None,'Creator':'Original AN-04 programme figure; CC0'})
fig.savefig(out/'composition-geometry.png',dpi=150)
plt.close(fig)

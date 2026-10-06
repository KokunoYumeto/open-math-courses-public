"""Exact global amplitude norm and forcing integrability. Original CC0.

Reproduce these PNG/SVG outputs with NumPy and Matplotlib. All curves are
the exact integrands in global-radiation-and-flux.md, Theorem 5.5.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                           'svg.hashsalt': 'global-amplitude-norms',
                           'axes.spines.top': False, 'axes.spines.right': False})
out=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
radius=2*np.sqrt(np.pi)
ax.add_patch(Circle((0,0),radius,facecolor='#c4e1ef',edgecolor='#216184',lw=2))
ax.axhline(0,color='#7c8b99',lw=.8);ax.axvline(0,color='#7c8b99',lw=.8)
ax.plot([0,radius],[0,0],color='#a45429',lw=2)
ax.text(1.65,-.7,r'$2\sqrt{\pi}$',color='#a45429',ha='center',fontsize=14)
ax.text(0,4.65,r'$\|[u]\|^2=(s^2+t^2)/(4\pi)$',ha='center',fontsize=14)
ax.text(0,-4.65,r'$(v_+,v_-)=(sa,ta)$, $\|a\|_2=1$',ha='center')
ax.set(xlim=(-5.2,5.2),ylim=(-5.2,5.2),xlabel=r'$s$',ylabel=r'$t$',title='A slice of the completed radiation unit ball')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.15)
x=np.geomspace(1,1000,1500);g=np.sqrt(1+4*x*x);v2=(1+x*x)**(-1.25)
bx.loglog(x,g*v2,lw=2,color='#216184',label=r'$g|v|^2\asymp |\eta|^{-3/2}$: integrable')
bx.loglog(x,g**3*v2,lw=2,color='#a45429',label=r'$g^3|v|^2\asymp |\eta|^{1/2}$: not integrable')
bx.set(xlabel=r'$|\eta|\geq1$',ylabel=r'exact integrand with respect to $d\eta$',title='The gradient factor restricts the forced pairs')
bx.legend(loc='center right',fontsize=11);bx.grid(alpha=.15,which='both')
fig.savefig(out/'global-amplitude-norms.svg',metadata={'Date':None,'Creator':'Original CC0 mathematical figure'})
fig.savefig(out/'global-amplitude-norms.png',dpi=180,metadata={'Software':'Original CC0 mathematical figure'})
plt.close(fig)

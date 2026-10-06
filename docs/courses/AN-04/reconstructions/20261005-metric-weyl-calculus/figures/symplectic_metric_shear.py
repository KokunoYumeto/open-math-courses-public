"""CC0. Exact metric ellipses in WC1, sampled only for drawing."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path'})
t=np.linspace(0,2*np.pi,1201);x=2*np.cos(t);xi=np.sin(t)
fig,ax=plt.subplots(figsize=(8,8.1))
fig.subplots_adjust(left=.1,right=.98,bottom=.16,top=.91)
ax.plot(x,xi,color='#087d8b',lw=2.5,label=r'$g=\frac{1}{4}\,dx^2+d\xi^2$')
ax.plot(x,x+xi,color='#b74d37',lw=2.5,label=r'$\chi^*g=\frac{1}{4}\,dx^2+(d\xi-dx)^2$')
for tt in [0,np.pi/2,np.pi,3*np.pi/2]:
 xx=2*np.cos(tt);zz=np.sin(tt)
 ax.scatter([xx],[zz],s=42,color='#087d8b',zorder=4)
 ax.scatter([xx],[xx+zz],s=42,color='#b74d37',zorder=4)
 if abs(xx)>.1:ax.annotate('',xy=(xx,xx+zz),xytext=(xx,zz),arrowprops={'arrowstyle':'->','color':'#666','lw':1.4})
ax.set(xlabel=r'$x$',ylabel=r'$\xi$',xlim=(-2.6,2.6),ylim=(-2.7,2.7),
 title=r'$\chi(x,\xi)=(x,\xi-x)$; the pullback ellipse is $\chi^{-1}$ of the original')
ax.axhline(0,color='#aaa',lw=.6);ax.axvline(0,color='#aaa',lw=.6)
ax.set_aspect('equal');ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=12)
fig.text(.5,.025,r'Both unit ellipses: $\det G=\frac{1}{4}$, area $2\pi$, Planck parameter $h=\frac{1}{2}$',ha='center',fontsize=12)
for ext in ['png','svg']:fig.savefig(Path(__file__).with_suffix('.'+ext),dpi=150,bbox_inches='tight')

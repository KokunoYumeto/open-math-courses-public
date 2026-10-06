"""CC0 figure for SP8. Coordinates are exact; displayed curves are sampled."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path'})
fig,axs=plt.subplots(2,1,figsize=(8,8.8),constrained_layout=True)
y=np.linspace(-1,1,601)
axs[0].plot(y,y*y,color='#087d8b',lw=2.5,label=r'$s=X(y)=y^2$')
for yy in [0,.5,1]:
 axs[0].scatter([yy],[yy*yy],s=40,color='#b74d37',zorder=3)
axs[0].set(xlabel=r'$y$',ylabel=r'$s$',title='The critical graph is curved')
axs[0].legend(loc='upper center');axs[0].grid(alpha=.2)
r=np.linspace(-1,1,601)
for yy,c in [(0,'#087d8b'),(.5,'#b74d37'),(1,'#6952a3')]:
 axs[1].plot(r,r*r+yy**4,color=c,lw=2.4,label=rf'$y={yy:g}$, $v=y^4={yy**4:g}$')
 axs[1].axhline(yy**4,color=c,ls='--',alpha=.65)
 axs[1].scatter([0],[yy**4],color=c,s=42,zorder=4)
axs[1].set(xlabel=r'$r=s-y^2$ (normal displacement)',ylabel=r'$f=r^2+y^4$',
 title='The square vanishes on the graph; the residual stays')
axs[1].legend(loc='upper center');axs[1].grid(alpha=.2)
fig.suptitle(r'$f(s,y)=(s-y^2)^2+y^4=v(y)+q(s,y)^2$',fontsize=17)
for ext in ['png','svg']:fig.savefig(Path(__file__).with_suffix('.'+ext),dpi=155)

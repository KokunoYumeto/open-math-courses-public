"""Exact covector sections for Exercises 14–15. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14})
fig,axs=plt.subplots(1,2,figsize=(11,5),layout='constrained')
s=np.linspace(-1.3,1.3,500)
ax=axs[0];ax.plot(s,s*s,color='#176b87',lw=2)
for q in [-1,-.5,0,.5,1]:
 for sign in [-1,1]:
  cov=sign*.21*np.array([-2*q,1])
  ax.annotate('',xy=(q+cov[0],q*q+cov[1]),xytext=(q,q*q),
              arrowprops=dict(arrowstyle='->',color='#8c326f',lw=1.5))
ax.scatter([0],[0],s=65,facecolors='white',edgecolors='#176b87',lw=2,zorder=5)
ax.annotate('Weight $s^2=0$, but still in its support',xy=(0,0),xytext=(-1.5,-.52),
            fontsize=10,arrowprops=dict(arrowstyle='->',color='#173c54'))
ax.set(xlabel='$s$',ylabel='$t$',xlim=(-1.65,1.65),ylim=(-.7,2.1),
       title='Analytic density on $t=s^2$\nBoth normal signs remain at a zero')
ax.set_aspect('equal')
ax=axs[1];th=np.linspace(0,2*np.pi,500)
ax.plot(np.cos(th),np.sin(th),color='#176b87',lw=3,label='Analytic wavefront: whole circle')
ax.scatter([0,0],[-1,1],s=85,color='#a93852',zorder=5,label='Smooth wavefront: normal pair')
ax.axhline(0,color='#b6bdc4',lw=.7);ax.axvline(0,color='#b6bdc4',lw=.7)
ax.set(xlabel=r'$\eta$ (tangential)',ylabel=r'$\zeta$ (normal)',
       xlim=(-1.35,1.35),ylim=(-1.5,1.35),
       title=r'Flat coefficient $h(s)\delta_0(t)$'+'\nUnit covectors at the origin')
ax.set_aspect('equal');ax.legend(loc='lower center',fontsize=9)
for a in axs:a.spines[['top','right']].set_visible(False)
out=Path(__file__).resolve().parent;name='tangential-coefficients-and-normal-directions'
fig.savefig(out/(name+'.png'),dpi=170);fig.savefig(out/(name+'.svg'))
p=out/(name+'.svg');p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')

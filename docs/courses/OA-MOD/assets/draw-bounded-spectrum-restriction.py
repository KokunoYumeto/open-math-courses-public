"""BK01: functions off the spectrum vanish in the interval calculus.

The example is T=diag(0,1), J=[-1,2], lambda=-1/2, delta=1/5.
The plotted geometric curve is a proved upper bound, not the actual norm,
which is zero. The abstract proof applies in every Hilbert dimension.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':13,'svg.fonttype':'path',
 'svg.hashsalt':'oa-mod-bounded-spectrum-restriction-v1'})
fig=plt.figure(figsize=(12,7.2))
fig.suptitle('The calculus depends only on values on the spectrum',fontsize=20,y=.96)
a=fig.add_axes([.08,.48,.39,.31])
t=np.linspace(-1,2,1501);h=np.maximum(0,1-5*np.abs(t+.5))
a.plot(t,h,lw=2,color='#176c91',label=r'$h(t)=\max(0,1-5|t+1/2|)$')
a.axvspan(-.7,-.3,color='#176c91',alpha=.10)
a.scatter([0,1],[0,0],color='#ab461f',s=65,zorder=5)
a.annotate(r'$\sigma(T)=\{0,1\}$',(0,0),(.63,.6),
 arrowprops={'arrowstyle':'->','color':'#ab461f'},color='#ab461f')
a.text(-.93,1.10,r'$h(t)=\max(0,1-5|t+1/2|)$',fontsize=10)
a.set(xlim=(-1,2),ylim=(-.1,1.2),xlabel=r'$t\in J=[-1,2]$',ylabel=r'$h(t)$')
a.set_title(r'$T=\mathrm{diag}(0,1),\quad h(T)=0$',fontsize=15)
a.grid(alpha=.2)
b=fig.add_axes([.61,.48,.33,.31]);n=np.arange(0,9)
b.semilogy(n,.4**n,'o-',lw=2,color='#176c91')
b.set(xlabel='integer n',ylabel='proved upper bound',xticks=np.arange(0,9,2))
b.set_title(r'$\|h(T)\|\leq(2/5)^n$',fontsize=15)
b.grid(alpha=.2)
b.text(.5,-.30,'The actual norm is zero at every n.',transform=b.transAxes,ha='center',fontsize=12)
a.text(.5,-.30,r'$\lambda=-1/2,\quad\delta=1/5,\quad\|(T-\lambda)^{-1}\|=2$',
 transform=a.transAxes,ha='center',fontsize=12)
c=fig.add_axes([.04,.065,.92,.23]);c.axis('off')
c.text(.5,.92,'Why the off-spectrum part disappears',ha='center',fontsize=16,fontweight='bold')
c.text(.5,.64,r'$h(T)=(T-\lambda I)^{-n}[(t-\lambda)^n h(t)](T)$',
 ha='center',fontsize=18)
c.text(.5,.36,r'$\|h(T)\|\leq'
 r'\left(\delta\|(T-\lambda I)^{-1}\|\right)^n\|h\|_\infty'
 r'\ \longrightarrow\ 0$',ha='center',fontsize=18)
c.text(.5,.065,'Localize away from the spectrum, then use a finite partition and uniform approximation.',
 ha='center',fontsize=12)
fig.text(.5,.018,'Proof: BK01, “Restriction to the spectrum”. The geometric decay is an upper bound in arbitrary dimension.',
 ha='center',fontsize=11)
out=Path(__file__).with_name('bounded-spectrum-restriction.svg')
fig.savefig(out,metadata={'Date':None,'Creator':'Original course illustration; BK01'})
print(out)

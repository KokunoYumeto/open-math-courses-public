"""Exact expanding-domain slices and complex normal ratios. AN01-U108; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','svg.hashsalt':'AN01-U108'})
R=2.;c=.25
x=np.linspace(-np.sqrt(R*R-c),np.sqrt(R*R-c),601)
d=np.sqrt(x*x+c)
fig,axes=plt.subplots(1,2,figsize=(12.5,5.4),layout='constrained')
colors=['#245a9c','#16916a','#933fad']
for a,color in reversed(list(zip([.25,.5,1.],colors))):
 y=a*(R-d)
 axes[0].fill_between(x,0,y,color=color,alpha=.12)
 axes[0].plot(x,y,color=color,lw=2,label=r'$a='+str(a)+'$')
axes[0].axhline(0,color='#303945',lw=1.2)
axes[0].annotate('',xy=(0,1),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#303945'})
axes[0].plot([0],[1],'o',color='#303945')
axes[0].annotate(r'Target $(0,1)$',xy=(0,1),xytext=(.38,1.18),arrowprops={'arrowstyle':'-','color':'#303945'})
axes[0].set(xlim=(-2.05,2.05),ylim=(-.08,1.67),xlabel=r'$x=\mathrm{Re}\,z_1$',ylabel=r'$s=\mathrm{Re}\,z_2$',
            title='Nested convex domains\nReal slice with both imaginary parts zero')
axes[0].legend(loc='upper left',fontsize=11)
for a,color in zip([.25,.5,1.],colors):
 axes[1].plot(x,a*x/d,color=color,lw=2,label=r'$a='+str(a)+'$')
for sign in [-1,1]:axes[1].axhline(sign,color='#46566b',ls='--',lw=1.3)
axes[1].axhline(0,color='#46566b',lw=.7)
axes[1].set(xlim=(-2.05,2.05),ylim=(-1.18,1.18),xlabel=r'$x=\mathrm{Re}\,z_1$',ylabel=r'$\zeta^\prime/\zeta_2=ax/\sqrt{x^2+1/4}$',
            title=r'Complex normal on this slice: $\zeta_2=1$'+'\nStrictly inside the cone bound')
axes[1].text(.05,1.025,r'$\epsilon=1$',fontsize=12)
axes[1].grid(alpha=.16)
fig.savefig(out/'analytic-cauchy-continuation.png',dpi=170)
svg=out/'analytic-cauchy-continuation.svg'
fig.savefig(svg,metadata={'Date':None})
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
plt.close(fig)

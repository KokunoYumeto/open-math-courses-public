"""Reproduce the two exact half-plane conditions in the complex rotation example.

Original figure source: CC0. Uses only Matplotlib and NumPy; no TeX compiler.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,axes=plt.subplots(1,2,figsize=(11,4.7),layout='constrained')
left,right=axes
left.set_xlim(-5,2);left.set_ylim(-2,4)
left.axhline(0,color='#87909a',linewidth=.8);left.axvline(0,color='#87909a',linewidth=.8)
left.plot([-5,0],[0,0],color='#ab303b',linewidth=4)
left.scatter([0],[0],color='#ab303b',s=45,zorder=4)
left.text(-3.9,-.7,r'Excluded: $\kappa\leq0$ real',color='#ab303b',fontsize=12)
left.scatter([-4,-3],[2,2],color=['#26669b','#13745b'],s=65,zorder=5)
left.annotate('',xy=(-3,2),xytext=(-4,2),arrowprops={'arrowstyle':'->','color':'#13745b','lw':2})
left.text(-4.8,2.45,r'$p_1=-4+2i$',color='#26669b')
left.text(-2.8,2.45,r'$\kappa=-3+2i$',color='#13745b')
left.text(-4.0,1.45,r'$\mathrm{Tr}_+Q=1$',color='#13745b')
left.set_title('Add the quadratic correction first',pad=12)
left.set_xlabel('Real part');left.set_ylabel('Imaginary part')
right.set_xlim(-.5,2.5);right.set_ylim(-4.5,1)
right.axhline(0,color='#87909a',linewidth=.8);right.axvline(0,color='#87909a',linewidth=1.4)
a=np.linspace(0,2.5,400)
right.fill_between(a,-4.5,-1.5*a,color='#aedecb',alpha=.8)
right.plot(a,-1.5*a,color='#13745b',lw=1.8,linestyle='--')
right.text(.8,-.1,r'$-3a-2b=0$',color='#13745b',rotation=-37)
right.scatter([1],[-2],color='#103b51',s=70,zorder=5)
right.annotate(r'$z=1-2i$',xy=(1,-2),xytext=(1.25,-2.25),color='#103b51')
right.text(.25,-3.75,r'$a>0$ and $-3a-2b>0$',color='#13745b')
right.set_title(r'Choose $z=a+ib$ in the intersection',pad=12)
right.set_xlabel(r'$a=\mathrm{Re}\,z$');right.set_ylabel(r'$b=\mathrm{Im}\,z$')
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
 ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_name('complex-rotation.png'),dpi=170,
            metadata={'Software':'Matplotlib; original course figure, CC0'})
plt.close(fig)

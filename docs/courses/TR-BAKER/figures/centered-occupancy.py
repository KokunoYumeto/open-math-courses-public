"""Figure 6.1: the exact marginals and quantile bounds in Lemma 6.4.

Written by GPT-6.1 Sol (OpenAI), Ultra. Original plot code: CC0.
The integer nodes and all constants are specified in the lesson's example.
Font glyphs retain their licences. Requires numpy and matplotlib.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12.2,4.9),layout='constrained')
ax=axes[0]
ax.bar([0,1,2,3],[2/6,1/6,1/6,2/6],width=1,align='center',
       color='#3c8ba8',edgecolor='white',linewidth=1.4)
ax.axhline(1/3,color='#ae4a35',ls='--',lw=1.6,label=r'Density cap $S/N=1/3$')
ax.set(xlim=(-.7,3.7),ylim=(0,.405),xlabel=r'$y$',ylabel='Probability density',
       title='Spread each integer node over a unit interval')
ax.set_xticks([-.5,.5,1.5,2.5,3.5])
ax.set_yticks([0,1/6,1/3],['0','1/6','1/3'])
ax.legend(loc='upper center',frameon=False,fontsize=11)

ax=axes[1]
t=np.linspace(0,6,601)
y=np.piecewise(t,[t<=2,(t>2)&(t<=3),(t>3)&(t<=4),t>4],
               [lambda u:-.5+u/2,lambda u:.5+(u-2),
                lambda u:1.5+(u-3),lambda u:2.5+(u-4)/2])
ax.plot(t,y,color='#3c8ba8',lw=2.6,label='Increasing quantile of the node marginal')
ax.plot(t,-.5+t/2,color='#ae4a35',ls='--',lw=1.5,label='Lower and upper envelopes')
ax.plot(t,.5+t/2,color='#ae4a35',ls='--',lw=1.5)
ax.plot(t[t<=3],(-.5+t/2)[t<=3],color='#543877',lw=4,alpha=.75)
ax.plot(t[t>=3],(.5+t/2)[t>=3],color='#543877',lw=4,alpha=.75,
        label='Envelope used in the upper bound')
ax.axvline(3,color='#777777',lw=1,ls=':')
ax.text(1.3,3.85,r'$x(t)<0$',ha='center',color='#543877')
ax.text(4.7,3.85,r'$x(t)>0$',ha='center',color='#543877')
ax.set(xlim=(0,6),ylim=(-.7,4.2),xlabel=r'Quantile parameter $t\in[0,N]$',
       ylabel=r'$y(t)$',title=r'Use the sign of $x(t)=t/2-3/2$')
ax.legend(loc='lower right',frameon=False,fontsize=10)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=170,facecolor='white')
plt.close(fig)

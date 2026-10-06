"""Reproducible finite-range numerical illustration; it is not proof of global bounds."""
from pathlib import Path
import numpy as np
import scipy.special as special
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent;dest=here/'airy-transition-and-derivative.svg'
plt.rcParams.update({'svg.fonttype':'path','font.size':17,'axes.labelsize':17,'axes.titlesize':18,'legend.fontsize':15,'xtick.labelsize':14,'ytick.labelsize':14})
r=np.linspace(-12,8,4001);ai,aip,_,_=special.airy(r)
fig,axes=plt.subplots(2,1,figsize=(6.6,8.8),sharex=True)
for ax in axes:
    ax.axvline(0,color='#777',lw=1);ax.axhline(0,color='#777',lw=.8)
    ax.grid(alpha=.18);ax.set_xlim(-12,8)
axes[0].plot(r,ai,color='#175e8f',lw=2,label=r'$\operatorname{Ai}(r)$')
axes[0].plot(r,aip,color='#b55a17',lw=2,label=r'$\operatorname{Ai}^{\prime}(r)$')
axes[0].set_title('Two stationary points meet at r = 0',pad=15)
axes[0].set_ylabel('Airy value');axes[0].legend(loc='upper right')
axes[1].plot(r,ai*(1+abs(r))**.25,color='#175e8f',lw=2,label=r'$\operatorname{Ai}(r)(1+|r|)^{1/4}$')
axes[1].plot(r,aip*(1+abs(r))**(-.25),color='#b55a17',lw=2,label=r'$\operatorname{Ai}^{\prime}(r)(1+|r|)^{-1/4}$')
axes[1].set_title('Divide by the proved polynomial weights',pad=15)
axes[1].set_ylabel('Weighted value');axes[1].set_xlabel('Real argument r')
axes[1].legend(loc='lower left',fontsize=13)
fig.text(.5,.025,'Numerical samples on [−12, 8].\nGlobal estimates: Theorem 1.3.',ha='center',fontsize=15)
fig.subplots_adjust(left=.17,right=.97,top=.94,bottom=.13,hspace=.27)
fig.savefig(dest)
fig.savefig(here/'airy-transition-and-derivative.png',dpi=160)
print(dest.name)

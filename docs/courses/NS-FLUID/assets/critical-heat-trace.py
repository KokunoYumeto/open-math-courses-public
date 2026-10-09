"""Exact heat-orbit norm formulas proved in NS-FLUID-07 Exercises 4 and 5."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
T=np.geomspace(1e-7,1,500)
nu=1.0
s=1+4*np.pi*nu*T
# expm1 retains the small-time values without subtractive cancellation.
one_minus=lambda n: -np.expm1(-n*np.log1p(4*np.pi*nu*T))
Z4=np.pi/(32*nu)*one_minus(4)+np.pi**2/(4*nu)*one_minus(5)+25*np.pi**3/(48*nu)*one_minus(6)
trace=np.sqrt(8*np.pi/3)
fig,axes=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
axes[0].semilogx(T,np.full_like(T,trace),color='#136778',lw=2.5)
axes[0].set(ylim=(0,3.5),xlabel='Original time interval length T',
            ylabel='Initial-trace norm',title='The source norm retains its initial trace')
axes[0].text(.035,.22,r'$\sup_{0<t<T}\|A^{1/4}e^{-tA}b\|_2=\sqrt{8\pi/3}$',
             transform=axes[0].transAxes,fontsize=12)
axes[1].loglog(T,Z4**.25,color='#a44e24',lw=2.5)
axes[1].set(xlabel='Original time interval length T',ylabel=r'$\|S_1(\cdot)b\|_{L^4(0,T;H^1)}$',
            title='The actual contraction norm tends to zero')
for ax in axes:
    ax.grid(True,which='major',alpha=.25)
fig.suptitle(r'$b(x)=(-2\pi x_2,2\pi x_1,0)e^{-\pi|x|^2}$; original source viscosity $\nu=1$',fontsize=13)
fig.savefig(HERE/'critical-heat-trace.png',dpi=180)
fig.savefig(HERE/'critical-heat-trace.svg')
plt.close(fig)

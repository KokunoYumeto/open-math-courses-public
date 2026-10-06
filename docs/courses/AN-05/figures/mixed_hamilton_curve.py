"""Exact original CC0 illustration of the mixed weighted Hamilton model."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

tau=np.linspace(-1,1,601)
t=2*tau
z=2*tau**3
xi2=-96*tau**7/7
q=t**9+t**3*z**2+t**2*xi2/2
xi1=-3*q/2
assert np.allclose(2*xi1+3*q,0,atol=1e-12)
assert np.allclose(q,3616*tau**9/7,rtol=1e-12,atol=1e-12)
assert np.allclose(9*t**8+3*t**2*z**2+t*xi2,16272*tau**8/7,rtol=1e-12,atol=1e-12)

fig,axes=plt.subplots(1,2,figsize=(11.5,5),layout='constrained')
fig.suptitle(r'$q=t^9+t^3z^2+t^2\xi_2/2,\quad h=2\xi_1+3q$',fontsize=15)
axes[0].plot(t,z,color='#076e92',lw=2.4)
for u in [-1,-.5,0,.5,1]:
 axes[0].scatter([2*u],[2*u**3],color='#076e92',s=26)
 axes[0].annotate(r'$\tau='+str(u)+r'$',(2*u,2*u**3),xytext=(6,6),textcoords='offset points',fontsize=9)
axes[0].set(xlabel=r'$t=2\tau$',ylabel=r'$z=2\tau^3$',title='Projection to the two base coordinates')
axes[0].set_xlim(-2.3,2.3);axes[0].set_ylim(-2.4,2.6)
axes[0].grid(alpha=.2)
axes[1].plot(tau,xi2,color='#b95710',lw=2.4)
axes[1].set(xlabel=r'$\tau$',ylabel=r'$\xi_2=-96\tau^7/7$',title='The transverse frequency along the same curve')
axes[1].grid(alpha=.2)
axes[1].set_xlim(-1.05,1.05);axes[1].set_ylim(-15.5,15.5)
fig.supxlabel(r'Exact Hamilton curve from zero; $h=0$ along it. It is not a curve in $q=0$.',fontsize=10)
fig.savefig(Path(__file__).with_name('mixed-hamilton-curve.png'),dpi=180,metadata={'Software':'Matplotlib; original CC0 figure'})

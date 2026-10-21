"""Reproduce Figure22.13. Numerical samples illustrate a proved bound."""
from pathlib import Path
import importlib.util
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('elliptic_growth_check',root/'elliptic-explicit-growth-check.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
mp.mp.dps=60
times=np.linspace(-3,3,301)
actual=[]
for t in times:
    # Evaluate only in a fundamental cell, then apply exact scalar automorphy.
    n=int(np.floor(t+0.5)); t0=mp.mpf(str(t))-n
    z0=mp.mpf(1)/3+1j*t0
    phi,_,wp,wpp=module.elliptic_values(1j,z0,terms=60)
    M=2*n*t0+n*n-n
    actual.append(float(3*mp.log(abs(phi))+mp.log(max(1,abs(wp),abs(wpp)))+3*mp.pi*M))
upper=np.log(3.33)+3*np.pi*(times-0.5)**2
assert np.all(np.asarray(actual)<=upper)
fig,ax=plt.subplots(figsize=(9.5,5.3),layout='constrained')
ax.plot(times,actual,color='#186b9e',linewidth=2,label=r'Numerical $\log\|\Phi_i(1/3+it)\|_\infty$')
ax.plot(times,upper,color='#d26924',linewidth=2,linestyle='--',label=r'Proved upper bound $\log(3.33)+3\pi(t-1/2)^2$')
ax.fill_between(times,actual,upper,color='#d26924',alpha=.10)
ax.axvline(.5,color='#767676',linewidth=1,linestyle=':')
ax.set(xlabel=r'Imaginary coordinate $t$',ylabel='Natural logarithm of coordinate norm',
       title='Elliptic coordinates inside their Gaussian envelope',xlim=(-3,3))
ax.grid(alpha=.18)
ax.legend(loc='upper center',fontsize=10,framealpha=.97)
fig.text(.5,-.015,r'Normalized lattice $\mathbb{Z}+i\mathbb{Z}$; samples illustrate Theorem 22.179.',ha='center',fontsize=10)
fig.savefig(root/'elliptic-growth-envelope.png',dpi=170,bbox_inches='tight')
plt.close(fig)
print('Figure22.13: 301 illustrative samples; saved elliptic-growth-envelope.png')

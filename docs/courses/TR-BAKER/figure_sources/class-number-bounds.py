"""The two explicit contradictions used in Lesson 18; original figure, CC0."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.titlesize':11,'legend.fontsize':8})
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.6,3.8),layout='constrained')
s=np.geomspace(1e8,2e12,600)
required=s/11-math.log(3000)
available=11059200*np.maximum(10,np.log(52.5*s))**2
ax.loglog(s,required,color='#aa3c32',label=r'$s/11-\log3000$')
ax.loglog(s,available,color='#245e86',label=r'$11059200\max(10,\log(52.5s))^2$')
ax.axvline(1e12,color='#3d464f',ls=':',lw=1.2)
ax.axvspan(1e12,2e12,color='#aa3c32',alpha=.10)
ax.text(8e11,2.8e8,r'$s=10^{12}$',rotation=90,ha='right',va='bottom')
ax.set(xlim=(1e8,2e12),ylim=(2e6,3e11),xlabel=r'$s=\sqrt{d}$',
       ylabel='Positive quantities in (18.10)',title='The logarithmic theorem bounds the range')
ax.legend(loc='upper left');ax.grid(alpha=.18,which='major')
t=np.linspace(100,700,400)
upper=(math.log(3000)-t/11)/math.log(10)
bx.plot(t,upper,color='#aa3c32',label=r'Upper bound: $\log_{10}(3000e^{-s/11})$')
bx.axhline(-18,color='#245e86',label=r'Certified lower bound: $\log_{10}|\Lambda|>-18$')
bx.axvline(600,color='#3d464f',ls=':',lw=1.2)
bx.axvspan(600,700,color='#aa3c32',alpha=.10)
bx.text(591,-2,r'$s=600$',rotation=90,ha='right',va='top')
bx.set(xlim=(100,700),ylim=(-25,1),xlabel=r'$s=\sqrt{d}$',ylabel=r'Bounds for $\log_{10}|\Lambda|$',
       title='Continued fractions reduce to a finite sieve')
bx.legend(loc='lower left');bx.grid(alpha=.18)
fig.savefig(HERE.parent/'figures/class-number-bounds.png',dpi=180)
plt.close(fig)
print(HERE.parent/'figures/class-number-bounds.png')

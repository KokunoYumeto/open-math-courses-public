"""Contours and the exact Fourier majorants of Lesson 17."""
from pathlib import Path
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
import runpy
record=runpy.run_path(str(HERE.parent/'verification/class-number-fourier-check.py'))['records'][0]
plt.rcParams.update({'font.size':10,'axes.titlesize':11,'axes.labelsize':10,
                     'legend.fontsize':8.5,'font.family':'DejaVu Sans'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.4,3.8),layout='constrained')
ax.axhspan(-1,1,color='#edf4f7')
ax.axhline(0,color='#69737d',lw=1)
ax.axvline(0,color='#69737d',lw=1)
ax.plot([-2.3,2.3,2.3,-2.3,-2.3],[0,0,-.5,-.5,0],color='#1f6487',lw=1.8)
for start,end in [((-.9,0),(.1,0)),((.9,-.5),(-.1,-.5))]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#1f6487','lw':1.8})
ax.scatter([0,0],[-1,1],color='#a33332',s=35,zorder=5)
ax.text(.15,1,'pole $i$',va='center')
ax.text(.15,-1,'pole $-i$',va='center')
ax.text(-2.2,.15,'real line',color='#1f6487')
ax.text(-2.2,-.76,r'shift to $\mathrm{Im}\,z=-1/2$',color='#1f6487')
ax.text(-2.2,1.37,r'$r>0,\quad \lambda=\pi r\sqrt{d}/(ka)$')
ax.text(-2.2,-1.48,r'$|e^{-i\lambda(u-i/2)}|=e^{-\lambda/2}$')
ax.set(xlim=(-2.6,2.6),ylim=(-1.65,1.65),xlabel=r'$\mathrm{Re}\,z$',ylabel=r'$\mathrm{Im}\,z$',
       title='The contour stays between the poles')
ax.set_xticks([-2,0,2]);ax.set_yticks([-1,-.5,0,1])
n=np.arange(1,81)
q=math.exp(-math.pi*math.sqrt(11)/21)
majorant=4*math.pi/math.sqrt(11)*n*q**n
tail=4*math.pi/math.sqrt(11)*q**(n+1)*((n+1)-n*q)/(1-q)**2
actual=np.array([(float(a)+float(b))/2 for a,b in record['nonzero_frequency_pair_absolute_values']])
bx.semilogy(n,majorant,color='#172b4d',label=r'Pair bound: $4\pi r q^r/\sqrt{11}$')
bx.semilogy(n,actual,'.',ms=3,color='#1f8098',label=r'Computed $|2\mathrm{Re}(A_r e^{\pi ir/21})|$')
bx.semilogy(n,tail,'--',color='#b23a34',label='Proved tail bound (17.31)')
bx.set(xlim=(0,82),ylim=(1e-20,2e2),xlabel=r'Frequency $r$ / cutoff $R$',ylabel='Absolute size',
       title=r'$d=11,\ k=21,\ f=(1,1,3)$')
bx.grid(alpha=.2);bx.legend(loc='upper right',framealpha=.95)
bx.text(4,3e-18,r'$R=80:\quad \mathrm{tail}<2.82\cdot10^{-15}$',fontsize=9)
out=HERE.parent/'figures/fourier-decay.png'
fig.savefig(out,dpi=180)
plt.close(fig)
print(out)

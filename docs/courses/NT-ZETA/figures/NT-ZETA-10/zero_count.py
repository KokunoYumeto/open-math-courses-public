"""Original CC0 geometry and numerical sample for the zero-count lesson."""
from pathlib import Path
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mp.mp.dps=45
gamma=[float(mp.im(mp.zetazero(n))) for n in range(1,30)]
Path(__file__).with_suffix('.json').write_text(json.dumps({'precision_digits':45,'numerical_critical_line_ordinates':gamma,'meaning':'Illustrative computed ordinates, not an interval-arithmetic certificate.'},indent=2)+'\n',encoding='utf-8')
green='#286766';orange='#ac5c38'
plt.rcParams.update({'font.size':10.5,'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.5),layout='constrained')
T=35
ax.plot([2,2,.5],[0,T,T],color=green,lw=2.4,label='Lₜ')
ax.plot([.5,-1,-1],[T,T,0],color=orange,lw=2.4,label='Reflected path')
ax.plot([-1,2],[0,0],color='#60716d',lw=1.4)
for start,end,color in [((2,12),(2,22),green),((1.8,T),(.8,T),green),((.3,T),(-.8,T),orange),((-1,24),(-1,13),orange),((-.7,0),(1.2,0),'#60716d')]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':1.8})
ax.axvline(.5,color='#8b9d96',ls=':',lw=1)
samples=[g for g in gamma if g<T]
ax.scatter([.5]*len(samples),samples,s=18,color='#293b3b',zorder=4)
ax.text(.65,18,'Numerical\nzero samples',fontsize=9,color='#293b3b')
ax.text(.46,T+1.5,'½ + iT',ha='center',fontsize=9)
ax.text(.5,2.4,'ξ is positive on the real base',ha='center',fontsize=8.8,color='#60716d')
ax.set(xlim=(-1.4,2.4),ylim=(-2,40),xticks=[-1,.5,2],xticklabels=['−1','½','2'],yticks=[0,10,20,35],yticklabels=['0','10','20','T = 35'],xlabel='Real part σ',ylabel='Imaginary part t',title='The argument-principle rectangle')
ax.text(1.86,28,'Lₜ',ha='right',color=green,fontsize=11)
ax.text(-.86,28,'Reflected\npath',color=orange,fontsize=9)
heights=np.linspace(1,100,400)
phase=[float(1+(mp.im(mp.loggamma(mp.mpf(1)/4+mp.j*t/2))-t/2*mp.log(mp.pi))/mp.pi) for t in heights]
bx.step([0]+gamma+[100],[0]+list(range(1,30))+[29],where='post',color=green,lw=1.7,label='Numerical count N(T)')
bx.plot(heights,phase,color=orange,lw=1.4,label='Smooth phase count 1 + ϑ(T)/π')
bx.set(xlim=(0,100),ylim=(-.5,31),xlabel='Height T',ylabel='Zero count',title='The smooth count and its staircase')
bx.grid(alpha=.18)
bx.legend(loc='upper left',fontsize=8.5)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)
plt.close(fig)

"""Original CC0 figure: the three-height weight and exact proved widths."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.4,4.4),layout='constrained')
theta=np.linspace(-2*np.pi,2*np.pi,2001)
ax.plot(theta,2*(1+np.cos(theta))**2,color='#286766',lw=2)
ax.scatter([-np.pi,np.pi],[0,0],color='#ac5c38',zorder=3)
ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['−2π','−π','0','π','2π'])
ax.set(xlabel='Phase angle θ',ylabel='3 + 4 cos θ + cos 2θ',ylim=(-.3,8.5),title='A nonnegative weight at every phase')
ax.grid(alpha=.18)
t=np.geomspace(2,100,500);ell=np.log(t+2);wide=5/ell;normal=1/ell;half=.5/ell
bx.fill_betweenx(t,0,wide,color='#dfebe7',label='Proved zero-free region, C = 1/2000')
bx.fill_betweenx(t,0,half,color='#286766',alpha=.45,label='All three bounds, half of c = 1/10000')
bx.plot(wide,t,color='#55716a',lw=2)
bx.plot(normal,t,color='#ac5c38',ls='--',lw=1.7,label='Zero-free boundary with c = 1/10000')
bx.plot(half,t,color='#286766',lw=1.6)
bx.set_yscale('log');bx.set_yticks([2,5,10,20,50,100],['2','5','10','20','50','100'])
bx.set(xlim=(0,4),ylim=(2,100),xlabel='u = 10⁴ (1 − σ)',ylabel='Height |t|',title='Widths from Theorems 3.2 and 4.1')
bx.grid(alpha=.16)
bx.text(.82,35,'Zeros\nexcluded',ha='center',va='center',fontsize=9,color='#375a51')
bx.legend(loc='lower right',fontsize=7.2,framealpha=.94)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)
plt.close(fig)

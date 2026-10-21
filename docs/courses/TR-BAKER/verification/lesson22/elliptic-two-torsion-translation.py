"""Figure22.16: the exact local branch of translation by(0,0)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base=Path(__file__).resolve().parent
t=np.linspace(-.35,.35,501)
s=2*t**3/(1+np.sqrt(1+4*t**4))
x=-t*t/(1+t*s)
y=-t/(1+t*s)
fig,axs=plt.subplots(1,3,figsize=(13.8,4.5),constrained_layout=True)
axs[0].plot(x,y,color='#1c6c9b',lw=2)
axs[0].scatter([0],[0],color='#a53c28',zorder=5)
axs[0].annotate(r'$q=(0,0)$',xy=(0,0),xytext=(-.105,.09),arrowprops={'arrowstyle':'-','color':'#666'})
axs[0].annotate('',xy=(0,-.17),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#a53c28'})
axs[0].text(-.112,-.18,r'Increasing $t$:'+'\n'+r'tangent $(0,-1)$',fontsize=10,color='#a53c28')
axs[0].set(xlabel=r'$x_q(t)$',ylabel=r'$y_q(t)$',title=r'Translated branch on $y^2=x^3-x$',xlim=(-.13,.025),ylim=(-.39,.39))
for ax,values,approx,label in [(axs[1],x,-t*t,'x'),(axs[2],y,-t,'y')]:
    ax.plot(t,values,label='Exact branch, sampled',color='#1c6c9b',lw=2.4)
    ax.plot(t,approx,'--',label=r'$-t^2$' if label=='x' else r'$-t$',color='#b65b24',lw=1.5)
    ax.set(xlabel=r'Identity parameter $t$',ylabel=rf'${label}_q(t)$',title='Quadratic first term' if label=='x' else 'Nonzero first derivative')
    ax.legend(loc='best',fontsize=9)
for ax in axs:
    ax.grid(alpha=.2)
    ax.axhline(0,color='#aaa',lw=.7)
fig.suptitle(r'Translation by a point of order two: formula (22.597)',fontsize=15)
fig.savefig(base/'elliptic-two-torsion-translation.png',dpi=160)
plt.close(fig)
print('Saved Figure22.16')

"""Exact examples from AN01-U082, Exercises 2 and 5. CC0; GPT-6 Astra, Ultra."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'svg.fonttype':'none'})
blue='#236da2';orange='#bf5811';grey='#a8b5c7'
fig,axes=plt.subplots(1,3,figsize=(15,4.8),layout='constrained')
fig.suptitle('A spectral limit direction and an exact Fourier rotation',fontsize=18)

ax=axes[0];j=np.arange(1,10)
ax.scatter(j,np.sqrt(j),color=blue,s=45,zorder=3)
for k in [1,4,9]:
 ax.annotate(r'$('+str(k)+r',\sqrt{'+str(k)+r'})$',(k,np.sqrt(k)),xytext=(0,10),textcoords='offset points',ha='center',fontsize=10)
ax.annotate('',xy=(9.3,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':orange,'lw':2})
ax.text(4.7,-.65,r'Limiting ray: $r e_1$, $r>0$',ha='center',color=orange)
ax.set(xlim=(-.3,10.3),ylim=(-1.1,4.5),xlabel=r'First frequency $\xi_1$',ylabel=r'Second frequency $\xi_2$',title=r'Samples of $(j,\sqrt{j})$, $j\geq1$')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18)

for ax in axes[1:]:
 ax.set(xlim=(-2.2,2.2),ylim=(-2.1,2.2))
 ax.set_aspect('equal',adjustable='box')
 ax.axhline(0,color=grey,lw=.8,zorder=0);ax.axvline(0,color=grey,lw=.8,zorder=0)
 ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])

ax=axes[1];ax.axhline(0,color=blue,lw=3)
ax.scatter([1],[0],color=orange,s=55,zorder=4)
ax.annotate('',xy=(1,1),xytext=(1,0),arrowprops={'arrowstyle':'->','color':orange,'lw':2.5})
ax.text(.05,1.32,r'$\xi=(0,1)$',color=orange)
ax.text(.15,-.45,r'$x=(1,0)$',color=orange)
ax.text(-2.0,-1.55,r'Support: $x_2=0$',color=blue)
ax.set(xlabel=r'$x_1$',ylabel=r'$x_2$',title=r'Physical side: $u=\delta(x_2)$')

ax=axes[2];ax.axvline(0,color=blue,lw=3)
ax.scatter([0],[1],color=orange,s=55,zorder=4)
ax.annotate('',xy=(-1,1),xytext=(0,1),arrowprops={'arrowstyle':'->','color':orange,'lw':2.5})
ax.text(-1.95,1.45,r'$-x=(-1,0)$',color=orange)
ax.text(.15,.55,r'$\xi=(0,1)$',color=orange)
ax.text(-2.0,-1.55,r'Support: $\xi_1=0$',color=blue)
ax.set(xlabel=r'$\xi_1$',ylabel=r'$\xi_2$',title=r'Fourier side: $\widehat u=2\pi\delta(\xi_1)$')

for ext in ['png','svg']:
 fig.savefig(HERE/f'fourier-support-and-rotation.{ext}',dpi=180)
svg=HERE/'fourier-support-and-rotation.svg'
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
plt.close(fig)

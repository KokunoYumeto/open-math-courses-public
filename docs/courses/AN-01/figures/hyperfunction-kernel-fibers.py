"""Exact outer covectors and proper sum fibers, AN01-U104 Exercises4,6; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U104-kernel-fibers','text.usetex':False})
D=Path(__file__).resolve().parent
blue='#17659b';orange='#bd6508';green='#147652';dark='#24354a'
fig,axs=plt.subplots(1,2,figsize=(12,6.7))
ax=axs[0]
ax.axhline(0,color='#c2cbd4',lw=.8);ax.axvline(0,color='#c2cbd4',lw=.8)
for theta in np.linspace(0,2*np.pi,16,endpoint=False):
 v=np.array([np.cos(theta),np.sin(theta)])
 ax.annotate('',xy=1.6*v,xytext=.14*v,arrowprops=dict(arrowstyle='->',color=blue,lw=1.8))
ax.scatter([0],[0],s=42,facecolors='white',edgecolors=dark,zorder=5)
ax.text(0,1.98,r'$\eta=0$ for every matched middle covector',ha='center',fontsize=12,color=orange)
ax.text(0,-2.05,'Every nonzero outer direction occurs\nArrows sample the full punctured plane',ha='center',fontsize=11)
ax.set(xlim=(-2.3,2.3),ylim=(-2.4,2.3),xlabel=r'outer $\xi$',ylabel=r'outer $\zeta$')
ax.set_aspect('equal',adjustable='box')
ax.set_title('Point-kernel contraction\n'+r'$C=\delta_0(x)\otimes\delta_0(z)$')
ax=axs[1]
ax.add_patch(Polygon([[0,0],[1,0],[0,1]],closed=True,facecolor='#d7e9f4',edgecolor=blue,lw=2))
ax.plot([0,1],[1,0],color=orange,lw=3,label=r'fiber $s+t=1$')
ax.scatter([0,1,0],[0,0,1],s=25,color=blue)
ax.text(.18,.24,r'$s,t\geq0$'+'\n'+r'$0\leq s+t\leq1$',fontsize=14,color=dark)
ax.text(.61,.65,r'$t=1-s$',color=orange)
ax.annotate('',xy=(1,-.13),xytext=(0,-.13),arrowprops=dict(arrowstyle='<->',color=green,lw=1.8))
ax.text(.5,-.22,r'fiber coordinate: $0\leq s\leq1$',ha='center',color=green,fontsize=11)
ax.set(xlim=(-.15,1.25),ylim=(-.32,1.25),xlabel=r'$s$',ylabel=r'$t$')
ax.set_aspect('equal',adjustable='box')
ax.set_title('A compact inverse image for addition\n'+r'$H*H=xH(x)$')
ax.legend(loc='upper right',fontsize=10)
fig.suptitle('Zero middle covectors and proper support are both visible',fontsize=17,y=.98)
fig.text(.5,.035,'Left: Exercise 4 retains every endpoint-zero case. Right: Exercise 6 integrates in s, not slanted arclength.\nThe exact relation and support arguments appear alongside the calculations.',ha='center',fontsize=11)
fig.subplots_adjust(top=.79,bottom=.2,wspace=.32)
fig.savefig(D/'hyperfunction-kernel-fibers.svg',metadata={'Date':None})
fig.savefig(D/'hyperfunction-kernel-fibers.png',dpi=170)
plt.close(fig)
svg=D/'hyperfunction-kernel-fibers.svg'
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())

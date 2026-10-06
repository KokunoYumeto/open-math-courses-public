"""Exact slit-annulus geometry, with schematic bank separation; CC0 1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.4,6.5),layout='constrained')
blue='#22718a';gold='#a86119';red='#9d3939'
phi=np.linspace(0,2*np.pi,900)
ax.plot(2.5*np.cos(phi),2.5*np.sin(phi),c=blue,lw=2)
ax.plot(.2*np.cos(phi),.2*np.sin(phi),c=gold,lw=2)
ax.plot([.2,2.5],[0,0],c='#999999',lw=1,ls=':')
ax.annotate('',xy=(2.3,.055),xytext=(.5,.055),arrowprops={'arrowstyle':'->','color':gold,'lw':2})
ax.annotate('',xy=(.5,-.055),xytext=(2.3,-.055),arrowprops={'arrowstyle':'->','color':gold,'lw':2})
ax.text(.7,.28,'Upper bank\n'+r'$\arg(-z)=-\pi$',fontsize=16)
ax.text(.7,-.67,'Lower bank\n'+r'$\arg(-z)=+\pi$',fontsize=16)
def circle_arrow(radius,start,end,color):
    ax.annotate('',xy=(radius*np.cos(end),radius*np.sin(end)),xytext=(radius*np.cos(start),radius*np.sin(start)),arrowprops={'arrowstyle':'->','color':color,'lw':2.3,'connectionstyle':'arc3,rad=.12'})
circle_arrow(2.5,.8,1.05,blue)
circle_arrow(.2,2.8,1.7,gold)
ax.text(1.05,1.82,r'$R_2=5\pi$',c=blue,fontsize=18)
ax.annotate(r'$\varepsilon=2\pi/5$',xy=(-.18,.07),xytext=(-2.35,.45),fontsize=16,color=gold,arrowprops={'arrowstyle':'->','color':gold})
for k in [-2,-1,1,2]:
    ax.scatter([0],[k],c=red,s=50,zorder=4)
    label={-2:r'$-4\pi i$',-1:r'$-2\pi i$',1:r'$2\pi i$',2:r'$4\pi i$'}[k]
    ax.text(.12,k+.05,label,c=red,fontsize=17)
ax.scatter([0],[0],facecolors='white',edgecolors='#555555',s=25,zorder=4)
ax.text(-.35,-.38,'0',fontsize=16)
ax.axhline(0,c='#999999',lw=.6,zorder=0);ax.axvline(0,c='#999999',lw=.6,zorder=0)
ax.set(xlim=(-2.75,2.85),ylim=(-2.75,2.75),xlabel=r'$\Re z/(2\pi)$',ylabel=r'$\Im z/(2\pi)$')
ax.set_aspect('equal');ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2]);ax.tick_params(labelsize=17)
ax.xaxis.label.set_size(18);ax.yaxis.label.set_size(18)
ax.set_title('The Hankel residue contour',fontsize=20)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180,metadata={'Software':None})

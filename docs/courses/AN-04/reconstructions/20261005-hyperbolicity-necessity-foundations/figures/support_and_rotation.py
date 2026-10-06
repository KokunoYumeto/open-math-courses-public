"""Exact illustrative examples for C2/C3 and F1/F2; CC0, 5 October 2026."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,'svg.fonttype':'none'})
fig,axs=plt.subplots(2,1,figsize=(7.5,11.6),layout='constrained')
ax=axs[0]
ax.add_patch(Rectangle((-1,-.4),2,.8,fc='#d4e8f2',ec='#266984',lw=2))
ax.text(0,0,r'$K=[-1,1]\times[-0.4,0.4]$',ha='center',va='center',fontsize=14)
q=np.array([13/8,1.0]);side=1/8;center=q+side/2
ax.add_patch(Rectangle((1.5,1),.25,.25,fc='none',ec='#969ca4',ls='--',lw=1.5))
expanded=side*9/8
ax.add_patch(Rectangle(center-expanded/2,expanded,expanded,fc='#fee1b7',ec='#c07c20',lw=1.5))
ax.add_patch(Rectangle(q,side,side,fc='none',ec='#a74024',lw=2))
anchor=np.array([1,.4])
ax.plot(*anchor,'o',color='#266984');ax.plot(*center,'o',color='#a74024',ms=4)
ax.plot([anchor[0],center[0]],[anchor[1],center[1]],color='#555',lw=1.2)
ax.annotate(r'$a_Q=(1,0.4)$',anchor,xytext=(.35,.69),arrowprops={'arrowstyle':'-'},fontsize=14)
ax.annotate(r'$Q,\ Q^*=(9/8)Q$',center,xytext=(-.45,1.23),arrowprops={'arrowstyle':'->'},fontsize=14)
ax.text(-1.15,-.84,'Solid cube: admissible.\nDashed parent: fails the distance test.',va='center',fontsize=14)
ax.set(xlim=(-1.2,2),ylim=(-1.05,1.55),xlabel=r'$x_1$',ylabel=r'$x_2$',
       title='Convex jets: one maximal cube')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
ax=axs[1]
ax.add_patch(Circle((0,0),.6,fc='#d8ece3',ec='#4b9271',lw=1.6))
ax.add_patch(Circle((0,0),.4,fc='white',ec='#4b9271',lw=1.6))
theta=np.linspace(0,2*np.pi,500)
ax.plot(.5*np.cos(theta),.5*np.sin(theta),color='#236748',ls='--',lw=1.2)
ax.scatter([-1,1],[0,0],marker='x',s=90,lw=2.5,c='#aa3c29',zorder=4)
ax.annotate('root −1',(-1,0),xytext=(-1.22,-.36),fontsize=14)
ax.annotate('root +1',(1,0),xytext=(.73,-.36),fontsize=14)
ax.annotate(r'$0.4\leq |z|\leq0.6$',(.43,.38),xytext=(-1.15,1.0),
            arrowprops={'arrowstyle':'->'},fontsize=14)
ax.text(0,-.92,r'$Q(z)=z^2-1:\quad |Q(z)|\geq 0.64$',ha='center',fontsize=14)
ax.axhline(0,color='#ddd',lw=.8,zorder=0);ax.axvline(0,color='#ddd',lw=.8,zorder=0)
ax.set(xlim=(-1.35,1.35),ylim=(-1.1,1.4),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',
       title='Rotation: a compact set avoiding zeros')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
for suffix in ['png','svg']:fig.savefig(HERE/f'support_and_rotation.{suffix}',dpi=170)
plt.close(fig)

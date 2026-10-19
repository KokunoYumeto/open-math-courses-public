"""Exact directional and approach sectors, AN01-U109 Lemma1/Exercise2; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','svg.hashsalt':'AN01-U109'})
theta=np.degrees(np.arctan(2));beta=np.degrees(np.arctan(.75))
fig,axes=plt.subplots(1,2,figsize=(12.4,6.1),layout='constrained')
def sector(ax,l,r,radius,color,label,alpha=.15,style='-'):
    ax.add_patch(Wedge((0,0),radius,l,r,facecolor=color,edgecolor=color,alpha=alpha,lw=1.3))
    for ang in [l,r]:
        t=np.radians(ang);ax.plot([0,radius*np.cos(t)],[0,radius*np.sin(t)],color=color,lw=1.6,ls=style)
    ax.plot([],[],color=color,lw=4,alpha=.8,label=label)
sector(axes[0],-45,75,1.04,'#c87a1c',r'$C_1:\ [-45^\circ,75^\circ]$')
sector(axes[0],theta,180-theta,1.12,'#245a9c',r'$C_0:\ [\arctan2,180^\circ-\arctan2]$')
sector(axes[0],theta,75,.92,'#7c3f9b',r'$E_1=C_0\cap C_1$ ',.6)
axes[0].annotate('',xy=(0,1),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#172334','lw':2})
axes[0].annotate(r'$\xi_0=e_2$',xy=(0,1),xytext=(-.4,1.15))
axes[0].set(title='Covectors: split the singular directions',xlabel=r'$\xi_1$',ylabel=r'$\xi_2$')
sector(axes[1],-15,theta+90,1.18,'#929ead',r'$\operatorname{int}E_1^*:\ (-15^\circ,\arctan2+90^\circ)$',.10,'--')
sector(axes[1],-12,180-beta,1.02,'#7c3f9b',r'$H_1=G_0+G_1$',.12,'--')
sector(axes[1],beta,180-beta,.84,'#245a9c',r'$G_0:\ (\arctan(3/4),180^\circ-\arctan(3/4))$',.20,'--')
sector(axes[1],-12,-8,1.02,'#c87a1c',r'$G_1:\ (-12^\circ,-8^\circ)$',.65,'--')
t=np.radians(-10)
axes[1].annotate('',xy=(np.cos(t),np.sin(t)),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#172334','lw':1.8})
axes[1].annotate(r'$e_2\cdot y=\sin(-10^\circ)<0$',xy=(np.cos(t),np.sin(t)),xytext=(-.60,-.56),arrowprops={'arrowstyle':'-','color':'#172334'},fontsize=11)
axes[1].set(title='Imaginary directions: solve on the larger cone',xlabel=r'$y_1$',ylabel=r'$y_2$')
for ax in axes:
    ax.axhline(0,color='#64748b',lw=.7);ax.axvline(0,color='#64748b',lw=.7)
    ax.set_aspect('equal');ax.set(xlim=(-1.34,1.34),ylim=(-.85,1.3))
    ax.legend(loc='upper center',bbox_to_anchor=(.5,-.14),fontsize=9.5,frameon=False)
    ax.spines[['right','top']].set_visible(False)
fig.suptitle(r'One exchange for $p_2(\zeta)=\zeta_1^2+\zeta_2^2$, $a=3/4$, $b=1/2$',fontsize=16)
fig.savefig(out/'hyperfunction-equation-cones.png',dpi=160,bbox_inches='tight')
fig.savefig(out/'hyperfunction-equation-cones.svg',metadata={'Date':None},bbox_inches='tight')
p=out/'hyperfunction-equation-cones.svg'
p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')

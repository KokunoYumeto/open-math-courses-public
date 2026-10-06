"""Original CC0 diagram of the exact two contours in Theorem 5.1."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

R=3
delta=.45
green='#286766'
orange='#ac5c38'
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(10.4,4.5),layout='constrained')
theta_right=np.linspace(-np.pi/2,np.pi/2,501)
theta_left=np.linspace(np.pi/2,3*np.pi/2,501)

def arc(ax,angles,color,label):
    x=R*np.cos(angles);y=R*np.sin(angles)
    ax.plot(x,y,color=color,lw=2.3,label=label)
    for frac in [.24,.72]:
        j=int(frac*(len(angles)-1))
        ax.annotate('',xy=(x[j+10],y[j+10]),xytext=(x[j-10],y[j-10]),
                    arrowprops={'arrowstyle':'->','color':color,'lw':2})

for ax in axes:
    ax.axhline(0,color='#9caaa9',lw=.8)
    ax.axvline(0,color='#9caaa9',lw=.8)
    ax.scatter([0],[0],color='#293b3b',s=18,zorder=4)
    ax.text(.13,.14,'0',fontsize=10)
    ax.scatter([0,0],[-R,R],color='#293b3b',s=18,zorder=4)
    ax.text(.16,R+.08,'iR',fontsize=10)
    ax.text(.16,-R-.23,'−iR',fontsize=10)
    ax.set(xlim=(-3.55,3.7),ylim=(-3.55,3.65),xlabel='Re z',ylabel='Im z')
    ax.set_aspect('equal')
    ax.set_xticks([-3,0,3]);ax.set_yticks([-3,0,3])
    arc(ax,theta_right,green,'C₊')

ax,bx=axes
arc(ax,theta_left,orange,'C₋')
ax.text(-1.7,.4,'Gₜ is entire',ha='center',color=orange)
ax.text(1.35,.4,'right arc',ha='center',color=green)
ax.set_title('The full circle for Gₜ')
ax.legend(loc='lower left',fontsize=9,framealpha=.95)

bx.add_patch(Rectangle((-delta,-R),delta,2*R,facecolor='#dfebe7',edgecolor='none',zorder=0))
bx.fill_betweenx(R*np.sin(theta_right),0,R*np.cos(theta_right),color='#dfebe7',zorder=0)
path=np.array([[0,R],[-delta,R],[-delta,-R],[0,-R]])
bx.plot(path[:,0],path[:,1],color=orange,lw=2.3,label='Γ₋')
bx.annotate('',xy=(-delta,-.65),xytext=(-delta,.65),arrowprops={'arrowstyle':'->','color':orange,'lw':2})
bx.annotate('',xy=(-delta,R),xytext=(0,R),arrowprops={'arrowstyle':'->','color':orange,'lw':1.4})
bx.annotate('',xy=(0,-R),xytext=(-delta,-R),arrowprops={'arrowstyle':'->','color':orange,'lw':1.4})
bx.text(-1.85,.5,'chosen narrow\nleft path',ha='center',color=orange)
bx.text(1.35,.4,'G is analytic\nhere',ha='center',color=green)
bx.text(-delta-.1,-R-.4,'−δ',ha='right',fontsize=9)
bx.set_title('The permitted contour for G')
bx.legend(loc='lower left',fontsize=9,framealpha=.95)
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)
plt.close(fig)

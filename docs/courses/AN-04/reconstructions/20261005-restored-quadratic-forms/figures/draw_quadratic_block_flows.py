"""Original exact real half-Hamiltonian orbits; last panel is a labelled projection."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

here=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'stix','svg.fonttype':'path','font.size':14})
fig, axes=plt.subplots(3,1,figsize=(6.5,14.))
fig.subplots_adjust(left=.16,right=.96,top=.94,bottom=.16,hspace=.72)
blue='#176a83';brown='#a75517'
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.axhline(0,color='#bbbbbb',linewidth=.8,zorder=0)
    ax.axvline(0,color='#bbbbbb',linewidth=.8,zorder=0)
def arrow(ax, start, end, color):
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','color':color,'lw':1.7,'mutation_scale':13})

ax=axes[0]
t=np.linspace(0,2*np.pi,1001)
for r,color in [(1.,blue),(.55,brown)]:
    ax.plot(r*np.cos(t),-r*np.sin(t),color=color,lw=2.1)
    for a in [.35,2.6,4.8]:arrow(ax,(r*np.cos(a),-r*np.sin(a)),(r*np.cos(a+.22),-r*np.sin(a+.22)),color)
ax.set_aspect('equal',adjustable='box')
ax.set(xlim=(-1.25,1.25),ylim=(-1.15,1.15),xlabel=r'$x$',ylabel=r'$\xi$')
ax.set_title(r'$Q=x^2+\xi^2$'+'\n'+r'$e^{tF}(r,0)=(r\cos t,-r\sin t)$',pad=13)
ax.text(.5,-.38,r'Clockwise rotation; $F=H_Q/2$',transform=ax.transAxes,ha='center')

ax=axes[1]
t=np.linspace(-.9,.9,1001)
for sx,sp in [(1,1),(-1,-1),(1,-1),(-1,1)]:
    color=blue if sx*sp>0 else brown
    ax.plot(sx*.65*np.exp(t),sp*.65*np.exp(-t),color=color,lw=2.1)
    for a in [-.4,.25]:
        arrow(ax,(sx*.65*np.exp(a),sp*.65*np.exp(-a)),(sx*.65*np.exp(a+.16),sp*.65*np.exp(-a-.16)),color)
ax.set_aspect('equal',adjustable='box')
ax.set(xlim=(-1.85,1.85),ylim=(-1.75,1.75),xlabel=r'$x$',ylabel=r'$\xi$')
ax.set_title(r'$Q=2x\xi$'+'\n'+r'$e^{tF}(x_0,\xi_0)=(e^t x_0,e^{-t}\xi_0)$',pad=13)
ax.text(.5,-.38,r'Four branches: $x_0,\xi_0=\pm0.65$',transform=ax.transAxes,ha='center')

ax=axes[2]
t=np.linspace(-2,2,1001)
ax.plot(-t,t*t/2,color=blue,lw=2.2)
for a in [-1.5,-.5,.7,1.5]:arrow(ax,(-a,a*a/2),(-a-.15,(a+.15)**2/2),blue)
ax.scatter([0],[0],color=blue,s=22,zorder=3)
ax.set(xlim=(-2.2,2.2),ylim=(-.08,2.3),xlabel=r'$x_2$',ylabel=r'$\xi_2$')
ax.set_title(r'$Q=x_2^2-2\xi_1\xi_2$'+'\n'+r'Specified $(x_2,\xi_2)$ projection',pad=13)
ax.text(.5,-.36,r'Full orbit: $(-t^3/6,-t,1,t^2/2)$',transform=ax.transAxes,ha='center')
ax.text(.5,-.51,r'$-2\leq t\leq2$, initial vector $\varepsilon_1$',transform=ax.transAxes,ha='center')
ax.text(.5,-.66,'Time increases along arrows',transform=ax.transAxes,ha='center')

out=here/'quadratic-block-flows.svg'
fig.savefig(out,metadata={'Creator':'Original AN-04 mathematical drawing','Date':None})
png=here/'quadratic-block-flows.png'
fig.savefig(png,dpi=145)
plt.close(fig)
print('Saved original quadratic block flow SVG and inspection PNG.')

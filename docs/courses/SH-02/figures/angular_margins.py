"""CC0 original exact examples for EA3 and EA11; no source figure reused.

Run this file to produce its PNG and SVG. Coordinates and constants are fixed.
The plotted front is an exact example of the defining inequalities, sampled for
display; the mathematical proof is EA1--EA11, not the finite numerical plot.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

root = Path(__file__).resolve().parent
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 16,
                     'mathtext.fontset': 'dejavusans'})
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'SH02-angular_margins-v1'})
fig, axes = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=True)

ax = axes[0]
eta = 1/4
y = np.linspace(0, 3.2, 300)
ax.fill_betweenx(y, -eta*y, eta*y, color='#92c5de', alpha=.55)
ax.plot(eta*y, y, color='#2166ac', lw=2)
ax.plot(-eta*y, y, color='#2166ac', lw=2)
ax.plot([0,0],[0,3.1], color='#1b7837', lw=3)
ax.annotate('', xy=(-1.25,0), xytext=(0,0),
            arrowprops={'arrowstyle':'->','color':'#b2182b','lw':3})
ax.text(-1.25,.12,r'$D=\{(-s,0):s\geq0\}$',color='#b2182b')
ax.plot([-.25,.25],[1,1], color='#762a83',lw=4)
ax.scatter([0,0],[1,2],color='#1b7837',s=45,zorder=4)
ax.text(.32,1.03,r'$B_\eta=B+[-\frac{1}{4},\frac{1}{4}]\times\{0\}$',fontsize=12)
ax.text(-.75,.78,r'$B=\{(0,1)\},\quad\delta=1$',fontsize=12)
ax.add_patch(Circle((0,2),2/9,edgecolor='#e08214',facecolor='#fdb863',alpha=.65))
ax.text(.43,2.05,r'$v=(0,2)$'+'\n'+r'$B_{2/9}(v)\subset\operatorname{Int}K$',fontsize=13)
ax.text(-1.28,3.22,r'$K=\{(x,y):y\geq0,\ |x|\leq y/4\}$',fontsize=14)
ax.text(-1.28,-.42,r'$\ell(x,y)=y,\quad\lambda=1,\quad\eta=1/4,\quad c=1/9$',fontsize=13)
ax.set_title('EA3: an exact angular thickening')
ax.set_xlim(-1.45,1.65); ax.set_ylim(-.6,3.65)
ax.set_aspect('equal'); ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.axhline(0,color='.7',lw=.8); ax.grid(alpha=.15)

ax=axes[1]
xx=np.linspace(-1.8,2.4,900)
yy=np.linspace(-2.75,2.75,1000)
X,Y=np.meshgrid(xx,yy)
d=np.sqrt(np.minimum(X,0)**2+Y**2)
ell=-X
lhs=np.maximum(d-1,0)*ell
rhs=(2-d)**2
inside=(ell<0)|((d<2)&(lhs<rhs))
ax.contourf(X,Y,inside.astype(float),levels=[.5,1.5],colors=['#d1e5f0'],alpha=.75)
ax.contour(X,Y,inside.astype(float),levels=[.5],colors=['#2166ac'],linewidths=2)
ax.contour(X,Y,d,levels=[1],colors=['#969696'],linestyles=['--'],linewidths=1.3)
ax.annotate('',xy=(2.25,0),xytext=(0,0),
            arrowprops={'arrowstyle':'->','color':'#1b7837','lw':3})
ax.text(.65,.13,r'$C=\{(s,0):s\geq0\}$',color='#1b7837',fontsize=12)
z=np.array([-.5,np.sqrt(2)])
dd=z/1.5
xi=np.array([-1.,0.])
dg=xi+3*dd
ax.scatter(*z,color='#b2182b',s=48,zorder=5)
ax.plot([0,z[0]],[0,z[1]],ls=':',color='#762a83',lw=1.5)
ax.annotate('',xy=z+.45*dd,xytext=z,
            arrowprops={'arrowstyle':'->','color':'#762a83','lw':2})
ax.annotate('',xy=z+.3*dg,xytext=z,
            arrowprops={'arrowstyle':'->','color':'#b2182b','lw':2.5})
ax.text(.12,1.48,r'$z=(-1/2,\sqrt{2})$'+'\n'+r'$d(z)=3/2,\quad b_1(d)=1/2$',fontsize=12)
ax.text(-1.66,2.45,r'$dg_z=(-2,2\sqrt{2})$',color='#b2182b',fontsize=12)
ax.text(-1.68,-2.40,r'$dg=\xi+\lambda\,dd,\quad\xi=(-1,0),\quad\lambda\geq0$'+'\n'+
        r'$dg(1,0)\leq-1$',fontsize=13)
ax.text(.32,-1.5,r'$N_1=\{\ell<0\}$'+'\n'+r'$\cup\{d<2,$'+'\n'+r'$\quad(d-1)_+\ell<(2-d)^2\}$',fontsize=10)
ax.set_title('EA11: the retained strict polar term')
ax.set_xlim(-1.8,2.4); ax.set_ylim(-2.75,2.75)
ax.set_aspect('equal'); ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.axvline(0,color='.7',lw=.8); ax.axhline(0,color='.7',lw=.8); ax.grid(alpha=.15)

fig.suptitle('Exact Euclidean examples: quantitative cone room and a C¹ rounded front',fontsize=18)
fig.savefig(root/'angular_margins.png',dpi=180)
fig.savefig(root/'angular_margins.svg',metadata={'Date':None})
plt.close(fig)

"""Original CC0 Figure 6.8c, equations DD.1–DD.11.

Run with Python 3, NumPy and Matplotlib. Figures are written beside this
reproduction directory; DejaVu Sans is bundled by Matplotlib. The analytic
curves are proved bounds, not sampled operator norms.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent.parent/'figures'
HERE.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.titlesize':16,
    'axes.labelsize':14,'svg.hashsalt':'plaque-dirichlet-input-DD-20261005'})
fig=plt.figure(figsize=(20,14),facecolor='white')
grid=fig.add_gridspec(2,2,left=.055,right=.97,bottom=.20,top=.875,hspace=.45,wspace=.26)
ax=fig.add_subplot(grid[0,0]); profiles=fig.add_subplot(grid[1,0])
norms=fig.add_subplot(grid[0,1]); constants=fig.add_subplot(grid[1,1])
green='#18765c';red='#b53b39';blue='#285fa2';gray='#656d78'
epsilon=1/16
radius=2/np.pi
def circle(t):return radius*np.cos(np.pi*t/2),radius*np.sin(np.pi*t/2)
t=np.linspace(0,4,800);ax.plot(*circle(t),color='#a7adb6',lw=5)
t=np.linspace(0,1,300);ax.plot(*circle(t),color=green,lw=7,label=r'fixed open chart $\Omega=(0,1)$')
t=np.linspace(5/12,7/12,120);ax.plot(*circle(t),color=blue,lw=12,label=r'output support $[5/12,7/12]$')
t=np.linspace(5*epsilon/4,7*epsilon/4,60);ax.plot(*circle(t),color=red,lw=13,label=r'input support $[5\varepsilon/4,7\varepsilon/4]$')
for value,label,offset in [(0,'t = 0',(.04,-.11)),(1,'t = 1',(-.12,.07))]:
    x,y=circle(value);ax.scatter([x],[y],s=85,facecolor='white',edgecolor=green,lw=2,zorder=8)
    ax.text(x+offset[0],y+offset[1],label,fontsize=13)
ax.text(-.48,.08,r'$M=\mathbb{R}/4\mathbb{Z}$',fontsize=20)
ax.text(-.47,-.10,r'$ds^2=dt^2$',fontsize=17)
ax.text(-.47,-.28,'global input u = 1\nallowed on the whole leaf',fontsize=14)
ax.annotate('fixed output g\nt in [5/12,7/12]',xy=circle(.5),xytext=(-.79,.78),fontsize=13,
    arrowprops={'arrowstyle':'->','color':blue},color=blue)
ax.annotate('h approaches the zero-trace endpoint\nt in [5 epsilon/4,7 epsilon/4]',xy=circle(1.5*epsilon),xytext=(-.02,-.65),fontsize=11,
    arrowprops={'arrowstyle':'->','color':red},color=red)
ax.set_aspect('equal');ax.set_xlim(-.91,.91);ax.set_ylim(-.84,.96);ax.axis('off')
ax.set_title('A. One fixed chart on the length-four circle',loc='left',pad=12)

x=np.linspace(0,1,3000)
def relative_bump(r):
    result=np.zeros_like(r);mask=(r>.25)&(r<.75)
    result[mask]=np.exp(16-1/((r[mask]-.25)*(.75-r[mask])))
    return result
profiles.plot(x,relative_bump((x-epsilon)/epsilon),color=red,lw=2.8,label=r'$h_\varepsilon/\|h_\varepsilon\|_\infty$')
profiles.plot(x,relative_bump(3*x-1),color=blue,lw=2.8,label=r'$g/\|g\|_\infty$')
profiles.plot(x,np.ones_like(x),color=gray,lw=1.5,ls='--',label='global constant input u = 1')
profiles.axvspan(epsilon,2*epsilon,color=red,alpha=.08)
profiles.axvline(0,color=green,ls=':',lw=2);profiles.axvline(1,color=green,ls=':',lw=2)
profiles.text(.19,.68,r'$\int h_\varepsilon\,dt=1$',fontsize=16,color=red)
profiles.text(.64,.38,r'$\|g\|_{L^2}=1$',fontsize=16,color=blue)
profiles.text(.18,.20,r'$v\in H_0^1:\quad |v(t)|\leq\sqrt{t}\,\|v^\prime\|_2$',fontsize=16)
profiles.set_title(r'B. Exact support geometry; $\varepsilon=1/16$',loc='left',pad=12)
profiles.set_xlim(-.02,1.02);profiles.set_ylim(-.04,1.16)
profiles.set_xlabel('physical plaque coordinate t');profiles.set_ylabel('profile / maximum')
profiles.legend(loc='upper right',fontsize=11,framealpha=.97)
profiles.grid(alpha=.17)

eps=np.geomspace(2**-14,1/12,500)
norms.semilogx(eps,np.sqrt(2*eps),color=red,lw=3,label=r'local Dirichlet norm $\leq\sqrt{2\varepsilon}$')
norms.semilogx(eps,np.full_like(eps,.5),color=blue,lw=3,label=r'global physical norm $\geq1/2$')
norms.set_ylim(0,.62);norms.set_xlim(eps[0],eps[-1])
norms.set_xlabel(r'$\varepsilon$');norms.set_ylabel('proved norm bound')
norms.set_title('C. Vanishing local bound; fixed global lower bound',loc='left',pad=12)
norms.legend(loc='upper left',fontsize=12);norms.grid(alpha=.23,which='both')
norms.text(.00010,.19,r'$H_0^1(0,1)\ \to\ L^2(0,1)$',fontsize=17,color=red)
norms.text(.00010,.40,r'$H^1(M)\ \to\ L^2(M)$',fontsize=17,color=blue)

constants.loglog(eps,1/(2*np.sqrt(2*eps)),color=green,lw=3)
constants.set_xlim(eps[0],eps[-1]);constants.set_xlabel(r'$\varepsilon$')
constants.set_ylabel('required comparison constant')
constants.set_title('D. A uniform lift estimate is impossible',loc='left',pad=12)
constants.grid(alpha=.23,which='both')
constants.text(.00019,4.0,r'$c_\varepsilon\geq\dfrac{1}{2\sqrt{2\varepsilon}}\longrightarrow\infty$',fontsize=23,color=green)
constants.text(.00019,1.8,'With the ambient quotient input:\n'+r'$\|A_\varepsilon\|=\|\widetilde B_\varepsilon\|_{R\to L^2(M)}\geq1/2$',fontsize=16)

fig.suptitle('A zero-trace plaque input misses a legitimate global constant',fontsize=25,fontweight='bold',y=.974)
fig.text(.055,.915,r'$k_\varepsilon(x,y)=g(x)h_\varepsilon(y),\qquad A_\varepsilon u=g\int h_\varepsilon u,\qquad P=1-\partial_t^2$',fontsize=21)
fig.text(.055,.105,'Figure 6.8c. DD.1–DD.11: exact supports, full completed input domains, analytic upper/lower bounds and quotient comparison.\n'
    'The curves are proved bounds, not computed operator norms. Kernel profiles in B are divided by their exact maxima.\n'
    'Historical context: Connes, IHES/P/79/301, Proposition 6(a), printed p.8.10. No historical local norm is inferred.\n'
    'Original independently authored diagram and reproducible source; CC0 1.0.',fontsize=12,linespacing=1.5,verticalalignment='top')
fig.savefig(HERE/'kt-plaque-dirichlet-input.png',dpi=110,metadata={'Software':'Original independently authored CC0 mathematical diagram'})
fig.savefig(HERE/'kt-plaque-dirichlet-input.svg',metadata={'Date':None,'Creator':'Original independently authored CC0 diagram'})
plt.close(fig)

"""CC0 reproducible illustrations of OF5's domain and collision estimate."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
D=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans'})
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'SH02-tubular_shrinking-v1'})
fig,axes=plt.subplots(2,1,figsize=(11,8),layout='constrained',gridspec_kw={'height_ratios':[1,1.65]})
ax=axes[0]
x=np.linspace(-4,4,1601);s=.2/(1+x*x)
ax.fill_between(x,-s,s,color='#cee5df');ax.plot(x,s,color='#197458');ax.plot(x,-s,color='#197458')
ax.axhline(0,color='#26466b',lw=2)
for a in [-2,0,2]:
    sa=.2/(1+a*a)
    ax.annotate('',xy=(a,sa),xytext=(a,-sa),arrowprops={'arrowstyle':'<->','color':'#26466b'})
ax.text(.1,.09,r'$f(x,v)=(x,v)$',fontsize=13)
ax.set_title('An explicit tube over a noncompact base',loc='left',fontsize=15,weight='bold')
ax.set_xlim(-4,4);ax.set_ylim(-.24,.24)
ax.set_xlabel(r'$x\in\mathbb{R}$ (a finite plotting window)');ax.set_ylabel(r'normal coordinate $v$')
ax.text(.02,.04,r'$M=\mathbb{R}\times\{0\},\quad D_s=\{|v|<s(x)\},\quad s(x)=0.2/(1+x^2)>0$',transform=ax.transAxes,fontsize=12)
ax.grid(alpha=.15)

ax=axes[1]
m=np.array([0.,0.]);mp=np.array([.8,0.]);z=np.array([.4,.3])
ax.add_patch(Circle(m,1,facecolor='#e7eff9',edgecolor='#426992',alpha=.65,lw=1.6))
ax.add_patch(Circle(mp,1.2,facecolor='#d9eee5',edgecolor='#338169',alpha=.5,lw=1.6))
ax.plot([0,.8],[0,0],color='#333333',lw=2)
for p in [m,mp]:ax.plot([p[0],z[0]],[p[1],z[1]],'--',color='#333333',lw=1.4)
ax.scatter([m[0],mp[0],z[0]],[m[1],mp[1],z[1]],color='#182b41',zorder=5)
ax.text(-.12,-.16,r'$m$',fontsize=14);ax.text(.82,-.16,r"$m'$",fontsize=14);ax.text(.39,.35,r'$z$',fontsize=14)
ax.annotate(r'$d(m,z)=0.5<1$',xy=(.2,.15),xytext=(-.92,.51),fontsize=10,arrowprops={'arrowstyle':'->','lw':.8})
ax.annotate(r"$d(m',z)=0.5<1.2$",xy=(.6,.15),xytext=(.72,.55),fontsize=10,arrowprops={'arrowstyle':'->','lw':.8})
ax.text(.4,-.40,r"$\delta=d(m,m')=0.8$",fontsize=11,ha='center')
ax.text(-.86,-.70,r'$r(m)=1$',color='#26466b',fontsize=12)
ax.text(1.10,-.83,r"$r(m')=1.2$",color='#197458',fontsize=12)
ax.set_title('The metric implication for a hypothetical common image z',loc='left',fontsize=15,weight='bold')
ax.set_xlim(-1.05,2.08);ax.set_ylim(-1.60,1.3);ax.set_aspect('equal')
ax.set_xticks([]);ax.set_yticks([])
ax.text(.02,.02,r"$\delta<r(m)+r(m')\leq2r(m)+\delta/4\quad\Rightarrow\quad\delta<8r(m)/3$",transform=ax.transAxes,fontsize=11)
fig.suptitle('Variable tubular shrinking — OF5.3–OF5.5',fontsize=17,weight='bold')
fig.savefig(D/'tubular_shrinking.png',dpi=180)
fig.savefig(D/'tubular_shrinking.svg',metadata={'Date':None})
plt.close(fig)
print('figure_written')

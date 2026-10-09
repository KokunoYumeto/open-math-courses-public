"""Exact spatial and time sections for CP.17-CP.31; original CC0 figure."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

root=Path(__file__).resolve().parent
data={'tau':1.,'alpha':.35,'beta':.65,'a':2.1,'b':2.5,'c':3.,
      'B_star':4.,'A':5.,'outer_transition_inner':3.2,'eta_real':.95,
      'eta_imag':0.,'sections':'one complex spatial coordinate; final w=-1 real'}
t=data['tau'];aa=data['alpha'];bb=data['beta'];c=data['c'];b=data['b']
ink='#173d46';orange='#ac552d';blue='#a8d4e0';green='#4d856b'
fig,axes=plt.subplots(1,2,figsize=(13,6.3),constrained_layout=True)
ax=axes[0];ax.set_aspect('equal');ax.set_facecolor('#f8faf8')
ax.add_patch(Circle((0,0),c*t,color=blue,alpha=.22))
ax.add_patch(Circle((0,0),data['A']*t,fill=False,color=ink,lw=1.5,ls='--'))
ax.add_patch(Wedge((0,0),data['B_star']*t,0,360,
                  width=(data['B_star']-data['outer_transition_inner'])*t,
                  color=green,alpha=.14))
ax.add_patch(Wedge((0,0),c*aa,0,360,width=(c-b)*aa,color=orange,alpha=.65))
ax.add_patch(Wedge((data['eta_real'],0),c*bb,0,360,
                  width=(c-b)*bb,color='#456fa2',alpha=.42))
ax.plot([0,data['eta_real']],[0,0],color=orange,lw=2)
ax.plot([0,data['eta_real']],[0,0],'o',color=orange,ms=4)
ax.text(.3,.14,r'$\eta=0.95$',color=orange)
ax.text(-1.1,-.23,r'$P$: $0.875\leq|\eta|\leq1.05$',fontsize=10,color=orange)
ax.text(.6,2.17,r'$Q$: $1.625\leq|\zeta-\eta|\leq1.95$',fontsize=10,color='#456fa2')
ax.text(-2.9,-2.13,r'Final density: $|\zeta|\leq c\tau=3$',color=ink)
ax.text(-3.3,3.63,r'Primitive: $|\zeta|<B_*\tau=4$',color=green)
ax.text(-4.1,-4.13,r'Common cone section: $|\zeta|\leq A\tau=5$',color=ink)
ax.set(xlim=(-5.45,5.45),ylim=(-5.45,5.45),xlabel=r'$\operatorname{Re}\zeta$',
       ylabel=r'$\operatorname{Im}\zeta$',title='Exact spatial sections at final time length 1')
ax.grid(alpha=.15)
ax=axes[1];ax.set_facecolor('#f8faf8')
v=np.linspace(0,1,200);ax.plot(v,1-v,color=ink,lw=3)
ax.scatter([aa],[bb],color=orange,s=75,zorder=4)
ax.text(aa+.025,bb+.04,r'$(\alpha,\tau-\alpha)=(0.35,0.65)$',color=orange)
ax.scatter([0,1],[1,0],color=ink,s=40)
ax.text(.08,.96,'Zero-moment subtraction\nat the first endpoint',fontsize=11,va='top')
ax.text(.54,.12,'Zero-moment subtraction\nat the second endpoint',fontsize=11)
ax.text(.09,.43,r'$\alpha\geq0,\quad\tau-\alpha\geq0$',fontsize=13)
ax.text(.09,.34,r'$\alpha+(\tau-\alpha)=\tau=1$',fontsize=13)
ax.text(.09,.24,r'$c\alpha+c(\tau-\alpha)=c\tau=3$',fontsize=13)
ax.set(xlim=(-.04,1.04),ylim=(-.04,1.04),xlabel=r'First negative time length $\alpha$',
       ylabel=r'Second negative time length $\tau-\alpha$',title='Exact compact intermediate time fibre')
ax.grid(alpha=.15);ax.set_aspect('equal')
fig.suptitle('Cauchy-shell convolution and the support of its explicit primitive',fontsize=16,color=ink)
fig.savefig(root/'shell-homotopy-geometry.png',dpi=180)
fig.savefig(root/'shell-homotopy-geometry.svg')
(root/'shell-homotopy-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')


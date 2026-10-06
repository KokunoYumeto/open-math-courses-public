"""Exact support and excess models for AC11/AC12/AC31–AC34. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-analytic-clean-composition','font.size':12})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,12),layout='constrained')
gs=fig.add_gridspec(3,1,height_ratios=[1.35,.8,1.1])
ax=fig.add_subplot(gs[0])
s=np.linspace(.02,4,500)
ax.fill_between(s,s/3,3*s,color='#e6eff2',label=r'Possible cutoff support: $1/3<\theta/\sigma<3$')
ax.fill_between(s,s/2,2*s,color='#b6d8dd',label=r'$\chi=1$ on $1/2\leq\theta/\sigma\leq2$')
ax.plot(s,s,color='#135d70',lw=2.4,label=r'Matching frequencies: $\theta=\sigma$')
for ratio in [.5,2]:ax.plot(s,ratio*s,color='#677b86',lw=.9,ls='--')
ax.set(xlim=(0,4),ylim=(0,4),xlabel=r'$\sigma>0$',ylabel=r'$\theta>0$',
       title='Separated frequencies have no middle stationary point (AC31)')
ax.text(.52,.08,r'$|\sigma-\theta|\geq(\sigma+\theta)/3$'+'\n'+r'on the support of $1-\chi$',
        transform=ax.transAxes,fontsize=12,bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.12)
ax=fig.add_subplot(gs[1]);ax.axis('off')
ax.set_title('The middle coordinate becomes a homogeneous variable',pad=12)
ax.text(.02,.78,r'$r=(|\theta|^2+|\sigma|^2)^{1/2},\qquad\omega=(ry,\theta,\sigma)$',fontsize=16,transform=ax.transAxes)
ax.text(.02,.46,r'$dy\,d\theta\,d\sigma=r^{-n_Y}\,d\omega$',fontsize=18,transform=ax.transAxes)
ax.text(.02,.13,r'New amplitude order: $\mu_1+\mu_2-n_Y$ (AC12–AC14)',fontsize=14,transform=ax.transAxes)
ax=fig.add_subplot(gs[2]);ax.axis('off')
ax.set_title('A proper composition with one excess direction (AC32–AC34)',pad=15)
for xy,label in [((.16,.77),r'$X:\ (x,\xi)$'),((.53,.77),r'$Y:\ ((x,v),(\xi,0))$'),((.89,.77),r'$Z:\ (x,\xi)$')]:
 ax.text(*xy,label,ha='center',va='center',fontsize=14,transform=ax.transAxes,
         bbox={'boxstyle':'round,pad=.45','facecolor':'#ecf4f6','edgecolor':'#53727f'})
ax.annotate('',xy=(.27,.77),xytext=(.36,.77),xycoords='axes fraction',arrowprops={'arrowstyle':'->','color':'#135d70'})
ax.annotate('',xy=(.70,.77),xytext=(.79,.77),xycoords='axes fraction',arrowprops={'arrowstyle':'->','color':'#135d70'})
ax.text(.03,.51,r'$v$ is the clean fibre; $\xi\ne0$ is preserved; $e=1$.',fontsize=15,transform=ax.transAxes)
ax.text(.03,.30,r'$m_A=m_B=-1/4,\quad m_{AB}=-1/4-1/4+1/2=0$',fontsize=15,transform=ax.transAxes)
ax.text(.03,.08,r'$AB=\left(\int\alpha(v)\beta(v)\,dv\right)\mathrm{Id}$',fontsize=18,transform=ax.transAxes)
fig.savefig(out/'analytic-composition.svg',metadata={'Date':None,'Creator':'Original AN-04 programme figure; CC0'})
fig.savefig(out/'analytic-composition.png',dpi=150)
plt.close(fig)

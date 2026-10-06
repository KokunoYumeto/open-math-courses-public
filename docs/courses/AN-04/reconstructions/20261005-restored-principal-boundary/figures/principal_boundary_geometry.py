"""Exact PTA4-PTA5 sections, CC0, GPT-6 Astra (OpenAI), 2026-10-05."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.fonttype':'path'})
fig,axes=plt.subplots(2,1,figsize=(7,9),layout='constrained')
ss=np.linspace(-1,1,701)
axes[0].axvspan(-.22,0,color='#e8edf0')
axes[0].plot(ss*ss,ss,color='#146575',lw=3)
axes[0].scatter([0],[0],s=60,color='#b64926',zorder=3)
axes[0].annotate(r'$H_pt=0$'+'\n'+r'$H_p^2t=2$',(0,0),xytext=(.35,-.17),arrowprops={'arrowstyle':'->'})
axes[0].set(xlim=(-.22,1.05),ylim=(-1.1,1.1),xlabel=r'$t$',ylabel=r'$\tau$',title='Projected characteristic at '+r'$\xi=1$'+'\n'+r'$(t,\tau)=(s^2,s)$')
axes[0].text(-.11,.75,'No real\nroots',ha='center',fontsize=13)
eps=.2;kappa=(1-3/np.sqrt(10))**2
x=np.linspace(-.46,.46,701)
colors=['#146575','#437dad','#9f5798']
for j,color in zip(range(1,4),colors):
 a=eps/2*(1-2**(1-2*j))
 tt=eps*(eps-a-x*x-kappa)
 axes[1].plot(x,np.where(tt>=0,tt,np.nan),color=color,lw=2,label=r'$\rho=a_'+str(j)+'$')
inner=eps*(eps/2-x*x-kappa)
axes[1].fill_between(x,0,np.maximum(inner,0),color='#bdcfa1',alpha=.8,label=r'Every $q_j=1$')
axes[1].plot(x,np.where(inner>=0,inner,np.nan),color='#4b6c30',lw=2,ls='--')
axes[1].set(xlabel=r'$x$',ylabel=r'$t$',ylim=(0,.032),title='One collar inside every cutoff\n'+r'$\epsilon=1/5,\quad \xi=3,\quad \eta=1$')
axes[1].legend(loc='upper right',fontsize=12)
for ax in axes:
 ax.grid(alpha=.18);ax.spines[['right','top']].set_visible(False)
fig.suptitle('Boundary merger and a fixed inner collar',fontsize=18)
fig.savefig(OUT/'principal-boundary-geometry.svg')
fig.savefig(OUT/'principal-boundary-geometry.png',dpi=160)

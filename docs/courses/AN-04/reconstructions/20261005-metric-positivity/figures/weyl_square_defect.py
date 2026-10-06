"""Original figure for MP6-MP7; CC0, GPT-6 Astra (OpenAI), 2026-10-05."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.fonttype':'path'})
fig,axes=plt.subplots(2,1,figsize=(6.4,8.8),layout='constrained')
t=np.linspace(-7,7,701);L=2
density=np.exp(-t*t/L**2)/(np.sqrt(np.pi)*L)
axes[0].plot(t,density,color='#146575',lw=2.8)
axes[0].fill_between(t,density,color='#146575',alpha=.12)
axes[0].set(xlabel=r'$t=\log x$',ylabel=r'$|v_2(t)|^2$',title=r'Normalized density at $L=2$')
axes[0].text(.98,.85,r'$\int |v_2(t)|^2\,dt=1$',transform=axes[0].transAxes,ha='right')
ell=np.linspace(.8,5,500);energy=1/(2*ell**2)-.25
axes[1].plot(ell,energy,color='#b64926',lw=2.8)
axes[1].axhline(0,color='#657581',lw=1);axes[1].axhline(-.25,color='#146575',ls='--',label=r'Limit $-1/4$')
axes[1].scatter([np.sqrt(2),2],[0,-.125],s=48,color='#b64926',zorder=3)
axes[1].annotate(r'$(\sqrt{2},0)$',(np.sqrt(2),0),xytext=(1.7,.20),arrowprops={'arrowstyle':'->','color':'#465665'})
axes[1].annotate(r'$(2,-1/8)$',(2,-.125),xytext=(2.5,.05),arrowprops={'arrowstyle':'->','color':'#465665'})
axes[1].set(xlabel=r'Spread $L>0$',ylabel=r'$E(L)$',title='Exact expectation for $u_L$\n'+r'$E(L)=\frac{1}{2L^2}-\frac{1}{4}$')
axes[1].legend(loc='upper right',fontsize=15)
for ax in axes:
 ax.grid(alpha=.2);ax.spines[['right','top']].set_visible(False)
fig.suptitle('An exact Weyl square defect\n'+r'$(x^2\xi^2)^w=(xD-i/2)^2-1/4$',fontsize=19)
fig.savefig(OUT/'weyl-square-defect.svg')
fig.savefig(OUT/'weyl-square-defect.png',dpi=160)

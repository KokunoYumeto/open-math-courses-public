"""Exact quadratic models for G3/G7/G8. Original programme figure, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-Maslov-composition','font.size':12})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,12),layout='constrained')
gs=fig.add_gridspec(3,1,height_ratios=[1,1.3,1.1])
ax=fig.add_subplot(gs[0]);ax.axis('off')
ax.set_title('The excess is removed from the phase, retained in the density',pad=16)
ax.text(.03,.83,r'$\Phi(y,\theta,\sigma)=y(\theta+\sigma)$',fontsize=17,transform=ax.transAxes)
ax.text(.03,.62,r'$u=\theta+\sigma,\quad t=\theta:\qquad\Phi=yu$',fontsize=17,transform=ax.transAxes)
ax.text(.03,.39,r'Critical set: $y=u=0$; free $t\in E\simeq\mathbb{R}$',fontsize=15,transform=ax.transAxes)
ax.text(.03,.14,r'Quotient phase: $yu$; signature $0$; remaining density $|dt|$',fontsize=15,transform=ax.transAxes)
ax=fig.add_subplot(gs[1])
for h in [np.linspace(-3,-.15,700),np.linspace(.15,3,700)]:
 c=np.exp(1j*np.pi*np.sign(h)/4)/np.sqrt(np.abs(h))
 ax.plot(h,c.real,color='#12647b',lw=2.2,label='Real part' if h[0]<0 else None)
 ax.plot(h,c.imag,color='#a4412b',lw=2.2,ls='--',label='Imaginary part' if h[0]<0 else None)
ax.axvline(0,color='#61707b',lw=1,ls=':')
ax.axhline(0,color='#61707b',lw=.7)
ax.set(xlabel=r'$h=a+b\ne0$',ylabel='Gaussian coefficient',
 title=r'Transverse chirps: $e^{\pi i\,\mathrm{sgn}(h)/4}/\sqrt{|h|}$ (G30)')
ax.text(.04,.93,r'$h=0$: excess $1$; (G30) has no value there',transform=ax.transAxes,va='top',
 bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
ax.legend(loc='lower right');ax.grid(alpha=.15)
ax=fig.add_subplot(gs[2]);ax.axis('off')
ax.set_title('Why the excess changes the order (G26–G29)',pad=14)
lines=[
 (r'Middle symplectic density: $\nu_Y\mapsto t^{n_Y}\nu_Y$',.88),
 (r'Dual-excess lifts: $v_j\mapsto t^{-1}T_Yv_j$ for $j=1,\ldots,e$',.64),
 (r'Normalization: $\sqrt{t^{n_Y}t^{-e}}=t^{(n_Y-e)/2}$',.40),
 (r'$M_{\rm out}=m_C+m_D+e/2+(n_X+n_Z)/4$',.14)]
for label,y in lines:ax.text(.03,y,label,fontsize=15,transform=ax.transAxes,va='center')
fig.savefig(out/'maslov-composition.svg',metadata={'Date':None,'Creator':'Original AN-04 programme figure; CC0'})
fig.savefig(out/'maslov-composition.png',dpi=150);plt.close(fig)

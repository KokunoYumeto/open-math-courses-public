"""Exact scalar frozen-frequency curvature model; original figure, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':11})
fig=plt.figure(figsize=(14,10),dpi=150,facecolor='#fffdfa')
ink='#193249';muted='#4b5867';blue='#4389b7';purple='#865987'
fig.text(.045,.955,'Curvature creates a positive factor estimate',fontsize=21,weight='bold',color=ink)
fig.text(.045,.916,r'$a(\eta)=i\langle\eta\rangle,\quad \eta_\tau=(\sqrt{\tau^2-1},0,\ldots,0),\quad\phi(t)=t+t^2/2$',fontsize=14,color=ink)
fig.text(.045,.88,r'Freeze $\langle\eta_\tau\rangle=\tau$ exactly: $T_\tau=D_t+i\tau\phi^\prime-i\tau=D_t+i\tau t$ on $t\in\mathbb{R}$.',fontsize=12,color=ink)
left=fig.add_axes([.08,.435,.38,.34],facecolor='#fffdfa')
right=fig.add_axes([.59,.435,.35,.34],facecolor='#fffdfa')
t=np.linspace(-.55,.55,1101)
for tau,color in [(16,blue),(64,purple)]:
    g=(tau/np.pi)**.25*np.exp(-tau*t*t/2)
    label={16:r'$\tau=16$',64:r'$\tau=64$'}[tau]
    left.plot(t,tau*t,color=color,lw=2.3,label=label)
    right.plot(t,g*g,color=color,lw=2.3,label=label)
    sigma=(2*tau)**-.5
    right.axvline(sigma,color=color,ls=':',lw=1.1)
    right.axvline(-sigma,color=color,ls=':',lw=1.1)
left.axhline(0,color='#9daab3',lw=1)
left.axvline(0,color='#9daab3',lw=1)
left.set_xlim(-.55,.55);left.set_ylim(-38,38)
left.set_xlabel(r'Time $t$');left.set_ylabel(r'Imaginary coefficient $\tau t$')
left.set_title(r'Coefficient slope $= \tau\phi^{\prime\prime}=\tau$',fontsize=13,weight='bold',pad=17)
right.set_xlim(-.55,.55);right.set_ylim(0,5)
right.set_xlabel(r'Time $t$');right.set_ylabel(r'Normalized density $|g_\tau(t)|^2$')
right.set_title('An exact Gaussian attains the energy identity',fontsize=12.5,weight='bold',pad=17)
for ax in [left,right]:
    ax.grid(alpha=.2);ax.legend(frameon=False)
    for spine in ax.spines.values():spine.set_color('#bdc7ce')
fig.text(.59,.353,r'$g_\tau(t)=(\tau/\pi)^{1/4}e^{-\tau t^2/2},\quad \|g_\tau\|_2=1$',fontsize=12,color=ink)
fig.text(.59,.317,r'Dotted lines: $t=\pm(2\tau)^{-1/2}$, the density standard deviation.',fontsize=10.5,color=muted)
fig.text(.08,.355,'Larger weight: steeper coefficient, narrower test profile.',fontsize=11,color=ink)
fig.text(.08,.316,'The horizontal axis is the same in both sampled plots.',fontsize=10.5,color=muted)
box=FancyBboxPatch((.045,.16),.91,.112,transform=fig.transFigure,boxstyle='round,pad=.008',facecolor='#f4f7f8',edgecolor='#587a92',lw=1.3)
fig.add_artist(box)
fig.text(.5,.232,r'$[T_\tau^*,T_\tau]=2\tau,\qquad T_\tau^*g_\tau=0,\qquad\|T_\tau g_\tau\|_2^2=2\tau$',ha='center',fontsize=15,color=ink)
fig.text(.5,.183,'Exact equality on the full time line. Compact cutoffs give the local scale; Exercise4 proves sharpness with compact tests.',ha='center',fontsize=10.5,color=ink)
fig.text(.045,.116,'This is a scalar frozen-frequency model: the Gaussian is Schwartz on ℝ, and is not a compact slab input.',fontsize=10.5,color=muted)
fig.text(.045,.083,'Full variable-symbol estimate: Theorem2.1 and (4.1)–(4.6). Exact model: Exercise3. Compact sharpness: Exercise4.',fontsize=9.5,color=muted)
fig.text(.045,.045,'Hörmander IV,Proposition28.1.2,pp221–222. Original diagram and reproducible Python source;CC0.',fontsize=9.5,color=muted)
fig.savefig(Path(__file__).with_name('curvature-and-cauchy-factor.png'),dpi=150)

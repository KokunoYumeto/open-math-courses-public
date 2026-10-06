"""Exact specified slices of U024 (7.2)/(7.4); sampled curves are illustrations."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans','mathtext.fontset':'stix',
 'font.size':18,'axes.titlesize':22,'axes.labelsize':20,'xtick.labelsize':17,'ytick.labelsize':17})
fig,axes=plt.subplots(2,1,figsize=(8,9.5),layout='constrained')
x=np.linspace(-.4,.4,1001)
for t,color in [(0,'#303b44'),(.5,'#bd6727'),(1,'#166782')]:
    denominator=1+t*1.5*x;assert np.min(denominator)>0
    axes[0].plot(x,1/denominator,color=color,lw=2.8,label=r'$t='+('1/2' if t==.5 else str(t))+r'$')
axes[0].axvline(0,color='#687984',lw=1.3,ls=':');axes[0].scatter([0],[1],s=45,color='#166782',zorder=4)
axes[0].annotate('Fixed critical ray',xy=(0,1),xytext=(-.25,2.15),fontsize=18,
 arrowprops={'arrowstyle':'->','color':'#687984'},color='#33434c',
 bbox={'facecolor':'white','edgecolor':'none','pad':.3})
axes[0].set(title=r'Radial flow: $r_t/r_0$',xlabel=r'$x_1$  (with $x_2=0$)',ylabel=r'$r_t/r_0$',
 xlim=(-.4,.4),ylim=(.5,2.65));axes[0].set_xticks([-.4,-.2,0,.2,.4]);axes[0].legend(loc='upper right',fontsize=18,framealpha=1)
z=np.linspace(-1,1,1001)
axes[1].plot(z,z*z,color='#166782',lw=2.8,label=r'$z^2$  (correct)')
axes[1].plot(z,2.25*z*z,color='#bd6727',lw=2.8,ls='--',label=r'$(9/4)z^2$  (reversed)')
axes[1].set(title='Quadratic block after substitution',xlabel=r'$z_{\mathrm{new}}$',ylabel='Quadratic term',
 xlim=(-1,1),ylim=(-.05,2.45));axes[1].set_xticks([-1,-.5,0,.5,1]);axes[1].legend(loc='upper center',fontsize=18,framealpha=1)
for ax in axes:
    ax.grid(alpha=.17);ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
fig.savefig(out/'phase-flow-and-quadratic-radius.svg',metadata={'Creator':'AN-04 original mathematical illustration',
 'Description':'Specified radial-flow and quadratic-radius slices, with exact equations and domains in U024 Figure 7.1.', 'Date':None})
fig.savefig(out/'phase-flow-and-quadratic-radius.png',dpi=170)
plt.close(fig)
print('Saved exact two-panel phase-flow/radius illustration and inspection PNG.')

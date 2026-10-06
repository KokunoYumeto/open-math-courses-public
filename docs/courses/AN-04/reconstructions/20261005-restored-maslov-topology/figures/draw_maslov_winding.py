"""Exact U025 determinant-square projection and transverse branch limits."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).resolve().parent
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans','mathtext.fontset':'stix',
 'font.size':18,'axes.titlesize':22,'axes.labelsize':20,'xtick.labelsize':17,'ytick.labelsize':17})
fig,axes=plt.subplots(2,1,figsize=(8,10.5),layout='constrained')
t=np.linspace(0,1,1001);ax=axes[0]
ax.plot(np.cos(2*np.pi*t),np.sin(2*np.pi*t),color='#166782',lw=2.8)
for a,b in [(.10,.16),(.58,.64)]:
    ax.annotate('',xy=(np.cos(2*np.pi*b),np.sin(2*np.pi*b)),xytext=(np.cos(2*np.pi*a),np.sin(2*np.pi*a)),
      arrowprops={'arrowstyle':'->','color':'#166782','lw':2.8,'mutation_scale':22})
ax.scatter([1,-1],[0,0],s=55,c=['#303b44','#bd6727'],zorder=5)
ax.annotate(r'$t=0,1$',xy=(1,0),xytext=(.30,-.40),fontsize=18,ha='center',
 arrowprops={'arrowstyle':'->','color':'#687984'},bbox={'facecolor':'white','edgecolor':'none','pad':.3})
ax.annotate(r'$t=1/2$'+'\nPositive crossing',xy=(-1,0),xytext=(-.12,.20),fontsize=18,ha='center',
 arrowprops={'arrowstyle':'->','color':'#687984'},bbox={'facecolor':'white','edgecolor':'none','pad':.3})
ax.set(title='Determinant square: one full turn',xlabel=r'$\operatorname{Re}\Delta$',ylabel=r'$\operatorname{Im}\Delta$',
 xlim=(-1.4,1.4),ylim=(-1.18,1.18),aspect='equal')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
ax=axes[1]
ax.plot(t,2*np.pi*t,color='#166782',lw=2.8,label=r'Continuous $\theta=2\pi t$')
left=np.linspace(0,.5-1e-6,1001);right=np.linspace(.5+1e-6,1,1001)
for values,label in [(left,r'Chart branch $F$'),(right,None)]:
    B=-np.tan(np.pi*values);F=-2*np.arctan(B)
    ax.plot(values,F,color='#bd6727',lw=2.8,ls='--',label=label)
ax.scatter([.5,.5],[np.pi,-np.pi],s=70,facecolor='white',edgecolor='#bd6727',linewidth=2.2,zorder=5)
ax.axvline(.5,color='#687984',lw=1.3,ls=':')
ax.annotate('',xy=(.53,-np.pi),xytext=(.53,np.pi),
 arrowprops={'arrowstyle':'->','color':'#687984','lw':1.5})
ax.text(.57,-.2,r'Jump $-2\pi$',color='#33434c',fontsize=18,
 bbox={'facecolor':'white','edgecolor':'none','pad':.3})
ax.text(.035,-2.0,r'$\nu=1$',fontsize=18,
 bbox={'facecolor':'white','edgecolor':'none','pad':.3})
ax.text(.035,-2.75,r'Coefficient $-i$',fontsize=18,
 bbox={'facecolor':'white','edgecolor':'none','pad':.3})
ax.set(title='Continuous phase and transverse chart branch',xlabel=r'$t$',ylabel='Phase',
 xlim=(0,1),ylim=(-3.75,7.15))
ax.set_xticks([0,.25,.5,.75,1]);ax.set_yticks([-np.pi,0,np.pi,2*np.pi],labels=[r'$-\pi$',r'$0$',r'$\pi$',r'$2\pi$'])
ax.legend(loc='upper left',fontsize=17,framealpha=1)
for ax in axes:
    ax.grid(alpha=.17);ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
fig.savefig(out/'maslov-winding-and-branch-jump.svg',metadata={'Creator':'AN-04 original mathematical illustration',
 'Description':'Determinant-square projection and exact transverse phase branch in U025 Figure 8.1. The line crossing is positive; forward Gaussian coefficient transport is -i.', 'Date':None})
fig.savefig(out/'maslov-winding-and-branch-jump.png',dpi=170)
plt.close(fig)
print('Saved exact Maslov winding and branch diagram and inspection PNG.',flush=True)

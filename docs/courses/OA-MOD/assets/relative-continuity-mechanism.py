"""Reproducible illustrations of the endpoint cutoff and the exact diagonal counterexample."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans','figure.facecolor':'#faf9f3','axes.facecolor':'#faf9f3','svg.hashsalt':'OA-MOD-RC-FIG-01'})
fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
fig.get_layout_engine().set(rect=(0,.08,1,.92))
s=np.linspace(.002,.998,1500)
ell=np.log((1-s)/s)
chi=np.where(s<.25,np.clip((s-.125)/.125,0,1),np.where(s<=.75,1,np.clip((.875-s)/.125,0,1)))
ax=axes[0];ax.plot(s,ell,color='#164c62',label=r'$\ell(s)=\log((1-s)/s)$');ax.axhline(0,color='#888888',lw=.6)
ax.set(xlim=(0,1),ylim=(-7,7),xlabel=r'$s=(1+a)^{-1}$',ylabel='Logarithmic spectral coordinate',title='The cutoff avoids both endpoints')
ax2=ax.twinx();ax2.plot(s,chi,color='#b34f2c',label=r'$\chi(s)$');ax2.set(ylim=(-.05,1.1),ylabel='One admissible cutoff')
ax.axvspan(0,.125,color='#b34f2c',alpha=.07);ax.axvspan(.875,1,color='#b34f2c',alpha=.07)
ax.text(.02,6,r'$a\to\infty$',fontsize=10);ax.text(.78,-6.2,r'$a\to0$',fontsize=10)
h1,l1=ax.get_legend_handles_labels();h2,l2=ax2.get_legend_handles_labels();ax.legend(h1+h2,l1+l2,loc='lower center',fontsize=10)
n=np.arange(1,13);strong=2*np.sqrt(3)*2.**(-n)
ax=axes[1];ax.plot(n,np.full(n.shape,2.),'s-',color='#b34f2c',label='Operator norm: exactly 2')
ax.plot(n,strong,'o-',color='#164c62',label=r'On $\eta_j=\sqrt{3}\,2^{-j}$: exactly $2\sqrt{3}\,2^{-n}$')
ax.set(yscale='log',xticks=[1,3,5,7,9,11],xlabel='Changed coordinate n',ylabel='Compact-time cocycle error',title=r'Strong convergence need not be norm convergence')
ax.grid(True,axis='y',alpha=.2);ax.legend(loc='lower left',fontsize=9)
fig.suptitle(r'Faithful relative modular continuity: RC-03 and RC-05',fontsize=14)
fig.text(.53,.005,r'Exact formulas at $T=\pi/\log 2$; the sample plot is not the general proof.',fontsize=9)
fig.savefig(out/'relative-continuity-mechanism.png',dpi=150)
fig.savefig(out/'relative-continuity-mechanism.svg',metadata={'Date':None})
plt.close(fig)


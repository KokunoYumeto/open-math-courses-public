"""Exact D_t model and cutoff from AN01-U090 Exercises 1 and 7. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(13,5.8),layout='constrained')
fig.set_facecolor('#f8fafc')
ax=axs[0]
ax.axhline(0,color='#c2ccd4',lw=.8);ax.axvline(0,color='#c2ccd4',lw=.8)
ax.plot([-2.1,0],[0,0],color='#ad5b35',lw=4)
ax.plot([0,2.1],[0,0],color='#236786',lw=4)
ax.annotate('',xy=(2.25,0),xytext=(1.9,0),arrowprops=dict(arrowstyle='->',color='#236786',lw=2.5))
ax.annotate('',xy=(-2.25,0),xytext=(-1.9,0),arrowprops=dict(arrowstyle='->',color='#ad5b35',lw=2.5))
for t in [-1.6,-.8,.8,1.6]:
 ax.annotate('',xy=(t,.48),xytext=(t,.02),arrowprops=dict(arrowstyle='->',color='#80508b',lw=1.8))
ax.scatter([0],[0],s=75,color='#263747',zorder=6)
ax.text(-1.8,-.3,r'$E_-:\ t\leq 0$',color='#ad5b35',fontsize=15)
ax.text(.55,-.3,r'$E_+:\ t\geq 0$',color='#236786',fontsize=15)
ax.text(-2.23,1.05,r'$D_tE_\pm=\delta_{(0,0)}$',fontsize=16)
ax.text(-2.23,.79,r'Purple arrows: $\xi=(0,1)$',color='#80508b',fontsize=12)
ax.annotate('Every nonzero covector\noccurs at the origin',xy=(0,0),xytext=(-.9,-1.04),fontsize=11,ha='center',arrowprops=dict(arrowstyle='->',color='#263747',connectionstyle='arc3,rad=-.1'))
ax.text(.6,-.87,r'Base flow: $\nabla p=(1,0)$',fontsize=11)
ax.set(xlim=(-2.4,2.4),ylim=(-1.25,1.35),xlabel=r'$t$',ylabel=r'$z$')
ax.set_title('Two signed transport kernels',fontweight='bold',pad=12)
ax=axs[1]
def flat(r):
 out=np.zeros_like(r,dtype=float);positive=r>0
 out[positive]=np.exp(-1/r[positive]);return out
def step(r):return flat(r)/(flat(r)+flat(1-r))
t=np.linspace(-1.05,2.05,2001);psi=step(4*(t+.75))*step(4*(1.75-t))
ax.axvspan(-1,.25,color='#e3edf0',alpha=.95)
for lo,hi in [(-.75,-.5),(1.5,1.75)]:ax.axvspan(lo,hi,color='#e9c9b8',alpha=.8)
ax.plot(t,psi,color='#236786',lw=2.7)
for value in [0,1]:
 ax.axvline(value,color='#9eabb6',lw=1,ls='--')
 ax.scatter([value],[1],s=32,color='#263747',zorder=5)
ax.text(-.05,1.1,r'$y=0$',ha='right')
ax.text(1.05,1.1,r'$x=1$',ha='left')
ax.text(-.31,.73,'Regular\nnear y',fontsize=11,color='#315e6b')
ax.annotate(r'Only $dt$ directions',xy=(-.625,.47),xytext=(.32,.42),fontsize=11,arrowprops=dict(arrowstyle='->',color='#80508b'),color='#80508b')
ax.annotate('',xy=(-1,-.2),xytext=(1,-.2),arrowprops=dict(arrowstyle='->',color='#263747',lw=1.6))
ax.text(-.05,-.32,r'Backward base ray: $t\leq 1$',ha='center',fontsize=10)
ax.set(xlim=(-1.05,2.05),ylim=(-.42,1.3),xlabel=r'$t$',ylabel=r'$\chi(t,0)=\psi(t)$')
ax.set_xticks([-.75,-.5,0,1,1.5,1.75],['−3/4','−1/2','0','1','3/2','7/4'])
ax.tick_params(axis='x',labelsize=10)
ax.set_title('A cutoff with the needed directions',fontweight='bold',pad=12)
fig.suptitle('Analytic singularities follow a characteristic direction',fontsize=16,fontweight='bold')
fig.supxlabel('Exact model P = Dₜ. The cutoff is the smooth step product in Exercise 7; the displayed covector is dz.',fontsize=10)
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.png'),dpi=190);fig.savefig(out.with_suffix('.svg'))
svg=out.with_suffix('.svg');svg.write_text('\n'.join(l.rstrip() for l in svg.read_text().splitlines())+'\n')

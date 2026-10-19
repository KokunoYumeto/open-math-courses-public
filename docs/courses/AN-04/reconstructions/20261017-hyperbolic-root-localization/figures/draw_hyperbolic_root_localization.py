"""Exact root, amplification and quadratic-cone sections. Independent code: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.titlesize':15,
 'axes.labelsize':13,'svg.fonttype':'none','svg.hashsalt':'an04-hyperbolic-root-localization'})
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
ax=axs[0,0];R=np.geomspace(1,100,501)
ax.plot(R,np.sqrt(R),color='#126b86',lw=2.5,label='Im(τ − R) = +√R')
ax.plot(R,-np.sqrt(R),color='#b85022',lw=2.5,label='Im(τ − R) = −√R')
ax.axhline(0,color='#9aa6ac',lw=.8)
ax.set(xscale='log',xlabel='Positive tangential frequency R',ylabel='Centered imaginary normal frequency',
 title='(a) Exact roots of (τ − R)² + R')
ax.text(2,-8.5,'Negative imaginary part:\nforward growth exp(t√R)',color='#8b3d1a',fontsize=12)
ax.legend(loc='upper left',fontsize=11)
ax=axs[0,1];R=np.geomspace(1,1_000_000,901)
ax.plot(R,np.sqrt(R)/4,color='#b85022',lw=2.5,label='log amplification = √R / 4')
ax.plot(R,6*np.log(R),color='#126b86',lw=2.5,label='log(R⁶) = 6 log R')
ax.set(xscale='log',xlabel='R',ylabel='Logarithm of the positive quantity',
 title='(b) Exact amplification at time T = 1/4')
ax.legend(loc='upper left',fontsize=11)
ax=axs[1,0];s=np.linspace(-1.15,1.15,701)
ax.fill_between(s,np.abs(s),1.45,where=np.abs(s)<1.45,color='#c9ddbd',label='Γ: z > |s|')
ax.plot(s,s,color='#126b86',lw=2);ax.plot(s,-s,color='#126b86',lw=2,label='Q = 0: z = ±s')
ax.scatter([0],[1],s=40,c='#ae4423',zorder=4);ax.annotate('N = (0, 1)',(0,1),(.17,1.15),
 arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set(xlim=(-1.15,1.15),ylim=(-1.35,1.45),xlabel='Parameter s',ylabel='Normal variable z',
 title='(c) Quadratic localization Q = z² − s²')
ax.legend(loc='lower left',fontsize=11)
ax=axs[1,1];t=np.linspace(0,1,701)
ax.axvspan(-.25,0,color='#e9eef2')
ax.plot(t,np.sqrt(t),color='#126b86',lw=2,label='z = +√t')
ax.plot(t,-np.sqrt(t),color='#b85022',lw=2,label='z = −√t')
ax.plot([-.25,1],[0,0],color='#31434c',lw=1.6,label='z = 0')
ax.text(-.125,.52,'Two roots\nnonreal',ha='center',fontsize=10.5)
ax.scatter([0],[0],s=35,c='#31434c',zorder=4)
ax.set(xlim=(-.25,1),ylim=(-1.12,1.12),xlabel='One-sided parameter t',ylabel='Real normal roots z',
 title='(d) z³ − tz: quadratic jet −tz')
ax.legend(loc='lower left',fontsize=10)
for ax in axs.flat:
 ax.grid(alpha=.2);ax.spines[['right','top']].set_visible(False)
fig.savefig(OUT/'hyperbolic-root-localization.svg',metadata={'Date':None,'Creator':'Independent programme figure; Python/Matplotlib'})
plt.close(fig)

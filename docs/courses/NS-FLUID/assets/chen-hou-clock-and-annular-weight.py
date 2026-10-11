"""Reproduce illustrations of QC1–QC21 and WT7–WT18; no source-profile numerics."""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':12,'legend.fontsize':10,'svg.fonttype':'none'})
colors=['#12645e','#ac4939','#5b57a2']
tau=np.linspace(0,6,161)
q=np.array([quad(lambda u:np.exp(-2*u+.25*(np.cos(t)-np.cos(t+u))),0,np.inf,epsabs=2e-12,epsrel=2e-12)[0] for t in tau])
Cw=5*np.exp(-2*tau+.25*(1-np.cos(tau)))
Cl=np.exp(-3*tau)
remaining=Cw*q
base=remaining/5
fig,axs=plt.subplots(1,2,figsize=(14,5.4),layout='constrained')
axs[0].plot(tau,q,color=colors[0],lw=2.3,label=r'Exact integral $q(\tau)$, sampled numerically')
axs[0].axhline(4/9,color=colors[1],ls='--',label=r'Proved lower bound $1/a_+=4/9$')
axs[0].axhline(4/7,color=colors[2],ls='--',label=r'Proved upper bound $1/a_-=4/7$')
axs[0].set(xlabel=r'Original rescaled time $\tau$',ylabel=r'$q=(T-t)/C_\omega$',title='The remaining-time factor retains the entire rate')
axs[0].set_ylim(.41,.60);axs[0].legend(loc='upper right')
axs[1].loglog(base,Cl,color=colors[0],lw=2.3,label=r'Original $C_l=e^{-3\tau}$')
axs[1].loglog(base,((7/4)*base)**(12/7),color=colors[1],ls='--',label=r'Lower: $[(7/4)(T-t)/5]^{12/7}$')
axs[1].loglog(base,np.minimum(1,((9/4)*base)**(4/3)),color=colors[2],ls='--',label=r'Upper: $\min\{1,[(9/4)(T-t)/5]^{4/3}\}$')
axs[1].set(xlabel=r'Original remaining time divided by $A$: $(T-t)/5$',ylabel=r'Original length factor $C_l$',title='Two exact rate endpoints give two different powers')
axs[1].legend(loc='upper left')
for ax in axs:ax.grid(alpha=.2)
fig.suptitle(r'Specified clock: $C_\omega(0)=5$, $\bar c_\omega=-2$, $\bar c_l=3$, $c_\omega(\tau)=-2+\frac{1}{4}\sin\tau$',fontsize=15)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-exact-clock.'+ext),dpi=160)
plt.close(fig)

def h(r):return np.exp(-1/((r-.5)*(6-r))) if .5<r<6 else 0.
Q=quad(h,.5,6,epsabs=2e-12,epsrel=2e-12)[0]
rr=np.linspace(0,7,281)
phi=np.array([1-quad(h,.5,min(max(r,.5),6),epsabs=2e-12,epsrel=2e-12)[0]/(2*Q) for r in rr])
damp=np.array([h(r)*(7/4)*r/(2*Q*p) for r,p in zip(rr,phi)])
Cstar=.5*np.exp(-.4)/(2*Q)
fig,axs=plt.subplots(1,2,figsize=(14,5.4),layout='constrained')
axs[0].plot(rr,phi,color=colors[0],lw=2.3,label=r'Constructed $\varphi_0$ (WT7–WT9)')
axs[0].axhline(1,color=colors[1],ls=':',label=r'Exact inner plateau $1$, $r\leq1/2$')
axs[0].axhline(.5,color=colors[2],ls=':',label=r'Exact outer plateau $1/2$, $r\geq6$')
axs[0].set(xlabel=r'Original radius $r=\sqrt{x^2+y^2}$',ylabel=r'$\varphi_0(r)$',ylim=(.44,1.07),title='Both original plateaus and the full transition')
axs[1].plot(rr,damp,color=colors[0],lw=2.3,label=r'Exact $-d_0=\dfrac{h(r)(7/4)r}{2Q\varphi_0(r)}$ along $x=y$')
axs[1].plot([1,3],[Cstar,Cstar],color=colors[1],ls='--',lw=2,label=r'Proved annular bound $C_*=\dfrac{(1/2)e^{-2/5}}{2Q}$')
axs[1].set(xlabel=r'Original radius $r$',ylabel=r'Positive local damping $-d_0$',title='Damping is proved on the actual annulus')
for ax in axs:
 ax.axvspan(1,3,alpha=.09,color=colors[0]);ax.axvline(1,color='#999999',lw=.7);ax.axvline(3,color='#999999',lw=.7);ax.grid(alpha=.2);ax.legend(loc='upper right')
fig.suptitle(r'Specified outgoing field $b=(x/2,3y)$; $R_1=1$, $R_2=3$, $Q=\int_{1/2}^{6}h(s)\,ds$ retained',fontsize=15)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-annular-weight.'+ext),dpi=160)
plt.close(fig)
meta=dict(scope='Original constructed clocks and weights, not the source approximate profile. Numerical samples illustrate complete analytic bounds; no interval-arithmetic certificate claimed.',proofs=['CHEN_HOU_EXACT_PHYSICAL_CLOCK_WORK_20261011.md QC1–QC21','CHEN_HOU_FULL_WEIGHTED_TRANSPORT_WORK_20261011.md WT7–WT18'],human_source='Chen and Hou arxiv:2210.07191v4; original TeX710–850 and1690–1799',clock=dict(A=5,bar_c_omega=-2,bar_c_l=3,delta='1/4',rate='-2+sin(tau)/4',tau=tau.tolist(),q=q.tolist(),C_omega=Cw.tolist(),C_l=Cl.tolist(),remaining_time=remaining.tolist()),weight=dict(R1=1,R2=3,a='1/2',d=6,c1='1/2',c2=3,Q_sample=Q,Cstar_sample=Cstar,r=rr.tolist(),phi0=phi.tolist(),minus_d0=damp.tolist()))
(R/'chen-hou-clock-weight-samples.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=['chen-hou-exact-clock.png','chen-hou-annular-weight.png'],Q_sample=Q,Cstar_sample=Cstar)))

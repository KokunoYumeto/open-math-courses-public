"""Reproducible physical examples for LC28–LC29 and EX9–EX15."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
T=2.;E=3.
def psi(t):
    w=(t-T/2)*(T-t)
    return np.exp(-1/w) if w>0 else 0.
den=quad(psi,T/2,T,epsabs=1e-13)[0]
def h(t):
    if t<=T/2:return 0.
    if t>=T:return 1.
    return quad(psi,T/2,t,epsabs=1e-13)[0]/den
ts=np.linspace(0,T,401);hs=np.array([h(t) for t in ts])
fig,ax=plt.subplots(figsize=(11,5.8),layout='constrained')
for z,color in [(0,'#1d4ed8'),(.25,'#0f766e'),(.5,'#b45309')]:
    ax.plot(ts,E*(1-z*hs),label=fr'$z={z:g}$',lw=2.7,color=color)
ax.axvspan(0,T/4,color='#dbeafe',alpha=.85)
ax.axvline(T/4,color='#64748b',ls='--')
ax.text(.25,1.7,'Every velocity agrees\nthrough t = 0.5',ha='center',fontsize=10)
ax.set(xlabel='Original time t',ylabel=r'Physical energy $\int_{\mathbb{T}_{2\pi}^3}|u_z|^2\,dx$',
       title='Same initial velocity; distinct prescribed energies',xlim=(0,T),ylim=(1.3,3.2))
ax.legend(loc='lower left',bbox_to_anchor=(.34,.02),ncol=3)
ax.grid(alpha=.2)
fig.text(.51,.015,'LC26–LC29 and EX14–EX15. T = 2, E* = 3; any fixed original viscosity ν > 0.\nNumerical samples of the exact smooth profiles; shaded interval is the proved velocity agreement.',
         ha='center',fontsize=10)
fig.get_layout_engine().set(rect=(0,.10,1,.90))
for ext in ['png','svg']:fig.savefig(OUT/f'original-prescribed-energy-continuum.{ext}',dpi=170)
plt.close(fig)
nu=.7;L=2*np.pi;alpha=2*np.pi/L;t0=.25
ts=np.linspace(t0,2.25,401);tau=ts-t0;c=nu*alpha**2
current=ts/nu*(1-np.exp(-c*tau))
remainder=-alpha**2*(1-(1+c*tau)*np.exp(-c*tau))/c**2
fig,ax=plt.subplots(figsize=(11,5.8),layout='constrained')
ax.plot(ts,current,lw=2,label='Current tensor term',color='#1d4ed8')
ax.plot(ts,remainder,lw=2,label='Time difference term',color='#b45309')
ax.plot(ts,current+remainder,lw=3,label='Exact derivative coefficient',color='#0f766e')
ax.axhline(0,color='#475569',lw=.8)
ax.set(xlabel='Original time t',ylabel=r'Coefficient of $(e_3\otimes(1,2,0))\cos(\alpha x_3)$',
       title='Both terms of the original heat derivative cancellation')
ax.legend();ax.grid(alpha=.2)
fig.text(.51,.015,'LC22 and EX9–EX13. L = 2π, α = 1, ν = 0.7, t₀ = 0.25; input F(t,x) = t M cos(x₃).\nExact formulas evaluated at the displayed times. This is the projected linear tensor receiver.',
         ha='center',fontsize=10)
fig.get_layout_engine().set(rect=(0,.10,1,.90))
for ext in ['png','svg']:fig.savefig(OUT/f'original-heat-derivative-cancellation.{ext}',dpi=170)
plt.close(fig)
print('Two physical figures generated from LC and exercise formulas.')

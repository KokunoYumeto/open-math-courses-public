"""Numerical samples of the exact MA6–MA8 formulas; proof is in the note."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
A,h,nu,r0,delta=20.,1.,1.,30.,.1
def c(r):
 r=np.asarray(r);z=np.zeros_like(r);inside=(r>r0)&(r<r0+delta)
 z[inside]=np.exp(-delta**2/((r[inside]-r0)*(r0+delta-r[inside])))
 return z
def G(r):return 8*np.pi/3*c(r)**2*r**4
grid=np.linspace(r0,r0+delta,20001);density=G(grid)/grid
primitive=np.concatenate(([0.],np.cumsum((density[1:]+density[:-1])/2*np.diff(grid))))
def F(r):return np.interp(r,grid,primitive,left=0.,right=primitive[-1])
a=np.linspace(28.9,30.2,15000)
volume=nu*(F(a+h)-F(a));surface=nu/2*(G(a)-G(a+h));flux=volume+surface
fig,axs=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
axs[0].plot(grid,G(grid),color='#136b62',linewidth=2)
axs[0].set(xlabel=r'Original radius $r$',ylabel=r'$G(r)=\int_{|x|=r}|z|^2\,dS$',title='Exact toroidal field; sampled radial density')
axs[0].axvspan(r0,r0+delta,alpha=.08,color='#136b62')
axs[1].plot(a,flux,color='#304d80',label=r'Full $Y_3(a)$',linewidth=1.7)
axs[1].plot(a,nu*G(a)/2,color='#c06435',linestyle='--',label=r'Lower bound $\nu G(a)/2$ on $30<a<30.1$')
axs[1].axvspan(r0,r0+delta,color='#136b62',alpha=.12)
axs[1].axhline(0,color='black',linewidth=.7)
axs[1].set(xlabel=r'Original inner radius $a$',ylabel='Signed heat flux',title='Both sphere terms retained; negative and positive peaks')
axs[1].legend(fontsize=9,loc='lower right')
for ax in axs:
 ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False)
fig.suptitle(r'$\nu=1,\ A=20,\ h=1,\ r_0=30,\ \delta=1/10$; outer spheres are disjoint from the field',fontsize=13)
fig.savefig(ROOT/'moving-annulus-flux.png',dpi=160);fig.savefig(ROOT/'moving-annulus-flux.svg')
print('Saved sampled exact heat-flux formulas; no numerical proof claimed.')

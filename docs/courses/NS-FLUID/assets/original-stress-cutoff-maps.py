"""Reproduce SC6–SC12 and EX9–EX11 with original coordinates and constants."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':12,'figure.facecolor':'white','savefig.facecolor':'white'})
def bump(z):
    z=np.asarray(z,dtype=float);out=np.zeros_like(z);ok=z>0;out[ok]=np.exp(-1/z[ok]);return out
def vartheta(t):return bump((t+.5)*(1-t))
def chi(y):
    y=np.asarray(y,dtype=float);out=np.zeros_like(y);ok=(y>.5)&(y<4)
    t=np.log(y[ok])/np.log(4);den=sum(vartheta(t-j)**2 for j in range(-3,4))
    out[ok]=vartheta(t)/np.sqrt(den);return out

yy=np.geomspace(1,64,1100);vals=[np.where(yy<=2,1,chi(yy))]+[chi(yy/4**i) for i in range(1,5)]
fig,ax=plt.subplots(2,1,figsize=(11,8),gridspec_kw={'height_ratios':[1,1]})
colors=['#125c85','#bc4d28','#477c38','#86569d','#9d751a']
for i,v in enumerate(vals):ax[0].plot(yy,v*v,label=rf'$\widetilde\chi_{i}(y)^2$',color=colors[i],lw=2)
ax[0].set(title='The specified squared partition: only adjacent cutoffs overlap',ylabel='Squared cutoff',ylim=(-.03,1.12))
ax[0].legend(ncol=5,loc='upper center',bbox_to_anchor=(.5,-.18),frameon=False)
F=sum(4**i*vals[i]**2 for i in range(1,5));bound=4/np.sqrt(3)*np.sqrt(yy*yy-1)
ax[1].plot(yy,F,lw=2.3,label=r'$F(y)=\sum_{i\geq1}4^i\widetilde\chi_i(y)^2$',color='#125c85')
ax[1].plot(yy,bound,'--',lw=1.8,label=r'Proved bound $4\sqrt{y^2-1}/\sqrt{3}$',color='#bc4d28')
ax[1].set(title='The full positive-index energy weight',ylabel='Actual weight',xlabel=r'Original cutoff argument $y=\sqrt{1+|S_\ell|^2/B^2}$')
ax[1].legend(loc='upper left',frameon=False)
for a in ax:
    a.set_xscale('log',base=4);a.set_xlim(1,64);a.set_xticks([1,2,4,8,16,32,64]);a.xaxis.set_major_formatter(FuncFormatter(lambda x,p:f'{x:g}'));a.grid(alpha=.2)
fig.suptitle('Exact cutoff geometry and its energy bound',fontsize=19)
fig.subplots_adjust(left=.09,right=.98,bottom=.17,top=.87,hspace=.70)
fig.text(.5,.015,'SC6–SC12 and EX3–EX5. Curves evaluate the explicitly constructed bump; the bound is proved in SC12.\nHuman comparison: Buckmaster–Vicol, arXiv:1709.10033v4, stress partition and energy amplitudes.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-stress-cutoff-partition.{ext}',dpi=170)
plt.close(fig)

mass=quad(lambda s:float(bump(1-s*s)),-1,1,epsabs=1e-13)[0]
def phi(s):return float(bump(1-s*s))/mass
ell=.2;ts=np.linspace(-.38,.5,400)
def integral(t,power):
    stop=min(1,t/ell)
    if stop<=-1:return 0.
    return quad(lambda s:max(t-ell*s,0)**power*phi(s),-1,stop,epsabs=1e-12)[0]
rho=np.maximum(ts,0);m=np.array([integral(t,1) for t in ts]);r0=np.array([integral(t,.5)**2 for t in ts])
c=quad(lambda s:np.sqrt(s)*phi(s),0,1,epsabs=1e-13)[0]**2
fig,ax=plt.subplots(1,2,figsize=(12,5.6),gridspec_kw={'width_ratios':[1.55,1]})
ax[0].plot(ts,rho,lw=2,label=r'$\rho(t)=t_+$',color='#333333')
ax[0].plot(ts,m,lw=1.8,label=r'$\rho*\varphi_\ell$',color='#bc4d28')
ax[0].plot(ts,r0,lw=2,label=r'$\rho_0=(\sqrt{\rho}*\varphi_\ell)^2$',color='#125c85')
ax[0].scatter([0],[ell*c],s=40,color='#125c85',zorder=5)
ax[0].set(title=r'Actual averaging window: $\ell=0.2$',xlabel='Original time t',ylabel='Energy coefficient',xlim=(-.38,.5),ylim=(-.01,.54))
ax[0].legend(loc='upper left',frameon=False,fontsize=11)
ells=np.linspace(0,.3,100);ax[1].plot(ells,c*ells,color='#125c85',lw=2)
ax[1].set(title='The exact first-order zero loss',xlabel=r'Original time scale $\ell$',ylabel=r'$\rho_0(0)-\rho(0)$',xlim=(0,.3),ylim=(0,c*.33))
ax[1].text(.025,c*.27,rf'$\rho_0(0)=c_\varphi\ell$'+'\n'+rf'$c_\varphi\approx {c:.6f}$',fontsize=13)
for a in ax:a.grid(alpha=.2)
fig.suptitle('Squaring a smoothed square root retains a visible zero loss',fontsize=17)
fig.subplots_adjust(left=.08,right=.98,bottom=.27,top=.80,wspace=.28)
fig.text(.5,.035,'EX9–EX11. The variance identity is exact. Curves use numerical quadrature of the specified unit-mass kernel\n'+r'$\varphi(s)=b(1-s^2)/\int_{-1}^1b(1-r^2)\,dr$'+'. The linear law is proved, and its displayed coefficient is numerical.\nHuman comparison: Buckmaster–Vicol, arXiv:1709.10033v4, square-root time smoothing.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-energy-square-root-smoothing.{ext}',dpi=170)
plt.close(fig)
(R/'stress-cutoff-figure-data.json').write_text(json.dumps({'kernel_mass_before_division':mass,'ell':ell,'c_phi_numerical':c,'partition_samples':len(yy),'time_samples':len(ts),'scope':'Numerical visualization of explicitly proved formulas; no numerical proof claim.'},indent=2)+'\n',encoding='utf8')

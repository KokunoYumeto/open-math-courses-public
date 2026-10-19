"""Exact models for AN01-U130, V12 and V32-V33; sampled plots are illustrations."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
a=.6
x=np.linspace(-.45,.45,801);q=x+a*x*x
u=np.linspace(-.24,.5,801);jac=1/np.sqrt(1+4*a*u)
p=.5;x1=np.linspace(-1,1,301);x2=np.linspace(-.4,1,281)
X1,X2=np.meshgrid(x1,x2);im=(X2-p)**2
fig,axs=plt.subplots(2,2,figsize=(12,8.2),layout='constrained')
ax=axs[0,0]
ax.plot(x,q,label=r'$q(x)=x+0.6x^2$',color='#17648f',lw=2)
ax.plot(x,x,'--',label=r'$x$',color='gray')
ax.scatter([0],[0],s=25,color='black')
ax.set(xlabel=r'$x$',ylabel=r'$u$',title='A. A nonlinear Gaussian coordinate')
ax.grid(alpha=.2);ax.legend(loc='upper left')
ax=axs[0,1]
ax.plot(u,jac,label=r"$v'(u)=(1+2.4u)^{-1/2}$",color='#17648f',lw=2)
ax.plot(u,1-2*a*u+6*a*a*u*u,'--',label='Taylor polynomial through degree 2',color='#b95422')
ax.axvline(0,color='gray',lw=.7);ax.axhline(1,color='gray',lw=.7)
ax.text(.48,.94,r'$P_1=6a^2=2.16$'+'\n'+r'$P_2=210a^4=27.216$',transform=ax.transAxes,va='top',fontsize=11)
ax.set(xlabel=r'$u$',ylabel='Inverse Jacobian',title='B. The Jacobian supplies the coefficients')
ax.grid(alpha=.2);ax.legend(loc='lower left',fontsize=9)
ax=axs[1,0]
implot=ax.pcolormesh(X1,X2,im,shading='auto',cmap='viridis',vmin=0,vmax=.81)
ax.axhline(p,color='white',lw=2,label=r'$\operatorname{Im}f=0:\ x_2=p$')
ax.axhline(0,color='#ffac4b',lw=2,ls='--',label=r'$f_{x_1}=0:\ x_2=0$')
ax.set(xlabel=r'$x_1$',ylabel=r'$x_2$',title=r'C. $f=x_1x_2+i(x_2-p)^2$, $p=1/2$')
ax.legend(loc='upper right',fontsize=9)
fig.colorbar(implot,ax=ax,label=r'$\operatorname{Im}f=(x_2-p)^2$',shrink=.8)
ax.text(.03,.05,r'$T=(i,0)$ is outside the real plane',color='white',transform=ax.transAxes,fontsize=10,bbox=dict(facecolor='black',alpha=.65,edgecolor='none',pad=4))
ax=axs[1,1];pp=np.linspace(-1,1,801)
ax.plot(pp,pp**2,color='#17648f',lw=3,label=r'$\operatorname{Im}f^0=p^2=|\operatorname{Im}T|^2/4$')
ax.plot(pp,np.zeros_like(pp),'--',color='#b95422',lw=2,label=r'$Y^tCY=0$')
ax.text(.32,.80,r'$Y=(2p,0),\quad CY=0$'+'\n'+r'$BY=(0,2p)$',transform=ax.transAxes,fontsize=12,bbox=dict(facecolor='white',alpha=.85,edgecolor='none',pad=4))
ax.set(xlabel=r'$p$',ylabel='Critical-value damping',title='D. The real mixed term gives positivity')
ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=9)
fig.suptitle('Finite Gaussian coefficients and a virtual critical graph',fontsize=16)
for ext in ['png','svg']:fig.savefig(R/('virtual-critical-coefficients.'+ext),dpi=170)
p=R/'virtual-critical-coefficients.svg';p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
print(dict(a=a,P1=6*a*a,P2=210*a**4,critical_point_at_half_p='(i,0)',phase_grid=[len(x2),len(x1)]))

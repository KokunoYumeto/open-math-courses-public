"""Original Dirichlet sections and proved norm envelope, with exact signed pair."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(16,6))
fig.subplots_adjust(left=.055,right=.975,bottom=.24,top=.78,wspace=.35)
fig.suptitle('Original intermittent factors: concentration and signed transport',fontsize=18,weight='bold')
y=np.linspace(-np.pi,np.pi,2401)
for r,col in [(2,'#246d96'),(8,'#c26d25')]:
    M=2*r+1
    dr=np.sum(np.cos(np.outer(np.arange(-r,r+1),y)),axis=0)
    axes[0].plot(y,np.sqrt(M)*dr,label=f'r={r}, M={M}',color=col,lw=1.25)
axes[0].set_title('Exact section of the full 3D kernel',fontsize=12)
axes[0].set_xlabel(r'Original argument $y$ in $D_r(y,0,0)$')
axes[0].set_ylabel(r'$D_r(y,0,0)=\sqrt{2r+1}\sum_{j=-r}^r\cos(jy)$')
axes[0].set_xticks([-np.pi,0,np.pi],labels=[r'$-\pi$','0',r'$\pi$'])
axes[0].legend(fontsize=10);axes[0].grid(alpha=.2)
r=np.unique(np.rint(np.geomspace(1,10**6,1200)).astype(int));M=2*r+1;L=2*np.pi
bound=L**1.5*M.astype(float)**(-1.5)*(1+np.log(M))**3
axes[1].loglog(r,bound,color='#26826e',lw=2)
axes[1].set_title(r'Proved upper bound; actual $L=2\pi$',fontsize=12)
axes[1].set_xlabel('Original integer r')
axes[1].set_ylabel(r'$L^{3/2}(2r+1)^{-3/2}[1+\log(2r+1)]^3$')
axes[1].grid(alpha=.2,which='both')
axes[1].text(.5,.04,r'Upper bound for $\|\eta_\xi\|_1/\|\eta_\xi\|_2$',ha='center',transform=axes[1].transAxes,fontsize=10)
axes[2].axis('off')
axes[2].set_title('Both orientations give the same pair',fontsize=12)
axes[2].text(.5,.80,r'$\zeta=\xi,\quad\varepsilon_\zeta=1$',ha='center',fontsize=17)
axes[2].text(.5,.61,r'$\zeta=-\xi,\quad\varepsilon_\zeta=-1$',ha='center',fontsize=17)
axes[2].text(.5,.38,r'$\varepsilon_\zeta\zeta=\xi$  in both cases',ha='center',fontsize=15,color='#246d96')
axes[2].text(.5,.15,r'$\eta_{-\xi}=\eta_\xi$',ha='center',fontsize=19)
fig.text(.5,.12,r'Exact pair divergence: $\nabla\eta_\zeta^2-(\varepsilon_\zeta\zeta/\mu)\,\partial_t\eta_\zeta^2$.  The original volume and temporal factor remain explicit.',ha='center',fontsize=13)
fig.text(.5,.04,'Proof: IB1–IB6, IB13, IB24. Human source: Buckmaster–Vicol, arXiv:1709.10033v4, original author source 474–655.',ha='center',fontsize=11)
fig.savefig(out/'original-intermittent-factors.png',dpi=150)
fig.savefig(out/'original-intermittent-factors.svg')

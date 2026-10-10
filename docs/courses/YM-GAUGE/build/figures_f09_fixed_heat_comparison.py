from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
E=Path(__file__).resolve().parent.parent/'figures'
E.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-F09-fixed_heat_comparison'
fig,ax=plt.subplots(figsize=(14,9),dpi=180)
fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc');ax.set_xlim(0,14);ax.set_ylim(0,9);ax.axis('off')
def box(x,y,w,h,title,body,color):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',fc=color,ec='#475569',lw=1.1)
    ax.add_patch(p);ax.text(x+w/2,y+h-.22,title,ha='center',va='top',fontsize=12,fontweight='bold',color='#0f172a')
    ax.text(x+w/2,y+h/2-.11,body,ha='center',va='center',fontsize=10.4,linespacing=1.45,color='#0f172a')
def arrow(a,b,label,offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,color='#334155',lw=1.4))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',fontsize=9.5,color='#334155',bbox={'fc':'#f8fafc','ec':'none','pad':2})
ax.text(7,8.62,'The prescribed heat endpoint S is retained',ha='center',fontsize=19,fontweight='bold',color='#0f172a')
ax.text(7,8.22,'A diagram of proved maps for two actual regular connections; every arrow has a proof locator.',ha='center',fontsize=10.5,color='#475569')
box(.45,5.65,3.9,1.8,'Original physical curves',r'$A_t^0=A_t^{0\prime}=0$'+'\n'+r'$\rho_A=\sup_I\|\partial\delta A^0\|_2$'+'\n'+r'$\rho_E=\sup_I\|\delta E^0\|_2$','#e0f2fe')
box(5.0,5.65,3.9,1.8,'Auxiliary endpoint sigma',r'$\sigma=\min(S,S_{R_a})>0$'+'\n'+r'$a_s^{[\sigma]}=0,\quad a_t^{[\sigma]}(\sigma)=0$'+'\n'+'FI.24–FI.27: starting jets from both inputs','#dbeafe')
box(9.65,5.65,3.9,1.8,'Original target on [0,S]',r'$a_s^{[S]}=0,\quad a_t^{[S]}(S)=0$'+'\n'+'FI.35: individual coefficients'+'\n'+'FI.41–FI.42: all difference receivers','#dcfce7')
box(3.7,2.9,6.6,1.55,'Intervening heat estimate on [sigma,S]',r'$\mathcal{Y}_5^2=\|\partial\delta a\|_{H_\ell^5}^2+\ell^2\|\delta G\|_{H_\ell^5}^2+c^{-2}\|\delta E\|_{H_\ell^5}^2$'+'\n'+r'$\mathcal{Y}_5(s)\leq\mathcal{Y}_5(\sigma)\exp\!\int_\sigma^s\Lambda_5(r)\,dr$'+'\n'+'FI.29–FI.32: every original coefficient difference','#fef3c7')
box(3.7,.6,6.6,1.5,'Physical-time transition with its actual anchor',r'$R_t=R\theta,\quad\theta=\int_\sigma^S W^{[\sigma]}(r)\,dr$'+'\n'+r'$R(t_*)=V_0(t_*,S)^{-1}V_0(t_*,\sigma)$'+'\n'+'FI.36–FI.39: tension difference and both anchor jets','#fae8ff')
arrow((4.48,6.55),(4.87,6.55),'FI.2–FI.27',(0,.44))
arrow((7,5.5),(7,4.6),'FI.26–FI.27',(.98,0))
arrow((7,2.75),(7,2.24),'FI.36–FI.37',(1.04,0))
arrow((10.43,1.45),(11.65,5.5),'FI.38–FI.42',(.72,0))
ax.text(1.96,3.8,'No replacement of S\nNo new high-order\ndifference datum',ha='center',va='center',fontsize=10.5,color='#334155',linespacing=1.6)
ax.text(7,.13,'The remaining nonlinear task is to control the physical-curve inputs by their single-time initial differences.',ha='center',fontsize=10,color='#475569')
fig.savefig(E/'f09-fixed-heat-comparison.png',bbox_inches='tight')
fig.savefig(E/'f09-fixed-heat-comparison.svg',bbox_inches='tight',metadata={'Date':None})
plt.close(fig)

def build():
    return None

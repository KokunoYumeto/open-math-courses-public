from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
E=Path(__file__).resolve().parent.parent/'figures'
E.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-F09-spatial_tension_difference'
fig,ax=plt.subplots(figsize=(15,11),dpi=180)
fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc');ax.set_xlim(0,15);ax.set_ylim(0,11);ax.axis('off')
def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',fc=color,ec='#475569',lw=1.1))
    ax.text(x+w/2,y+h-.18,title,ha='center',va='top',fontsize=12,fontweight='bold',color='#0f172a')
    ax.text(x+w/2,y+h/2-.12,body,ha='center',va='center',fontsize=10.5,linespacing=1.55,color='#0f172a')
def arrow(p,q,label,dx=0,dy=0):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=15,color='#334155',lw=1.3))
    ax.text((p[0]+q[0])/2+dx,(p[1]+q[1])/2+dy,label,ha='center',va='center',fontsize=9.2,color='#334155',bbox={'fc':'#f8fafc','ec':'none','pad':2})
ax.text(7.5,10.65,'The complete spatial tension difference',ha='center',fontsize=20,fontweight='bold',color='#0f172a')
ax.text(7.5,10.22,r'Two actual connections on $I\times\mathbb{R}^3\times[0,S]$; original $c$, full tuples and heat measure $ds/s$',ha='center',fontsize=11,color='#475569')
box(.45,7.75,6.45,1.7,'Constructed coefficient differences',r'$\eta=a-a^{\prime},\quad B=F-F^{\prime}$'+'\n'+r'$s^{j/2+1/4}\|\partial^{(j)}\eta\|_\infty\leq\Delta U_j\quad(0\leq j\leq4)$'+'\n'+'TDI.7–TDI.10: actual physical-curve inputs; unchanged S','#dbeafe')
box(8.05,7.75,6.45,1.7,'Paired electric heat smoothing',r'$u=E-E^{\prime},\quad\lambda_Q=\delta b+\delta c_{Q-1}$'+'\n'+r'$s^{j/2+1/4}\partial^{(j)}u\ \in\ L^p(ds/s;L^4_{t,x})$'+'\n'+'TDI.12–TDI.17: p = 2, infinity; Q = 4','#e0f2fe')
box(4.0,4.85,7.0,1.9,'Spatial tension: exact zero heat datum',r'$z_i=w_i-w_i^{\prime},\quad w_i=c^{-2}D_tE_i-G_i$'+'\n'+r'$(\partial_s-D^jD_j)z_i=2[F_{ij},z_j]+H_i+\delta Q_i$'+'\n'+r'$z(0)=0,\quad H=D^j[\eta_j,w^{\prime}]+[\eta^j,D_j^{\prime}w^{\prime}]+2[B,w^{\prime}]$'+'\n'+'TDI.5–TDI.6; TDI.18–TDI.22: energy and derivative recurrence','#fef3c7')
box(.45,1.75,6.45,1.95,'All six low-order wave receivers',r'$\|s^{q/2+1}\partial^{(q)}\delta\mathscr{T}\|_{L^p_sL^2_{t,x}}\leq\Theta_q^{\delta,p}$'+'\n'+r'$q=0,1,2,\quad p=2,\infty$'+'\n'+r'Wave contribution: $2c|I|^{1/2}\Theta_q^{\delta,p}$'+'\n'+'TDI.23–TDI.32: full-tuple constants 1, 6, 4, 4','#dcfce7')
box(8.05,1.75,6.45,1.95,'Physical-time spatial receiver',r'$\int_0^S\nabla\mathrm{div}\,z=\mathbf{P}_{\mathrm{cf}}(z(S)-\int_0^S N_z)$'+'\n'+r'$\int_0^S\|N_z\|_2\,ds\leq\mathcal{L}_N^\delta$'+'\n'+r'$c^2(A_0^\delta+\mathcal{L}_N^\delta+\mathcal{L}_{aw}^\delta)$'+'\n'+'TDI.33–TDI.35: temporal product retained separately','#fae8ff')
arrow((6.1,7.62),(5.6,6.89),'Full coefficient terms',-.6,0)
arrow((9.0,7.62),(9.4,6.89),r'$\delta Q$; every electric product',.9,0)
arrow((6.0,4.72),(4.5,3.84),'TDI.20 → TDI.25',-.45,0)
arrow((9.0,4.72),(10.5,3.84),'TDI.33 → TDI.35',.45,0)
ax.text(7.5,1.0,r'Gauge anchors retained: $a_t(S)=a_t^{\prime}(S)=0$, $R(t_*)=V_0(t_*,S)^{-1}V_0(t_*,\sigma)$',ha='center',fontsize=10.5,color='#334155')
ax.text(7.5,.52,'Every displayed bound vanishes with the actual differences. These maps do not assume nonlinear initial-data stability.',ha='center',fontsize=10.4,color='#475569')
ax.text(7.5,.13,'Proof map, not a sampled solution. Human source: Sung-Jin Oh, arXiv:1210.1558v2, original author TeX; exact reading ledger retained.',ha='center',fontsize=9,color='#64748b')
fig.savefig(E/'f09-spatial-tension-difference.png',bbox_inches='tight')
fig.savefig(E/'f09-spatial-tension-difference.svg',bbox_inches='tight',metadata={'Date':None})
plt.close(fig)


def build():
    return None

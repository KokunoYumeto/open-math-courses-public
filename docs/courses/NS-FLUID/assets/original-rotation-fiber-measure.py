"""Exact geometric maps and full measure factors, RF1–RF24."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(15,9),facecolor='white');ax.set(xlim=(0,15),ylim=(0,9));ax.axis('off')
def box(x,y,w,h,color='#176b75'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor='#f2f7f8',edgecolor=color,lw=1.8))
ax.text(7.5,8.65,'Every original closing rotation and every measure factor',ha='center',fontsize=21)
box(.35,6.75,4.45,1.15);box(9.0,6.75,5.55,1.15)
ax.text(2.58,7.47,r'$SO(3)\times(\mathbb{R}/2\pi\mathbb{Z})^3$',ha='center',fontsize=18)
ax.text(2.58,6.98,'One common rotation and three full spin angles',ha='center',fontsize=10)
ax.text(11.75,7.48,r'$\Sigma_\xi=G_\xi^{-1}(0)\subset SO(3)^3$',ha='center',fontsize=18)
ax.text(11.75,6.98,'The entire six-dimensional rotation fiber',ha='center',fontsize=11)
ax.add_patch(FancyArrowPatch((4.98,7.3),(8.77,7.3),arrowstyle='<->',mutation_scale=20,lw=2,color='#bd611e'))
ax.text(6.86,7.65,r'$\Phi_\xi\quad$ smooth bijection',ha='center',fontsize=14)
ax.text(7.5,6.14,r'$\Phi_\xi(S,\theta)=(S R_{\eta_1}^{\theta_1}Q_1,\ S R_{\eta_2}^{\theta_2}Q_2,\ S R_{\eta_3}^{\theta_3}Q_3)$',ha='center',fontsize=18)
ax.text(7.5,5.63,r'$Q_j\xi_j=\eta_j,\quad |\eta_j|=|\xi_j|=r_j,\quad\eta_1+\eta_2+\eta_3=0,\quad H=|\eta_1\times\eta_2|>0$',ha='center',fontsize=14)
box(.35,3.54,14.2,1.62)
ax.text(7.5,4.81,'Both complete Jacobians, with the original radii retained',ha='center',fontsize=15)
ax.text(7.5,4.26,r'$\det K_r=3H^2(r_1^2+r_2^2+r_3^2),\qquad \det K_0=\frac{3H^2(r_1^2+r_2^2+r_3^2)}{r_1^2r_2^2r_3^2}$',ha='center',fontsize=18)
ax.text(7.5,3.77,r'$\Phi_\xi^*d\sigma=\sqrt{\det K_0}\,dV(S)\,d\theta,\qquad dR=dV(R)/(8\pi^2)$',ha='center',fontsize=17)
ax.text(7.5,3.00,'Under this exact parametrization, the delta measure becomes',ha='center',fontsize=15)
ax.text(7.5,2.30,r'$\delta(G_\xi(R))\,dR_1\,dR_2\,dR_3\quad\longleftrightarrow\quad\frac{dS\,d\theta}{(8\pi^2)^2r_1r_2r_3}$',ha='center',fontsize=23)
ax.text(7.5,1.58,r'$G_\xi(R)=R_1\xi_1+R_2\xi_2+R_3\xi_3,\qquad dS\ {\rm probability\ Haar},\quad \int_{[0,2\pi]^3}d\theta=(2\pi)^3$',ha='center',fontsize=14)
ax.text(7.5,.83,'RF1–RF24 prove the explicit closing maps, global fiber, coarea limit and complete tensor recovery.',ha='center',fontsize=11)
ax.text(7.5,.45,'Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex640–752. Full metric conventions are in RF10–RF15.',ha='center',fontsize=10)
ax.text(7.5,.12,'The delta notation is the proved approximate-identity limit RF16. No angle, radius or group-volume factor is omitted.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,bottom=.02,top=.99)
for ext in ['png','svg']:fig.savefig(P/f'original-rotation-fiber-measure.{ext}',dpi=160,facecolor='white')

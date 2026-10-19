"""Exact shear-realization mechanism; schematic layout, no sampled data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(18,9));fig.patch.set_facecolor('#fafbf9')
ax.set(xlim=(0,18),ylim=(0,9));ax.axis('off')
ax.text(.35,8.55,'A finite shear modification completes the leading profile',fontsize=23,weight='bold',color='#16362f')
ax.text(.35,8.12,'Original Appendix C · V0–V7     Exact equations; schematic radial positions.',fontsize=12,color='#506459')
def box(x,y,w,h,title,rows,color='#e8f0eb'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.10',facecolor=color,edgecolor='#90a89c'))
 ax.text(x+.18,y+h-.27,title,fontsize=14,weight='bold',va='top',color='#16362f')
 ax.text(x+.18,y+h-.75,'\n'.join(rows),fontsize=12,va='top',linespacing=1.65,color='#223d34')
def arrow(x1,y,x2):
 ax.add_patch(FancyArrowPatch((x1,y),(x2,y),arrowstyle='-|>',mutation_scale=13,color='#577e6d',linewidth=1.5))
box(.35,4.8,3.9,2.85,'1. Admissible loop',[
 r'$2<v<\mathcal{U}(P_c(t),J_c(t))$',
 r'$d\varphi=\frac{a(1+t^2)}{2\pi v}\,d\theta^{\prime}$',
 r'$\int_0^1(a_L,-b_L)d\varphi=(a,-b_s)$',
 'Exact average; positive cone gaps', 'V1–V2'])
box(4.8,4.8,4.05,2.85,'2. Actual radial fields',[
 r'$E_N=E\exp(\mathcal{A}/N)$',r'$U_N=U+\mathcal{B}/N$',
 r'$\varphi=N\log X$',
 'Fields and moments: '+r'$O(N^{-1})$',
 'Shears follow the loop; V3'])
box(9.4,4.8,3.9,2.85,'3. Five exact equations',[
 'First reserved patch only',r'$U=0,\ E=KX^{-1/2-\lambda}$',
 '2 axial + 3 angular bumps',r'$B c+\mathcal{Q}(c,c)=-\Delta\mathbf{m}$',
 'Full quadratic map; V4'])
box(13.85,4.8,3.8,2.85,'4. Exact exterior',[
 r'$\widetilde{\mathbf{m}}=\mathbf{m}$',r'$\widetilde\Pi=\Pi$',
 r'$\widetilde Q_s=Q_s,\ \widetilde N_s=N_s$',
 'Heat field and outer edge retained', 'V4.6; G3'])
arrow(4.28,6.25,4.77);arrow(8.88,6.25,9.37);arrow(13.33,6.25,13.82)
box(.35,1.5,8.45,2.8,'Both endpoint directions and the same flat weight',[
 r'$n(X_a)\parallel(a,-b_s),\qquad n(X_b)=(1,0)$',
 r'$y_a=\log(X/X_a),\quad y_b=\log(X_b/X)$',
 r'$\zeta=\exp(-t_1^2/y_a^2-4/y_b^2)$',
 r'$|\mathcal{T}_0|\geq c\zeta,\quad |\partial^\alpha\mathcal{T}_0|\leq C_\alpha\zeta\delta^{-m_\alpha}$',
 'Exact inner and outer factors: V5–V6'])
box(9.2,1.5,8.45,2.8,'Theorem 4.6: all six leading-profile properties',[
 'Smooth axis and a common analytic parameter neighborhood',
 'Exact radial pressure and leading stress identities',
 'Admissible interior and uniform endpoint direction margins',
 'Flat stress bounds; exact heat exterior and total moments',
 'The two later correction patches remain available; V7'],color='#e9eef5')
ax.text(.35,.91,'One finite N is chosen after all profile parameters. The base is constructed in Z0–Z8; the full blowup theorem remains unverified.',fontsize=12,color='#5d4630')
ax.text(.35,.4,'Source: OpenAI, Finite Time Blowup for Navier–Stokes, pp. 31–35, 38, 158–165. Proof: shear-realization-audit.md, V0–V7.',fontsize=10,color='#526058')
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(root/'shear-realization.png',dpi=120,facecolor=fig.get_facecolor())
fig.savefig(root/'shear-realization.svg',facecolor=fig.get_facecolor())

"""Exact six-coordinate mechanism and integral bound; schematic, no samples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(18,8));fig.patch.set_facecolor('#fafbf9');ax.set(xlim=(0,18),ylim=(0,8));ax.axis('off')
ax.text(.35,7.6,'Why higher-order axis corrections keep one radial interval',fontsize=23,weight='bold',color='#16362f')
ax.text(.35,7.18,'Original Lemma 5.1 · D0–D6     Exact coordinate spaces, matrix support and estimates.',fontsize=12,color='#506459')
def box(x,y,w,h,title,rows,color='#e8f0eb'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.10',facecolor=color,edgecolor='#90a89c'))
 ax.text(x+.18,y+h-.26,title,fontsize=14,weight='bold',va='top',color='#16362f')
 ax.text(x+.18,y+h-.73,'\n'.join(rows),fontsize=13,va='top',linespacing=1.6,color='#223d34')
box(.35,4.0,5.45,2.65,'The original six coordinates',[
 r'$W_n=(\phi_n,U_n,K_n,\Pi_n,\partial_\xi\phi_n,\partial_\xi U_n)$',
 r'$K_n=\mathcal{A}_XU_n-U_n,\quad X=\xi^2$',
 r'$W_n^\prime+\xi^{-1}C_d W_n=A_0W_n+A_1\partial_\eta W_n+f_n$',
 r'$C_d=\mathrm{diag}(0,0,2,0,3,1)$'])
box(6.25,4.0,5.45,2.65,'The derivative matrix has only one direction',[
 r'$E_4=\mathrm{span}(e_1,e_2,e_3,e_4)$',r'$E_2=\mathrm{span}(e_5,e_6)$',
 r'$A_1:E_4\to E_2,\qquad A_1|_{E_2}=0$',
 r'$A_1(\xi)D_0\partial_\eta^j A_1(s)=0$'])
box(12.15,4.0,5.45,2.65,'A nonzero word has separated derivatives',[
 r'$A_1\partial_\eta\quad A_1\partial_\eta\quad =0$',
 r'$p_k\leq\lceil k/2\rceil$',
 'Diagonal radial kernels preserve both spaces.',
 'Variable coefficients retain this identity.'])
box(.35,1.15,8.45,2.4,'The exact radial inverse and convergent series',[
 r'$(Gg)_i(\xi)=\int_0^\xi(s/\xi)^{c_i}g_i(s)\,ds$',
 r'$\mathcal{K}=G(A_0+A_1\partial_\eta)$',
 r'$W_n=\sum_{k\geq0}\mathcal{K}^kGf_n$'],color='#e9eef5')
box(9.25,1.15,8.35,2.4,'The estimate permits every fixed interval length a',[
 r'$\|\mathcal{K}^kGf_n\|\leq\frac{C_n^{k+1}a^{k+1}}{(k+1)!}\max(1,p_k/\Delta)^{p_k}$',
 r'$\Delta=\rho-\rho^\prime>0,\qquad p_k=\lceil k/2\rceil$',
 'The kth root tends to zero; a need not shrink.'],color='#e9eef5')
ax.text(.35,.72,'D5 proves smoothness in X, parity and exact recovery of the radial average. D6 constructs the actual first correction.',fontsize=12,color='#16362f')
ax.text(.35,.32,'Source: OpenAI, Finite Time Blowup for Navier–Stokes, pp. 45–49. Proof: higher-axis-coefficients-audit.md. The global extension is proved in Y0–Y7; the base in Z0–Z8.',fontsize=10,color='#5d4630')
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(p/'higher-axis-coefficients.png',dpi=120,facecolor=fig.get_facecolor())
fig.savefig(p/'higher-axis-coefficients.svg',facecolor=fig.get_facecolor())

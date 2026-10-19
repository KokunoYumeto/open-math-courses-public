"""Exact base-field cutoff and residual mechanism, proof Z0–Z8."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(18,10),facecolor='#fafcfb');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,18);ax.set_ylim(0,10);ax.axis('off')
ink='#193b35';muted='#557168'
ax.text(.35,9.65,'From the actual coefficients to the base field',fontsize=23,color=ink,weight='bold')
ax.text(.35,9.18,'Propositions 5.3 and 5.5 · Z0–Z8    Exact cutoffs, preserved divergence and the complete residual.',fontsize=12,color=muted)
def box(x,y,w,h,title,lines,face='#eaf2ee'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=.08',facecolor=face,edgecolor='#91aba0'))
 ax.text(x+.2,y+h-.42,title,fontsize=15,color=ink,weight='bold')
 for j,s in enumerate(lines):ax.text(x+.2,y+h-.93-j*.43,s,fontsize=13,color=ink)
box(.35,6.1,8.45,2.65,'Cut the potential, then take its full curl',[
 r'$S_n=q^{1-A+2nh}F_n,\qquad \mathcal{A}_n=(S_n/r)e_\theta$',
 r'$u_n^{\rm cut}=\operatorname{curl}(\chi(c_nq)\mathcal{A}_n)+\chi(c_nq)u_{\theta,n}e_\theta$',
 r'$ru_{r,n}^{\rm cut}=q^{2nh}[\chi(c_nq)V_n-\frac{2\eta}{L}(c_nq)\chi^{\prime}(c_nq)F_n]$',
 r'Both radial terms are required; $\operatorname{div}u_n^{\rm cut}=0$.'])
box(9.15,6.1,8.45,2.65,'One cutoff sequence controls every fixed derivative',[
 r'$c_n=1+\left\lceil\max\{2c_{n-1},2,(2^nM_n)^{1/(nh)}\}\right\rceil$',
 r'$M_n$: finite norms of the actual fields and both stresses.',
 r'$|W_n(c_n)|_m\leq2^{-n}q^{nh-\ell_m^{\prime}}\quad(m\leq n)$',
 r'$\ell_m^{\prime}=2A+m+1,\qquad c_n\geq2c_{n-1}$'])
box(.35,3.05,8.45,2.65,'Compare with one sufficiently long finite sum',[
 r'$|\mathcal{F}_{\rm slow}(\mathcal{U}^{[J]})|_m\leq C_{J,m}q^{2h(J+1)-(2A+1/2+m)}$',
 r'$|\mathcal{U}_B-\mathcal{U}^{[J]}|_m\leq2^{-J}q^{h(J+1)-\ell_m^{\prime}}$',
 r'The loss is independent of $J$; all cutoff-curl terms remain.',
 r'For each derivative and decay order, choose one finite $J$.'],face='#eaf0f8')
box(9.15,3.05,8.45,2.65,'Keep the whole nonlinear and stress difference',[
 r'$\partial_te-\Delta e+\nabla\pi+(v\!\cdot\!\nabla)e+(e\!\cdot\!\nabla)v+(e\!\cdot\!\nabla)e$',
 r'$\quad +(\partial_r+2/r)\tau_\theta e_\theta+(\partial_r+1/r)\tau_ze_z$',
 r'$\mathcal{R}(u_B,p_B)=-\operatorname{div}_{\rm tan}T_{\rm phys}+\mathcal{E}_B$',
 r'$|\mathcal{E}_B|_m\leq C_{m,M}q^M$ for every $m,M$'],face='#eaf0f8')
ax.text(.45,2.55,'The resulting fields retain the original data',fontsize=16,color=ink,weight='bold')
ax.text(.45,2.08,r'$u_B=u^{(0)},\ p_B=p^{(0)}$ for $X\geq X_+$; exact leading velocity on $\mathcal{I}_{\rm mean}$.',fontsize=13,color=ink)
ax.text(.45,1.63,r'$|\mathscr{D}^{I}(q^{A+1/2}T_{\rm phys}-\mathcal{T}_0)|\leq C_Iq^{2h}\zeta\delta^{-N_I}$, including the full first-order heat term.',fontsize=13,color=ink)
ax.text(.45,1.18,'All original coefficient powers, endpoint derivatives and viscosity factors are retained in Z6–Z8.',fontsize=13,color=ink)
ax.text(.4,.65,'Proof: base-field-realization-audit.md, Z0–Z8. The full blowup theorem remains unverified.',fontsize=11,color=muted)
ax.text(.4,.25,'Source: OpenAI, Finite Time Blowup for Navier–Stokes, pp. 55–62. Exact operator schematic; no numerical data.',fontsize=10,color=muted)
fig.savefig(out/'base-field-realization.png',dpi=140,facecolor=fig.get_facecolor())
fig.savefig(out/'base-field-realization.svg',facecolor=fig.get_facecolor())
plt.close(fig)

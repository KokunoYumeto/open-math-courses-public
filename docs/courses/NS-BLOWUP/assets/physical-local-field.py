"""Exact physical local-field construction, PL0–PL7 and LC0–LC8. CC0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(14,17),dpi=100)
fig.patch.set_facecolor('#f6f8fb');ax.set_facecolor('#f6f8fb');ax.set_xlim(0,14);ax.set_ylim(0,17);ax.axis('off')
ink='#142c44';blue='#dcebf8';green='#e0eee6';orange='#f7ebd9'
ax.text(7,16.55,'The actual local field',ha='center',fontsize=28,color=ink,weight='bold')
ax.text(7,16.12,'Complete potentials, one cutoff sequence, and all four local conclusions',ha='center',fontsize=15,color=ink)
def box(y,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((.4,y),13.2,h,boxstyle='round,pad=0.12,rounding_size=0.15',facecolor=color,edgecolor='#8aa2b5'))
    ax.text(.72,y+h-.35,title,fontsize=17,color=ink,weight='bold')
    for k,line in enumerate(lines):ax.text(.75,y+h-.79-k*.4,line,fontsize=15,color=ink)
def arrow(y):ax.annotate('',xy=(7,y-.32),xytext=(7,y+.08),arrowprops=dict(arrowstyle='->',color='#335c7b',lw=2))
box(13.96,1.7,'Actual finite states and their increments  |  LC0–LC3, PL0',[
    r'$Z_j=(A_j,B_j^{\rm vec},p_j),\quad \Delta u_j=\operatorname{curl}A_j+B_j^{\rm vec}$',
    r'$B_j^{\rm vec}=b_j e_\theta,\quad \partial_\theta b_j=0,\quad p_j=p^{[j]}-p^{[j-1]}$',
    'Same base, original phases and fixed inverses on one positive domain.'],blue)
arrow(13.83)
box(11.66,1.85,'Physical derivatives have a stage-independent loss  |  PL1–PL3',[
    r'$g_j=hj/10,\quad \ell_m=2A+(m+1)(1+3h/2)$',
    r'$|Z_j|_m+|\Delta u_j|_m\leq C_{j,m}q^{g_j-\ell_m}(1+|\log q|)^{P_{j,m}}$',
    'Carrier frequency, auxiliary-coordinate derivatives and frame terms are included.'],green)
arrow(11.53)
box(8.96,2.25,'One actual cutoff sum  |  PL4, LC4',[
    r'$a_{j+1}\geq2a_j,\quad \mathcal{A}=\mathcal{A}_0+\sum_j\chi(a_jq)A_j$',
    r'$u=\operatorname{curl}\mathcal{A}+\mathcal{B} e_\theta,\quad p=p^{[0]}+\sum_j\chi(a_jq)p_j$',
    r'$\operatorname{curl}(\chi(a_jq)A_j)=\chi(a_jq)\operatorname{curl}A_j$',
    r'$\qquad\qquad+\ a_j\chi^\prime(a_jq)\nabla q\times A_j$'],green)
arrow(8.83)
box(6.46,2.05,'The full nonlinear residual  |  PL5, LC4',[
    r'$u=v+e,\quad p=p^{[J]}+\pi$',
    r'$\mathscr{R}_\nu(u,p)-\mathscr{R}_\nu(v,p^{[J]})=\partial_t e-\nu\Delta e+\nabla\pi$',
    r'$\qquad+(v\cdot\nabla)e+(e\cdot\nabla)v+(e\cdot\nabla)e$',
    'For each derivative order and decay power, compare with one finite stage.'],orange)
box(3.27,2.68,'All four properties of the local theorem  |  LC4–LC7',[
    '1. Exact divergence zero; smooth Cartesian potentials at the axis.',
    '2. Compatible one-sided derivatives away from q = 0.',
    '3. Every residual derivative decays to every order; exact exterior heat field.',
    r'4. $u_{\theta,\nu}(\sqrt{2\nu X_{\rm in}\tau},0,0,1-\tau)$',
    r'$\qquad=\sqrt{\nu}\,\tau^{-A}(e_0+O(\tau^{2h})),\quad e_0>0.$'],blue)
box(.75,2.0,'Original physical viscosity and preserved regions  |  PL3, LC7',[
    r'$y=x_\nu/\sqrt{\nu},\quad u_\nu=\sqrt{\nu} u(y,t),\quad p_\nu=\nu p(y,t),\quad\mathcal{A}_\nu=\nu\mathcal{A}(y,t)$',
    r'$q_\nu-(z_\nu^2/\nu)q_\nu^{2h}=1-t,\quad X_\nu=r_\nu^2/(2\nu q_\nu)$',
    r'Corrections: $X_a\leq X_\nu\leq X_b$. Inner and exterior fields are unchanged.'],green)
ax.text(7,.2,'Source: OpenAI, Theorem 3.1, Lemma 9.8, Proposition 9.9. Proofs: PL0–PL7 and LC0–LC8.',ha='center',fontsize=11,color=ink)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(P/'physical-local-field.svg');fig.savefig(P/'physical-local-field.png');plt.close(fig)
p=P/'physical-local-field.svg';p.write_text(re.sub(r'width="1008pt" height="1224pt"','width="1400" height="1700"',p.read_text(encoding='utf8')),encoding='utf8')

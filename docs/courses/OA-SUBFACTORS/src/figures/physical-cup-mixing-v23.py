"""Reproduce Figure PCM. Independently authored; CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'svg.fonttype':'none','mathtext.fontset':'dejavusans'})
fig, ax = plt.subplots(figsize=(14,9))
fig.patch.set_facecolor('#f5f8fa')
ax.set(xlim=(0,14), ylim=(0,9))
ax.axis('off')

def box(x,y,w,h,title,text,color='#e5eef7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',
                 facecolor=color,edgecolor='#526779',linewidth=1.3))
    ax.text(x+.16,y+h-.25,title,fontsize=12.5,fontweight='bold',va='top',color='#18334a')
    ax.text(x+.16,y+h-.7,text,fontsize=11,va='top',linespacing=1.45,color='#18334a')

def arrow(x1,y1,x2,y2,label=None):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',
                 mutation_scale=17,linewidth=1.5,color='#415e73'))
    if label:
        ax.text((x1+x2)/2,(y1+y2)/2+.08,label,ha='center',va='bottom',fontsize=11,
                bbox={'facecolor':'#f5f8fa','edgecolor':'none','pad':2})

ax.text(.3,8.65,'Mixing actual marked local choices',fontsize=24,fontweight='bold',color='#123047')
ax.text(.3,8.18,'PCM.1-PCM.3: finite Jones origins, both inherited traces and fixed physical targets',
        fontsize=13,color='#415e73')

box(.4,5.45,3.6,2.25,'Two selected near-covers',
    r'$r_i=U_i g_i U_i^*,\quad s_j=V_j h_j V_j^*$'+'\n'+
    r'$U_i,V_j\in N_k;\quad g_i,h_j\in F_m^{N_k}$'+'\n'+
    'Individual ordinary tunnels.\nResidual traces: '+r'$\theta_A,\theta_B$')
box(5.1,5.45,3.8,2.25,'One actual finite cup split',
    r'$p\in\mathrm{Mat}_2\subset N_m,\quad\tau(p)=1/2$'+'\n'+
    r'$q=uc_\ell u^*\leq p,\quad \alpha=\tau(q)\to1/2$'+'\n'+
    r'$\widetilde S^L=uS^Lu^*,\quad u\in N_m$'+'\n'+
    'The old finite supports stay fixed.', '#e8f3ed')
arrow(4.12,6.6,4.94,6.6)

box(.4,2.48,5.8,2.15,'Transported physical splits',
    r'$\widehat r_i=U_i(g_iq)U_i^*$'+'\n'+
    r'$\widehat s_j=V_j(h_j(1-q))V_j^*$'+'\n'+
    r'$\|\widehat r_i\widehat s_j\|_2\leq\delta_i+\delta_j^\prime$'+'\n'+
    r'$\delta_i=\|U_iqU_i^*-q\|_2$'+': chosen arbitrarily small')
box(7.3,2.48,6.1,2.15,'Equal-trace orthogonal correction',
    r'$r_i^\prime=w_i\widehat r_iw_i^*,\quad s_j^\prime=w_j\widehat s_jw_j^*$'+'\n'+
    r'$w_t\in N_k,\quad\|w_t-1\|_2\leq2\|p_t^\prime-p_t\|_2$'+'\n'+
    'Each corrected cell retains its actual whole origin.\n'+
    r'$\theta_C=\alpha\theta_A+(1-\alpha)\theta_B$', '#e8f3ed')
arrow(6.37,3.58,7.13,3.58)
arrow(7.05,5.28,3.3,4.79, 'PCM.18')

box(10,5.45,3.4,2.25,'Two separate trace laws',
    r'$\tau(g_iq)=\alpha\tau(g_i)$'+'\n'+
    r'$\rho_J^L(g_iq)=\alpha\rho_m^L(g_i)$'+'\n'+
    r'$L=M,N,N_k$'+'\n'+
    'The two traces can be unequal.', '#fff0d9')
arrow(9.03,6.6,9.84,6.6)

ax.text(.52,1.73,'Exact normal profile, with the core comparison retained',
        fontsize=15,fontweight='bold',color='#18334a')
ax.text(.52,1.22,r'$(\operatorname{Ad}u)^{-1}H_C^L=\alpha H_A^L+(1-\alpha)H_B^L$',
        fontsize=21,color='#18334a')
ax.text(.52,.6,'All three commuting-square rows and every earlier cup are retained. '
        'The residual remains an actual corner block.',fontsize=12,color='#415e73')
ax.text(.52,.2,'Rectangle sizes are schematic. No small fractional loss or full residual certificate is asserted.',
        fontsize=11,color='#415e73')
fig.savefig(OUT/'physical-cup-mixing-v23.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(OUT/'physical-cup-mixing-v23.png',dpi=140,bbox_inches='tight',facecolor=fig.get_facecolor())

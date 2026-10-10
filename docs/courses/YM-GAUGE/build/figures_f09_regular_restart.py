"""Diagram of the proved first-translation to affine-restart map, RI.29-RI.37."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
HERE=Path(__file__).resolve().parent.parent/'figures'
HERE.mkdir(parents=True,exist_ok=True)
plt.rcParams['svg.hashsalt']='YM-GAUGE-F09-regular_restart'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(16,11),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,11);ax.axis('off')
ax.text(.7,10.45,'The first spatial-translation estimate reaches the original restart',
        fontsize=22,weight='bold',color='#15344e')
ax.text(.7,9.9,r'$V=(A-A_*,E,B),\qquad c>0,\quad\ell>0,\quad J=[t_*,t],\quad t<T$',
        fontsize=20,color='#34485b')
def box(y,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((.8,y),14.4,h,boxstyle='round,pad=.16,rounding_size=.12',
                              facecolor=color,edgecolor='#8ca6bc',linewidth=1.2))
    ax.text(1.08,y+h-.28,title,va='top',fontsize=18,weight='bold',color='#183850')
    for n,line in enumerate(lines):
        ax.text(1.08,y+h-.85-n*.43,line,va='top',fontsize=17,color='#132536')
def arrow(y0,y1):
    ax.add_patch(FancyArrowPatch((8,y0),(8,y1),arrowstyle='-|>',mutation_scale=19,
                                color='#5b7891',linewidth=2))
box(7.5,1.8,'RI.34–RI.37 · The exact translation input',[
 r'$Z_{\rm phys}=(\partial_xA,c^{-1}E),\qquad'
 r'\mathcal{T}(J)=\sup_{t\in J}\|\partial_xZ_{\rm phys}(t)\|_2$',
 r'$\mathcal{T}(J)\leq L_{\rm tr}(J)\|\partial_xZ_{\rm phys}(t_*)\|_2,'
 r'\qquad N_2(J)=\int_J\|\partial_x^{(2)}A\|_2\,dt\leq |J|\mathcal{T}(J)$'],
 '#fff0d7')
arrow(7.24,6.89)
box(4.95,1.8,'RI.29–RI.31 · The full mixed multiplier, with all three terms',[
 r'$K_{\rm mix}(A)=\|A\|_\infty+2C_S\|\partial_xA\|_3'
 r'+\ell^2b_\ell\|\partial_x^{(2)}A\|_2$',
 r'$\|Af\|_{H_\ell^2},\ \|fA\|_{H_\ell^2}\leq K_{\rm mix}(A)\|f\|_{H_\ell^2},'
 r'\qquad \|R_A V\|_{X_2}\leq12cK_{\rm mix}(A)\|V\|_{X_2}$'], '#e4f0fa')
arrow(4.7,4.34)
box(2.08,2.1,'RI.32–RI.33 · Actual finite bound in the original X2 norm',[
 r'$\|V(t)\|_{X_2}\leq\|V(t_*)\|_{X_2}\exp\!\left['
 r'(c/\ell)|J|+12c(C_MC_S+2C_S^{3/2})\sqrt{M_1|J|N_2(J)}\right.$',
 r'$\left.\hspace{1}+12c\ell^2b_\ell N_2(J)\right],'
 r'\qquad M_1\geq\sup_J\|\partial_xA\|_2$',
 r'Initial datum remains $(0,E_*,\mathscr{B}(A_*))$ with its full $H_\ell^2$ norms.'], '#e7f5ed')
arrow(1.83,1.49)
ax.text(.98,1.08,'RI.13–RI.16: strong endpoint → same-gauge restart → every finite derivative and constraint',
        fontsize=17,weight='bold',color='#173b50')
ax.text(.98,.48,'The map is proved. FC has not yet bounded the actual translation amplification uniformly at T.',
        fontsize=15,color='#775414')
fig.savefig(HERE/'f09-regular-restart.png',dpi=160)
fig.savefig(HERE/'f09-regular-restart.svg',metadata={'Date':None})
plt.close(fig)
print('Saved f09-regular-restart.png and .svg')

def build():
    return None

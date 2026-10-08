"""Original CC0 explanatory diagram for the relative P1 generation proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(14, 8.5))
fig.patch.set_facecolor('#fbfcff')
ax.set(xlim=(0, 14), ylim=(0, 8.5))
ax.axis('off')
blue, teal, orange = '#183b65', '#13786c', '#ac5424'
ax.text(7, 8.12, r'Relative $\mathbf{P}^1$ generation: redundant lists, then exact gluing',
        ha='center', fontsize=21, color=blue)
ax.text(7, 7.65, r'$A$ is arbitrary coherent on $D\times\mathbf{P}^1$: singular and nonflat sheaves are included.',
        ha='center', fontsize=13, color=blue)

def box(x, y, w, h, color, title, lines):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',
                              edgecolor=color,facecolor='white',linewidth=1.6))
    ax.text(x+w/2,y+h-.33,title,ha='center',va='center',fontsize=15,color=color)
    for j, text in enumerate(lines):
        ax.text(x+w/2,y+h-.82-.48*j,text,ha='center',va='center',fontsize=14,color=blue)

box(.55,4.45,5.55,2.72,blue,'Inner chart',[
    r'$U_1=D_0\times\{|z|<R_0\}$',
    r'$S_1=(\tau_k s_1,\;\tau_k B^{\prime}s_1)^{\mathsf{T}}$',
    r'$s_2=B s_1$ on the overlap',
    r'$B^{\prime}$ has a finite pole only at $0$'])
box(7.85,4.45,5.55,2.72,blue,'Outer chart, including infinity',[
    r'$U_2=D_0\times\{|z|>r_0\}$',
    r'$S_2=(\tau_k C^{\prime}s_2,\;\tau_k s_2)^{\mathsf{T}}$',
    r'$s_1=C s_2$ on the overlap',
    r'$C^{\prime}$ has a finite pole only at $\infty$'])
ax.add_patch(FancyArrowPatch((6.2,5.85),(7.65,5.85),arrowstyle='-|>',
                             mutation_scale=19,color=teal,linewidth=2))
ax.text(6.92,6.14,r'$S_2=T S_1$',ha='center',fontsize=13,color=teal)
ax.text(7,4.03,r'$T-I=\left[\,(C^{\prime}-C)B\quad 0\;;\; B-B^{\prime}\quad 0\,\right]$',
        ha='center',fontsize=16,color=teal)
ax.text(7,3.57,r'$\|T-I\|<\epsilon\quad\Longrightarrow\quad T=G_2^{-1}G_1$',
        ha='center',fontsize=17,color=teal)
ax.text(7,3.08,r'Bounded Laurent splitting: $L=U_1-U_2$;  $\|L_{j+1}\|\leq 2K\|L_j\|^2$.',
        ha='center',fontsize=13,color=blue)
box(2.1,1.35,9.8,1.25,teal,'The exact glued list',[
    r'$G_1S_1=G_2S_2\;\in\Gamma(D_0\times\mathbf{P}^1,A(k))^{2t}$'])
ax.text(7,.93,r'$\tau_k=X_1^bX_0^{k-b},\ k\geq2b$: cancels the finite poles; generation holds away from $\{0,\infty\}$.',
        ha='center',fontsize=12.5,color=orange)
ax.text(7,.45,r'Repeat with disjoint endpoints $\{p,q\}$: the combined global lists generate everywhere.',
        ha='center',fontsize=13,color=orange)
ax.text(7,.03,'Proof locator: Lemma 5.8.1, (5.8a)–(5.8g). Source: Norguet (1958), II.1–II.2, pp. 11-10–11-14.',
        ha='center',fontsize=10,color=blue)
fig.tight_layout(pad=.7)
fig.savefig(out/'relative-p1-generation-mechanism.svg',bbox_inches='tight')
fig.savefig(out/'relative-p1-generation-mechanism.png',dpi=160,bbox_inches='tight')

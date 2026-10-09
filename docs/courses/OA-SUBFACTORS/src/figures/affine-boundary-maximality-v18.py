"""CC0-1.0. Reproduce the exact objects and schematic AB lamp window."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'svg.hashsalt': 'affine-boundary-maximality-v18'})
fig, ax = plt.subplots(figsize=(13, 10))
fig.patch.set_facecolor('#f6f8fb')
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')

def box(x, y, width, height, text, color='#e3edf8', size=12):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
        boxstyle='round,pad=0.1,rounding_size=0.12',
        facecolor=color, edgecolor='#334e68', linewidth=1.3))
    ax.text(x+width/2, y+height/2, text, ha='center', va='center',
            fontsize=size, color='#122c43', linespacing=1.5)

def arrow(x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0,y0), (x1,y1),
        arrowstyle='-|>', mutation_scale=17, color='#334e68', linewidth=1.5))

ax.text(0.35, 9.65, 'The whole boundary of the alternating affine walk',
        fontsize=20, fontweight='bold', color='#122c43')
ax.text(0.35, 9.27,
        r'$G=\mathbb{F}_2[t,t^{-1}]\rtimes\mathbb{Z}$ acts on '
        r'$K=\mathbb{F}_2((t))$ by $x\mapsto b+t^n x$', fontsize=13)

box(0.45, 7.65, 5.7, 1.2,
    'Plus first:  1, a, T  with  (1/4, 1/4, 1/2)\n'
    'Then minus:  1, a, T⁻¹  with  (2/5, 2/5, 1/5)')
box(6.65, 7.65, 5.7, 1.2,
    'Minus first:  1, a, T⁻¹  with  (2/5, 2/5, 1/5)\n'
    'Then plus:  1, a, T  with  (1/4, 1/4, 1/2)')
arrow(3.3, 7.52, 3.3, 7.1)
arrow(9.5, 7.52, 9.5, 7.1)
box(0.9, 6.35, 4.8, 0.62, r'$X\sim\mu_V$  (AB.7)', '#dcefe6', 14)
box(7.1, 6.35, 4.8, 0.62, r'$X\sim\mu_U$  (AB.7)', '#dcefe6', 14)

ax.text(6.5, 5.82,
    r'$G_{2n}=(B_{2n},S_{2n}),\quad S_{2n}/n\to v=3/10,\quad '
    r'X=B_{2n}+t^{S_{2n}}X^{(2n)}$', ha='center', fontsize=14)
ax.text(6.5, 5.3,
    'On the event whose probability tends to one (AB.16–AB.18):',
    ha='center', fontsize=13, fontweight='bold')

colors = ['#dcefe6', '#fff0ca', '#e7eaf0']
segments = [(0.65,4.65,3.95),(4.6,4.65,3.8),(8.4,4.65,3.95)]
for (x,y,w), color in zip(segments, colors):
    ax.add_patch(Rectangle((x,y),w,0.38,facecolor=color,
                          edgecolor='#334e68',linewidth=1.2))
ax.text(2.6,4.45,r'$j<\ell_n$'+'\n'+r'Known: $(B_{2n})_j=X_j$',
        ha='center',va='top',fontsize=12,linespacing=1.4)
ax.text(6.5,4.45,r'$\ell_n\leq j\leq u_n$'+'\n'+'Binary choices',
        ha='center',va='top',fontsize=12,linespacing=1.4)
ax.text(10.4,4.45,r'$j>u_n$'+'\n'+r'Known: $(B_{2n})_j=0$',
        ha='center',va='top',fontsize=12,linespacing=1.4)
ax.text(4.6,3.85,r'$\ell_n=\lfloor(v-\varepsilon)n\rfloor$',ha='center')
ax.text(8.4,3.85,r'$u_n=\lceil(v+\varepsilon)n\rceil$',ha='center')
ax.text(6.5,3.37,
    r'$M_n=(u_n-\ell_n+1)\,2^{u_n-\ell_n+1}$ possible endpoints given $X$',
    ha='center',fontsize=14)
ax.text(6.5,2.95,
    'The first factor counts heights; the second counts lamp coefficients.',
    ha='center',fontsize=11)

arrow(6.5, 2.75, 6.5, 2.38)
box(0.8, 1.7, 11.4, 0.58,
    r'$H(G_{2n}\mid X)=o(n)\ \Longrightarrow\ '
    r'\bigcap_j\sigma(G_j,G_{j+1},\ldots)=\sigma(X)$', '#dcefe6', 15)
arrow(6.5,1.59,6.5,1.26)
box(0.8,0.51,11.4,0.62,
    r'Full endpoint-core centers: $Z(R_+)\cong L^\infty(K,\mu_V)$ and '
    r'$Z(R_-)\cong L^\infty(K,\mu_U)$', '#e3edf8',14)
ax.text(0.45,0.1,
    'Proofs: AB.4–AB.7. Coefficient window is schematic, with no metric scale. '
    'Method: Kaimanovich (2000).',fontsize=10,color='#526476')

fig.savefig(HERE/'affine-boundary-maximality-v18.png', dpi=145,
            bbox_inches='tight', facecolor=fig.get_facecolor())
fig.savefig(HERE/'affine-boundary-maximality-v18.svg',
            bbox_inches='tight', facecolor=fig.get_facecolor(), metadata={'Date': None})
plt.close(fig)

# Normalize serializer whitespace; coordinates and geometry are unchanged.
svg_path = HERE/'affine-boundary-maximality-v18.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines()).rstrip()+'\n', encoding='utf-8')

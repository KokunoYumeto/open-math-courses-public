from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(14, 9), dpi=160)
fig.patch.set_facecolor('#f7f7f2')
ax.set_facecolor('#f7f7f2')
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

def box(x, y, w, h, title, lines, color='#e3eeeb'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.13',
                              facecolor=color, edgecolor='#264c48', linewidth=1.3))
    ax.text(x+0.18, y+h-0.28, title, fontsize=13, fontweight='bold',
            color='#183b37', va='top')
    ax.text(x+0.18, y+h-0.78, '\n'.join(lines), fontsize=13,
            color='#162d2a', va='top', linespacing=1.6)

def arrow(a, b):
    ax.annotate('', xy=b, xytext=a,
                arrowprops=dict(arrowstyle='->', color='#264c48', lw=1.8))

ax.text(0.3, 8.75, 'Every boundary factor inherits regularity at infinity',
        fontsize=20, fontweight='bold', color='#183b37', va='top')
ax.text(0.3, 8.17, r'$P$ proper and smooth; $D$ SNC; arbitrary rank and Jordan blocks',
        fontsize=13, color='#264c48', va='top')

box(0.35, 6.18, 4.0, 1.45, 'Finite logarithmic lattices',
    [r'$M=\bigcup_m\overline{E}(mD)$',
     r'$\overline{E}(mD)$ is stable under $\mathscr{L}_P$'])
box(5.00, 6.18, 8.48, 1.45, 'Any simple subquotient, including a boundary factor',
    [r'$F=A/B=\bigcup_m L_m$',
     r'$L_m=\mathrm{im}(A\cap\overline{E}(mD)\longrightarrow A/B)$  (5.13d)'])
arrow((4.55, 6.91), (4.78, 6.91))

box(0.35, 3.28, 13.13, 2.15, 'Kashiwara extraction: $Z$ is one connected component of $D_I$',
    [r'$Q_m=\det(\mathcal{I}/\mathcal{I}^2)\otimes\mathrm{ann}_{\mathcal{I}}L_m$  (5.13k)',
     r'$z_i\partial_{z_i}v=-v$; the conormal determinant contributes $+v$  (5.13l)–(5.13m)',
     r'Normal-lift contributions cancel; tangent logarithmic fields preserve $Q_m$.'],
    color='#e9e5f2')
arrow((9.25, 6.00), (9.25, 5.61))

box(0.35, 0.45, 6.13, 1.92, 'A lattice at every remaining boundary divisor',
    [r'$\widetilde{Q}_m=\mathrm{im}(Q_m\to Q(*B_Z))$  (5.13o)',
     r'Choose $m$ of full generic rank.',
     r'At each transverse DVR: $t\partial_t L\subset L$.'],
    color='#e3eaf4')
box(7.13, 0.45, 6.35, 1.92, 'All curves, including infinity',
    [r'$H=Q|_{Z\setminus B_Z}$ is nonsingular.',
     r'Use the proved connection divisorial criterion.',
     r'$F=(Z\setminus B_Z\hookrightarrow P)_{!*}H$  (5.13q)'],
    color='#f2ecd8')
arrow((3.43, 3.08), (3.43, 2.55))
arrow((6.70, 1.40), (6.92, 1.40))

fig.tight_layout(pad=0)
fig.savefig(OUT/'snc-boundary-extraction.png', bbox_inches='tight',
            facecolor=fig.get_facecolor())
fig.savefig(OUT/'snc-boundary-extraction.svg', bbox_inches='tight',
            facecolor=fig.get_facecolor())

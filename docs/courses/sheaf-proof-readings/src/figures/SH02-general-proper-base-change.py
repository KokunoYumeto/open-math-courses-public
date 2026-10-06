"""Compact-germ gluing and general topological proper base change.

Original explanatory drawing, GPT-6 Astra (OpenAI), Ultra, 2026-10-06. CC0.
Mathematical source: SH02-open-prerequisite-proofs.html#general-proper-base-change,
GP2--GP3 and GP7--GP11. Existing human references are retained in that lesson.
The plane drawing encodes only labelled set relations, not an ambient metric,
Euclidean structure, Hausdorff condition, or local compactness assumption.

Run with Python and Matplotlib. The default writes only the claimed SVG.
An optional --preview /absolute/private/path.png writes a review PNG.
"""
from pathlib import Path
import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'mathtext.fontset': 'dejavusans',
    'svg.fonttype': 'path',
    'svg.hashsalt': 'SH02-general-proper-base-change-v1',
    'font.size': 16,
})

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'figures' / 'SH02-general-proper-base-change.svg'
INK, MUTED = '#172c3e', '#4c5e6b'
BLUE, ORANGE, GREEN, PURPLE = '#28668f', '#a85725', '#277348', '#694192'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', type=Path)
    args = parser.parse_args()

    fig = plt.figure(figsize=(16, 13), dpi=100, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 1600), ylim=(1300, 0))
    ax.set_axis_off()

    def text(x, y, value, size=16, color=INK, **kw):
        return ax.text(x, y, value, fontsize=size, color=color,
                       va='center', **kw)

    def panel(x, y, width, height):
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                     boxstyle='round,pad=0,rounding_size=15',
                     facecolor='#f8fafc', edgecolor='#cbd5df', linewidth=1.2))

    def arrow(x0, y0, x1, y1, color=INK, scale=16):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                     arrowstyle='-|>', mutation_scale=scale,
                     linewidth=1.6, color=color))

    text(45, 43, 'Compact germs make the proper-fibre comparison canonical',
         25, fontweight='bold')
    text(45, 79, 'Arbitrary topological spaces; proper means separated and universally closed.',
         16, MUTED)

    panel(40, 111, 1520, 623)
    text(66, 145, 'A  Shrink the overlaps into the agreement open', 20, fontweight='bold')
    text(66, 178, r'$K$ is compact; distinct points of $K$ have disjoint open neighborhoods in $X$.', 16)
    text(66, 207, 'Set-inclusion schematic only. The ambient opens Uᵢ and Uⱼ are not drawn.', 14, MUTED)

    # Ambient X is a drawing frame, not a coordinate chart or Hausdorff region.
    ax.add_patch(FancyBboxPatch((68, 229), 908, 323,
                 boxstyle='round,pad=0,rounding_size=12',
                 facecolor='white', edgecolor='#dae1e7', linewidth=1))
    text(88, 251, r'$X$', 19, MUTED)

    # P and Q are disjoint ambient opens. A may meet both.
    ax.add_patch(Rectangle((118, 283), 334, 207,
                 facecolor='#d5e9f5', edgecolor=BLUE, linewidth=1.4,
                 linestyle=(0, (4, 3))))
    ax.add_patch(Rectangle((568, 283), 327, 207,
                 facecolor='#f6e0cf', edgecolor=ORANGE, linewidth=1.4,
                 linestyle=(0, (4, 3))))
    ax.add_patch(Rectangle((354, 267), 293, 246,
                 facecolor='#d8eedf', edgecolor=GREEN, linewidth=1.5,
                 alpha=.9))
    text(183, 305, r'$P_{ij}$', 19, BLUE)
    text(814, 305, r'$Q_{ij}$', 19, ORANGE)
    text(500, 287, r'$A_{ij}$', 19, GREEN, ha='center')

    # Two closed pieces of the finite closed cover of K. All illustrated
    # intersections of K_i and K_j lie in A. The clipping highlights L_ij.
    ki_center, ki_width, ki_height = (370, 369), 498, 131
    ki = Ellipse(ki_center, ki_width, ki_height,
                 facecolor='none', edgecolor=PURPLE, linewidth=2)
    li = Ellipse(ki_center, ki_width, ki_height,
                 facecolor='#c6b4de', edgecolor='none', alpha=.75)
    ax.add_patch(li)
    li.set_clip_path(Rectangle((0, 0), 354, 1300, transform=ax.transData))
    ax.add_patch(ki)
    ax.add_patch(Ellipse((696, 404), 244, 135,
                 facecolor='#e9e4f0', edgecolor=PURPLE, linewidth=2, alpha=.95))
    # Redraw the first outline over the overlapping piece to show both sets.
    ax.add_patch(Ellipse(ki_center, ki_width, ki_height,
                 facecolor='none', edgecolor=PURPLE, linewidth=2))
    text(246, 370, r'$L_{ij}$', 20, PURPLE, ha='center')
    text(478, 365, r'$K_i$', 21, PURPLE, ha='center')
    text(728, 404, r'$K_j$', 21, PURPLE, ha='center')

    # K's dashed outline signifies only a schematic containing subset. It is
    # explicitly not a declaration that K is closed in the ambient X.
    ax.add_patch(Ellipse((497, 388), 796, 277,
                 facecolor='none', edgecolor=MUTED, linewidth=1.2,
                 linestyle=(0, (3, 5))))
    text(179, 510, r'$K$ (dashed)', 14, MUTED)
    text(641, 538, r'$K_i,K_j$ are closed in $K$', 15, PURPLE, ha='center')

    # Exact proof formulas, independent of the illustrative planar positions.
    text(1020, 258, 'Agreement of local representatives', 15, fontweight='bold')
    text(1020, 293, r'$K_i\cap K_j\subseteq A_{ij}\subseteq U_i\cap U_j$', 18)
    text(1020, 329, r'$s_i|_{A_{ij}}=s_j|_{A_{ij}}$', 19, GREEN)
    text(1020, 376, 'Separate the disjoint compact sets', 15, fontweight='bold')
    text(1020, 413, r'$L_{ij}=K_i\setminus A_{ij}\subseteq P_{ij}$', 18)
    text(1020, 450, r'$K_j\subseteq Q_{ij},\qquad P_{ij}\cap Q_{ij}=\varnothing$', 18)
    text(1020, 493, 'Both Pᵢⱼ and Qᵢⱼ are open in X.', 14, MUTED)
    text(1020, 527, 'Ambient closedness of Kᵢ or Kⱼ is not assumed.', 14, MUTED)

    text(76, 584, r'$N_i^{ij}=U_i\cap(A_{ij}\cup P_{ij}),\qquad N_j^{ij}=U_j\cap Q_{ij}$', 21)
    arrow(927, 585, 997, 585, GREEN)
    text(1030, 584, r'$N_i^{ij}\cap N_j^{ij}\subseteq A_{ij}$', 23, GREEN)
    text(1466, 620, 'GP3', 13, MUTED, ha='right')

    text(76, 640, 'Intersect the finitely many choices for each index:', 16, fontweight='bold')
    text(76, 682, r'$K_i\subseteq W_i\subseteq U_i$; the sections $s_i|_{W_i}$ glue on $W=\bigcup_iW_i\supseteq K$.', 19)
    text(1466, 707, 'GP2', 13, MUTED, ha='right')

    panel(40, 763, 1520, 426)
    text(66, 799, 'B  Closedness gives cofinal fibre neighborhoods; restriction gives the map',
         20, fontweight='bold')

    text(75, 850, r'$X_y\subseteq W$, with $W$ open in $X$', 18)
    text(75, 893, r'$V=Y\setminus f(X\setminus W)$', 23, BLUE)
    text(75, 936, r'$y\in V,\qquad f^{-1}V\subseteq W$', 22, BLUE)
    text(75, 980, 'V is open because f is closed.', 16)
    text(75, 1010, 'Neither {y} nor Xᵧ needs to be closed.', 15, MUTED)
    text(75, 1050, 'Use these neighborhoods in the stalk colimit.', 15, MUTED)

    # All arrows in the square are the actual maps of GP7 and GP10--GP11.
    # y=g(y') and A_y=A restricted to X_y; beta is the base-change map.
    text(1090, 845, r'$y=g(y^\prime),\qquad h:X^\prime_{y^\prime}\overset{\sim}{\longrightarrow}X_y$',
         18, ha='center')
    text(857, 902, r'$(f_*A)_y$', 22, ha='center')
    text(1332, 902, r'$(f^\prime_*g^{\prime-1}A)_{y^\prime}$', 22, ha='center')
    arrow(976, 902, 1175, 902)
    text(1074, 876, r'$\beta_{A,y^\prime}$', 17, ha='center')
    arrow(857, 937, 857, 1001, BLUE)
    arrow(1332, 937, 1332, 1001, BLUE)
    text(767, 968, 'restriction', 14, BLUE, ha='center')
    text(1451, 968, 'restriction', 14, BLUE, ha='center')
    text(857, 1032, r'$\Gamma(X_y;A_y)$', 21, ha='center')
    text(1332, 1032, r'$\Gamma(X^\prime_{y^\prime};h^{-1}A_y)$', 21, ha='center')
    arrow(1005, 1032, 1132, 1032, GREEN)
    text(1068, 1006, r'$h^*\ \cong$', 17, GREEN, ha='center')
    text(1090, 1083, r'$A_y=A|_{X_y},\qquad h(x,y^\prime)=x$', 17, MUTED, ha='center')
    text(1090, 1115, 'The square commutes on representative sections.  GP7, GP10–GP11',
         13, MUTED, ha='center')

    text(75, 1151, 'Acyclic restrictions of injectives give', 15, fontweight='bold')
    text(535, 1151, r'$(Rf_*F)_y\ \simeq\ R\Gamma(X_y;F|_{X_y})\qquad(F\in D^+(k_X)).$', 21)
    text(1490, 1151, 'GP8', 13, MUTED, ha='right')

    text(45, 1222, 'The fibre is compact Hausdorff with ambient point separation; the source and target spaces remain arbitrary.',
         15, MUTED)
    text(45, 1254, 'Proof locators: GP2–GP3 and GP7–GP11 in the general proper-base-change proof.  Coefficients: arbitrary k-modules.',
         14, MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, format='svg', metadata={
        'Title': 'Compact-germ gluing and general topological proper base change',
        'Creator': 'GPT-6 Astra (OpenAI), Ultra; reproducible Matplotlib source',
        'Date': None,
        'Description': 'Set-inclusion schematic for GP2--GP3 and the actual restriction square for GP7--GP11. Compact K has ambient point separation; neither ambient space is assumed Hausdorff or locally compact. All inclusions are non-strict.',
        'Rights': 'Original explanatory figure CC0. Mathematical references and component notices remain in the lesson.',
    })
    if args.preview:
        args.preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview, format='png', dpi=100,
                    metadata={'Software': 'Reproducible general proper base-change figure'})
    plt.close(fig)


if __name__ == '__main__':
    main()

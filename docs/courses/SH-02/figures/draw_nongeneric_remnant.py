"""CC0 1.0: exact tangent-space obstruction and finite analytic descent.

The left panel is an identified coordinate section of a stated complex line
in T*C^2, rather than an example of a microsupport. Sources: NG6–NG8.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none',
                     'svg.hashsalt': 'SH02-NG-remnant-v1'})
fig = plt.figure(figsize=(13.8, 9.4), layout='constrained')
gs = fig.add_gridspec(3, 2, height_ratios=[.22, 1, .68])
title = fig.add_subplot(gs[0, :])
title.axis('off')
title.text(0, .65, 'Why no nongeneric closed remnant can remain', fontsize=21, weight='bold')
title.text(0, .16, 'Exact linear calibration for n = 2, followed by the general finite-dimension argument', fontsize=12)

ax = fig.add_subplot(gs[1, 0])
ax.axhline(0, color='#2563eb', linewidth=3)
ax.axvline(0, color='#94a3b8', linewidth=1)
ax.scatter([0], [0], color='#111827', s=55, zorder=5)
ax.annotate('', xy=(0, .85), xytext=(0, 0),
            arrowprops={'arrowstyle': '-|>', 'lw': 3, 'color': '#dc2626'})
ax.text(.12, .58, r'$H\theta=\partial_{x_2}$' + '\n' + r'$\theta=d\xi_{x_2}\in\operatorname{Ann}(T_pT)$',
        color='#b91c1c', fontsize=12)
ax.text(-1.18, -.25, r'$T_pT\cap\mathrm{section}$', color='#1d4ed8')
ax.text(.08, -.16, r'$p=0$', fontsize=12)
ax.set_xlabel(r'base coordinate $x_1$')
ax.set_ylabel(r'base coordinate $x_2$')
ax.set_title(r'$\mathcal{Z}=\{z_2=\zeta_1=\zeta_2=0\}\subset T^*_{\mathbb{C}}\mathbb{C}^2$', fontsize=14)
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.15, 1.15)
ax.set_aspect('equal', adjustable='box')
ax.grid(alpha=.15)

ax = fig.add_subplot(gs[1, 1])
ax.axis('off')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
def box(y, height, text, color):
    ax.add_patch(FancyBboxPatch((.035, y), .92, height,
        boxstyle='round,pad=.015', facecolor=color, edgecolor='#94a3b8'))
    ax.text(.07, y + height / 2, text, va='center', fontsize=13)
box(.75, .20, r'$Q=T^*_{\mathbb{R}}\mathbb{C}^2,\quad\dim_{\mathbb{R}}Q=8$' + '\n' +
    r'$T_pT=\operatorname{span}(\partial_{x_1},\partial_{y_1}),\quad\dim_{\mathbb{R}}T=2$', '#dbeafe')
box(.45, .20, r'$H\operatorname{Ann}(T_pT)=(T_pT)^\omega$' + '\n' +
    r'$\dim_{\mathbb{R}}(T_pT)^\omega=8-2=6$', '#fee2e2')
ax.annotate('', xy=(.50, .68), xytext=(.50, .74), arrowprops={'arrowstyle': '-|>', 'lw': 1.5})
box(.08, .25, r'$p\in A\subset T\quad\Longrightarrow\quad C_p(A,A),C_p(A)\subset T_pT$' + '\n' +
    r'I15 would force $(T_pT)^\omega\subset T_pT$.' + '\n' +
    r'Impossible: $6\leq2$. The red vector also witnesses it.', '#fef3c7')
ax.annotate('', xy=(.50, .35), xytext=(.50, .44), arrowprops={'arrowstyle': '-|>', 'lw': 1.5})

ax = fig.add_subplot(gs[2, :])
ax.axis('off')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.text(.01, .91, 'The general argument uses finite analytic containing sets', fontsize=16, weight='bold')
ax.text(.01, .70, r'$A=\mathrm{SS}(i_*F)\cap(Q\setminus V)\subset J(\mathcal{B}),\qquad\dim_{\mathbb{C}}\mathcal{B}\leq n-1$', fontsize=16)
ax.text(.01, .49, r'On every exposed smooth piece: $\dim_{\mathbb{R}}T\leq2n-2$, but I15 requires $\dim_{\mathbb{R}}T\geq2n$.', fontsize=14)
ax.text(.01, .28, r'After deleting those pieces: $n-1\ \longrightarrow\ n-2\ \longrightarrow\ \cdots\ \longrightarrow\ -1$ (empty).', fontsize=15)
ax.text(.01, .05, 'At most n strict dimension drops; the residual A need not itself be analytic or stratified. Proof: NG6–NG8, NG15–NG18.', fontsize=11)
fig.savefig(OUT / 'nongeneric-remnant.svg', bbox_inches='tight', metadata={'Date': None})
fig.savefig(OUT / 'nongeneric-remnant.png', dpi=160, bbox_inches='tight')
plt.close(fig)
print('Rendered nongeneric-remnant.svg and nongeneric-remnant.png')

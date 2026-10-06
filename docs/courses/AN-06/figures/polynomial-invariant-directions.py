"""Exact strength sublevel and invariant-direction projection. CC0.

The infinite strip is shown in a finite window, with continuation arrows.
Reproduce the sibling PNG and SVG with NumPy and Matplotlib.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                           'svg.hashsalt': 'polynomial-invariant-directions',
                           'axes.spines.top': False, 'axes.spines.right': False})
out = Path(__file__).resolve().parent
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12, 5.8), layout='constrained')
ax.axvspan(-1, 1, color='#c4e1ef')
for x in [-1, 1]: ax.axvline(x, color='#216184', lw=1.7)
ax.axhline(0, color='#7c8b99', lw=.9)
ax.axvline(0, color='#7c8b99', lw=.9)
ax.plot([-1, 1], [0, 0], color='#a45429', lw=5, solid_capstyle='butt')
for x in [-.65, 0, .65]:
    for sign in [-1, 1]:
        ax.annotate('', xy=(x, sign*2.8), xytext=(x, sign*2.15),
                    arrowprops={'arrowstyle': '->', 'color': '#216184', 'lw': 1.5})
ax.annotate(r'$P\eta=(\eta_1,0)$', xy=(.5, 0), xytext=(1.2, -.9),
            arrowprops={'arrowstyle': '->', 'color': '#a45429'}, color='#a45429')
ax.text(.12, 1.55, r'$W=\{(0,\eta_2)\}$', fontsize=12)
ax.text(-2.3, -1.8, r'$\widetilde p(\eta)=\sqrt{\eta_1^2+1}\leq\sqrt{2}$ iff $|\eta_1|\leq1$', fontsize=11,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .92})
ax.set(xlim=(-2.5, 2.5), ylim=(-3, 3), xlabel=r'$\eta_1$', ylabel=r'$\eta_2$',
       title=r'$p(\eta)=\eta_1$: sublevel and compact projection')
ax.set_aspect('equal', adjustable='box')
ax.grid(alpha=.16)
x = np.linspace(-4, 4, 1601)
ratio = (np.abs(x)+1)/np.sqrt(x*x+1)
bx.plot(x, ratio, color='#216184', lw=2)
bx.axhline(1, color='#a45429', ls='--', label='proved lower bound: 1')
bx.text(0, 1.6, r'$\frac{|p(\eta)|+|\nabla p(\eta)|}{\widetilde p(\eta)}=\frac{|\eta_1|+1}{\sqrt{\eta_1^2+1}}$',
        ha='center', fontsize=15)
bx.text(0, .82, r'Independent of $\eta_2$; all ambient cutoffs are retained', ha='center', fontsize=11)
bx.set(xlim=(-4.2, 4.2), ylim=(.75, 1.75), xlabel=r'$\eta_1$', ylabel='zero-energy ratio',
       title='The threshold estimate survives the flat direction')
bx.grid(alpha=.16)
bx.legend(loc='upper right', fontsize=10)
fig.savefig(out/'polynomial-invariant-directions.svg', metadata={'Date': None, 'Creator': 'Original CC0 mathematical figure'})
fig.savefig(out/'polynomial-invariant-directions.png', dpi=180, metadata={'Software': 'Original CC0 mathematical figure'})
plt.close(fig)

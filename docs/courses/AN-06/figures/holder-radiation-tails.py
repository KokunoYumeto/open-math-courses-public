"""Exact Hölder remainder and radiation quotient slice. Original source: CC0.

Reproduce the sibling PNG and SVG with NumPy and Matplotlib. The omitted
central interval in the left numerical sample is indicated, not regularized.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                           'svg.hashsalt': 'holder-radiation-tails',
                           'axes.spines.top': False, 'axes.spines.right': False})
out = Path(__file__).resolve().parent
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.7), layout='constrained')
ax = axes[0]
for x in [-np.geomspace(.005, 1, 1200)[::-1], np.geomspace(.005, 1, 1200)]:
    y = -np.sign(x)/np.sqrt(np.abs(x))/(1+np.sqrt(np.abs(x)))
    ax.plot(x, y, color='#216184', lw=2)
ax.axvline(0, color='#a45429', ls='--', lw=1)
ax.axhline(0, color='#9aa5b1', lw=.7)
ax.text(.05, .95, r'$G(t)=-\frac{\mathrm{sgn}(t)}{\sqrt{|t|}(1+\sqrt{|t|})}$',
        transform=ax.transAxes, va='top', fontsize=15,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .94})
ax.text(.05, .12, r'$\int_{-\varepsilon}^{\varepsilon}|G(t)|\,dt=4\log(1+\sqrt{\varepsilon})$',
        transform=ax.transAxes, fontsize=13,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .94})
ax.text(.05, .04, r'Samples: $0.005\leq|t|\leq1$; singular at $0$',
        transform=ax.transAxes, fontsize=10)
ax.set(xlim=(-1.04, 1.04), ylim=(-14, 14), xlabel=r'$t$', ylabel=r'$G(t)$',
       title=r'$p(t)=t(1+\sqrt{|t|})$: an integrable remainder')
ax.grid(alpha=.16)
ax = axes[1]
radius = 1/np.sqrt(np.pi)
ax.add_patch(Circle((0, 0), radius, facecolor='#c4e1ef', edgecolor='#216184', lw=2))
ax.axhline(0, color='#7c8b99', lw=.8)
ax.axvline(0, color='#7c8b99', lw=.8)
ax.plot([0, radius], [0, 0], color='#a45429', lw=2)
ax.annotate(r'$1/\sqrt{\pi}$', xy=(radius/2, 0), xytext=(.22, -.22),
            arrowprops={'arrowstyle': '->', 'color': '#a45429'}, color='#a45429')
ax.text(0, .73, r'$\|s\mathscr{W}_+a+t\mathscr{W}_-a\|^2=\pi(s^2+t^2)$',
        ha='center', fontsize=14)
ax.text(0, -.77, r'$\|a\|_2=1$; real two-dimensional slice', ha='center', fontsize=11)
ax.set(xlim=(-.9, .9), ylim=(-.85, .85), xlabel=r'$s$: outgoing coordinate',
       ylabel=r'$t$: incoming coordinate', title='The exact quotient unit ball')
ax.set_aspect('equal', adjustable='box')
ax.grid(alpha=.16)
fig.savefig(out/'holder-radiation-tails.svg', metadata={'Date': None, 'Creator': 'Original CC0 mathematical figure'})
fig.savefig(out/'holder-radiation-tails.png', dpi=180, metadata={'Software': 'Original CC0 mathematical figure'})
plt.close(fig)

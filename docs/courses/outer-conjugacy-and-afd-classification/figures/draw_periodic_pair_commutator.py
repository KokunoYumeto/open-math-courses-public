"""Reproduce the exact finite-matrix angle curves in Lemma 2.1.

Run with the versions in requirements.txt. No infinite-dimensional
conclusion is inferred from the numerical samples used for this plot.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DEST = Path(__file__).resolve().parent
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 22,
    'axes.labelsize': 25,
    'axes.titlesize': 22,
    'svg.fonttype': 'path',
    'svg.hashsalt': 'periodic-pair-commutator-v1',
})
fig, axes = plt.subplots(2, 1, figsize=(8.2, 10.8), layout='constrained')
colors = {2: '#2456a6', 3: '#af4d12', 5: '#247342'}
points = {}
for p, color in colors.items():
    omega = np.pi / (np.sqrt(2) * p**2)
    t_star = np.arcsin(np.sqrt((1 - np.cos(omega)) /
                             (2 * np.sin(np.pi / p)**4))) / 2
    points[p] = (t_star / np.pi, omega / np.pi)
    for ax, extent in zip(axes, [0.25, 0.054]):
        t = np.linspace(0, extent * np.pi, 600)
        angle = 2 * np.arcsin(np.clip(np.sin(np.pi / p)**2 * np.sin(2 * t), 0, 1))
        ax.plot(t / np.pi, angle / np.pi, color=color, linewidth=2.8,
                label=fr'$p={p}$')
        ax.scatter([t_star / np.pi], [omega / np.pi], color=color,
                   edgecolor='white', linewidth=1.0, s=76, zorder=5)
for ax in axes:
    ax.set_xlabel(r'Rotation $t/\pi$')
    ax.set_ylabel(r'Commutator angle $\omega/\pi$')
    ax.grid(color='#dce2e8', linewidth=0.8)
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_ylim(bottom=0)
axes[0].set_xlim(0, 0.25)
axes[0].set_ylim(0, 1.04)
axes[0].set_title('The full range of rotation')
axes[0].legend(loc='upper left', frameon=True, facecolor='white')
axes[1].set_xlim(0, 0.054)
axes[1].set_ylim(0, 0.23)
axes[1].set_title('The selected irrational angles')
for p, color in colors.items():
    x, y = points[p]
    axes[1].annotate(fr'$p={p}$', (x, y), xytext=(7, 7),
                     textcoords='offset points', color=color, fontsize=22)
fig.suptitle(r'$U^p=V_t^p=1,\quad W_t=UV_tU^*V_t^*$', fontsize=25)
fig.savefig(DEST / 'periodic-pair-commutator.svg',
            metadata={'Date': None, 'Creator': 'Matplotlib',
                      'Description': 'Exact curves from Lemma 2.1; chosen angles from equation 2.6.'})
fig.savefig(DEST / 'periodic-pair-commutator.png', dpi=190,
            metadata={'Software': 'Matplotlib'})
plt.close(fig)

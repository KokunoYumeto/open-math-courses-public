"""Exact scalar valuation diagram for Lemma9.5 at p=2. Original CC0 figure."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent.parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14})
fig, ax = plt.subplots(figsize=(10.8, 6.7), layout='constrained')
fig.set_facecolor('#fbfcfe')
ax.set_facecolor('#fbfcfe')
left = np.linspace(0.015, 0.998, 200)
right = np.linspace(1.002, 2.6, 200)
ax.plot(left, 2*left, color='#1b6598', lw=3, label=r"$c<1:\quad c'=2c$")
ax.plot(right, right+1, color='#bd582a', lw=3, label=r"$c>1:\quad c'=c+1$")
ax.scatter([1], [2], facecolors='#fbfcfe', edgecolors='#59616d', s=95, lw=2, zorder=5)
ax.annotate('', xy=(1, 4.45), xytext=(1, 2.02), arrowprops={'arrowstyle': '-|>', 'linestyle': '--', 'color': '#59616d', 'lw': 2})
ax.text(1.10, 3.96, r"$c=1:\quad c'\geq2$", fontsize=15)
ax.text(1.10, 4.35, r"$\xi=-1:\quad c'=+\infty$", fontsize=13)
ax.scatter([.5, 1, 1, 2], [1, 2.5, 3, 3], color=['#1b6598', '#7456a4', '#7456a4', '#bd582a'], s=62, zorder=6)
ax.annotate(r'$\xi=1+\sqrt{2}$', xy=(.5, 1), xytext=(.09, 1.43), arrowprops={'arrowstyle': '-', 'color': '#1b6598'}, fontsize=14)
ax.annotate(r'$\xi=(1+\sqrt{2})^2$', xy=(1, 2.5), xytext=(1.18, 1.70), arrowprops={'arrowstyle': '-', 'color': '#7456a4'}, fontsize=14)
ax.annotate(r'$\xi=3$', xy=(1, 3), xytext=(.33, 3.21), arrowprops={'arrowstyle': '-', 'color': '#7456a4'}, fontsize=14)
ax.annotate(r'$\xi=5$', xy=(2, 3), xytext=(2.12, 2.78), arrowprops={'arrowstyle': '-', 'color': '#bd582a'}, fontsize=14)
ax.set(xlim=(0, 2.7), ylim=(0, 4.66), xlabel=r'$c=v_2(\xi-1)>0$', ylabel=r"$c'=v_2(\xi^2-1)$", title='Squaring near one: exact branches and a boundary inequality')
ax.set_xticks([0, .5, 1, 1.5, 2, 2.5], ['0', '1/2', '1', '3/2', '2', '5/2'])
ax.set_yticks([0, 1, 2, 2.5, 3, 4], ['0', '1', '2', '5/2', '3', '4'])
ax.grid(alpha=.16)
ax.legend(loc='lower right', fontsize=13, framealpha=.95)
fig.savefig(root/'figures/padic-squaring.png', dpi=170, metadata={'Software': 'Original CC0 mathematical figure by GPT-6.1 Sol (OpenAI), Ultra'})
plt.close(fig)

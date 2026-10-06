"""Exact exponent slacks for the auxiliary construction, n=2.

Original course figure by GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0.
This is a plot of proved parameter inequalities, not numerical logarithm data.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent.parent / 'figures'
out.mkdir(exist_ok=True)
delta = [i / 600 for i in range(301)]
eta = [1 - 3 * d for d in delta]
fig, ax = plt.subplots(figsize=(8.5, 4.6), constrained_layout=True)
ax.axvspan(0, 1 / 3, color='#ddece2', alpha=0.8)
ax.axhline(0, color='#64748b', linewidth=1)
ax.plot(delta, eta, color='#16658d', linewidth=2.4, label=r'dimension saving $\eta_\delta=1-3\delta$')
ax.plot(delta, delta, color='#b56812', linewidth=2.4, label=r'coefficient saving $\delta$')
ax.axvline(1 / 3, color='#64748b', linestyle='--', linewidth=1.2)
ax.axvline(1 / 8, color='#92506c', linestyle=':', linewidth=1.4)
ax.scatter([1 / 8, 1 / 8], [5 / 8, 1 / 8], color=['#16658d', '#b56812'], s=50, zorder=5)
ax.annotate(r'$\delta=1/8,\quad\eta_\delta=5/8$', (1 / 8, 5 / 8),
            xytext=(0.17, 0.74), fontsize=11,
            arrowprops={'arrowstyle': '-', 'color': '#92506c'})
ax.text(0.03, -0.31, r'both savings positive: $0<\delta<1/3$', fontsize=12, color='#175e50')
ax.set_xlim(0, 0.5)
ax.set_ylim(-0.55, 1.1)
ax.set_xticks([0, 1 / 8, 1 / 3, 1 / 2], ['0', '1/8', '1/3', '1/2'])
ax.set_xlabel(r'$\delta$', fontsize=13)
ax.set_ylabel('power of h', fontsize=12)
ax.set_title('Two logarithms: balancing dimension and coefficient size', fontsize=13)
ax.legend(loc='upper right', fontsize=10, frameon=False)
ax.grid(alpha=0.15)
fig.savefig(out / 'auxiliary-parameter-window.png', dpi=175)
fig.savefig(out / 'auxiliary-parameter-window.svg')
print(str((out / 'auxiliary-parameter-window.png').resolve()))

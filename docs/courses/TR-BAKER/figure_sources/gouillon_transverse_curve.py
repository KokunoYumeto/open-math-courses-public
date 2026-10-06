"""Real slice of the finite-torsion example, with exact derivative directions.

Original course figure by GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0.
The complex variety is X1=0, X0=Y**2, Y!=0; this plot is its real slice.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent.parent / 'figures'
out.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(9.0, 5.5), constrained_layout=True)
y_values = [0.03 + j * (1.72 - 0.03) / 400 for j in range(401)]
x_values = [y * y for y in y_values]
ax.plot(x_values, y_values, color='#16658d', linewidth=2.4)
ax.plot(x_values, [-y for y in y_values], color='#16658d', linewidth=2.4,
        label=r'$V:\ X_0=Y^2,\quad X_1=0$')
ax.axvline(2, color='#64748b', linestyle='--', linewidth=1.3)
ax.scatter([2, 2], [math.sqrt(2), -math.sqrt(2)], color='#bd3c23', s=48, zorder=5)
ax.annotate(r'$Y=+\sqrt{2}$', (2, math.sqrt(2)), xytext=(2.12, 1.45), fontsize=11)
ax.annotate(r'$Y=-\sqrt{2}$', (2, -math.sqrt(2)), xytext=(2.12, -1.47), fontsize=11)
ax.text(2.07, 0.1, r'fiber $X_0=2$', fontsize=11, color='#475569')
for y in [0.28, 1 / math.sqrt(2), 1.14, -0.28, -1 / math.sqrt(2), -1.14]:
    x = y * y
    # Every arrow is the same positive multiple 0.24 of (1,Y).
    ax.annotate('', xy=(x + 0.24, y + 0.24 * y), xytext=(x, y),
                arrowprops={'arrowstyle': '->', 'color': '#b56812', 'lw': 1.7})
ax.scatter([0.5, 0.5], [1 / math.sqrt(2), -1 / math.sqrt(2)],
           facecolors='white', edgecolors='#b56812', s=70, linewidth=1.6, zorder=6)
ax.scatter([0], [0], facecolors='white', edgecolors='#16658d', s=45, linewidth=1.5, zorder=6)
ax.text(0.1, -0.1, 'origin excluded', fontsize=10, color='#475569')
ax.annotate(r'tangency: $2Y^2=1$', (0.5, 1 / math.sqrt(2)),
            xytext=(0.1, 1.47), fontsize=11,
            arrowprops={'arrowstyle': '-', 'color': '#b56812'})
ax.text(0.08, -1.67, r'arrows: $0.24\,(1,Y)$, the direction of $\mathcal{D}$', fontsize=11,
        color='#92520d')
ax.set_xlim(-0.08, 3.05)
ax.set_ylim(-1.85, 1.85)
ax.set_xlabel(r'$X_0$', fontsize=12)
ax.set_ylabel(r'$Y$', fontsize=12, rotation=0, labelpad=12)
ax.set_title('A degree-two projection with a generically transverse derivative', fontsize=13)
ax.grid(alpha=0.14)
ax.legend(loc='center', bbox_to_anchor=(0.4, 0.51), frameon=False, fontsize=11)
fig.savefig(out / 'gouillon-transverse-curve.png', dpi=175)
fig.savefig(out / 'gouillon-transverse-curve.svg')
print(str((out / 'gouillon-transverse-curve.png').resolve()))

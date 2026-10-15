"""Exact coordinates for GP6.1; emit SVG and a local PNG for inspection."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'oa-mod-gp6-v1', 'font.size': 12})
out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(7.4, 5.8), constrained_layout=True)
ax.set_aspect('equal')
ax.plot([-0.12, 0.7], [-0.24, 1.4], color='#147a83', linewidth=3)
ax.annotate('', xy=(1, 0), xytext=(0, 0), arrowprops={'arrowstyle': '->', 'color': '#777777', 'lw': 2})
ax.annotate('', xy=(1/5, 2/5), xytext=(0, 0), arrowprops={'arrowstyle': '->', 'color': '#164d9b', 'lw': 3})
ax.plot([1/5, 1], [2/5, 0], '--', color='#d06b25', lw=2)
ax.scatter([1, 1/5], [0, 2/5], c=['#777777', '#164d9b'], zorder=5)
ax.annotate(r'$e_1=(1,0)$', (1,0), xytext=(-5,-29), textcoords='offset points', ha='center')
ax.annotate(r'$P_Ge_1=(1/5,2/5)$', (1/5,2/5), xytext=(19,15), textcoords='offset points', color='#164d9b')
ax.text(0.35, 1.15, r'$G: y=2x$', color='#147a83')
ax.text(0.74,0.27, 'Orthogonal\nresidual', color='#a9541a', ha='center')
ax.text(0.76,0.83, r'$a=1/5$'+'\n'+r'$b=2/5$'+'\n'+r'$\|R_\eta\|=2$', ha='center', bbox={'facecolor':'#eff4f8','edgecolor':'none','pad':12})
ax.set_xlim(-0.2,1.22); ax.set_ylim(-0.22,1.45)
ax.set_xticks([0,1/5,1], ['0','1/5','1']); ax.set_yticks([0,2/5,1], ['0','2/5','1'])
ax.set_xlabel('First coordinate'); ax.set_ylabel('Second coordinate')
ax.grid(alpha=0.17); ax.spines[['top','right']].set_visible(False)
ax.set_title('A lower projection bound controls the graph slope', pad=16)
fig.savefig(out/'bounded-right-graph.svg', metadata={'Date':None})
fig.savefig(out/'bounded-right-graph.png', dpi=150)
plt.close(fig)

"""Figure 22.11 from exact bounded-product denominators."""
from pathlib import Path
from math import lgamma, log
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).parent
data = json.loads((root/'elliptic-first-jet-height-check.json').read_text())
rows = data['denominator_figure_data']
N = [r['N'] for r in rows]
exact = [log(int(r['delta_2'])) for r in rows]
plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                     'axes.spines.right': False, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(10, 5.8), layout='constrained')
ax.plot(N, [lgamma(n+1) for n in N], color='#9b3b30', lw=2,
        label=r'Factorial: $\log(N!)$')
ax.plot(N, [3*log(2)*n for n in N], color='#526276', lw=2,
        label=r'Proved bound: $3(\log 2)N$')
ax.scatter(N, exact, s=17, color='#087b88',
           label=r'Exact values: $\log\Delta_N(2)$', zorder=3)
ax.set(xlabel='Total jet order N', ylabel='Natural logarithm of denominator',
       xlim=(0, 82), ylim=(0, 290),
       title='At most two logarithm factors: a denominator with linear log growth')
ax.grid(alpha=.2)
ax.legend(loc='upper left', frameon=False)
fig.savefig(root/'first-jet-denominators.png', dpi=160)
plt.close(fig)

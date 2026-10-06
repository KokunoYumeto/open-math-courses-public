"""Reproduce Figure 1: exact prime-power jumps and ten numerical zero pairs.

Original CC0 figure, OpenAI GPT-6.1 Sol in Codex, Ultra setting, October 2026.
Requires numpy, matplotlib and mpmath. Samples do not certify an error bound.
"""
from pathlib import Path
import math
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mp.mp.dps = 40
zeros = [complex(mp.zetazero(j)) for j in range(1, 11)]
prime_powers = {}
for p in range(2, 111):
    if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
        continue
    n = p
    while n <= 110:
        prime_powers[n] = math.log(p)
        n *= p

def psi_left(x):
    return sum(weight for n, weight in prime_powers.items() if n < x)

points = np.linspace(90, 110, 2001)
logx = np.log(points)
pair_sum = 2 * np.real(sum(np.exp(rho * logx) / rho for rho in zeros))
approximation = points - pair_sum - math.log(2 * math.pi) - .5 * np.log1p(-points ** -2)
jumps = [n for n in sorted(prime_powers) if 90 < n < 110]
edges = [90] + jumps + [110]
levels = [psi_left(n) + prime_powers.get(n, 0) for n in edges]

plt.rcParams.update({'font.size': 12, 'axes.labelsize': 13})
fig, ax = plt.subplots(figsize=(10.4, 5.7), constrained_layout=True)
ax.step(edges, levels, where='post', color='#244766', linewidth=2.2,
        label=r'Exact $\psi$: one-sided staircase')
ax.plot(points, approximation, color='#c25523', linewidth=2.0,
        label=r'$P_{10}$: ten computed conjugate pairs')
midpoints = [psi_left(n) + prime_powers[n]/2 for n in jumps]
ax.scatter(jumps, midpoints, s=44, color='#244766', edgecolor='white',
           linewidth=.7, zorder=5, label=r'Half-weight value $\psi_0$ at each jump')
for n, mid in zip(jumps, midpoints):
    ax.annotate(str(n), (n, mid), xytext=(5, -15), textcoords='offset points',
                fontsize=10, color='#244766')
ax.set_xlim(90, 110)
ax.set_ylim(85, 118)
ax.set_xticks(range(90, 111, 2))
ax.set_xlabel(r'$x$')
ax.set_ylabel('Weighted prime-power count')
ax.set_title('The sharp explicit formula near 100: a finite illustration', pad=12)
ax.grid(alpha=.2)
ax.legend(loc='upper left', framealpha=.95, fontsize=11)
fig.savefig(Path(__file__).with_suffix('.png'), dpi=180)
plt.close(fig)

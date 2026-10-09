"""CC0 exact two-dimensional TC3 radial-straightening example.

The displayed formulas define the example; sampled traces are illustrative.
The orientation, endpoints, reciprocal interpolation and vertex are retained.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'svg.fonttype': 'none', 'svg.hashsalt': 'SH02-TC3-radial-example-v1',
                     'mathtext.fontset': 'dejavusans'})
u = np.linspace(-1, 1, 601)
delta = 1 / 4
r = 1 / 2 + 3 * u / 25 + 2 * u * u / 25
R = 1 / ((1-u)/(2*(23/50)) + (1+u)/(2*(7/10)))
assert np.min(r) >= 91/200 - 1e-12 and np.max(r) <= 7/10 + 1e-12
assert np.all(R > delta) and np.all(R < 1)
fig, axes = plt.subplots(1, 2, figsize=(13.8, 8.3), dpi=180)
fig.patch.set_facecolor('#f8fafc')
fig.suptitle('An exact example of the radial triangulation map', fontsize=21, fontweight='bold', y=.975)
for ax, middle, title in zip(axes, (R, r), ('Straight model', 'Original analytic branches')):
    ax.set_facecolor('#f8fafc')
    ax.fill([0, 1, 1], [0, -1, 1], color='#eef2ff', zorder=0)
    ax.plot([0, 1, 1, 0], [0, -1, 1, 0], color='#334155', lw=1.6)
    for slope in (-1, -.5, 0, .5, 1):
        ax.plot([0, 1], [0, slope], color='#94a3b8', lw=.8, ls='--')
    for h, color in ((np.full_like(u, delta), '#a16207'), (middle, '#2563eb'), (np.ones_like(u), '#334155')):
        ax.plot(h, h*u, color=color, lw=2.7)
    ax.scatter([0], [0], s=35, color='#0f172a', zorder=4)
    ax.text(.025, -.07, r'$a=(0,0)$', fontsize=12)
    ax.text(.265, -.31, r'$r_0=R_0=1/4$', color='#a16207', fontsize=11)
    ax.text(1.015, .80, r'$u\mapsto(1,u)$', fontsize=11)
    ax.set_title(title, fontsize=17, fontweight='bold', pad=13)
    ax.set_xlim(-.07, 1.19); ax.set_ylim(-1.10, 1.10)
    ax.set_aspect('equal'); ax.axis('off')
R0 = 1 / ((1/(2*(23/50))) + (1/(2*(7/10))))
axes[0].scatter([R0], [0], color='#15803d', s=50, zorder=5)
axes[0].annotate(r'$(R_1(0),0)$', (R0, 0), xytext=(.57, -.20),
                 arrowprops={'arrowstyle': '-', 'color': '#15803d'}, color='#15803d', fontsize=11)
axes[1].scatter([.5], [0], color='#15803d', s=50, zorder=5)
axes[1].annotate(r'$(r_1(0),0)=(1/2,0)$', (.5, 0), xytext=(.51, -.22),
                 arrowprops={'arrowstyle': '-', 'color': '#15803d'}, color='#15803d', fontsize=11)
fig.text(.075, .238, r'$R_1(u)=\left(\frac{1-u}{2}\frac{50}{23}+\frac{1+u}{2}\frac{10}{7}\right)^{-1}$', fontsize=15, color='#2563eb')
fig.text(.54, .238, r'$r_1(u)=\frac{1}{2}+\frac{3u}{25}+\frac{2u^2}{25}$', fontsize=15, color='#2563eb')
fig.text(.5, .56, r'$T$', fontsize=22, ha='center', color='#0f172a')
axes[0].annotate('', xy=(.527, .51), xytext=(.477, .51), xycoords=fig.transFigure,
                 arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': '#0f172a'})
fig.text(.075, .168, r'For $R_i(u)\leq t\leq R_{i+1}(u)$, $T(t,tu)=(h,hu)$,', fontsize=14)
fig.text(.075, .119, r'$h=r_i(u)+\frac{t-R_i(u)}{R_{i+1}(u)-R_i(u)}\,[r_{i+1}(u)-r_i(u)]$, with $i=0,1$ and $r_2=R_2=1$.', fontsize=14)
fig.text(.075, .073, r'$-1\leq u\leq1$, $1/4<91/200\leq r_1(u)\leq7/10<1$; the inner triangle is fixed and $\tau=\mathrm{id}$.', fontsize=12)
fig.text(.075, .032, 'Exact TC3 example. Curves are sampled from the displayed formulas; the proof supplies the bounds and compatibility.', fontsize=10)
fig.subplots_adjust(left=.045, right=.975, top=.85, bottom=.29, wspace=.14)
fig.savefig(OUT/'triangulation-radial-straightening.svg', facecolor=fig.get_facecolor(), metadata={'Date': None})
fig.savefig(OUT/'triangulation-radial-straightening.png', facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered the exact TC3 radial-straightening example.')

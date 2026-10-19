"""An exact prime-support example for the Stewart--Yu grouping argument."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
out = HERE.parent/'figures/prime-parts.png' if HERE.name == 'figure_sources' else HERE/'prime-parts.png'
assert 11**2 + 3**2*5**6*7**3 == 2**21*23
assert 2*3*5*7*11*23 == 53130
assert 53130//(11*7*23) == 30

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(12, 7.2), facecolor='#fbfcfe')
ax = fig.add_axes([.025, .025, .95, .95])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ink = '#18334a'
blue = '#d9edf8'
orange = '#f7e5c9'
ax.text(.5, .965, 'Keeping three greatest primes separate',
        ha='center', va='top', fontsize=20, color=ink, weight='bold')
ax.text(.5, .875, r'$121+48\,234\,375=48\,234\,496$',
        ha='center', fontsize=18, color=ink)
ax.text(.14, .80, 'component', ha='center', color=ink, weight='bold')
ax.text(.46, .80, 'grouped part', ha='center', color=ink, weight='bold')
ax.text(.79, .80, 'greatest-prime power', ha='center', color=ink, weight='bold')

rows = [
    (.69, r'$a=11^2$', r'$R_a=1$', r'$p_a^{\,2}=11^2$'),
    (.53, r'$b=3^2\cdot5^6\cdot7^3$', r'$R_b=3^2\cdot5^6$', r'$p_b^{\,3}=7^3$'),
    (.37, r'$c=2^{21}\cdot23$', r'$R_c=2^{21}$', r'$p_c=23$'),
]
for y, label, group, greatest in rows:
    ax.text(.14, y, label, ha='center', va='center', fontsize=18, color=ink)
    for x, color, text in [(.46, blue, group), (.79, orange, greatest)]:
        ax.add_patch(FancyBboxPatch((x-.125, y-.055), .25, .11,
                                   boxstyle='round,pad=0.008,rounding_size=0.012',
                                   facecolor=color, edgecolor='#8aa1b0', linewidth=1))
        ax.text(x, y, text, ha='center', va='center', fontsize=19, color=ink)
    ax.text(.625, y, r'$\times$', ha='center', va='center', fontsize=19, color=ink)

ax.text(.5, .265,
        r'$r=6,\quad \exp((\log r)^2)=24.789\ldots,\quad M=30$',
        ha='center', fontsize=15, color=ink)
ax.text(.5, .205, 'All six primes are below the cutoff; the three greatest primes stay separate.',
        ha='center', fontsize=12, color=ink)
ax.text(.5, .115,
        r'$\frac{c}{b}=\left(\frac{2^{21}}{3^2\cdot5^6}\right)\cdot23\cdot7^{-3}$',
        ha='center', va='center', fontsize=24, color=ink)
ax.text(.5, .025, 'Five prime bases become three independent rational bases.',
        ha='center', fontsize=14, color=ink, weight='bold')
fig.savefig(out, dpi=160, facecolor=fig.get_facecolor(),
            metadata={'Software': 'TR-BAKER reproducible figure'})
plt.close(fig)
print(out)

"""Exact finite geometry for Lemmas 19.2 and 19.3 (CC0).

The lattice points and residue classes are exact; decimal axis positions
only display the real simplex. This is an illustration, not a finite
substitute for the asymptotic Stewart--Tijdeman theorem.
"""
from pathlib import Path
from math import log, gcd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Patch

HERE = Path(__file__).resolve().parent
points = [(i, j, 3**i*5**j) for i in range(5) for j in range(3)
          if 3**i*5**j <= 100]
values = sorted(n for i, j, n in points)
assert values == [1, 3, 5, 9, 15, 25, 27, 45, 75, 81]
assert 81 % 8 == 9 % 8 == 1 and gcd(81, 9) == 9
assert (81-9)//9 == 8

plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11,
                     'axes.titlesize':13, 'axes.labelsize':11})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.8, 4.9),
                             gridspec_kw={'width_ratios':[1, 1.2]})
fig.subplots_adjust(left=.065, right=.985, bottom=.26, top=.87, wspace=.28)
for i, j, n in points:
    ax.add_patch(Rectangle((i, j), 1, 1, facecolor='#e6eff8',
                            edgecolor='#7fa4c7', linewidth=.9))
ax.add_patch(Polygon([(0, 0), (log(100)/log(3), 0),
                     (0, log(100)/log(5))], closed=True,
                    facecolor='#ffd56a', alpha=.58, edgecolor='#aa7300', linewidth=1.8))
for i, j, n in points:
    ax.plot(i, j, 'o', color='#123d63', ms=4, zorder=4)
    ax.text(i+.10, j+.16, str(n), fontsize=10, color='#102f49')
ax.set(xlim=(-.12, 5.1), ylim=(-.12, 3.25), xticks=range(6), yticks=range(4),
       xlabel=r'Exponent $i$ in $3^i5^j$', ylabel=r'Exponent $j$',
       title='Ten admissible cubes cover the simplex\n'+r'$i\log3+j\log5\leq\log100$')
ax.legend(handles=[Patch(facecolor='#ffd56a', alpha=.58, label='Real simplex'),
                   Patch(facecolor='#e6eff8', edgecolor='#7fa4c7', label='Admissible unit cubes')],
          loc='upper right', frameon=True, fontsize=9)

for residue in [1, 3, 5, 7]:
    bx.axhline(residue, color='#dae1e8', lw=.8, zorder=0)
for n in values:
    special = n in [9, 81]
    bx.scatter(n, n % 8, s=60 if special else 30,
               color='#ac2c32' if special else '#205b83', zorder=3)
    dy = .48 if n in [1, 5, 9, 45, 81] else -.55
    bx.text(n, n % 8+dy, str(n), ha='center', va='center', fontsize=10)
bx.annotate('', xy=(81, 1), xytext=(9, 1),
            arrowprops={'arrowstyle':'<->', 'color':'#ac2c32', 'lw':1.5,
                        'connectionstyle':'arc3,rad=-.17'})
bx.text(46, 2.0, r'$81-9=72=8\cdot9$', ha='center', fontsize=11, color='#9e252d')
bx.set(xlim=(-4, 102), ylim=(-.05, 8.1), yticks=[1, 3, 5, 7],
       xticks=[0, 25, 50, 75, 100], xlabel=r'Supported integer $n\leq100$',
       ylabel=r'Residue $n\ \mathrm{mod}\ 8$', title='An odd gcd preserves the power of two')
bx.text(.5, -.27, r'$g=9:\quad 9+72=81\ \longmapsto\ 1+8=9$',
        transform=bx.transAxes, ha='center', fontsize=12, color='#9e252d')
fig.text(.06, .035, 'Labels in the left panel give the integer represented by each exponent vector.',
         fontsize=10, color='#34495e')
output = HERE.parent/'figures/abc-construction.png' if HERE.name == 'figure_sources' else HERE/'abc-construction.png'
fig.savefig(output, dpi=170, facecolor='white',
            metadata={'Software':'Matplotlib; original Lesson 19 figure (CC0)'})
plt.close(fig)
print({'lattice_points':len(points), 'selected_pair':[81,9], 'gcd':9, 'reduced_triple':[1,8,9]})

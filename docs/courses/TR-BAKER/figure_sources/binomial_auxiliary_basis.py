"""Exact k=L=2 binomial basis and rational coefficient matrix; original CC0 figure."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans',
                     'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 11})
folder = Path(__file__).resolve().parent
fig, (left, right) = plt.subplots(1, 2, figsize=(12.2, 6.1), gridspec_kw={'width_ratios': [1.1, 1]})
x = np.linspace(-3, -1, 601)
f0 = (x+1)*(x+2)/2
f1 = (x+2)*(x+3)/2
colors = ['#2468a0', '#bd6829', '#3c805f', '#8b4d8b']
for values, label, color, style in zip([f0, f1, f0*f0, f1*f1],
        [r'$F_{0,1}$', r'$F_{1,1}$', r'$F_{0,2}$', r'$F_{1,2}$'], colors, ['-', '-', '--', '--']):
    left.plot(x, values, label=label, color=color, linestyle=style, linewidth=2)
left.axhline(0, color='#555555', linewidth=.8)
left.axvline(-2, color='#777777', linestyle=':', linewidth=1)
left.scatter([-2], [0], color='#222222', s=38, zorder=5)
left.annotate('Shared root at −2', xy=(-2, 0), xytext=(-2.8, .42),
              arrowprops={'arrowstyle': '->', 'color': '#444444'}, fontsize=11)
left.set(xlim=(-3, -1), ylim=(-.2, 1.08), xlabel=r'Real coordinate $X$', ylabel='Polynomial value',
         title='Four independent polynomials')
left.grid(alpha=.18)
left.legend(ncol=2, loc='upper center', framealpha=.95)
right.axis('off')
right.set_title('Exact coefficient matrix', pad=14)
cells = [[r'$3/2$', r'$5/2$', r'$3$', r'$15$'],
         [r'$1/2$', r'$1/2$', r'$13/4$', r'$37/4$'],
         [r'$0$', r'$0$', r'$3/2$', r'$5/2$'],
         [r'$0$', r'$0$', r'$1/4$', r'$1/4$']]
table = right.table(cellText=cells, rowLabels=[r'$X$', r'$X^2$', r'$X^3$', r'$X^4$'],
                    colLabels=[r'$F_{0,1}$', r'$F_{1,1}$', r'$F_{0,2}$', r'$F_{1,2}$'],
                    cellLoc='center', loc='center', bbox=[.06, .33, .94, .52])
table.auto_set_font_size(False)
table.set_fontsize(13)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#b5bdc5')
    if row == 0:
        cell.set_facecolor('#e9edf1')
    elif col >= 0:
        cell.set_facecolor('#e7f0f8' if row <= 2 and col <= 1 else '#eaf3ec' if row >= 3 and col >= 2 else '#ffffff')
right.text(.5, .2, r'$\det A=(-1/2)(-1/4)=1/8$', transform=right.transAxes,
           ha='center', fontsize=15)
right.text(.5, .075, 'The omitted constant coefficient is fixed\nby the common vanishing at −2.',
           transform=right.transAxes, ha='center', fontsize=11)
fig.suptitle(r'$F_{a,\ell}(X)=\left((X+a+1)(X+a+2)/2\right)^\ell$', y=.99, fontsize=15)
fig.subplots_adjust(left=.07, right=.98, top=.87, bottom=.12, wspace=.29)
fig.savefig(folder/'binomial-auxiliary-basis.png', dpi=180, facecolor='white')
plt.close(fig)

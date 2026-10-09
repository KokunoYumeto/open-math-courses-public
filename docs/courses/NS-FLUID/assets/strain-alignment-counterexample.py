"""Exact support sections and spectra from NS-FLUID-08, Exercise 5."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
fig = plt.figure(figsize=(13.2, 5.2), layout='constrained')
gs = fig.add_gridspec(1, 3, width_ratios=[1.55, 1, 1])
ax = fig.add_subplot(gs[0])
for center, color, name in [(-3, '#a34b31', r'$-x_+$'), (3, '#176879', r'$x_+$')]:
    ax.add_patch(Circle((center, 0), 1, color=color, alpha=.16))
    ax.add_patch(Circle((center, 0), 1, fill=False, color=color, lw=1.8))
    ax.add_patch(Circle((center, 0), .5, fill=False, color=color, lw=2, ls='--'))
    ax.plot(center, 0, '.', color=color)
    ax.text(center, 1.2, name, ha='center', fontsize=13, color=color)
ax.axhline(0, lw=.6, color='#555555')
ax.axvline(0, lw=.6, color='#555555')
ax.set(xlim=(-4.5, 4.5), ylim=(-2, 2), aspect='equal', xlabel=r'$x_1$', ylabel=r'$x_3$',
       title=r'Exact section $x_2=0$; $a=\ell=1$')
ax.set_xticks([-4, -3, -2, 0, 2, 3, 4])
ax.set_yticks([-1, 0, 1])
ax.text(.5, -.22, 'Solid: support radius 1\nDashed: affine radius 1/2', transform=ax.transAxes,
        ha='center', va='top', fontsize=11)
for index, values, coords, title, color, direction, role in [
    (1, [-3, 1, 2], ['e₁', 'e₂', 'e₃'], r'Inner ball at $x_+$', '#176879', r'$\omega=e_3$', 'largest'),
    (2, [-2, -1, 3], ['e₃', 'e₂', 'e₁'], r'Inner ball at $-x_+$', '#a34b31', r'$\omega=-e_3$', 'smallest'),
]:
    a = fig.add_subplot(gs[index])
    a.axhline(0, color='#555555', lw=.7)
    a.scatter([1, 2, 3], values, s=80, color=color, zorder=3)
    for x, value, coord in zip([1, 2, 3], values, coords):
        a.vlines(x, 0, value, color=color, lw=1.8)
        a.annotate(f'{value} along {coord}', (x, value), xytext=(0, 11 if value>=0 else -20),
                   textcoords='offset points', ha='center', fontsize=10)
    a.set(xlim=(.4, 3.6), ylim=(-4.2, 4.2), xticks=[1, 2, 3],
          xticklabels=[r'$\lambda_1$', r'$\lambda_2$', r'$\lambda_3$'],
          ylabel='Strain eigenvalue', title=title)
    a.grid(axis='y', alpha=.15)
    a.text(.5, -.19, direction+'\n'+f'Vorticity follows the {role} eigenvalue',
           transform=a.transAxes, ha='center', va='top', fontsize=10)
fig.suptitle(r'Zero total stretching: $\int\omega\cdot S\omega=0$ by odd parity', fontsize=15)
fig.savefig(HERE/'strain-alignment-counterexample.png', dpi=180)
fig.savefig(HERE/'strain-alignment-counterexample.svg')
plt.close(fig)

"""Reproduce the exact support/rank schematic and oscillator kernel (CC0-1.0)."""
from pathlib import Path
import argparse
import tempfile
import math
import os

HERE = Path(__file__).resolve().parent
CACHE = tempfile.TemporaryDirectory(prefix='local-tree-figure-')
os.environ['MPLCONFIGDIR'] = CACHE.name
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=HERE.parents[1] / 'figures')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

REG = FontProperties(fname=str(HERE / 'fonts/DejaVuSans.ttf'))
BOLD = FontProperties(fname=str(HERE / 'fonts/DejaVuSans-Bold.ttf'))
plt.rcParams.update({'svg.fonttype': 'path', 'svg.hashsalt': 'local-tree-dirac-20261006'})
BLUE, RED, INK = '#2563a6', '#bd4949', '#233244'
fig, axes = plt.subplots(1, 3, figsize=(14.8, 6.4), gridspec_kw={'width_ratios': [1.06, 1, 1.1]})
fig.patch.set_facecolor('white')

def txt(ax, x, y, text, size=11, bold=False, color=INK, ha='center'):
    return ax.text(x, y, text, fontsize=size, fontproperties=BOLD if bold else REG,
                   color=color, ha=ha, va='center', transform=ax.transAxes, linespacing=1.35)

def arr(ax, start, end, color=INK):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=15,
                                linewidth=1.8, color=color, transform=ax.transAxes))

for ax in axes:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')

a = axes[0]
txt(a, .5, .96, 'A. Actual support movement', 13, True)
txt(a, .5, .86, 'Two disjoint lifted plaques in X\n(common source-column coordinates)', 10)
for y, col, title in [(.58, BLUE, 'vertex copy: W_a = a^-1 z(W)'), (.23, RED, 'edge copy: W_e = z(W)')]:
    a.add_patch(Rectangle((.13, y), .74, .17, fill=False, edgecolor=col,
                          linewidth=1.7, transform=a.transAxes))
    a.add_patch(Rectangle((.34, y+.045), .26, .07, color=col, alpha=.30,
                          transform=a.transAxes))
    txt(a, .5, y+.125, title, 10, color=col)
    txt(a, .5, y+.055, 'nonzero smooth support', 9)
arr(a, (.51, .58), (.51, .415))
txt(a, .79, .50, 'QM', 12, True)
txt(a, .5, .15, 'Q(delta_a) = edge {e,a}, based at e', 10)
txt(a, .5, .055, 'A finite-order differential expression\nkeeps its input support (LD.2–LD.4).', 10)

a = axes[1]
txt(a, .5, .96, 'B. Unbalanced normal volume', 13, True)
txt(a, .5, .86, 'SU(2) normal spinor: physical rank 2\nF2 tree: one vertex / two edge orbits', 10)
for sign, y, num, col in [('+', .69, 2, BLUE), ('−', .46, 4, RED)]:
    txt(a, .09, y, sign, 15, True, col)
    for k in range(num):
        a.add_patch(Circle((.27+.155*k, y), .051, facecolor=col, alpha=.75,
                           transform=a.transAxes))
    txt(a, .5, y-.105, f'normal-volume {sign} eigenspace: dimension {num}', 9)
txt(a, .5, .265, 'An invertible leaf Clifford matrix\nmust exchange these eigenspaces.', 11)
txt(a, .5, .15, '2 cannot equal 4', 14, True, RED)
txt(a, .5, .055, 'Any Hermitian elliptic extension fails too:\ndeterminant winding +1 (LD.16–LD.17).', 10)

a = axes[2]
txt(a, .5, .96, 'C. Balanced local oscillator', 13, True)
txt(a, .5, .86, 'One positive / one negative auxiliary copy\nphysical normal-volume dimensions: 2 and 2', 10)
for sign, x0, col in [('+', .16, BLUE), ('−', .65, RED)]:
    txt(a, x0-.045, .70, sign, 14, True, col)
    for k in range(2):
        a.add_patch(Circle((x0+.08+.11*k, .70), .041, facecolor=col,
                           alpha=.75, transform=a.transAxes))
arr(a, (.435, .70), (.59, .70))
txt(a, .5, .59, 'D = [[0, −d/dx+x], [d/dx+x, 0]]', 10)
xs = [-3.2 + 6.4*k/320 for k in range(321)]
ys = [math.pi**(-.25)*math.exp(-x*x/2) for x in xs]
plotx = [.12+.76*(x+3.2)/6.4 for x in xs]
ploty = [.24+.27*y/math.pi**(-.25) for y in ys]
a.plot(plotx, ploty, color=BLUE, linewidth=2.2, transform=a.transAxes)
a.plot([.10,.91],[.24,.24], color=INK, linewidth=.7, transform=a.transAxes)
for x in [-3,0,3]:
    pos=.12+.76*(x+3.2)/6.4
    a.plot([pos,pos],[.235,.245], color=INK, linewidth=.7, transform=a.transAxes)
    txt(a,pos,.21,str(x),9)
txt(a,.945,.24,'x',10)
txt(a,.5,.135,'Normalized kernel: pi^(-1/4) exp(−x²/2)',10)
txt(a,.5,.055,'Positive kernel dimension 1; negative 0.\nScalar index +1 (LD.18; Section 11E).',10)

fig.subplots_adjust(left=.03, right=.985, top=.93, bottom=.11, wspace=.19)
fig.text(.5,.985,'A tree completion and two tests for a local differential realization',
         ha='center',va='top',fontsize=16,fontproperties=BOLD,color=INK)
fig.text(.5,.018,'Plaques are schematic; all ranks, signs and the Gaussian are exact.  Original diagram: CC0-1.0; fonts retain their own notice.',
         ha='center',va='bottom',fontsize=9,fontproperties=REG,color=INK)
notice=(HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
png=args.output/'kt-local-tree-differential-obstruction.png'
svg=args.output/'kt-local-tree-differential-obstruction.svg'
fig.savefig(png,dpi=160,metadata={'Title':'Local tree differential obstruction','Description':notice})
fig.savefig(svg,metadata={'Date':'2026-10-06','Title':'Local tree differential obstruction',
                         'Description':notice,'Creator':'Original CC0 mathematical diagram'})
plt.close(fig)
print(f'Wrote {png.name} and {svg.name}')
CACHE.cleanup()

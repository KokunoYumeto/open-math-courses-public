"""CC0 1.0. Reproduce Figure PH.1; all plotted diagnostic values are exact."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none'})
fig = plt.figure(figsize=(12, 8), facecolor='white')
grid = fig.add_gridspec(2, 2, height_ratios=[1.12, 1], hspace=.30, wspace=.28)
top = fig.add_subplot(grid[0, :]); top.set_axis_off()
top.set_xlim(0, 1); top.set_ylim(0, 1)
blue = '#215a83'; green = '#247653'; red = '#a34531'
top.text(.5, .97, 'Physical compression at a fixed tower stage',
         ha='center', va='top', fontsize=16, weight='bold', color=blue)
top.text(.5, .85, r'Original trace $\tau$; $B_m=M^\prime\cap M_m$, '
         r'$D=(M^\prime\cap T)^\prime\cap T$', ha='center', fontsize=12)

def box(ax, xy, width, height, label, edge=blue):
    ax.add_patch(FancyBboxPatch(xy, width, height,
        boxstyle='round,pad=0.012', edgecolor=edge, facecolor='#f6f9fb', lw=1.5))
    ax.text(xy[0]+width/2, xy[1]+height/2, label,
            ha='center', va='center', fontsize=12, linespacing=1.45)

box(top, (.035, .53), .24, .19,
    '$H_l=L^2(M_l)$\ninput stage')
box(top, (.38, .53), .24, .19,
    '$L^2(T,\\tau)$\n$Q_m=E_{B_m^\\prime\\cap T}$')
box(top, (.725, .53), .24, .19,
    '$H_l=L^2(M_l)$\n$K_{l,m}=P_lQ_m|_{H_l}$')
for left, right in [(.275, .38), (.62, .725)]:
    top.add_patch(FancyArrowPatch((left+.009, .625), (right-.01, .625),
        arrowstyle='-|>', mutation_scale=17, lw=1.6, color=blue))
top.text(.327, .73, 'include', ha='center', fontsize=10)
top.text(.672, .73, '$P_l$', ha='center', fontsize=11)
top.text(.5, .38,
    r'$K_{l,m}\in\operatorname{End}_{M-M}(H_l)$: finite dimensional, '
    r'$K_{l,m}\downarrow K_l$ in operator norm',
    ha='center', fontsize=12, color=blue)
top.text(.5, .23,
    r'$L^2(D)\cap H_l=L^2(M)\quad\Longrightarrow\quad '
    r'g_l=1-\|K_l|_{H_l\ominus L^2(M)}\|>0$',
    ha='center', fontsize=13, color=green)
top.text(.5, .07,
    'PH.2–PH.6: each finite stage has a positive gap.  '
    'PH.8: the uniform-depth bound remains unproved.',
    ha='center', fontsize=11, color=red)

left = fig.add_subplot(grid[1, 0]); right = fig.add_subplot(grid[1, 1])
depths = list(range(1, 11))
log2_gaps = [-2*l for l in depths]
left.plot(depths, log2_gaps, marker='o', color=blue, lw=2, ms=5)
left.set_xticks([1, 2, 4, 6, 8, 10]); left.set_yticks([0, -4, -8, -12, -16, -20])
left.set_xlim(.6, 10.4); left.set_ylim(-21, 1)
left.set_xlabel('Finite cutoff $l$'); left.set_ylabel(r'$\log_2 g_l$')
left.set_title('Exact Hilbert-space diagnostic: $g_l=4^{-l}$', fontsize=12)
left.grid(color='#dce3e9', alpha=.85)
left.text(.06, .14, r'$V\cap H_l=\mathbb{C} e_0$ for every $l$'+'\n'
          r'$V\neq\mathbb{C} e_0$, yet $\bigcup_lH_l$ is dense',
          transform=left.transAxes, fontsize=11,
          bbox={'facecolor':'white', 'edgecolor':'#dce3e9', 'pad':6})

ns = list(range(1, 9)); weights = [float(Fraction(3, 4**n)) for n in ns]
right.bar(ns, weights, color=green, width=.65)
right.set_xticks(ns); right.set_xlabel('Coordinate $n$')
right.set_ylabel(r'$|\langle a,e_n\rangle|^2=3\,4^{-n}$')
right.set_ylim(0, .83); right.grid(axis='y', color='#dce3e9', alpha=.85)
right.set_axisbelow(True)
right.set_title(r'$V=\operatorname{span}\{e_0,a\}$, '
                r'$a=\sqrt{3}\sum_{n\geq1}2^{-n}e_n$', fontsize=12)
right.text(.25, .67, r'$\|a\|^2=1$'+'\n'
           r'$\|a-P_{H_l}a\|^2=4^{-l}$', transform=right.transAxes,
           fontsize=13, color=green,
           bbox={'facecolor':'white', 'edgecolor':'#dce3e9', 'pad':7})
fig.text(.5, .024,
    'Lower panels: Exercise PH.2, an abstract Hilbert-space example. '
    'These are not measured Jones-tower gaps or a subfactor counterexample.',
    ha='center', fontsize=10, color=red)
fig.subplots_adjust(left=.075, right=.97, top=.965, bottom=.13)
fig.savefig(HERE/'physical-haar-finite-stage-gaps-v26.png', dpi=160)
fig.savefig(HERE/'physical-haar-finite-stage-gaps-v26.svg')
fig.savefig(HERE/'physical-haar-finite-stage-gaps.pdf')
plt.close(fig)
(HERE/'physical-haar-finite-stage-data.json').write_text(json.dumps({
    'license':'CC0-1.0',
    'interpretation':'Abstract Hilbert-space diagnostic of Exercise PH.2, not a Jones tower.',
    'rows':[{'l':l,'gap':str(Fraction(1,4**l)),
             'compressed_eigenvalue':str(Fraction(4**l-1,4**l)),
             'log2_gap':-2*l} for l in depths],
    'coordinate_weights':[{'n':n,'squared_coefficient':str(Fraction(3,4**n))} for n in ns]
}, indent=2)+'\n',encoding='utf-8')
print(json.dumps({'png':'physical-haar-finite-stage-gaps-v26.png',
                  'svg':'physical-haar-finite-stage-gaps-v26.svg',
                  'pdf':'physical-haar-finite-stage-gaps.pdf',
                  'diagnostic_points':len(depths)}))

"""Original, deterministic 2D illustration of OC.3 and OC.9--OC.20.

No external TeX, no source-book images, no global matplotlib cache writes.
Run with the existing miniconda Python (matplotlib and numpy installed).
"""
from pathlib import Path
import os

HERE = Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR'] = str(HERE / '.mplconfig')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'text.usetex':False,'svg.hashsalt':'OA-MOD-OC-022','savefig.facecolor':'white'})
fig = plt.figure(figsize=(15, 9), facecolor='white')
gs = fig.add_gridspec(2, 2, height_ratios=[1.05, .52], width_ratios=[1, 1.35],
                      hspace=.36, wspace=.3)
ax = fig.add_subplot(gs[0, 0])
x = np.geomspace(.006, 2, 1800)
exact = 2*np.sin(np.minimum(np.abs(np.log(x)), np.pi/2))
bound = 4*np.abs(x-1)
ax.plot(x, bound, color='#6e7785', lw=2.4, label=r'Proved bound $4|x-1|$')
ax.plot(x, exact, color='#136f9e', lw=2.4,
        label=r'Exact supremum for $x>0$')
ax.scatter([0], [1], s=66, color='#b44632', zorder=5)
ax.scatter([0], [2], s=56, facecolors='white', edgecolors='#136f9e', zorder=5)
ax.annotate('Kernel convention:\nvalue 1 at x = 0', xy=(0, 1), xytext=(.26, .58),
            fontsize=10, color='#9b3525',
            arrowprops={'arrowstyle':'->','color':'#9b3525'})
ax.axvline(.5, color='#bec3ca', linestyle=':', lw=1)
ax.text(.52, 3.22, 'proof splits at x = 1/2', fontsize=9, color='#596271')
ax.set(xlim=(-.045, 2.02), ylim=(-.1, 4.2),
       xlabel=r'$x=\sqrt{\lambda}$', ylabel='Scalar error',
       title='Spectral control, T = 1 (OC.3)')
ax.grid(alpha=.18)
ax.legend(loc='upper center', fontsize=9, framealpha=1)

flow = fig.add_subplot(gs[0, 1]); flow.axis('off')
flow.set(xlim=(0, 1), ylim=(0, 1))
flow.set_title('Proof mechanism for any directed net', pad=15)
boxes = [
    (.83, r'$\delta_{ij}=\|\omega_j\circ\alpha_i^{-1}-\omega_j\|\to0$',
     'Predual norm; each fixed finite state summand'),
    (.61, r'$\|(A_{ij}^{1/2}-1)\xi_j\|\leq\delta_{ij}^{1/2}$',
     'OC.9: the exact supported square-root identity'),
    (.39, r'$\mathrm{sup}_{|t|\leq T}\|q_{ij}C_i(t)\xi_j-\xi_j\|\leq e_{ij}$',
     r'OC.16: $e_{ij}=4\max(1,T)\delta_{ij}^{1/2}$'),
    (.17, r'$\mathrm{sup}_{|t|\leq T}\|(C_i(t)-1)\xi_j\|\leq e_{ij}+\sqrt{2e_{ij}}$',
     r'OC.17: unitarity, with $\|\xi_j\|=1$'),
]
for y, line, caption in boxes:
    flow.add_patch(FancyBboxPatch((.025, y-.075), .95, .15,
        boxstyle='round,pad=0.012', edgecolor='#a6bdcc', facecolor='#f1f7fa', lw=1))
    flow.text(.5, y+.024, line, ha='center', va='center', fontsize=13)
    flow.text(.5, y-.031, caption, ha='center', va='center', fontsize=9.5, color='#435766')
for y in [.72,.50,.28]:
    flow.add_patch(FancyArrowPatch((.5,y+.018),(.5,y-.025),
        arrowstyle='-|>',mutation_scale=14,color='#536a7c',lw=1.5))

notes = fig.add_subplot(gs[1, :]); notes.axis('off')
notes.text(0, .94,
    r'$\theta=\sum_{j\in I}\omega_j,\quad p_j=s(\omega_j),\quad'
    r'\sum_jp_j=1,\quad \xi_j=\Lambda_\theta(p_j),\quad q_{ij}=\alpha_i(p_j)$',
    fontsize=14, va='top')
notes.text(0, .67,
    'The index set I may be uncountable. The state supports are orthogonal.\n'
    'The spatial derivative uses the fixed commutant reference: '
    r'$A_{ij}=d(\omega_j\circ\alpha_i^{-1})/d\theta^{\mathrm{opp}}$.'
    '\nHere '+r'$C_i(t)=[D(\theta\circ\alpha_i^{-1}):D\theta]_t\in\mathcal{U}(M)$'+'.',
    fontsize=11, va='top', linespacing=1.65)
notes.text(0, .16,
    r'$\overline{\operatorname{span}}\{M^{\prime}\xi_j:j\in I\}=H$'
    '  +  uniform norm bound 2  '+r'$\Longrightarrow$'
    '  all test vectors (OC.18).\n'
    'Faithful chain rule and naturality transfer to any n.s.f. reference '
    'and any limit automorphism (OC.19--OC.20).',
    fontsize=11, va='top', linespacing=1.6)
fig.suptitle('From finite positive functionals to general cocycle continuity',
             fontsize=19, x=.06, ha='left', y=.98)
fig.text(.06, .027,
    'Proof: OA-MOD-OC-03 through OA-MOD-OC-08. '
    'Antecedents: Takesaki II, IX.1/IX.3; Strătilă, 2nd ed., sections 3.11, 3.16, 7.3--7.7.',
    fontsize=8.5, color='#4c535e')
fig.subplots_adjust(left=.065, right=.97, bottom=.13, top=.88)
fig.savefig(HERE/'continuity-mechanism.png', dpi=150)
fig.savefig(HERE/'continuity-mechanism.svg', metadata={'Date':None})
plt.close(fig)
print('Created continuity-mechanism.png and continuity-mechanism.svg')

"""Reproduce exact wave-coefficient diagram and geometry; original work CC0."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.hashsalt': 'AN02-wave-torsion035', 'font.family': 'DejaVu Sans', 'font.size': 11})
import matplotlib.pyplot as plt
import numpy as np
HERE = Path(__file__).resolve().parent
(HERE / 'figures').mkdir(exist_ok=True)
def save(p, value):
    p.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
theta = np.linspace(0, 2 * np.pi, 401)
z3 = np.exp(1j * theta / 2)
phase = np.exp(1j * theta)
values = np.linspace(0, 2, 401)
fig, axes = plt.subplots(1, 3, figsize=(15, 5.2), dpi=160, gridspec_kw={'width_ratios': [1, 1, 1.05]})
fig.suptitle('The wave sphere: exact fiber retraction, antipodal seam, and integral torsion', fontsize=17, y=.98)
ax = axes[0]
ax.plot(values, np.sqrt(1 + values**2), color='#215d94', lw=2.4)
ax.scatter([0, 2], [1, np.sqrt(5)], color=['#3c7c47', '#8e4492'], s=45, zorder=3)
ax.annotate('contract b to zero', xy=(.55, np.sqrt(1 + .55**2)), xytext=(.75, 2.03), arrowprops={'arrowstyle': '->', 'color': '#3c7c47'}, color='#3c7c47')
ax.text(.1, 2.35, 'v = i a e1 + sqrt(1+a^2) e3\nq(v) = 1,  a from 2 to 0', fontsize=10)
ax.set(xlabel='Im v1 = a', ylabel='Re v3 = sqrt(1+a^2)', xlim=(-.12, 2.2), ylim=(.82, 2.64), title='An exact coordinate section of Q')
ax.grid(alpha=.2)
ax = axes[1]
ax.plot(phase.real, phase.imag, lw=2.3, color='#215d94', label='q = exp(i theta)')
ax.plot(z3.real, z3.imag, lw=3, color='#8e4492', linestyle='--', label='z3 = exp(i theta/2)')
ax.scatter([1, -1], [0, 0], c=['#3c7c47', '#b84a38'], s=45, zorder=4)
ax.annotate('u=e3 at theta=0', (1, 0), xytext=(.12, -.42), arrowprops={'arrowstyle': '->'}, fontsize=10)
ax.annotate('-u at theta=2pi', (-1, 0), xytext=(-1.02, 1.13), arrowprops={'arrowstyle': '->'}, fontsize=10)
ax.annotate('', xy=(np.cos(.9), np.sin(.9)), xytext=(np.cos(.65), np.sin(.65)), arrowprops={'arrowstyle': '->', 'color': '#215d94'})
ax.set(xlim=(-1.3, 1.3), ylim=(-1.25, 1.5), aspect='equal', xlabel='real part', ylabel='imaginary part', title='One base turn flips the sphere')
ax.axhline(0, color='.7', lw=.7)
ax.axvline(0, color='.7', lw=.7)
ax.legend(loc='lower center', fontsize=9)
ax = axes[2]
ax.axis('off')
ax.set_title('The actual integer quotient', pad=14)
ax.text(.06, .86, 'Two intersection sphere generators', fontsize=11)
ax.text(.06, .75, 'D = [[ 1, 1],\n     [-1, 1]]', family='DejaVu Sans Mono', fontsize=14)
ax.text(.06, .52, 'relations: eA - eB = 0\n           eA + eB = 0', family='DejaVu Sans Mono', fontsize=11)
ax.text(.06, .32, 'H2(M; Z) = Z/2Z', fontsize=15, color='#215d94')
ax.text(.06, .19, '[sphere] = eA is nonzero\n2 [sphere] = 0', fontsize=12, color='#b84a38')
ax.text(.06, .055, 'Over Q, R or C: det D = 2 is invertible.\nThe same sphere bounds there.', fontsize=10, color='#3c7c47')
fig.subplots_adjust(left=.06, right=.985, top=.82, bottom=.15, wspace=.37)
fig.text(.5, .025, 'The first two panels are exact coordinate sections, not a drawing of all six real dimensions. See WT4-WT20.', ha='center', fontsize=10)
fig.savefig(HERE / 'figures/wave-cycle-torsion.png')
fig.savefig(HERE / 'figures/wave-cycle-torsion.svg', metadata={'Date': None})
plt.close(fig)
save(HERE / 'figures/geometry.json', {'polynomial': 'q(z)=z1^2+z2^2+z3^2', 'fiber': 'q=1', 'fiber_section': {'u': [0, 0, 1], 'b': 'a*e1', 'a_range': [0, 2]}, 'phase_range': [0, '2*pi'], 'base': 'exp(i*theta)', 'complex_section': 'exp(i*theta/2)*e3', 'seam': '(u,2*pi)=(-u,0)', 'integer_matrix': [[1, 1], [-1, 1]], 'left_unimodular_matrix': [[1, 0], [1, 1]], 'right_unimodular_matrix': [[1, -1], [0, 1]], 'smith_diagonal': [1, 2], 'sphere_target_generator': [1, 0], 'actual_integer_sphere_class': 'nonzero of exact order2', 'not_a_plot_proof': True})
print('Wrote figures/wave-cycle-torsion.png, wave-cycle-torsion.svg and geometry.json')

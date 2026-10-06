"""Original faithful-state core illustration. CC0-1.0; dependencies retain their terms."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='oa-flow-faithful-state-core-v1'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

directory = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13, 'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none'})
figure, (maps, spectrum) = plt.subplots(1, 2, figsize=(15.2, 6.6), gridspec_kw={'width_ratios': [1.45, 1]}, constrained_layout=True)
figure.patch.set_facecolor('#fbfcff')
for axis in (maps, spectrum):
    axis.set_facecolor('#fbfcff')
maps.set_xlim(0, 1)
maps.set_ylim(0, 1)
maps.axis('off')
maps.set_title('Whole-cone averaging and trace cutoffs', loc='left', fontsize=17, pad=18, color='#162b45')

def box(x, y, width, height, label, color='#eaf0f8'):
    maps.add_patch(FancyBboxPatch((x, y), width, height, boxstyle='round,pad=0.009,rounding_size=0.012', facecolor=color, edgecolor='#647895', linewidth=1.2))
    maps.text(x + width / 2, y + height / 2, label, ha='center', va='center', fontsize=14, color='#162b45')

def arrow(start, end, label, offset=0.05, size=13):
    maps.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=15, linewidth=1.6, color='#375e8b'))
    maps.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + offset, label, ha='center', va='center', fontsize=size, color='#162b45')

box(0.02, 0.68, 0.14, 0.13, r'$C_+$')
box(0.37, 0.68, 0.23, 0.13, r'$\widehat{\pi(M)}_+$')
box(0.80, 0.68, 0.17, 0.13, r'$[0,\infty]$')
arrow((0.17, 0.745), (0.36, 0.745), r'$\mathcal{P}$')
arrow((0.61, 0.745), (0.79, 0.745), r'$\widehat{\varphi}\circ\pi^{-1}$', size=12)
maps.text(0.48, 0.59, r'$\Phi=\widehat{\varphi}\circ\pi^{-1}\circ\mathcal{P}$', ha='center', fontsize=16, color='#162b45')
maps.text(0.48, 0.53, 'Forms include a possible infinite spectral part (FS-16, FS-17).', ha='center', fontsize=11, color='#506176')

box(0.02, 0.31, 0.14, 0.13, r'$C_+$')
box(0.40, 0.31, 0.15, 0.13, r'$C_+$')
box(0.80, 0.31, 0.17, 0.13, r'$[0,\infty)$', '#e4f4ee')
arrow((0.17, 0.375), (0.39, 0.375), r'$a\mapsto b_jab_j$', size=12)
arrow((0.56, 0.375), (0.79, 0.375), r'$\Phi$')
maps.text(0.48, 0.235, r'$b_j=e^{-P/2}1_{[-j,j]}(P),\quad F_j(a)=\Phi(b_jab_j)$', ha='center', fontsize=14, color='#162b45')
maps.text(0.48, 0.17, r'$F_j(a)\ \uparrow\ \tau(a)$', ha='center', fontsize=18, color='#1f7157')
maps.text(0.48, 0.095, 'Each Fj is finite; the supremum may be infinite (FS-20, FS-25).', ha='center', fontsize=11, color='#506176')
maps.text(0.48, 0.035, 'The arrows describe maps and scalar limits, not operator-order claims.', ha='center', fontsize=11, color='#506176')

spectrum.set_title('The dual action shifts spectral intervals', loc='left', fontsize=17, pad=18, color='#162b45')
r = np.linspace(-0.3, 2.4, 700)
density = np.exp(-r) / (2 * np.pi)
spectrum.plot(r, density, color='#243e64', linewidth=2.4)
for start, end, color, label in [(0, 1, '#3f86b6', r'$I=[0,1]$'), (1, 2, '#b3762e', r'$I+1=[1,2]$')]:
    values = np.linspace(start, end, 250)
    spectrum.fill_between(values, 0, np.exp(-values) / (2 * np.pi), color=color, alpha=0.35, label=label)
    spectrum.axvline(start, color=color, linestyle=':', linewidth=1)
    spectrum.axvline(end, color=color, linestyle=':', linewidth=1)
spectrum.set_xlim(-0.3, 2.4)
spectrum.set_ylim(0, 0.28)
spectrum.set_xticks([0, 1, 2])
spectrum.set_xlabel(r'Spectral coordinate $r$ of $P$', fontsize=13)
spectrum.set_ylabel(r'Scalar density $e^{-r}/(2\pi)$', fontsize=13)
spectrum.spines[['top', 'right']].set_visible(False)
spectrum.grid(axis='y', alpha=0.13)
spectrum.legend(loc='upper right', frameon=False, fontsize=13)
spectrum.text(0.05, 0.98, r'$\theta_1(P)=P-1$', transform=spectrum.transAxes, va='top', fontsize=15, color='#162b45')
spectrum.text(0.05, 0.88, r'$\theta_1(e_I)=e_{I+1}$', transform=spectrum.transAxes, va='top', fontsize=15, color='#162b45')
spectrum.text(0.08, 0.50, r'$m(I)=\frac{1-e^{-1}}{2\pi}$', transform=spectrum.transAxes, fontsize=16, color='#285f87')
spectrum.text(0.08, 0.37, r'$m(I+1)=e^{-1}m(I)$', transform=spectrum.transAxes, fontsize=16, color='#8a541e')
spectrum.text(0.08, 0.18, r'$m(J)=\tau(e_J)$', transform=spectrum.transAxes, fontsize=15, color='#162b45')
spectrum.text(0.08, 0.09, 'Exact example of FS-06 and FS-30–FS-31.', transform=spectrum.transAxes, fontsize=11, color='#506176')

figure.savefig(directory / 'faithful-state-core-construction.png', dpi=170)
figure.savefig(directory / 'faithful-state-core-construction.svg', metadata={'Date':None, 'Creator':'OA-FLOW original core construction'})
import re
svg_path=directory/'faithful-state-core-construction.svg'
svg_path.write_bytes(re.sub(br'<!DOCTYPE[^>]*>\s*',b'',svg_path.read_bytes(),count=1))
plt.close(figure)
data = {
    'type': 'Expository map diagram and exact scalar spectral-measure example; not a numerical proof or a geometric model of M.',
    'domains_and_maps': ['Pcal:C_+ -> extended pi(M)_+', 'Phi=extended phi o pi^-1 o Pcal:C_+ -> [0,infinity]', 'F_j(a)=Phi(b_j a b_j):C_+ -> [0,infinity)', 'tau(a)=sup_j F_j(a)'],
    'interval': [0, 1],
    'dual_shift_s': 1,
    'shifted_interval': [1, 2],
    'spectral_density': 'exp(-r)/(2*pi)',
    'exact_interval_mass': '(1-exp(-1))/(2*pi)',
    'exact_shifted_mass': 'exp(-1)*(1-exp(-1))/(2*pi)',
    'proof_locators': ['FS-06', 'FS-16', 'FS-17', 'FS-20', 'FS-25', 'FS-30', 'FS-31']
}
(directory / 'FIGURE_BINDINGS.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print('Rendered reproducible PNG and SVG proof-mechanism illustration.')

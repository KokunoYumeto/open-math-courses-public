"""Exact directional/full-strength model figure; no constructed solution sampled."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'elementary-wave-directional-and-full-strength-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'A characteristic ray sees directional growth that full strength controls', fontsize=28, weight='bold', color='#132a38')
    fig.text(0.045, 0.91, 'Wave $P=\\xi_1^2+\\xi_2^2-\\xi_3^2$, $Q=\\xi_1$, $N=e_2$; comparison elliptic $P_{\\mathrm{e}}=|\\xi|^2+1$.', fontsize=21, color='#41505a')
    left = fig.add_axes([0.055, 0.355, 0.34, 0.445], facecolor='white')
    right = fig.add_axes([0.575, 0.355, 0.38, 0.445], facecolor='white')
    coord = np.linspace(-8, 8, 601)
    xx, zz = np.meshgrid(coord, coord)
    ratio = np.abs(xx) / np.sqrt((xx * xx - zz * zz) ** 2 + 4)
    mesh = left.pcolormesh(coord, coord, ratio, cmap='viridis', shading='nearest', vmin=0, vmax=4, rasterized=True)
    left.plot(coord, coord, color='white', ls='--', lw=2.4)
    left.plot(coord, -coord, color='white', ls='--', lw=2.4)
    left.set_aspect('equal')
    left.set_xlim(-8, 8)
    left.set_ylim(-8, 8)
    left.set_xlabel('$\\xi_1$')
    left.set_ylabel('$\\xi_3$')
    left.set_title('Exact directional ratio in $\\xi_2=0$', pad=22)
    cax = fig.add_axes([0.425, 0.355, 0.013, 0.445])
    bar = fig.colorbar(mesh, cax=cax)
    bar.set_label('$\\mathcal{S}_{e_2}Q/\\mathcal{S}_{e_2}P$', fontsize=19)
    tt = np.linspace(0.01, 32, 2001)
    wave = tt / 2
    full = np.sqrt(tt * tt + 1) / np.sqrt(8 * tt * tt + 12)
    elliptic = tt / np.sqrt((2 * tt * tt + 1) ** 2 + 4)
    right.semilogy(tt, wave, color='#167194', lw=3.5)
    right.semilogy(tt, full, color='#7954a1', ls='--', lw=3.5)
    right.semilogy(tt, elliptic, color='#ba5237', ls=':', lw=4)
    right.set_xlim(0, 32)
    right.set_ylim(0.003, 20)
    right.set_xticks([0, 8, 16, 24, 32])
    right.set_xlabel('Ray parameter $t>0$ at $(t,0,t)$')
    right.set_ylabel('Strength ratio (logarithmic vertical axis)')
    right.set_title('Exact ratios on the same real ray', pad=22)
    right.grid(color='#d7dedf', alpha=0.6, which='both')
    fig.text(0.05, 0.26, 'Dashed lines: $\\xi_3=\\pm\\xi_1$, where $P=0$.', fontsize=20, color='#132a38')
    fig.text(0.05, 0.205, 'On either ray, $\\mathcal{S}_{e_2}P=2$ exactly.', fontsize=20, color='#132a38')
    fig.text(0.05, 0.15, 'Thus $Q=\\xi_1$ grows while the denominator stays fixed.', fontsize=18.5, color='#41505a')
    fig.text(0.05, 0.09, 'The full strength still controls this lower-order perturbation.', fontsize=18.5, color='#41505a')
    for ypos, color, style, label in [(0.26, '#167194', '-', 'Wave directional: $t/2$'), (0.205, '#7954a1', '--', 'Wave full strength: $\\sqrt{t^2+1}/\\sqrt{8t^2+12}$'), (0.15, '#ba5237', ':', 'Elliptic directional: $t/\\sqrt{(2t^2+1)^2+4}$')]:
        fig.add_artist(Line2D([0.54, 0.57], [ypos + 0.003, ypos + 0.003], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.582, ypos, label, fontsize=20, color='#132a38')
    fig.text(0.54, 0.09, 'All plotted quantities are exact strength ratios; no solution is sampled.', fontsize=18.5, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (4)–(10), (23)–(26); Exercise 2. Exact directional and full strength ratios.', fontsize=15, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    metadata = {'schema': 'exact-wave-directional-full-strength-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(4)-(10)', '(23)-(26)', 'Exercise 2'], 'symbols': {'P': 'xi1^2+xi2^2-xi3^2', 'Q': 'xi1', 'N': [0, 1, 0], 'P_elliptic': 'xi1^2+xi2^2+xi3^2+1'}, 'left': {'slice': 'xi2=0', 'xi1_and_xi3_range': [-8, 8], 'sample_count_each_axis': 601, 'exact_ratio': 'abs(xi1)/sqrt((xi1^2-xi3^2)^2+4)', 'characteristic_lines': ['xi3=xi1', 'xi3=-xi1'], 'equal_euclidean_axes': True, 'colorbar_range': [0, 4]}, 'right': {'ray': '(t,0,t)', 'parameter_range': [0.01, 32], 'sample_count': 2001, 'vertical_axis': 'logarithmic', 'exact_ratios': {'wave_directional': 't/2', 'wave_full': 'sqrt(t^2+1)/sqrt(8*t^2+12)', 'elliptic_directional': 't/sqrt((2*t^2+1)^2+4)'}}, 'asymptotic_replacements_used_in_plots': False, 'constructed_solution_or_coefficient_sampled': False, 'sampled_values_replace_proof': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

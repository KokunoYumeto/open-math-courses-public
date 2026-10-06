"""Exact interval and nodal-division models; no assembled mode is sampled."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'neighbouring-mode-intervals-and-nodal-division-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21, 'legend.fontsize': 18})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'Neighbouring modes and division at a nodal Q-image', fontsize=30, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact interval geometry and an exact opposing-phase model; the unknown transport modes are not sampled.', fontsize=20, color='#41505a')
    left = fig.add_axes([0.07, 0.35, 0.4, 0.47], facecolor='white')
    right = fig.add_axes([0.56, 0.35, 0.39, 0.47], facecolor='white')
    q = 4
    w = 5
    d = 8 ** (-0.25)
    indices = np.arange(64, 69)
    delta = d * indices ** (-0.25)
    centre = delta[0]
    scale = centre ** 5
    data = []
    for index, dd in zip(indices, delta):
        y = 68 - index
        c = (dd - centre) / scale
        half = dd ** w / scale
        left.plot([c - 2 * half, c + 2 * half], [y, y], lw=20, color='#e1e6e4', solid_capstyle='butt')
        left.plot([c - 1.5 * half, c + 1.5 * half], [y, y], lw=11, color='#a7cbd5', solid_capstyle='butt')
        left.plot([c - 1.25 * half, c + 1.25 * half], [y, y], lw=5, color='#167194', solid_capstyle='butt')
        left.scatter([c], [y], color='#132a38', s=65, zorder=5)
        b = c - half
        if index < 68:
            left.plot([b, b], [y - 1, y], ls='--', color='#ba5237', lw=2)
            left.text(b + 0.1, y - 0.55, f'$B_{{{index}}}$', fontsize=17, color='#963d2c', va='center')
        data.append({'nu': int(index), 'delta_expression': f'8^(-1/4)*{index}^(-1/4)', 'centre_normalized': float(c), 'half_unit_normalized': float(half), 'B_normalized': float(b)})
    left.set_xlim(-9.7, 2.6)
    left.set_ylim(-0.55, 4.6)
    left.set_yticks(range(5), ['$\\nu=68$', '$\\nu=67$', '$\\nu=66$', '$\\nu=65$', '$\\nu=64$'])
    left.set_xlabel('Normal coordinate $(s-\\delta_{64})/\\delta_{64}^{5}$')
    left.set_title('Exact geometry: $q=4,\\quad w=5$', pad=20)
    left.grid(axis='x', color='#d7dedf', alpha=0.6)
    h = np.linspace(0, 2, 501)
    modulus = -np.expm1(-h)
    bound = (1 - np.exp(-1)) * np.minimum(1, h)
    quotient = np.zeros_like(h)
    mask = h > 0
    quotient[mask] = np.exp(-1 / h[mask] ** 2) / (2 * np.sinh(h[mask] / 2))
    right.plot(h, modulus, lw=4, color='#167194')
    right.plot(h, bound, lw=4, color='#7954a1', ls='--')
    right.plot(h, quotient, lw=4, color='#ba5237', ls=':')
    right.scatter([0], [0], s=85, facecolors='#fbfaf6', edgecolors='#132a38', linewidths=2, zorder=5)
    right.set_xlim(0, 2)
    right.set_ylim(-0.035, 0.94)
    right.set_xlabel('Distance $|h|$ in the exact model, $T=1$')
    right.set_ylabel('Dimensionless model quantity')
    right.set_title('A zero denominator with a flat quotient', pad=20)
    right.grid(color='#d7dedf', alpha=0.6)
    for y, color, lw, label in [(0.238, '#e1e6e4', 10, 'Mode interval: $|S|\\leq2$'), (0.183, '#a7cbd5', 7, 'Cutoff support: $|S|<3/2$'), (0.128, '#167194', 4, 'Plateau: $\\chi=1$ for $|S|\\leq5/4$')]:
        fig.add_artist(Line2D([0.05, 0.082], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=lw))
        fig.text(0.095, y, label, fontsize=21, color='#132a38')
    fig.text(0.05, 0.074, 'Dots: centres. Dashed vertical segments: matching planes $B_\\nu$.', fontsize=18, color='#41505a')
    for y, color, style, label in [(0.238, '#167194', '-', 'Normalized Q-image modulus $1-e^{-|h|}$'), (0.183, '#7954a1', '--', 'Lower bound $(1-e^{-1})\\min(1,|h|)$'), (0.128, '#ba5237', ':', 'Flat quotient modulus $e^{-1/h^2}/[2\\sinh(|h|/2)]$')]:
        fig.add_artist(Line2D([0.54, 0.572], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.585, y, label, fontsize=20, color='#132a38')
    fig.text(0.54, 0.074, 'At h=0 the Q-images cancel; the extended quotient has every jet zero.', fontsize=18, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (5)–(7), (20)–(23); Exercise 3. Exact interval and nodal-division models.', fontsize=14, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    metadata = {'schema': 'exact-neighbour-intervals-and-nodal-division-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(5)-(7)', '(20)-(23)', 'Exercise 3'], 'interval_panel': {'q': q, 'w': w, 'gamma': '1/4', 'd': '8^(-1/4)', 'nu': [64, 65, 66, 67, 68], 'coordinate': '(s-delta64)/delta64^5', 'intervals': data, 'switches': 'Bnu=delta_nu-delta_nu^5'}, 'division_panel': {'h_domain': [0, 2], 'T': 1, 'sample_count': 501, 'opposing_Q_images': ['exp(h/2)', '-exp(-h/2)'], 'normalized_modulus': '1-exp(-abs(h))', 'lower_bound': '(1-exp(-1))*min(1,abs(h))', 'flat_quotient_modulus': 'exp(-1/h^2)/(2*sinh(abs(h)/2))', 'quotient_at0': 0, 'quotient_every_jet_at0': 0, 'toy_model_is_not_the_assembled_solution': True}, 'finite_parameter_transport_phase_sampled': False, 'physical_space_solution_sampled': False, 'periodic_seed_constructed': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

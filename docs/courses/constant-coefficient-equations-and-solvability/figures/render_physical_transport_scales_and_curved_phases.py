"""Exact physical-scale and limiting-phase data; no finite mode is sampled."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'physical-transport-scales-and-phase-curvature-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 20, 'svg.hashsalt': STEM, 'axes.titlesize': 24, 'axes.labelsize': 22, 'legend.fontsize': 19})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'Physical transport scales and the phase curvature', fontsize=31, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact rational scale model and exact zero-parameter phase; the full carrier-weighted mode is not sampled.', fontsize=20, color='#41505a')
    left = fig.add_axes([0.08, 0.35, 0.395, 0.47], facecolor='white')
    right = fig.add_axes([0.56, 0.35, 0.39, 0.47], facecolor='white')
    delta = np.geomspace(0.25, 0.5, 257)
    left.loglog(delta, 2 * delta ** 19, lw=4, color='#167194', ls='-')
    left.loglog(delta, delta ** 22, lw=4, color='#7954a1', ls='--')
    left.loglog(delta, delta ** 32 / (1 - delta ** 8), lw=4, color='#ba5237', ls=':')
    left.set_xlim(0.25, 0.5)
    left.set_ylim(1e-20, 1e-05)
    left.set_xlabel('Positive parameter $\\delta$')
    left.set_ylabel('Length in the physical normal coordinate')
    left.set_title('Physical lengths: $p=2,\\quad w=19$', pad=20)
    left.grid(True, which='both', color='#d7dedf', alpha=0.65)
    left.set_xticks([0.25, 0.3, 0.4, 0.5], ['0.25', '0.30', '0.40', '0.50'])
    left.tick_params(axis='x', which='minor', labelbottom=False)
    s = np.linspace(-2, 2, 501)
    right.plot(s, s * s / 3, lw=4, color='#167194', ls='-')
    right.plot(s, 2 * s / 3, lw=4, color='#7954a1', ls='--')
    right.axhline(0, color='#8c979b', lw=1.2)
    right.axvline(0, color='#d7dedf', lw=1.2)
    right.set_xlim(-2, 2)
    right.set_ylim(-1.55, 1.55)
    right.set_xlabel('Rescaled normal coordinate $S$')
    right.set_ylabel('Imaginary part')
    right.set_title('Phase and derivative on $\\delta=0$', pad=20)
    right.grid(True, color='#d7dedf', alpha=0.65)
    for y, color, style, text in [(0.235, '#167194', '-', 'Patch half-width $2\\delta^{19}$'), (0.179, '#7954a1', '--', 'Normal frequency length $1/T=\\delta^{22}$'), (0.123, '#ba5237', ':', 'Carrier growth length $1/\\lambda=\\delta^{32}/(1-\\delta^8)$')]:
        fig.add_artist(Line2D([0.06, 0.088], [y + 0.005, y + 0.005], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.1, y, text, fontsize=21, color='#132a38')
    for y, color, style, text in [(0.235, '#167194', '-', '$\\operatorname{Im}\\phi_0=S^2/3$'), (0.179, '#7954a1', '--', "$\\operatorname{Im}\\phi'_0=2S/3$")]:
        fig.add_artist(Line2D([0.55, 0.578], [y + 0.005, y + 0.005], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.59, y, text, fontsize=22, color='#132a38')
    fig.text(0.55, 0.122, '$\\phi_0=\\dfrac{p j_0S^2}{2a},\\quad a=-24-24i,\\quad j_0=16$', fontsize=21, color='#132a38')
    fig.text(0.55, 0.074, "$\\operatorname{Im}\\phi''_0=2/3>0,\\quad\\mu=\\delta^3$", fontsize=20, color='#132a38')
    fig.text(0.045, 0.035, 'Equations (4), (12)–(14), (21)–(22). Exact scales and limiting phase; no finite mode is sampled.', fontsize=14, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    data = {'schema': 'exact-physical-transport-scales-and-limiting-phase-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(4)', '(12)-(14)', '(21)-(22)'], 'parameters': {'p': 2, 'kappa': 9, 'tau': 11, 'Lambda': 16, 'j0': 16, 'a': [-24, -24], 'N': [0, 1], 'w': 19, 'm0': 3}, 'length_panel': {'delta_domain': ['1/4', '1/2'], 'logarithmic_sample_count': 257, 'physical_normal_coordinate': 't=x2', 'patch_half_width': '2*delta^19', 'normal_frequency_length': 'delta^22', 'carrier_growth_length': 'delta^32/(1-delta^8)', 'normal_frequency_length_is_not_asserted_local_wavelength_at_zero_phase_derivative': True}, 'phase_panel': {'S_domain': [-2, 2], 'sample_count': 501, 'phi0': '-(1-i)*S^2/3', 'Im_phi0': 'S^2/3', 'Im_phi0_derivative': '2*S/3', 'Im_phi0_second_derivative': '2/3', 'mu': 'delta^3', 'curves_are_at_parameter0_only': True, 'parameter_power_factor_retained': True}, 'highest_operator_coefficient': 'delta^27/(1-8*i*delta^16)', 'Q_image_factor': 'delta^-192', 'finite_parameter_phase_or_amplitude_sampled': False, 'full_carrier_weighted_mode_sampled': False, 'physical_space_solution_sampled': False, 'periodic_seed_constructed': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

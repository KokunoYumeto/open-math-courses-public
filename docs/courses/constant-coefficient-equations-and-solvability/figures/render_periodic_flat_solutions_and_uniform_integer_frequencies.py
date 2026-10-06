"""Exact integer rounding and coefficient-error terms, not a sampled seed."""
import argparse, hashlib, json, math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'uniform-periodic-rounding-and-coefficient-errors-025'
SAMPLES = [(2, 5), (3, 8), (4, 11), (5, 13), (6, 17), (7, 19), (8, 23), (9, 25)]

def rounding_sample(num, den, index):
    eps = Fraction(num, den)
    xi1 = eps ** (-45)
    k1 = (2 * xi1.numerator + xi1.denominator) // (2 * xi1.denominator)
    alpha1 = Fraction(k1) - xi1
    xi2_squared = (1 - eps ** 6) * eps ** (-96)
    floor2 = math.isqrt(xi2_squared.numerator // xi2_squared.denominator)
    k2 = floor2 + int(4 * xi2_squared.numerator > xi2_squared.denominator * (2 * floor2 + 1) ** 2)
    assert abs(alpha1) <= Fraction(1, 2)
    assert (2 * k2 - 1) ** 2 * xi2_squared.denominator <= 4 * xi2_squared.numerator <= (2 * k2 + 1) ** 2 * xi2_squared.denominator
    with localcontext() as context:
        context.prec = 150
        exact_decimal = (Decimal(xi2_squared.numerator) / Decimal(xi2_squared.denominator)).sqrt()
        alpha2 = Decimal(k2) - exact_decimal
        alpha2_display = format(alpha2, '.60f')
    return {'sample': index, 'epsilon': str(eps), 'xi1': str(xi1), 'xi2_squared': str(xi2_squared), 'k1': str(k1), 'k2': str(k2), 'alpha1': str(alpha1), 'alpha2_exact_expression': f'{k2}-sqrt({xi2_squared})', 'alpha2_decimal': alpha2_display, 'decimal_precision': 150, 'nearest_integer_choice_certified_by_exact_rational_inequalities': True, 'alpha1_float': float(alpha1), 'alpha2_float': float(alpha2)}

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21, 'legend.fontsize': 18})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'Integer rounding and the weighted coefficient errors', fontsize=30, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact frequency samples and selected exact error terms; no constructed transport mode is sampled.', fontsize=20, color='#41505a')
    left = fig.add_axes([0.09, 0.35, 0.37, 0.47], facecolor='white')
    right = fig.add_axes([0.56, 0.35, 0.39, 0.47], facecolor='white')
    samples = [rounding_sample(n, d, i + 1) for i, (n, d) in enumerate(SAMPLES)]
    left.plot([-0.5, 0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, 0.5, -0.5], color='#7954a1', ls='--', lw=3)
    left.axhline(0, color='#d7dedf', lw=1.2)
    left.axvline(0, color='#d7dedf', lw=1.2)
    for sample in samples:
        x = sample['alpha1_float']
        y = sample['alpha2_float']
        left.scatter([x], [y], s=105, color='#167194', zorder=4)
        dx = -0.045 if x > 0.38 else 0.026
        dy = -0.045 if y > 0.38 else 0.026
        left.text(x + dx, y + dy, str(sample['sample']), fontsize=19, color='#132a38', va='top' if dy < 0 else 'bottom', ha='right' if dx < 0 else 'left')
    left.set_xlim(-0.57, 0.57)
    left.set_ylim(-0.57, 0.57)
    left.set_aspect('equal', adjustable='box')
    left.set_xlabel('First residual $\\alpha_1=k_1-\\xi_1$')
    left.set_ylabel('Second residual $\\alpha_2=k_2-\\xi_2$')
    left.set_title('Every choice lies in $[-1/2,1/2]^2$', pad=20)
    left.set_xticks([-0.5, -0.25, 0, 0.25, 0.5])
    left.set_yticks([-0.5, -0.25, 0, 0.25, 0.5])
    left.grid(color='#d7dedf', alpha=0.6)
    eps = np.geomspace(0.2, 0.5, 257)
    U = 1 - eps ** 20 / 32 - eps ** 36 / 512 - eps ** 52 / 32768
    B = 1 + 2 * eps ** 6 + 3 * eps ** 12 + 4 * eps ** 18 + 5 * eps ** 24
    R = np.sqrt(1 - eps ** 6)
    right.loglog(eps, 6 * eps ** 9 - 5 * eps ** 15, color='#167194', lw=4)
    right.loglog(eps, 2 * eps ** 24 / U, color='#7954a1', lw=4, ls='--')
    right.loglog(eps, 2 * B * R ** 3 * eps ** 27, color='#ba5237', lw=4, ls=':')
    right.set_xlim(0.2, 0.5)
    right.set_ylim(1e-20, 0.04)
    right.set_xlabel('Small frequency parameter $\\varepsilon$')
    right.set_ylabel('Magnitude of selected exact term')
    right.set_title('Terms in the weighted coefficient errors', pad=20)
    right.grid(True, which='both', color='#d7dedf', alpha=0.6)
    right.set_xticks([0.2, 0.25, 0.3, 0.4, 0.5], ['0.20', '0.25', '0.30', '0.40', '0.50'])
    right.tick_params(axis='x', which='minor', labelbottom=False)
    fig.text(0.07, 0.238, 'Samples 1–4:  2/5, 3/8, 4/11, 5/13', fontsize=21, color='#132a38')
    fig.text(0.07, 0.183, 'Samples 5–8:  6/17, 7/19, 8/23, 9/25', fontsize=21, color='#132a38')
    fig.text(0.07, 0.128, 'Nearest integers are certified with rational inequalities.', fontsize=18, color='#41505a')
    fig.text(0.07, 0.074, 'The compact parameter square includes discontinuous rounding choices.', fontsize=18, color='#41505a')
    for y, color, style, label in [(0.238, '#167194', '-', 'Full scalar-normalization error $6\\varepsilon^9-5\\varepsilon^{15}$'), (0.183, '#7954a1', '--', 'First P-rounding term $2\\varepsilon^{24}/U$'), (0.128, '#ba5237', ':', 'First Q-rounding term $2B_4R^3\\varepsilon^{27}$')]:
        fig.add_artist(Line2D([0.54, 0.572], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.585, y, label, fontsize=20, color='#132a38')
    fig.text(0.54, 0.074, 'P and Q curves are selected monomials, not full-error bounds.', fontsize=18, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (7), (11)–(12), (23). Exact integer samples and selected coefficient-error terms.', fontsize=14, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    meta = {'schema': 'exact-periodic-rounding-and-weighted-error-terms-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(7)', '(11)-(12)', '(23)'], 'rounding_samples': samples, 'rounding_panel': {'parameter_square': [[-0.5, 0.5], [-0.5, 0.5]], 'sample_frequencies_are_not_claimed_to_be_the_actual_mode_assembly_sequence': True}, 'error_panel': {'epsilon_domain': ['1/5', '1/2'], 'sample_count': 257, 'full_scalar_normalization_error': '6*epsilon^9-5*epsilon^15', 'first_P_rounding_monomial_magnitude': '2*epsilon^24/U(epsilon)', 'first_Q_rounding_monomial_magnitude': '2*B4(epsilon)*R(epsilon)^3*epsilon^27', 'P_Q_curves_are_complete_error_bounds': False, 'rounding_monomials_use_abs_alpha': '1/2'}, 'actual_transport_phase_sampled': False, 'actual_amplitude_sampled': False, 'physical_space_solution_sampled': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200], 'exact_rounding_samples': 8}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

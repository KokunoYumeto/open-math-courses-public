"""Exact toy slope and dominance geometry for the real-frequency construction draft."""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'real-frequency-slope-profile-and-dominance-025'

def smooth_step(y):
    a = np.zeros_like(y, dtype=float)
    b = np.zeros_like(y, dtype=float)
    mask = y > 0
    a[mask] = np.exp(-1 / y[mask])
    mask = y < 1
    b[mask] = np.exp(-1 / (1 - y[mask]))
    return a / (a + b)

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'Real-frequency modes: a deep phase well and an exact switch', fontsize=29, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact toy $P=\\xi_2^2+\\xi_1$, $Q=\\xi_1^2$, $\\xi(t)=(t^3,0)$; $\\kappa=2$, $\\gamma=1$, mode $\\nu=16$.', fontsize=21, color='#41505a')
    left = fig.add_axes([0.07, 0.37, 0.4, 0.45], facecolor='white')
    right = fig.add_axes([0.56, 0.37, 0.39, 0.45], facecolor='white')
    nu = 16
    B = 3
    M = 52
    A0 = 480
    join = (1 / nu + 1 / (nu + 1)) / 2
    upper = (1 / (nu - 1) + 1 / nu) / 2
    ell = 1 / (nu * nu - 1)
    rho = 1 / (16 * nu * nu)
    rho_upper = 1 / (16 * (nu - 1) ** 2)
    y = np.linspace(0, 1, 1001)
    s = join + ell * y
    ll = 1 - smooth_step((s - join - 4 * rho) / (2 * rho))
    rr = smooth_step((s - upper + 6 * rho_upper) / (2 * rho_upper))
    sigma_plus = math.sqrt(4 - 7 / (2 * 2 ** (nu - 1)))
    psi = ll * 1j + rr * 1j * sigma_plus + (1 - ll - rr) * (1 - 1j * A0)
    left.plot(y, psi.imag, lw=4, color='#167194')
    left.axhline(0, color='#a7afb2', lw=1)
    middle_left = 6 * rho / ell
    middle_right = 1 - 6 * rho_upper / ell
    left.axvspan(middle_left, middle_right, color='#d9ebe6', alpha=0.6)
    left.text(0.45, -380, '$1-480i$', fontsize=23, color='#132a38', ha='center')
    left.set_xlim(0, 1)
    left.set_ylim(-515, 40)
    left.set_xlabel('Normal position $(s-B_{16})/\\ell_{16}$')
    left.set_ylabel('Imaginary slope $\\operatorname{Im}\\psi_{16}$')
    left.set_title('Positive join slopes, negative mean', pad=20)
    left.grid(color='#d7dedf', alpha=0.6)
    zoom = left.inset_axes([0.38, 0.6, 0.2, 0.3])
    zoom.plot([0, 1], [1, sigma_plus], color='#132a38', marker='o', lw=0, markersize=7)
    zoom.set_xlim(-0.2, 1.2)
    zoom.set_ylim(0.7, 2.3)
    zoom.set_xticks([0, 1], ['lower', 'upper'])
    zoom.set_yticks([1, 2])
    zoom.set_title('Join values', fontsize=15)
    zoom.tick_params(labelsize=13)
    zoom.grid(color='#d7dedf', alpha=0.6)
    h = np.linspace(-1, 1, 501)
    right.axvspan(-0.5, 0.5, color='#d9ebe6', alpha=0.7)
    right.axvspan(-1, -0.5, color='#f6e3d8', alpha=0.7)
    right.axvspan(0.5, 1, color='#f6e3d8', alpha=0.7)
    right.plot(h, -h, lw=4, color='#7954a1')
    right.axhline(0, color='#a7afb2', lw=1)
    right.scatter([0], [0], s=80, color='#132a38', zorder=5)
    right.set_xlim(-1, 1)
    right.set_ylim(-1.14, 1.14)
    right.set_xlabel('Join distance $h=(s-B_{16})/\\rho_{16}$')
    right.set_ylabel('$\\log|U_{17}/U_{16}|/(\\Lambda_{16}\\rho_{16})$')
    right.set_title('The exact logarithmic magnitude ratio', pad=20)
    right.text(-0.67, 1.02, 'U17 larger', fontsize=19, color='#132a38', ha='center')
    right.text(0.67, -1.04, 'U16 larger', fontsize=19, color='#132a38', ha='center')
    right.grid(color='#d7dedf', alpha=0.6)
    sigma_next = math.sqrt(4 - 7 / (2 * 2 ** nu))
    T = 2 ** (2 * nu)
    lambda_rho = T * (4 * sigma_next - 1) * rho
    fig.add_artist(Line2D([0.05, 0.082], [0.267, 0.267], transform=fig.transFigure, color='#167194', lw=3.5))
    fig.text(0.095, 0.263, 'Complete smooth profile from (10)–(14)', fontsize=21, color='#132a38')
    fig.text(0.05, 0.206, '$B=3$, $M=52$, $A_0=480$; $A_0>8(M+2B)=464$.', fontsize=19, color='#132a38')
    fig.text(0.05, 0.151, 'Middle plateau has positive real part 1 and negative imaginary part.', fontsize=18, color='#41505a')
    fig.text(0.05, 0.092, 'Endpoint markers are magnified in the inset; the profile misses 0.', fontsize=18, color='#41505a')
    fig.text(0.54, 0.263, 'Green strip: both cutoffs equal 1; exact coefficient $-r_{16}$.', fontsize=19, color='#132a38')
    fig.text(0.54, 0.206, 'Orange strips: the smaller mode is being cut off.', fontsize=19, color='#132a38')
    fig.text(0.54, 0.151, 'At $|h|=1/2$, smaller/larger $\\leq e^{-3.6\\times10^6}$.', fontsize=20, color='#7954a1')
    fig.text(0.54, 0.092, 'Magnitude equality at the plane permits cancellation; no Q-division there.', fontsize=17, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (9)–(15), (21)–(22), (27)–(32); Exercise 1. The assembled solution is not sampled.', fontsize=14.5, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    metadata = {'schema': 'exact-toy-real-frequency-slope-and-dominance-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(9)-(15)', '(21)-(22)', '(27)-(32)', 'Exercise 1'], 'symbols': {'P': 'xi2^2+xi1', 'Q': 'xi1^2', 'N': [0, 1], 'path': ['t^3', '0'], 'kappa': 2, 'gamma': 1}, 'slope_panel': {'nu': 16, 'B': 3, 'M': 52, 'A0': 480, 'A0_strict_lower_bound': 464, 'sigma_plus_exact': 'i*sqrt(4-7/(2*2^15))', 'sigma_plus_imag_displayed': sigma_plus, 'Bnu_exact': '(1/16+1/17)/2', 'upper_B_exact': '(1/15+1/16)/2', 'ell_exact': '1/255', 'rho_exact': '1/4096', 'upper_rho_exact': '1/3600', 'normal_coordinate': '(s-B16)/ell16', 'sample_count': 1001, 'smooth_step': 'exp(-1/y)/(exp(-1/y)+exp(-1/(1-y))) with constant extensions', 'whole_psi': 'L*i+R*sigma_plus+(1-L-R)*(1-480i)', 'integral_negative_mean_is_proved_analytically': True, 'numerical_quadrature_claimed_as_proof': False}, 'dominance_panel': {'nu': 16, 'h_domain': [-1, 1], 'sample_count': 501, 'h': '(s-B16)/rho16', 'Lambda_exact': '2^32*(4*sqrt(4-7/(2*2^16))-1)', 'Lambda_times_rho_displayed': lambda_rho, 'certified_transition_suppression_exponent_lower_bound': 3600000, 'normalized_log_ratio': '-h', 'plateau_halfwidth': '1/2', 'transition_strips': [[-1, -0.5], [0.5, 1]], 'Q_image_nonvanishing_at_join_claimed': False}, 'actual_toy_slope_profile_sampled': True, 'complete_phase_integrated_or_sampled': False, 'infinite_assembled_solution_sampled': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

"""Exact toy bridge geometry and the complete normalized coefficient; no slab sum is sampled."""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'compact-slab-nonzero-bridge-and-exact-quotient-025'

def step(y):
    a = np.zeros_like(y, dtype=float)
    b = np.zeros_like(y, dtype=float)
    mask = y > 0
    a[mask] = np.exp(-1 / y[mask])
    mask = y < 1
    b[mask] = np.exp(-1 / (1 - y[mask]))
    hh = a / (a + b)
    der = np.zeros_like(y)
    mask = (y > 0) & (y < 1)
    der[mask] = hh[mask] * (1 - hh[mask]) * (1 / y[mask] ** 2 + 1 / (1 - y[mask]) ** 2)
    return (hh, der)

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'A compact slab: opposite slopes connected through 1', fontsize=30, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact toy $P=\\xi_2^2+\\xi_1$, $Q=\\xi_1^2$, $\\xi(t)=(t^3,0)$; interval $[0,1]$, $t_0=2^{16}$.', fontsize=21, color='#41505a')
    left = fig.add_axes([0.065, 0.37, 0.4, 0.45], facecolor='white')
    right = fig.add_axes([0.56, 0.37, 0.39, 0.45], facecolor='white')
    theta = np.linspace(0, 1, 1201)
    tt = 2 ** 16
    sigma = math.sqrt(4 - 7 / (2 * 2 ** 15))
    uw, ud = step(6 * (theta - 1 / 3))
    ww, wd = step(6 * (theta - 1 / 2))
    psi = (1 - uw) * 1j * sigma + (uw - ww) - ww * 1j * sigma
    prime = 6 * (-ud * 1j * sigma + (ud - wd) - wd * 1j * sigma)
    left.plot(psi.real, psi.imag, lw=5, color='#167194')
    left.scatter([0, 1, 0], [sigma, 0, -sigma], s=85, color='#132a38', zorder=5)
    left.scatter([0], [0], s=90, marker='x', color='#ba5237', linewidths=3, zorder=5)
    left.annotate('$\\sigma_L\\approx2i$', xy=(0, sigma), xytext=(0.42, 2.17), fontsize=20, color='#132a38')
    left.annotate('$1$', xy=(1, 0), xytext=(1.22, 0.08), fontsize=22, color='#132a38')
    left.annotate('$-\\sigma_R\\approx-2i$', xy=(0, -sigma), xytext=(0.37, -2.4), fontsize=20, color='#132a38')
    left.annotate('0 is avoided', xy=(0, 0), xytext=(-1.53, -0.3), fontsize=18, color='#963d2c')
    left.annotate('', xy=(0.65, 0.35 * sigma), xytext=(0.42, 0.58 * sigma), arrowprops={'arrowstyle': '->', 'color': '#167194', 'lw': 2.3})
    left.annotate('', xy=(0.42, -0.58 * sigma), xytext=(0.65, -0.35 * sigma), arrowprops={'arrowstyle': '->', 'color': '#167194', 'lw': 2.3})
    left.set_xlim(-1.75, 2.4)
    left.set_ylim(-2.65, 2.65)
    left.set_aspect('equal', adjustable='box')
    left.set_xlabel('$\\operatorname{Re}\\Psi$')
    left.set_ylabel('$\\operatorname{Im}\\Psi$')
    left.set_title('Exact nonzero normal-slope geometry', pad=20)
    left.grid(color='#d7dedf', alpha=0.6)
    coefficient = -psi ** 2 + 1j * tt ** (-2) * prime - 1 / tt
    right.axvspan(1 / 3, 2 / 3, color='#d9ebe6', alpha=0.7)
    right.plot(theta, coefficient.real, lw=3.5, color='#167194')
    right.plot(theta, coefficient.imag, lw=3.5, color='#7954a1', ls='--')
    right.plot(theta, np.abs(coefficient), lw=3.5, color='#ba5237', ls=':')
    right.axhline(0, color='#a7afb2', lw=1)
    right.set_xlim(0, 1)
    right.set_ylim(-2.3, 4.55)
    right.set_xticks([0, 1 / 3, 0.5, 2 / 3, 1], ['0', '1/3', '1/2', '2/3', '1'])
    right.set_xlabel('Normal position $\\theta=s$ on $[0,1]$')
    right.set_ylabel('Complete normalized coefficient $t_0^2c_0(s)$')
    right.set_title('The exact ordered polynomial quotient', pad=20)
    right.grid(color='#d7dedf', alpha=0.6)
    fig.text(0.05, 0.263, 'Two smooth segments: $\\sigma_L\\to1\\to-\\sigma_R$.', fontsize=20, color='#132a38')
    fig.text(0.05, 0.206, 'Euclidean axes have the same scale; the carrier is unchanged.', fontsize=18, color='#41505a')
    fig.text(0.05, 0.151, 'Flat end weights join each single-mode boundary tail.', fontsize=19, color='#132a38')
    fig.text(0.05, 0.092, 'No complex conjugation of the symbols is used.', fontsize=19, color='#41505a')
    for y, color, style, label in [(0.263, '#167194', '-', 'Real part of the full quotient'), (0.21, '#7954a1', '--', 'Imaginary part of the full quotient'), (0.157, '#ba5237', ':', 'Modulus of the full quotient')]:
        fig.add_artist(Line2D([0.54, 0.572], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.585, y, label, fontsize=20, color='#132a38')
    fig.text(0.54, 0.092, "$t_0^2c_0=-\\Psi^2+i\\,t_0^{-2}\\Psi'-t_0^{-1}$; Q-image is exactly $t_0^6V_0$.", fontsize=19, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (3)–(12); Exercises 1–2. Exact bridge coefficient; the complete slab solution is not sampled.', fontsize=14.5, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    metadata = {'schema': 'exact-toy-compact-slab-bridge-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(3)-(12)', 'Exercises 1-2'], 'symbols': {'P': 'xi2^2+xi1', 'Q': 'xi1^2', 'N': [0, 1], 'path': ['t^3', '0'], 'kappa': 2, 'beta': 2}, 'interval': [0, 1], 't0': tt, 'nu0': 16, 'sample_count': 1201, 'endpoint_root_exact': 'i*sqrt(4-7/(2*2^15))', 'endpoint_imaginary_sampled': sigma, 'connector': '(1-u)*sigma+(u-w)*1+w*(-sigma)', 'weights': {'u': 'h(6*(theta-1/3))', 'w': 'h(6*(theta-1/2))', 'h': 'e(y)/(e(y)+e(1-y)); e(y)=exp(-1/y) for y>0 and0 otherwise'}, 'complete_normalized_coefficient': "-Psi^2+i*t0^(-2)*Psi'-t0^(-1)", 'complete_Q_image': 't0^6*V0', 'coefficient_real_and_imaginary_parts_sampled': True, 'numerically_sampled_minimum_modulus': float(np.min(np.abs(coefficient))), 'sampled_minimum_claimed_as_proof': False, 'complex_axes_equal_scale': True, 'full_phase_integrated_or_sampled': False, 'complete_slab_solution_sampled': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

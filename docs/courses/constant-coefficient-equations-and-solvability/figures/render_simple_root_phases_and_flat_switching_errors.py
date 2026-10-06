"""An exact Gaussian model and a labelled switching-curve geometry."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
STEM = 'simple-root-transport-and-flat-switching-025'
matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15, 'mathtext.fontset': 'dejavusans', 'svg.hashsalt': STEM})

def render(destination):
    destination.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(16, 8), dpi=150, facecolor='white')
    fig.text(0.05, 0.95, 'Simple-root transport and flat switching errors', fontsize=25, weight='bold')
    fig.text(0.05, 0.902, 'An exact one-dimensional model and the curve geometry used to correct a general residual.', fontsize=16, color='#444444')
    ax = fig.add_axes([0.065, 0.35, 0.405, 0.475])
    S = np.linspace(-2, 2, 1001)
    for delta, color in [(1 / 4, '#1f78b4'), (1 / 8, '#b75116'), (1 / 16, '#654b99')]:
        denominator = round(1 / delta)
        ax.plot(S, np.exp(-S * S / (2 * delta)), lw=2.6, color=color, label=f'$\\delta=1/{denominator}$')
    ax.set(xlim=(-2, 2), ylim=(0, 1.06), xlabel='$S$', ylabel='$U_\\delta(S)$')
    ax.set_title('$U_\\delta(S)=e^{-S^2/(2\\delta)}$, $\\delta>0$', loc='left', fontsize=18, pad=14)
    ax.grid(alpha=0.2)
    ax.legend(loc='upper right', fontsize=14, frameon=False)
    bx = fig.add_axes([0.565, 0.35, 0.38, 0.475])
    for center in (-1, 1):
        bx.axvspan(center - 1 / 4, center + 1 / 4, color='#e4ebf0')
        bx.axvline(center, color='#b75116', lw=2.4)
        bx.scatter([center], [0], color='#b75116', s=55, zorder=4)
    bx.axhline(0, color='#344f67', lw=2.3)
    bx.text(-1.92, 0.205, '$\\Gamma_1:S=-1$', fontsize=15, color='#8c4115')
    bx.text(0.43, 0.205, '$\\Gamma_2:S=1$', fontsize=15, color='#8c4115')
    bx.text(-0.48, 0.012, '$\\delta=0$', fontsize=14, color='#344f67')
    bx.text(-1.4, -0.21, 'First tube', fontsize=13, color='#344f67')
    bx.text(0.66, -0.21, 'Second tube', fontsize=13, color='#344f67')
    bx.set(xlim=(-2, 2), ylim=(-1 / 4, 1 / 4), xlabel='$S$', ylabel='$\\delta$')
    bx.set_yticks([-1 / 4, 0, 1 / 4], ['−1/4', '0', '1/4'])
    bx.set_title('Disjoint tubes of radius 1/4; transverse curves', loc='left', fontsize=16, pad=14)
    bx.grid(alpha=0.15)
    fig.text(0.065, 0.23, '$G_\\delta=D_S-iS/\\delta,\\quad H(S,z)=z-iS,\\quad \\phi=iS^2/2,\\quad W=1,\\quad R=0.$', fontsize=19)
    fig.text(0.065, 0.173, 'The right panel shows permitted correction neighbourhoods. In this exact model, the correction is zero.', fontsize=14)
    fig.text(0.065, 0.122, 'Equations (8)–(10), (15)–(17), (20). Exact Gaussian model and switching-curve geometry.', fontsize=14)
    fig.text(0.065, 0.076, 'The model is not a half-space nonuniqueness construction or a periodic seed.', fontsize=14, color='#444444')
    fig.text(0.065, 0.033, 'The Gaussian correction is zero; the tubes show where a general correction can be supported.', fontsize=13, color='#555555')
    fig.savefig(destination / (STEM + '.png'), metadata={'Software': 'Original exact mathematical model; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(destination / (STEM + '.svg'), metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    data = {'schema': 'original-simple-root-transport-exact-model/v1', 'authorship': 'GPT-6.1 Sol (OpenAI), Ultra; original expression CC0', 'human_source': 'Lars Hörmander, The Analysis of Linear Partial Differential Operators II', 'lesson_equations': ['(8)..(10)', '(15)..(17)', '(20)'], 'dimensions': [2400, 1200], 'model': {'S_domain': [-2, 2], 'delta_profiles': ['1/4', '1/8', '1/16'], 'G': 'D_S-iS/delta', 'H': 'z-iS', 'phi': 'iS^2/2', 'W': 1, 'R': 0, 'mode': 'exp(-S^2/(2delta)); delta>0', 'D_convention': '-i partial_S'}, 'curve_geometry': {'Gamma1': 'S=-1', 'Gamma2': 'S=1', 'delta_range': ['-1/4', '1/4'], 'tube_radius': '1/4', 'intersections': [[-1, 0], [1, 0]], 'shown_tubes_are_permitted_neighbourhoods': True, 'actual_correction_in_this_model': 0}, 'periodic_seed_or_nonuniqueness_solution_asserted': False}
    (destination / (STEM + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return data
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    print(json.dumps({'figure': STEM, 'dimensions': render(args.output_dir)['dimensions']}))

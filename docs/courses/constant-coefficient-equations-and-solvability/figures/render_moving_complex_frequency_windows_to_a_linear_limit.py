"""Deterministic scientific figure of the general linear-limit model."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
STEM = 'complex-window-shift-and-linear-limit-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 20, 'svg.hashsalt': STEM, 'axes.titlesize': 24, 'axes.labelsize': 21, 'legend.fontsize': 18})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'A complex window moves to a linear limit', fontsize=31, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact sixth-degree algebra: a derivative sign, a translated centre, and reciprocal scale adjustments.', fontsize=21, color='#41505a')
    left = fig.add_axes([0.075, 0.34, 0.395, 0.49], facecolor='white')
    right = fig.add_axes([0.565, 0.34, 0.385, 0.49], facecolor='white')
    grid = np.linspace(-1.7, 1.7, 601)
    xx, yy = np.meshgrid(grid, grid)
    sign = 6 * (5 * xx ** 4 * yy - 10 * xx ** 2 * yy ** 3 + yy ** 5)
    left.contourf(xx, yy, sign, levels=[-100000.0, 0, 100000.0], colors=['#f5d3c8', '#d5e9ed'], alpha=0.85)
    for k in range(10):
        theta = k * np.pi / 5
        length = 3
        left.plot([0, length * np.cos(theta)], [0, length * np.sin(theta)], color='#7a858a', lw=1.1)
    left.scatter([1], [1], s=120, color='#ba5237', zorder=5)
    left.annotate('$z_0=1+i$' + '\n' + "$r'(z_0)=-24-24i$", xy=(1, 1), xytext=(-1.57, 1.58), fontsize=21, va='top', color='#132a38', arrowprops={'arrowstyle': '->', 'color': '#132a38'})
    left.text(-1.58, -1.51, "Coral: Im r' < 0\nBlue: Im r' > 0", fontsize=18, bbox={'facecolor': 'white', 'edgecolor': '#d7dedf', 'alpha': 0.95})
    left.set_xlim(-1.7, 1.7)
    left.set_ylim(-1.7, 1.7)
    left.set_aspect('equal', adjustable='box')
    left.set_xlabel('$\\operatorname{Re}z$')
    left.set_ylabel('$\\operatorname{Im}z$')
    left.set_title('Derivative sign: $r(z)=z^6$', pad=20)
    z0 = 1 + 1j
    argument = np.linspace(-0.25, 0.25, 501)
    for v, color in [(1 / 2, '#ba5237'), (1 / 4, '#7954a1'), (1 / 8, '#167194')]:
        values = ((z0 + v * argument) ** 6 - z0 ** 6) / (v * (1 - 8j * v ** 8))
        right.plot(values.real, values.imag, color=color, lw=3.5, label=f'v = {v:g}')
        right.scatter([values.real[0], values.real[-1]], [values.imag[0], values.imag[-1]], s=38, color=color)
    limit = (-24 - 24j) * argument
    right.plot(limit.real, limit.imag, color='#132a38', lw=2.5, ls='--', label='Limit $(-24-24i)z$')
    right.scatter([0], [0], s=60, color='#132a38', zorder=5)
    right.set_xlim(-8.4, 8.4)
    right.set_ylim(-8.4, 8.4)
    right.set_aspect('equal', adjustable='box')
    right.set_xlabel('$\\operatorname{Re}F_v(z)$')
    right.set_ylabel('$\\operatorname{Im}F_v(z)$')
    right.set_title('Full complex values: real $z\\in[-1/4,1/4]$', pad=20)
    right.grid(True, color='#d7dedf')
    right.legend(loc='lower right', framealpha=0.95)
    fig.text(0.06, 0.218, '$h=(K/T)^{1/4},\\quad\\widehat T=hT,\\quad\\widehat K=K/h$', fontsize=22, color='#132a38')
    fig.text(0.06, 0.163, '$\\widehat K/\\widehat T=(K/T)^{1/2}\\to0,\\quad\\widehat T\\widehat K=TK$', fontsize=22, color='#132a38')
    fig.text(0.06, 0.108, "$r_\\nu^*(0)=0\\quad\\Longrightarrow\\quad r_\\nu^*(hz)/h\\to r'(z_0)z$", fontsize=22, color='#132a38')
    fig.text(0.545, 0.217, '$F_v(z)=\\dfrac{(1+i+vz)^6-(1+i)^6}{v(1-8iv^8)}$', fontsize=23, color='#132a38')
    fig.text(0.545, 0.145, '$(\\kappa,\\tau,\\Lambda)=(9,11,16),\\quad \\lambda^*=v^{-16}(1-v^4)>0$', fontsize=21, color='#132a38')
    fig.text(0.545, 0.092, 'Dots mark the endpoints z = -1/4 and z = 1/4.', fontsize=19, color='#41505a')
    fig.text(0.045, 0.045, 'Equations (3)–(16). Exact derivative-sign, window-shift and shrinking models.', fontsize=15, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    data = {'schema': 'exact-complex-window-linear-limit-model-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(3)-(4)', '(7)-(12)', '(13)-(16)'], 'derivative_panel': {'r': 'z^6', 'derivative': '6*z^5', 'imaginary_derivative': '6*(5*x^4*y-10*x^2*y^3+y^5)', 'argument_domain': [['-17/10', '17/10'], ['-17/10', '17/10']], 'grid': [601, 601], 'zero_sign_rays': 'theta=k*pi/5,k=0,...,9', 'z0': [1, 1], 'derivative_at_z0': [-24, -24], 'equal_coordinate_units': True, 'negative_sign_color': 'coral', 'positive_sign_color': 'blue'}, 'limit_panel': {'F_v': '((1+i+v*z)^6-(1+i)^6)/(v*(1-8*i*v^8))', 'real_argument_domain': ['-1/4', '1/4'], 'argument_sample_count': 501, 'v_values': ['1/2', '1/4', '1/8'], 'limit': '(-24-24*i)*z', 'both_real_and_imaginary_coordinates_shown': True, 'equal_coordinate_units': True, 'endpoint_dots_are_argument_endpoints': True}, 'rational_model': {'P': '(xi1-i*xi2)^6-xi1^5', 'Q': 'xi1^6', 'N': [0, 1], 'zeta': ['v^-16', 'v^-12-i*(v^-16-v^-12)'], 'T': 'v^-11', 'K': 'v^-9', 'lambda': 'v^-16*(1-v^4)', 'c': '-v^80/(1-8*i*v^8)', 'b': 'v^96', 'coefficient_ratio': '-v^16*(1-8*i*v^8)', 'leading_exponents': {'kappa': 9, 'tau': 11, 'Lambda': 16}, 'differences': [2, 5, 4], 'normal_imaginary_direction_negative_for': '0<v<1'}, 'physical_space_solution_sampled': False, 'periodic_seed_constructed': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

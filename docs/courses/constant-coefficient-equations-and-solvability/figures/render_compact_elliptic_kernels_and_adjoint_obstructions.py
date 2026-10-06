"""Reproduce an original exact section and operator diagram; no solution is sampled."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, FancyBboxPatch
import numpy as np
STEM = 'compact-elliptic-kernel-and-adjoint-obstruction-025'
matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15, 'mathtext.fontset': 'dejavusans', 'svg.hashsalt': STEM, 'axes.spines.top': False, 'axes.spines.right': False})

def render(destination):
    destination.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(16, 8), dpi=150, facecolor='#ffffff')
    fig.text(0.05, 0.955, 'From a periodic seed to a compact adjoint obstruction', fontsize=24, weight='bold')
    fig.text(0.05, 0.908, 'The written periodic seed supplies the compact kernel; the picture shows its support bound and operator maps.', fontsize=16, color='#444444')
    ax = fig.add_axes([0.055, 0.285, 0.43, 0.565])
    ax.set_aspect('equal')
    ax.add_patch(Wedge((0, 0), 3, 0, 360, width=2, facecolor='#e4ebf0', edgecolor='none'))
    ax.add_patch(Wedge((0, 0), 17 / 8, 0, 360, width=1 / 8, facecolor='#1f78b4', alpha=0.7, edgecolor='none'))
    for radius in (3 / 4, 13 / 4):
        ax.add_patch(Circle((0, 0), radius, fill=False, ls='--', lw=1.6, color='#777777'))
    for radius in (1, 3):
        ax.add_patch(Circle((0, 0), radius, fill=False, lw=1.8, color='#344f67'))
    ax.add_patch(Circle((0, 0), 2, fill=False, lw=1.4, color='#12659a'))
    ax.scatter([1], [np.sqrt(3)], color='#b75116', s=55, zorder=5)
    ax.annotate('$t=1,\\ \\theta=\\pi/6$' + '\n' + '$(y_1,\\varrho-4)=(1,\\sqrt{3})$', xy=(1, np.sqrt(3)), xytext=(1.05, 2.7), fontsize=13, arrowprops={'arrowstyle': '->', 'color': '#b75116'}, color='#8c4115')
    ax.text(-3.25, 2.9, '$r=3$', fontsize=13, color='#344f67')
    ax.text(-0.55, 0.12, '$r<1$', fontsize=13, color='#555555')
    ax.text(-2.9, -2.5, '$1\\leq r\\leq3$' + '\nSupport bound', fontsize=14, color='#344f67')
    ax.annotate('Joining band\n' + '$2\\leq r\\leq17/8$', xy=(-1.85, 0.8), xytext=(-3.4, 0.95), fontsize=13, arrowprops={'arrowstyle': '->', 'color': '#12659a'}, color='#12659a')
    ax.set(xlim=(-3.7, 3.7), ylim=(-3.45, 3.45), xlabel='$y_1$', ylabel='$\\varrho-4$')
    ax.set_title('Exact section at $\\phi=0$; illustrated $\\epsilon=1/8$', loc='left', fontsize=16, pad=12)
    ax.grid(alpha=0.15)
    bx = fig.add_axes([0.55, 0.24, 0.405, 0.61])
    bx.set_xlim(0, 1)
    bx.set_ylim(0, 1)
    bx.axis('off')
    bx.text(0, 1.02, 'The operator and its transpose have distinct roles', fontsize=16)

    def box(bottom, height, lines, color='#edf3f7'):
        bx.add_patch(FancyBboxPatch((0.02, bottom), 0.96, height, boxstyle='round,pad=0.012,rounding_size=0.012', lw=1.2, ec='#7a8b95', fc=color))
        for index, line in enumerate(lines):
            bx.text(0.5, bottom + height * (1 - (index + 0.7) / len(lines)), line, ha='center', va='center', fontsize=17 if len(lines) < 3 else 16)
    box(0.77, 0.2, ['$0\\ne w\\in C_c^\\infty(\\mathbb{R}^3),\\quad Lw=0$', '$E=L^{\\mathrm{t}},\\quad E^{\\mathrm{t}}=L$'])
    box(0.47, 0.19, ['$\\mathcal{A}=D_yE+Q,\\quad \\mathrm{ord}\\,Q\\leq4$', '$R^{-1}\\mathcal{A}(D_y+R)\\longrightarrow E$'])
    box(0.15, 0.2, ['$E^{\\mathrm{t}}(w\\otimes h)=0$', '$0\\ne h\\in C_c^\\infty(\\mathbb{R})$', 'Compact adjoint kernel in four dimensions'], '#fcf0e7')
    for bottom, top in [(0.67, 0.75), (0.36, 0.45)]:
        bx.annotate('', xy=(0.5, bottom), xytext=(0.5, top), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#b75116'})
    bx.text(0.5, 0.035, '$S_{\\mathcal{A}}\\asymp\\langle\\eta\\rangle\\langle\\xi\\rangle^4$', ha='center', fontsize=19, color='#344f67')
    fig.text(0.055, 0.197, '$\\varrho=(y_2^2+y_3^2)^{1/2},\\quad r=t+1$', fontsize=14)
    fig.text(0.055, 0.145, '$|\\det D\\Phi|=r(4+r\\cos\\theta)>0$' + '   •   The shading bounds support; it does not depict values of a constructed solution.', fontsize=14, color='#333333')
    fig.text(0.055, 0.097, 'Propositions 1–3; equations (10), (12)–(17), (23)–(26). Support bound and exact operator maps.', fontsize=14)
    fig.text(0.055, 0.058, 'A right kernel for L becomes an adjoint kernel for E=L^t; the solution is not sampled.', fontsize=13, color='#555555')
    fig.savefig(destination / (STEM + '.png'), dpi=150, metadata={'Software': 'Original mathematical figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(destination / (STEM + '.svg'), metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    geometry = {'schema': 'original-receiving-compact-elliptic-witness-geometry/v1', 'authorship': 'GPT-6.1 Sol (OpenAI), Ultra; original expression CC0', 'human_source': 'Lars Hörmander, The Analysis of Linear Partial Differential Operators II', 'lesson_equations': 'Propositions 1–3, (10), (12)–(17), (23)–(26)', 'coordinates': {'theta': 'x1 modulo2pi', 'phi': 'x2 modulo2pi', 't': 'x3', 'map': ['(t+1)sin(theta)', '(4+(t+1)cos(theta))cos(phi)', '(4+(t+1)cos(theta))sin(phi)'], 'r': 't+1', 'varrho': '4+r cos(theta)', 'jacobian_order': ['theta', 'phi', 't'], 'jacobian_determinant': '-r varrho', 'domain_r': ['3/4', '13/4']}, 'section': {'phi': 0, 'axes': ['y1', 'varrho-4'], 'support_bound_r': [1, 3], 'actual_filled_support_asserted': False, 'epsilon_illustrated': '1/8', 'joining_band_r': ['2', '17/8'], 'marked_theta': 'pi/6', 'marked_t': 1, 'marked_point_in_section': ['1', 'sqrt(3)'], 'marked_point_in_R3': ['1', '4+sqrt(3)', '0']}, 'operators': {'given': 'Lw=0; w nonzero compact smooth on R3', 'E': 'L^t', 'A': 'Dy E+Q; Q independent of y, order<=4', 'positive_shift': 'A(Dy+R)/R -> E; R>0', 'kernel': 'E^t(w tensor h)=0; h nonzero compact smooth on R', 'strength': '<eta><xi>^4'}, 'actual_solution_sampled': False, 'dimensions': [2400, 1200]}
    (destination / (STEM + '.json')).write_text(json.dumps(geometry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return geometry
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    print(json.dumps({'figure': STEM, 'dimensions': render(args.output_dir)['dimensions']}))

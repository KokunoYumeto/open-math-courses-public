"""Exact polynomial windows and their growth envelopes; no physical mode is sampled."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'real-laurent-path-growth-envelopes-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 19, 'svg.hashsalt': STEM, 'axes.titlesize': 23, 'axes.labelsize': 21, 'legend.fontsize': 18})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'A real path: Q grows faster, then P catches up', fontsize=30, weight='bold', color='#132a38')
    fig.text(0.045, 0.912, 'Exact symbols $P=\\xi_2^2+\\xi_1$, $Q=\\xi_1^2$, $N=e_2$, along $\\xi(t)=(t^3,0)$.', fontsize=22, color='#41505a')
    left = fig.add_axes([0.07, 0.37, 0.4, 0.45], facecolor='white')
    right = fig.add_axes([0.56, 0.37, 0.39, 0.45], facecolor='white')
    h = np.linspace(0, 3.5, 701)
    left.axvspan(1.5, 3, color='#d9ebe6', alpha=0.8)
    left.plot(h, np.maximum(3, 2 * h), lw=4, color='#167194')
    left.plot(h, np.full_like(h, 6), lw=4, color='#ba5237')
    left.plot([2, 2], [0, 6], lw=2, ls='--', color='#7954a1')
    left.scatter([1.5, 2, 3], [3, 4, 6], s=[75, 110, 85], color='#167194', zorder=5)
    left.scatter([2], [6], s=110, color='#ba5237', zorder=5)
    left.annotate('$g_P=4$', xy=(2, 4), xytext=(2.16, 3.7), fontsize=20, color='#167194')
    left.annotate('$g_Q=6$', xy=(2, 6), xytext=(1.68, 6.38), fontsize=20, color='#963d2c')
    left.text(0.22, 3.36, 'P slope 0', fontsize=19, color='#167194')
    left.text(2.5, 4.4, 'P slope 2', fontsize=19, color='#167194')
    left.set_xticks([0, 1, 1.5, 2, 3, 3.5], ['0', '1', '3/2', '2', '3', '7/2'])
    left.set_yticks([0, 2, 3, 4, 6, 7])
    left.set_xlim(0, 3.5)
    left.set_ylim(0, 7.35)
    left.set_xlabel('Normal window exponent $h$')
    left.set_ylabel('Growth exponent $G_R(h)$')
    left.set_title('Choose the scale before the first meeting', pad=20)
    left.grid(color='#d7dedf', alpha=0.6)
    z = np.linspace(-2, 2, 501)
    colors = ['#167194', '#7954a1', '#6c997b']
    for tt, color in zip([2, 4, 8], colors):
        right.plot(z, z * z + 1 / tt, lw=3, color=color)
    right.plot(z, z * z, lw=3, color='#132a38', ls='--')
    right.plot(z, np.ones_like(z), lw=3, color='#ba5237', ls=':')
    right.set_xlim(-2, 2)
    right.set_ylim(-0.12, 4.9)
    right.set_xlabel('Real normal variable $z$')
    right.set_ylabel('Normalized polynomial value')
    right.set_title('Whole window: $z^2+t^{-1}\\ \\to\\ z^2$', pad=20)
    right.grid(color='#d7dedf', alpha=0.6)
    for y, color, style, label in [(0.263, '#167194', '-', '$G_P(h)=\\max(3,2h)$'), (0.21, '#ba5237', '-', '$G_Q(h)=6$'), (0.157, '#7954a1', '--', 'Selected $\\kappa=2$: $d_P=2>d_Q=0$')]:
        fig.add_artist(Line2D([0.05, 0.082], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.095, y, label, fontsize=21, color='#132a38')
    fig.text(0.05, 0.092, 'Shaded interval $3/2<h<3$: P is lower and has larger slope.', fontsize=18, color='#41505a')
    for y, color, style, label in [(0.263, '#167194', '-', '$t=2$: $z^2+1/2$'), (0.21, '#7954a1', '-', '$t=4$: $z^2+1/4$'), (0.157, '#6c997b', '-', '$t=8$: $z^2+1/8$')]:
        fig.add_artist(Line2D([0.54, 0.572], [y + 0.004, y + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.585, y, label, fontsize=21, color='#132a38')
    fig.text(0.54, 0.092, 'Dashed: P limit $z^2$. Dotted: normalized Q is exactly 1.', fontsize=18, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (15)–(21), (22)–(25). Exact growth envelopes and polynomial windows.', fontsize=15, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    metadata = {'schema': 'exact-real-laurent-path-growth-envelopes-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(15)-(21)', '(22)-(25)'], 'symbols': {'P': 'xi2^2+xi1', 'Q': 'xi1^2', 'N': [0, 1], 'm': 2, 'path': ['t^3', '0']}, 'envelope_panel': {'h_domain': [0, 3.5], 'sample_count': 701, 'G_P': 'max(3,2h)', 'G_Q': '6', 'P_breakpoint': '3/2', 'first_meeting': 3, 'chosen_kappa': 2, 'g_P': 4, 'g_Q': 6, 'd_P': 2, 'd_Q': 0, 'shaded_interval': ['3/2', 3], 'spherical_maximizer_output_claimed': False}, 'window_panel': {'z_domain': [-2, 2], 'sample_count': 501, 't_values': [2, 4, 8], 'complete_normalized_P': 'z^2+t^(-1)', 'complete_normalized_Q': '1', 'limit_P': 'z^2', 'limit_Q': '1', 'c_P': 1, 'c_Q': 1}, 'physical_space_solution_sampled': False, 'transport_phase_sampled': False, 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)

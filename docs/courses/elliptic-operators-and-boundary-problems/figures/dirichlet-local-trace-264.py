"""Exact n=1 half-space sections of DSP-E22--DSP-E23a; no external TeX process."""
from pathlib import Path
import argparse
import numpy as np
from scipy.special import sici
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
args = parser.parse_args()
args.output_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'text.usetex': False, 'svg.hashsalt': 'AN03-U026-DSP-E23-264',
                     'font.family': 'DejaVu Sans', 'font.size': 12})
r0 = 2.0
def sine_ratio(a, t):
    return a * np.sinc(a * np.asarray(t) / np.pi)
def kernel(x, y, cutoff):
    a = np.sqrt(cutoff)
    return (sine_ratio(a, x-y) - sine_ratio(a, x+y)) / (np.pi*r0)
def diagonal(x, cutoff):
    a = np.sqrt(cutoff)
    return (a-sine_ratio(a, 2*x))/(np.pi*r0)
def local_trace(length, cutoff):
    a = np.sqrt(cutoff)
    return a*length/np.pi-sici(2*a*length)[0]/(2*np.pi)

fig = plt.figure(figsize=(14, 10), facecolor='#fffdf8')
gs = fig.add_gridspec(2, 2, left=.075, right=.965, bottom=.135, top=.80,
                      wspace=.28, hspace=.40)
ax_diag = fig.add_subplot(gs[0, 0])
ax_terms = fig.add_subplot(gs[0, 1])
ax_kernel = fig.add_subplot(gs[1, 0])
ax_trace = fig.add_subplot(gs[1, 1])
for ax in (ax_diag, ax_terms, ax_kernel, ax_trace):
    ax.set_facecolor('#fffdf8')
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=11)
x = np.linspace(0, 6, 1801)
for cutoff, color in [(1, '#225e7b'), (4, '#ab5732')]:
    ax_diag.plot(x, diagonal(x, cutoff), color=color, lw=2.2,
                 label=f'closed cutoff: lambda = {cutoff}')
    ax_diag.axhline(np.sqrt(cutoff)/(np.pi*r0), color=color, lw=1, ls='--')
    ax_trace.plot(x, local_trace(x, cutoff), color=color, lw=2.2,
                  label=f'lambda = {cutoff}')
    ax_trace.plot(x, np.sqrt(cutoff)*x/np.pi, color=color, lw=1, ls='--')
ax_diag.set_title('Weighted diagonal vanishes at the wall', fontsize=14)
ax_diag.set_xlabel('x in the original half-line')
ax_diag.set_ylabel('e(x, x, lambda), relative to 2 dx')
ax_diag.set_xlim(0, 6); ax_diag.set_ylim(-.015, .43)
ax_diag.legend(loc='lower right', fontsize=10, frameon=False)
ax_diag.annotate('x = 0: exact cancellation', xy=(0, 0), xytext=(.55, .07),
                 fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#44566a'})

direct = np.full_like(x, 1/(2*np.pi))
reflected = sine_ratio(1, 2*x)/(2*np.pi)
ax_terms.plot(x, direct, color='#52784a', lw=2, label='direct contribution: 1 / (2 pi)')
ax_terms.plot(x, reflected, color='#a36c93', lw=2,
              label='reflected contribution: sin(2x) / (4 pi x)')
ax_terms.plot(x, direct-reflected, color='#225e7b', lw=2,
              label='their difference: e(x, x, 1)')
ax_terms.axhline(0, color='#95a1aa', lw=.7)
ax_terms.set_title('Both original contributions are retained', fontsize=14)
ax_terms.set_xlabel('x'); ax_terms.set_xlim(0, 6)
ax_terms.legend(loc='lower right', fontsize=10, frameon=False)

grid = np.linspace(0, 4, 501)
xx, yy = np.meshgrid(grid, grid, indexing='xy')
values = kernel(xx, yy, 1)
im = ax_kernel.imshow(values, origin='lower', extent=(0, 4, 0, 4),
                      cmap='RdBu_r', vmin=-.23, vmax=.23, aspect='equal')
ax_kernel.set_xlabel('x'); ax_kernel.set_ylabel('y')
ax_kernel.set_title('Two-variable section: e(x, y, 1)', fontsize=14)
fig.colorbar(im, ax=ax_kernel, pad=.02, fraction=.04).set_label('kernel relative to 2 dy')
ax_kernel.text(.12, 3.64, 'r = 2; n = 1', fontsize=10,
               bbox={'facecolor': '#fffdf8', 'edgecolor': 'none', 'alpha': .9})
ax_trace.set_title('Finite local trace; infinite global rank\nT(L) = aL / pi - Si(2aL) / (2 pi)', fontsize=13)
ax_trace.set_xlabel('physical window length L')
ax_trace.set_ylabel('integral from 0 to L of e(x, x, lambda) 2 dx')
ax_trace.set_xlim(0, 6); ax_trace.set_ylim(0, 4)
ax_trace.legend(loc='upper left', frameon=False, fontsize=10)

fig.text(.5, .945, 'Finite physical traces on infinite spectral subspaces',
         ha='center', fontsize=23, weight='bold', color='#173750')
fig.text(.5, .89, 'Original operator: -d²/dx² on x > 0; Dirichlet boundary; density r = 2; a = sqrt(lambda)',
         ha='center', fontsize=13, color='#315f78')
fig.text(.5, .845, 'e(x,y,lambda) = [sin(a(x-y))/(x-y) - sin(a(x+y))/(x+y)] / (2 pi)',
         ha='center', fontsize=13, color='#315f78')
fig.text(.5, .073, 'DSP-E22--DSP-E23a: numerical samples of the exact formulas. Dashed lines retain the direct contributions.',
         ha='center', fontsize=10.8, color='#405163')
fig.text(.5, .04, 'Every zero denominator uses its continuous limit. lambda = 0 gives the zero kernel; closed endpoints are retained.',
         ha='center', fontsize=10.5, color='#405163')
for suffix in ('png', 'svg'):
    metadata = {'Date': None} if suffix == 'svg' else {'Software': 'AN03-U026-DSP-E23-264'}
    fig.savefig(args.output_dir/f'dirichlet-local-trace-264.{suffix}', dpi=200,
                facecolor=fig.get_facecolor(), metadata=metadata)
plt.close(fig)
print('Rendered exact Dirichlet kernel and localized trace sections.')

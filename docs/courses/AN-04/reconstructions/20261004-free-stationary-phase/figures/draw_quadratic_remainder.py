"""Exact Gaussian model for Q7/E1 in ../quadratic-stationary-phase.md.

Mathematical source route: Guillemin and Sternberg, author draft 2010-01-13,
https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf, sections 14.1–14.5.
Original plot and exact-model calculation for this private reconstruction.
The curves are numerical samples; the dashed constants are proved in E1.
"""
from pathlib import Path
import json
import math
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
mp.mp.dps = 70
hvals = np.geomspace(0.01, 1.0, 220)
orders = (1, 2, 3)
constants = {n: mp.binomial(2*n, n)/mp.mpf(4)**n for n in orders}
samples = []
for hv in hvals:
    h = mp.mpf(str(hv))
    exact = (1+1j*h)**(-mp.mpf('0.5'))
    approximations = {
        n: sum((-1)**k*mp.binomial(2*k, k)/mp.mpf(4)**k*(1j*h)**k
               for k in range(n)) for n in orders
    }
    errors = {n: abs(exact-approximations[n])/h**n for n in orders}
    if any(errors[n] > constants[n] + mp.mpf('1e-55') for n in orders):
        raise RuntimeError('Sample violates the proved E1 bound')
    samples.append({'h': float(h), 'exact_real': float(exact.real),
                    'exact_imag': float(exact.imag),
                    'three_term_real': float(approximations[3].real),
                    'three_term_imag': float(approximations[3].imag),
                    'scaled_errors': {str(n): float(errors[n]) for n in orders}})

plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8), constrained_layout=True)
ax = axes[0]
colors = ['#125D98', '#B34426', '#6C4594']
ax.plot(hvals, [r['exact_real'] for r in samples], color=colors[0], label='Exact real part')
ax.plot(hvals, [r['three_term_real'] for r in samples], '--', color=colors[0], label='Three-term real part')
ax.plot(hvals, [r['exact_imag'] for r in samples], color=colors[1], label='Exact imaginary part')
ax.plot(hvals, [r['three_term_imag'] for r in samples], '--', color=colors[1], label='Three-term imaginary part')
ax.set(title='Normalized integral: $(1+ih)^{-1/2}$', xlabel='$h$', ylabel='Value')
ax.legend(loc='center left', fontsize=9, frameon=False)
ax.grid(alpha=0.18)
ax = axes[1]
for n, color in zip(orders, colors):
    ax.semilogx(hvals, [r['scaled_errors'][str(n)] for r in samples], color=color, label=f'$N={n}$: sampled error')
    ax.axhline(float(constants[n]), color=color, linestyle='--', linewidth=1)
    ax.text(0.035, float(constants[n])+0.005, f'Proved bound: {float(constants[n]):.4g}', color=color, fontsize=9)
ax.set(title='Remainder after $N$ terms', xlabel='$h$ (log scale)', ylabel='$|R_N(h)|/h^N$', ylim=(0.20, 0.54))
ax.legend(loc='lower left', fontsize=9, frameon=False)
ax.grid(alpha=0.18)
fig.suptitle('Quadratic stationary phase — exact Gaussian example', fontsize=15)
fig.savefig(out / 'quadratic-remainder.png', dpi=170)
fig.savefig(out / 'quadratic-remainder.svg')
plt.close(fig)
(out / 'quadratic-remainder-data.json').write_text(json.dumps({
    'scope': 'Numerical illustration of Q7/E1; not a proof or release clearance',
    'precision_decimal_digits': mp.mp.dps,
    'samples': samples,
    'proved_bound_constants': {str(n): str(constants[n]) for n in orders},
    'all_sampled_bounds_satisfied': True,
}, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'figure': str(out / 'quadratic-remainder.png'),
                  'sample_count': len(samples), 'sampled_bound_checks': len(samples)*len(orders),
                  'all_sampled_bounds_satisfied': True}))

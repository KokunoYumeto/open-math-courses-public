"""Exact certificates and original figure for TR-BAKER-10, results 164--165.

Written by GPT-6.1 Sol (OpenAI), Ultra. CC0.
The plotted quantities are proved envelopes, not measured valuations.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent

def exp_bounds(x, order=32):
    total = term = F(1)
    for n in range(1, order + 1):
        term *= x / n
        total += term
    next_term = term * x / (order + 1)
    ratio = x / (order + 2)
    assert ratio < 1
    return total, total + next_term / (1 - ratio)

rows = []
for nu, k, ell, lmin, sqrt_upper, log_upper, target in [
    (6, F(47, 10), F(12, 5), 16, F(217, 100), F(36, 5), F(361, 10)),
    (4, F(11, 2), F(5, 2), 12, F(47, 20), F(67, 10), F(269, 5)),
]:
    assert sqrt_upper**2 > k
    nmax = k * lmin**2 + lmin
    assert exp_bounds(log_upper)[0] > nmax
    reciprocal_sqrt = F(1, 4) if nu == 6 else F(3, 10)
    assert reciprocal_sqrt**2 * lmin >= 1
    left = k * (1 - F(nu + 1) / (ell * nu + 1))
    right = sqrt_upper + reciprocal_sqrt + F(3, 5) / ell * log_upper / lmin
    assert left > right
    lam = ell + F(2, nu)
    coefficient = k * lam**2 + lam / nu + F(1, nu)
    assert coefficient < target
    collision = F(1, nu) + 2 * sqrt_upper * lam / nu + F(7, 10) / (5 * nu)
    assert collision < (3 if nu == 6 else 4)
    rows.append({
        'nu': nu, 'k': str(k), 'ell': str(ell), 'minimum_L': lmin,
        'minimum_K': 76 if nu == 6 else 67,
        'left_lower': str(left), 'right_upper': str(right),
        'positive_determinant_margin': str(left - right),
        'total_constant_upper': str(coefficient),
        'stated_constant': str(target), 'positive_constant_margin': str(target - coefficient),
        'collision_coefficient_upper': str(collision),
    })
assert F(729, 640) < F(6, 5)
assert F(81, 80)**2 > F(67, 66)
assert exp_bounds(F(11, 10))[1] < F(10, 3)
assert F(47, 10) > 4
assert exp_bounds(F(7, 10))[0] > 2
record = {
    'state': 'passed_exact_rational_certificate', 'rows': rows,
    'factorial': 'Q_K <= exp(3/2)/(K-1), proved by integral and convex trapezoid bounds',
    'beta': 'K>=67; f(K)<6/5; exp(11/10)<10/3; k>4; hence log(beta)<log(D)+2/5',
    'coverage': 'All B>=nu, z>=1, qB>=5; monotonicity arguments in the full proof reduce logarithmic envelopes to minimum L. Both injectivity alternatives covered.',
    'finite_checks_are_not_the_proof': True,
}
(ROOT / 'sharp-E-parameter-endpoints.json').write_text(json.dumps(record, indent=2)+'\n')

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.4), constrained_layout=True)
colors = ['#145e88', '#b15124']
for row, color in zip(rows, colors):
    nu = row['nu']; k = float(F(row['k'])); ell = float(F(row['ell']))
    b = np.linspace(nu, 20, 3000)
    l = np.floor(ell*b) + 2
    margin = k*(1-(b+1)/l) - math.sqrt(k) - 1/np.sqrt(l) - 3*b*np.log(k*l*l+l)/(5*l*l)
    total = k*(l/b)**2 + l/b**2 + 1/b
    assert np.min(margin) > 0
    assert np.max(total) < float(F(row['stated_constant']))
    axes[0].plot(b, margin, color=color, linewidth=1.5, label=f"ν = {nu}: k = {k:g}, ℓ = {ell:g}")
    axes[1].plot(b, total, color=color, linewidth=1.5, label=f"ν = {nu}: N and common p-part")
    target = float(F(row['stated_constant']))
    axes[1].axhline(target, color=color, linestyle='--', linewidth=1.0)
    axes[1].text(20.1, target, f'{target:g}', color=color, va='center')
axes[0].axhline(0, color='#555555', linewidth=0.9)
axes[0].set(title='Guaranteed determinant margin', xlabel='B = Hν / (E ln p)', ylabel='Normalized margin mν(B)', xlim=(4, 20))
axes[1].set(title='Guaranteed valuation coefficient', xlabel='B = Hν / (E ln p)', ylabel='Upper bound for (EN + u) / (EzB²)', xlim=(4, 21.5))
for ax in axes:
    ax.grid(alpha=.18)
    ax.legend(loc='best', fontsize=9)
fig.suptitle('Sharp E-parameter bounds: all B ≥ ν, z ≥ 1 and (E ln p)B ≥ 5', fontsize=13)
fig.savefig(ROOT/'sharp-E-parameter-budget.png', dpi=160)
plt.close(fig)
print(json.dumps({'state': record['state'], 'rows': rows}))

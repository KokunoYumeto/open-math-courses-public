"""Coefficient proximity in the Thue exponent bound (CC0).

Theorem 13.8 proves the full range. Exact rational margins below check
its elementary constants; the plotted integer samples are illustrative.
Primary context: M. Mignotte, Acta Arithmetica 75 (1996), Theorem 2,
https://www.impan.pl/shop/en/publication/transaction/download/product/109013
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math


def exact_checks():
    # atanh series with a geometric upper bound for the positive tail
    z = F(1, 3)
    terms = 12
    log2_lo = 2 * sum(z ** (2*j+1) / (2*j+1) for j in range(terms))
    log2_hi = log2_lo + 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    exp_5_2_lo = sum(F(5, 2)**j / math.factorial(j) for j in range(9))
    checks = {
        'log2_above_two_thirds': log2_lo-F(2, 3),
        'log2_below_one': 1-log2_hi,
        'exp_five_halves_above_ten': exp_5_2_lo-10,
        'radius_contradiction_margin': F(1, 2)-F(2, 10**7),
        'radius_a1_margin': 2-F(4, 10**7),
        'final_threshold_margin': F(10**7)-7020*19**2,
    }
    assert 390*4*2*F(9,4) == 7020
    assert all(v > 0 for v in checks.values())
    # A finite check of the sign reduction; the proof covers all integers.
    cases = 0
    for a in range(1, 13):
        for b in range(1, 13):
            if a == b:
                continue
            for n in range(3, 9):
                for y in range(2, 10):
                    for x in range(-y+1, y):
                        if not x:
                            continue
                        c = a*x**n-b*y**n
                        if not c:
                            continue
                        if n > 3*math.log(1.5*abs(c)/b):
                            assert x**n > 0 and a > b
                        cases += 1
    return {'exact_positive_margins': {k: str(v) for k,v in checks.items()},
            'coefficient_identity': '390*4*2*(3/2)^2 = 7020',
            'finite_supplementary_sign_cases': cases,
            'full_range_argument': 'Theorem 13.8, equations (13.49)-(13.57)'}


def figure(destination):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    values = np.unique(np.rint(np.geomspace(3, 10**8, 420)).astype('int64'))
    l = np.log(values.astype(float))
    adjacent = l/np.log1p(l/np.log1p(1/(values.astype(float)-1)))
    separated = l/math.log(2)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.5), constrained_layout=True)
    for ax in axes:
        ax.set_xscale('log')
        ax.set_xlabel('Integer coefficient a')
        ax.set_ylabel(r'Coefficient factor $\log A/\lambda$')
        ax.grid(alpha=.22)
    axes[0].plot(values, adjacent, color='#176b72', lw=2.3, label='b = a - 1')
    axes[0].axhline(2, color='#9c533b', linestyle='--', label='Proved upper bound: 2')
    axes[0].set_ylim(.5, 2.2)
    axes[0].set_title('Adjacent coefficients')
    axes[0].legend(loc='center right')
    axes[1].plot(values, separated, color='#9c533b', lw=2.3, label='b = 1')
    axes[1].plot(values, adjacent, color='#176b72', lw=2.3, label='b = a - 1')
    axes[1].set_title('Effect of coefficient separation')
    axes[1].legend()
    fig.savefig(destination, dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    output = Path(__file__).resolve().parent
    result = exact_checks()
    (output/'family-parameter-checks.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    figure(output/'family-parameter-bound.png')
    print(json.dumps(result))

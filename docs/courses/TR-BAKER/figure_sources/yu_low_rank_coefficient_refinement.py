"""Exact dependent example and a reproducible illustration of Results 10.227–229."""
from pathlib import Path
from fractions import Fraction
import json
import math


def valuation(value, prime):
    value = Fraction(value)
    assert value
    numerator, denominator = abs(value.numerator), value.denominator
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def checks():
    rows = []
    for k in range(1, 33):
        bound = 5 ** k
        exponent = 3 * bound + 5
        assert exponent % 4 == 0 and valuation(exponent, 5) == 1
        residue = (pow(2, exponent, 125) - 1) % 125
        assert residue % 25 == 0 and residue != 0
        rows.append({'k': k, 'B': bound, 'M': exponent,
                     'M_mod_4': exponent % 4, 'v5_M': 1,
                     'Xi_minus_one_mod_125': residue, 'v5_Xi_minus_one': 2})
    edges = [
        (2, [Fraction(-3), Fraction(9)], [1, 1], 2),
        (2, [Fraction(-2), Fraction(1, 2)], [1, 1], 1),
        (5, [Fraction(10), Fraction(2, 5)], [1, 1], 0),
        (5, [Fraction(5), Fraction(2)], [-1, 1], -1),
    ]
    edge_rows = []
    for prime, bases, coefficients, expected in edges:
        product = math.prod(a ** b for a, b in zip(bases, coefficients))
        assert valuation(product - 1, prime) == expected
        edge_rows.append({'p': prime, 'bases': list(map(str, bases)),
                          'coefficients': coefficients, 'Xi': str(product),
                          'valuation': expected})
    assert Fraction(14, 3) < 5 and 16 ** 6 > 5
    return {
        'state': 'exact_example_and_constant_checks_passed',
        'examples': rows, 'edge_examples': edge_rows,
        'constant_gap': str(Fraction(5) - Fraction(14, 3)),
        'two_base_rank_cases': [0, 1, 2],
        'analytic_proof': [
            'A primitive integer valuation vector generates the rational line; Bezout proves integral exponents.',
            'Rational heights give |M| < 2n B Omega and h(beta) <= Omega.',
            'The even power 2(p-1) removes signs and enters the domain of the proved local power identity.',
            'U >= Omega L and U >= epsilon r imply log|M| < 3U for every allowed input.',
            'L > (n+1)log p and log p < p-1 give the all-prime factor14/3 <5.',
            'Rank0/1 and independent rank2 exhaust arbitrary rational two-base unit parts.'
        ],
        'scope': 'The proof covers every rational rank-at-most-one unit-part list and every rational two-base input. Finite example checks do not substitute for the displayed general proof.',
        'remaining': 'Intermediate dependent ranks for three or more rational inputs and the full general-number-field refinement.'
    }


def figure(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.size': 10, 'mathtext.fontset': 'stix'})
    p, k = 5, 8
    bound = 5 ** k
    exponent = 3 * bound + 5
    omega = math.log(8) * math.log(4)
    epsilon = np.geomspace(1 / bound, .5, 500)
    logarithm = 92 + np.log(1250 * omega / epsilon)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.4),
                             gridspec_kw={'width_ratios': [1, 1.15]})
    left, right = axes
    left.set_axis_off()
    left.set_xlim(0, 1); left.set_ylim(0, 1)
    left.set_title('One primitive valuation vector')
    boxes = [(.16, r'$8=2^3$', r'$b_1=5^8$'),
             (.50, r'$4=2^2$', r'$b_2=2$'),
             (.84, r'$2=2^1$', r'$b_3=1$')]
    for x, base, coefficient in boxes:
        left.text(x, .82, base, ha='center', va='center', fontsize=15,
                  bbox={'boxstyle': 'round,pad=.35', 'fc': '#eaf2fb', 'ec': '#47789d'})
        left.text(x, .66, coefficient, ha='center', fontsize=12)
        left.annotate('', xy=(.5, .43), xytext=(x, .61),
                      arrowprops={'arrowstyle': '->', 'color': '#47789d', 'lw': 1.5})
    left.text(.5, .35, r'$M=3\cdot5^8+2\cdot2+1$'+'\n'+f'$={exponent:,}$',
              ha='center', va='center', fontsize=14)
    left.text(.5, .14, r'$\Xi=2^M,\qquad v_5(\Xi-1)=2$',
              ha='center', fontsize=15)
    right.loglog(epsilon, omega * logarithm, label=r'$\Omega L$', lw=2)
    right.loglog(epsilon, epsilon * bound, label=r'$\varepsilon r$', lw=2)
    right.set_xlabel(r'$\varepsilon$')
    right.set_ylabel('Factors whose maximum is U')
    right.set_title('Coefficient budgets for the dependent list')
    right.grid(True, which='both', alpha=.2)
    right.legend(loc='upper left')
    fig.suptitle(r'$p=5,\ (a_1,a_2,a_3)=(8,4,2),\ B=5^8,\ B_n=1$', y=.98)
    fig.text(.5, .025, r'$\Omega=(\log8)(\log4),\quad L=92+\log(1250\Omega/\varepsilon).$'
             +'  The plotted factors give bounds; the exact valuation is 2.', ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .07, 1, .93))
    fig.savefig(destination, dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    directory = Path(__file__).resolve().parent
    (directory / 'yu-low-rank-coefficient-refinement-check.json').write_text(
        json.dumps(checks(), indent=2) + '\n', encoding='utf-8')
    figure(directory / 'yu-low-rank-coefficient-refinement.png')
    print('Exact examples and constant comparisons passed; figure rendered.')

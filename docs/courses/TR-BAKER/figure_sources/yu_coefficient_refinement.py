"""Exact constants and a numerical illustration of height inflation.

Original CC0 work by GPT-6 Astra (OpenAI), Ultra. Lemmas 10.224--10.225
and Theorem 10.226 prove the continuous and all-rank statements.
The plotted samples and the finite exact checks do not replace those proofs.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import sys


def certificate():
    checks = {}

    def less(name, left, right):
        left, right = F(left), F(right)
        assert left < right, name
        checks[name] = {'left': str(left), 'right': str(right),
                        'positive_gap': str(right-left)}

    less('exponential_upper_tail', F(8, 3)+F(5, 96), F(11, 4))
    less('log_two_upper', F(25, 36), F(7, 10))
    less('log_five_lower', F(11, 4)**3, 25)
    less('odd_large_prime_scalar', F(20052, 2048), 10)
    less('three_scalar', F(729, 128), 6)
    less('two_maximum', F(41503, 8000), 6)
    less('two_scalar', F(345303, 262144), F(4, 3))
    less('height_parameter_log52', 52, F(8, 3)**5)
    less('exercise_log500', 500, F(8, 3)**7)
    less('exercise_log3', 3, F(8, 3)**2)
    less('exercise_inflation', 116, F(390625, 2))
    profiles = [
        ('p_at_least_five', F(10), 3, F(7, 256), F(245, 4096), F(189, 2048)),
        ('p_three', F(6), 3, F(21, 256), F(1323, 4096), F(567, 2048)),
        ('p_two', F(4, 3), 2, F(13, 32), F(169, 192), F(117, 128)),
    ]
    for name, coefficient, power, base, start, ratio in profiles:
        assert coefficient*2**power*base**2 == start
        assert F(3, 2)**power*base == ratio
        less(name+'_start', start, 1)
        less(name+'_ratio', ratio, 1)
    assert 5**8 == 390625
    assert pow(2, 20, 25) == 1
    assert 5**8 % 20 == 5
    assert (3*pow(2, 5**8, 25)-1) % 25 == 20
    return {
        'state': 'exact_comparisons_passed', 'checks': checks,
        'checked_inequalities': len(checks),
        'example_valuation_at_five': 1,
        'all_rank_argument': 'For every n>=2, (1+1/n)^k <= (3/2)^k. The displayed ratios bound every successor, not a finite sample.',
        'scope': 'Padded-height monotonicity; rational numerical constant at every prime and rank; coefficient refinement for independent rational p-unit parts.',
        'not_proved_here': 'Arbitrary dependent unit parts and the full general-number-field coefficient refinement.',
    }


def figure(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    certificate()
    r = 5**8
    epsilon = np.geomspace(1/r, .5, 500)
    height = np.log(3)
    L = 51+np.log(250/epsilon)
    first, second = height*L, epsilon*r
    inflated = np.maximum(height, second/L)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.7))
    axes[0].loglog(epsilon, first, label=r'$\Omega L=(\log 3)L$', lw=2)
    axes[0].loglog(epsilon, second, label=r'$\varepsilon r$', lw=2)
    axes[0].set_ylabel(r'Factor multiplied by $\mathcal{C}_2(5)$')
    axes[0].set_title('Two branches of the bound')
    axes[0].legend(loc='upper left')
    axes[1].loglog(epsilon, inflated, lw=2, color='#7c3c88', label=r'$w_2^*=\max\{\log 3,\varepsilon r/L\}$')
    axes[1].axhline(height, color='#637583', linestyle='--', label=r'$w_2=\log 3$')
    axes[1].set_ylabel('Last height bound')
    axes[1].set_title('Only the last height is enlarged')
    axes[1].legend(loc='upper left')
    for ax in axes:
        ax.set_xlabel(r'$\varepsilon$')
        ax.grid(True, which='both', alpha=.18)
        ax.set_xlim(1/r, .5)
    fig.suptitle(r'$p=5,\ (a_1,a_2)=(2,3),\ (b_1,b_2)=(5^8,1),\ B_n=1,\ r=390625$', fontsize=12)
    fig.text(.5, .015, r'$L=51+\log(250/\varepsilon)$; plotted values are samples of the explicit formulas. The exact valuation is 1.', ha='center', fontsize=10)
    fig.tight_layout(rect=(0, .055, 1, .93))
    fig.savefig(destination, dpi=160)
    plt.close(fig)


if __name__ == '__main__':
    result = certificate()
    if '--figure' in sys.argv:
        figure(Path(__file__).with_name('yu-coefficient-refinement.png'))
    print(json.dumps(result, indent=2))

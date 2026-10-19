"""Exact scalar checks for the second application bound. CC0.

These rational enclosures accompany the written all-rank proof; the finite
checks do not replace its uniform inequalities.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from yu_application_height_certificate import log_interval, exp_upper

LAMBDA = F(2099, 2100)
ROWS = [
    ('I.1', 1438, 58, 3, 7, F('1.94'), 2, 1),
    ('I.2', 648, 17, 3, 7, F('2.76'), 1, 1),
    ('II', 690, 58, 5, 7, F('0.71'), 2, 1),
    ('III.1', 495, 58, 1, 7, F('1.99'), 2, 1),
    ('III.2', 557, 17, 1, 7, F('3.32'), 1, 1),
    ('IV', 2418, 58, 1, 7, F('3.58'), 2, 1),
    ('V', 406, 58, 4, 13, F('1.48'), 2, 2),
]


def certificate():
    rows = []
    for label, c, rho, p0, a, a1, d0, torsion in ROWS:
        k = LAMBDA * c * torsion / (rho * p0 * F(11, 4))
        a0 = 2 + log_interval(F(a * p0))[0]
        log_k = log_interval(k)[0]
        log_d = log_interval(F(d0))[0]
        exponential = exp_upper(a1)
        slope = k * a0 - exponential
        endpoint = k * (2*a0 + log_d + log_k) - 3*exponential
        coefficient_height = 2*(2*a0 + log_d + log_k) - 2*log_d - 6
        assert slope > 0 and endpoint > 0 and coefficient_height > 0, label
        assert 2*a0 + log_d + log_k > 1
        rows.append({'case': label, 'K_lower': str(k),
                     'linear_slope_lower': str(slope),
                     'n2_endpoint_lower': str(endpoint),
                     'n2_coefficient_height_margin_lower': str(coefficient_height)})

    e_lower = sum(F(1, factorial(i)) for i in range(7))
    assert e_lower == F(1957, 720)
    two_margin = 13*e_lower**2 - 96 - F(9, 512)
    odd_margin = 7*e_lower**2 - 50 - F(3, 32)
    assert two_margin > 0 and odd_margin > 0
    assert 25/(7*e_lower**2) < F(1, 2)
    assert 48/(13*e_lower**2) < F(1, 2)
    circuit_upper = F(24*58**2, 1)/(LAMBDA*200*7**3*F(8, 3)**2)
    assert circuit_upper == F(68121, 411404) and circuit_upper < F(1, 5)
    threshold_lower = LAMBDA*200*F(8, 3)*4*7/58
    assert threshold_lower > 200
    torsion_budget_lower = F(200, 58)*7**2*81
    assert torsion_budget_lower > 7900
    log5 = log_interval(F(5))
    assert exp_upper(F(3))*log5[1]**4 < 135
    assert 2*3*4**2 == 2**5*3 == 96
    assert -1*2*3*4 == -24 and (-24)**2 == 2**2*3**2*4**2 == 576
    assert (96-1)//5 == 19 and (96-1) % 25 != 0
    assert -24-1 == -25 and (576-1)//25 == 23

    # Exact endpoint checks supplement the written monotonicity in r and s.
    envelopes = []
    for r in range(2, 41):
        for s in range(41-r):
            n = r+s+1
            value = F(8*58**2*n, 1)/(LAMBDA*200*7**(r+1)*F(8, 3)**r*2**s)
            assert value <= circuit_upper
            envelopes.append(value)
    return {
        'state': 'exact_scalar_checks_passed',
        'coefficient_height_rows': rows,
        'two_adic_rank_margin': str(two_margin),
        'odd_rank_margin': str(odd_margin),
        'circuit_envelope_upper': str(circuit_upper),
        'circuit_samples': len(envelopes),
        'large_B_threshold_factor_lower': str(threshold_lower),
        'torsion_budget_factor_lower': str(torsion_budget_lower),
        'worked_examples': {'dependent_product': 96, 'transferred_coefficients': [5, 1],
                           'valuation_at_five': 1, 'torsion_product': -24,
                           'squared_product': 576, 'torsion_example_valuations': [2, 2],
                           'M3_first_branch_margin_lower': str(135-exp_upper(F(3))*log5[1]**4)},
        'proof_scope': 'Uniform written envelopes prove all n,r,s; seven exact row comparisons establish the independent coefficient-height conversion. No external theorem substitutes for the programme proof.'
    }


def draw_figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch
    fig, ax = plt.subplots(figsize=(13.5, 6.5))
    ax.set(xlim=(0, 13.5), ylim=(0, 6.5)); ax.axis('off')
    def box(x, y, label, color='#eaf2fb', size=10):
        ax.text(x, y, label, ha='center', va='center', fontsize=size,
                bbox=dict(boxstyle='round,pad=.5', fc=color, ec='#37608c', lw=1.2))
    def arrow(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='->',
                                    mutation_scale=13,color='#37608c',lw=1.2))
    ax.text(6.75,6.2,'The second application estimate: every multiplicative rank',
            ha='center',fontsize=15)
    box(3.2,5.35,'Independent bases: coefficient conversion\nLemma 10.233 and Theorem 10.234')
    box(10.0,5.35,'Dependent list, large-coefficient branch\nThe original greedy basis is retained')
    box(1.55,3.65,r'$B/\log B\leq W_n$'+'\nLocal height inequality',size=11)
    box(4.9,3.65,r'$B/\log B>W_n$'+'\nAll coefficient conditions follow',size=10)
    arrow(2.6,4.85,1.75,4.18);arrow(3.8,4.85,4.65,4.18)
    box(8.2,3.65,'Circuit removes a discarded base\n'+r'$H^\prime/H\leq 2+z/(4\mathrm{e}X_n)$',size=10)
    box(11.65,3.65,'Remove a torsion base\n'+r'$H^\prime/H\leq 2$',size=10)
    arrow(9.4,4.85,8.5,4.18);arrow(10.6,4.85,11.35,4.18)
    box(3.2,1.95,r'$\operatorname{ord}_{\mathfrak{p}}(\Xi-1)<C_n\Omega_n H$',
        color='#e9f5eb',size=13)
    arrow(1.7,3.12,2.8,2.4);arrow(4.7,3.12,3.6,2.4)
    box(10.0,1.95,'Rank reduction absorbs the complete coefficient increase\n'
        +r'$a\mathrm{e}^2-(4\mathrm{e}Pt)^{-1}>2\varkappa$',color='#e9f5eb',size=11)
    arrow(8.5,3.12,9.6,2.4);arrow(11.4,3.12,10.4,2.4)
    arrow(7.1,1.95,5.5,1.95)
    ax.text(3.2,.8,'Rank one has the stronger factor 1/4000.\n'
            'A rank-zero torsion product has its separate local-height bound.',
            ha='center',fontsize=10)
    ax.text(10,.8,'Exact lower margin in the 2-adic absorption:\n'
            +r'$13(1957/720)^2-96-9/512=25049/1036800>0$',
            ha='center',fontsize=11)
    ax.text(6.75,.15,'Lemma 10.235 and Theorem 10.236. All displayed bounds are proved in the lesson; arrows show proof implications.',
            ha='center',fontsize=9)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name('yu-second-application-completion.png'),dpi=160)
    plt.close(fig)


if __name__ == '__main__':
    result = certificate()
    out = Path(__file__).with_name('yu-second-application-completion-check.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    draw_figure()
    print(json.dumps({'state':result['state'],'field_case_checks':len(result['coefficient_height_rows']),
                      'circuit_samples':result['circuit_samples'],
                      'two_adic_rank_margin':result['two_adic_rank_margin'],
                      'worked_examples':result['worked_examples']},indent=2))

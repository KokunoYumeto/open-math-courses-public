"""Exact one-base budgets for Yu's second application constant (CC0).

Theorem 10.161 proves the inequalities for every field in each case.
These rational calculations certify their seven endpoints; plotting
converts the certified values to floats only after the comparisons pass.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json


def certificate():
    rows = []
    # case, c lower, a, degree lower, rho, w_K/q^u lower, log multiplier
    cases = [
        ('I.1', 1438, 7, 2, 58, 1, F(5, 3)),
        ('I.2', 648, 7, 1, 17, 1, F(5, 3)),
        ('II', 690, 7, 2, 58, 1, F(5, 3)),
        ('III.1', 495, 7, 2, 58, 1, F(23, 16)),
        ('III.2', 557, 7, 1, 17, 1, F(23, 16)),
        ('IV', 2418, 7, 2, 58, 1, F(5, 3)),
        ('V', 406, 13, 2, 58, 2, F(5, 3)),
    ]
    for label, c, a, degree, rho, torsion, multiplier in cases:
        A = F(14, 3) if degree == 1 else F(16, 3)
        lower = 8 * c * a * F(27, 10) * torsion * A / rho
        logarithm = multiplier / lower
        height = 1 / (2 * c * a * F(27, 10) * degree)
        total = logarithm + height
        gap = F(1, 4000) - total
        assert gap > 0
        rows.append(dict(case=label, c_lower=c, a=a, degree_lower=degree,
                         rho=rho, torsion_ratio_lower=torsion,
                         A_lower=str(A), logarithm_multiplier=str(multiplier),
                         U_over_H_lower=str(lower),
                         logarithmic_upper_share=str(logarithm),
                         raw_residue_height_upper_share=str(height),
                         total_upper_share=str(total),
                         positive_gap_below_1over4000=str(gap)))
    exact_powers = []
    for k in range(1, 7):
        value = pow(4, 3 ** k) - 1
        valuation = 0
        while value % 3 == 0:
            value //= 3
            valuation += 1
        assert valuation == k + 1
        exact_powers.append(dict(k=k, valuation=valuation))
    assert F(4 * 648 * 7, 4000) > F(9, 2)
    assert F(8, 3) ** 2 > 7
    assert F(9, 2) * 7 * 4 == 126
    return dict(state='passed', exact_field_cases=rows,
                example_exact_powers=exact_powers,
                all_k_example='The proved power identity gives k+1 for every k>=1; the estimate exceeds 126k.',
                minimum_gap=str(min(F(r['positive_gap_below_1over4000']) for r in rows)),
                all_prime_III_scope='(p-1)/(p-2)>1; the case table uses its lower bound1.',
                proof_scope='One non-torsion local unit, original residue order, every nonzero integer exponent.')


def draw(data, path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    rows = data['exact_field_cases']
    log = [float(4000 * F(r['logarithmic_upper_share'])) for r in rows]
    height = [float(4000 * F(r['raw_residue_height_upper_share'])) for r in rows]
    fig, ax = plt.subplots(figsize=(11.5, 7.0), facecolor='white')
    ax.set_facecolor('#f5f7fb')
    for i, r in enumerate(rows):
        ax.barh(i, log[i], color='#285f9e', height=.56,
                label='Exponent logarithm' if i == 0 else None)
        ax.barh(i, height[i], left=log[i], color='#d58a27', height=.56,
                label='Original residue-order height term' if i == 0 else None)
        ax.text(log[i] + height[i] + .012, i,
                f"{log[i] + height[i]:.3f}", va='center', fontsize=11)
    ax.axvline(1, color='#a62836', linewidth=2)
    ax.set_yticks(range(len(rows)), [r['case'] for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 1.16)
    ax.set_xlabel(r'Upper budgets divided by $U_2/4000$, where $U_2=(t/d)\mathcal{T}_2$')
    ax.grid(axis='x', color='#d4dce8', linewidth=.6)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', bbox_to_anchor=(-.02, -.16), frameon=False,
              ncol=1, fontsize=11)
    fig.suptitle('The second one-base estimate: both contributions fit',
                 x=.08, y=.965, ha='left', fontsize=19, fontweight='bold')
    ax.set_title('Seven exact field cases; the red line is the proved allowance',
                 loc='left', pad=16, fontsize=12)
    fig.text(.08, .025,
             'Every stacked endpoint is strictly below 1. Decimal labels only summarize exact rational bounds.\n'
             'Theorem 10.161 proves the uniform comparisons; the source program retains every positive gap.',
             fontsize=10.5, color='#303b4b')
    fig.subplots_adjust(left=.10, right=.96, top=.84, bottom=.27)
    fig.savefig(path, dpi=160, facecolor='white', metadata={'Software': 'Original CC0 mathematical figure'})
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', type=Path)
    parser.add_argument('--figure', type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.certificate:
        args.certificate.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    if args.figure:
        draw(result, args.figure)
    print(json.dumps(dict(state=result['state'], cases=7, minimum_gap=result['minimum_gap'])))

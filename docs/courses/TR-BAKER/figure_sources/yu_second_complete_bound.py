"""Exact endpoint checks and proof map for the complete second Yu estimate.

Original CC0 work by GPT-6 Astra (OpenAI), Ultra. The accompanying proof
establishes the all-rank inequalities and the actual zero inductions.
No finite calculation in this file substitutes for those arguments.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys


def log_interval(x, terms=64):
    x = F(x)
    assert x >= 1
    power = 0
    while x > 2:
        x /= 2
        power += 1

    def unit(z):
        y = (z-1)/(z+1)
        lo = 2*sum((y**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
        tail = 2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
        return lo, lo+tail

    a, b = unit(x)
    c, d = unit(F(2))
    return a+power*c, b+power*d


def certificate():
    checks = {}

    def positive(name, gap):
        assert gap > 0, name
        small = F(gap.numerator*10**10//gap.denominator-1, 10**10)
        assert 0 < small < gap
        checks[name] = {'strict_gap_lower_bound': str(small)}

    e0 = sum((F(1, factorial(k)) for k in range(11)), F(0))
    l5 = log_interval(5)[0]
    positive('exceptional_rank_two_constant', F(495,1794)*F(3,8)*e0**2*l5-F(123,100))
    positive('other_field_constant', F(3,2)-F(123,100))
    positive('degree_one_constant', F(11,8)-F(123,100))
    rank_two = F(3,2)*F(100,123)/2
    assert rank_two == F(25,41)
    positive('rank_two_target_gap', 1-rank_two)
    positive('weighted_first_rank_one_sum', 1-F(11,4000))
    positive('second_rank_one_sum', F(1,3000)-F(13,50000))
    positive('example_gamma', 7*F(27,10)**2/2-25)
    residue_upper = F(9,4)*F(13,8)**3
    positive('example_residue_ceiling', 10-residue_upper)
    positive('example_first_residue_entry', residue_upper-F(5,2))
    positive('example_weight_allowance', F(25,3)-2)
    positive('log2_lower', log_interval(2)[0]-F(2,3))
    positive('log3_lower', log_interval(3)[0]-1)
    positive('log6_upper', 2-log_interval(6)[1])
    positive('log5_upper', F(13,8)-log_interval(5)[1])
    assert 2*3*11-1 == 5*13 and 13 % 5 != 0
    return {
        'state': 'exact_comparisons_passed',
        'checks': checks,
        'checked_inequalities': len(checks),
        'rank_two_ratio_bound': str(rank_two),
        'example_original_bases': [2, 3, 11],
        'example_reduced_bases': [6, 11],
        'example_original_delta': 1,
        'example_reduced_delta': 2,
        'example_valuation_at_five': 1,
        'all_rank_argument': 'The analytic proof of F(j+1)/F(j)>exp(1), not sampled ranks, gives the complete quotient bound.',
        'coefficient_scope': 'Original integer coefficients retained; rational reduced coefficients are never substituted into their height data.',
    }


def figure(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    certificate()
    fig, ax = plt.subplots(figsize=(13.8, 7.0))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')

    def box(x, y, width, height, text, color='#e7effa', fontsize=10):
        ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.08',
                                  facecolor=color,edgecolor='#526479',linewidth=1))
        ax.text(x+width/2,y+height/2,text,ha='center',va='center',fontsize=fontsize,
                linespacing=1.45)

    def arrow(a, b):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'#526479','lw':1.3})

    box(3.8,5.8,6.4,.85,'Original target T = C2(n) h2 × height product\nLeast integral-form rank r with the second allowance',fontsize=12)
    columns=[(.15,2.7),(3.15,2.8),(6.3,3.0),(9.85,3.8)]
    labels=[
        'r = 1\nElementary residue-order bound\nProposition 10.193\nValuation / T < 1/3000',
        'r = 2, original n ≥ 3\nWeighted first estimate\nLemmas 10.221–10.222\nValuation / T < 25/41',
        'r ≥ 3, r/t − A0 ≤ 3/5\nWeighted first estimate\nC2(r)/C1(r) > 3/2\nValuation / T < 1',
        'r ≥ 3, r/t − A0 > 3/5\nAssume valuation ≥ T\nActual hatted kernel\nTheorem 10.203',
    ]
    for (x,width),text in zip(columns,labels):
        box(x,3.5,width,1.65,text,fontsize=9.7)
        arrow((7,5.72),(x+width/2,5.23))
    box(7.0,1.15,3.1,1.65,'IG ≤ IM\nActual zeros: Corollary 10.209\nRank reduction: Theorem 10.204\nRank-product factor < 10⁻⁶\nContradicts least rank','#e3f1e9',9.3)
    box(10.55,1.15,3.1,1.65,'IM < IG\nFixed-order successors\nTheorems 10.216–10.217\nMore roots than degree\nContradicts nonzero polynomial','#e3f1e9',9.3)
    arrow((11.75,3.42),(8.55,2.88))
    arrow((11.75,3.42),(12.1,2.88))
    box(.3,1.25,5.8,1.35,'At every rank: original integer coefficients and weighted forms.\nActual intermediate residue factors cancel.\nOriginal length n = 2: Theorem 10.220.',color='#f5eedc',fontsize=10.4)
    ax.text(7,.43,'Theorem 10.223: the second estimate for every original n ≥ 2',
            ha='center',va='center',fontsize=13,fontweight='bold')
    fig.tight_layout()
    fig.savefig(destination,dpi=160,bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    result = certificate()
    if '--figure' in sys.argv:
        figure(Path(__file__).with_name('yu-second-complete-bound.png'))
    print(json.dumps(result, indent=2))

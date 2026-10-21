"""Exact rational reductions and a proof diagram for TR-BAKER-10. CC0.

Original exposition, checks and figure: GPT-6 Astra (OpenAI), Ultra.
Human-source target: Theorem 2.3, Bugeaud, On the digital representation
of integers with bounded prime factors, freely accessible author version:
https://irma.math.unistra.fr/~bugeaud/travaux/StroblRev1.pdf
The proof is in TR-BAKER-10 Lemma10.230, Proposition10.231 and Theorem10.232.
Finite arithmetic examples check identities; they are not the all-rank proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd, prod
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def vp(x, p):
    x = Q(x)
    if not x:
        return float('inf')
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        v += 1
        a //= p
    while b % p == 0:
        v -= 1
        b //= p
    return v


def product(bases, coefficients):
    return prod((Q(a)**b for a, b in zip(bases, coefficients)), start=Q(1))


def checks():
    rows = []
    for p, a, last in [(2, 3, 5), (3, 2, 5), (5, 2, 3), (7, 2, 3)]:
        for power in [2, 3, 4]:
            for sign in [-1, 1]:
                bases = [-a, sign*a**power, last]
                primitive = [-power, 1, 0]
                assert gcd(*primitive) == 1
                eta = product(bases, primitive)
                assert eta in [Q(-1), Q(1)]
                circuit = [2*k for k in primitive]
                assert product(bases, circuit) == 1
                pivot = 1
                for d in [0, 1, 2]:
                    for scalars in [(0, 1, 1), (1, 1, 1), (-2, 3, 1)]:
                        b = [p**d*t for t in scalars]
                        transferred = [circuit[pivot]*b[i]-circuit[i]*b[pivot]
                                       for i in range(3) if i != pivot]
                        kept = [bases[i] for i in range(3) if i != pivot]
                        xi = product(bases, b)
                        assert product(kept, transferred) == xi**circuit[pivot]
                        assert vp(transferred[-1], p) == d+vp(2, p)
                        assert min(vp(x, p) for x in transferred) == vp(transferred[-1], p)
                        if xi != 1:
                            assert vp(xi-1, p) <= vp(xi**circuit[pivot]-1, p)
                        rows.append({'p': p, 'bases': bases, 'b': b,
                                     'relation_sign': int(eta), 'transferred': transferred,
                                     'minimum_before': d, 'minimum_after': d+vp(2, p)})
    for p, a, b, last in [(2, 3, 5, 7), (3, 2, 5, 7), (5, 2, 3, 7), (7, 2, 3, 11)]:
        bases = [a, -b, a*b, last]
        k = [-1, -1, 1, 0]
        assert product(bases, k) == -1
        for d in [0, 1, 2]:
            coeff = [2*p**d, -p**d, 3*p**d, p**d]
            out = [2*coeff[i]-2*k[i]*coeff[2] for i in [0, 1, 3]]
            xi = product(bases, coeff)
            assert product([bases[i] for i in [0, 1, 3]], out) == xi**2
            assert min(vp(z, p) for z in out) == d+vp(2, p)
            rows.append({'p': p, 'bases': bases, 'b': coeff, 'relation_sign': -1,
                         'transferred': out, 'minimum_before': d,
                         'minimum_after': d+vp(2, p)})
    # Explicit Cramer reductions of valuation vectors (standard basis + their sum).
    cramer = []
    for generators in [[2, 3], [2, 3, 5], [2, 3, 5, 7]]:
        bases = generators+[prod(generators)]
        for sign in [-1, 1]:
            bases[-1] = sign*prod(generators)
            coeff = list(range(1, len(bases)+1))
            out = [2*(coeff[j]+coeff[-1]) for j in range(len(generators))]
            assert product(bases, coeff)**2 == product(generators, out)
            cramer.append({'bases': bases.copy(), 'b': coeff, 'D': 2, 'M': out})
    # Nontrivial lattice index: determinant4, even powering exponent8.
    assert product([9,25,15],[1,-1,1])**8 == product([9,25],[12,-4])
    cramer.append({'bases':[9,25,15],'b':[1,-1,1],'D':8,'M':[12,-4]})
    xi = Q(-405)
    assert xi**2 == Q(-3)**8*Q(5)**2 == 164025
    assert vp(xi-1, 2) == 1 and vp(xi**2-1, 2) == 3
    assert vp(xi**4-1, 2) == 4
    return {'state': 'exact_reductions_passed', 'circuit_examples': rows,
            'circuit_example_count': len(rows), 'cramer_examples': cramer,
            'uniform_positive_gap': 'D_n-(n+n^2)=5(n+1)^2>0',
            'redundant_rank_constant_ratio_below': str(Q(5, 512)),
            'induction_constant_ratio_below': str(Q(1, 128)),
            'proof_scope': 'Every rational rank and n>=2, with the exact original coefficient constant and auxiliary parameter; zero non-distinguished coefficients allowed.',
            'coefficient_domain': 'rational numbers',
            'proof_not_sampling': 'The all-rank proof uses determinant expansion, primitive circuits, exact parameter cancellation and induction. Finite examples validate arithmetic and signs only.'}


def figure(destination):
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.6))
    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    def box(ax, x, y, text, color='#eaf3fc', size=11):
        ax.text(x, y, text, ha='center', va='center', fontsize=size,
                bbox={'boxstyle': 'round,pad=.55', 'fc': color, 'ec': '#386488'})
    def arrow(ax, start, end):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops={'arrowstyle': '->', 'color': '#386488', 'lw': 1.6})
    a, b = axes
    a.set_title('Two exhaustive cases for the distinguished vector', fontsize=13, pad=10)
    box(a, .50, .88, 'Intermediate rank: 2 ≤ s < n')
    box(a, .26, .63, 'Last vector is in\nthe span of the others')
    box(a, .75, .63, 'Last vector increases\nthe preceding rank')
    arrow(a, (.43, .82), (.26, .73)); arrow(a, (.57, .82), (.75, .73))
    box(a, .26, .36, 'Cramer reduction\nW ≤ V; coefficient cost < 5U', size=10)
    box(a, .75, .36, 'Primitive circuit avoids n\nε′B′/B′ₙ = εB/Bₙ; U′ ≤ 2U', size=10)
    arrow(a, (.26, .54), (.26, .45)); arrow(a, (.75, .54), (.75, .45))
    box(a, .50, .10, r'$v_p(\Xi-1)<\mathcal{C}_n(p)U$', '#e8f5e9', 15)
    arrow(a, (.26, .27), (.40, .15)); arrow(a, (.75, .27), (.60, .15))
    b.set_title('Exact sign and coefficient transfer at p = 2', fontsize=13, pad=10)
    box(b, .50, .88, r'$(c_1,c_2,c_3)=(-3,27,5),\quad b=(1,1,1)$')
    box(b, .50, .65, r'$(-3)^{-3}27=-1$'+'\n'+r'$\kappa=(-6,2,0),\quad x=2$')
    arrow(b, (.50, .81), (.50, .74))
    box(b, .50, .39, r'$\Xi^2=(-405)^2=(-3)^8 5^2=164025$'+'\n'+r'$b^\prime=(8,2),\quad\min v_2(b^\prime)=1$', '#e8f5e9')
    arrow(b, (.50, .55), (.50, .48))
    b.text(.50, .16, r'$v_2(\Xi-1)=1\leq3=v_2(\Xi^2-1)$', ha='center', fontsize=14)
    b.text(.50, .06, 'The doubled relation kills the sign.\nIts common factor preserves the coefficient minimum.', ha='center', fontsize=10)
    fig.suptitle('All rational inputs: exact reductions preserve the coefficient refinement', fontsize=16, y=.98)
    fig.text(.50, .015, 'Lemma 10.230 • Proposition 10.231 • Theorem 10.232 • Solution 91.  Bounds and identities are proved in the lesson.', ha='center', fontsize=10)
    fig.subplots_adjust(left=.03, right=.98, bottom=.10, top=.87, wspace=.13)
    fig.savefig(destination, dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    results = checks()
    (here/'yu-rational-coefficient-refinement-check.json').write_text(json.dumps(results, indent=2)+'\n')
    figure(here/'yu-rational-coefficient-refinement.png')
    print(json.dumps({k: results[k] for k in ['state', 'circuit_example_count', 'uniform_positive_gap']}))

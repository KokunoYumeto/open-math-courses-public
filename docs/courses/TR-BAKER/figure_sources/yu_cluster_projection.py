"""Exact example and figure for TR-BAKER Theorems 10.180--10.183. CC0.

The finite calculation checks the displayed example, not the all-parameter
proofs. Run with Python, SymPy and matplotlib. No source download is needed.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial, gcd, lcm, comb
import hashlib
import json


def valuation(a, p=3):
    a = Fraction(a)
    if not a:
        return None
    n, d = abs(a.numerator), a.denominator
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    while d % p == 0:
        d //= p
        result -= 1
    return result


def rising_delta(a, t):
    out = Fraction(1)
    for j in range(1, t + 1):
        out *= Fraction(a + j, j)
    assert out.denominator == 1
    return out.numerator


def exact_example():
    import sympy as sy
    from sympy.polys.matrices import DomainMatrix

    u1, u2 = Fraction(10), Fraction(3281, 500)
    xi = u1**3 * u2
    assert xi == 1 + 3**8
    assert (valuation(u1 - 1), valuation(u2 - 1), valuation(xi - 1)) == (2, 3, 8)
    residues = {}
    modulus = 27
    for x in range(6):
        for y in range(6):
            a = u1**x * u2**y
            residue = (a.numerator * pow(a.denominator, -1, modulus)) % modulus
            residues.setdefault(residue, []).append((x, y))
    support = residues[1]
    assert support == [(x, y) for x in [0, 3] for y in range(6)]
    assert sorted(map(len, residues.values())) == [12, 12, 12]
    assert valuation(u1**3 - 1) == 3
    # The pair (3,1) has unprojected frequency log(xi) and projected frequency zero.
    assert 3 - 3 * 1 == 0

    X = sy.Symbol('X')
    cols = [(a, ell, x, y) for a in range(2) for ell in [1, 2] for x, y in support]
    jets = [(t0, t1) for t0 in range(3) for t1 in range(3 - t0)]
    rows = [(s, t0, t1) for s in [-1, 0, 1] for t0, t1 in jets]
    polynomials = {(a, ell): ((X + a + 1) * (X + a + 2) / 2)**ell
                   for a in range(2) for ell in [1, 2]}
    scalars = {(a, ell, s, t): Fraction(sy.diff(poly, X, t).subs(X, s)
                                     * sy.Rational(2**t, factorial(t)))
               for (a, ell), poly in polynomials.items()
               for s in [-1, 0, 1] for t in range(3)}
    matrix = []
    for s, t0, t1 in rows:
        row = [scalars[a, ell, s, t0] * rising_delta(x - 3 * y, t1)
               * (u1**x * u2**y)**s for a, ell, x, y in cols]
        denominator = lcm(*(v.denominator for v in row))
        integer_row = [int(v * denominator) for v in row]
        common = gcd(*integer_row)
        if common:
            integer_row = [v // common for v in integer_row]
        matrix.append(integer_row)
    M = sy.Matrix(matrix)
    nullspace = DomainMatrix.from_Matrix(M).nullspace().to_Matrix()
    assert nullspace.rows > 0
    kernel = [int(x) for x in nullspace.row(0)]
    common = gcd(*kernel)
    assert common
    kernel = [x // common for x in kernel]
    if next(x for x in kernel if x) < 0:
        kernel = [-x for x in kernel]
    assert M * sy.Matrix(kernel) == sy.zeros(len(rows), 1)
    assert gcd(*kernel) == 1
    # Check the original, uncleared equations as well.
    for s, t0, t1 in rows:
        total = sum(Fraction(c) * scalars[a, ell, s, t0]
                    * rising_delta(x - 3 * y, t1) * (u1**x * u2**y)**s
                    for c, (a, ell, x, y) in zip(kernel, cols))
        assert total == 0
    assert len(cols) == 48 and len(rows) == 18
    beta = min(valuation(c) for c in kernel if c)
    assert beta == 0
    # N=2, D=4, H=8, mu=3, and B=C0=0.
    assert 8 + 4 * (Fraction(2) + Fraction(1, 2)) == 3 * 3 * 2 == 18
    assert Fraction(18, 48 - 18) == Fraction(3, 5)
    assert Fraction(4 * 25, 3) > Fraction(11, 6) * 18
    return {
        'prime': 3, 'u1': str(u1), 'u2': str(u2), 'xi': str(xi),
        'original_coefficient_vector': [3, 1],
        'unit_valuations': [2, 3], 'relation_valuation': 8,
        'j': 2, 'm': 1, 'actual_unit_quotient_order': 3,
        'selected_support': support, 'columns': cols, 'rows': rows,
        'primitive_integral_kernel': kernel,
        'kernel_beta': beta, 'all_18_original_equations_zero': True,
        'matrix_nullity': nullspace.rows, 'column_count': 48, 'row_count': 18,
        'height_row_coefficient': '3/5', 'analytic_radius_exponent': 2,
        'normalizing_valuation': 10, 'output_valuation_lower_bound': 8,
        'budget_left': 18, 'budget_right': 18,
        'scope': 'Exact example only. General statements are proved in the lesson.'
    }


def figure(data, destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 12})
    fig = plt.figure(figsize=(10.8, 7.2), layout='constrained')
    grid = fig.add_gridspec(2, 2, height_ratios=[1, .65])
    axes = [fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1]), fig.add_subplot(grid[1, :])]
    colors = ['#167d8d', '#d89827', '#8c6bb1']
    ax = axes[0]
    for x in range(6):
        for y in range(6):
            ax.scatter(x, y, color=colors[x % 3], s=28, alpha=1 if x % 3 == 0 else .35)
    ax.scatter([0, 3], [0, 1], s=135, facecolors='none', edgecolors='#253849', linewidths=1.2)
    ax.set(xlabel=r'$\lambda_1$', ylabel=r'$\lambda_2$', xticks=range(6), yticks=range(6),
           title='Selected quotient class modulo 27\n12 exponents; all four polynomial indices')
    ax.set_aspect('equal')

    ax = axes[1]
    labels = [r'$\log u_1$', r'$\log u_2$', 'Selected quotient\nproved minimum', r'$\log\Xi$']
    values = [2, 3, 3, 8]
    bars = ax.barh(labels, values, color=['#9fb6bc', '#9fb6bc', '#167d8d', '#d89827'])
    ax.axvline(2.5, color='#b33e35', linestyle='--', label=r'$N+1/(p-1)=5/2$')
    for bar, value in zip(bars, values):
        ax.text(value + .12, bar.get_y() + bar.get_height()/2, str(value), va='center')
    ax.set(xlim=(0, 9), xlabel=r'$3$-adic valuation', title='Combined frequencies\npermit N = 2')
    ax.legend(loc='lower right', fontsize=10)
    ax.invert_yaxis()

    ax = axes[2]
    bars = ax.bar(['Before\nselection', 'Selected\ncolumns', 'Full\nrow list'], [144, 48, 18],
                  color=['#9fb6bc', '#167d8d', '#d89827'])
    for bar, value in zip(bars, [144, 48, 18]):
        ax.text(bar.get_x()+bar.get_width()/2, value+3, str(value), ha='center')
    ax.set(ylim=(0, 165), ylabel='Exact count', title='A global kernel and a local budget')
    ax.text(.98, .90, 'Analytic budget\n'+r'$18=10+8$'+'\nnormalization + precision',
            transform=ax.transAxes, ha='right', va='top', fontsize=10)
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.12)
        ax.set_axisbelow(True)
    fig.savefig(destination, dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    data = exact_example()
    figure(data, here/'yu-cluster-projection.png')
    target = here/'yu-cluster-projection-example.json'
    target.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: data[k] for k in ['column_count', 'row_count', 'matrix_nullity',
          'kernel_beta', 'all_18_original_equations_zero', 'normalizing_valuation',
          'output_valuation_lower_bound']}))

"""Exact examples for local coefficients, translation and bounded products."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import reduce
from math import lcm, log
from pathlib import Path
import json
import sympy as s

checks = Counter()


def check(value, family):
    assert bool(value), family
    checks[family] += 1


ORDER = 30


def mul(a, b):
    c = [Q(0)] * (ORDER + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:ORDER + 1 - i]):
                if y:
                    c[i + j] += x * y
    return c


def plus(*series):
    return [sum(values, Q(0)) for values in zip(*series)]


def scale(a, c):
    return [c*x for x in a]


def power(a, n):
    out = [Q(1)] + [Q(0)] * ORDER
    for _ in range(n):
        out = mul(out, a)
    return out


def monomial(n, c=1):
    out = [Q(0)] * (ORDER+1)
    out[n] = Q(c)
    return out


def valuation(a, p):
    a = Q(a)
    assert a
    def v(n):
        n = abs(n)
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        return e
    return v(a.numerator) - v(a.denominator)


series_by_curve = {}
for A, B in [(Q(0), Q(-2)), (Q(-1), Q(0)),
             (Q(-1, 16), Q(0)), (Q(0), Q(-2, 729))]:
    t = monomial(1)
    st = monomial(0, 0)
    for _ in range(ORDER):
        st = plus(monomial(3), scale(mul(t, power(st, 2)), A),
                  scale(power(st, 3), B))
    check(st == plus(monomial(3), scale(mul(t, power(st, 2)), A),
                     scale(power(st, 3), B)), 'formal_curve_equation')
    denominator = plus(monomial(0), scale(mul(t, st), -2*A),
                       scale(power(st, 2), -3*B))
    inverse = [Q(1)] + [Q(0)]*ORDER
    for n in range(1, ORDER+1):
        inverse[n] = -sum(denominator[j]*inverse[n-j]
                          for j in range(1, n+1))
    ell = [Q(0)] + [inverse[n-1]/n for n in range(1, ORDER+1)]
    # Independent closed coefficient formula versus formal differential.
    for n in range(1, ORDER+1):
        expected = Q(0)
        for a in range(n//4+1):
            for b in range(n//6+1):
                if 4*a+6*b == n-1:
                    c = s.factorial(2*a+3*b)//(
                        s.factorial(a)*s.factorial(b)*s.factorial(a+2*b))
                    expected += Q(int(c), n)*A**a*B**b
        check(ell[n] == expected, 'logarithm_coefficients')
    for p in [2, 3, 5, 7]:
        exponent = max(Q(0), -Q(valuation(A, p), 4) if A else Q(0),
                       -Q(valuation(B, p), 6) if B else Q(0))
        for n in range(1, ORDER+1):
            if st[n]:
                check(valuation(st[n], p) >= -(n-3)*exponent,
                      'finite_coordinate_weights')
            if ell[n]:
                check(valuation(n*ell[n], p) >= -(n-1)*exponent,
                      'finite_logarithm_weights')
    series_by_curve[(A, B)] = st, ell


def delta_dynamic(N, d):
    """Prime-by-prime knapsack maximum, with at most d factors."""
    value = 1
    for p in s.primerange(2, N+1):
        # best[b] includes all products using the currently allowed factors
        # and with sum of factor values at most b.
        best = [0]*(N+1)
        for _ in range(min(d, N)):
            best = [max([best[b]] + [best[b-n]+valuation(n, p)
                                      for n in range(1, b+1)])
                    for b in range(N+1)]
        value *= int(p)**best[N]
    return value


def delta_enumerated(N, d):
    """Independent enumeration of integer products, retaining every length."""
    values = {1}
    def visit(budget, factors, current):
        values.add(current)
        if factors:
            for n in range(1, budget+1):
                visit(budget-n, factors-1, current*n)
    visit(N, d, 1)
    return reduce(lcm, values, 1)


for N in range(13):
    for d in range(5):
        check(delta_dynamic(N, d) == delta_enumerated(N, d),
              'bounded_product_denominator_two_methods')

denominator_data = []
for N in range(1, 81):
    value = delta_dynamic(N, 2)
    LN = reduce(lcm, range(1, N+1), 1)
    LN2 = reduce(lcm, range(1, N//2+1), 1)
    check((LN*LN2) % value == 0, 'denominator_divisibility_bound')
    # Exact integer version of Delta_N(2) <= 2^(3N).
    check(value <= 2**(3*N), 'linear_logarithmic_denominator_bound')
    denominator_data.append({'N': N, 'delta_2': str(value)})

# Two-variable products: denominators involve the total order, not an
# independently chosen bound in each variable.
ell1 = series_by_curve[(Q(-1), Q(0))][1]
ell2 = series_by_curve[(Q(0), Q(-2))][1]
for r in range(5):
    for a in range(r+1):
        one, two = power(ell1, a), power(ell2, r-a)
        for i in range(13):
            for j in range(13-i):
                c = int(s.binomial(r, a))*one[i]*two[j]
                if c:
                    check((delta_dynamic(i+j, r)*c).denominator == 1,
                          'two_variable_logarithm_denominators')

X, Y, Z = s.symbols('X Y Z')
A = 3*Y**2+30*Y*Z+18*Z**2-31*X*Z-10*X*Y
B = 45*X**2-27*X*Y+5*Y**2-19*Y*Z-30*Z**2
C = Y**2+27*X*Z-9*X**2-25*Z**2
curve = Y**2*Z-X**3+2*Z**3
den = 3*Z-X
nx = (5*Z-Y)**2*Z-(X+3*Z)*den**2
ny = -Y*den**3+(5*Z-Y)*(X*den**2-nx)
factor = (3*X-Y-4*Z)*(3*X+Y-14*Z)
check(s.expand(A*Z*den**2-C*nx-curve*factor) == 0,
      'translated_chord_polynomial_identity')
check(s.expand(B*Z*den**3-C*ny-curve*(Y-5*Z)*factor) == 0,
      'translated_chord_polynomial_identity')

st, ell = series_by_curve[(Q(0), Q(-2))]
translated = scale(plus(scale(t, -31), scale(power(t, 2), -135),
                        scale(st, -207), scale(mul(t, st), -155),
                        scale(power(st, 2), 180)), Q(1, 25))
check(translated[0] == 0 and translated[1] == Q(-31, 25),
      'first_translated_jet')
check(Q(-31, 25) == Q(1, 5)*Q(-31, 5),
      'normalizing_scalar_identity')
for k in range(1, 9):
    coefficients = power(translated, k)
    check(all(c == 0 for c in coefficients[:k]), 'first_total_order_of_powers')
    check(coefficients[k] == Q(-31, 25)**k, 'first_coefficient_of_powers')
    check(coefficients[k] == Q(1, 5)**k*Q(-31, 5)**k,
          'first_jet_unit_factor_for_powers')

output = {
    'utc': datetime.now(timezone.utc).isoformat(), 'state': 'passed',
    'checks': dict(checks), 'total': sum(checks.values()),
    'formal_series_order': ORDER, 'denominator_figure_data': denominator_data,
    'translation_example': {'c': '-31/25', 'b': '1/5', 'f': '-31/5'},
    'limits': 'Exact finite examples supplement the written proofs. They do not establish the global height theorem or the final quantitative logarithm estimate by themselves.'
}
Path(__file__).with_suffix('.json').write_text(
    json.dumps(output, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'state': 'passed', 'total': output['total'], 'checks': dict(checks)}))

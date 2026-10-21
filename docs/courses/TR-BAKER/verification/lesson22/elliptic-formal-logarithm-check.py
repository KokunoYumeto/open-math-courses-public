"""Exact coefficient, denominator, and first-jet examples."""
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from math import factorial, lcm, prod
from pathlib import Path
import json

import sympy as S

checks = Counter()


def verify(condition, family):
    assert bool(condition), family
    checks[family] += 1


t, A, B = S.symbols("t A B")
order = 25


def truncate(p, variable=t, bound=order):
    return sum(
        c * variable**m[0]
        for m, c in S.Poly(S.expand(p), variable).terms()
        if m[0] < bound
    )


# Construct the implicit coordinate recursively, independently of its
# coefficient formula. Invert the unit differential denominator geometrically.
s = S.Integer(0)
for _ in range(7):
    s = truncate(t**3 + A * t * s**2 + B * s**3)
verify(truncate(s - t**3 - A*t*s**2 - B*s**3) == 0, "implicit_coordinate")
unit_tail = truncate(2*A*t*s + 3*B*s**2)
omega = S.Integer(1)
power = S.Integer(1)
for _ in range(1, 7):
    power = truncate(power * unit_tail)
    omega += power
omega = truncate(omega)
verify(truncate(omega * (1-unit_tail)) == 1, "implicit_coordinate")
verify(truncate((1-unit_tail)*S.diff(s,t) - 3*t**2-A*s**2,
                bound=order-1) == 0, "implicit_coordinate")

logarithm = S.integrate(omega, t)
formula = S.Integer(0)
for a in range(7):
    for b in range(5):
        n = 4*a+6*b+1
        if n <= order:
            C = factorial(2*a+3*b)//(factorial(a)*factorial(b)*factorial(a+2*b))
            formula += S.Rational(C,n)*A**a*B**b*t**n
for n in range(1, order+1):
    verify(S.expand(logarithm-formula).coeff(t,n) == 0,
           "explicit_logarithm_coefficients")
    coeff = S.Poly(S.expand(n*logarithm.coeff(t,n)), A, B)
    verify(all(c.is_Integer for c in coeff.coeffs()),
           "explicit_logarithm_coefficients")
    verify(all(4*m[0]+6*m[1] == n-1 for m,c in coeff.terms() if c != 0),
           "weighted_homogeneity")


@lru_cache(None)
def products(budget, factors):
    result = {1}
    if factors:
        for first in range(1, budget+1):
            result.update(first*p for p in products(budget-first,factors-1))
    return frozenset(result)


def delta(budget, factors):
    return lcm(*products(budget,factors))


for N in range(1, 17):
    L = lcm(*range(1, N+1))
    verify(L <= 4**(N-1), "least_common_multiple_bound")
    for d in range(1, 5):
        upper = prod(lcm(*range(1, N//j+1)) for j in range(1,min(d,N)+1))
        verify(upper % delta(N,d) == 0, "bounded_product_denominators")
verify(delta(6,2) == 360, "bounded_product_denominators")

# Two curves and a polynomial of degree three in the additive coordinate.
u, v, beta1, beta2 = S.symbols("u v beta1 beta2")
l1 = truncate(logarithm.subs({A:-1,B:0}), bound=13).subs(t,u)
l2 = truncate(logarithm.subs({A:0,B:1}), bound=13).subs(t,v)
q = beta1*l1+beta2*l2
P = S.Poly(S.expand(1+(2+u)*q+(v-3)*q**2+q**3),u,v)
for (i,j), coefficient in P.terms():
    if i+j <= 12:
        cleared = S.Poly(S.expand(delta(i+j,3)*coefficient), beta1,beta2)
        verify(all(c.is_Integer for c in cleared.coeffs()),
               "two_curve_parameter_change")
        verify(cleared.total_degree() <= 3, "two_curve_parameter_change")

# Invert the logarithm successively; do not use a precomputed reversion.
z, beta = S.symbols("z beta")
ell = truncate(logarithm.subs({A:-1,B:0}), bound=14)
inverse = z
for n in range(2, 10):
    error = S.expand(ell.subs(t,inverse)).coeff(z,n)
    inverse -= error*z**n
    inverse = truncate(inverse,variable=z,bound=10)
verify(inverse == z+S.Rational(2,5)*z**5+S.Rational(2,15)*z**9,
       "first_jet_and_later_coefficient")
H = S.expand(beta**2*(z**2-inverse**2))
J = S.expand(beta**2*(ell**2-t**2))
verify(all(H.coeff(z,n)==0 and J.coeff(t,n)==0 for n in range(6)),
       "first_jet_and_later_coefficient")
verify(H.coeff(z,6) == J.coeff(t,6) == -S.Rational(4,5)*beta**2,
       "first_jet_and_later_coefficient")
verify(H.coeff(z,10) == -S.Rational(32,75)*beta**2,
       "first_jet_and_later_coefficient")
verify(J.coeff(t,10) == S.Rational(112,75)*beta**2,
       "first_jet_and_later_coefficient")
verify(H.coeff(z,10) != J.coeff(t,10), "first_jet_and_later_coefficient")

result = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "state": "passed",
    "checks": dict(checks),
    "total": sum(checks.values()),
    "limits": (
        "Finite exact examples verify the independently computed implicit "
        "coordinate and logarithm coefficients, denominator divisibility, and "
        "first-jet invariance. A later coefficient is explicitly different. "
        "These calculations do not prove a quantitative elliptic logarithm bound."
    ),
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result))

"""Rational checks of the sharp symmetric-grid interpolation inequalities.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
Finite checks supplement the full proof and do not certify an infinite theorem.
Complex numbers are exact pairs of Fractions; comparisons use squared moduli.
"""
from fractions import Fraction as F
import json
from laurent_constant import E

def multiply(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def norm_squared(a):
    return a[0]*a[0]+a[1]*a[1]

def polynomial(point, roots):
    value = (F(1), F(0))
    for root in roots:
        value = multiply(value, (point[0]-root, point[1]))
    return value

def central_product(m):
    k = m//2
    first = F(1)
    for j in range(k):
        first *= F(2*j+1, 2)
    return first*first if m % 2 == 0 else first*first*F(2*k+1, 2)

assert E.lo > F(8, 3)
assert E.lo**2 > 6
assert E.lo**3 > 16
for m in range(1, 201):
    dm = central_product(m)
    numerator = F(1)
    for j in range(1, m):
        numerator *= F(2*j+1, 2)
    assert numerator/dm < E.lo**m
    if m >= 3:
        factorial = 1
        for j in range(1, m+1):
            factorial *= j
        assert F(factorial)/dm < E.lo**m

directions = [
    (F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1)),
    (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
]
local_checks = outer_checks = 0
for m in range(1, 19):
    roots = [F(2*j-m+1, 2) for j in range(m)]
    samples = sorted({
        F(m, 2), -F(m, 2), F(m+1, 2), F(m+3, 2),
        roots[0]-F(1, 8), roots[-1]+F(1, 8),
        roots[m//2]+F(1, 4), roots[m//2]-F(1, 4),
    })
    for z in samples:
        if z in roots:
            continue
        z0 = max(abs(z), F(m, 2))
        radius = min(F(1), min(abs(z-x) for x in roots))/2
        numerator = norm_squared(polynomial((z, F(0)), roots))
        local_limit = (2*E.lo*z0/m)**(2*m)
        for root in roots:
            for direction in directions:
                point = (root+radius*direction[0], radius*direction[1])
                denominator = norm_squared(polynomial(point, roots))
                assert numerator <= local_limit*denominator
                local_checks += 1
        outer_radius = z0+F(1, 3)
        for direction in directions:
            point = (outer_radius*direction[0], outer_radius*direction[1])
            denominator = norm_squared(polynomial(point, roots))
            assert numerator <= (z0/outer_radius)**(2*m)*denominator
            outer_checks += 1

RESULT = {
    "status": "all exact comparisons passed",
    "central_product_indices": 200,
    "local_circle_checks": local_checks,
    "outer_circle_checks": outer_checks,
    "use": "finite supplement to the complete analytic proof",
}
if __name__ == "__main__":
    print(json.dumps(RESULT, indent=2))

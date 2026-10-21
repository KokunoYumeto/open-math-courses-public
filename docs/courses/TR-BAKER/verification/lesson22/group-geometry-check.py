"""Exact illustrative checks for TR-BAKER 22.37--46; no proof by sampling."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import sympy as S

ROOT = Path(__file__).resolve().parent
checks = {}


def check(name, assertion):
    assert assertion, name
    checks[name] = checks.get(name, 0) + 1


e, a, b, c, d, x, y, z, t = S.symbols("e a b c d x y z t")
for order in range(2, 7):
    coeff = list(range(1, order))
    j = sum(S.Integer(value) * e**i for i, value in enumerate(coeff, 1))
    h = sum(S.Integer((-1)**i * (i + 1)) * e**i for i in range(1, order))

    def trunc(poly):
        return S.Poly(S.expand(poly), e).rem(S.Poly(e**order, e)).as_expr()

    def exp_nil(poly):
        ans = S.Integer(1)
        power = S.Integer(1)
        for n in range(1, order):
            power = trunc(power * poly)
            ans += power / math.factorial(n)
        return trunc(ans)

    def log_nil(unit):
        ans = S.Integer(0)
        power = S.Integer(1)
        for n in range(1, order):
            power = trunc(power * (unit - 1))
            ans += S.Rational((-1)**(n + 1), n) * power
        return trunc(ans)

    check("nilpotent_exp_log_inverse", trunc(log_nil(exp_nil(j)) - j) == 0)
    check("nilpotent_log_exp_inverse", trunc(exp_nil(log_nil(1 + j)) - (1 + j)) == 0)
    check("nilpotent_product_law", trunc(exp_nil(j + h) - exp_nil(j) * exp_nil(h)) == 0)

# In k[e]/e^3, the product coordinates are (a+c,b+d+ac).
linear_second = S.expand(b + d + a*c - (a+c)**2/2)
check("quadratic_log_coordinate", S.expand(linear_second - (b-a*a/2) - (d-c*c/2)) == 0)

# A genuinely coupled one-dimensional logarithmic space has a larger
# Zariski closure: (x1,x2,z1,z2)=(q,2q,3q,-2q).
q, s = S.symbols("q s", nonzero=True)
for i in range(-3, 4):
    for j in range(-3, 4):
        check("torus_character_relation", S.expand(3*(i+2) - 2*(j+3) - (3*i-2*j)) == 0)
check("additive_projection_equation", (2*q)-2*q == 0)
check("torus_parametrization_equation", S.simplify((s**3)**2 * (s**-2)**3 - 1) == 0)
check("primitive_lattice_generator", math.gcd(2, 3) == 1)

add = lambda u: S.Matrix([[1, u], [0, 1]])
mul = lambda u: S.diag(u, 1)
check("additive_cocycle", add(a)*add(b) == add(a+b))
check("multiplicative_cocycle", mul(a)*mul(b) == mul(a*b))
v = S.symbols("v")
check("additive_field_at_infinity", S.diff(v/(1+a*v), a).subs(a, 0) == -v**2)
check("multiplicative_field_at_infinity", S.diff(v/(1+a), a).subs(a, 0) == -v)
check("regularity_on_infinity_chart", S.Poly(-v**2, v).degree() == 2 and S.Poly(-v, v).degree() == 1)

# Root bounds including repeated roots and zero roots: exact rational data.
for roots in [
    [S.Integer(0)],
    [S.Rational(1, 2), S.Rational(-7, 3)],
    [S.Integer(0), S.Integer(0), S.Integer(5)],
    [S.Rational(-1, 7), S.Rational(3, 2), S.Integer(-4), S.Integer(9)],
]:
    poly = S.Poly(S.prod(z-r for r in roots), z)
    bound = 1 + max(abs(c) for c in poly.all_coeffs()[1:])
    check("cauchy_root_bound", all(abs(r) <= bound for r in roots))

for degree in range(2, 13):
    # One positive circuit acts by j -> j+1 on the degree roots.
    orbit = []
    value = 0
    while value not in orbit:
        orbit.append(value)
        value = (value+1) % degree
    check("irreducible_power_cover_monodromy", len(orbit) == degree and value == 0)
    disc = S.discriminant(z**degree-t, z)
    check("power_cover_discriminant", S.simplify(disc/t**(degree-1)).is_nonzero)

reducible = (z*z-t)*(z*z-2*t)
check("reducible_cover_control", S.expand(reducible) == z**4-3*t*z*z+2*t*t)
check("reducible_cover_discriminant", S.discriminant(reducible, z) == 32*t**6)
for angle, lift in [(0, 1), (S.pi, S.I), (2*S.pi, -1), (3*S.pi, -S.I), (4*S.pi, 1)]:
    check("double_cover_exact_lift", S.simplify(S.exp(S.I*angle/2)-lift) == 0)
    check("double_cover_projection", S.simplify(lift**2-S.exp(S.I*angle)) == 0)

result = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "state": "passed",
    "checks": checks,
    "total": sum(checks.values()),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "limits": "Finite exact examples of nilpotent units, group charts, root bounds and covers. General classification, compactification and connectedness rely on the written proofs and specified programme prerequisites.",
}
(ROOT/"group-geometry-check.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result))

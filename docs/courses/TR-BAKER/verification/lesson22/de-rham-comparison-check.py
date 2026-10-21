"""Exact identities accompanying 22.84--89; not a proof of the period theorem."""
from pathlib import Path
from itertools import combinations, product
import datetime
import json
import sympy as s

x, t, u = variables = s.symbols("x t u")
checks = {}


def clean(form):
    return {w: s.expand(c) for w, c in form.items() if s.expand(c) != 0}


def add(*forms):
    answer = {}
    for form in forms:
        for wedge, coefficient in form.items():
            answer[wedge] = answer.get(wedge, 0) + coefficient
    return clean(answer)


def exterior_derivative(form):
    answer = {}
    for wedge, coefficient in form.items():
        for j, variable in enumerate(variables):
            if j in wedge:
                continue
            sign = (-1) ** sum(i < j for i in wedge)
            new_wedge = tuple(sorted((j,) + wedge))
            answer[new_wedge] = answer.get(new_wedge, 0) + sign*s.diff(coefficient, variable)
    return clean(answer)


def euler_contraction(form):
    answer = {}
    for wedge, coefficient in form.items():
        for position, j in enumerate(wedge):
            if j == 0:  # x is a base variable, not a fibre variable.
                continue
            new_wedge = wedge[:position] + wedge[position+1:]
            answer[new_wedge] = answer.get(new_wedge, 0) + (-1)**position*coefficient*variables[j]
    return clean(answer)


# Include base differentials, mixed wedges and fibre-weight-zero cases.
wedges = [w for degree in range(4) for w in combinations(range(3), degree)]
count = 0
for exponents in product(range(3), repeat=3):
    coefficient = s.prod(v**n for v, n in zip(variables, exponents))
    for wedge in wedges:
        form = {wedge: coefficient}
        weight = exponents[1] + exponents[2] + sum(j != 0 for j in wedge)
        lhs = add(exterior_derivative(euler_contraction(form)),
                  euler_contraction(exterior_derivative(form)))
        assert lhs == clean({wedge: weight*coefficient})
        assert exterior_derivative(exterior_derivative(form)) == {}
        if weight:
            assert {w: s.cancel(c/weight) for w, c in lhs.items()} == form
        count += 1
checks["Euler_homotopy_with_base_and_fibre_differentials"] = count

# The sign of the Cech transition sum in (22.210).
count = 0
for n in range(2, 7):
    vertices = list(range(n)) + [0]
    for power in range(1, 5):
        origins = [(i+1)*x**power + i*x + i*i for i in range(n)]
        arcs = sum(origins[i].subs(x, vertices[i+1])-origins[i].subs(x, vertices[i])
                   for i in range(n))
        transitions = sum((origins[(i+1) % n]-origins[i]).subs(x, vertices[i+1])
                          for i in range(n))
        assert s.expand(arcs+transitions) == 0
        count += 1
checks["Cech_boundary_integral_cancellation"] = count

# Laurent coefficients at O for y^2=4x^3-g2*x-g3 and t=-2*x/y.
g2, g3 = s.symbols("g2 g3")
xs = t**-2 + g2*t**2/4 + g3*t**4/4 - g2**2*t**6/16
relation = xs-g2/(4*xs)-g3/(4*xs**2)-t**-2
assert s.series(relation, t, 0, 7).removeO().expand() == 0
alpha = s.series(-t*s.diff(xs, t)/(2*xs), t, 0, 7).removeO().expand()
beta = s.series(-t*s.diff(xs, t)/2, t, 0, 5).removeO().expand()
assert alpha == 1-g2*t**4/2-3*g3*t**6/4
assert beta == t**-2-g2*t**2/4-g3*t**4/2
assert beta.coeff(t, -1) == 0
assert s.diff(-1/t, t) == t**-2
assert s.expand(beta-s.diff(-1/t, t)).as_leading_term(t).as_powers_dict().get(t, 0) >= 0
checks["elliptic_Laurent_and_principal_part_identities"] = 6

# Coordinate ring normal form prevents an uncancelled pole of order one.
even_orders = {2*n for n in range(1, 21)}
odd_orders = {3+2*n for n in range(21)}
assert not even_orders.intersection(odd_orders)
assert 1 not in even_orders | odd_orders
checks["elliptic_pole_order_examples"] = 2

# CM action on both differential rows and the complete relation kernel.
assert s.simplify(-1/s.I-s.I) == 0
assert s.simplify(1/s.I+s.I) == 0
M = s.Matrix([[1, s.I, 0, 0], [0, 0, 1, -s.I]])
K = s.Matrix.hstack(s.Matrix([-s.I, 1, 0, 0]), s.Matrix([0, 0, s.I, 1]))
assert M*K == s.zeros(2, 2)
assert M.rank() == K.rank() == 2
assert s.Matrix.hstack(*M.nullspace(), K).rank() == 2
assert s.diag(s.eye(2), M).rank() == 4
checks["CM_differential_action_and_complete_relation_space"] = 6

result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "state": "passed",
    "checks": checks,
    "total": sum(checks.values()),
    "scope": "Exact homotopy signs, Cech integral cancellation, elliptic principal parts and CM relations.",
    "limits": "Finite symbolic examples supplement the written proofs. They do not prove torsor descent, the universal extension, the analytic subgroup theorem or the general period dimension."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))

"""Exact contractions and the nodal-curve pairing in components 118--124."""
from collections import Counter
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import json
import sympy as s

checks = Counter()


def exterior_operators(rank):
    size = 1 << rank
    wedges, contractions = [], []
    for i in range(rank):
        wedge = s.zeros(size)
        contraction = s.zeros(size)
        for mask in range(size):
            sign = (-1) ** ((mask & ((1 << i) - 1)).bit_count())
            if mask & (1 << i):
                contraction[mask ^ (1 << i), mask] = sign
            else:
                wedge[mask | (1 << i), mask] = sign
        wedges.append(wedge)
        contractions.append(contraction)
    return wedges, contractions


for rank in range(1, 5):
    wedges, contractions = exterior_operators(rank)
    size = 1 << rank
    for pole in range(1, 5):
        # Tangential logarithmic weights commute with the first contraction.
        for tangential in product(range(2), repeat=rank - 1):
            weights = (-pole,) + tangential
            differential = sum(
                (a * w for a, w in zip(weights, wedges)), s.zeros(size)
            )
            homotopy = -contractions[0] / pole
            assert differential * homotopy + homotopy * differential == s.eye(size)
            assert differential * differential == s.zeros(size)
            checks["pole_order_contraction_and_square_zero"] += 1
    for weights in product(range(3), repeat=rank):
        if not any(weights):
            continue
        i = next(i for i, n in enumerate(weights) if n)
        differential = sum(
            (a * w for a, w in zip(weights, wedges)), s.zeros(size)
        )
        homotopy = contractions[i] / weights[i]
        assert differential * homotopy + homotopy * differential == s.eye(size)
        checks["nonconstant_logarithmic_weight_contraction"] += 1


def cech_differential(cardinality, degree):
    """Functions on S^(degree+1), including degree -1 = functions on a point."""
    source = list(product(range(cardinality), repeat=degree + 1))
    target = list(product(range(cardinality), repeat=degree + 2))
    index = {value: i for i, value in enumerate(source)}
    result = s.zeros(len(target), len(source))
    for row, value in enumerate(target):
        for i in range(len(value)):
            result[row, index[value[:i] + value[i + 1:]]] += (-1) ** i
    return result


def cech_homotopy(cardinality, degree):
    source = list(product(range(cardinality), repeat=degree + 1))
    target = list(product(range(cardinality), repeat=degree))
    index = {value: i for i, value in enumerate(source)}
    result = s.zeros(len(target), len(source))
    for row, value in enumerate(target):
        result[row, index[(0,) + value]] = 1
    return result


for cardinality in (1, 2, 3):
    for degree in range(4):
        delta = cech_differential(cardinality, degree)
        previous = cech_differential(cardinality, degree - 1)
        h = cech_homotopy(cardinality, degree)
        following_h = cech_homotopy(cardinality, degree + 1)
        assert previous * h + following_h * delta == s.eye(cardinality ** (degree + 1))
        assert delta * previous == s.zeros(delta.rows, previous.cols)
        checks["augmented_cech_insertion_identity"] += 1

# A concrete cochain map with nonzero differentials checks the cone signs.
d_a = s.Matrix([[0, 0], [1, 0]])
d_b = s.Matrix([[0, 0], [2, 0]])
f = s.diag(1, 2)
assert d_b * f == f * d_a
cone_d = s.BlockMatrix([[d_a, s.zeros(2)], [f, -d_b]]).as_explicit()
assert cone_d * cone_d == s.zeros(4)
checks["relative_cone_differential_signs"] += 1

u = s.symbols("u")
x, y = u**2 - 1, u * (u**2 - 1)
assert s.expand(y**2 - x**2 * (x + 1)) == 0
assert s.cancel(y / x) == u
assert s.expand(u**2 - (x + 1)) == 0
assert (x.subs(u, 2), y.subs(u, 2)) == (3, 6)
assert s.solve(x, u) == [-1, 1]
assert all(y.subs(u, a) == 0 for a in (-1, 1))
checks["normalization_and_node_fibres"] += 6

q = (u + 1) / 2
assert (q.subs(u, -1), q.subs(u, 1)) == (0, 1)
assert s.simplify(s.diff(s.log(2 - u), u) - 1 / (u - 2)) == 0
assert s.integrate(1 / (u - 2), (u, -1, 1)) == -s.log(3)
assert s.integrate(s.diff(q, u), (u, -1, 1)) == 1
assert s.Rational(1 - 2, -1 - 2) == s.Rational(1, 3)
assert s.residue(1 / (u - 2), u, 2) == 1
period = s.Matrix([[2 * s.pi * s.I, -s.log(3)], [0, 1]])
assert period.det() == 2 * s.pi * s.I
checks["relative_pairing_and_period_matrix"] += 7

# A trace matrix with an integral basis gives the denominator enclosure.
t = s.symbols("t")
trace_matrix = s.diag(2, 2 * t)  # basis 1, sqrt(t) of k(t)(sqrt(t))
v0, v1 = s.symbols("v0 v1")
coordinates = trace_matrix.inv() * s.Matrix([v0, v1])
assert trace_matrix.det() == 4 * t
assert all(s.denom(s.cancel(4 * t * c)) == 1 for c in coordinates)
checks["trace_denominator_example"] += 2

result = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "state": "passed",
    "checks": dict(checks),
    "total": sum(checks.values()),
    "limits": (
        "Exact finite examples test contraction signs, relative cone signs, "
        "normalization formulas and the worked period matrix. They do not "
        "constitute computational proofs of hypercover descent, resolution "
        "or the general de Rham comparison."
    ),
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result))

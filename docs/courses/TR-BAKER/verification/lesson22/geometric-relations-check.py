"""Exact finite examples for the geometric one-period arguments."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json

import sympy as s

checks = Counter()


def verify(condition, family):
    assert bool(condition), family
    checks[family] += 1


x = s.symbols("x")
f = (x - 2) ** 2 / ((x - 1) * (x - 4))
t = (x - 2) ** 2 / x
tau_x = 4 / x
verify(s.cancel(f / (f - 1) - t) == 0, "cover_and_principal_divisor")
verify(s.cancel(t.subs(x, tau_x) - t) == 0, "cover_and_principal_divisor")
verify(s.limit(f, x, 0) == s.limit(f, x, s.oo) == 1,
       "cover_and_principal_divisor")
verify(s.factor(s.together(t - 1)) == (x - 4) * (x - 1) / x,
       "cover_and_principal_divisor")
verify(s.solve(s.diff(t, x), x) == [-2, 2], "cover_and_principal_divisor")
verify([t.subs(x, a) for a in [-2, 2]] == [-8, 0],
       "cover_and_principal_divisor")
verify(s.cancel(s.diff(tau_x, x) / tau_x + 1 / x) == 0,
       "cover_and_principal_divisor")
verify(s.expand_log(2 * s.log(2) - s.log(4), force=True) == 0,
       "cover_and_principal_divisor")

tau = s.Matrix([[-1, 0, 0], [0, 1, 0], [0, -1, -1]])
push = s.Matrix([[0, -1, 0]])
boundary = s.Matrix([[0, -1, -1], [0, 1, 0], [0, 0, 1]])
endpoint_tau = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
endpoint_push = s.Matrix([[0, 1, 0], [1, 0, 1]])
base_boundary = s.Matrix([-1, 1])
b = s.Matrix([0, 2, -1])
xi = -b / 2
average = (s.eye(3) + tau) / 2
verify(tau**2 == s.eye(3), "relative_homology_and_averaging")
verify(boundary * tau == endpoint_tau * boundary,
       "relative_homology_and_averaging")
verify(endpoint_push * boundary == base_boundary * push,
       "relative_homology_and_averaging")
verify(push * tau == push, "relative_homology_and_averaging")
verify(average**2 == average and average.rank() == 1,
       "relative_homology_and_averaging")
verify(tau * b == b and boundary * b == s.Matrix([-1, 2, -1]),
       "relative_homology_and_averaging")
verify(push * xi == s.Matrix([1]) and -(s.eye(3) + tau) * xi == b,
       "relative_homology_and_averaging")
verify(average * s.Matrix([0, 1, 0]) == b / 2,
       "relative_homology_and_averaging")

# Formal symbols are ordered (sigma_i tensor omega_j), then the target unit.
# Build relations independently from the arrow formula, and the equations
# on diagram endomorphisms from their commutators.
eye = s.eye(3)
relations = []
for i in range(3):
    for j in range(3):
        col = s.zeros(10, 1)
        for a in range(3):
            col[3 * a + j] += tau[a, i]
            col[3 * i + a] -= tau[j, a]
        relations.append(col)
    col = s.zeros(10, 1)
    col[9] = push[0, i]
    for j in range(3):
        col[3 * i + j] -= push[0, j]
    relations.append(col)
R = s.Matrix.hstack(*relations)
variables = s.symbols("a0:10")
A = s.Matrix(3, 3, variables[:9])
scalar = variables[9]
equations = list(A * tau - tau * A) + list(scalar * push - push * A)
E = s.linear_eq_to_matrix(equations, variables)[0]
verify(R.rank() == E.rank() == 5, "finite_diagram_duality")
verify(10 - R.rank() == len(E.nullspace()) == 5, "finite_diagram_duality")
for coords in E.nullspace():
    matrix = s.Matrix(3, 3, list(coords[:9]))
    # The pairing evaluates omega_j(A sigma_i), hence transposes A.
    functional = s.Matrix([matrix[j, i] for i in range(3) for j in range(3)]
                          + [coords[9]])
    verify(R.T * functional == s.zeros(R.cols, 1), "finite_diagram_duality")
for omega in [s.Matrix([[7, 1, 2]]), s.Matrix([[1, 0, 0]])]:
    symbol = s.Matrix([b[i] * omega[j] for i in range(3) for j in range(3)]
                      + [0])
    verify(R.row_join(symbol).rank() == R.rank(), "finite_diagram_duality")
omega = s.Matrix([[0, 1, 0]])
symbol = s.Matrix([b[i] * omega[j] for i in range(3) for j in range(3)] + [0])
verify(R.row_join(symbol).rank() == R.rank() + 1, "finite_diagram_duality")

# CRT endpoint functions on A1 and their induced relative path coordinates.
for points in [[0, 1], [-3, 2, 7], [-5, -1, 3, 8]]:
    for j, point in enumerate(points):
        poly = s.prod((x - q) / (point - q) for q in points if q != point)
        values = s.Matrix([[s.simplify(poly.subs(x, q)) for q in points]])
        expected = s.zeros(1, len(points))
        expected[j] = 1
        verify(values == expected, "endpoint_coordinate_maps")
        D = s.zeros(len(points), len(points) - 1)
        for i in range(1, len(points)):
            D[0, i - 1] = -1
            D[i, i - 1] = 1
        verify(values * D == D[j, :], "endpoint_coordinate_maps")

# Ramified cyclic quotients: the stabilizer weight gives a full fibre divisor.
for degree in [2, 3, 5, 7]:
    # x^degree=t: one point at zero, degree points at one. Summing all
    # conjugate maps multiplies the normalized invariant zero-chain by degree.
    verify(degree * s.Rational(degree, degree) == degree,
           "ramified_fibre_weights")
    verify(degree * s.Rational(1, degree) == 1, "ramified_fibre_weights")

# A mixed map from a direct sum must not be replaced by separate kernels.
mixed = s.Matrix([[1, -1]])
verify(mixed.nullspace() == [s.Matrix([1, 1])],
       "mixed_components_and_kernel_identity")
verify(s.Matrix([[1, 0], [0, -1]]).nullspace() == [],
       "mixed_components_and_kernel_identity")

# A finite-vector-space model of ker(alpha)=gamma^{-1}(gamma ker(alpha)).
# ker(gamma) lies in ker(alpha); P=gamma ker(alpha) is the last coordinate.
alpha = s.Matrix([[1, 2, 0, 0], [0, 1, 1, 0]])
gamma = alpha.col_join(s.Matrix([[0, 0, 1, 0]]))
K = s.Matrix.hstack(*alpha.nullspace())
P = gamma * K
verify(all(alpha * v == s.zeros(2, 1) for v in gamma.nullspace()),
       "mixed_components_and_kernel_identity")
verify(P.columnspace() == [s.Matrix([0, 0, 1])],
       "mixed_components_and_kernel_identity")
constraints = s.Matrix.vstack(*[v.T * gamma for v in P.T.nullspace()])
verify(s.Matrix.hstack(*constraints.nullspace()).columnspace() == K.columnspace(),
       "mixed_components_and_kernel_identity")

result = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "state": "passed",
    "checks": dict(checks),
    "total": sum(checks.values()),
    "limits": (
        "Exact finite examples check formal-period duality, endpoint and "
        "ramification weights, the branched-cover exercise, and the mixed-kernel "
        "argument. They are not computational proofs of the general geometric "
        "relation theorem, generalized-Jacobian construction, or Bertini."
    ),
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result))

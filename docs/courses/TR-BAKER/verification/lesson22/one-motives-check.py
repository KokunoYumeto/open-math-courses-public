"""Exact torus, lattice and relative-period examples for 22.90--100."""
from pathlib import Path
from itertools import product
import datetime
import json
import sympy as s

checks = {}
x, y, z, a, b, c = s.symbols("x y z a b c", nonzero=True)

# Complete Laurent-polynomial 2-cocycle space in a bounded exponent box.
exponents = list(product(range(-1, 2), repeat=2))
coefficients = s.symbols("c0:9")
cochain = sum(v*x**i*y**j for v, (i, j) in zip(coefficients, exponents))
identity = (cochain
            + cochain.subs({x: x*y, y: z}, simultaneous=True)
            - cochain.subs({x: y, y: z}, simultaneous=True)
            - cochain.subs({x: x, y: y*z}, simultaneous=True))
equations = s.Poly(s.expand(x*y*z*identity), x, y, z).coeffs()
equations += s.Poly(s.expand(x*cochain.subs(y, 1)), x).coeffs()
equations += s.Poly(s.expand(y*cochain.subs(x, 1)), y).coeffs()
A, rhs = s.linear_eq_to_matrix(equations, coefficients)
assert rhs == s.zeros(len(equations), 1)
basis = A.nullspace()
assert len(basis) == 2
coboundaries = []
for n in [-1, 1]:
    F = x**n-1
    delta = s.expand(F+F.subs(x, y)-F.subs(x, x*y))
    coboundaries.append(s.Matrix([delta.coeff(x, i).coeff(y, j) for i, j in exponents]))
B = s.Matrix.hstack(*coboundaries)
assert A*B == s.zeros(A.rows, 2)
assert s.Matrix.hstack(*basis, B).rank() == 2
checks["complete_bounded_Laurent_cocycle_space"] = 4

# Two-dimensional torus: coefficient projection recovers the splitting.
x1, x2, y1, y2, z1, z2 = s.symbols("x1 x2 y1 y2 z1 z2", nonzero=True)
count = 0
for i, j in product(range(-2, 3), repeat=2):
    if i == j == 0:
        continue
    F = x1**i*x2**j-1
    Fy = F.subs({x1: y1, x2: y2}, simultaneous=True)
    Fxy = F.subs({x1: x1*y1, x2: x2*y2}, simultaneous=True)
    C = s.expand(F+Fy-Fxy)
    recovered = C.coeff(y1, 0).coeff(y2, 0)
    assert s.expand(recovered-F) == 0
    assert s.expand(C+Fxy-F-Fy) == 0
    count += 1
checks["two_torus_constant_coefficient_splittings"] = count

# Off-diagonal lift changes must be compatible with exactness.
I = s.Matrix([[1, a], [0, b], [0, 1], [0, 0]])
P = s.Matrix([[0, 1, -b, c], [0, 0, 0, 1]])
assert P*I == s.zeros(2, 2)
assert I.extract([0, 2], [0, 1]).det() == 1
assert P.extract([0, 1], [1, 3]).det() == 1
assert I.cols+P.rows == I.rows
checks["block_triangular_exactness"] = 4
D = s.Matrix(2, 2, s.symbols("d0:4"))
shear = s.BlockMatrix([[s.eye(2), D], [s.zeros(2), s.eye(2)]]).as_explicit()
inverse = s.BlockMatrix([[s.eye(2), -D], [s.zeros(2), s.eye(2)]]).as_explicit()
assert shear*inverse == s.eye(4)
assert shear.det() == 1
checks["change_of_lattice_lifts"] = 2

# Connected H can meet the lifted lattice in a nonsaturated subgroup.
count = 0
for n in range(-12, 13):
    assert (s.Integer(-1)**n == 1) == (n % 2 == 0)
    assert s.Integer(-1)**(2*n) == 1
    count += 1
checks["root_of_unity_endpoint_and_finite_index_lattice"] = count

# Row-major entries of (22.250) in the independent basis (1,tau,log2,log3).
R = s.Matrix([[0,0,0,0,1,0,0,0,1],
              [1,0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0]])
relations = []
for index in [3, 5, 6, 7]:
    v = s.zeros(9, 1)
    v[index] = 1
    relations.append(v)
v = s.zeros(9, 1)
v[4], v[8] = 1, -1
relations.append(v)
K = s.Matrix.hstack(*relations)
assert R.rank() == 4
assert K.rank() == 5
assert R*K == s.zeros(4, 5)
assert s.Matrix.hstack(*R.nullspace(), K).rank() == 5
checks["complete_two_endpoint_matrix_relation_space"] = 4

result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "state": "passed",
    "checks": checks,
    "total": sum(checks.values()),
    "scope": "Exact Laurent cocycles, compatible lift changes, lattice torsion and the nine-entry period matrix.",
    "limits": "These examples do not prove the geometric realization, subgroup comparison or period-relation theorem. Those arguments are supplied in the component manuscripts."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))

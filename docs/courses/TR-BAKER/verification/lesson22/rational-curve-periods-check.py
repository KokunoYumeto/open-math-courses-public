"""Exact finite de Rham quotients and the rational integral in 22.101--105."""
from pathlib import Path
import datetime
import json
import sympy as s

x = s.symbols("x", real=True)
checks = {}


def interpolation(points, index):
    target = points[index]
    return s.prod((x-p)/(target-p) for j, p in enumerate(points) if j != index)


# Compute the quotient itself in a finite subcomplex, including constants.
# Differentiation of poles of order <=2 gives poles of order <=3.
functions = [s.Integer(1), x, x**2, x**3, 1/x, 1/x**2, 1/(x+1), 1/(x+1)**2]
forms = [s.Integer(1), x, x**2] + [1/(x-a)**j for a in [0, -1] for j in range(1, 4)]
denominator = x**3*(x+1)**3
polynomial_columns = [
    s.Matrix([s.Poly(s.cancel(v*denominator), x).nth(j) for j in range(9)])
    for v in forms
]
conversion = s.Matrix.hstack(*polynomial_columns)
assert conversion.det() != 0


def form_coordinates(v):
    poly = s.Poly(s.cancel(v*denominator), x)
    assert poly.degree() <= 8
    return conversion.inv()*s.Matrix([poly.nth(j) for j in range(9)])


count = 0
for size in range(4):
    points = list(map(s.Integer, range(1, size+1)))
    columns = [
        form_coordinates(s.diff(f, x)).col_join(s.Matrix(size, 1, [f.subs(x, p) for p in points]))
        for f in functions
    ]
    differential = s.Matrix.hstack(*columns)
    expected_rank = 7 if not points else 8
    assert differential.rank() == expected_rank
    basis_forms = [1/x, 1/(x+1)]
    basis_forms += [s.diff(interpolation(points, j), x) for j in range(1, size)]
    classes = s.Matrix.hstack(*[
        form_coordinates(v).col_join(s.zeros(size, 1)) for v in basis_forms
    ])
    assert classes.cols == 2+max(size-1, 0)
    assert s.Matrix.hstack(differential, classes).rank() == 9+size
    # The computed quotient has exactly the claimed independent classes.
    assert 9+size-differential.rank() == classes.cols
    count += 4
checks["finite_relative_deRham_quotients_including_empty_endpoint_set"] = count

# All empty and nonempty blocks of the comparison matrix.
tau = s.symbols("tau", nonzero=True)
count = 0
for punctures in range(5):
    for endpoints in range(5):
        logs = s.Matrix(punctures, endpoints, lambda i, j: s.Symbol(f"l{i}_{j}"))
        matrix = s.BlockMatrix([
            [tau*s.eye(punctures), logs],
            [s.zeros(endpoints, punctures), s.eye(endpoints)]
        ]).as_explicit()
        assert matrix.det() == tau**punctures
        count += 1
checks["comparison_determinants_with_empty_blocks"] = count

# Check the actual algebraic map for the two-endpoint figure.
q1, q2 = (x-1)*(3-x), (x-1)*(x-2)/2
assert [[q.subs(x, p) for p in [1, 2, 3]] for q in [q1, q2]] == [[0, 1, 0], [0, 0, 1]]
assert [s.integrate(s.diff(q, x), (x, 1, p)) for p in [2, 3] for q in [q1, q2]] == [1, 0, 0, 1]
checks["two_endpoint_algebraic_map"] = 2

# The relative sign: an exact pair pairs to zero even with internal vertices.
F = (x**3+2)/(x+1)
vertices = list(map(s.Integer, [1, 2, 4, 7]))
edges = [(0, 1, 3), (1, 2, 3), (2, 3, 3), (1, 3, -2), (3, 1, -2)]
boundary = [0]*len(vertices)
integral = 0
for start, end, multiplicity in edges:
    boundary[start] -= multiplicity
    boundary[end] += multiplicity
    integral += multiplicity*(F.subs(x, vertices[end])-F.subs(x, vertices[start]))
assert boundary == [-3, 0, 0, 3]
assert integral == sum(n*F.subs(x, p) for n, p in zip(boundary, vertices))
checks["relative_boundary_sign_and_internal_endpoint_cancellation"] = 2

R = 1/(1+x**3)
parts = 1/(3*(x+1))+(2-x)/(3*(x**2-x+1))
primitive = s.log(x+1)/3-s.log(x**2-x+1)/6+s.atan((2*x-1)/s.sqrt(3))/s.sqrt(3)
assert s.cancel(R-parts) == 0
assert s.simplify(s.diff(primitive, x)-R) == 0
assert s.simplify(primitive.subs(x, 1)-primitive.subs(x, 0)-s.log(2)/3-s.pi/(3*s.sqrt(3))) == 0
roots = [-1, (1+s.sqrt(3)*s.I)/2, (1-s.sqrt(3)*s.I)/2]
assert s.cancel(sum(1/(3*a**2*(x-a)) for a in roots)-R) == 0
checks["rational_integral_partial_fractions_primitive_and_endpoints"] = 4

result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "state": "passed",
    "checks": checks,
    "total": sum(checks.values()),
    "scope": "Finite de Rham quotient ranks, comparison blocks, endpoint maps, boundary signs and the exact third-kind integral.",
    "limits": "These calculations do not prove the general topological comparison or transcendence. Those are written arguments using the proved 1-motive and logarithm theorems."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))

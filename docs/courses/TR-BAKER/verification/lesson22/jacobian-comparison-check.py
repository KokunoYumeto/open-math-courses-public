"""Exact local identities and linear algebra for 22.106--112."""
from pathlib import Path
from itertools import combinations, permutations, product
from math import factorial
import datetime
import json
import sympy as s

checks = {}

# The invariant part of degree-one product cohomology is the diagonal copy.
count = 0
for n in range(1, 5):
    for g in range(4):
        dimension = 2*g
        average = s.zeros(n*dimension)
        for permutation in permutations(range(n)):
            P = s.zeros(n*dimension)
            for i, target in enumerate(permutation):
                for j in range(dimension):
                    P[target*dimension+j, i*dimension+j] = 1
            average += P
        average /= factorial(n)
        diagonal = s.Matrix(n*dimension, dimension, lambda i, j: int(i % dimension == j))
        first_factor = s.Matrix(dimension, n*dimension, lambda i, j: int(i == j))
        assert average*average == average
        assert average.rank() == dimension
        assert average*diagonal == diagonal
        assert first_factor*diagonal == s.eye(dimension)
        count += 1
checks["symmetric_power_H1_averaging_and_unscaled_basepoint_pullback"] = count

# Exterior-algebra Cartan homotopy, including a weight-zero base differential.
count = 0
for fibre_dimension in [1, 2]:
    all_indices = range(fibre_dimension+1)  # index0 is the base differential
    basis = [p for size in range(fibre_dimension+2) for p in combinations(all_indices, size)]
    positions = {p: i for i, p in enumerate(basis)}
    for weight in product(range(-2, 3), repeat=fibre_dimension):
        if not any(weight):
            continue
        derivative = s.zeros(len(basis))
        contraction = s.zeros(len(basis))
        j = next(i for i, m in enumerate(weight) if m)
        direction = j+1
        for col, indices in enumerate(basis):
            for i, coefficient in enumerate(weight):
                index = i+1
                if index not in indices:
                    target = tuple(sorted(indices+(index,)))
                    sign = (-1)**sum(k < index for k in indices)
                    derivative[positions[target], col] += sign*coefficient
            if direction in indices:
                offset = indices.index(direction)
                target = indices[:offset]+indices[offset+1:]
                contraction[positions[target], col] = s.Rational((-1)**offset, weight[j])
        assert derivative*derivative == s.zeros(len(basis))
        assert derivative*contraction+contraction*derivative == s.eye(len(basis))
        count += 1
checks["logarithmic_weight_homotopy_including_negative_weights_and_base_forms"] = count

# Winding coordinates with the first puncture used as reference.
count = 0
for punctures in range(1, 8):
    W = s.Matrix(punctures-1, punctures, lambda i, j: -1 if j == 0 else int(j == i+1))
    assert W*s.ones(punctures, 1) == s.zeros(punctures-1, 1)
    assert W.rank() == punctures-1
    assert W[:, 1:] == s.eye(punctures-1)
    assert s.Matrix.hstack(*W.nullspace(), s.ones(punctures, 1)).rank() == 1
    count += 1
checks["puncture_lattice_quotient_and_reference_frame_signs"] = count

x, y, a, b, g2, g3, t = s.symbols("x y a b g2 g3 t", nonzero=True)
curve = 4*x**3-g2*x-g3
at_Q = 4*a**3-g2*a-g3
rho = (y+b)/(2*(x-a)*y)
regular_at_minus_Q = (4*(x**2+a*x+a**2)-g2)/(2*y*(y-b))
numerator = s.together(rho-regular_at_minus_Q).as_numer_denom()[0]
remainder = s.rem(s.Poly(numerator, y), s.Poly(y**2-curve, y)).as_expr()
remainder = s.rem(s.Poly(remainder, b), s.Poly(b**2-at_Q, b)).as_expr()
assert s.expand(remainder) == 0
c1, c2 = s.symbols("c1 c2")
assert s.limit(t*rho.subs({x:a+t, y:b+c1*t+c2*t**2}, simultaneous=True), t, 0) == 1
assert s.limit(t*rho.subs({x:a+t, y:-b+c1*t+c2*t**2}, simultaneous=True), t, 0) == 0
X = t**-2+c1*t**2+c2*t**4
Y = -2*t**-3+g2*t+g3*t**3
infinity_form = rho.subs({x:X, y:Y}, simultaneous=True)*s.diff(X, t)
assert s.limit(t*infinity_form, t, 0) == -1
checks["elliptic_third_kind_identity_and_three_local_pole_checks"] = 4

om1, om2, eta1, eta2, r1, r2, u, v, w, tau = s.symbols("om1 om2 eta1 eta2 r1 r2 u v w tau")
P = s.Matrix([[om1,om2,0,u],[-eta1,-eta2,0,v],[r1,r2,tau,w],[0,0,0,1]])
assert s.expand(P.det()-tau*(om2*eta1-om1*eta2)) == 0
x0, x1 = s.symbols("x0 x1")
F = (x-x0)/(x1-x0)
assert s.simplify(F.subs(x,x0)) == 0
assert s.simplify(F.subs(x,x1)) == 1
assert s.simplify(s.integrate(s.diff(F,x), (x,x0,x1))) == 1
checks["elliptic_relative_period_determinant_and_endpoint_normalization"] = 4

result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "state": "passed",
    "checks": checks,
    "total": sum(checks.values()),
    "scope": "Exact local logarithmic complexes, cohomology invariants, puncture winding signs, elliptic residues and the relative matrix.",
    "limits": "These finite identities supplement the written geometric proofs; they do not establish Picard representability, GAGA, the general comparison or transcendence by computation."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

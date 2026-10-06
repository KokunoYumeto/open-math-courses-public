"""Exact check of the tangent direction and the polynomial column basis.

The proof is in the lesson. This small confluent-Vandermonde instance checks
two normalizations which would change the actual auxiliary matrix.
"""
from __future__ import annotations

import hashlib
import json
from math import factorial, prod
from pathlib import Path

import sympy as sp


def check() -> dict:
    x, u = sp.symbols("x u")
    rows = [(a, t) for a in range(6) for t in [-1, 0, 1]]
    orders = list(range(18))
    ordinary = sp.Matrix([
        [
            0 if sigma < a
            else sp.binomial(sigma, a) * factorial(a) * sp.Integer(t) ** (sigma-a)
            for sigma in orders
        ]
        for a, t in rows
    ])
    # At (X,Y)=(0,1), D=partial_X+Y partial_Y agrees with
    # differentiation of X^a exp(t X). Keeping only partial_X loses t.
    wrong_direction = sp.Matrix([
        [factorial(a) if sigma == a else 0 for sigma in orders]
        for a, t in rows
    ])
    ordinary_det = ordinary.det(method="domain-ge")
    expected_absolute = sp.Integer(2) ** 36 * prod(factorial(a) for a in range(6)) ** 3
    assert abs(ordinary_det) == expected_absolute
    assert ordinary.rank() == 18
    assert wrong_direction.rank() == 6
    blocks = [
        sp.Poly((u*(u+1)/2) ** (sigma//2) * u ** (sigma % 2), u)
        for sigma in orders
    ]
    transition = sp.Matrix([
        [blocks[sigma].nth(a) for sigma in orders]
        for a in orders
    ])
    block_det = (ordinary * transition).det(method="domain-ge")
    transition_det = sp.prod(
        sp.Rational(1, 2) ** (sigma//2) for sigma in orders
    )
    assert transition.det() == transition_det
    assert block_det == ordinary_det * transition_det
    assert block_det != 0
    chosen_log = sp.Symbol("lambda")
    s = sp.Symbol("s")
    linear_form = 1 - chosen_log
    assert sp.expand(s*chosen_log + s*linear_form - s) == 0
    def indices(d: int, cap: int):
        if d == 0:
            yield ()
            return
        for a in range(cap+1):
            for rest in indices(d-1, cap-a):
                yield (a,)+rest
    counts = []
    for d in range(1, 7):
        for cap in range(1, 10):
            all_indices = list(indices(d, cap))
            number = int(sp.binomial(cap+d, d))
            first_sum = sum(tau[0] for tau in all_indices)
            total_sum = sum(sum(tau) for tau in all_indices)
            assert len(all_indices) == number
            assert first_sum * (d+1) == cap * number
            assert total_sum * (d+1) == d * cap * number
            counts.append({"d":d, "T0":cap, "rows_per_t":number,
                           "first_degree_sum":first_sum,
                           "total_degree_sum":total_sum})
    # The analytic value has exp(t*s*Lambda) times the algebraic value.
    return {
        "status": "all checks passed",
        "example": "m=d=1, T0=5, T1=1, beta0=1, alpha1=2",
        "rows": 18,
        "derivative_orders": [0, 17],
        "ordinary_rank": 18,
        "ordinary_determinant": str(ordinary_det),
        "expected_absolute_determinant": str(expected_absolute),
        "rank_if_multiplicative_tangent_component_is_dropped": 6,
        "block_basis_H": 2,
        "transition_determinant": str(transition_det),
        "block_basis_determinant": str(block_det),
        "plane_identity": "s*lambda+s*(1-lambda)=s",
        "exponential_factor": "analytic/algebraic=exp(t*s*Lambda)",
        "row_degree_sum_checks": counts,
        "limits": "Finite normalization check, not a replacement for the full rank or constant proof.",
    }


if __name__ == "__main__":
    result = check()
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, indent=2))

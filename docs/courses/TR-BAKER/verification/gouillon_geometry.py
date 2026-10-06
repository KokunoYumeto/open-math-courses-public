"""Exact finite examples for the zero estimate; not a proof by sampling.

Independent course certificate by GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0.
Uses only the Python standard library. No external source text is included.
"""
from fractions import Fraction
from math import comb
import json


def rational_rank(columns):
    basis = {}
    for column in columns:
        value = {i: Fraction(v) for i, v in enumerate(column) if v}
        while value:
            pivot = min(value)
            if pivot not in basis:
                scale = value[pivot]
                basis[pivot] = {i: v / scale for i, v in value.items()}
                break
            scale = value[pivot]
            for i, v in basis[pivot].items():
                value[i] = value.get(i, 0) - scale * v
                if not value[i]:
                    del value[i]
    return len(basis)


def graph_dimension(n, multiplicity, u, v):
    """Use the independent weight blocks in C[Q,Y]/Q**multiplicity."""
    total = 0
    for weight in range(n * u + v + 1):
        allowed = [a for a in range(u + 1) if 0 <= weight - n * a <= v]
        total += min(multiplicity, len(allowed))
    return total


def graph_block_rank(n, multiplicity, u, v):
    """Actually expand X0**a Y**c=(Q+Y**n)**a Y**c and rank each block."""
    total = 0
    for weight in range(n * u + v + 1):
        columns = [
            [comb(a, i) if i <= a else 0 for i in range(multiplicity)]
            for a in range(u + 1) if 0 <= weight - n * a <= v
        ]
        total += rational_rank(columns)
    return total


def interpolation_columns(K, L, R, S, T, b1, b2, alpha1, alpha2):
    rows = [(k0, k1, ell) for ell in range(L + 1)
            for k0 in range(K + 1) for k1 in range(K - k0 + 1)]
    columns = []
    for r in range(R + 1):
        for s in range(S + 1):
            x = r * b2 + s * b1
            y = alpha1 ** r * alpha2 ** s
            for t in range(T + 1):
                columns.append([
                    x ** k1 * comb(t, k0) * ell ** (t - k0) * y ** ell
                    if t >= k0 else 0 for k0, k1, ell in rows
                ])
    return rows, columns


def main():
    hilbert_checks = 0
    for n in range(1, 7):
        for multiplicity in range(1, 6):
            for u in range(multiplicity - 1, multiplicity + 7):
                for v in range(n * multiplicity - 1, n * multiplicity + 6):
                    actual = graph_dimension(n, multiplicity, u, v)
                    target = multiplicity * (n * u + v + 1) - n * multiplicity * (multiplicity - 1)
                    assert actual == target, (n, multiplicity, u, v, actual, target)
                    hilbert_checks += 1
    block_checks = 0
    for n in range(2, 5):
        for multiplicity in range(1, 4):
            for u in range(0, 7):
                for v in range(0, 9):
                    assert graph_block_rank(n, multiplicity, u, v) == graph_dimension(n, multiplicity, u, v)
                    block_checks += 1
    crossing_checks = 0
    for multiplicity in range(1, 7):
        for u in range(2 * multiplicity, 2 * multiplicity + 8):
            for v in range(multiplicity - 1, multiplicity + 6):
                additive = sum(1 for a in range(u + 1) for b in range(u + 1 - a)
                               if a < multiplicity or b < multiplicity)
                assert additive == 2 * multiplicity * u + 3 * multiplicity - 2 * multiplicity ** 2
                hilbert = additive * min(v + 1, multiplicity)
                assert hilbert == multiplicity * (2 * multiplicity * u + 3 * multiplicity - 2 * multiplicity ** 2)
                assert 2 * multiplicity ** 2 >= 2 * multiplicity
                crossing_checks += 1
    # A full-rank example with multiplicatively dependent bases (2,4).
    K = L = 2
    Rj = Sj = [1, 1, 1]
    Tj = [2, 2, 6]
    b1, b2, alpha1, alpha2 = 2, 3, 2, 4
    pairs = [{(r * b2 + s * b1, alpha1 ** r * alpha2 ** s)
              for r in range(Rj[j] + 1) for s in range(Sj[j] + 1)} for j in range(3)]
    X = [len({x for x, y in p}) for p in pairs]
    Y = [len({y for x, y in p}) for p in pairs]
    assert Tj[0] >= K and X[0] >= K + 1
    assert (Tj[0] + 1) * Y[0] >= L + 1
    assert (Tj[1] + 1) * Y[1] >= 2 * K * L + 1
    assert (Tj[1] + 1) * X[1] >= K * K + 1
    assert (Tj[2] + 1) * len(pairs[2]) >= 3 * K * K * L + 1
    rows, columns = interpolation_columns(K, L, sum(Rj), sum(Sj), sum(Tj), b1, b2, alpha1, alpha2)
    rank = rational_rank(columns)
    assert rank == len(rows) == 18
    # Exact finite-torsion orbit counts; H-cosets merge the two signs.
    points = [(k * k, sign * k) for k in range(1, 8) for sign in [-1, 1]]
    torsion_cosets = len({(x, abs(y)) for x, y in points})
    identity_cosets = len(set(points))
    assert identity_cosets == 2 * torsion_cosets == 14
    # The original tail need not be nested before normalization.
    sets = [{2, 4}, {7, 9}, {13, 15}]
    chosen = [min(s) for s in sets]
    normalized = [{x - a for x in s} for s, a in zip(sets, chosen)]
    original_sum = {x + y + z for x in sets[0] for y in sets[1] for z in sets[2]}
    normalized_sum = {x + y + z for x in normalized[0] for y in normalized[1] for z in normalized[2]}
    assert {s - sum(chosen) for s in original_sum} == normalized_sum
    assert all(0 in s for s in normalized)
    print(json.dumps({
        'graph_fat_hilbert_checks': hilbert_checks,
        'independent_rational_weight_block_checks': block_checks,
        'crossing_component_checks': crossing_checks,
        'dependent_base_cardinalities': {'X': X, 'Y': Y, 'pairs': [len(p) for p in pairs]},
        'dependent_base_rank': rank,
        'matrix_shape': [len(rows), len(columns)],
        'finite_torsion_orbit_counts': [identity_cosets, torsion_cosets],
        'translated_set_normalization': 'passed',
        'limits': 'Exact finite teaching examples supplement the written general proofs; not a sampled proof of the zero theorem or of the final numerical logarithm bounds.'
    }))


if __name__ == '__main__':
    main()

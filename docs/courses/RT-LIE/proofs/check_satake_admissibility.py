"""Exact finite checks for Definition 8.4, independent of Lie-algebra matrices.

The convention is A[i][j] = alpha_i(h_j), with indices zero-based internally.
Only Python's standard library is used. This enumeration checks the universal
proof; it does not replace its reconstruction or injectivity arguments.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def cartan(rank, edges):
    matrix = [[2 * (i == j) for j in range(rank)] for i in range(rank)]
    for i, j, a_ij, a_ji in edges:
        matrix[i][j], matrix[j][i] = a_ij, a_ji
    return matrix


def finite_matrix(kind, rank):
    edges = [(i, i + 1, -1, -1) for i in range(rank - 1)]
    if kind == "B":
        # Last simple root is short.
        edges[-1] = (rank - 2, rank - 1, -2, -1)
    elif kind == "C":
        # Last simple root is long.
        edges[-1] = (rank - 2, rank - 1, -1, -2)
    elif kind == "D":
        edges = [(i, i + 1, -1, -1) for i in range(rank - 3)]
        edges += [(rank - 3, rank - 2, -1, -1),
                  (rank - 3, rank - 1, -1, -1)]
    elif kind == "E":
        # Vertex 0 is central; arm lengths are (rank-4, 2, 1).
        edges = []
        vertex = 1
        for length in (rank - 4, 2, 1):
            previous = 0
            for _ in range(length):
                edges.append((previous, vertex, -1, -1))
                previous, vertex = vertex, vertex + 1
        assert vertex == rank
    elif kind == "F":
        # Vertices 0,1 long; vertices 2,3 short.
        assert rank == 4
        edges[1] = (1, 2, -2, -1)
    elif kind == "G":
        # Vertex 0 short, vertex 1 long.
        assert rank == 2
        edges = [(0, 1, -1, -3)]
    elif kind != "A":
        raise ValueError(kind)
    return cartan(rank, edges)


def sum_matrices(*matrices):
    rank = sum(len(a) for a in matrices)
    answer = [[0] * rank for _ in range(rank)]
    offset = 0
    for a in matrices:
        for i, row in enumerate(a):
            for j, value in enumerate(row):
                answer[offset + i][offset + j] = value
        offset += len(a)
    return answer


def inverse_permutation(tau):
    inverse = [0] * len(tau)
    for i, j in enumerate(tau):
        inverse[j] = i
    return inverse


def automorphisms(a):
    groups = defaultdict(list)
    for i in range(len(a)):
        signature = tuple(sorted((a[i][j], a[j][i]) for j in range(len(a))))
        groups[signature].append(i)
    groups = list(groups.values())
    answer = []
    for images in product(*(permutations(group) for group in groups)):
        tau = list(range(len(a)))
        for group, image in zip(groups, images):
            for i, j in zip(group, image):
                tau[i] = j
        if all(a[tau[i]][tau[j]] == a[i][j]
               for i in range(len(a)) for j in range(len(a))):
            answer.append(tuple(tau))
    return answer


def solve_exact(a, b):
    rank = len(a)
    augmented = [[Fraction(value) for value in row] + [Fraction(b[i])]
                 for i, row in enumerate(a)]
    for column in range(rank):
        pivot = next(i for i in range(column, rank)
                     if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for i in range(rank):
            if i != column:
                scale = augmented[i][column]
                augmented[i] = [left - scale * right for left, right
                                in zip(augmented[i], augmented[column])]
    return [row[-1] for row in augmented]


def black_data(a, x):
    """Compute longest element by increasing length, using RT-LIE-08 4.3/5.1."""
    if not x:
        return {}, {}, 0
    b = [[a[i][j] for j in x] for i in x]
    coefficients = solve_exact(b, [2] * len(x))
    assert all(value.denominator == 1 and value > 0 for value in coefficients)
    # columns[j] is w(alpha_j); right multiplication by s_i increases length
    # exactly when column i is positive.
    columns = [[int(i == j) for i in range(len(x))] for j in range(len(x))]
    length = 0
    while True:
        assert all(all(value >= 0 for value in column) or
                   all(value <= 0 for value in column) for column in columns)
        candidates = [j for j, column in enumerate(columns)
                      if all(value >= 0 for value in column)]
        if not candidates:
            break
        i = candidates[0]
        root = columns[i][:]
        columns = [[value - b[j][i] * root[k] for k, value in enumerate(column)]
                   for j, column in enumerate(columns)]
        length += 1
        assert length < 1000, "Finite-root longest computation did not terminate"
    opposition = {}
    for j, column in enumerate(columns):
        indices = [i for i, value in enumerate(column) if value]
        assert len(indices) == 1 and column[indices[0]] == -1
        opposition[x[j]] = x[indices[0]]
    return dict(zip(x, map(int, coefficients))), opposition, 2 * length


def connected_components(a):
    remaining = set(range(len(a)))
    components = []
    while remaining:
        component, queue = set(), [min(remaining)]
        while queue:
            i = queue.pop()
            if i in component:
                continue
            component.add(i)
            queue.extend(j for j in remaining if a[i][j] and j != i)
        remaining -= component
        components.append(component)
    return components


def check_type(label, a, expected_classes=None, expected_rank_k=None):
    rank = len(a)
    autos = automorphisms(a)
    involutions = [tau for tau in autos
                   if all(tau[tau[i]] == i for i in range(rank))]
    cache = {}
    for bits in range(1 << rank):
        x = tuple(i for i in range(rank) if bits & (1 << i))
        cache[x] = black_data(a, x)
    full_roots = cache[tuple(range(rank))][2]
    representatives = {}
    rejected_opposition = rejected_parity = 0
    admissible_total = 0
    for tau in involutions:
        for x, (c, opposition, black_roots) in cache.items():
            x_set = set(x)
            if {tau[i] for i in x} != x_set:
                continue
            if any(tau[i] != opposition[i] for i in x):
                rejected_opposition += 1
                continue
            parity = {i: sum(a[i][j] * c[j] for j in x)
                      for i in range(rank) if i not in x_set}
            if any(parity[i] % 2 for i in parity if tau[i] == i):
                rejected_parity += 1
                continue
            admissible_total += 1
            images = []
            for f in autos:
                inverse = inverse_permutation(f)
                image_x = tuple(sorted(f[i] for i in x))
                image_tau = tuple(f[tau[inverse[i]]] for i in range(rank))
                images.append((image_x, image_tau))
            key = min(images)
            if key in representatives:
                continue
            # All component exchanges must be white.
            for component in connected_components(a):
                if {tau[i] for i in component} != component:
                    assert not (x_set & component)
            white_orbits = []
            for i in range(rank):
                if i not in x_set and i <= tau[i]:
                    white_orbits.append(sorted({i, tau[i]}))
            split_rank = len(white_orbits)
            compact_dim = rank - split_rank + (full_roots + black_roots) // 2
            assert (full_roots + black_roots) % 2 == 0
            representatives[key] = {
                "black_vertices": [i + 1 for i in x],
                "tau": [i + 1 for i in tau],
                "white_orbits": [[i + 1 for i in orbit] for orbit in white_orbits],
                "black_opposition": {str(i + 1): j + 1 for i, j in opposition.items()},
                "H_X_simple_coroot_coefficients": {str(i + 1): value for i, value in c.items()},
                "white_alpha_H_X": {str(i + 1): value for i, value in parity.items()},
                "split_rank": split_rank,
                "black_roots_count": black_roots,
                "compact_fixed_dimension": compact_dim,
                "killing_signature_positive_negative":
                    [rank + full_roots - compact_dim, compact_dim],
            }
    representatives = [representatives[key] for key in sorted(representatives)]
    count = len(representatives)
    if expected_classes is not None:
        assert count == expected_classes, (label, count, expected_classes)
    if expected_rank_k is not None:
        actual = sorted((row["split_rank"], row["compact_fixed_dimension"])
                        for row in representatives)
        assert actual == sorted(expected_rank_k), (label, actual, expected_rank_k)
    return {
        "label": label, "column_coroot_cartan": a, "rank": rank,
        "full_roots_count": full_roots, "diagram_automorphisms": len(autos),
        "diagram_involutions": len(involutions),
        "admissible_pairs_before_diagram_isomorphism": admissible_total,
        "isomorphism_classes": count, "expected_count_check": expected_classes,
        "rejected_opposition_pairs": rejected_opposition,
        "rejected_fixed_white_parity_pairs": rejected_parity,
        "representatives": representatives,
    }


def main():
    checks = []
    for rank in range(1, 9):
        expected = 2 if rank == 1 else (rank + 1) // 2 + 2 + (rank % 2)
        checks.append(check_type(f"A{rank}", finite_matrix("A", rank), expected))
    for kind in ("B", "C"):
        for rank in range(2, 9):
            expected = rank + 1 if kind == "B" else rank // 2 + 2
            checks.append(check_type(f"{kind}{rank}", finite_matrix(kind, rank), expected))
    for rank in range(4, 9):
        checks.append(check_type(f"D{rank}", finite_matrix("D", rank),
                                 5 if rank == 4 else rank + 2))
    exceptional = [
        ("E", 6, [(0, 78), (2, 52), (2, 46), (4, 38), (6, 36)]),
        ("E", 7, [(0, 133), (3, 79), (4, 69), (7, 63)]),
        ("E", 8, [(0, 248), (4, 136), (8, 120)]),
        ("F", 4, [(0, 52), (1, 36), (4, 24)]),
        ("G", 2, [(0, 14), (2, 6)]),
    ]
    for kind, rank, rank_k in exceptional:
        checks.append(check_type(f"{kind}{rank}", finite_matrix(kind, rank),
                                 len(rank_k), rank_k))
    for rank, expected in ((1, 4), (2, 7)):
        a = finite_matrix("A", rank)
        checks.append(check_type(f"A{rank}+A{rank}", sum_matrices(a, a), expected))
    checks.append(check_type("rank_zero", [], 1))
    payload = {
        "scope": "All exceptional finite types; classical ranks through 8; D4 triality; A1+A1 and A2+A2 component exchanges; rank zero",
        "arithmetic": "Exact Python integers and Fraction Gaussian elimination; no floating point",
        "convention": "a_ij=alpha_i(h_j); internal indices 0-based, report vertices 1-based",
        "method": "Enumerate involutive directed Cartan automorphisms and invariant black subsets; compute opposition and H_X; test fixed white parity; quotient by all directed diagram automorphisms",
        "proof_dependency": "RT-LIE-17 Section8.5 Definition8.4, RT-LIE-08 Lemma4.1 and length/chamber Theorem5.1",
        "not_a_proof_replacement": "Existence, maximal-split reconstruction, completeness and real-isomorphism injectivity are proved universally in RT-LIE-17 Section8.5, not inferred from these counts",
        "checks_passed": True,
        "types_checked": len(checks),
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "results": checks,
    }
    target = Path(__file__).with_name("satake_admissibility_checks.json")
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "checks_passed": True, "types_checked": len(checks),
        "counts": {row["label"]: row["isomorphism_classes"] for row in checks},
        "output": target.name,
    }))


if __name__ == "__main__":
    main()

"""Exact finite certificates for the E6/E8 branch projections.

Only Python's standard library is needed. Every coefficient is a rational
polynomial modulo Phi_48 or Phi_120. There is no floating arithmetic.
Original authored code: CC0. GPT-6.1 Sol (OpenAI), Ultra, September 2026.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import hashlib, json

def field(modulus, order):
    degree = len(modulus)-1

    def reduce(values):
        values = list(values)+[F(0)]*max(0, degree-len(values))
        for i in range(len(values)-1, degree-1, -1):
            if values[i]:
                for j in range(degree):
                    if modulus[j]:
                        values[i-degree+j] -= values[i]*modulus[j]
        return tuple(values[:degree])

    @lru_cache(None)
    def product(a, b):
        values = [F(0)]*(2*degree-1)
        for i, v in enumerate(a):
            if v:
                for j, w in enumerate(b):
                    if w:
                        values[i+j] += v*w
        return reduce(values)

    @lru_cache(None)
    def inverse(a):
        columns = [product(a, tuple(F(i == j) for i in range(degree))) for j in range(degree)]
        rows = [[columns[j][r] for j in range(degree)]+[F(r == 0)] for r in range(degree)]
        for col in range(degree):
            pivot = next(r for r in range(col, degree) if rows[r][col])
            rows[col], rows[pivot] = rows[pivot], rows[col]
            factor = rows[col][col]
            rows[col] = [v/factor for v in rows[col]]
            for r in range(degree):
                if r != col and rows[r][col]:
                    factor = rows[r][col]
                    rows[r] = [v-factor*w for v, w in zip(rows[r], rows[col])]
        return tuple(row[-1] for row in rows)

    class K:
        def __init__(self, value=0):
            self.a = value.a if isinstance(value, K) else (F(value),)+(F(0),)*(degree-1)

        @classmethod
        def vector(cls, values):
            out = cls()
            out.a = reduce(values)
            return out

        def __add__(x, y):
            y = K(y)
            out = K()
            out.a = tuple(v+w for v, w in zip(x.a, y.a))
            return out

        __radd__ = __add__

        def __neg__(x):
            return K.vector([-v for v in x.a])

        def __sub__(x, y):
            return x+-K(y)

        def __rsub__(x, y):
            return K(y)+-x

        def __mul__(x, y):
            y = K(y)
            out = K()
            out.a = product(x.a, y.a)
            return out

        __rmul__ = __mul__

        def __truediv__(x, y):
            y = K(y)
            out = K()
            out.a = product(x.a, inverse(y.a))
            return out

        def __rtruediv__(x, y):
            return K(y)/x

        def __pow__(x, n):
            if n < 0:
                return (1/x)**(-n)
            out = K(1)
            while n:
                if n & 1:
                    out = out*x
                x = x*x
                n //= 2
            return out

        def __eq__(x, y):
            return x.a == K(y).a

        def __bool__(x):
            return any(x.a)

        def conj(x):
            return sum((v*conjugate_powers[i] for i, v in enumerate(x.a) if v), K())

    z = K.vector([0, 1])
    assert z**order == 1
    assert all(z**j != 1 for j in range(1, order) if order % j == 0)
    conjugate_powers = [z**((-j) % order) for j in range(degree)]
    return K, z

def run(name, branch, h, modulus):
    order = 4*h
    K, z = field([F(x) for x in modulus], order)
    zero, one = K(), K(1)
    epsilon = z**(h-1)
    iepsilon = z**(order-h+1)
    delta = -(epsilon**2+iepsilon**2)
    k = branch+1
    short = branch+3
    graph = {j: [] for j in range(branch+4)}
    for j in range(branch+2):
        graph[j].append(j+1)
        graph[j+1].append(j)
    graph[branch].append(short)
    graph[short].append(branch)
    for ns in graph.values():
        ns.sort()
    q = [zero, one]
    for _ in range(h):
        q.append(delta*q[-1]-q[-2])
    assert q[h] == 0
    mu = {j: q[j+1] for j in range(branch+1)}
    mu[short] = mu[branch]/delta
    mu[branch+2] = mu[branch]/(delta**2-1)
    mu[branch+1] = delta*mu[branch+2]
    assert all(sum((mu[b] for b in graph[a]), zero) == delta*mu[a] for a in graph)
    assert all(mu[a].conj() == mu[a] for a in graph)

    def paths(n, start):
        out = [(start,)]
        for _ in range(n):
            out = [p+(a,) for p in out for a in graph[p[-1]]]
        return out

    # The diagonal change of basis D_p=product sqrt(mu(p_j)) removes radicals.
    # Below, S_i=D^-1(ordinary cell swap)D.
    def apply_swap(vector, position):
        out = defaultdict(K)
        for p, value in vector.items():
            out[p] += epsilon*value
            a, c, d = p[position-1:position+2]
            if a == d:
                coefficient = iepsilon*mu[c]/mu[a]*value
                for b in graph[a]:
                    target = p[:position]+(b,)+p[position+1:]
                    out[target] += coefficient
        return {p: value for p, value in out.items() if value}

    word = ["v"]*k+["h"]*k
    swaps = []
    while any(word[j:j+2] == ["v", "h"] for j in range(2*k-1)):
        j = next(j for j in range(2*k-1) if word[j:j+2] == ["v", "h"])
        swaps.append(j+1)
        word[j:j+2] = ["h", "v"]
    assert len(swaps) == k*k and word == ["h"]*k+["v"]*k
    prefix = tuple(range(branch+1))+(short,)
    assert len(prefix) == k+1

    def matmul(a, b):
        rights = defaultdict(list)
        for (i, j), value in b.items():
            rights[i].append((j, value))
        out = defaultdict(K)
        for (i, middle), value in a.items():
            for j, other in rights[middle]:
                out[i, j] += value*other
        return {ij: value for ij, value in out.items() if value}

    def difference(a, b):
        out = dict(a)
        for ij, value in b.items():
            out[ij] = out.get(ij, zero)-value
        return {ij: value for ij, value in out.items() if value}

    def encode(value):
        return {str(i): str(v) for i, v in enumerate(value.a) if v}

    def encode_matrix(matrix):
        return {f"{i},{j}": encode(value) for (i, j), value in sorted(matrix.items())}

    endpoints = sorted({p[-1] for p in paths(k, short)})
    blocks = []
    for endpoint in endpoints:
        suffixes = [p for p in paths(k, short) if p[-1] == endpoint]
        n = len(suffixes)
        complete = [prefix+p[1:] for p in suffixes]
        lookup = {p: i for i, p in enumerate(suffixes)}
        selected = {p: i for i, p in enumerate(complete)}
        compression = {}
        for col, p in enumerate(complete):
            vector = {p: one}
            for position in swaps:
                vector = apply_swap(vector, position)
            for target, row in selected.items():
                if vector.get(target, zero):
                    compression[row, col] = vector[target]
        identity = {(i, i): one for i in range(n)}
        generators = {}
        for position in range(1, k):
            U = defaultdict(K)
            for col, p in enumerate(suffixes):
                a, c, d = p[position-1:position+2]
                if a == d:
                    for b in graph[a]:
                        target = p[:position]+(b,)+p[position+1:]
                        U[lookup[target], col] += mu[c]/mu[a]
            generators[position] = {ij: value for ij, value in U.items() if value}
        wenzl = identity
        for position in range(1, k):
            removed = matmul(matmul(wenzl, generators[position]), wenzl)
            factor = q[position]/q[position+1]
            wenzl = difference(wenzl, {ij: factor*value for ij, value in removed.items()})
        assert matmul(wenzl, wenzl) == wenzl
        for U in generators.values():
            assert not matmul(U, wenzl) and not matmul(wenzl, U)
            assert not matmul(U, compression) and not matmul(compression, U)
        wenzl_trace = sum((wenzl.get((i, i), zero) for i in range(n)), zero)
        wenzl_rank = next(j for j in range(n+1) if wenzl_trace == j)
        phase = sum((compression.get((i, i), zero) for i in range(n)), zero)
        metric = []
        for p in suffixes:
            weight = one
            for vertex in p[1:-1]:
                weight *= mu[vertex]
            metric.append(weight)
        assert all(weight.conj() == weight for weight in metric)
        if compression:
            i0, j0 = min(compression)
            pivot = compression[i0, j0]
            column = [compression.get((i, j0), zero) for i in range(n)]
            row_vector = [compression.get((i0, j), zero)/pivot for j in range(n)]
            # Every entry, including zeros, equals this rank-one outer product.
            assert all(compression.get((i, j), zero) == column[i]*row_vector[j]
                       for i in range(n) for j in range(n))
            column_norm = sum((metric[i]*v.conj()*v for i, v in enumerate(column)), zero)
            dual_row_norm = sum((v.conj()*v/metric[j] for j, v in enumerate(row_vector)), zero)
            # This is the sole nonzero squared singular value in the positive metric.
            assert column_norm*dual_row_norm == one
            if name == "E8" and endpoint == 4:
                # A compact human-checkable form of the heaviest norm identity.
                N = [6, 13, 15, 10, 3, -5, -8, -5]
                M = [-4, -1, 2, 3, 1, 1, 0, -4]
                phi30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]
                quotient = [-25, -33, -28, -8, 3, 12, 20]
                assert column_norm == sum((v*z**(4*j) for j, v in enumerate(N)), zero)
                assert dual_row_norm == sum((v*z**(4*j) for j, v in enumerate(M)), zero)
                residual = [sum(N[j]*M[i-j] for j in range(8) if 0 <= i-j < 8) for i in range(15)]
                residual[0] -= 1
                for j, value in enumerate(quotient):
                    for l, coefficient in enumerate(phi30):
                        residual[j+l] -= value*coefficient
                assert not any(residual)
            compression_rank = 1
            exponent = next((j for j in range(order) if phase == z**j), None) if n == 1 else None
        else:
            column, row_vector = [], []
            column_norm, dual_row_norm = zero, zero
            compression_rank = 0
            exponent = None
        row = {
            "endpoint": endpoint,
            "suffix_path_count": n,
            "suffix_paths": suffixes,
            "wenzl_rank": wenzl_rank,
            "compression_rank": compression_rank,
            "compression_phase_zeta_exponent": exponent,
            "compression_trace": encode(phase),
            "rank_one_column": [encode(v) for v in column],
            "rank_one_row": [encode(v) for v in row_vector],
            "positive_metric": [encode(v) for v in metric],
            "column_squared_norm": encode(column_norm),
            "dual_row_squared_norm": encode(dual_row_norm),
            "squared_nonzero_singular_value": 1 if compression else 0,
            "nonunit_singular_values": 0,
            "compression": encode_matrix(compression),
            "wenzl_projection": encode_matrix(wenzl)
        }
        if name == "E8" and endpoint == 4:
            row["compact_norm_identity"] = {
                "t": "zeta_120^4",
                "column_norm_coefficients": N,
                "dual_row_norm_coefficients": M,
                "Phi_30_coefficients": phi30,
                "NM_minus_one_quotient_coefficients": quotient,
                "NM_minus_one_equals_Phi30_times_quotient": True
            }
        blocks.append(row)
        print(json.dumps({"graph": name, "endpoint": endpoint, "size": n,
                          "rank": compression_rank, "wenzl_rank": wenzl_rank, "phase_exponent": exponent,
                          "partial_isometry": "exactly passed"}), flush=True)
    return {
        "graph": name,
        "h": h,
        "field_order": order,
        "cyclotomic_modulus": modulus,
        "root": 0,
        "branch": branch,
        "short_tip": short,
        "k": k,
        "index": "4cos²(pi/h)",
        "depth": branch+2,
        "graph_adjacency": graph,
        "perron_weights": {str(v): encode(mu[v]) for v in graph},
        "selected_prefix": prefix,
        "swap_positions": swaps,
        "blocks": blocks,
        "exact_branch_projection_commutation": True
    }

def main():
    phi48 = [1]+[0]*7+[-1]+[0]*7+[1]
    phi120 = [0]*33
    for exponent, value in {0: 1, 4: 1, 12: -1, 16: -1, 20: -1, 28: 1, 32: 1}.items():
        phi120[exponent] = value
    examples = [run("E6", 2, 12, phi48), run("E8", 4, 30, phi120)]
    expected = {
        "E6": [(0, 1, 1, 3), (2, 3, 0, None), (4, 1, 1, 39)],
        "E8": [(0, 1, 1, 5), (2, 5, 0, None), (4, 11, 1, None), (6, 4, 0, None)]
    }
    for example in examples:
        assert [(b["endpoint"], b["suffix_path_count"], b["compression_rank"],
                 b["compression_phase_zeta_exponent"]) for b in example["blocks"]] == expected[example["graph"]]
    source = Path(__file__)
    certificate = {
        "schema": "exceptional-flatness-exact-certificate/v1",
        "arithmetic": "Rational polynomial reduction modulo Phi_48/Phi_120; no tolerance",
        "basis": "D_p=product sqrt(mu(interior vertices)); matrices are D^-1 T D",
        "generator": "epsilon I + epsilon^-1 mu(input-middle)/mu(outer), when outer vertices agree",
        "wenzl_recursion": "F_(j+1)=F_j-[j]/[j+1] F_j U_j F_j",
        "checker_sha256": hashlib.sha256(source.read_bytes()).hexdigest().upper(),
        "graphs": examples
    }
    target = source.with_name("exceptional-flatness-certificate.json")
    target.write_text(json.dumps(certificate, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"graphs": len(examples), "exact": "passed",
                      "certificate": target.name}), flush=True)

if __name__ == "__main__":
    main()

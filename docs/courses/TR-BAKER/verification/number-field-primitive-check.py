"""Exact finite checks supporting, not replacing, the proofs of 16.11--16.14."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import re
import sympy as sp

HERE = Path(__file__).resolve().parent
X = sp.Symbol("X")


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def sub(z, w):
    return z[0]-w[0], z[1]-w[1]


def power(z, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, z)
        z = mul(z, z)
        n >>= 1
    return out


def divide(z, w):
    norm = w[0]**2+w[1]**2
    a = z[0]*w[0]+z[1]*w[1]
    b = z[1]*w[0]-z[0]*w[1]
    return (a//norm, b//norm) if a % norm == b % norm == 0 else None


def valuation(z, pi):
    assert z != (0, 0)
    v = 0
    while (q := divide(z, pi)) is not None:
        z = q
        v += 1
    return v


def cyclotomic_coefficients(n):
    return [int(c) for c in sp.Poly(sp.cyclotomic_poly(n, X), X).all_coeffs()]


def homogeneous(coeffs, a, b):
    out = (coeffs[0], 0)
    bp = (1, 0)
    for c in coeffs[1:]:
        bp = mul(bp, b)
        out = sub(mul(out, a), (-c*bp[0], -c*bp[1]))
    return out


def gaussian_norm_data():
    rows = []
    for n in range(40, 101):
        value = homogeneous(cyclotomic_coefficients(n), (1, 1), (1, 0))
        norm = value[0]**2+value[1]**2
        assert norm > n*n
        rows.append({"n": n, "value": list(value), "norm": norm})
    return rows


def main():
    coeffs = {n: cyclotomic_coefficients(n) for n in range(1, 97)}
    # Each listed pi generates a Gaussian prime ideal. For the split entries,
    # its norm is p; for inert 3 and 7 its norm is p^2; above 2, e=2.
    primes = [
        ((1, 1), 2, 2), ((2, 1), 5, 1), ((2, -1), 5, 1),
        ((3, 2), 13, 1), ((3, -2), 13, 1),
        ((4, 1), 17, 1), ((4, -1), 17, 1),
        ((3, 0), 3, 1), ((7, 0), 7, 1),
    ]
    units = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = order_count = large_old = 0
    critical_examples = []
    pairs = []
    for x in range(-3, 4):
        for y in range(-3, 4):
            a = (x, y)
            if a == (0, 0):
                continue
            for b in [(1, 0), (2, 0), (3, 0)]:
                if any(a == mul(u, b) for u in units):
                    continue
                # Coprime ideals for these particular denominators.
                if b == (2, 0) and (x-y) % 2 == 0:
                    continue
                if b == (3, 0) and x % 3 == y % 3 == 0:
                    continue
                pairs.append((a, b))
    for a, b in pairs:
        values = {n: homogeneous(cs, a, b) for n, cs in coeffs.items()}
        for pi, p, e in primes:
            if valuation(a, pi) or valuation(b, pi):
                continue
            normpi = pi[0]**2+pi[1]**2
            f = next(m for m in range(1, normpi)
                     if divide(sub(power(a, m), power(b, m)), pi) is not None)
            assert (normpi-1) % f == 0 and f % p != 0
            order_count += 1
            w0 = valuation(sub(power(a, f), power(b, f)), pi)
            for n in range(1, 97):
                actual = valuation(values[n], pi)
                expected = 0
                if n == f:
                    expected = w0
                elif n % f == 0:
                    t = n//f
                    j = 0
                    while t % p == 0:
                        t //= p
                        j += 1
                    if t == 1 and j:
                        prev = valuation(sub(power(a, n//p), power(b, n//p)), pi)
                        curr = valuation(sub(power(a, n), power(b, n)), pi)
                        expected = curr-prev
                        if (p-1)*prev < e:
                            assert curr == p*prev
                        elif (p-1)*prev > e:
                            assert curr == prev+e
                        else:
                            assert curr >= p*prev
                            if expected > e and len(critical_examples) < 8:
                                critical_examples.append(
                                    {"a": a, "b": b, "pi": pi, "n": n,
                                     "before": prev, "after": curr, "e": e})
                        if n > 36:
                            assert expected == e
                            large_old += 1
                assert actual == expected, (a, b, pi, n, actual, expected)
                count += 1
    assert critical_examples and large_old
    # Exact integer versions of both elementary arithmetic inequalities.
    for n in range(1, 10001):
        fac = sp.factorint(n)
        assert 2*int(sp.totient(n))**2 >= n
        assert 2**(4*len(fac)) <= 64**4*n
    # This coefficient comparison proves the constant domination for every
    # d>=1, after d+44d^3<=45d^3 and log(ed)>=1 are applied in the text.
    assert 45*2**35+11 < 2**42
    source = HERE.parent/"src"/"TR-BAKER-16.md"
    tags = [int(t) for t in re.findall(r"\\tag\{16\.(\d+)\}", source.read_text(encoding="utf-8"))]
    assert tags == list(range(1, 110))
    rows = gaussian_norm_data()
    record = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "state": "passed_finite_exact_checks",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "gaussian_pairs": len(pairs), "residue_order_cases": order_count,
        "cyclotomic_valuation_cases": count, "large_nonprimitive_cases": large_old,
        "ramified_cancellation_examples": critical_examples,
        "arithmetic_inequality_indices": 10000,
        "figure_values": rows,
        "limits": "Finite computations check concrete cases and constants. The unrestricted results are proved in the Markdown; these computations do not establish them by themselves.",
    }
    (HERE/"number-field-primitive-check.json").write_text(
        json.dumps(record, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in record.items()
                      if k not in ["figure_values", "manual_proof_checks",
                                   "ramified_cancellation_examples"]}))


if __name__ == "__main__":
    main()

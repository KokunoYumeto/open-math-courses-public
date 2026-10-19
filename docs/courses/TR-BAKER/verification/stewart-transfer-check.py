"""Exact elementary checks for the conditional transfer in Lemma 16.15."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib
import json
import math
import re
import sympy as sp

HERE = Path(__file__).resolve().parent
epsilon = Fraction(10, 519)-Fraction(2, 104)
assert epsilon == Fraction(1, 26988) and epsilon > 0
assert Fraction(16**6, math.factorial(6)) > 24*16**2
totient_cases = 0
for n in range(1, 10001):
    fs = sp.factorint(n)
    assert n <= int(sp.totient(n))*(len(fs)+1)
    assert 2**len(fs) <= n
    totient_cases += 1

X = sp.Symbol("X")
prime_cases = 0
for a in range(2, 9):
    for b in range(1, a):
        if math.gcd(a, b) != 1:
            continue
        for n in range(7, 31):
            cs = sp.Poly(sp.cyclotomic_poly(n, X), X).all_coeffs()
            phi = sum(int(c)*a**(len(cs)-1-j)*b**j for j, c in enumerate(cs))
            fac = sp.factorint(phi)
            old_product = 1
            primitive = []
            for p, e in fac.items():
                f = int(sp.n_order(a*pow(b, -1, int(p)) % p, p))
                if f == n:
                    assert p % n == 1
                    primitive.append(int(p))
                else:
                    old_product *= int(p)**int(e)
            assert old_product <= n
            assert len(primitive)*n <= int(max(fac))
            prime_cases += 1

names = ["../src/TR-BAKER-16.md"]
hashes = {}
tags = []
for name in names:
    p = HERE/name
    hashes[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    tags.extend(int(t) for t in re.findall(
        r"\\tag\{16\.(\d+)\}", p.read_text(encoding="utf-8")))
assert tags == list(range(1, 110))
report = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "state": "passed_finite_exact_checks",
    "epsilon": str(epsilon),
    "totient_cases": totient_cases,
    "prime_factor_cases": prime_cases,
    "consecutive_equation_tags": len(tags),
    "source_hashes": hashes,
    "conditional_boundary": "Lemma16.15 proves (16.88) implies (16.89); it does not establish (16.88).",
    "orientation_boundary": "BHV, Stewart and Mihailescu statements are not proof inputs to the drafted numbered results or exercises.",
    "limits": "Finite checks supplement the written proofs; they do not establish the universal prime valuation estimate or the literature theorems.",
}
(HERE/"stewart-transfer-check.json").write_text(
    json.dumps(report, indent=2)+"\n", encoding="utf-8", newline="\n")
print(json.dumps({k: v for k, v in report.items() if k != "source_hashes"}))

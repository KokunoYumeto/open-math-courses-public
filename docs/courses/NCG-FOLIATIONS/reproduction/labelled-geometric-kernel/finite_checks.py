"""CC0 exact finite mechanisms for the labelled geometric-kernel illustration.

No proof/provider files are read. These checks do not prove a general
Riemannian-pseudogroup globalization or a kernel existence theorem.
"""
from pathlib import Path
from itertools import product
from math import isqrt
import argparse
import json


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def qmul(u, v):
    """Exact multiplication in Q[alpha], alpha^2=1-alpha."""
    a, b = u
    c, d = v
    return a*c+b*d, a*d+b*c-b*d


def qpower(n):
    value = (1, 0)
    for _ in range(n):
        value = qmul(value, (0, 1))
    return value


def run():
    checks = []

    def check(name, condition, scope):
        assert condition, name
        checks.append({"name": name, "passed": True, "scope": scope})

    for m in range(1, 19):
        sign = (-1)**(m-1)
        rhs = tuple(sign*v for v in qpower(m))
        lhs = (-fibonacci(m-1), fibonacci(m))
        check(f"fibonacci-return-{m}", lhs == rhs,
              "Exact Q[alpha] identity; alpha^2=1-alpha, GK.3.")

    check("escaping-fibonacci-labels", all(fibonacci(m+1) > fibonacci(m)
          for m in range(2, 18)), "Finite monotonicity samples; escape is proved in GK.2.")
    labels = (-7, -2, 0, 3)
    cnd_ok = True
    for first in product(range(-2, 3), repeat=3):
        cs = (*first, -sum(first))
        lhs = sum(cs[i]*cs[j]*(labels[j]-labels[i])**2
                  for i in range(4) for j in range(4))
        rhs = -2*sum(cs[i]*labels[i] for i in range(4))**2
        cnd_ok &= lhs == rhs and lhs <= 0
    check("integer-labelled-cnd", cnd_ok,
          "125 exact zero-sum quadratic identities; GK.5.")
    check("integer-sublevels", all(
          {n for n in range(-40, 41) if n*n <= r} ==
          set(range(-isqrt(r), isqrt(r)+1)) for r in range(101)),
          "Exact integer sublevels within a sufficient finite window; GK.5.")
    check("full-inverse-character", all((n + (-n)) % 10 == 0
          and (2*n+2*(-n)) % 10 == 0 for n in range(-30, 31)),
          "Exact character and determinant exponents modulo 10; GK.2.")
    check("label-55-phase", 55 % 10 == 5 and (2*55) % 10 == 0,
          "Derivative=1; inverse central phase=-1; determinant=1.")

    # Finite action labels C3, noninvariant Hilbert map f=(0,1,4).
    # A common range p changes source labels to p-g; no unlabelled endpoint
    # or fixed-fibre simplification is used.
    f = (0, 1, 4)
    psi = lambda d, q: (f[(d+q) % 3]-f[q % 3])**2
    check("finite-symmetry", all(psi(d, q) == psi(-d, d+q)
          for d in range(3) for q in range(3)), "C3 arrow reversal, GK.11.")
    check("finite-kernel-is-not-invariant", len({psi(1, q) for q in range(3)}) == 3,
          "The compactification accepts a noninvariant coarse kernel.")
    cnd_ok = True
    gram_ok = True
    for p in range(3):
        e = [f[(p-g) % 3]-f[p] for g in range(3)]
        matrix = [[psi(j-i, p-j) for j in range(3)] for i in range(3)]
        for first in product(range(-2, 3), repeat=2):
            cs = (*first, -sum(first))
            lhs = sum(cs[i]*cs[j]*matrix[i][j]
                      for i in range(3) for j in range(3))
            rhs = -2*sum(cs[i]*f[(p-i) % 3] for i in range(3))**2
            cnd_ok &= lhs == rhs and lhs <= 0
        for i in range(3):
            for j in range(3):
                twice_gram = psi(i, p-i)+psi(j, p-j)-matrix[i][j]
                gram_ok &= twice_gram == 2*e[i]*e[j]
    check("finite-common-range-cnd", cnd_ok,
          "75 exact C3 tests using p-g source labels; GK.12.")
    check("finite-gram-typing", gram_ok,
          "27 exact Gram entries at their actual range p; GK.14.")
    b = lambda d, q: f[q % 3]-f[(d+q) % 3]
    check("finite-affine-cocycle", all(b(d, e+q)+b(e, q) == b(d+e, q)
          for d in range(3) for e in range(3) for q in range(3)),
          "27 exact affine composition identities; GK.15.")
    check("finite-displacement", all(b(d, q)**2 == psi(d, q)
          for d in range(3) for q in range(3)), "9 exact squared displacements.")
    check("right-invariant-control-typing", all((d+g)-g == d
          for d in range(-5, 6) for g in range(-8, 9)),
          "Composition difference is the arrow label d; GK.16-GK.17.")
    return {
        "schema": "labelled-geometric-kernel-finite-checks/v1",
        "result": "passed",
        "proof_scope": "Exact finite identities only; GK.9 remains an unproved general input.",
        "checks": checks,
        "count": len(checks),
        "cyclic_model": {"group": "C3", "f": list(f),
                         "psi_generator_1": [psi(1, q) for q in range(3)]},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("finite-checks.json"))
    args = parser.parse_args()
    result = run()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"result": result["result"], "count": result["count"]}))

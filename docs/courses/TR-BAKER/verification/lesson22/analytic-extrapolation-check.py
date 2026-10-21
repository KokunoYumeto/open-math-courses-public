"""Exact finite checks of examples; the general proofs are in the manuscript."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, gcd
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
out = {"scope": "Finite examples and exact parameter identities, not a proof of general AST."}

matrices = [
    [[-1, 0, 1, 1], [1, -1, 0, 1]],
    [[1, 1, 1, 1], [1, -1, 1, -1]],
    [[1, 0, 0, 0], [0, 1, 0, 0]],
    [[2, 1, -1, 1], [1, 2, 1, -1]],
]
kernels = []
for mat in matrices:
    n = len(mat[0]); h = max(abs(a) for row in mat for a in row); q = 3*n*h
    seen = {}
    for vec in product(range(q+1), repeat=n):
        av = tuple(sum(a*x for a, x in zip(row, vec)) for row in mat)
        if av in seen:
            c = [x-y for x, y in zip(vec, seen[av])]
            assert any(c) and max(map(abs, c)) <= q
            assert all(sum(a*x for a, x in zip(row, c)) == 0 for row in mat)
            kernels.append({"matrix": mat, "vector": c, "bound": q})
            break
        seen[av] = vec
    else:
        raise AssertionError("No pigeonhole collision")
out["integer_kernel_examples"] = kernels

disk_checks = 0
R, r, a = F(5), F(2), F(1)
bound = R*(r+a)/(R*R+r*a)
zs = [(F(x, 2), F(y, 2)) for x, y in product(range(-4, 5), repeat=2)
      if x*x+y*y <= 16]
bs = [(F(x, 2), F(y, 2)) for x, y in product(range(-2, 3), repeat=2)
      if x*x+y*y <= 4]
for (zx, zy), (bx, by) in product(zs, bs):
    numerator = R*R*((zx-bx)**2+(zy-by)**2)
    denominator = (R*R-bx*zx-by*zy)**2+(by*zx-bx*zy)**2
    assert numerator/denominator <= bound*bound
    disk_checks += 1
assert R*(r+a)/(R*R+r*a) == F(5, 9)
out["disk_factor_checks"] = disk_checks

parameter_checks = []
for n, m, k in product(range(2, 6), [1, 2], [5, 6]):
    K = n*k+2+12*n*m; C0 = 2*K+1
    ell = 32*C0+1; S = ell**(2*n+1)
    for q in [1, S+1]:
        A = 2*n*m*q*S**(n*k)
        D = A//S**k; T = A-n; M = T//2
        assert D**n == 2*n*m*q*(T+n)**(n-1)
        assert comb(D+n, n) >= 2*m*q*comb(T+n-1, n-1)
        assert 8*M >= A
        assert D*(S*S+S**4) <= 2*A
        assert D*(S*S+ell**4) <= 2*A
        assert S > 16*C0*(1+ell**(2*n))
        parameter_checks.append({"n": n, "m": m, "k": k, "ell": ell,
                                 "q_case": "one" if q == 1 else "S+1"})
out["parameter_cases"] = parameter_checks

count_checks = 0
for S, ell, kappa in product(range(1, 17), range(2, 12), range(1, 17)):
    old = min(kappa, S+1); new = min(kappa*ell, ell*S+1)
    assert 2*new >= ell*old
    count_checks += 1
assert 3*2+1 == 7 and 3*(2+1) == 9
# u/(2*pi*i) = 3/2: both exp(u) and exp(u/3) have order 2.
u = F(3, 2)
assert u.denominator == (u/3).denominator == 2
out["division_count_cases"] = count_checks
out["counterexamples"] = {
    "inclusive_endpoint_equality": {"S": 2, "ell": 3, "actual": 7, "incorrect": 9},
    "arbitrary_root_order": {"u_over_2pii": "3/2", "ell": 3, "old_order": 2, "new_order": 2},
}

x, y, z = sp.symbols("x y z")
zero = {x: 0, y: 0, z: 0}
def delta(p, i):
    return sp.expand(sp.diff(p, x)+y*sp.diff(p, z)) if i == 0 else sp.diff(p, y)
def word(p, w):
    for i in w:
        p = delta(p, i)
    return sp.expand(p)
assert sp.expand(delta(delta(z, 1), 0)-delta(delta(z, 0), 1)) == -1
jet_checks = 0
for i in range(6):
    for aa in range(i+1):
        bb = i-aa
        p = (1+x+y+z)*x**aa*y**bb
        for w in product(range(2), repeat=i):
            expected = factorial(aa)*factorial(bb) if w.count(0) == aa else 0
            assert word(p, w).subs(zero) == expected
            jet_checks += 1
out["noncommuting_jet_coefficient_checks"] = jet_checks

ideal_checks = 0
for T in range(5):
    for aa in range(T+2):
        for bb in range(T+2-aa):
            cc = T+1-aa-bb
            p = x**aa*y**bb*z**cc
            for order in range(T+1):
                for w in product(range(2), repeat=order):
                    assert word(p, w).subs(zero) == 0
                    ideal_checks += 1
    assert comb(T+3, 3) >= comb(T+2, 2)
out["primary_ideal_generator_word_checks"] = ideal_checks
assert sp.diff(x**4, x, 4) == 24
assert comb(3+2, 2) == 10 < comb(4+2, 2)
out["strict_escape_threshold"] = {"ideal": "(x,y)^4", "length": 10,
    "no_escape_through_order": 3, "escape": "d_x^4(x^4)=24"}
(ROOT/"analytic-extrapolation-check.json").write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"kernels": len(kernels), "disk_cases": disk_checks,
    "parameter_cases": len(parameter_checks), "division_counts": count_checks,
    "jet_coefficients": jet_checks, "ideal_words": ideal_checks, "status": "pass"}))

"""Exact boundary and cofactor checks supplementing the full Lesson 12 proofs.

Original implementation: OpenAI Codex — GPT-6 Astra, Ultra. CC0.
These finite calculations do not replace Lemmas 12.10–12.11.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, prod
from random import Random
import json


def determinant(a):
    if not a:
        return F(1)
    return sum((-1)**j * a[0][j] *
               determinant([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(len(a)))


def checks():
    rng = Random(12012)
    telescoping = cofactor_cases = centered_cases = 0
    for r in range(1, 13):
        multipliers = [max(F(1), F(i, 2)) for i in range(1, r+1)]
        assert prod(multipliers) == F(factorial(r), 2**(r-1))
        for _ in range(20):
            minima = sorted(F(rng.randrange(1, 40), 3) for _ in range(r))
            growth = minima[0]**r
            for i in range(1, r):
                growth *= (minima[i]/minima[i-1])**(r-i)
            assert growth == prod(minima)
            telescoping += 1
        # The final quotient can have arbitrary index k>=2; signs center
        # independently and repeated minima are included.
        for i in range(1, r+1):
            for k in range(2, 13):
                assert F(1, k)+F(i-1, 2) <= F(i, 2)
                centered_cases += 1
    for r in range(1, 6):
        for _ in range(18):
            a = [[F(rng.randrange(-7, 8), rng.randrange(1, 5))
                  for j in range(r)] for i in range(r)]
            if determinant(a) == 0:
                continue
            column_norms = [sum(abs(a[i][j]) for i in range(r))
                            for j in range(r)]
            for col, row in product(range(r), repeat=2):
                minor = [line[:col]+line[col+1:]
                         for i, line in enumerate(a) if i != row]
                assert abs(determinant(minor)) <= prod(
                    column_norms[j] for j in range(r) if j != col)
                cofactor_cases += 1
    # The missing d**r would fail even for a one-dimensional lattice.
    r, d, R, minimum = 1, 2, F(1), F(1)
    c4 = F(factorial(r)**2, 2**(r-1)*d**r)
    assert F(1) > c4*R/minimum
    assert F(1) == c4*d**r*R/minimum
    # Exercise 6: basis of Z^r + Z*(1/2,...,1/2), index two.
    for r in range(3, 10):
        a = [[F(int(i == j)) if j < r-1 else F(1, 2)
              for j in range(r)] for i in range(r)]
        assert determinant(a) == F(1, 2)
        assert sum(abs(a[i][-1]) for i in range(r)) == F(r, 2)
    # Exercise 4 must specialize exactly the theorem's constants.
    d, Delta = 2, 5
    C = 2*Delta
    V = 8*d**5*C*C**(d*(d*d+1))
    P = d*d*(2*3**d+1)**d
    L = d*factorial(d)*V**d*(2*d*d*P)**d
    S = d*(d*V+5)+5
    C0 = 64800*d*d*S*(2*S+1)
    q = (1600*C0*L*(d+1))**2
    G = d*V*(8*L+4*(d+5)*q**(2*d+1))+4*d+3
    assert V == 256*10**11 and P == 1444
    assert L == 4*V**2*(8*P)**2 and S == 4*V+15
    assert C0 == 259200*S*(2*S+1) and q == (4800*C0*L)**2
    assert G == 2*V*(8*L+28*q**5)+11
    return {
        "state": "passed",
        "successive_minimum_telescoping_cases": telescoping,
        "centered_quotient_cases": centered_cases,
        "exact_cofactor_checks": cofactor_cases,
        "index_two_basis_dimensions": list(range(3, 10)),
        "missing_degree_factor_counterexample_checked": True,
        "golden_ratio_constants_match_theorem": True,
        "golden_ratio_starting_exponent_bound_digits": len(str(5*G)),
        "scope": "Supplemental finite checks; full general proofs in Lesson 12.",
    }


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))

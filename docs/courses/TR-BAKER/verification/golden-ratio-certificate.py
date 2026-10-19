"""Exact certificate for the proved exponent bound |j|, |k| <= 2.

Integers (a,b) represent a+b*phi, where phi**2=phi+1.
The bound is proved in Proposition 12.7; enumeration checks its full box.
Original implementation: OpenAI Codex, GPT-6 Astra, Ultra. CC0.
"""
from itertools import product
import json


def multiply(x, y):
    a, b = x
    c, e = y
    return a*c+b*e, a*e+b*c+b*e


def norm(x):
    a, b = x
    return a*a+a*b-b*b


def power(exponent):
    base = (0, 1) if exponent >= 0 else (-1, 1)
    result = (1, 0)
    for _ in range(abs(exponent)):
        result = multiply(result, base)
    return result


def signed_unit(sign, exponent):
    return tuple(sign*a for a in power(exponent))


def certificate():
    units = [(s, j, signed_unit(s, j))
             for s, j in product((-1, 1), range(-2, 3))]
    assert len({u for s, j, u in units}) == 10
    assert all(norm(u) in (-1, 1) for s, j, u in units)
    answers = []
    for sx, j, x in units:
        for sy, k, y in units:
            if (x[0]+y[0], x[1]+y[1]) == (1, 0):
                s, t = norm(x), norm(y)
                assert 2*x[0]+x[1] == 1+s-t
                answers.append((sx, j, sy, k))
    expected = {
        (1, 1, -1, -1), (-1, -1, 1, 1),
        (1, 2, -1, 1), (-1, 1, 1, 2),
        (1, -1, 1, -2), (1, -2, 1, -1),
    }
    assert len(answers) == 6 and set(answers) == expected
    # An independent finite coefficient check of the four norm polynomials.
    norm_answers = set()
    for s, t in product((-1, 1), repeat=2):
        trace = 1+s-t
        for a, b in product(range(-4, 5), repeat=2):
            if 2*a+b == trace and norm((a, b)) == s:
                x = (a, b)
                y = (1-a, -b)
                assert norm(y) == t
                norm_answers.add((x, y))
    actual_pairs = {(signed_unit(sx,j), signed_unit(sy,k))
                    for sx,j,sy,k in answers}
    assert norm_answers == actual_pairs
    return {
        "state": "passed",
        "arithmetic": "integer pairs in Z[phi]",
        "proved_exponent_bound": 2,
        "ordered_candidates": 100,
        "ordered_solutions": sorted(answers),
        "independent_norm_cases": 4,
        "completeness_basis": "Proposition 12.7, trace/norm reduction",
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))

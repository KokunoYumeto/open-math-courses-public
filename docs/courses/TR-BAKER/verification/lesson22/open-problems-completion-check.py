"""Exact checks of the finite examples; conjectures are not tested or proved here."""
from pathlib import Path
from math import gcd
from itertools import product
import json

ROOT = Path(__file__).resolve().parent


def valuation(n, p):
    assert n != 0
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


lifting = []
for p in (3, 5, 7, 11, 13):
    for a, k, m in product(range(1, 5), range(3), (1, 2, 4)):
        actual = valuation(pow(1 + p**a, p**k * m) - 1, p)
        assert actual == a + k
        lifting.append(dict(p=p, a=a, k=k, m=m, valuation=actual))

# This excluded case verifies that the odd-prime hypothesis matters.
assert valuation(3**2 - 1, 2) == 3 != 1 + 1

points = []
for xyz in product(range(-5, 6), repeat=3):
    if xyz == (0, 0, 0) or gcd(*xyz) != 1:
        continue
    if next(c for c in xyz if c) < 0:
        continue
    x, y, z = xyz
    if x*x + y*y == z*z:
        points.append(xyz)
expected = {(1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)}
expected |= {(x, sy*y, sz*5) for x, y in ((3, 4), (4, 3))
             for sy, sz in product((-1, 1), repeat=2)}
assert set(points) == expected and len(points) == 12
positive_square_pairs = [(x, y, z) for x, y, z in product(range(1, 6), repeat=3)
                         if x*x+y*y == z*z]
assert positive_square_pairs == [(3, 4, 5), (4, 3, 5)]

record = {
    'state': 'passed',
    'arithmetic': 'exact_integer',
    'lifting_checks': lifting,
    'excluded_two_adic_example': {'actual': 3, 'incorrect_odd_prime_formula': 2},
    'primitive_projective_points_height_at_most_five': points,
    'positive_square_pairs': positive_square_pairs,
    'exact_assertions': len(lifting) + 3,
    'scope': 'Finite examples only. Uniform statements and conditional consequences are proved in the manuscript; no conjecture is asserted proved.',
}
(ROOT/'open-problems-completion-check.json').write_text(
    json.dumps(record, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'state': record['state'], 'exact_assertions': record['exact_assertions'],
                  'projective_points': len(points)}))

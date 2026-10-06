"""Exact endpoint and exponent checks for the larger-term S-unit gap proof.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0.
The finite cases test orientation and edge cases, not the global logarithm theorem.
The full general argument is written in Lesson 8, Section 7.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from laurent_constant import Interval, LN2

margin = 3 * (1 + LN2).log() - (1 - LN2.log())
assert margin.lo > 0
assert LN2.lo > F(1, 2) and LN2.hi < 1
assert Interval(F(3, 2)).log().lo > F(1, 3)
one_prime_margin = 4 * (1 + LN2).log() - LN2
assert one_prime_margin.lo > 0
assert (2 * 30**4 * LN2).lo > 1

def units(primes, limit):
    vectors = {1: (0,) * len(primes)}
    for index, prime in enumerate(primes):
        old = list(vectors.items())
        for value, vector in old:
            power, exponent = value, 0
            while power <= limit // prime:
                power *= prime
                exponent += 1
                new = list(vector)
                new[index] = exponent
                assert power not in vectors
                vectors[power] = tuple(new)
    return sorted(vectors.items())

records = []
for primes in [(2,), (3,), (2, 3), (2, 5), (2, 3, 5)]:
    values = units(primes, 4096)
    pairs = first_pairs = far_pairs = 0
    for (u, ui), (v, vi) in combinations(values, 2):
        assert u < v and v >= 2
        exponents = tuple(x - y for x, y in zip(ui, vi))
        B = max(map(abs, exponents))
        assert B >= 1 and 2**B <= v
        ratio = F(1)
        for prime, exponent in zip(primes, exponents):
            ratio *= F(prime)**exponent
        assert ratio == F(u, v) != 1
        assert (1 - ratio) * v == v - u
        if len(primes) == 1:
            assert 2 * (v - u) >= v
        pairs += 1
        first_pairs += u == 1
        far_pairs += v >= 2 * u
    records.append({'primes': primes, 'units': len(values), 'pairs': pairs,
                    'pairs_starting_at_one': first_pairs,
                    'pairs_with_v_at_least_2u': far_pairs})

RESULT = {'status': 'passed', 'proof_home': 'Lesson8Section7 larger-S-unit corollary',
          'scope': 'Exact arithmetic orientation/first-term/nonadjacent cases and outward endpoint intervals; the infinite proof and Matveev prerequisite remain in the lesson.',
          'exact_cases': records,
          'pair_count': sum(x['pairs'] for x in records),
          'logarithmic_endpoint_margin': [str(margin.lo), str(margin.hi)],
          'single_prime_endpoint_margin': [str(one_prime_margin.lo), str(one_prime_margin.hi)]}
if __name__ == '__main__':
    print(json.dumps(RESULT, indent=2))

"""Exact finite checks for counting measures and genuine first entrances.

These regressions do not establish an asymptotic distribution theorem.
The general proofs and scale hypotheses are in the accompanying lesson.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb
import json


def step(n):
    v, a = 3*n+1, 0
    while v % 2 == 0:
        v //= 2
        a += 1
    return v, a


def path(n, length):
    values, letters = [n], []
    for _ in range(length):
        n, a = step(n)
        values.append(n)
        letters.append(a)
    return values, letters


def entrance(values, x):
    return next((j for j, n in enumerate(values) if n <= x), None)


def norm(mu):
    return sum(map(abs, mu.values()), F(0))


def difference(mu, nu):
    return {v: mu.get(v, 0)-nu.get(v, 0) for v in set(mu)|set(nu)}


def main():
    counts = Counter()
    # The exact infinite geometric law can be compared with a finite observed
    # support: every unobserved word contributes its remaining probability mass.
    for first, size in [(1, 31), (7, 50), (101, 87), (1001, 151)]:
        starts = range(first, first+2*size, 2)
        for length in range(1, 6):
            hist = Counter(tuple(path(n, length)[1]) for n in starts)
            geometric_seen = sum((F(1, 2**sum(a)) for a in hist), F(0))
            actual_distance = sum((abs(F(v, size)-F(1, 2**sum(a)))
                                   for a, v in hist.items()), F(0)) + 1-geometric_seen
            for q in range(length, 3*length+1):
                residue = Counter(n % 2**q for n in starts)
                eta = sum((abs(F(residue.get(z, 0), size)-F(1, 2**(q-1)))
                           for z in range(1, 2**q, 2)), F(0))
                geometric_tail = 1-sum((F(comb(s-1, length-1), 2**s)
                                       for s in range(length, q)), F(0))
                assert actual_distance <= eta+2*geometric_tail
                counts['finite_sampling_comparisons'] += 1
    # Sharp multiplicity term and the positive-mass division estimate.
    for j in range(1, 9):
        for numerator in range(1, 10):
            eps = F(numerator, 10)
            mu = {'a': F(1)}
            eh = {'a': 1-eps, 'b': j*eps}
            assert norm(difference(eh, mu)) == (j+1)*eps
            counts['sharp_multiplicity_cases'] += 1
    for a in range(1, 10):
        for b in range(1, 10):
            mu = {0: F(a, 10), 1: 1-F(a, 10)}
            nu = {0: F(b, 12), 1: F(1, 3)}
            error = norm(difference(mu, nu))
            mass = sum(nu.values())
            assert abs(1-mass) <= error
            assert norm(difference(nu, {v:w/mass for v,w in nu.items()})) == abs(1-mass)
            assert norm(difference(mu, {v:w/mass for v,w in nu.items()})) <= 2*error
            counts['mass_comparisons'] += 1
    # Terminal entrance plus an explicit earlier-time check is equivalent to
    # the first entrance of the full path, with exact index offsets.
    for start in range(1, 402, 2):
        values, letters = path(start, 16)
        for x in [3, 5, 10, 20, 50]:
            first = entrance(values, x)
            for r in range(0, 10):
                for m in range(1, 5):
                    terminal = entrance(values[r:r+m+1], x) == m
                    no_earlier = all(v > x for v in values[:r])
                    assert (terminal and no_earlier) == (first == r+m)
                    counts['first_entrance_identifications'] += 1
    values, letters = path(7, 5)
    assert values == [7, 11, 17, 13, 5, 1] and letters == [1, 1, 2, 3, 4]
    assert entrance(values, 5) == 4 and entrance(values, 10) == 0
    assert entrance(values[2:], 5) == entrance(values[2:], 10) == 2
    # Pushforward can erase information; the contraction and mass preservation
    # used in the proof hold without probability normalisation.
    for seed in range(1, 40):
        mu = {j: F(((j+seed)%7)-3, 11) for j in range(13)}
        pushed = {v:sum((w for j,w in mu.items() if j%3 == v), F(0)) for v in range(3)}
        assert norm(pushed) <= norm(mu)
        assert sum(pushed.values()) == sum(mu.values())
        counts['pushforward_comparisons'] += 1
    tau = F(5097587, 77645938)
    assert 0 < tau < F(1, 2) and tau > F(1, 16)
    assert F(2, 5) < 1-2*tau
    assert (1-F(2, 5))/2 > tau
    print(json.dumps({'passed': True, 'arithmetic': 'exact integers and rational numbers',
        'counts': dict(counts), 'tau': str(tau), 'scope':
        'Finite sampling, multiplicity, mass, pushforward and first-entrance regression checks. '
        'No finite experiment verifies the asymptotic entrance theorem or convergence of all Collatz orbits.'}, indent=2))


if __name__ == '__main__':
    main()

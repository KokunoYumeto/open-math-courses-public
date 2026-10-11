"""Exact finite regressions for retained totals; not an analytic proof."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
import json


def compositions(total, length):
    if length == 0:
        if total == 0:
            yield ()
        return
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total-length+2):
        for tail in compositions(total-first, length-1):
            yield (first,)+tail


def offset(word):
    total, result = 0, F(0)
    for i, a in enumerate(word):
        total += a
        result += F(3**i, 2**total)
    return result


def mod_fraction(x, modulus):
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def mass(length, total):
    if length == 0:
        return F(int(total == 0))
    return F(comb(total-1, length-1), 2**total) if total >= length else F(0)


def main():
    counts = Counter()
    for n in range(1, 7):
        modulus = 3**n
        for total in range(n, 13):
            words = list(compositions(total, n))
            assert len(words) == comb(total-1, n-1)
            assert F(len(words), 2**total) == mass(n, total)
            counts['composition_laws'] += 1
            groups = defaultdict(list)
            for word in words:
                observed = tuple(word[2*j]+word[2*j+1] for j in range(n//2))
                if n % 2:
                    observed += (word[-1],)
                groups[observed].append(word)
                pair_offset, pair_total = F(0), 0
                for j in range(n//2):
                    pair_total += word[2*j]+word[2*j+1]
                    pair_offset += F(3**(2*j)*(2**word[2*j+1]+3), 2**pair_total)
                if n % 2:
                    pair_offset += F(3**(n-1), 2**total)
                assert pair_offset == offset(word)
                prefix = 0
                numerator = 0
                for a in word:
                    numerator = 3*numerator+2**prefix
                    prefix += a
                assert F(numerator, 2**total) == offset(tuple(reversed(word)))
                counts['pair_and_reversal_identities'] += 1
            for observed, group in groups.items():
                pairs = observed[:n//2]
                splits = product(*(range(1, b) for b in pairs))
                actual = Counter(mod_fraction(offset(w), modulus) for w in group)
                factored = Counter()
                for rights in splits:
                    word = tuple(a for b, right in zip(pairs, rights) for a in (b-right, right))
                    if n % 2:
                        word += (observed[-1],)
                    factored[mod_fraction(offset(word), modulus)] += 1
                assert actual == factored
                counts['conditional_product_distributions'] += 1

    for n in range(1, 7):
        for k in range(1, n+1):
            modulus = 3**k
            for total in range(n, 12):
                actual = Counter()
                for word in compositions(total, n):
                    x = mod_fraction(offset(word), modulus)
                    assert x == mod_fraction(offset(word[:k]), modulus)
                    actual[x] += F(1, 2**total)
                convolved = Counter()
                for first_total in range(k, total+1):
                    tail_mass = mass(n-k, total-first_total)
                    if not tail_mass:
                        continue
                    for word in compositions(first_total, k):
                        x = mod_fraction(offset(word), modulus)
                        convolved[x] += F(1, 2**first_total)*tail_mass
                assert actual == convolved
                counts['joint_residue_total_convolutions'] += 1

    for n in range(2, 81):
        assert mass(n, 2*n) >= F(1, 2*(2*n+1))
        for s in range(n, 3*n):
            assert mass(n, s+1)/mass(n, s) == F(s, 2*(s-n+1))
            counts['exact_adjacent_ratios'] += 1
        for d in range(1, n//2+1):
            for i in range(d):
                x = F(i+2, 2*n+2*i+2)
                assert 0 <= x <= F(1, 2)
                assert 2*x <= F(i+2, n)
            for i in range(2, d):
                x = F(i-1, 2*n-i-1)
                assert 0 <= x <= F(1, 2)
                assert 2*x <= F(2*i, n)
            counts['rational_lower_bound_inequalities'] += 1

    assert [mod_fraction(offset(w), 9) for w in compositions(3, 2)] == [2, 4]
    assert [mod_fraction(offset(w), 9) for w in compositions(4, 2)] == [8, 1, 2]
    assert [mod_fraction(offset(w), 27) for w in [(1, 2, 2), (2, 1, 2)]] == [2, 22]
    counts['worked_distributions'] = 3
    print(json.dumps({'passed': True, 'scope': 'Exact finite rational and integer regressions, not a proof of asymptotic Fourier decay', 'checks': dict(counts)}, indent=2))


if __name__ == '__main__':
    main()

"""Exact finite regressions for arithmetic separation and fine-scale mixing.

The all-scale analytic theorem is proved in the lesson, not by this program.
All geometric residue tails below are summed exactly, never truncated.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json


def compositions(total, length):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total-length+2):
        for rest in compositions(total-first, length-1):
            yield (first,)+rest


def offset(word):
    total, value = 0, F(0)
    for j, a in enumerate(word):
        total += a
        value += F(3**j, 2**total)
    return value


def recover(value, length):
    partials = []
    for r in range(length, 0, -1):
        denominator = value.denominator
        assert denominator > 1 and denominator & (denominator-1) == 0
        total = denominator.bit_length()-1
        partials.append(total)
        value -= F(3**(r-1), denominator)
    assert value == 0
    partials.reverse()
    return tuple(v-u for u, v in zip([0]+partials[:-1], partials))


def residue(value, modulus):
    return value.numerator*pow(value.denominator, -1, modulus) % modulus


@lru_cache(None)
def inverse_power_law(modulus):
    inv = pow(2, -1, modulus)
    period = 1
    while pow(inv, period, modulus) != 1:
        period += 1
    law = {pow(inv, a, modulus): F(2**(period-a), 2**period-1)
           for a in range(1, period+1)}
    assert len(law) == period and sum(law.values(), F(0)) == 1
    return law


@lru_cache(None)
def affine_law(length, modulus):
    # Reversing independent identically distributed coordinates gives the T law.
    law = {0: F(1)}
    for _ in range(length):
        new = defaultdict(F)
        for x, px in law.items():
            for inv, pa in inverse_power_law(modulus).items():
                new[(3*x+1)*inv % modulus] += px*pa
        law = dict(new)
    return law


def direct_continuation(word, n, modulus):
    # Direct ordered-sum state: current offset and cumulative inverse power.
    pairs = {(residue(offset(word), modulus), pow(2, -sum(word), modulus)): F(1)}
    for j in range(len(word), n):
        new = defaultdict(F)
        for (x, invsum), mass in pairs.items():
            for inv, pa in inverse_power_law(modulus).items():
                v = invsum*inv % modulus
                new[(x+3**j*v) % modulus, v] += mass*pa
        pairs = dict(new)
    result = defaultdict(F)
    for (x, _), mass in pairs.items():
        result[x] += mass
    return dict(result)


def lift(law, low, high):
    factor = F(1, 3**(high-low))
    return {x: factor*law.get(x % (3**low), F(0)) for x in range(3**high)}


def main():
    counts = defaultdict(int)
    for r in range(1, 6):
        seen = set()
        for total in range(r, 13):
            family = list(compositions(total, r))
            for word in family:
                value = offset(word)
                assert value not in seen
                seen.add(value)
                assert recover(value, r) == word
                numerator = value*2**total
                assert numerator.denominator == 1 and numerator.numerator % 2 == 1
                counts['recovered_words'] += 1
            for n in range(1, 7):
                residues = [residue(offset(w), 3**n) for w in family
                            if offset(w)*2**total < 3**n]
                assert len(residues) == len(set(residues))
                counts['height_separated_families'] += 1

    assert recover(F(49, 64), 3) == (2, 1, 3)
    assert recover(F(97, 128), 3) == (1, 3, 3)
    nums = [int(offset(w)*32) for w in compositions(5, 2)]
    assert nums == [19, 11, 7, 5]
    assert [x % 3 for x in nums] == [1, 2, 1, 2]
    assert [x % 9 for x in nums] == [1, 2, 7, 5]
    assert 4*F(1, 32)**2 == F(1, 256) == F(1, 32)*F(1, 8)
    assert 4*F(1, 4)**2 == F(1, 4)
    assert 1/(1-F(18, 19)**2) == F(361, 37)

    # Toy disjoint first-crossing pieces at threshold two. These test exact
    # decomposition, not the asymptotic high-probability event of the theorem.
    for n in (2, 3):
        modulus = 3**n
        mixture, direct = defaultdict(F), defaultdict(F)
        qsum = F(0)
        for r, total in product(range(1, n), range(3, 7)):
            words = [w for w in compositions(total, r)
                     if sum(w[:-1]) <= 2 < sum(w)
                     and max(w) <= 4 and offset(w)*2**total < modulus]
            f = defaultdict(F)
            q = len(words)*F(1, 2**total)
            qsum += q
            for word in words:
                f[residue(offset(word), modulus)] += F(1, 2**total)
                for y, mass in direct_continuation(word, n, modulus).items():
                    direct[y] += F(1, 2**total)*mass
                counts['prefix_tail_direct_words'] += 1
            assert sum(f.values(), F(0)) == q
            assert all(v == F(1, 2**total) for v in f.values())
            assert sum((v*v for v in f.values()), F(0)) == F(1, 2**total)*q
            tail = affine_law(n-r, 3**(n-r))
            g = defaultdict(F)
            for x, mass in tail.items():
                y = 3**r*pow(2, -total, modulus)*x % modulus
                assert y % (3**r) == 0
                assert (y//(3**r)*2**total) % (3**(n-r)) == x
                g[y] += mass
                counts['subgroup_inverse_identities'] += 1
            assert sum(g.values(), F(0)) == 1
            for x, fx in f.items():
                for y, gy in g.items():
                    mixture[(x+y) % modulus] += fx*gy
            counts['exact_prefix_collision_identities'] += 1
        assert dict(mixture) == dict(direct)
        full = affine_law(n, modulus)
        assert direct_continuation((), n, modulus) == full
        exceptional = [full.get(x, F(0))-mixture.get(x, F(0)) for x in range(modulus)]
        assert all(x >= 0 for x in exceptional)
        assert sum(exceptional, F(0)) == 1-qsum
        counts['exact_disjoint_full_law_decompositions'] += 1

    # Pullback equality modulo one and exact character order, with large moduli
    # represented as integers rather than enumerating all their states.
    for n in range(20, 61):
        m = (9*n+9)//10
        for r in (1, n//2, 17*n//20):
            for j in range(n-m):
                k = n-r-j
                assert 20*k > n
                for total, eta, x in product((3, 8, 17), (1, 2, 4, 5), (0, 1, 7)):
                    big, small = 3**n, 3**(n-r)
                    xi = 3**j*eta
                    image = 3**r*pow(2, -total, big)*x % big
                    frequency = xi*pow(2, -total, small) % small
                    assert (F(xi*image, big)-F(frequency*x, small)).denominator == 1
                    assert frequency % (3**j) == 0 and frequency % (3**(j+1)) != 0
                    assert (frequency*3**k) % small == 0
                    assert (frequency*3**(k-1)) % small != 0
                    counts['character_pullback_and_order_checks'] += 1

    mu = {n: affine_law(n, 3**n) for n in range(1, 5)}
    for a, b, n in ((1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)):
        assert lift(lift(mu[a], a, b), b, n) == lift(mu[a], a, n)
        counts['lift_compositions'] += 1
    a, b, c, n = 1, 2, 3, 4
    difference = lambda lo, hi: {x: mu[hi].get(x, F(0))-v for x, v in lift(mu[lo], lo, hi).items()}
    terms = [lift(difference(a, b), b, n), lift(difference(b, c), c, n), difference(c, n)]
    assert {x: sum((term[x] for term in terms), F(0)) for x in range(3**n)} == difference(a, n)
    for m, n in product(range(18, 91), range(91, 401, 7)):
        chain = [m]
        while chain[-1] < n:
            chain.append(min(n, 10*chain[-1]//9))
        for i, (lo, hi) in enumerate(zip(chain, chain[1:])):
            assert lo < hi and 10*lo >= 9*hi
            assert F(lo, m) >= F(19, 18)**i
        assert sum((F(m*m, h*h) for h in chain[:-1]), F(0)) <= F(361, 37)
        counts['integer_scale_chains'] += 1

    # Weighted conditional discrepancies, including zero-mass fibres.
    for m in range(1, 4):
        n = 4
        projected = defaultdict(F)
        for x, mass in mu[n].items():
            projected[x % (3**m)] += mass
        uniform = lift(projected, m, n)
        lhs = sum((abs(mu[n].get(x, F(0))-uniform[x]) for x in range(3**n)), F(0))
        rhs = F(0)
        for y, q in projected.items():
            if q:
                rhs += q*sum((abs(mu[n].get(x, F(0))/q-F(1, 3**(n-m)))
                              for x in range(y, 3**n, 3**m)), F(0))
        assert lhs == rhs
        counts['conditional_discrepancy_identities'] += 1

    print(json.dumps({'passed': True, 'counts': dict(counts),
        'arithmetic': 'Exact integers and fractions; full geometric residue tails summed by their exact period.',
        'scope': 'Finite checks of inverse maps, height separation, stopped-prefix masses and convolution, character orders, compatible lifts, conditional interpretation and exercises. The analytic large-n height, concentration and Fourier estimates and the uniform all-scale theorem are established by the written proofs, not these tests.'}, indent=2))


if __name__ == '__main__':
    main()

"""Exact finite regression examples for the four-lesson pathway.

No bounded enumeration is claimed to certify an infinite theorem.
Run with Python 3; only the standard library is used.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import json
import math


def T(n):
    return (3*n+1)//2 if n % 2 else n//2


def itinerary(n, k):
    word = []
    states = [n]
    for _ in range(k):
        word.append(n % 2)
        n = T(n)
        states.append(n)
    return tuple(word), states


def coordinates(word):
    a, s = 0, 0
    for k, b in enumerate(word):
        a = 3**b*a+b*2**k
        s += b
    return len(word), s, a


def push(mu, mapping):
    out = defaultdict(Q)
    for n, mass in mu.items():
        out[mapping(n)] += mass
    return dict(out)


def l1(mu, nu):
    return sum((abs(mu.get(n, 0)-nu.get(n, 0)) for n in mu.keys() | nu.keys()), Q(0))


def main():
    counts = Counter()
    # General return-clock example: rotation on Z/6Z, recorded at 0, 2 and 5.
    A = {0, 2, 5}
    x, clock = 0, 0
    visits = []
    for _ in range(20):
        visits.append(clock)
        tau = next(t for t in range(1, 7) if (x+t) % 6 in A)
        for r in range(tau):
            assert (x+r) % 6 == (clock+r) % 6
            counts['return_block_states'] += 1
        x = (x+tau) % 6
        clock += tau
    assert visits[:6] == [0, 2, 5, 6, 8, 11]
    assert visits == [t for t in range(clock) if t % 6 in A]

    # All residue classes and all word splits up to length ten, including k=0.
    for k in range(11):
        representatives = {}
        for n in range(2**k):
            w, states = itinerary(n, k)
            assert w not in representatives
            representatives[w] = n
            _, s, a = coordinates(w)
            assert 2**k*states[-1] == 3**s*n+a
            for t in range(1, 4):
                start = n+2**k*t
                wt, st = itinerary(start, k)
                assert wt == w
                assert st[-1] == states[-1]+3**s*t
                assert Q(2**k*st[-1]-a, 3**s) == start
                counts['cylinder_lifts'] += 1
            for cut in range(k+1):
                u, v = w[:cut], w[cut:]
                ku, su, au = coordinates(u)
                kv, sv, av = coordinates(v)
                assert a == 3**sv*au+2**ku*av
                assert Q(a, 2**k*3**s) == Q(au, 2**(ku+kv)*3**su)+Q(av, 2**kv*3**(su+sv))
                counts['concatenations'] += 1
        assert set(representatives) == set(product((0, 1), repeat=k))
        frequencies = Counter(sum(w) for w in representatives)
        assert all(frequencies[h] == math.comb(k, h) for h in range(k+1))
        # Positive full interval has the same word bijection.
        assert len({itinerary(n, k)[0] for n in range(1, 2**k+1)}) == 2**k
        counts['words'] += len(representatives)
    u, v = (1, 0, 0, 0, 1), (1, 1, 0)
    assert coordinates(u) == (5, 2, 19)
    assert coordinates(v) == (3, 2, 5)
    assert coordinates(u+v) == (8, 4, 331)
    assert coordinates(v+u) == (8, 4, 197)
    assert itinerary(37, 8)[1] == [37, 56, 28, 14, 7, 11, 17, 26, 13]
    assert itinerary(1, 3)[0] == (1, 0, 1)
    assert abs(Q(sum(sum(itinerary(n, 5)[0]) == 2 for n in range(1, 1001)), 1000)-Q(5, 16)) <= Q(10, 1000)

    def odd(n):
        while n % 2 == 0:
            n //= 2
        return n

    def val(n):
        return (n & -n).bit_length()-1

    H = [Q(0)]
    Ho = [Q(0)]
    for X in range(1, 257):
        H.append(H[-1]+Q(1, X))
        Ho.append(Ho[-1]+(Q(1, X) if X % 2 else 0))
        assert Ho[X] == H[X]-H[X//2]/2
        mu = {n:Q(1, n)/H[X] for n in range(1, X+1)}
        projected = push(mu, odd)
        oddlaw = {m:Q(1, m)/Ho[X] for m in range(1, X+1, 2)}
        D = Q(0)
        for m in oddlaw:
            j = (X//m).bit_length()-1
            assert projected[m] == (2-Q(1, 2**j))/(m*H[X])
            D += Q(1, 2**j*m)
            counts['logarithmic_fibres'] += 1
        assert D == H[X]-H[X//2]
        assert l1(projected, oddlaw)/2 <= D/H[X]
        if X <= 12:
            keys = list(oddlaw)
            maxevent = max(abs(sum((projected.get(m, 0)-oddlaw.get(m, 0) for m in E), Q(0)))
                           for length in range(len(keys)+1) for E in combinations(keys, length))
            assert maxevent == l1(projected, oddlaw)/2
        for a in range(10):
            weight = sum((Q(1, n) for n in range(1, X+1) if val(n) == a), Q(0))
            assert weight == Q(1, 2**a)*Ho[X//2**a]
            tail = sum((Q(1, n) for n in range(1, X+1) if val(n) > a), Q(0))
            assert tail == Q(1, 2**(a+1))*H[X//2**(a+1)]
            assert tail/H[X] <= Q(1, 2**(a+1))
            counts['valuation_strata_and_tails'] += 1
        if X % 4 == 0:
            E = [m for m in range(X//2+1, X+1) if m % 2]
            uniform = push({n:Q(1, X) for n in range(1, X+1)}, odd)
            assert sum(uniform[m] for m in E) == Q(1, 4)
            assert Q(len(E), X//2) == Q(1, 2)
    p4 = push({n:Q(1, n)/H[4] for n in range(1, 5)}, odd)
    assert p4 == {1:Q(21, 25), 3:Q(4, 25)}
    assert l1(p4, {1:Q(3, 4), 3:Q(1, 4)})/2 == Q(9, 100)

    # Finite map has a genuine nonentering two-cycle. None is the failure symbol.
    F = {1:1, 2:1, 3:2, 4:3, 5:6, 6:5}

    def entrance(n, threshold):
        if n is None:
            return None, None
        seen, t = set(), 0
        while n > threshold:
            if n in seen:
                return None, None
            seen.add(n)
            n = F[n]
            t += 1
        return n, t

    def K(threshold, mu):
        return push(mu, lambda n:entrance(n, threshold)[0])

    for x in range(1, 7):
        for y in range(x, 7):
            for n in [None]+list(F):
                px, tx = entrance(n, x)
                py, ty = entrance(n, y)
                assert entrance(py, x)[0] == px
                assert entrance(px, y)[0] == px
                if tx is not None:
                    assert tx == ty+entrance(py, x)[1]
                counts['nested_passage_tests'] += 1
    mu = {n:Q(1, 6) for n in F}
    assert K(2, mu) == {1:Q(1, 6), 2:Q(1, 2), None:Q(1, 3)}
    assert K(2, K(4, mu)) == K(2, mu)
    laws = [{1:Q(1)}, {None:Q(1)}, mu,
            {n:Q(n, 21) for n in F}, {2:Q(1, 3), 5:Q(2, 3)}]
    for law in laws:
        for x in range(1, 7):
            assert K(x, K(x, law)) == K(x, law)
            for other in laws:
                assert l1(K(x, law), K(x, other)) <= l1(law, other)
    for selected in product(laws, repeat=3):
        thresholds = [1, 2, 4]
        nu = [K(x, law) for x, law in zip(thresholds, selected)]
        errors = [l1(nu[i], K(thresholds[i], nu[i+1])) for i in range(2)]
        result = K(1, nu[-1])
        assert l1(nu[0], result) <= sum(errors)
        assert result.get(None, 0) <= nu[0].get(None, 0)+sum(errors)/2
        counts['finite_transport_chains'] += 1
    # For alpha=2 use exact logarithmic exponents: K=2^k and s=2^a.
    for k in range(8, 41):
        for a in range(k//2+1, 81):
            J = 1
            while Q(a, 2**J) >= Q(k, 2):
                J += 1
            ylog, ulog = Q(a, 2**J), Q(a, 2**(J+1))
            assert Q(k, 4) <= ylog < Q(k, 2)
            assert Q(k, 8) <= ulog < k
            assert ulog*2**J == Q(a, 2)
            counts['scale_selections'] += 1
    print(json.dumps({'passed':True, 'arithmetic':'exact integers and fractions',
                      'ranges':{'max_word_length':10, 'max_logarithmic_cutoff':256,
                                'finite_dynamics_states':6},
                      'counts':dict(counts),
                      'scope':'Finite examples and regression tests only; general theorems are proved in the lesson text. No formal certification or Collatz convergence claim.'}, indent=2))


if __name__ == '__main__':
    main()

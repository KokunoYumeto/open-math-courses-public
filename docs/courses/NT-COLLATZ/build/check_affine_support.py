"""Exact finite regressions for inverse branches, masses and moving supports.

All arithmetic below is integer or rational. These finite checks do not replace
the general proofs in the lesson and do not assert a universal orbit result.
"""
from fractions import Fraction as Q
from itertools import product
import json


def coords(word):
    total = offset = 0
    for a in word:
        offset = 3 * offset + 2**total
        total += a
    return total, offset


def step(n):
    m, a = 3*n+1, 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return m, a


def hit(n, b, limit):
    for j in range(limit+1):
        if n <= b:
            return j
        n = step(n)[0]
    return None


def decode(word, m):
    n = m
    for a in reversed(word):
        numerator = 2**a*n-1
        if numerator % 3:
            return None
        n = numerator//3
        assert n > 0 and n % 2
    return n


def odd_band(l, u):
    return [n for n in range(1, (u.numerator+u.denominator-1)//u.denominator, 2)
            if l <= n < u]


counts = dict(word_endpoint_pairs=0, genuine_inverse_branches=0,
              sharp_offset_words=0, terminal_records=0, terminal_families=0,
              support_comparisons=0, exact_atom_weight_identities=0)
for r in range(6):
    maximum = Q(0)
    for word in product(range(1,6), repeat=r):
        a, c = coords(word)
        f = Q(c, 2**a)
        assert f <= Q(3,2)**r-1
        maximum = max(maximum, f)
        counts['sharp_offset_words'] += 1
        for m in range(1,202,2):
            counts['word_endpoint_pairs'] += 1
            compatible = (2**a*m-c) % 3**r == 0
            n = decode(word, m)
            assert compatible == (n is not None)
            if n is None:
                continue
            assert n == (2**a*m-c)//3**r and m > f
            current = n
            for letter in word:
                current, actual = step(current)
                assert actual == letter
            assert current == m
            counts['genuine_inverse_branches'] += 1
    assert maximum == Q(3,2)**r-1

bands = [(Q(1),Q(50)), (Q(9),Q(10)), (Q(37,4),Q(12)),
         (Q(9),Q(28,3)), (Q(20),Q(81)), (Q(51),Q(101)),
         (Q(101,2),Q(501,2))]
for b in [6,20,50]:
    for h in range(1,5):
        endpoints = [m for m in range(1,202,2) if hit(m,b,h) == h]
        records = []
        for r in range(1,h+2):
            for word in product(range(1,4), repeat=r):
                a, c = coords(word)
                for m in endpoints:
                    n = decode(word,m)
                    if n is not None:
                        nominal = Q(2**a*m,3**r)
                        alpha = Q(c,2**a*m)
                        assert n == (1-alpha)*nominal
                        records.append((r+h,word,m,n,nominal,alpha))
        assert len(records) == len({row[3] for row in records})
        counts['terminal_records'] += len(records)
        counts['terminal_families'] += 1
        if not records:
            continue
        # q=exp(epsilon) and rho are exact upper bounds over this finite family.
        q = max(row[4]/row[3] for row in records)
        rho = max(row[5] for row in records)
        for z,u in bands:
            carrier = odd_band(z,u)
            assert carrier, 'Every pictured/tested band must support both laws.'
            d, H = len(carrier), sum((Q(1,n) for n in carrier),Q(0))
            uf = iff = uh = ih = Q(0)
            lower = set(odd_band(z/q,z))
            upper = set(odd_band(u/q,u))
            for _,_,_,n,n0,alpha in records:
                p,qq = z <= n < u, z < n0 < u
                mu,nu = Q(int(p),1)/(H*n), Q(int(p),1)/(H*n0)
                assert mu-nu == alpha*mu
                counts['exact_atom_weight_identities'] += 1
                if p != qq:
                    assert n in (upper if p else lower)
                uf += Q(int(p),d)
                iff += Q(int(qq),d)
                uh += mu
                ih += Q(int(qq),1)/(H*n0)
            assert uf <= 1 and uh <= 1
            union = lower | upper
            assert abs(uf-iff) <= Q(len(union),d)
            assert abs(uh-ih) <= rho*uh + sum((Q(1,n) for n in union),Q(0))/H
            assert iff <= uf + Q(len(lower),d)
            assert ih <= uh + sum((Q(1,n) for n in lower),Q(0))/H
            # The two measures have the same finite carrier.
            for n in carrier:
                assert z/u <= H*n/d <= u/z
            counts['support_comparisons'] += 1

word = (2,1,1)
assert coords(word) == (4,29)
for j in range(101):
    assert decode(word,17+54*j) == 9+32*j
orbit = [81]
letters = []
for _ in range(5):
    n,a = step(orbit[-1])
    orbit.append(n)
    letters.append(a)
assert orbit == [81,61,23,35,53,5]
assert letters == [2,3,1,1,5]
assert hit(81,50,5) == 2 and hit(61,50,1) == hit(53,50,1) == 1
assert decode((2,),61) == decode((2,3,1,1),53) == 81
assert Q(999,1000)-Q(21,2000)*Q(41,100) == Q(198939,200000)
assert 1+Q(41,100)+Q(41,100)**2/2+Q(41,100)**3/6 > Q(3,2)
assert Q(198939,200000)-Q(9,10) == Q(18939,200000)
assert Q(18939,200000)*300000 > 1
print(json.dumps(dict(passed=True, arithmetic='exact integer and rational',
    counts=counts, example=dict(word=[2], endpoint=7, source=9,
    nominal='28/3', relative_defect='1/28', same_support_harmonic='27/28',
    upper_endpoint_harmonic='0', repeated_source_orbit=orbit),
    scope='Finite regression tests only. General statements are proved in the lesson.'),indent=2))

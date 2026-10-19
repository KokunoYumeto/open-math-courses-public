"""Exact finite examples for the Stewart--Tijdeman construction.

Finite cases check the gcd and radical inequalities. They do not replace
the asymptotic argument in the written proof.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
from decimal import Decimal, localcontext
import hashlib
import json

HERE = Path(__file__).resolve().parent


def factors(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def radical(n):
    answer = 1
    for p in factors(n):
        answer *= p
    return answer


def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1


def smooth(primes, X):
    values = {1}
    for p in primes:
        new = set()
        for base in values:
            n = base
            while n <= X:
                new.add(n)
                n *= p
        values = new
    return sorted(values)


def box(values, primes, X):
    N = len(values)
    m = (N-1).bit_length()-1
    assert (1 << m) < N <= (1 << (m+1))
    buckets = {}
    for x in values:
        key = x % (1 << m)
        if key in buckets:
            y = buckets[key]
            break
        buckets[key] = x
    else:
        raise AssertionError('Pigeonhole pair missing')
    g = gcd(x, y)
    a, b, c = y//g, (x-y)//g, x//g
    P = 1
    for p in primes:
        P *= p
    G = radical(a*b*c)
    assert a+b == c and gcd(a, b) == gcd(a, c) == gcd(b, c) == 1
    assert g % 2 and v2(b) == v2(x-y) >= m
    assert G*N < 4*P*c and c <= X
    return {'N': N, 'm': m, 'x': x, 'y': y, 'gcd': g,
            'a': a, 'b': b, 'c': c, 'radical': G, 'v2_b': v2(b),
            'strict_radical_inequality': [G*N, 4*P*c]}


def logarithm(n):
    assert n >= 1
    power = n.bit_length()-1
    x = Fraction(n, 1 << power)

    def series(t):
        total = sum((2*t**(2*j+1)/(2*j+1) for j in range(80)), Fraction(0))
        tail = 2*t**161/(161*(1-t*t))
        return total, total+tail

    low, high = series((x-1)/(x+1))
    l2, u2 = series(Fraction(1, 3))
    return low+power*l2, high+power*u2


def outward_decimal(interval):
    scale = 10**50
    lo = interval[0].numerator*scale//interval[0].denominator
    hi = -((-interval[1].numerator*scale)//interval[1].denominator)
    return [str(x//scale)+'.'+str(x % scale).zfill(50) for x in (lo, hi)]


rows = []
for r in range(1, 6):
    primes = [3, 5, 7, 11, 13][:r]
    for X in (100, 1000, 10000, 100000):
        values = smooth(primes, X)
        assert all(n % 2 and all(p in primes for p in factors(n)) for n in values)
        if X <= 1000:
            assert values == [n for n in range(1, X+1) if all(p in primes for p in factors(n))]
        rows.append({'r': r, 'X': X, **box(values, primes, X)})
nontrivial_gcd = box([3, 9, 27], [3], 27)
assert nontrivial_gcd['gcd'] == 3

examples = []
assert 4375 == 5**4*7 == 2*3**7+1
assert 48234496 == 2**21*23 == 3**2*5**6*7**3+11**2
for a, b, c in [(1, 2*3**7, 4375), (11**2, 3**2*5**6*7**3, 48234496)]:
    assert a+b == c and gcd(a, b) == 1
    G = radical(a*b*c)
    lc, lg = logarithm(c), logarithm(G)
    quality = (lc[0]/lg[1], lc[1]/lg[0])
    examples.append({'a': a, 'b': b, 'c': c, 'radical': G,
                     'factorizations': {str(n): factors(n) for n in (a, b, c)},
                     'quality_interval': outward_decimal(quality)})

source = HERE/'lower-bound.md' if (HERE/'lower-bound.md').exists() else HERE.parent/'src/TR-BAKER-19.md'
output = HERE/'exact-check.json' if (HERE/'lower-bound.md').exists() else HERE/'abc-construction-check.json'
record = {'state': 'passed', 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'finite_box_cases': rows, 'nontrivial_gcd_case': nontrivial_gcd,
          'historical_examples': examples,
          'limitations': 'Finite examples verify exact integer identities and gcd/radical handling; infinitude and the constant4 are proved in the text using the programme quantitative PNT.'}
output.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({'cases': len(rows), 'nontrivial_gcd': nontrivial_gcd,
                  'examples': [{'radical': e['radical'], 'quality_interval': e['quality_interval']} for e in examples]}))

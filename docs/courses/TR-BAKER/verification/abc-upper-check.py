"""Exact checks for Lesson 19's constants and p-adic reduction.

The universal estimates are proved in upper-bound.md. Finite examples
exercise the reduction, including p=2, zero coefficients and signs.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, factorial
from collections import Counter
import hashlib
import json

HERE = Path(__file__).resolve().parent
SCALE = 10**35


def rounded(lo, hi):
    return (F(lo.numerator*SCALE//lo.denominator, SCALE),
            F(-((-hi.numerator*SCALE)//hi.denominator), SCALE))


def log_interval(x):
    x = F(x)
    assert x > 0
    power = 0
    while x < 1:
        x *= 2
        power -= 1
    while x >= 2:
        x /= 2
        power += 1

    def series(z):
        s = sum((2*z**(2*j+1)/(2*j+1) for j in range(48)), F(0))
        return s, s+2*z**97/(97*(1-z*z))

    a, b = series((x-1)/(x+1))
    c, d = series(F(1, 3))
    return rounded(a+power*(c if power >= 0 else d),
                   b+power*(d if power >= 0 else c))


def exp_interval(x):
    x = F(x)
    assert 0 <= x < 65
    total = sum((x**j/factorial(j) for j in range(65)), F(0))
    tail = x**65/factorial(65)/(1-x/66)
    return rounded(total, total+tail)


def decimal_pair(pair):
    return [f'{(v*SCALE).numerator//(v*SCALE).denominator//SCALE}.'
            f'{((v*SCALE).numerator//(v*SCALE).denominator)%SCALE:035d}'
            for v in pair]


constants = []
for label, arg, bound in [('exp(15/4)<48', F(15, 4), F(48)),
                          ('exp(13/10)<15/4', F(13, 10), F(15, 4)),
                          ('exp(1/4)<13/10', F(1, 4), F(13, 10)),
                          ('exp(1)<11/4', F(1), F(11, 4)),
                          ('exp(6)<405', F(6), F(405))]:
    lo, hi = exp_interval(arg)
    assert hi < bound
    constants.append({'claim': label, 'interval': decimal_pair((lo, hi)),
                      'strict_margin_lower': str(bound-hi)})
assert exp_interval(6)[0] > 400
assert exp_interval(1)[0] > F(27, 10)
assert exp_interval(F(12, 7))[1] < 6
assert exp_interval(F(3, 2))[1] < 6
assert log_interval(32)[1] < 4
assert F(52)*(F(11, 4))**2 < 400
assert log_interval(2)[0] > F(1, 2)
assert exp_interval(2)[0] > 6
# 2-log(4)+log(2)-1 = 1-log(2) > 0.
assert log_interval(2)[1] < 1

l0, l1 = log_interval(200*2680)
k0, k1 = 10400+2*l0, 10400+2*l1
extra0 = log_interval(2*(k0+6))[0]
extra1 = log_interval(2*(k1+6))[1]
kappa = rounded(k0+4+2*extra0, k1+4+2*extra1)
assert kappa[1] < 10500


def factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def valuation(n, p):
    assert n
    n = abs(n)
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


factor = {n: factors(n) for n in range(1, 501)}
counts = Counter()
examples = {}
for c in range(2, 501):
    for a in range(1, c//2+1):
        b = c-a
        if gcd(a, b) != 1:
            continue
        if (a, b, c) == (1, 1, 2):
            counts['exceptional'] += 1
            continue
        f = {**factor[a], **factor[b], **factor[c]}
        p = max(sorted(f), key=f.get)
        beta = f[p]
        u, v = ((c, b) if p in factor[a] else
                (c, a) if p in factor[b] else (a, b))
        xi = F(u, v)**2
        assert xi != 1 and xi.denominator % p
        value = valuation((xi-1).numerator, p)-valuation((xi-1).denominator, p)
        assert value >= beta
        bases = sorted(set(f)-{p})
        coefficients = [2*(factor[u].get(q, 0)-factor[v].get(q, 0)) for q in bases]
        product = F(1)
        for q, exponent in zip(bases, coefficients):
            product *= F(q)**exponent
        assert product == xi and any(coefficients)
        assert max(map(abs, coefficients)) <= 2*beta
        G = 1
        for q in f:
            G *= q
        assert p*factorial(len(bases)) <= G
        assert 2**beta <= c
        counts['triples'] += 1
        counts['p=2' if p == 2 else 'odd_p'] += 1
        if 0 in coefficients:
            counts['zero_coefficient'] += 1
        category = 'p=2' if p == 2 else 'p=3' if p == 3 else 'p>=5'
        if category not in examples:
            examples[category] = {'triple': [a, b, c], 'p': p, 'beta': beta,
                                  'Xi': str(xi), 'valuation': value,
                                  'bases': bases, 'coefficients': coefficients,
                                  'radical': G}

source = HERE/'upper-bound.md' if (HERE/'upper-bound.md').exists() else HERE.parent/'src/TR-BAKER-19.md'
output = HERE/'upper-check.json' if (HERE/'upper-bound.md').exists() else HERE/'abc-upper-check.json'
record = {'state': 'passed', 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'constant_checks': constants, 'kappa_interval': decimal_pair(kappa),
          'finite_reduction_counts': dict(counts), 'reduction_examples': examples,
          'limitations': 'Finite cases verify the exact squared-ratio reduction and numerical inequalities. All-rank cancellation, logarithmic-product estimate, inversion and asymptotic upper bound are proved in the text.'}
output.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({'state': 'passed', 'kappa_interval': record['kappa_interval'],
                  'counts': dict(counts), 'examples': examples}))

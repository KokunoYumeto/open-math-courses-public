"""Exact finite examples for Quotient distributions and Fourier mixing.

Standard library only. Roots of unity are represented in Q[z]/Phi_N(z),
with Phi_N constructed by exact polynomial division. These are regression
checks of finite instances, not proofs of the general statements.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def divide(p, d):
    p, d = trim(p), trim(d)
    q = [Q(0)] * max(1, len(p)-len(d)+1)
    while len(p) >= len(d) and any(p):
        k, c = len(p)-len(d), Q(p[-1], d[-1])
        q[k] += c
        for j, a in enumerate(d):
            p[k+j] -= c*a
        p = trim(p)
    return trim(q), trim(p)


@lru_cache(None)
def cyclotomic(n):
    p = [Q(-1)] + [Q(0)]*(n-1) + [Q(1)]
    for d in range(1, n):
        if n % d == 0:
            p, remainder = divide(p, cyclotomic(d))
            assert not any(remainder)
    return tuple(p)


class Field:
    def __init__(self, n):
        self.n, self.phi = n, cyclotomic(n)
        self.degree = len(self.phi)-1
        self.zero = self.reduce([0])
        self.one = self.reduce([1])

    def reduce(self, p):
        _, r = divide(list(map(Q, p)), self.phi)
        return tuple(r + [Q(0)]*(self.degree-len(r)))

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def scale(self, a, c):
        return tuple(c*x for x in a)

    def mul(self, a, b):
        p = [Q(0)]*(2*self.degree-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                p[i+j] += x*y
        return self.reduce(p)

    def conjugate(self, a):
        p = [Q(0)]*self.n
        for j, x in enumerate(a):
            p[(-j) % self.n] += x
        return self.reduce(p)

    def norm2(self, a):
        return self.mul(a, self.conjugate(a))

    def total(self, xs):
        out = self.zero
        for x in xs:
            out = self.add(out, x)
        return out

    def dft(self, f):
        assert len(f) == self.n
        out = []
        for r in range(self.n):
            p = [Q(0)]*self.n
            for x, a in enumerate(f):
                p[(-r*x) % self.n] += a
            out.append(self.reduce(p))
        return out


def reduce_mass(f, m):
    return [sum(f[a::m]) for a in range(m)]


def lift(h, n):
    m = len(h)
    assert n % m == 0
    return [h[x % m]/(n//m) for x in range(n)]


def conv(f, g):
    n = len(f)
    return [sum(f[y]*g[(x-y) % n] for y in range(n)) for x in range(n)]


def compositions(total, length):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total-length+2):
        for tail in compositions(total-first, length-1):
            yield (first,)+tail


def offset(word, modulus):
    s, out = 0, 0
    for i, a in enumerate(word):
        s += a
        out += 3**i * pow(pow(2, s, modulus), -1, modulus)
    return out % modulus


def main():
    quotients = 0
    for n in range(1, 19):
        field = Field(n)
        f = [Q((x*x+2*x+3) % 7 + 1) for x in range(n)]
        f = [x/sum(f) for x in f]
        g = [Q((3*x+1) % 5 + 1) for x in range(n)]
        g = [x/sum(g) for x in g]
        hf, hg = field.dft(f), field.dft(g)
        c = conv(f, g)
        assert field.dft(c) == [field.mul(a,b) for a,b in zip(hf,hg)]
        assert field.total(map(field.norm2,hf)) == field.scale(field.one, n*sum(x*x for x in f))
        for m in range(1, n+1):
            if n % m:
                continue
            l = n//m
            reduced = reduce_mass(f, m)
            p = lift(reduced, n)
            assert reduce_mass(p,m) == reduced
            assert lift(reduce_mass(p,m),n) == p
            hp = field.dft(p)
            assert hp == [hf[r] if r % l == 0 else field.zero for r in range(n)]
            # Direct evaluation of the coarse transform in the same root field:
            for k in range(m):
                poly = [Q(0)]*n
                for a, mass in enumerate(reduced):
                    poly[(-l*k*a) % n] += mass
                assert field.reduce(poly) == hf[l*k]
            diff = [a-b for a,b in zip(f,p)]
            energy = field.total(field.norm2(hf[r]) for r in range(n) if r % l)
            assert energy == field.scale(field.one,n*sum(x*x for x in diff))
            assert sum(abs(x) for x in diff)**2 <= n*sum(x*x for x in diff)
            h = [Q(1,l) if x % m == 0 else Q(0) for x in range(n)]
            assert conv(f,h) == p
            quotients += 1
    f = [Q(1,2) if x in (0,1) else Q(0) for x in range(9)]
    g = [Q(1,2) if x in (0,3) else Q(0) for x in range(9)]
    mu = conv(f,g)
    p = lift(reduce_mass(mu,3),9)
    diff = [a-b for a,b in zip(mu,p)]
    assert sum(map(abs,diff)) == Q(2,3)
    assert 9*sum(x*x for x in diff) == Q(3,4)
    field = Field(9)
    for r, coeff in enumerate(field.dft(g)):
        assert field.norm2(coeff) == field.scale(field.one,Q(1) if r%3==0 else Q(1,4))
    assert sum(map(abs,diff))**2 <= Q(1,4)*9*sum(x*x for x in f)
    uh = [Q(1,3) if x%3==0 else Q(0) for x in range(9)]
    assert sum(abs(x-Q(1,9)) for x in uh) == Q(4,3)
    block_cases = word_cases = 0
    for n in range(2,5):
        modulus = 3**n
        for k in range(1,n):
            for l in range(k,k+5):
                f = [Q(0)]*modulus
                g = [Q(0)]*modulus
                actual = [Q(0)]*modulus
                prefixes = list(compositions(l,k))
                tails = list(product(range(1,4),repeat=n-k))
                tail_mass = Q(1,len(tails))
                multiplier = 3**k*pow(pow(2,l,modulus),-1,modulus)
                images = {(multiplier*z)%modulus for z in range(3**(n-k))}
                assert images == set(range(0,modulus,3**k))
                for prefix in prefixes:
                    f[offset(prefix,modulus)] += Q(1,2**l)
                for tail in tails:
                    t = multiplier*offset(tail,3**(n-k)) % modulus
                    g[t] += tail_mass
                    for prefix in prefixes:
                        result = offset(prefix+tail,modulus)
                        assert result == (offset(prefix,modulus)+t)%modulus
                        actual[result] += Q(1,2**l)*tail_mass
                        word_cases += 1
                assert conv(f,g) == actual
                assert sum(actual) == Q(len(prefixes),2**l)
                block_cases += 1
    # Explicit exercise values; no asymptotic inference is made from these tests.
    d = [Q(1),Q(0),Q(0),Q(0)]
    p2, p1 = lift(reduce_mass(d,2),4), lift(reduce_mass(d,1),4)
    assert [sum(abs(x-y) for x,y in zip(a,b)) for a,b in [(d,p1),(d,p2),(p2,p1)]] == [Q(3,2),Q(1),Q(1)]
    assert conv([Q(1,2),Q(1,2)],[Q(1,2),Q(1,2)]) == [Q(1,2),Q(1,2)]
    print(json.dumps({'passed':True,'arithmetic':'exact fractions and cyclotomic polynomial quotients',
        'cyclic_moduli':list(range(1,19)),'quotient_cases':quotients,
        'prefix_tail_cases':block_cases,'prefix_tail_words':word_cases,
        'example_l1':'2/3','example_scaled_energy':'3/4',
        'scope':'Finite regression checks; general theorems are proved in the lesson. Tail enumeration uses an explicitly finite uniform test law, not a truncated law presented as a full geometric distribution.'},indent=2))


if __name__ == '__main__':
    main()

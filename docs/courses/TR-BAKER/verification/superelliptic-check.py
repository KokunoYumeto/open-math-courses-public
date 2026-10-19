"""Exact supplementary checks for Lesson 15; no numerical search proves finiteness."""
from pathlib import Path
from fractions import Fraction
from itertools import product
from math import isqrt
import hashlib
import json
import re
import sympy as sp

HERE = Path(__file__).resolve().parents[1] / 'src'


def check():
    A, B, t, r = sp.symbols("A B t r", nonzero=True)
    u1 = (r + B/r)/2
    u3 = (B/r - r)/2
    u2 = u1 - t*r
    assert sp.factor(u1**2-u3**2-B) == 0
    assert sp.factor(u1**2-u2**2-A - (r*r*t*(1-t)+B*t-A)) == 0
    assert sp.factor((A-B*t)/(t*(1-t))*t*(1-t)+B*t-A) == 0

    triple_cases = 0
    for a, b, c in product(range(-8, 9), repeat=3):
        aa, bb = a*a-b*b, a*a-c*c
        if not aa or not bb or aa == bb:
            continue
        rr, pp = a-c, a-b
        tt = Fraction(pp, rr)
        D = abs(bb)
        P, Q = Fraction(D*pp, rr), Fraction(D*(b-c), rr)
        assert P.denominator == Q.denominator == 1 and P+Q == D
        assert tt not in (0, 1)
        assert Fraction(aa-bb*tt, tt*(1-tt)) == rr*rr
        assert (Fraction(rr)+Fraction(bb, rr))/2 == a
        assert (Fraction(bb, rr)-Fraction(rr))/2 == c
        assert a-tt*rr == b
        support = set(sp.factorint(abs(D*aa*bb*(bb-aa))))
        assert set(sp.factorint(abs(P.numerator))) <= support
        assert set(sp.factorint(abs(Q.numerator))) <= support
        triple_cases += 1

    rational_power_cases = 0
    for m, a, b, c, d, sign in product(
            range(2, 6), range(8), range(8), range(3), range(2), (-1, 1)):
        z = sign*2**a*3**b*5**(m*c)*7**(m*d)
        mu = sign*2**(a % m)*3**(b % m)
        xi = 2**(a//m)*3**(b//m)*5**c*7**d
        assert z == mu*xi**m and xi >= 1
        rational_power_cases += 1

    u, v, w = sp.symbols("u v w")
    cube = sp.rem(sp.Poly((u+v*w)**3, w), sp.Poly(w*w+2, w)).as_expr()
    assert sp.expand(cube-(u**3-6*u*v*v+v*(3*u*u-2*v*v)*w)) == 0
    X, Y = sp.symbols("X Y")
    assert sp.expand((X+2)*(X*X-2*X+4)-(X**3+8)) == 0

    text = (HERE/'TR-BAKER-15.md').read_text(encoding='utf-8')
    blocks = re.findall(r"~~~python\n(.*?)\n~~~", text, flags=re.S)
    assert len(blocks) == 1
    ns = {}
    exec(compile(blocks[0], 'lesson15-included-certificate', 'exec'), ns)
    assert ns['M'] == 1966336
    assert ns['divided_residues'] == {2532, 5149}
    odd_cases = []
    for k in range(8):
        value = 2**(2*k+1)-7
        if value >= 0 and isqrt(value)**2 == value:
            odd_cases.append([isqrt(value), 2*k+1])
    assert odd_cases == [[1, 3], [5, 5], [11, 7], [181, 15]]
    assert 22**2 < 505 < 23**2
    assert 45**2 < 2041 < 46**2
    assert 90**2 < 8185 < 91**2

    # Independent integer-matrix check of recurrence coverage, also backwards.
    M = ns['M']
    x, y = 1, 2
    forward_y, backward_y = [], []
    for i in range(256):
        forward_y.append(y)
        x, y = (3*x+4*y) % M, (2*x+3*y) % M
    x, y = 1, 2
    for i in range(256):
        backward_y.append(y)
        x, y = (3*x-4*y) % M, (-2*x+3*y) % M
    assert set(backward_y) == set(forward_y)
    assert {y//256 for y in forward_y if y % 256 == 0} == {2532, 5149}

    names = ['TR-BAKER-15.md']
    all_text = '\n'.join((HERE/n).read_text(encoding='utf-8') for n in names)
    tags = re.findall(r'\\tag\{15\.(\d+)\}', all_text)
    assert sorted(map(int, tags)) == list(range(1, 76))
    for n in names:
        s = (HERE/n).read_text(encoding='utf-8')
        assert s.count(r'\[') == s.count(r'\]')
        assert s.count(r'\(') == s.count(r'\)')
    return {
        'scope': 'Exact algebra and included Ramanujan–Nagell certificate; text proofs supply the all-parameter arguments.',
        'symbolic_recovery_identities': 3,
        'rational_three_square_cases': triple_cases,
        'rational_power_factor_cases': rational_power_cases,
        'quadratic_ring_cube_identity': True,
        'mordell_plus7_factorization': True,
        'ramanujan_nagell': {
            'included_certificate_executed': True,
            'modulus': M, 'period_sufficient': 256,
            'divided_residues': sorted(ns['divided_residues']),
            'power_tests': [ns['power_mod'](b, 3840, 7681) for b in [2, 2532, 5149]],
            'backwards_period_independently_checked': True,
            'odd_exponent_solutions': odd_cases,
            'even_exponent_solution': [3, 4],
        },
        'equation_tags': len(tags),
        'source_hashes': {
            n: hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in names
        },
        'limits': 'These finite checks supplement, and do not replace, the all-parameter proofs in the lesson.'
    }


if __name__ == '__main__':
    print(json.dumps(check(), ensure_ascii=False, indent=2))

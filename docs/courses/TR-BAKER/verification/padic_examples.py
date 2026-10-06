"""Exact finite checks of worked p-adic examples in Lesson09; standard library. CC0."""
from math import comb, factorial
from fractions import Fraction
import json


def valuation(n, p):
    if n == 0:
        return float('inf')
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


def digitsum(n, p):
    answer = 0
    while n:
        n, digit = divmod(n, p)
        answer += digit
    return answer


def shifted_cyclotomic(p, u):
    degree = (p-1)*p**(u-1)
    return [sum(comb(j*p**(u-1), k) for j in range(p) if j*p**(u-1) >= k)
            for k in range(degree+1)]


def main():
    checks = 0
    for base, p in [(16, 5), (729, 7), (5, 2)]:
        initial = valuation(base-1, p)
        for k in range(1, 161):
            assert valuation(pow(base, k)-1, p) == initial + valuation(k, p)
            checks += 1
    for k in range(1, 161):
        expected = 1 if k % 2 else 2 + valuation(k, 2)
        assert valuation(pow(3, k)-1, 2) == expected
        checks += 1
    # These examples discriminate the strict cutoff from its boundary.
    assert valuation(3-1, 2) == 1 and valuation(3**2-1, 2) == 3
    assert (-1)**2-1 == 0
    for p in [2, 3, 5, 7, 11]:
        for n in range(1, 180):
            assert valuation(factorial(n), p) == (n-digitsum(n, p))//(p-1)
            checks += 1
        for j in range(1, 5):
            n = p**j
            # Exact valuation of the exponential term at the boundary.
            assert Fraction(n, p-1) - (n-1)//(p-1) == Fraction(1, p-1)
            checks += 1
    for p, maximum_u in [(2, 5), (3, 3), (5, 2), (7, 2)]:
        for u in range(1, maximum_u+1):
            coefficients = shifted_cyclotomic(p, u)
            assert coefficients[-1] == 1 and coefficients[0] == p
            assert all(x % p == 0 for x in coefficients[:-1])
            checks += 1
    # Independently multiply pairs A+B*sqrt(2) to check the labelled example.
    def multiply(x, y):
        a,b=x;c,d=y
        return (a*c+2*b*d, a*d+b*c)
    square = multiply((1,1), (1,1))
    fourth = multiply(square, square)
    assert square == (3,2) and fourth == (17,12)
    assert multiply((0,4),(3,2)) == (16,12)
    assert valuation(16**125-1,5) == 4 and valuation(729**343-1,7) == 4
    assert valuation(factorial(99),5) == 22
    print(json.dumps({'passed':True,'finite_checks':checks,'boundary_counterexamples':True,
                      'quadratic_example_exact':True,'proof_scope':'Worked examples and exact coefficient identities; general proofs are in Lesson09.'}))


if __name__ == '__main__':
    main()

"""Exact relative class-number determinants; Python 3 standard library, CC0."""
from fractions import Fraction
import json

def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        v = a[k][k]
        result *= v
        for i in range(k + 1, len(a)):
            factor = a[i][k] / v
            for j in range(k + 1, len(a)):
                a[i][j] -= factor * a[k][j]
    assert result.denominator == 1
    return result.numerator

EXPECTED = {3: (-1, 1), 5: (10, 1), 7: (-196, 1), 11: (-234256, 1),
            13: (11881376, 1), 17: (52523350144, 1),
            19: (-4347792138496, 1), 23: (-127262242448329728, 3)}

def check():
    rows = []
    for p, expected in EXPECTED.items():
        n = (p - 1) // 2
        matrix = [[2 * (a * pow(b, -1, p) % p) - p
                   for b in range(1, n + 1)] for a in range(1, n + 1)]
        d = determinant(matrix)
        hminus = Fraction((-1)**n * d, (2 * p)**(n - 1))
        assert hminus.denominator == 1
        assert (d, hminus.numerator) == expected
        rows.append({"p": p, "determinant": d, "relative_class_number": hminus.numerator,
                     "all_exact_checks_passed": True})
    return rows

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

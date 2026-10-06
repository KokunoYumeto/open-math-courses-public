"""Exact normalization checks for algebraic jets and factorial derivatives.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
The universal proofs are in the lesson; these finite checks cover signs,
zero evaluation factors, repeated blocks and derivative normalizations.
"""
from math import factorial, gcd
import json
import sympy as sp


def integer_coefficients(offsets):
    coefficients = [1]
    for offset in offsets:
        next_coefficients = [0]*(len(coefficients)+1)
        for index, coefficient in enumerate(coefficients):
            next_coefficients[index] += offset*coefficient
            next_coefficients[index+1] += coefficient
        coefficients = next_coefficients
    return coefficients


denominator_checks = 0
zero_coefficients = 0
for block in range(1, 11):
    block_lcm = 1
    for index in range(1, block+1):
        block_lcm = block_lcm//gcd(block_lcm, index)*index
    for degree in range(33):
        quotient, remainder = divmod(degree, block)
        denominator = factorial(block)**quotient*factorial(remainder)
        for point in range(-10, 11):
            offsets = ([point+i for i in range(block)]*quotient
                       + [point+i for i in range(remainder)])
            coefficients = integer_coefficients(offsets)
            for order, coefficient in enumerate(coefficients):
                assert (block_lcm**order*coefficient) % denominator == 0, (
                    block, degree, point, order)
                denominator_checks += 1
                zero_coefficients += coefficient == 0

x, y = sp.symbols("x y")
indices = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
monomials = [1, x, y-1, x*x, x*(y-1), (y-1)**2]


def derivative(value, index):
    value = sp.sympify(value)
    for _ in range(index[0]):
        value = sp.diff(value, x)
    for _ in range(index[1]):
        value = y*sp.diff(value, y)
    return sp.expand(value).subs({x: 0, y: 1})


matrix = sp.Matrix([[derivative(value, index) for value in monomials]
                    for index in indices])
assert matrix.det() == 4
normalized = sp.diag(*[sp.Rational(1, factorial(a)*factorial(b))
                      for a, b in indices])*matrix
assert normalized.det() == 1
assert matrix == sp.Matrix([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 2],
])
# Every degree-three generator of J**3 has all jets through degree two zero.
for a in range(4):
    value = x**a*(y-1)**(3-a)
    assert all(derivative(value, index) == 0 for index in indices)
assert sp.expand((1+(y-1))*(1-(y-1)+(y-1)**2)-1-(y-1)**3) == 0

RESULT = {
    "status": "all exact normalization and divisibility checks passed",
    "polynomial_denominator_checks": denominator_checks,
    "zero_coefficients_included": zero_coefficients,
    "parameter_ranges": {
        "block": [1, 10], "degree": [0, 32], "integer_point": [-10, 10],
        "derivative_order": "0 through degree",
    },
    "jet_indices": indices,
    "jet_matrix": matrix.tolist(),
    "ordinary_jet_determinant": 4,
    "factorial_normalized_jet_determinant": 1,
    "dimension_of_point_jet_quotient": 6,
    "arithmetic": "integer convolution and exact symbolic derivatives",
    "limits": "finite normalization checks; the universal arguments are supplied separately",
}
if __name__ == "__main__":
    print(json.dumps(RESULT, indent=2, default=int))

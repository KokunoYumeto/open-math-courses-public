"""Exact numerical check for the degree-cubed height lower bound.

Original certificate: GPT-6.1 Sol (OpenAI), in Codex, Ultra; October 2026.
CC0. This checks the numerical inequalities in Theorem 8.3 of the
many-logarithm lesson, where the complete height-gap proof is supplied.
"""
from laurent_constant import Interval, E
from fractions import Fraction as F
import json

minimum = 44*(1+1/(16*E)).log()
assert minimum.lo > 1
assert Interval(2).log().lo > F(1,11)
print(json.dumps({"status":"exact rational interval checks passed",
    "degree_two_minimum_rational_interval":[str(minimum.lo),str(minimum.hi)],
    "degree_two_minimum_decimal_approximation":float((minimum.lo+minimum.hi)/2),
    "uniform_argument":"z log(1+1/(4e z)) increases for z >= 4"},indent=2))

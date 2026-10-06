"""Exact margins for the many-logarithm lesson's conversions and applications.

Original certificate: GPT-6.1 Sol (OpenAI), in Codex, Ultra; October 2026.
CC0. Uses the independently written outward rational interval arithmetic
in laurent_constant.py; no floating-point comparisons certify any bound.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval, E, PI, LN2

ln3 = Interval(3).log()
ln5 = Interval(5).log()
conversion = PI * E**2 / 8
assert conversion.hi < F(2902, 1000)
assert (8 * (3 - conversion) - LN2).lo > 0
assert (E / 2).hi < F(136, 100)

powers_constant = 30**5 * 32 * Interval(2).sqrt() * LN2 * ln3
assert powers_constant.hi < 840_000_000
endpoint = 40_000_000_000
search_margin = (endpoint * LN2 - Interval(20).log()
                 - 840_000_000 * (1 + Interval(endpoint).log()))
assert search_margin.lo > 0
derivative_margin = LN2 - F(840_000_000, endpoint)
assert derivative_margin.lo > 0
n_endpoint = (endpoint + 1) * LN2 / ln3
assert n_endpoint.hi < 30_000_000_000

offset = 1 - LN2.log()
all_terms_margin = 3 * (1 + LN2).log() - offset
printed_range_margin = 5 * (2 * LN2).log() - offset
assert all_terms_margin.lo > 0
assert printed_range_margin.lo > 0

three_prime_constant = 2 * 30**6 * 81 * Interval(3).sqrt() * LN2 * ln3 * ln5
assert three_prime_constant.hi < 250_700_000_000
radius_ratio = Interval(F(4, 3)).log() / ln3
assert radius_ratio.hi < F(263, 1000)
factorial_zero = (2 * PI).sqrt() / E
factorial_one = F(3, 2) * (3 * PI).sqrt() / Interval(F(3, 2)).exp()
factorial_large_log_margin = (Interval(F(11, 10)).log()
                             - (F(5, 2) * Interval(F(5, 4)).log() - F(1, 2)))
assert factorial_zero.hi < F(11, 10)
assert factorial_one.hi < F(11, 10)
assert factorial_large_log_margin.lo > 0

def record(interval):
    return {
        "rational_interval": [str(interval.lo), str(interval.hi)],
        "decimal_approximation": float((interval.lo + interval.hi) / 2),
    }

RESULT = {
    "status": "all rational interval comparisons passed",
    "complex_conversion_coefficient": record(conversion),
    "powers_of_two_and_three_coefficient": record(powers_constant),
    "search_endpoint_positive_margin": record(search_margin),
    "search_derivative_positive_margin": record(derivative_margin),
    "resulting_n_endpoint": record(n_endpoint),
    "uniform_S_unit_logarithmic_margin": record(all_terms_margin),
    "S_unit_printed_range_margin": record(printed_range_margin),
    "three_prime_exercise_coefficient": record(three_prime_constant),
    "close_to_one_radius_height_ratio": record(radius_ratio),
    "factorial_index_zero_maximum": record(factorial_zero),
    "factorial_index_one_maximum": record(factorial_one),
    "factorial_large_index_logarithmic_margin": record(factorial_large_log_margin),
}

if __name__ == "__main__":
    print(json.dumps(RESULT, indent=2))

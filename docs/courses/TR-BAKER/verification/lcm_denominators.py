"""Exact finite prefix and analytic tail for lcm(1,...,n)<3**n.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
Mathematical source: Hanson (1972), for the Sylvester-factorial mechanism;
the course gives a separate entropy bound, infinite tail and exact prefix.
"""
from fractions import Fraction as F
from math import gcd
import json
from laurent_constant import Interval, LN2

sequence = [2]
for _ in range(5):
    sequence.append(sequence[-1]*(sequence[-1]-1)+1)
assert sequence == [2, 3, 7, 43, 1807, 3263443]
entropy = sum((Interval(a).log()/a for a in sequence[:5]), Interval(0))
tail_first = Interval(sequence[5]).log()/sequence[5]
tail_ratio = F(2, sequence[5]-1)
entropy_upper = entropy+tail_first/(1-tail_ratio)
assert entropy_upper.hi < F(108241, 100000)

threshold = 10000
log_threshold = Interval(threshold).log()
assert log_threshold.lo > 9
tail_error = (log_threshold**2/LN2
              +(2+1/LN2)*log_threshold+1)/threshold
infinite_upper = entropy_upper+tail_error-Interval(3).log()
assert infinite_upper.hi < 0
# Every term t**j*exp(-t), j=0,1,2, decreases for t>=9.

lcm = 1
power3 = 1
for index in range(1, threshold):
    lcm = lcm//gcd(lcm, index)*index
    power3 *= 3
    assert lcm < power3, index

RESULT = {
    'status': 'exact finite prefix and analytic infinite tail passed',
    'finite_range': [1, threshold-1],
    'finite_checks': threshold-1,
    'infinite_range': f'n >= {threshold}',
    'sylvester_sequence': sequence,
    'entropy_upper_bound': str(entropy_upper.hi),
    'entropy_upper_bound_approximation': float(entropy_upper.hi),
    'infinite_logarithmic_margin_upper_bound': str(infinite_upper.hi),
    'infinite_logarithmic_margin_upper_bound_approximation': float(infinite_upper.hi),
    'final_finite_lcm_bit_length': lcm.bit_length(),
    'arithmetic': 'integer lcm and powers; 128-bit outward rational intervals',
    'use': 'complete prefix with a separately proved infinite bound',
}
if __name__ == '__main__':
    print(json.dumps(RESULT, indent=2))

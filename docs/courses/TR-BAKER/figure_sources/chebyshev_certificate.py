"""Exact finite certificate for the elementary Chebyshev recurrence.

Independently authored mathematical implementation: OpenAI Codex,
GPT-6.1 Sol, Ultra effort. CC0. Human method: N. Costa Pereira,
Acta Arithmetica 52 (1989), 307-337, especially 321-323.
Only Python's standard library is used. No prime or logarithm table is read.
Run this file directly to print the certificate as JSON.
"""

from array import array
from fractions import Fraction
from math import factorial
import json

Q = 10**12
J = 16
N = 10**6
WEIGHTS = {1: 1, 2: -1, 3: -1, 5: -1, 6: 1, 7: -1,
           10: 1, 11: -1, 13: -1, 14: 1, 15: 1,
           30: -1, 42: -1, 110: -1, 182: 1}
FIRST_BELOW = {0: 877, 1: 66}  # lower bounds, not both asserted first hits
FIRST_ABOVE = {2: 17, 3: 19, 4: 439}
UPPER_INTERVALS = {
    1: [(67, 126), (157, 176), (179, 220), (223, 275),
        (277, 330), (359, 429)],
    2: [(17, 22), (23, 26), (29, 35), (47, 52),
        (59, 65), (71, 78), (79, 88), (191, 210)],
    3: [(19, 21)],
}
LOWER_INTERVALS = {
    2: [(26, 29), (65, 71), (117, 139)],
    3: [(21, 31), (33, 61), (63, 73), (84, 103),
        (110, 193), (208, 229), (242, 271), (294, 323),
        (325, 373), (440, 493)],
    4: [(440, 877)],
}


def floor_weight(n):
    return sum(v * (n // r) for r, v in WEIGHTS.items())


def atanh_interval(a, b):
    """Return integer endpoints for Q log((b+a)/(b-a)).

    Requires 0 <= a/b <= 1/3. Each of the J positive terms is
    rounded down. The omitted tail times Q is less than one,
    since 9Q < 4(2J+1)3**(2J+1). Thus adding J+1 is safe.
    """
    assert 0 <= 3 * a <= b and b > 0
    if a == 0:
        return 0, 0
    assert 9 * Q < 4 * (2 * J + 1) * 3**(2 * J + 1)
    total = 0
    a_power, b_power = a, b
    for j in range(J):
        total += (2 * Q * a_power) // ((2 * j + 1) * b_power)
        a_power *= a * a
        b_power *= b * b
    return total, total + J + 1


LOG2_LO, LOG2_HI = atanh_interval(1, 3)


def log_interval(n):
    assert isinstance(n, int) and n >= 1
    a = n.bit_length() - 1
    two_power = 1 << a
    lo, hi = atanh_interval(n - two_power, n + two_power)
    return a * LOG2_LO + lo, a * LOG2_HI + hi


def recurrence_certificate():
    assert sum((Fraction(v, r) for r, v in WEIGHTS.items()), Fraction()) == 0
    assert sum(abs(v) for v in WEIGHTS.values()) == 15
    assert sum(WEIGHTS.values()) == -3
    assert [n + n // 15 - n // 2 - n // 3 - n // 5 - n // 30
            for n in range(30)] == [0, 1, 1, 1, 1, 1, 0, 1, 1, 1,
                0, 1, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2]
    for s, a in FIRST_BELOW.items():
        assert all(floor_weight(n) >= s for n in range(1, a))
    for s, a in FIRST_ABOVE.items():
        assert all(floor_weight(n) < s for n in range(1, a))
    for s, pairs in UPPER_INTERVALS.items():
        threshold = FIRST_BELOW.get(s, FIRST_ABOVE.get(s))
        for b, c in pairs:
            assert threshold <= b < c
            assert all(floor_weight(n) >= s for n in range(b, c))
        assert all(pairs[i][1] <= pairs[i + 1][0]
                   for i in range(len(pairs) - 1))
    for s, pairs in LOWER_INTERVALS.items():
        for b, c in pairs:
            assert FIRST_ABOVE[s] <= b < c
            assert all(floor_weight(n) < s for n in range(b, c))
        assert all(pairs[i][1] <= pairs[i + 1][0]
                   for i in range(len(pairs) - 1))
    inv = lambda n: Fraction(1, n)
    upper = [p for pairs in UPPER_INTERVALS.values() for p in pairs]
    lower = [p for pairs in LOWER_INTERVALS.values() for p in pairs]
    A = 1 - sum(map(inv, FIRST_BELOW.values())) - sum(inv(c) for b, c in upper)
    B = sum(inv(b) for b, c in upper)
    C = sum(map(inv, FIRST_ABOVE.values())) + sum(inv(c) for b, c in lower)
    D = 1 - sum(inv(b) for b, c in lower)
    assert A >= Fraction(732878, 10**6)
    assert B >= Fraction(297381, 10**6)
    assert C <= Fraction(263738, 10**6)
    assert D <= Fraction(802853, 10**6)
    omega_lo, omega_hi = Fraction(), Fraction()
    for r, v in WEIGHTS.items():
        lo, hi = log_interval(r)
        coefficient = Fraction(-v, r * Q)
        omega_lo += coefficient * (lo if coefficient >= 0 else hi)
        omega_hi += coefficient * (hi if coefficient >= 0 else lo)
    assert Fraction(1046524, 10**6) < omega_lo <= omega_hi < Fraction(1046525, 10**6)
    assert sum((Fraction(7, 3)**i / factorial(i) for i in range(7)), Fraction()) > 10
    epsilon = Fraction(9, 40000)
    U, L = Fraction(27, 26), Fraction(25, 26)
    coarse_upper_margin = (Fraction(732878, 10**6) * U
                           + Fraction(297381, 10**6) * L
                           - Fraction(1046525, 10**6) - epsilon)
    coarse_lower_margin = (Fraction(1046524, 10**6) - epsilon
                           - Fraction(263738, 10**6) * U
                           - Fraction(802853, 10**6) * L)
    assert coarse_upper_margin > 0 and coarse_lower_margin > 0
    assert A * U + B * L > omega_hi + epsilon
    assert C * U + D * L < omega_lo - epsilon
    return {
        "integer_floor_checks": "all specified initial ranges and every interval checked",
        "weight_sum": -3,
        "inverse_weight_sum": "0",
        "absolute_weight_sum": 15,
        "A": str(A), "B": str(B), "C": str(C), "D": str(D),
        "omega_enclosure": [str(omega_lo), str(omega_hi)],
        "coarse_upper_induction_margin": str(coarse_upper_margin),
        "coarse_lower_induction_margin": str(coarse_lower_margin),
        "error_for_x_at_least_N": str(epsilon),
    }


def prime_power_intervals(limit=N):
    """Exact Eratosthenes sieve and enclosures for each Lambda(n)."""
    assert limit >= 114
    composite = bytearray(limit + 1)
    lo, hi = array("q", [0]) * (limit + 1), array("q", [0]) * (limit + 1)
    prime_count = power_count = 0
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        prime_count += 1
        if p * p <= limit:
            for n in range(p * p, limit + 1, p):
                composite[n] = 1
        lower, upper = log_interval(p)
        power = p
        while power <= limit:
            assert lo[power] == 0 and hi[power] == 0
            lo[power], hi[power] = lower, upper
            power_count += 1
            power *= p
    return lo, hi, prime_count, power_count


def finite_certificate():
    lo, hi, primes, powers = prime_power_intervals()
    psi_lo = psi_hi = 0
    small = []
    min_upper_margin = min_lower_margin = None
    min_upper_at = min_lower_at = None
    for n in range(1, N):
        psi_lo += lo[n]
        psi_hi += hi[n]
        if n <= 113:
            small.append((n, psi_lo, psi_hi))
        if n >= 114:
            margin = 27 * Q * n - 26 * psi_hi
            assert margin > 0, ("upper", n, margin)
            if min_upper_margin is None or margin < min_upper_margin:
                min_upper_margin, min_upper_at = margin, n
        if n >= 227:
            margin = 26 * psi_lo - 25 * Q * (n + 1)
            assert margin > 0, ("lower", n, margin)
            if min_lower_margin is None or margin < min_lower_margin:
                min_lower_margin, min_lower_at = margin, n
    reference_lo, reference_hi = small[-1][1:]
    small_margin = min(107 * Q * n - 103 * h for n, l, h in small)
    assert small_margin > 0
    extremum_margin = min(n * reference_lo - 113 * h for n, l, h in small[:-1])
    assert extremum_margin > 0
    assert 26 * reference_lo > 27 * Q * 113
    assert psi_hi < 2**63
    return {
        "sieve_limit": N,
        "prime_count_at_N": primes,
        "prime_power_count_at_N": powers,
        "upper_checked_integer_range": [114, N - 1],
        "lower_checked_integer_range": [227, N - 1],
        "upper_min_integer_margin": min_upper_margin,
        "upper_min_margin_at": min_upper_at,
        "lower_min_integer_margin": min_lower_margin,
        "lower_min_margin_at": min_lower_at,
        "small_range_107_over_103_min_integer_margin": small_margin,
        "small_range_extremum_113_min_integer_margin": extremum_margin,
        "psi_113_scaled_interval": [reference_lo, reference_hi],
        "integer_storage_no_overflow": True,
    }


def certificate():
    return {"method": "elementary finite induction; no zeta zeros or imported tables",
            "fixed_point_denominator": Q, "positive_log_terms": J,
            "recurrence": recurrence_certificate(), "finite": finite_certificate()}


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))

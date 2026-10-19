"""Exact rational certificate for |2**m-3**n| <= 20, n >= 4.

The proof of the finite reduction is in the accompanying Lesson 11. No floating
point calculation supplies an inequality used by that proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def log_interval(x, terms=100):
    """Integrate the geometric series for 2/(1-z*z), with its tail bound."""
    x = F(x)
    assert x > 1
    z = (x - 1) / (x + 1)
    lower = 2 * sum((z ** (2 * j + 1) / (2 * j + 1) for j in range(terms)), F(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def exp_partial(x, terms):
    term = F(1)
    result = term
    for k in range(1, terms + 1):
        term *= F(x, k)
        result += term
    return result


def lower_abs(lo, hi):
    assert lo * hi > 0, "Uncertified sign"
    return min(abs(lo), abs(hi))


def main():
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    assert l2 > F(69, 100) and u2 < F(7, 10)
    assert l3 > 1 and u3 < F(11, 10)
    assert exp_partial(17, 60) > 20_000_000
    assert exp_partial(4, 10) > 30
    endpoint_margin = F(10_000_000 * 69, 100) - 21600 * F(11, 10) * 17**2 - 4
    derivative_margin = F(69, 100) - F(43200 * 11 * 17, 10 * 10_000_000)
    assert endpoint_margin > 0 and derivative_margin > 0
    assert F(69, 100) * (3**6 - 20) > 40 * 6

    # Both endpoints must force the same partial quotient. Stop only after
    # a convergent exceeds the proved bound on the reduced numerator.
    lo, hi = l3 / u2, u3 / l2
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    convergents = []
    for index in range(100):
        a = lo.numerator // lo.denominator
        assert a == hi.numerator // hi.denominator
        p, q = a * pm1 + pm2, a * qm1 + qm2
        error_lo = p * l2 - q * u3
        error_hi = p * u2 - q * l3
        error = lower_abs(error_lo, error_hi)
        convergents.append({
            "index": index, "partial_quotient": a, "p": p, "q": q,
            "sign_of_p_log2_minus_q_log3": 1 if error_lo > 0 else -1,
            "error_lower_exact": str(error),
            "error_times_100000000_lower_integer": (error * 100000000).__floor__(),
        })
        if p >= 10_000_000:
            break
        assert lo > a
        lo, hi = 1 / (hi - a), 1 / (lo - a)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    else:
        raise AssertionError("No stopping convergent")
    relevant = convergents[:-1]
    minimum_error = min(F(r["error_lower_exact"]) for r in relevant)
    # A deliberately short common lower bound can be printed in the lesson.
    denominator = 1
    while F(1, denominator) >= minimum_error:
        denominator *= 10
    error_bound = F(1, denominator)
    maximum_n = 5
    while 3 ** (maximum_n + 1) <= 20 * denominator + 20:
        maximum_n += 1
    assert 3 ** (maximum_n + 1) > 20 * denominator + 20

    # Enumerate the remaining n by nearest consecutive powers, not a
    # large unproved search window for m.
    final_rows = []
    solutions = []
    for n in range(4, maximum_n + 1):
        power = 3**n
        k = power.bit_length() - 1
        assert 2**k < power < 2**(k+1)
        left, right = power - 2**k, 2**(k+1) - power
        final_rows.append({"n": n, "lower_exponent": k,
                           "distance_below": left, "distance_above": right})
        for m in (k, k+1):
            if abs(2**m-power) <= 20:
                solutions.append([m, n])
    assert solutions == [[6, 4], [8, 5]]

    lesson7 = Path(__file__).resolve().parents[1] / "src/TR-BAKER-07.md"
    result = {
        "state": "passed_exact_rational_certificate",
        "scope": "Complete finite certificate after the proved analytic/Legendre reductions; n>=4, m positive.",
        "programme_input": "Theorem 7.1, equation (7.1), in the preceding lesson Two logarithms II: explicit lower bounds.",
        "programme_input_sha256": hashlib.sha256(lesson7.read_bytes()).hexdigest(),
        "logarithm_series_terms": 100,
        "m_strict_upper_bound": 10_000_000,
        "endpoint_margin_lower": str(endpoint_margin),
        "derivative_margin_lower": str(derivative_margin),
        "convergents_including_first_excluded": convergents,
        "uniform_error_lower_bound": str(error_bound),
        "n_upper_bound": maximum_n,
        "final_integer_rows": final_rows,
        "solutions": solutions,
        "gcd_handling": "For m=g*p,n=g*q, g>=1 multiplies the convergent error; it cannot make it smaller.",
    }
    target = Path(__file__).with_name("powers-2-3-check.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("state", "m_strict_upper_bound", "uniform_error_lower_bound", "n_upper_bound", "solutions")}))
    print(json.dumps([{k:r[k] for k in ("index", "partial_quotient", "p", "q", "sign_of_p_log2_minus_q_log3")} for r in convergents]))
    print(json.dumps(final_rows))


if __name__ == "__main__":
    main()

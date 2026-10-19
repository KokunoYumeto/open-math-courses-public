"""Exact certificates for |2**m-p**n|<=20, p in {3,5}, m,n positive.

The finite reductions are proved in Lesson 21. Only integer and rational
arithmetic is used here. Running this file writes equation-certificates.json.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def log_interval(x, terms=100):
    x = F(x)
    assert x > 1
    z = (x-1)/(x+1)
    total = F(0)
    power = z
    for k in range(terms):
        total += 2*power/(2*k+1)
        power *= z*z
    return total, total+2*power/((2*terms+1)*(1-z*z))


def exp_partial(x, terms):
    term = F(1)
    total = term
    for k in range(1, terms+1):
        term *= F(x, k)
        total += term
    return total


def convergents(prime, numerator_limit, intervals):
    l2, u2 = intervals[2]
    lp, up = intervals[prime]
    lo, hi = lp/u2, up/l2
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    rows = []
    for index in range(100):
        a = lo.__floor__()
        assert a == hi.__floor__()
        p, q = a*pm1+pm2, a*qm1+qm2
        assert abs(p*qm1-pm1*q) == 1
        el, eu = p*l2-q*up, p*u2-q*lp
        assert el*eu > 0
        error = min(abs(el), abs(eu))
        rows.append({'index': index, 'a': a, 'p': p, 'q': q,
                     'sign': 1 if el > 0 else -1,
                     'error_lower_exact': str(error),
                     'error_upper_exact': str(max(abs(el), abs(eu))),
                     'L_scaled_by_100000000': (10**8*error).__floor__()})
        if p >= numerator_limit:
            assert rows[-2]['p'] < numerator_limit
            break
        assert lo > a
        lo, hi = 1/(hi-a), 1/(lo-a)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    else:
        raise AssertionError('Missing first excluded convergent')
    assert all(r['p'] < s['p'] for r, s in zip(rows, rows[1:]))
    return rows


def case(prime, intervals):
    l2, u2 = intervals[2]
    lp, up = intervals[prime]
    assert F(69, 100) < l2 < u2 < F(7, 10)
    if prime == 3:
        numerator_limit, log_upper, log_at_limit = 10**7, F(11, 10), 17
        analytic_n, legendre_n, form_constant = 4, 6, 30
    else:
        numerator_limit, log_upper, log_at_limit = 2*10**7, F(17, 10), 18
        analytic_n, legendre_n, form_constant = 3, 4, 24
    assert 1 < lp < up < log_upper
    assert exp_partial(log_at_limit, 80) > 2*numerator_limit
    assert exp_partial(4, 12) > form_constant
    assert 2*numerator_limit > 2**20 and 20*l2 > 10
    endpoint = numerator_limit*F(69, 100)-21600*log_upper*log_at_limit**2-4
    derivative = F(69, 100)-F(43200)*log_upper*log_at_limit/numerator_limit
    assert endpoint > 0 and derivative > 0
    assert 40*legendre_n < F(69, 100)*(prime**legendre_n-20)

    cf = convergents(prime, numerator_limit, intervals)
    minimum = min(F(r['error_lower_exact']) for r in cf[:-1])
    denominator = 1
    while F(1, denominator) >= minimum:
        denominator *= 10
    n_bound = legendre_n-1
    while prime**(n_bound+1) < 20*denominator+20:
        n_bound += 1
    assert prime**(n_bound+1) >= 20*denominator+20

    # Small n may admit more than the two nearest powers: enumerate them all.
    small_rows, solutions = [], []
    for n in range(1, legendre_n):
        power = prime**n
        mmax = (power+20).bit_length()-1
        rows = []
        for m in range(1, mmax+1):
            difference = 2**m-power
            rows.append({'m': m, 'difference': difference})
            if abs(difference) <= 20:
                solutions.append([m, n, difference])
        assert 2**(mmax+1) > power+20
        small_rows.append({'n': n, 'all_m_checked': [1, mmax], 'rows': rows})

    # For n>=legendre_n the nearest two powers suffice: all others are >20 away.
    final_rows = []
    for n in range(legendre_n, n_bound+1):
        power = prime**n
        k = power.bit_length()-1
        assert 2**k < power < 2**(k+1)
        left, right = power-2**k, 2**(k+1)-power
        # A farther power below is separated by at least 2**(k-1)>20,
        # and a farther power above by at least 2**(k+1)>20.
        assert 2**(k-1) > 20
        final_rows.append({'n': n, 'k': k, 'distance_below': left, 'distance_above': right})
        for m in (k, k+1):
            delta = 2**m-power
            if abs(delta) <= 20:
                solutions.append([m, n, delta])

    expected = ([[1,1,-1],[2,1,1],[3,1,5],[4,1,13],
                 [1,2,-7],[2,2,-5],[3,2,-1],[4,2,7],
                 [3,3,-19],[4,3,-11],[5,3,5],[6,4,-17],[8,5,13]]
                if prime == 3 else
                [[1,1,-3],[2,1,-1],[3,1,3],[4,1,11],
                 [3,2,-17],[4,2,-9],[5,2,7],[7,3,3]])
    assert solutions == expected
    if prime == 3:
        # Reproduce every printed continued-fraction tuple of Lesson 11.
        expected_cf = [(1,1,1,40546510),(1,2,1,28768207),(1,3,2,11778303),
                       (2,8,5,5211600),(2,19,12,1355103),(3,65,41,1146290),
                       (1,84,53,208813),(5,485,306,102223),(2,1054,665,4365),
                       (23,24727,15601,1819),(2,50508,31867,726),
                       (2,125743,79335,366),(1,176251,111202,360),
                       (1,301994,190537,6),(55,16785921,10590737,5)]
        assert [(r['a'],r['p'],r['q'],r['L_scaled_by_100000000']) for r in cf] == expected_cf
        assert n_bound == 19 and denominator == 10**8
    return {'prime': prime, 'programme_input': 'Lesson 7 Theorem 7.1; Lesson 11 Theorem 11.3 and (11.13)',
            'analytic_start_n': analytic_n, 'Legendre_start_n': legendre_n,
            'm_strict_upper_bound': numerator_limit, 'form_upper_constant': form_constant,
            'endpoint_margin_lower': str(endpoint), 'derivative_margin_lower': str(derivative),
            'convergents_including_first_excluded': cf,
            'uniform_error_strict_lower_bound': str(F(1, denominator)),
            'n_upper_bound': n_bound, 'small_n_exhaustive_rows': small_rows,
            'nearest_power_rows': final_rows, 'solutions_m_n_signed_difference': solutions,
            'gcd_handling': 'For m=g*p,n=g*q the logarithmic error is multiplied by g>=1.',
            'bound_proof': 'The positive endpoint and derivative margins exclude m at or above its bound; Legendre plus every relevant convergent error excludes n above the finite search bound.'}


def main():
    intervals = {p: log_interval(p) for p in [2,3,5]}
    result = {'state': 'passed_two_complete_equation_certificates',
              'domain': 'm,n positive integers', 'absolute_difference_limit': 20,
              'arithmetic': 'Exact integers and fractions; 100 atanh-series terms with a geometric remainder.',
              'logarithm_intervals': {str(p): [str(a),str(b)] for p,(a,b) in intervals.items()},
              'cases': [case(p, intervals) for p in [3,5]]}
    Path(__file__).with_name('equation-certificates.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for r in result['cases']:
        print(json.dumps({k:r[k] for k in ['prime','m_strict_upper_bound','endpoint_margin_lower','derivative_margin_lower','uniform_error_strict_lower_bound','n_upper_bound','solutions_m_n_signed_difference']}))
        if r['prime']==5:
            print(json.dumps([{k:x[k] for k in ['a','p','q','sign','L_scaled_by_100000000']} for x in r['convergents_including_first_excluded']]))
            print(json.dumps(r['nearest_power_rows']))


if __name__=='__main__':
    main()

"""Exact finite checks for the prime grouping in the Stewart--Yu argument.

These calculations check examples and reduction identities, not universal
logarithmic-form bounds. Small-prime decisions use rational log enclosures.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from decimal import Decimal, localcontext
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent


def log_unit(x, terms=28):
    assert F(1) <= x <= F(2)
    z = (x-1)/(x+1)
    total = sum((2*z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return total, total+tail


LOG2 = log_unit(F(2))


@lru_cache(None)
def log_integer(n):
    assert n >= 1
    k = n.bit_length()-1
    lo, hi = log_unit(F(n, 2**k))
    return lo+k*LOG2[0], hi+k*LOG2[1]


@lru_cache(None)
def factor(n):
    ans = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            ans[q] = ans.get(q, 0)+1
            n //= q
        q += 1
    if n > 1:
        ans[n] = ans.get(n, 0)+1
    return ans


def val(n, p):
    assert n != 0
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


@lru_cache(None)
def small(q, r):
    qlo, qhi = log_integer(q)
    rlo, rhi = log_integer(r)
    if qhi < rlo*rlo:
        return True
    assert qlo > rhi*rhi, ("Unresolved cutoff comparison", q, r)
    return False


def inspect(a, b, c, counts):
    assert a+b == c and a < b and math.gcd(a, b) == 1
    numbers = [a, b, c]
    fs = [factor(x) for x in numbers]
    support = set().union(*fs)
    r = len(support)
    greatest = [max(f, default=1) for f in fs]
    assert len(set(greatest)) == 3
    G = math.prod(support)
    M = G // math.prod(greatest)
    assert M*math.prod(greatest) == G
    T = max(16, M)
    groups = [
        math.prod(q**k for q, k in f.items() if q != pmax and small(q, r))
        for f, pmax in zip(fs, greatest)
    ]
    counts['triples'] += 1
    counts['a_equals_one'] += a == 1
    counts['archimedean_branch'] += a*a < b
    counts['empty_group_components'] += sum(x == 1 for x in groups)
    counts['nontrivial_group_components'] += sum(x != 1 for x in groups)
    counts['T_equals_16'] += T == 16
    counts['max_r'] = max(counts['max_r'], r)
    for target, i, j in [(0, 2, 1), (1, 2, 0), (2, 0, 1)]:
        numerator = numbers[i]**2 - numbers[j]**2
        assert numerator != 0
        for p, exponent in fs[target].items():
            assert numbers[i] % p and numbers[j] % p
            assert val(numerator, p) >= exponent
            counts['valuation_comparisons'] += 1
            counts['two_adic_comparisons'] += p == 2
        remaining_i = numbers[i] // groups[i]
        remaining_j = numbers[j] // groups[j]
        remaining = set(factor(remaining_i)) | set(factor(remaining_j))
        grouped = F(groups[i], groups[j])
        n = len(remaining) + (grouped != 1)
        assert 1 <= n <= r
        assert not remaining.intersection(set(factor(groups[i])) | set(factor(groups[j])))
        reconstructed = grouped
        for q in remaining:
            exponent = fs[i].get(q, 0)-fs[j].get(q, 0)
            assert exponent != 0
            reconstructed *= F(q)**exponent
            assert q in greatest or not small(q, r)
        assert reconstructed == F(numbers[i], numbers[j])
        # All independent basis vectors have disjoint prime supports except
        # inside the single grouped vector, which is nonzero if retained.
        if grouped != 1:
            assert groups[i] != groups[j]
        if n > 3:
            Llo, Lhi = log_integer(T)
            rlo, rhi = log_integer(r)
            assert (n-3)*rhi*rhi <= Llo
            counts['positive_large_prime_count_checks'] += 1
        counts['grouped_identities'] += 1
        counts['rank_one_groups'] += n == 1
        counts['max_grouped_rank'] = max(counts['max_grouped_rank'], n)
    return {'triple': numbers, 'factorizations': fs, 'G': G, 'M': M, 'T': T,
            'r': r, 'greatest_primes': greatest, 'small_parts': groups}


def main():
    counts = {k: 0 for k in [
        'triples', 'a_equals_one', 'archimedean_branch',
        'empty_group_components', 'nontrivial_group_components',
        'T_equals_16', 'max_r', 'valuation_comparisons',
        'two_adic_comparisons', 'grouped_identities', 'rank_one_groups',
        'max_grouped_rank', 'positive_large_prime_count_checks']}
    for c in range(3, 1001):
        for a in range(1, (c+1)//2):
            b = c-a
            if math.gcd(a, b) == 1:
                inspect(a, b, c, counts)
    example = inspect(121, 48234375, 48234496, counts)
    assert example['factorizations'] == [{11: 2}, {3: 2, 5: 6, 7: 3}, {2: 21, 23: 1}]
    assert example['small_parts'] == [1, 140625, 2097152]
    assert example['G'] == 53130 and example['M'] == 30
    assert (48234496+48234375) % 11 == 4
    assert val(48234496**2-48234375**2, 11) == 2
    with localcontext() as ctx:
        ctx.prec = 80
        u = 100*Decimal(10).ln()
        eta = (u+Decimal(8).ln()).ln().ln()/u.ln()
        comparison = {
            'eta_at_G_10pow100': str(eta),
            'log10_modern_bound_kappa10500': str(100+1050000*eta),
            'log10_SY_radical_factor': str(Decimal(100)/3+3*u.log10()),
            'small_prime_cutoff_r6': str((Decimal(6).ln()**2).exp()),
            'interpretation': 'Numerical evaluations of bounding functions; unknown effective prefactors are retained in the lesson.',
        }
    # Rational sufficient margins in the universal calculus envelopes.
    e_lower = F(8, 3)
    log2_lower = F(2, 3)
    margins = {
        'valuation_monotonicity_factor_16':
            F(16)-54/(e_lower**3*log2_lower**3),
        'archimedean_log_cube_factor_3': F(3)-54/e_lower**3,
        'rank_small_case_factor_2': F(2)-8/e_lower**2,
        'rank_large_case_factor_4': F(4)-12/e_lower**2-6/e_lower,
        'cutoff_factor_6': F(6)-27/e_lower**3-16/e_lower**2-4/e_lower,
    }
    assert all(v > 0 for v in margins.values())
    files = ['logarithmic-inputs.md', 'elementary-bounds.md',
             'prime-part-reduction.md', 'assembly.md', 'examples-and-exercises.md']
    hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in files if (HERE/name).exists()}
    result = {
        'state': 'passed',
        'scope': 'Every coprime ordered triple a<b, a+b=c, 3<=c<=1000; plus the displayed large example.',
        'not_a_universal_proof': 'Universal estimates and all-rank inequalities are proved in the lesson; these are finite identity and arithmetic checks.',
        'counts': counts, 'example': example, 'numerical_comparison': comparison,
        'cutoff_method': '28-term rational positive logarithm series, with rigorous geometric tail and range reduction; all decisions strictly separated.',
        'rational_positive_margins': {k: str(v) for k, v in margins.items()},
        'component_sha256': hashes,
    }
    out = HERE/'prime-part-check.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'state': result['state'], 'counts': counts, 'example': example}))


if __name__ == '__main__':
    main()

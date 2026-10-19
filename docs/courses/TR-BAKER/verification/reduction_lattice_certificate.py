"""Exact three-logarithm component of the Lesson 21 certificate (stdlib only)."""
from fractions import Fraction as F
from pathlib import Path
import json
import math

HERE = Path(__file__).resolve().parent


def log_series(y, terms=240):
    """Positive atanh series and its geometric upper remainder, 1<=y<=2."""
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    power = z
    total = F(0)
    for k in range(terms):
        total += 2*power/(2*k+1)
        power *= z*z
    error = 2*power/((2*terms+1)*(1-z*z))
    return total, total+error


def log_integer(p):
    k = p.bit_length()-1
    lo2, hi2 = log_series(F(2))
    lo, hi = log_series(F(p, 2**k))
    return k*lo2+lo, k*hi2+hi


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def gs(basis):
    n = len(basis)
    stars = []
    norms = []
    mu = [[F(0) for _ in basis] for _ in basis]
    for i, v in enumerate(basis):
        star = list(map(F, v))
        for j in range(i):
            mu[i][j] = F(dot(v, stars[j]), norms[j])
            star = [x-mu[i][j]*y for x, y in zip(star, stars[j])]
        stars.append(star)
        norms.append(dot(star, star))
        assert norms[-1] > 0
    assert all(dot(stars[i], stars[j]) == 0 for i in range(n) for j in range(i))
    return mu, norms


def potential(basis):
    _, norms = gs(basis)
    prefix = F(1)
    result = F(1)
    for value in norms[:-1]:
        prefix *= value
        assert prefix.denominator == 1
        result *= prefix
    assert result.denominator == 1 and result >= 1
    return result.numerator


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def lll(original):
    b = [row[:] for row in original]
    n = len(b)
    u = [[int(i == j) for j in range(n)] for i in range(n)]
    operations = []
    k = 1
    passes = 0
    while k < n:
        passes += 1
        assert passes <= 10000, 'Bounded certificate implementation limit'
        for j in range(k-1, -1, -1):
            mu, _ = gs(b)
            v = mu[k][j]
            q = (2*v.numerator+v.denominator)//(2*v.denominator)
            if q:
                before = potential(b)
                b[k] = [x-q*y for x, y in zip(b[k], b[j])]
                u[k] = [x-q*y for x, y in zip(u[k], u[j])]
                assert potential(b) == before
                operations.append(['reduce', k, j, q])
        mu, norms = gs(b)
        if norms[k] >= (F(3, 4)-mu[k][k-1]**2)*norms[k-1]:
            k += 1
        else:
            before = potential(b)
            b[k], b[k-1] = b[k-1], b[k]
            u[k], u[k-1] = u[k-1], u[k]
            after = potential(b)
            assert 4*after < 3*before
            operations.append(['swap', k-1, k])
            k = max(1, k-1)
    return b, u, operations


def fraction_data(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def main():
    scale = 10**70
    initial_bound = 10**20
    intervals = {p: log_integer(p) for p in (2, 3, 5)}
    floors = []
    for p, (lo, hi) in intervals.items():
        k = (scale*lo).numerator//(scale*lo).denominator
        assert k <= scale*lo < scale*hi < k+1, p
        floors.append(k)
    original = [[1, 0, floors[0]], [0, 1, floors[1]], [0, 0, floors[2]]]
    assert det3(original) == floors[2] != 0
    reduced, change, operations = lll(original)
    assert abs(det3(change)) == 1
    assert [[sum(change[i][k]*original[k][j] for k in range(3))
             for j in range(3)] for i in range(3)] == reduced

    # Replay every integer operation; validate each exact potential comparison.
    replay = [v[:] for v in original]
    for op in operations:
        before = potential(replay)
        if op[0] == 'reduce':
            _, i, j, q = op
            replay[i] = [x-q*y for x, y in zip(replay[i], replay[j])]
            assert potential(replay) == before
        else:
            _, i, j = op
            replay[i], replay[j] = replay[j], replay[i]
            assert 4*potential(replay) < 3*before
    assert replay == reduced
    mu, norms = gs(reduced)
    assert all(abs(mu[i][j]) <= F(1, 2) for i in range(3) for j in range(i))
    lovasz = [norms[i]-(F(3, 4)-mu[i][i-1]**2)*norms[i-1] for i in (1, 2)]
    assert all(x >= 0 for x in lovasz)

    l0_squared = F(dot(reduced[0], reduced[0]), 4)
    radicand = l0_squared-2*initial_bound**2
    assert radicand > 0
    root_lower = math.isqrt(radicand.numerator//radicand.denominator)
    assert root_lower**2 <= radicand < (root_lower+1)**2
    error_lower = root_lower-3*initial_bound
    assert error_lower > 0
    assert error_lower*10**48 > scale
    assert F(8, 3)**120 > 10**48
    result = {
        'state': 'passed_three_logarithm_component',
        'scope': 'Every nonzero integer coefficient vector with |b_j|<=10^20 for log2,log3,log5.',
        'additional_upper_bound_required': '|Lambda|<exp(-X), X=max|b_j|, to infer X<=119.',
        'logarithm_method': '240 terms of positive 2atanh series, exact rational geometric remainder, range reduction by powers of two.',
        'scale': str(scale), 'initial_bound': str(initial_bound),
        'logarithm_intervals': {str(p): {'lo': fraction_data(lo), 'hi': fraction_data(hi)}
                                for p, (lo, hi) in intervals.items()},
        'certified_floors': list(map(str, floors)),
        'basis_vectors_as_rows': original, 'reduced_basis_vectors_as_rows': reduced,
        'change_of_basis_rows': change,
        'orientation': 'reduced[i]=sum(change[i][j]*original[j]); the lattice generators are the displayed row vectors.',
        'change_determinant': det3(change), 'operations': operations,
        'swap_count': sum(op[0] == 'swap' for op in operations),
        'mu': [[fraction_data(x) for x in row] for row in mu],
        'gram_schmidt_norms_squared': [fraction_data(x) for x in norms],
        'lovasz_margins': [fraction_data(x) for x in lovasz],
        'l0_squared': fraction_data(l0_squared), 'sqrt_radicand_integer_lower_bound': str(root_lower),
        'E_integer_lower_bound': str(error_lower), 'linear_form_strict_lower_bound': '10^-48',
        'conditional_reduced_bound': 119,
        'proof_locator': 'Lesson21 Propositions21.2–21.3 and Lemma21.4, with e>8/3.'
    }
    (HERE/'reduction-lattice-check.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'state': result['state'], 'reduced_basis': reduced,
                      'swaps': result['swap_count'], 'operations': len(operations),
                      'E_lower': str(error_lower), 'conditional_reduced_bound': 119}))


if __name__ == '__main__':
    main()

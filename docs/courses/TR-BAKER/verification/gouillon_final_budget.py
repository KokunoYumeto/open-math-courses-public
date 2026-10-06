"""Exact margins for the completed rounded determinant family in Lesson 7.

GPT-6.1 Sol (OpenAI), Codex, Ultra; CC0. Mathematical mechanism credited to
N. Gouillon's freely readable 2003 thesis, Section 5.3. The course supplies
the full adapted proof with log(3) denominators, collisions and conversion.
The finite abstract parameter checks supplement that proof; they do not
certify all published numerical specializations or the separate 78500 bound.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval, LN2, decimal_out

g = F(241, 1000)
gamma = F(1309, 1000)
mu = F(946, 1000)
ln3 = Interval(3).log()

def root(value, n):
    value = F(value)
    scale = 1 << 128
    target = value.numerator * scale**n // value.denominator
    lo, hi = 0, 1 << ((target.bit_length() + n - 1) // n)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**n <= target:
            lo = mid
        else:
            hi = mid
    return Interval(F(lo, scale), F(lo + 1, scale))

def floor_root(value, n):
    value = F(value)
    lo, hi = 0, 1
    while hi**n <= value:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**n <= value:
            lo = mid
        else:
            hi = mid
    assert lo**n <= value < (lo + 1)**n
    return lo

def ceil_interval(v):
    return -((-v.hi.numerator) // v.hi.denominator)

Cstar = root(3, 3) + 1 / root(1350, 3)
M0 = (ln3 / 3 + F(1, 2700)) * root(2 * gamma, 3)**2
M0 /= root(3, 3) * root(g, 3)**2
M0 *= root(F(2701, 2700), 3)
log_cost = mu * (2 + (M0 / mu).log())
assert log_cost.hi < F(216, 100)
Qmin = mu * (1 - Interval(mu).log()) + F(216, 100)
Qmin += mu * Interval(300).log() / 3
assert Qmin.lo > F(49, 10)
assert (mu * Interval(F(49, 10)).log() / F(49, 10)).hi < gamma - 1
psi = (F(1, 3) + gamma / 150) / F(51, 10)
psi += g / root(400, 2) + g / (3 * 400)
psi += 3 * root(g, 3)**2 * root(gamma, 3) * Cstar / (root(2, 3)**2 * root(400, 3))
assert psi.hi < F(249, 1000)
assert F(249, 1000) - gamma / 2700 > F(2485, 10000)
assert (20 * gamma + 1) / mu < 50
assert Interval(100).log().hi < F(100, 8)
assert (Interval(2700 * 1351).log() + 1).hi / (2700 * 1351) < F(1, 100000)
assert F(50001, 100000) * F(2702, 2700) * F(1352, 1351) < F(501, 1000)

cases = 0
degree_radius_pairs = [(1, F(1)), (2, F(1)), (10, F(2)),
                       (10**30, F(10**30)), (10**1000, F(10**1000))]
for D, lam in degree_radius_pairs:
    t = lam / D
    cutoff = Interval(t) + F(216, 100) + mu * Interval(400).log() / 3
    cutoff -= mu * Interval(t).log()
    Q = max(t, F(ceil_interval(cutoff)))
    for p1, p2 in [(1, 1), (1, 100), (100, 1)]:
        a1, a2 = 3 * lam * p1, 3 * lam * p2
        A = a1 * a2
        # An explicit positive coefficient pair; collisions are separately
        # handled symbolically in the lesson, so no injectivity is inferred.
        b1, b2 = 11 * D, 13 * D
        B0 = F(b1, 1) / a2 + F(b2, 1) / a1
        hcut = Interval(B0).log() + Interval(lam).log() + t + F(524, 1000)
        h = max(265 * t, 150 * Q, F(ceil_interval(hcut)))
        c0, c1 = 400, F(51, 10)
        k, ell = c0 * A * D * Q / lam**3, c1 * D * h / lam
        K, L = k.numerator // k.denominator, ell.numerator // ell.denominator
        G = min(F(K + 1, 2), F(L + 1))
        y6 = F((K + 1)**4) * (2 * gamma * D * Q)**2 / (g * g * A)
        r6, s6 = y6 * (a2 / a1)**3, y6 * (a1 / a2)**3
        Rj = [floor_root((K + 1) * a2 / a1, 2), floor_root(r6 / G**2, 6), floor_root(9 * r6, 6)]
        Sj = [floor_root((K + 1) * a1 / a2, 2), floor_root(s6 / G**2, 6), floor_root(9 * s6, 6)]
        z3 = g * g * (L + 1)**3 * A * (K + 1)**2 / (2 * gamma * D * Q)**2
        Tj = [max((L + 1) // (K + 1), K), floor_root(z3 / G, 3), floor_root(3 * z3, 3)]
        R, S, T = sum(Rj), sum(Sj), sum(Tj)
        N = (K + 1) * (K + 2) * (L + 1) // 2
        q = (R + 1) * (S + 1)
        omega = 1 - F(N, 2 * q * (T + 1))
        omega0 = F(2 * q * (T + 1), N)
        U = omega * T + omega0
        J = 1 + K * ln3 / 3
        Z = J * L / (mu * T)
        assert (Interval(t) + mu * (2 + Z.log())).hi < gamma * Q
        assert (mu * T + 20) < (J * L).lo
        omega_cost = Interval(U) * (2 + (J * L / U).log())
        tangent = mu * T * (2 + Z.log()) + 20 * (1 + Z.log())
        assert omega_cost.hi < tangent.lo
        Bdet = F(R * b2 + S * b1, 2 * K)
        budget = Interval(F(N, 2)).log() + F(K, 3) * Interval(Bdet).log()
        budget += F(K, 3) * Interval(F(T, K * L)).log() + F(11 * K, 9) + J + omega_cost
        height = g * F(L + 1, 2) * ((R + 1) * a1 + (S + 1) * a2)
        rhs = D * budget + LN2 + (T + F(K, 3)) * lam + height
        V = F(K + 2, 4) * (L + root(L * L - 1, 2)) * lam
        assert rhs.hi < (V / 2).lo
        conversion = V + Interval(F(L * max(R, S), 2)).log() + 1
        final = F(501, 1000) * c0 * c1 * A * D * D * h * Q / lam**3
        assert conversion.hi < final
        collision_cost = Interval(1) + 2 * D * LN2 + R * a1 + S * a2
        assert collision_cost.hi < final
        cases += 1

result = {'status': 'passed', 'abstract_rounded_cases': cases,
          'degree_radius_edge_cases': ['D=lambda=10^30', 'D=lambda=10^1000'],
          'scalar_intervals': {
              'derivative_constant': [decimal_out(log_cost.lo, 12), decimal_out(log_cost.hi, 12, up=True)],
              'Q_minimum': [decimal_out(Qmin.lo, 12), decimal_out(Qmin.hi, 12, up=True)],
              'normalized_budget_400_5_1': [decimal_out(psi.lo, 12), decimal_out(psi.hi, 12, up=True)]},
          'scope': 'Outward rational scalar checks and complete-budget abstract examples supplement the symbolic full family/collision/conversion proof. Separate exact published constants and78500target are not certified.'}
if __name__ == '__main__':
    print(json.dumps(result, indent=2))

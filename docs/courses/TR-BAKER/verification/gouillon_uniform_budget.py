"""Integer and outward rational checks for the uniform derivative budget.

GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
The general inequalities are proved in the course. These checks exercise
rounding on both sides of H_b=max(L,b-1), including b>T, and supplement
the complete Hanson denominator certificate.
"""
from fractions import Fraction as F
from math import factorial, lcm
import json
from laurent_constant import Interval

c = Interval(3).log()
rounding = derivative_bound = beyond_T = branch_L = branch_b = 0
for K in range(1, 13):
    J = 1 + c*K/3
    for L in (1, 2, 5, 17):
        N = (K+1)*(K+2)*(L+1)//2
        for T in (K, 2*K+1, 9*K):
            for excess in (0, 1, 7):
                q = (N+T)//(T+1) + excess
                assert N <= q*(T+1)
                omega = 1 - F(N, 2*q*(T+1))
                omega0 = F(2*q*(T+1), N)
                U = omega*T + omega0
                quotient = U/J
                low = quotient.lo.numerator//quotient.lo.denominator
                high = quotient.hi.numerator//quotient.hi.denominator
                assert low == high
                b = low+1
                assert F(b) > quotient.hi and F(b-1) < quotient.lo
                H = max(L, b-1)
                maximum = max(Interval(1).lo, (J*L/U).lo)
                assert F(H,b) <= maximum
                assert (J*b).hi <= (U+J).lo
                exact_cost = K*Interval(lcm(*range(1,b+1))).log()/3 + b
                exact_cost += U*(1+Interval(F(H,b)).log())
                logarithm = Interval(0) if (J*L/U).hi <= 1 else (J*L/U).log()
                assert (J*L/U).hi <= 1 or (J*L/U).lo >= 1
                upper_cost = J+2*U+U*logarithm
                assert exact_cost.hi < upper_cost.lo
                rounding += 1
                derivative_bound += 1
                beyond_T += b > T
                branch_L += H == L
                branch_b += H == b-1 and H > L

factorial_checks = 0
for n in range(6, 401):
    assert factorial(n)*2**n <= n**n
    factorial_checks += 1

K,L,q,T,N = 2,2,16,10,18
omega = 1-F(N,2*q*(T+1))
omega0 = F(2*q*(T+1),N)
U = omega*T+omega0
assert (omega,omega0,U) == (F(167,176),F(176,9),F(23003,792))
J = 1+c*K/3
assert (16*J).hi < U < (17*J).lo
assert 17 > T and max(L,17-1) == 16

RESULT = {
    'status': 'all integer and outward rational checks passed',
    'rounded_block_cases': rounding,
    'exact_denominator_cost_comparisons': derivative_bound,
    'cases_with_block_size_above_T': beyond_T,
    'cases_with_H_equal_L': branch_L,
    'cases_with_H_equal_b_minus_one_above_L': branch_b,
    'factorial_cases': factorial_checks,
    'exercise': {'omega':str(omega),'omega0':str(omega0),'U':str(U),'b':17,'H_b':16},
    'arithmetic': 'integers, Fraction and 128-bit outward rational intervals',
    'scope': 'finite checks of rounding and budget; general proof is in (7.57)-(7.58)',
}
if __name__ == '__main__':
    print(json.dumps(RESULT,indent=2))

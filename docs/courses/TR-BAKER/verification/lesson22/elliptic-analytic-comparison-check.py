"""Exact polynomial and rounding checks for the two sampling arguments."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import factorial, floor
from pathlib import Path
import json
import sympy as s
import mpmath as mp

checks = Counter()


def check(value, name):
    assert bool(value), name
    checks[name] += 1


# Rounded node/order counts: rational U includes points just above integers.
for n in range(2, 6):
    for C0 in [2, 3, 7, 24]:
        for offset in [0, 1, C0*C0-1]:
            S = 4*C0*C0-1+offset
            X = Q(S+1, C0*C0)
            S0 = floor(X)
            for U in [Q(2*C0*C0), Q(6*C0*C0+1, 3),
                      Q(20*C0*C0+9, 10)]:
                T = floor(U)
                T0 = floor(U/(C0*C0))
                S1 = 2*n*S+1
                check(S0 >= 2 and S0 >= X/2, 'nonperiodic_node_rounding')
                check(T >= U/2 and S0*T >= X*U/4,
                      'nonperiodic_interpolation_order')
                check(1 <= T0 <= T and T0 >= U/(2*C0*C0),
                      'periodic_order_rounding')
                check(X*U/2 <= S1*T0 <= (2*n+1)*X*U,
                      'periodic_interpolation_order')
                check(Q(144*2*n*(S+1), S0) <= 576*n*C0*C0,
                      'nonperiodic_interpolation_amplification')
                check(Q(144*2*S1, S1) == 288,
                      'periodic_interpolation_amplification')

# The pigeonhole exponent for all tested ranks, independently of the
# number of prescribed rows. Z is the combined row-norm/smallness budget.
for nu in range(8, 129):
    for rho in range(1, nu//8+1):
        theta = Q(rho, nu)
        delta = 4*theta
        check(2*rho*(delta+1) <= nu*delta,
              'rank_sensitive_pigeonhole_exponent')
        check(Q(2*rho, nu-2*rho) <= 4*theta,
              'rank_fraction_inequality')

kg, DL, C0, b, L0, X, c, U = s.symbols(
    'kg DL C0 b L0 X c U', positive=True)
pstar = 4*b*L0*X+4*c
delta = 4*kg*(pstar+2*c)*U/(DL*C0)
check(s.expand(DL*delta/U-(16*kg*b*L0*X+24*kg*c)/C0) == 0,
      'field_degree_cancellation_in_height')

# Independently compare derivatives of the restricted polynomial with
# the exact multi-index formula (22.486).
z, y1, y2, q1, q2 = s.symbols('z y1 y2 q1 q2')
x0, x1, x2 = s.symbols('x0 x1 x2')
F = x0**3*x1**2+x0*x2**4+x1**6+x2**5+1
f1, f2 = (1, 1, 0), (-1, 0, 1)
w = (5, 2, -3)  # 2*f1-3*f2
poly = s.Poly(s.expand(F.subs({x0:5*z+y1-y2,
                               x1:2*z+y1,x2:-3*z+y2})), y1,y2)


def compositions2(m):
    return [(j, m-j) for j in range(m+1)]


for a1 in range(4):
    for a2 in range(4-a1):
        G = poly.coeff_monomial(y1**a1*y2**a2)
        for m in range(4):
            for node in [0, 1, 2]:
                lhs = s.diff(G,z,m).subs(z,node)/factorial(m)
                rhs = 0
                for j,k in compositions2(m):
                    rhs += 2**j*(-3)**k*s.binomial(a1+j,a1)*s.binomial(a2+k,a2)*\
                        poly.coeff_monomial(y1**(a1+j)*y2**(a2+k)).subs(z,node)
                check(s.expand(lhs-rhs) == 0, 'nonperiodic_derivative_identity')
            coefficient_sum = sum(2**j*3**k*s.binomial(a1+j,a1)*s.binomial(a2+k,a2)
                                  for j,k in compositions2(m))
            check(coefficient_sum <= 2**(a1+a2+m)*5**m,
                  'nonperiodic_derivative_coefficient_bound')

# Periodic sampling: f=(f1,w), so differentiation of the line variable
# agrees exactly with its last basis direction, including mixed jets.
periodic = s.Poly(s.expand(F.subs({x0:5*z+y1+5*y2,
                                   x1:2*z+y1+2*y2,
                                   x2:-3*z-3*y2})), y1,y2)
for a in range(5):
    G = periodic.coeff_monomial(y1**a)
    for m in range(6):
        for node in [0, 1, 3]:
            lhs = s.diff(G,z,m).subs(z,node)/factorial(m)
            rhs = periodic.coeff_monomial(y1**a*y2**m).subs(z,node)
            check(s.expand(lhs-rhs) == 0, 'periodic_last_direction_identity')

# Exact inverse-basis entry sums for small nonzero last components.
for a in [Q(-3,2), Q(0), Q(7,3)]:
    for last in [Q(1,7), Q(-1,35), Q(2,13)]:
        M=s.Matrix([[1,s.Rational(a.numerator,a.denominator)],
                    [0,s.Rational(last.numerator,last.denominator)]])
        actual=sum(abs(x) for x in M.inv())
        expected=1+(1+abs(a))/abs(last)
        check(actual==s.Rational(expected.numerator,expected.denominator),
              'periodic_inverse_basis_sum')

# Numerical supplements for transcendental exponential comparisons.
# These are deliberately separated from the exact symbolic checks.
mp.mp.dps=80
numerical=[]
for Qbudget in [16, 32, 64, 100, 1000]:
    Qm=mp.mpf(Qbudget)
    upper=2*mp.exp(-3*Qm/4)+mp.exp(-23*Qm/8)+mp.exp(-4*Qm)
    simplified=mp.exp(-5*Qm/8)
    lower=mp.exp(-Qm/4)
    assert upper<=simplified<lower
    numerical.append({'a0_X_U':Qbudget,'upper_less_than_lower':True,
                      'log_upper_minus_log_lower':str(mp.log(upper)-mp.log(lower))})

choices=[]
for g in range(1,5):
    n=g+1;Kg=factorial(n)*3**g;kg=factorial(n)*2**n*(3*n)**g
    C0=2
    while C0<max(4*Kg,8*kg,2**(2*n)*factorial(n-1)) or \
        mp.mpf(16*kg*(2*n+1))*mp.log(576*n*C0*C0)/C0>mp.log(2)/64:
        C0*=2
    assert mp.mpf(16*kg*(2*n+1))*mp.log(576*n*C0*C0)/C0<=mp.log(2)/64
    choices.append({'g':g,'C0':str(C0),'constant_selection_inequality':True})

result={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed',
        'exact_checks':dict(checks),'exact_total':sum(checks.values()),
        'numerical_exponential_checks':numerical,
        'numerical_C0_choices':choices,'numerical_checks':len(numerical)+len(choices),
        'limits':'Finite examples check the index, basis, rounding and comparison formulas. The complete theorem rests on the written uniform proofs, not these examples. Numerical C0 choices only test inequality22.489 and the stated lower thresholds; they are not numerical elliptic-logarithm constants.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'state':'passed','exact_total':result['exact_total'],
                  'exact_checks':dict(checks),'numerical_checks':result['numerical_checks']}))

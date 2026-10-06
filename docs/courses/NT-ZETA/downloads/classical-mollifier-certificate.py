"""Exact rational certificate for Lesson 17's one-third theorem.

Only the descriptive decimal values use floating point. All inequalities
asserted by the proof are certified by Python's exact Fraction arithmetic.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import mpmath as mp

ROOT = Path(__file__).resolve().parent
theta, R = F(49, 100), F(13, 10)
lam = 2 * R
P = {1: F(25, 28), 3: F(3, 28)}
I0 = sum(a * b / (i + j + 1) for i, a in P.items() for j, b in P.items())
I1 = sum(i * j * a * b / (i + j - 1) for i, a in P.items() for j, b in P.items())
assert I0 == F(629, 2058)
assert I1 == F(989, 980)

E_taylor = sum(lam ** k / factorial(k) for k in range(21))
E_tail_bound = lam ** 21 / factorial(21) / (1 - lam / 22)
E_upper = F(1683, 125)
assert E_taylor + E_tail_bound < E_upper

def c_of_E(E):
    IQ = (2 * E - lam ** 2 - 2 * lam - 2) / lam ** 3
    ID = (E - 1) / (2 * lam) + F(1, 2) - lam / 4
    return F(1, 2) + I1 / theta * IQ + theta * I0 * ID

c_upper = c_of_E(E_upper)
assert c_upper < F(59, 25) < F(237, 100)
target = F(13, 15)
target_taylor = sum(target ** k / factorial(k) for k in range(7))
assert F(237, 100) < target_taylor
assert target / R == F(2, 3)

mp.mp.dps = 60
def dec(x):
    return mp.mpf(x.numerator) / x.denominator
actual_c = c_of_E(mp.exp(dec(lam)))
actual_kappa = 1 - mp.log(actual_c) / dec(R)
numeric_IQ = mp.quad(lambda v: mp.exp(dec(lam)*v)*(1-v)**2, [0,1])
numeric_ID = mp.quad(lambda v: mp.exp(dec(lam)*v)*(-1+dec(R)*(1-v))**2, [0,1])
formula_IQ = (2*mp.exp(dec(lam))-dec(lam)**2-2*dec(lam)-2)/dec(lam)**3
formula_ID = (mp.exp(dec(lam))-1)/(2*dec(lam))+mp.mpf('0.5')-dec(lam)/4
assert abs(numeric_IQ - formula_IQ) < mp.mpf('1e-50')
assert abs(numeric_ID - formula_ID) < mp.mpf('1e-50')

record = {
    'nature': 'Exact rational inequalities; decimal values are consistency checks only.',
    'parameters': {'theta': str(theta), 'R': str(R), 'P': {str(k): str(v) for k,v in P.items()}, 'Q': '1-v'},
    'I0': str(I0), 'I1': str(I1),
    'exp_13_over_5_upper': str(E_upper),
    'positive_margin_above_taylor_plus_tail': str(E_upper-E_taylor-E_tail_bound),
    'c_upper': str(c_upper),
    'positive_margin_below_59_over_25': str(F(59,25)-c_upper),
    'exp_13_over_15_taylor_lower': str(target_taylor),
    'positive_margin_above_237_over_100': str(target_taylor-F(237,100)),
    'certified_simple_critical_line_liminf': '> 1/3',
    'descriptive_c': mp.nstr(actual_c, 40),
    'descriptive_kappa_star_lower_bound': mp.nstr(actual_kappa, 40),
    'quadratic_integral_formula_checks': 'passed at 60 decimal digits',
    'all_assertions_passed': True,
}
(ROOT/'classical_mollifier_certificate.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))

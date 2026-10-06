"""Supplementary exact checks for the absolute real-radius cutoff.

CC0. GPT-6.1 Sol (OpenAI), Codex, Ultra; October2026.
The course supplies the complete proof, including dependence. The free
Laurent2008 determinant proof supplies its independent-base input.
Only standard-library rational intervals and the included certificate
laurent_constant.py are needed.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval as I

v = I(2).log()
assert v.lo > F(3, 20)
assert F(351, 10)*F(10, 3)**2 == 390
margin = 1 - (1 + v)/260
assert margin.lo > F(99, 100)

# X^D-2 is Eisenstein for every D. With coprime r,s, the two
# powers of its positive root generate the same degree-D field.
# Heights are exactly r*log2/D and s*log2/D. E=2 is admissible.
degrees = [1, 2, 3, 4, 10, 100, 10000, 10**30, 10**1000]
powers = [(1, 2), (2, 3), (3, 4), (17, 18)]
coefficients = [(-1, 1), (-3, 2), (-4, 3), (1, 1), (0, 1), (1, 0)]
checks = 0
for D in degrees:
    logD = I(D).log()
    for r, s in powers:
        s1 = I(max(r*v.hi, F(1)))
        s2 = I(max(s*v.hi, F(1)))
        assert (F(3, 2)*s1).lo > v.hi
        assert (F(3, 2)*s2).lo > v.hi
        for c1, c2 in coefficients:
            k = c1*r+c2*s
            if not k:
                continue
            Bprime = abs(c1)/s2+abs(c2)/s1
            w = max(F(3,D), (Bprime.log()/v).hi, F(1))
            T = 390*D**2*s1*s2*w*w/v
            actual = (abs(k)*v).log()-logD
            assert actual.lo > -T.lo
            checks += 1

print(json.dumps({'certificate':'real-radius-absolute-cutoff',
 'exact_coefficient':390,'dependent_cost_margin_lower':str(margin.lo),
 'actual_eisenstein_field_forms_checked':checks,
 'degree_range':'1 through10^1000, finite sample',
 'limitation':'Does not certify the distinct recorded bound omitting cutoff1.'}))

"""Uniform rational certificate for the logarithmic-lattice cardinality bound.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
Each box encloses every real parameter it covers, rather than a sample value.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval, E, PI, LN2

C = F(116, 25)
START, END, STEP = F(127, 50), F(13), F(1, 100)
LN8 = Interval(8).log()

def exponential(value):
    # All calls have |value|<=13; the original Taylor certificate handles <=6.
    return (Interval.of(value)/4).exp()**4

assert (START*exponential(START)/C).hi < 7
worst = F(-1_000_000)
boxes = 0
a = START
while a < END:
    b = min(a+STEP, END)
    t = Interval(a, b)
    epsilon = 1/(t*exponential(t)/C-1)
    g = (t/C).log()/t
    bound = (1+epsilon)*(2+g)-LN8
    assert bound.hi < 0, (str(a), str(b), float(bound.hi))
    worst = max(worst, bound.hi)
    boxes += 1
    a = b

epsilon_tail = 1/(END*exponential(END)/C-1)
tail = (1+epsilon_tail)*(2+1/(C*E))-LN8
assert tail.hi < 0
real_base = F(5, 2)*Interval(F(1, 5)).exp()
complex_base = F(9, 4)*Interval(F(2, 9)).exp()
assert real_base.hi < F(31, 10)
assert complex_base.hi < F(31, 10)

small_height_margins = []
for degree in range(3, 100):
    length = Interval(F(11*degree, 5)).log()
    order_interval = F(4, 5)*degree*length
    order_lo = -((-order_interval.lo.numerator)//order_interval.lo.denominator)
    order_hi = -((-order_interval.hi.numerator)//order_interval.hi.denominator)
    assert order_lo == order_hi
    order = order_lo
    bound = (degree*Interval(order).log()/(order-1)
             + F(4*order, 9*degree)/length
             + (F(8*order, 9*degree)/length).log()
             - F(3, 2) + F(1, 2*order))
    assert bound.hi < 0, (degree, order, float(bound.hi))
    small_height_margins.append((degree, order, bound.hi))

assert E.lo > F(27, 10)
assert E.hi < F(14, 5)
assert F(1) + F(40, 297) + F(1, 2000) < F(143, 100)*F(399, 500)
tail_ratio = F(802, 1125)
height_tail = (F(143, 100)+F(4, 9)*F(401, 500)
               +(tail_ratio-1)-(tail_ratio-1)**2/2
               -F(3, 2)+F(1, 800))
assert height_tail < 0
quadratic_cutoff = F(4, 9)/Interval(F(22, 5)).log()
golden_logarithm = ((1+Interval(5).sqrt())/2).log()
assert quadratic_cutoff.hi < LN2.lo
assert quadratic_cutoff.hi < golden_logarithm.lo
assert quadratic_cutoff.hi < (PI/4).lo
assert LN2.lo > F(2, 3)

def lattice_radius(degree):
    return F(8, 9)/(degree*Interval(degree).sqrt()*Interval(E.lo*degree, E.hi*degree).log())

radius2, radius3 = lattice_radius(2), lattice_radius(3)
assert (2*radius2).hi < golden_logarithm.lo
assert (2*radius2).hi < LN2.lo
assert (2*radius3).hi < Interval(F(6, 5)).log().lo
assert (2*radius2).hi < (PI/4).lo
assert (2*radius3).hi < (PI/9).lo

def cubic(x, a, b):
    return x**3+a*x*x+b*x+1

cubic_checks = []
for a in range(-3, 4):
    for b in range(-3, 4):
        if a+b == -2 or a == b:
            continue  # Rational roots +1 or -1; not an irreducible cubic.
        big, small = F(6, 5), F(5, 6)
        if cubic(big, a, b) <= 0:
            reason = "positive root at least 6/5"
        elif cubic(-big, a, b) >= 0:
            reason = "negative root at most -6/5"
        else:
            assert cubic(small, a, b)*cubic(-small, a, b) <= 0
            reason = "real root in [-5/6,5/6]"
        cubic_checks.append([a, b, reason])
assert len(cubic_checks) == 38

# Positive rational bases: the cases r=1,2,3 and a proved parity recurrence.
prime_logs = [LN2, Interval(3).log(), Interval(5).log()]
gamma = {1: PI.sqrt()/2, 2: Interval(1), 3: 3*PI.sqrt()/4}
product = Interval(1)
covolume_ratio_checks = []
for rank in (1, 2, 3):
    product *= prime_logs[rank-1]
    left = (Interval(2).sqrt()**rank)/product
    right = (F(11, 5)*gamma[rank]*(3/PI).sqrt()**rank*F(9, 8)**rank)
    assert left.hi < right.lo
    covolume_ratio_checks.append([rank, str(left.hi), str(right.lo)])
assert 256*PI.hi < 972
assert prime_logs[2].lo > 1

RESULT = {
    "status": "uniform interval and analytic-tail comparisons passed",
    "boxes": boxes,
    "covered_interval": [str(START), str(END)],
    "box_width": str(STEP),
    "worst_box_upper_bound": str(worst),
    "worst_box_upper_bound_approximation": float(worst),
    "analytic_tail_upper_bound": str(tail.hi),
    "analytic_tail_upper_bound_approximation": float(tail.hi),
    "real_product_base_upper_bound": str(real_base.hi),
    "complex_product_base_upper_bound": str(complex_base.hi),
    "small_height_finite_degrees": [3, 99],
    "small_height_worst_finite_upper_bound": str(max(x[2] for x in small_height_margins)),
    "small_height_worst_finite_upper_bound_approximation": float(max(x[2] for x in small_height_margins)),
    "small_height_degrees_at_least_100_upper_bound": str(height_tail),
    "small_height_tail_upper_bound_approximation": float(height_tail),
    "small_height_orders": [[d, order] for d, order, _ in small_height_margins],
    "quadratic_edge_comparisons": "all passed",
    "small_lattice_radius_comparisons": "all passed",
    "cubic_unit_cases": cubic_checks,
    "positive_rational_covolume_ratio": covolume_ratio_checks,
    "covolume_ratio_infinite_tail": "gamma recurrence, separately on each parity",
    "arithmetic": "128-bit outward rational intervals with explicit series tails",
}
if __name__ == "__main__":
    print(json.dumps(RESULT, indent=2))

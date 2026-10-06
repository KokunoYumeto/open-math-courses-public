"""Certified comparison for convergents of log(3)/log(2).

Original certificate: GPT-6.1 Sol (OpenAI), in Codex, Ultra; October 2026.
CC0. Uses the independently supplied rational interval arithmetic in
laurent_constant.py. Output fractions are rigorous; decimal displays
are explicitly approximations. No external numerical library is used.
"""
from fractions import Fraction as F
from laurent_constant import Interval
import json

ln2, ln3 = Interval(2).log(), Interval(3).log()
xi = ln3/ln2
partial = xi
p0,p1,q0,q1 = 0,1,1,0
rows = []
for index in range(1,17):
    digit = partial.lo.numerator//partial.lo.denominator
    assert digit == partial.hi.numerator//partial.hi.denominator
    p,q = digit*p1+p0, digit*q1+q0
    form = p*ln2-q*ln3
    assert form.lo*form.hi > 0
    absolute = form if form.lo > 0 else -form
    log_absolute = absolute.log()
    bp = p/ln3+q
    lbp = bp.log()
    general_M = Interval(max(F(10),lbp.lo),max(F(10),lbp.hi))
    sharp_M = Interval(max(F(20),lbp.lo+F(21,100)),
                      max(F(20),lbp.hi+F(21,100)))
    general = -21600*ln3*general_M**2
    sharp = -F(126,5)*ln3*sharp_M**2
    assert log_absolute.lo > general.hi
    assert log_absolute.lo > sharp.hi
    rows.append({
        "index":index,"partial_quotient":digit,"p":p,"q":q,
        "absolute_form_rational_interval":[str(absolute.lo),str(absolute.hi)],
        "absolute_form_decimal_approximation":float((absolute.lo+absolute.hi)/2),
        "log_absolute_form_rational_interval":[str(log_absolute.lo),str(log_absolute.hi)],
        "log_absolute_form_decimal_approximation":float((log_absolute.lo+log_absolute.hi)/2),
        "general_log_lower_bound_decimal_approximation":float((general.lo+general.hi)/2),
        "sharp_log_lower_bound_decimal_approximation":float((sharp.lo+sharp.hi)/2)
    })
    p0,p1,q0,q1 = p1,p,q1,q
    partial = 1/(partial-digit)

RESULT = {"status":"all continued-fraction digits, signs and comparisons certified",
          "arithmetic":"outward rational intervals; 128 fractional bits",
          "decimal_values":"display approximations; rigorous endpoints are the fractions",
          "rows":rows}
if __name__ == "__main__":
    print(json.dumps(RESULT,indent=2))

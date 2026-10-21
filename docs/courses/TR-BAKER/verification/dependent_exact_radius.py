"""Supplementary exact checks for the dependent exact-radius proposition.

CC0. GPT-6 Astra (OpenAI), Codex, Ultra; October 2026.
The lesson proves the universal inequalities; samples only check examples.
"""
from fractions import Fraction as F
import contextlib, io, json, pathlib, sys

HERE=pathlib.Path(__file__).resolve().parent
if not (HERE/'laurent_constant.py').exists():
    sys.path.insert(0,str(HERE/'publication-current/docs/courses/TR-BAKER/verification'))
with contextlib.redirect_stdout(io.StringIO()):
    from laurent_constant import Interval as I


def checks():
    ln2=I(2).log()
    assert ln2.lo>F(2,3)>F(1,2)
    assert ln2.log().lo>-1
    assert 78500*9==706500
    assert F(706500)*F(2,3)**2==314000
    assert 314000-1==313999
    assert (313999*ln2-1).lo>0
    # Exact degree follows from the irreducibility argument in the lesson.
    degrees=[1,2,3,4,8,31,32,100,10000,10**8,10**30,10**100,10**1000]
    rows=[]
    for degree in degrees:
        m=max(3,degree.bit_length())
        assert 2**m>=degree+1
        v=I(degree+1).log()
        S1=m*ln2;S2=(m+1)*ln2
        assert S1.lo>1
        assert (F(3,2)*S1-v).lo>0
        bprime=1/S1+1/S2
        assert bprime.hi<1
        # W0=3/D, so D cancels symbolically before interval evaluation.
        target=706500*S1*S2/v
        exact_cost=I(degree).log()-ln2.log()
        radius_cost=v-ln2.log()
        assert (target-exact_cost).lo>0
        assert (target-radius_cost).lo>0
        rows.append({'degree':str(degree),'primitive_powers':[m,m+1],
                     'radius':str(degree+1),'coefficient_cutoff':'3/D',
                     'bound_margin_positive':True})
    return {'actual_nonunit_field_examples':rows,
            'universal_scalar_checks':6,
            'scope':'Dependent bases with the exact radius: nonunit bases in all degrees, or the stated bound on primitive exponents.'}


if __name__=='__main__':print(json.dumps(checks(),indent=2))

"""Exact bounds for fixed-order successor integer closure. CC0.

The accompanying proof supplies the continuous r1 and infinite-rank bounds.
The finite substitutions below certify their stated rational endpoints only.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import importlib.util, json

HERE = Path(__file__).resolve().parent
BASE = HERE / 'integer_comparison_bounds.py'
INPUT = HERE / 'fixed_order_input_endpoints.py'
if not BASE.exists():
    BASE = HERE.parents[1] / 'publication-current/docs/courses/TR-BAKER/figure_sources/integer_comparison_bounds.py'
if not INPUT.exists():
    INPUT = HERE.parents[1] / 'publication-current/docs/courses/TR-BAKER/figure_sources/fixed_order_input_endpoints.py'
def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
base = module('integer_bounds', BASE)
initial = module('fixed_input', INPUT)
lam = F(189, 188)

def log_lower(value):
    z = (value - 1) / (value + 1)
    assert 0 < z < 1
    return 2 * sum(z**(2*j+1) / (2*j+1) for j in range(5))

def endpoint(row, r, uniform=False):
    name,c0,c1,c3,c4,q,c2,y,omega,c01,cs = base.constants(row)
    c = cs[2] if uniform else cs[0 if r == 2 else 1]
    a = r+1; eta = 1-c/a; H = eta**a; Q = q*H
    ell = F(347,500) if q == 2 else F(1099,1000)
    br = F(7200,29)*14**(r-2)
    sm = base.minimum_S(name,c3,q,r)
    lower = F(initial.endpoint(row,r,uniform)['g4_lower'])
    g9 = F(107,103) if uniform or name in ('I.2','III.2') else max(F(107,103),1+F(1,3*a))
    remainder = c1*(F(1,300)+1/(273*999*br))
    previous = base.arithmetic(row,r,high=uniform)[2]
    old_eta = 1 if uniform else eta
    coefficient = previous-remainder-g9*old_eta/(c3*y)-lam*(1+omega)/c4
    minimum_depth = 0
    while c*lower*H**(minimum_depth+1)/a >= 1:
        minimum_depth += 1
    assert Q**minimum_depth > q
    torus = 1/(c2*Q**minimum_depth)
    common = coefficient+remainder+g9*a/(c*c3*y*lower)+lam/c4*(
        1+omega+3*ell/log_lower(Q)+(1+F(1,q-1))*ell/5)
    cost_zero = common+torus
    mass_zero = 2*c*(q-1)*q*eta-2*q*(q-1)*a/(sm*lower)
    mass_gap = mass_zero-cost_zero
    # For all 0<=r1<=r, Q^I1>q bounds the largest torus term.
    max_cost = common+F(q**(r-1),1)/c2+lam*r*ell/(5*c4)
    input = c1*q**a-1/(c3*y*lower)-4*c/(3*c3*y*a)
    input_gap = input-max_cost
    assert mass_gap > F(3,100) and input_gap > 8
    return {'case':name,'rank':'all_r_ge_8' if uniform else r,
        'initial_multiplicity_lower':str(lower),'minimum_stopping_depth':minimum_depth,
        'Q':str(Q),'Q_to_minimum_depth':str(Q**minimum_depth),
        'coefficient_upper':str(coefficient),'common_arithmetic_upper':str(common),
        'mass_lower_at_r1_zero':str(mass_zero),'arithmetic_upper_at_r1_zero':str(cost_zero),
        'mass_margin':str(mass_gap),'input_margin':str(input_gap),
        'mass_margin_decimal':float(mass_gap),'input_margin_decimal':float(input_gap),
        'uniform_after_rank8':uniform}

def universal_checks():
    odd = (2*F(5267,10000)*4*F(11,20)*F(12,25)-F(347,500)/F(7,4))/2-lam*F(347,500)/(5*18)
    v = (2*F(3,4)*2*9*F(5,12)*F(3,4)-F(1099,1000)/F(13,9))/3-lam*F(1099,1000)/(5*F(15,4))
    assert odd > F(1,3) and v > 2
    assert log_lower(F(122,75))>F(12,25) and log_lower(F(2173,1000))>F(3,4)
    assert all((1-c/F(a))**a > F(11,20) for a,c in [(3,F(538,1000)),(4,F(551,1000)),(9,F(14,25))])
    assert all((1-c/F(a))**a > F(5,12) for a,c in [(3,F(753,1000)),(4,F(78,100)),(9,F(827,1000))])
    assert F(11,20)**8*F(4500,29)>1 and F(11,10)**8>2
    assert F(5,12)**6*F(6750,29)>1 and F(5,4)**6>3
    return {'odd_continuous_r1_derivative_lower':str(odd),'V_continuous_r1_derivative_lower':str(v),
        'coarse_stopping_depths':{'odd':8,'V':6},'state':'passed'}

def certificate():
    rows = [endpoint(row,r,r==8) for row in base.rows for r in range(2,9)]
    table = []
    for row in base.rows:
        subset = [x for x in rows if x['case']==row[0]]
        mg = min(F(x['mass_margin']) for x in subset)
        ig = min(F(x['input_margin']) for x in subset)
        mf = (1000*mg).numerator//(1000*mg).denominator
        inf = (1000*ig).numerator//(1000*ig).denominator
        assert mg>F(mf,1000) and ig>F(inf,1000)
        table.append({'case':row[0],'strict_mass_margin_per_1000':mf,'strict_input_margin_per_1000':inf})
    return {'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_in_written_all_rank_envelope',
        'rows':rows,'table':table,'universal_checks':universal_checks(),
        'minimum_mass_margin':min(x['mass_margin_decimal'] for x in rows),
        'minimum_input_margin':min(x['input_margin_decimal'] for x in rows),
        'scope':'48 finite and8 analytically uniform endpoints for the original-K successor integer closure, with fixed Tflat/R. Actual q-deleted input family is a hypothesis; neither fractional zeros nor existence of stage-I3 is asserted.'}

if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ['state','table','minimum_mass_margin','minimum_input_margin']}))

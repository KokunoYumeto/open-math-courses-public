"""Exact two-radius fixed-order fractional comparisons. CC0.

The written proof supplies the all-rank two-step enclosure and the actual
integer/fractional/phase induction. This program certifies its rational
endpoint substitutions; it is not a finite-rank substitute for that proof.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import factorial
import importlib.util, json, sys
sys.set_int_max_str_digits(200000)
HERE=Path(__file__).resolve().parent

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

SOURCE=HERE/'successor_fixed_order_endpoints.py'
if not SOURCE.exists():
    SOURCE=HERE.parents[1]/'publication-current/docs/courses/TR-BAKER/figure_sources/successor_fixed_order_endpoints.py'
previous=module('successor_bounds',SOURCE)
base=previous.base;xi=F(24,25);lam=F(189,188)

def strict_floor(value,scale=1000000):
    n=(scale*value).numerator//(scale*value).denominator
    assert value>F(n,scale)
    return n

def endpoint(row,r,uniform=False):
    high=r>=8
    old=previous.endpoint(row,r,high)
    name,c0,c1,c3,c4,q,c2,y,omega,c01,cs=base.constants(row)
    c=cs[2] if high else cs[0 if r==2 else 1]
    a=r+1;eta=1-c/a;H=eta**a;Q=q*H
    ell=F(347,500) if q==2 else F(1099,1000)
    L=F(old['initial_multiplicity_lower']);K=F(old['common_arithmetic_upper'])
    depth=old['minimum_stopping_depth'];mu=F(q**r)/Q**depth
    sm=base.minimum_S(name,c3,q,r);Gamma=lam*omega/c4
    factor=max(F(1),xi*c1/(2*c*q*H))
    j=0
    while mu*factor>q**j:j+=1
    cost=K+lam*j*ell/(5*c4)+mu*factor/c2
    first=2*c*q*q*eta-2*q*q*a/(sm*L)-cost
    second=xi*c1*q**r-2*q*a/(sm*L)-(K+lam*(j+1)*ell/(5*c4)+q*mu*factor/c2)
    fractional=xi*c1*q-(K-Gamma+lam*j*ell/(5*c4)+mu/c2)-Gamma/q**r-2*q*a/(sm*L*q**r)
    input_gap=(1-xi)*c1*q**a-1/(c3*y*L)
    assert min(first,second,fractional,input_gap)>0,(name,r)
    return {'case':name,'rank':('all_even_r_ge_32' if r==32 else 'all_odd_r_ge_33') if uniform else r,
            'minimum_stopping_depth':depth,'scalar_j':j,
            'first_strict_margin_per_million':strict_floor(first),
            'second_strict_margin_per_million':strict_floor(second),
            'fractional_strict_margin_per_million':strict_floor(fractional),
            'input_strict_margin_per_million':strict_floor(input_gap),
            'first_margin_decimal':float(first),'second_margin_decimal':float(second),
            'fractional_margin_decimal':float(fractional),
            'q_rank_over_Q_min_depth_decimal':float(mu),'uniform_parity_enclosure':uniform}

def universal_checks():
    r=8
    ratio=(1+F(1,r))**r*(1+F(1,r+1))**(r+1)
    assert ratio>F(13,2)
    checks=[]
    for c,q,astar,d in [(F(14,25),2,F(7),12),(F(11,20),2,F(7,2),11),(F(827,1000),3,F(26,3),9)]:
        H=(1-c/33)**33;Q=q*H
        multiplicity_ratio=astar**2*F(13,2)**2*H**d
        degree_ratio=Q**d/F(q*q)
        assert multiplicity_ratio>1 and degree_ratio>1
        checks.append({'c':str(c),'q':q,'a_star':str(astar),'two_step_depth_increment':d,
                       'multiplicity_ratio_decimal':float(multiplicity_ratio),
                       'Q_depth_over_q_squared_decimal':float(degree_ratio),
                       'exact_integer_cross_products_passed':True})
    # Other odd rows have c<=14/25 and a_star>=7. III rows have
    # c=11/20 and a_star=7/2 in the infinite rank band.
    return {'state':'passed','F_successive_ratio_gt_13_over_2_at_rank8':True,
            'rank32_two_step_checks':checks}

def certificate():
    rows=[endpoint(row,r,r>=32) for row in base.rows for r in range(2,34)]
    table=[]
    for original in base.rows:
        subset=[v for v in rows if v['case']==original[0]]
        table.append({'case':original[0],
                      'first_strict_margin_per_million':min(v['first_strict_margin_per_million'] for v in subset),
                      'second_strict_margin_per_million':min(v['second_strict_margin_per_million'] for v in subset),
                      'fractional_strict_margin_per_million':min(v['fractional_strict_margin_per_million'] for v in subset)})
    return {'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_in_written_all_rank_enclosure',
            'xi':str(xi),'rows':rows,'table':table,'universal_checks':universal_checks(),
            'minimum_first_margin':min(v['first_margin_decimal'] for v in rows),
            'minimum_second_margin':min(v['second_margin_decimal'] for v in rows),
            'minimum_fractional_margin':min(v['fractional_margin_decimal'] for v in rows),
            'maximum_scalar_j':max(v['scalar_j'] for v in rows),
            'scope':'240 finite endpoints and16 infinite parity enclosures; full q^r fractional degree, original selected derivative order, original required radius, and every arithmetic term retained. The written two-step monotonicity, input and two-radius zero arguments are required.'}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ['state','table','minimum_first_margin','minimum_second_margin','minimum_fractional_margin','maximum_scalar_j']}))

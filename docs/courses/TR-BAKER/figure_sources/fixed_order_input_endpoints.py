"""Exact full-node, zero-extra-jet input bounds at the multiplicity stop. CC0.
The written proof establishes the uniform rank enclosure and every field row.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from datetime import datetime, timezone
import importlib.util, json

HERE=Path(__file__).resolve().parent
BASE=HERE/'integer_comparison_bounds.py'
if not BASE.exists(): BASE=HERE.parents[1]/'publication-current/docs/courses/TR-BAKER/figure_sources/integer_comparison_bounds.py'
spec=importlib.util.spec_from_file_location('integer_comparison_bounds',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
# rho, explicit upper depth, a_* and lower g1 factor in the actual g4.
parameters={
 'I.1':(58,F(3,2),F(7),1),'I.2':(17,F(3,2),F(7),5),
 'II':(58,F(5,4),F(7),1),
 'III.1':(58,F(1),F(7,2),5),'III.2':(17,F(1),F(7,2),5),
 'IV.P1':(58,F(7,6),F(7),1),'IV.Plarge':(58,F(7,6),F(7),1),
 'V':(58,F(2),F(26,3),1)
}

def endpoint(row,r,uniform=False):
    name,c0,c1,c3,c4,q,c2,y,gamma,c01,cs=base.constants(row)
    c=cs[2] if uniform else cs[0 if r==2 else 1]
    a=r+1;eta=1-c/a;rho,upper_depth,astar,gfactor=parameters[name]
    fr=F(r**r*a**r,factorial(r)**2)
    g4lower=2*c0*c4*q*a*astar**r*fr*gfactor/(rho*upper_depth)
    sm=base.minimum_S(name,c3,q,r)
    bound=2*c*q*eta**r+F(3*a,q**r*sm*g4lower)+1/(c3*y*g4lower*q**a)
    gap=c1-bound;assert gap>F(1,50000),(name,r,uniform)
    return {'case':name,'rank':'all_r_ge_8' if uniform else r,'g4_lower':str(g4lower),
            'input_upper':str(bound),'input_margin':str(gap),'margin_decimal':float(gap),
            'uniform_after_rank8':uniform}

def certificate():
    rec=[endpoint(row,r,r==8) for row in base.rows for r in range(2,9)]
    table=[]
    for row in base.rows:
        gap=min(F(x['input_margin']) for x in rec if x['case']==row[0]);floor=(10**6*gap).numerator//(10**6*gap).denominator
        assert gap>F(floor,10**6)
        table.append({'case':row[0],'strict_lower_margin_per_million':floor})
    return {'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_in_written_uniform_envelope',
            'rows':rec,'table':table,'minimum_margin':min(x['margin_decimal'] for x in rec),
            'scope':'48 exact finite endpoints and8 analytically uniform endpoints. Actual g4 formula and original explicit depth choices used; all-rank monotonicity proved in the accompanying note. This certifies only the analytic input, not the remaining global fractional arithmetic comparison.'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args();data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ['state','table','minimum_margin']}))

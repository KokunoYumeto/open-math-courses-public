"""Exact endpoint certificate for the original terminal integer seed. CC0.

The accompanying proof establishes why ranks >=8 are enclosed by one row.
This program computes endpoint fractions; finite sampling is not that proof.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import importlib.util
import json

HERE = Path(__file__).resolve().parent
if (HERE/'integer_comparison_bounds.py').exists():
    BASE = HERE/'integer_comparison_bounds.py'
else:
    BASE = HERE.parents[1]/'publication-current/docs/courses/TR-BAKER/figure_sources/integer_comparison_bounds.py'
spec = importlib.util.spec_from_file_location('integer_comparison_bounds', BASE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
lam = F(189,188)

def endpoint(row, r, uniform=False):
    name,c0,c1,c3,c4,q,c2,y,gamma,c01,cs = base.constants(row)
    c = cs[2] if uniform else cs[0 if r==2 else 1]
    a=r+1; eta=1-c/a; H=eta**a
    br=F(7200,29)*14**(r-2)
    sminus=base.minimum_S(name,c3,q,r)
    ellq=F(347,500) if q==2 else F(1099,1000)
    out=base.arithmetic(row,r,high=uniform)[2]
    if uniform:
        # eta^r decreases; both small remainder factors are bounded by1.
        input_upper=F(98,25)*c*eta**r+2*c/(q**r*sminus)+c1/(7*a*br*q**a)+c/(c3*y*a*q**a)
        cost_upper=out/q**a+lam*ellq*(r+F(1,q-1))/(5*c4*q**a)+1/c2
    else:
        input_upper=F(98,25)*c*eta**r+2*c*eta**r/(q**r*sminus)+c1/(7*a*br*q**a)+c*eta**r/(c3*y*a*q**a)
        g9=F(107,103) if name in ('I.2','III.2') else max(F(107,103),1+F(1,3*a))
        cost_upper=(out+g9*(H-eta)/(c3*y)+lam*ellq*(r+F(1,q-1))/(5*c4))/q**a+1/c2
    mass_lower=F(98,25)*c*H*(1-F(1,q**r*sminus))
    input_margin=c1-input_upper; mass_margin=mass_lower-cost_upper
    assert input_margin>F(1,100) and mass_margin>F(2,5),(name,r,uniform)
    return {'case':name,'rank':'all_r_ge_8' if uniform else r,
            'input_upper':str(input_upper),'arithmetic_upper':str(cost_upper),'mass_lower':str(mass_lower),
            'input_margin':str(input_margin),'mass_margin':str(mass_margin),
            'input_decimal':float(input_margin),'mass_decimal':float(mass_margin),
            'uniform_after_rank8':uniform}

def records():
    return [endpoint(row,r,r==8) for row in base.rows for r in range(2,9)]

def analytic_endpoints():
    # Complete universal input bounds for the preceding levels j<=r-1.
    br2=F(7200,29)
    odd=4*F(14,25)/2+2*F(14,25)/(4*58)+F(3)/(7*3*br2*8)+F(14,25)/(F(19,10)*3*8)
    v=4*F(827,1000)/3+2*F(827,1000)/(9*58)+F(3)/(7*3*br2*27)+F(827,1000)/(F(19,20)*3*27)
    assert odd<F(23,20)<F(7,5) and v<F(9,8)<F(5,2)
    # The derivative criterion c<2(1-c/y), y>=3, is uniform.
    assert F(827,1000)<2*(1-F(827,3000))
    assert F(107,103)>1+F(1,27)
    return {'state':'passed','ordinary_odd_input_upper':str(odd),'ordinary_V_input_upper':str(v),
            'trim_fraction':'24/25','terminal_mass_factor':'98/25',
            'monotonicity_endpoint':'c<=827/1000<2(1-c/3); g9=107/103 for all r>=8'}

def certificate():
    rec=records(); table=[]
    for row in base.rows:
        subset=[x for x in rec if x['case']==row[0]]
        im=min(F(x['input_margin']) for x in subset);mm=min(F(x['mass_margin']) for x in subset)
        ilower=(1000*im).numerator//(1000*im).denominator
        mlower=(1000*mm).numerator//(1000*mm).denominator
        assert im>F(ilower,1000) and mm>F(mlower,1000)
        table.append({'case':row[0], 'input_lower_per_1000':ilower,
                      'mass_lower_per_1000':mlower})
    return {'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_in_proved_analytic_envelope',
            'rows':rec,'table':table,'analytic_endpoints':analytic_endpoints(),
            'minimum_input_margin':min(x['input_decimal'] for x in rec),
            'minimum_mass_margin':min(x['mass_decimal'] for x in rec),
            'scope':'48 exact rank2–7 endpoint rows and8 analytically uniform rank>=8 rows. The written monotonicity argument, nested cardinal proof, full input inequality and original-field arithmetic comparison are required; finite rows alone are not an all-rank proof.'}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ['state','table','minimum_input_margin','minimum_mass_margin']}))

"""Exact first-contraction checks for the second-scale selected kernel.

GPT-6 Astra (OpenAI), Ultra; independently authored and self-checked. CC0.
The proof supplies the uniform tail reduction, not a rank sampling claim.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import argparse
from yu_second_fractional_profile import calculate, case_data, exp_bounds


def calculate_contraction():
    fractional = calculate()
    rows = []
    for data, row in zip(case_data(), fractional['cases']):
        name,c1,c3,c4,a,q,zeta,amin,dmin,w,nfactor,chi,pref,target = data
        c = Q(27,50) if q == 2 else Q(4,5)
        lam, xi = Q(59,58), Q(101,100)
        comparisons = []
        for entry in row['comparisons']:
            tail = entry['ranks'] == 'all >= 8'
            r = 8 if tail else entry['ranks']
            fraction = (1-c/Q(r+1))**(r+1)
            fraction_upper = 1/exp_bounds(c)[0] if tail else fraction
            tmin = Q(12,29)*(r+1)*12**r
            arithmetic = Q(entry['arithmetic_upper'])
            normal = lam*nfactor/c4
            mass = 2*c*q*(q-1)-normal
            input_lower = (c1*chi*q**(r+1)
                           -xi*(2*c*fraction_upper/Q(r+1)+2/tmin)
                           /(c3*(1+amin)))
            mass_gap, input_gap = mass-arithmetic, input_lower-arithmetic
            assert mass_gap > Q(3,5) and input_gap > 9
            comparisons.append({'ranks':entry['ranks'],'A0_endpoint':entry['A0_endpoint'],
                                'arithmetic_upper':str(arithmetic),
                                'mass_minus_normalization':str(mass),
                                'input_lower':str(input_lower),
                                'mass_gap':str(mass_gap),'input_gap':str(input_gap)})
        rows.append({'case':name,'comparisons':comparisons,
                     'minimum_mass_gap':str(min(Q(x['mass_gap']) for x in comparisons)),
                     'minimum_input_gap':str(min(Q(x['input_gap']) for x in comparisons))})
    bounds = [(Q(61,100),10),(Q(3,5),9),(Q(37,50),10),
              (Q(63,100),10),(Q(31,50),11),(Q(69,100),13),(Q(71,10),230)]
    for row, (mass_bound, input_bound) in zip(rows,bounds):
        assert Q(row['minimum_mass_gap']) > mass_bound
        assert Q(row['minimum_input_gap']) > input_bound
    assert sum(len(x['comparisons']) for x in rows)==82
    # The exact annulus example from Solution80 is separate from a parameter instance.
    r,q,c,S,T=3,2,Q(27,50),Q(21,2),Q(1200)
    eta=1-c/(r+1); frac=eta**(r+1); S1=S/frac;T1=frac*T
    R=q*(int(S1)+1);M=int(c*T1/(r+1))+1;O=int(eta*T1)
    assert R==38 and M==91 and O==581
    assert O+M-1 <= int(T1)==671
    deleted=[s for s in range(-R,R+1) if s%q]
    assert len(deleted)==38 and len(deleted)*M==3458
    assert frac == Q(895745041,1600000000)
    assert S1 == Q(16800000000,895745041) and T1 == Q(2687235123,4000000)
    return {'state':'all_exact_comparisons_passed','results':[202],
            'scope':'First selected-support contraction, stronger q-deleted block and full integer closure; no all-depth claim.',
            'endpoint_comparisons':82,'strict_mass_gap':'3/5','strict_input_gap':'9',
            'cases':rows,'counting_example':{'R':R,'input_order':int(T1),'multiplicity':M,
            'output_order':O,'deleted_nodes':len(deleted),'mass':len(deleted)*M}}


def render(result, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, (ax, budget) = plt.subplots(1,2,figsize=(12.5,4.2),
                                    gridspec_kw={'width_ratios':[2.2,1]},layout='constrained')
    odd=list(range(-37,38,2)); even=list(range(-38,39,2))
    ax.scatter(odd,[671]*38,s=18,color='#17668b',label='38 retained odd nodes')
    ax.scatter(odd,[581]*38,s=18,color='#17668b')
    ax.scatter(even,[581]*39,s=18,color='#b45428',label='39 added even nodes')
    ax.set(xlim=(-40,40),ylim=(555,702),yticks=[581,671],xticks=[-38,-20,0,20,38],
           xlabel='Integer node s',ylabel='Available total derivative order',
           title='Higher-order input is retained')
    ax.legend(loc='upper center',fontsize=8)
    ax.grid(axis='y',alpha=.2)
    budget.barh(['Input','Output + jets'],[671,581],color=['#17668b','#b45428'])
    budget.barh(['Output + jets'],[90],left=[581],color='#d2a348')
    budget.text(335.5,0,'671',va='center',ha='center',color='white',fontsize=12)
    budget.text(290.5,1,'581',va='center',ha='center',color='white',fontsize=12)
    budget.text(626,1,'90',va='center',ha='center',fontsize=10)
    budget.set(xlim=(0,700),xlabel='Total order',title='581 + (91 - 1) = 671')
    budget.text(.5,-.27,'38 nodes x 91 jets = 3458 conditions',ha='center',transform=budget.transAxes,fontsize=9)
    fig.suptitle('First contraction: exact counting example, q = 2 and R = 38',fontsize=14)
    fig.savefig(output/'yu-second-first-contraction.png',dpi=160)
    plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--figure',action='store_true')
    args=parser.parse_args();args.output.mkdir(exist_ok=True,parents=True)
    result=calculate_contraction()
    target=args.output/'second-first-contraction-check.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.figure: render(result,args.output)
    print(json.dumps({k:result[k] for k in ('state','endpoint_comparisons','strict_mass_gap','strict_input_gap','counting_example')}))

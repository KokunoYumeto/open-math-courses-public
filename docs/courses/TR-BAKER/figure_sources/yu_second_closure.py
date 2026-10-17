"""Exact certificates and Figure10.55 for TR-BAKER10.188--10.190.

CC0. Rational constants are certified with Fraction. The worked support
uses the sibling yu_second_scale.py, supplied in the same source package.
Plot coordinates illustrate proved inequalities, not sampled valuations.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json


def certificate():
    rows = [
        ('At least 3 bases; outside III', F(1209,1340)*F(27,20)*F(9,8)**2, F(3,2)),
        ('At least 3 bases; III', F(495,1794)*F(27,10)*F(3,2)**2, F(3,2)),
        ('Two bases; p=7, III', F(495,1794)*F(27,10)**2*F(5,6)*F(19,20), F(3,2)),
        ('Two bases; p=7, IV', F(1209,1340)*F(27,20)**2*F(19,20), F(3,2)),
        ('Two bases; Q at p=5', F(557,1790)*F(19,7)**2*F(3,4)*F(4,5), F(11,8)),
    ]
    comparisons = []
    for name, ratio, height_cap in rows:
        gap = ratio-height_cap
        assert gap > 0
        comparisons.append({'case':name,'constant_ratio_strict_lower':str(ratio),
                            'height_ratio_strict_upper':str(height_cap),'positive_gap':str(gap)})
    assert F(557,1790)*F(19,7)**2*F(3,4)*F(4,5) == F(603231,438550)
    assert F(603231,438550)-F(11,8) == F(899,1754200)
    assert F(495,1794)*F(19,7)**2*F(3,4)*F(4,5)>1
    assert F(11,8)*F(303,25)-F(827,50) == F(1,8)
    assert F(1957,720) > F(19,7) > F(27,10)
    assert F(163,60)+F(7,4320) == F(11743,4320) < F(87,32) < F(11,4)
    assert F(55,8) < 7 < F(19,7)**2
    assert F(27,10)**2*(1+F(7,10)+F(49,200)) > F(346,25)
    assert F(87,32)**2/F(559,375) < 5
    assert F(27,10)**3 > 18
    assert F(76,75)*(2+F(1,16)+F(1,3)) == F(437,180)
    assert F(437,180)/F(56,5) == F(437,2016) < F(1,4)
    assert F(1,16)+F(1,12)+F(1,3) == F(23,48) < 1
    # This only imports the previously supplied exact interval arithmetic.
    sibling = Path(__file__).with_name('yu_second_scale.py')
    spec = importlib.util.spec_from_file_location('tr_baker_second_scale', sibling)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    example = module.worked_example()
    I = module.Interval
    S = I(*map(F,example['S_interval']))
    D = I(*map(F,example['D_interval']))
    t = module.log_integer(3)
    U = 32*S*D/t
    N = F(example['analytic_N'])
    mu, s0, M0 = example['first_step_mu'], example['integer_node_radius'], 7
    actual_ratio = mu*((2*s0+1)*N+M0)/U
    assert F(8,100) < actual_ratio.lo <= actual_ratio.hi < F(9,100)
    # h150 really meets the required G2 bound: ln21<4 and ln5<2.
    assert F(27,10)**4 > 21 and F(19,7)**2 > 5 and 5*(24+3+2) < 150
    return {'constant_comparisons':comparisons,'first_step_uniform_fraction':str(F(437,2016)),
            'first_step_simpler_fraction':'1/4','normality_cost_fraction':str(F(23,48)),
            'worked_first_step_input_fraction_interval':actual_ratio.record(),
            'worked_h':'150','worked_G2_strict_upper':'145',
            'scope':'All-rank comparison and first local input proofs in10.188–10.190. Global zero production not inferred.'}


def figure(data, target):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':11})
    fig,axes=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
    ax=axes[0]
    labels=['n>=3\noutside III','n>=3\nIII','n=2\np=7, III','n=2\np=7, IV','n=2\nQ, p=5']
    gaps=[float(F(x['positive_gap'])) for x in data['constant_comparisons']]
    bars=ax.bar(labels,gaps,color='#167d8d')
    for bar,g in zip(bars,gaps):
        ax.text(bar.get_x()+bar.get_width()/2,g*1.18,f'{g:.4g}',ha='center',fontsize=9)
    ax.set(yscale='log',ylim=(0.0001,0.7),ylabel='Strict positive gap: constant ratio minus height ratio',
           title='The first estimate proves these second-bound ranges')
    ax=axes[1]
    uniform=float(F(data['first_step_uniform_fraction']))
    example=sum(float(F(x)) for x in data['worked_first_step_input_fraction_interval'])/2
    ax.barh(['Uniform bound','Four-base example'],[uniform,example],color='#167d8d')
    ax.axvline(1,color='#b33e35',linestyle='--',label='Available U')
    ax.axvline(.25,color='#9c7638',linestyle=':',label='Simpler uniform bound: U/4')
    for i,value in enumerate([uniform,example]):
        ax.text(value+.02,i,f'< {value+0.0001:.4f} U',va='center')
    ax.set(xlim=(0,1.07),xlabel='First local input cost / U',
           title='Every original jet cost is included')
    ax.legend(loc='lower right',fontsize=9)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False)
        ax.grid(alpha=.15)
        ax.set_axisbelow(True)
    fig.savefig(target,dpi=180)
    plt.close(fig)


if __name__=='__main__':
    here=Path(__file__).resolve().parent
    data=certificate()
    (here/'yu-second-closure-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    figure(data,here/'yu-second-closure.png')
    print(json.dumps(data,indent=2))

"""Exact first fractional-block comparisons at the second scale.

Authored and self-checked by GPT-6 Astra (OpenAI), Ultra. CC0.
The accompanying proof establishes the reductions for all ranks and fields.
No floating-point test is used to certify a mathematical inequality.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import argparse
import json


def case_data():
    xi = Q(101, 100)
    # name,c1,c3,c4,a,q,zeta2,A0 minimum,d minimum,Siegel ratio,
    # normal factor,counterhypothesis multiplier,prefactor upper,target
    return [
        ('I.1', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 2, Q(2,25), Q(3,2)+xi/2, Q(11,10), 627, 1438),
        ('I.2', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 1, Q(2,25), Q(3,2)+xi/2, Q(51,50), 631, 648),
        ('II', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(5,2), 2, Q(1,134), Q(5,4)+xi/4, Q(21,20), 627, 690),
        ('III.1', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 2, Q(10,71), xi, Q(109,100), 452, 495),
        ('III.2', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 1, Q(10,71), xi, Q(6,5), 454, 557),
        ('IV', Q(7,10), Q(3), 14, 7, 2, Q(1321,1250), Q(1,2), 2, Q(4,23), Q(7,6)+xi/6, Q(13,10), 1763, 2418),
        ('V', Q(41,50), Q(3,5), 6, 13, 3, Q(507,500), Q(2), 2, Q(5,211), 1+xi/2, Q(7,6), 343, 406),
    ]


def exp_bounds(c):
    lower = sum(c**k / factorial(k) for k in range(11))
    upper = lower + c**11 / (factorial(11) * (1-c/12))
    return lower, upper


def calculate():
    lam, xi = Q(59,58), Q(101,100)
    rows = []
    for name,c1,c3,c4,a,q,zeta,amin,dmin,w,nfactor,chi,pref,target in case_data():
        c2 = Q(a,q*q)/zeta
        c = Q(27,50) if q == 2 else Q(4,5)
        ell = Q(7,50) if q == 2 else Q(11,50)
        rmin = 3 if q == 2 else 4
        assert chi*pref < target
        r0 = rmin
        radius_upper = (1-c/Q(r0+1))**(-r0-1) + 1/(c3*q*dmin*(r0+1)**2)
        assert radius_upper < q
        comparisons = []
        for r in list(range(rmin,8)) + [8]:
            tail = r == 8
            y = Q(1,r+1)
            eta, smin = 1-c*y, c3*q*dmin*(r+1)**2
            tmin = Q(12,29)*(r+1)*12**r
            br = 1500*12**(r-3)
            eps = Q(8*r+15,9*(r+1)*br)
            rem = Q(1,79)+Q(1,71928*br)
            hminus = eta**(r+1)
            hplus = 1/exp_bounds(c)[0] if tail else hminus
            cr = Q(1) if tail else 1-Q(483,824)*y
            common = ((1/hminus+1/smin)/c2
                      + w/(2*c2)*(1+1/(2*smin))
                      + y*y/(c2*c3*q)
                      + (1+w/2)*c1*eps+(1+w)*c1*rem)
            b = lam*(1+ell+w+ell*Q(q,q-1))
            k = (Q(107,103)+Q(3,8)*y)*hplus+w*cr
            arith = {
                'minimum': common+xi*(b*amin/c4+k/c3)/(1+amin),
                'infinity': common+xi*b/c4,
            }
            if tail:
                gamma = (2*c*q/exp_bounds(c)[1]*sum(Q(1,q**j) for j in range(4))
                         - Q(q*9*17,q**8)/smin)
            else:
                gamma = (2*c*q/Q(q**r)*sum((q*eta)**j for j in range(r+1))
                         - Q(q*(r+1),q**r)/smin
                         *(1-hminus+2*sum(eta**j-hminus for j in range(1,r+1))))
            normal = lam*nfactor/(c4*q**r)
            input_lower = c1*q*chi-xi*(1-hminus+2/tmin)/(q**r*c3*(1+amin))
            for endpoint, arithmetic in arith.items():
                gap_a, gap_i = gamma-normal-arithmetic, input_lower-arithmetic
                assert gap_a > Q(1,2), (name,r,endpoint,'mass',float(gap_a))
                assert gap_i > Q(1,1000), (name,r,endpoint,'input',float(gap_i))
                comparisons.append({
                    'ranks': 'all >= 8' if tail else r,
                    'A0_endpoint': endpoint, 'arithmetic_upper': str(arithmetic),
                    'normal_loss_upper': str(normal), 'mass_lower': str(gamma),
                    'input_lower': str(input_lower),
                    'mass_gap': str(gap_a), 'input_gap': str(gap_i),
                })
        bounds = {'I.1':(Q(99,100),Q(3,25)),'I.2':(Q(99,100),Q(3,2000)),'II':(Q(109,100),Q(3,20)),'III.1':(Q(93,100),Q(1,20)),'III.2':(Q(93,100),Q(19,100)),'IV':(Q(51,50),Q(11,25)),'V':(Q(27,25),Q(69,100))}
        assert all(Q(v['mass_gap'])>bounds[name][0] and Q(v['input_gap'])>bounds[name][1] for v in comparisons)
        rows.append({'case':name,'siegel_ratio_upper':str(w),
                     'counterhypothesis_multiplier':str(chi),
                     'scaled_prefactor_upper':str(chi*pref),
                     'stated_prefactor':target,'radius_upper':str(radius_upper),
                     'comparisons':comparisons,
                     'minimum_mass_gap':str(min(Q(v['mass_gap']) for v in comparisons)),
                     'minimum_input_gap':str(min(Q(v['input_gap']) for v in comparisons))})
    # Exact elementary lower bounds on p^(f A0) in the seven rows.
    assert 3**3 > 5**2
    assert 5**5 > 50**2
    assert 5**3 > 3**4
    assert Q(7) > Q(5,2)**2
    rho_bounds = [Q(5),Q(5),Q(50),Q(3),Q(3),Q(5,2),Q(16)]
    for row, lower in zip(rows,rho_bounds):
        assert 1/(Q(27,10)*lower-1) == Q(row['siegel_ratio_upper'])
    return {'state':'all_exact_comparisons_passed',
            'scope':'First fractional block at second scale with strengthened kernel choice and casewise chi*U counterhypothesis; actual degree at most q^r*d retained. No contracted-stage conclusion.',
            'finite_ranks':34,'uniform_tail_rows':7,'endpoint_comparisons':82,
            'strict_mass_gap':'1/2','strict_input_gap':'1/1000','cases':rows}


def render(result, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
    labels = [r['case'] for r in result['cases']]
    x = list(range(7))
    axes[0].bar(x,[float(Q(r['siegel_ratio_upper'])) for r in result['cases']],color='#267d69')
    axes[0].axhline(10/17,color='#a44436',linestyle='--',label='Earlier sufficient bound 10/17')
    axes[0].set(xticks=x,xticklabels=labels,ylabel='Upper bound for row / surplus ratio',
                title='Extra selected columns lower coefficient height')
    axes[0].legend(fontsize=8)
    axes[1].bar(x,[float(Q(r['minimum_input_gap'])) for r in result['cases']],color='#175e86')
    axes[1].set(yscale='log',xticks=x,xticklabels=labels,
                ylabel='Strict lower bound for input minus arithmetic cost',
                title='Full root-field cost: all ranks in each case')
    axes[1].axhline(.001,color='#a44436',linestyle='--',label='Proved uniform margin 1/1000')
    axes[1].legend(fontsize=8)
    for ax in axes: ax.grid(axis='y',alpha=.2)
    fig.suptitle('The first second-scale fractional zero block',fontsize=14)
    fig.savefig(output/'yu-second-fractional-profile.png',dpi=160)
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--figure',action='store_true')
    args = parser.parse_args()
    result = calculate()
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/'second-fractional-profile-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.figure: render(result,args.output)
    print(json.dumps({k:result[k] for k in ('state','finite_ranks','uniform_tail_rows','endpoint_comparisons','strict_mass_gap','strict_input_gap')}))

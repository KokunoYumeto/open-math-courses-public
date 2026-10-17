"""Exact endpoints and Figure 10.57 for TR-BAKER-10.

Authored and self-checked by GPT-6 Astra (OpenAI), Ultra. CC0.
This calculation checks rational identities and endpoints. The lesson
proves the reductions that make these finitely many comparisons uniform.
Run with --output-dir PATH to save the figure and exact JSON certificate.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json


def calculate():
    lam, xi = Q(59, 58), Q(101, 100)
    eps, rem = Q(13, 18000), Q(1, 79) + Q(1, 71928 * 1500)
    rows = [
        ('I.1', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 2, Q(3,2)+xi/2, Q(27,500), 3),
        ('I.2', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 1, Q(3,2)+xi/2, Q(41,1000), 3),
        ('II', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(5,2), 2, Q(5,4)+xi/4, Q(3,10), 3),
        ('III.1', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 2, xi, Q(93,1000), 1),
        ('III.2', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 1, xi, Q(93,1000), 1),
        ('IV', Q(7,10), Q(3), 14, 7, 2, Q(1321,1250), Q(1,2), 2, Q(7,6)+xi/6, Q(91,250), 1),
        ('V', Q(41,50), Q(3,5), 6, 13, 3, Q(507,500), Q(2), 2, 1+xi/2, Q(4,3), 4),
    ]
    result = []
    for name, c1, c3, c4, a, q, zeta2, amin, dmin, nfactor, lower, pmin in rows:
        c2 = Q(a, q*q)/zeta2
        c5 = Q(27,50) if q == 2 else Q(4,5)
        gamma = c3*q*dmin
        kappa = Q(107,103)+Q(10,17)
        delta = c5-Q(3,8)+Q(10,17)*Q(483,824)
        b = lam*((Q(57,50) if q == 2 else Q(61,50))+Q(10,17))
        norm = lam*nfactor/(c1*c4)
        dlower = Q(2,58)*Q(27,10)*c1*c4*Q(99,100)*(c2*q*pmin)**3*48
        assert dlower > 1500
        assert c1*c2*c3*q > 2
        assert c1*c2*c3*q*pmin > Q(15,4)
        endpoints = []
        for y in (Q(0), Q(1,4)):
            analytic = 2*c5*q/c1*(1-y*y/(2*gamma))
            common = (q/(c1*c2)+Q(10,17)/(2*c1*c2)*(1+y*y/(2*gamma))
                      +y*y/2+Q(22,17)*eps+Q(27,17)*rem+norm)
            for ae in ('minimum', 'infinity'):
                ratio = b/c4 if ae == 'infinity' else (b*amin/c4+(kappa-delta*y)/c3)/(1+amin)
                arithmetic = common+xi/c1*ratio
                gap = analytic-arithmetic
                assert gap > lower > Q(1,25)
                endpoints.append({'y':str(y), 'A0_endpoint':ae, 'analytic':str(analytic),
                                  'arithmetic_with_normal_loss':str(arithmetic), 'gap':str(gap)})
        # Coefficient of y^2 in either gap: strictly negative.
        quadratic = -c5*q/(c1*gamma)-Q(10,17)/(4*c1*c2*gamma)-Q(1,2)
        assert quadratic < 0
        result.append({'case':name,'D_over_A_lower_at_rank3':str(dlower),
                       'c1_c2_c3_q':str(c1*c2*c3*q), 'quadratic_coefficient':str(quadratic),
                       'proved_gap_lower_bound':str(lower),'endpoints':endpoints})
    assert Q(25,1998) < Q(1,79)
    assert Q(20907,89600) < Q(1,4) and Q(2323,22680) < Q(1,4)
    assert Q(27,10)**9 > 7500 and Q(27,10)**3 > 12
    assert Q(40,39)*6+Q(1,2) < 7
    assert Q(117,10)+Q(71,100)+Q(4,3) > Q(40,3)
    return {'state':'exact_rational_endpoints_passed','scope':'First integer extension at depth zero, every field case; not fractional or later-stage vanishing.',
            'cases':result, 'endpoint_count':28, 'common_gap_lower_bound':'1/25'}


def symbolic_checks():
    import sympy as s
    r,c1,c3,c4,q,d,H,D,t,e,N,theta,A,lam=s.symbols('r c1 c3 c4 q d H D t e N theta A lam',positive=True)
    S=c3*q*(r+1)*d*H/t
    T=q*(r+1)*D/(c1*e*N*t)
    Z=S*D/d
    assert s.simplify(T*H/Z-1/(c1*c3*e*N)) == 0
    degree=lam*Z*theta/(c1*c4*N*A)
    assert s.simplify(degree*(N+1/(q-1))/(Z*d/(e*t))
                      -lam*e*theta*t/(c1*c4*A*d)*(1+1/((q-1)*N))) == 0
    C=(r+s.Rational(4,103))/(r+1)+s.Rational(3,8)*(r-1)/(r+1)**2
    assert s.simplify(1-C-(483*r+1101)/(824*(r+1)**2)) == 0
    count=(s.Rational(10,9)/(r+1)**2+r/(3*(r+1))
           +5*(3*r+1)/(9*(r+1)**2)+5*r/(9*(r+1)))
    assert s.simplify(count-(8*r+15)/(9*(r+1))) == 0
    return ['TH/Z identity', 'normalization identity with symbolic prime-minus-one',
            'simplex mean deficit', 'four-term logarithmic column sum']


def render(result, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    ranks=np.arange(3,31)
    exact=(ranks+4/103)/(ranks+1)+3*(ranks-1)/(8*(ranks+1)**2)
    envelope=1-483/(824*(ranks+1))
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    ax=axes[0]
    ax.plot(ranks,exact,color='#175e86',label=r'$C_r$')
    ax.plot(ranks,envelope,color='#bd6b22',linestyle='--',label=r'$1-483/[824(r+1)]$')
    ax.axhline(1,color='#555555',linewidth=1)
    ax.set(xlabel='Rank r',ylabel='Coefficient of TH in the mean scalar bound',
           title='Complete derivative simplex',ylim=(0.78,1.015))
    ax.legend(loc='lower right');ax.grid(alpha=.2)
    vals=[min(float(Q(x['gap'])) for x in row['endpoints']) for row in result['cases']]
    ax=axes[1]
    ax.bar([x['case'] for x in result['cases']],vals,color='#267d69')
    ax.set_yscale('log');ax.axhline(1/25,color='#a44436',linestyle='--',label='Common margin 1/25')
    for i,v in enumerate(vals): ax.text(i,v*1.12,f'{v:.3f}',ha='center',fontsize=9)
    ax.set(ylabel='Analytic minus arithmetic bound, divided by Zd/(et)',
           title='First integer extension: radius qS, order ηT',ylim=(.025,2.1))
    ax.legend(loc='upper left',fontsize=9);ax.grid(axis='y',alpha=.2)
    fig.suptitle('Second-scale coefficient heights and exact algebraic zeros',fontsize=14)
    fig.savefig(output/'yu-second-initial-height.png',dpi=160)
    plt.close(fig)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    result=calculate();result['symbolic_identities']=symbolic_checks()
    (args.output_dir/'second-initial-height-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    render(result,args.output_dir)
    print(json.dumps({'state':result['state'],'endpoints':28,'symbolic_identities':len(result['symbolic_identities'])}))


if __name__ == '__main__': main()

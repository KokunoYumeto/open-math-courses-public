"""Exact certificates for the second-scale integer extension, TR-BAKER-10.

Authored and self-checked by GPT-6 Astra (OpenAI), Ultra. CC0.
The lesson proves the uniform reductions. This script verifies their
rational coefficients, endpoints and exponential-series bounds.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import argparse
import json


def calculate():
    import sympy as sp
    y = sp.symbols('y')
    lam, xi = Q(59, 58), Q(101, 100)
    eps, rem = Q(13, 18000), Q(1, 79) + Q(1, 71928 * 1500)
    # name,c1,c3,c4,a,q,zeta2,A0min,dmin,normal factor,
    # strict finite-step lower bound, strict tail-at-five lower bound
    cases = [
        ('I.1', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 2, Q(3,2)+xi/2, Q(7,10), Q(12,5)),
        ('I.2', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(3,2), 1, Q(3,2)+xi/2, Q(69,100), Q(119,50)),
        ('II', Q(7,10), Q(6,5), 14, 7, 2, Q(5101,5000), Q(5,2), 2, Q(5,4)+xi/4, Q(93,100), Q(67,25)),
        ('III.1', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 2, xi, Q(73,100), Q(67,50)),
        ('III.2', Q(7,10), Q(8,5), 14, 7, 2, Q(2083,2000), Q(3,4), 1, xi, Q(18,25), Q(33,25)),
        ('IV', Q(7,10), Q(3), 14, 7, 2, Q(1321,1250), Q(1,2), 2, Q(7,6)+xi/6, Q(93,100), Q(41,50)),
        ('V', Q(41,50), Q(3,5), 6, 13, 3, Q(507,500), Q(2), 2, 1+xi/2, Q(9,2), Q(57,10)),
    ]
    results, total_coefficients = [], 0
    for name,c1,c3,c4,a,q,zeta,amin,dmin,nfactor,finite_bound,tail_bound in cases:
        c2 = Q(a,q*q)/zeta
        c5 = Q(27,50) if q == 2 else Q(4,5)
        ell = Q(7,50) if q == 2 else Q(11,50)
        gamma, normal = c3*q*dmin, lam*nfactor/(c1*c4)
        polynomials = []
        for j in range(1,5):
            eta = 1-c5*y
            analytic = 2*c5*q**(j+1)/c1*eta**j-c5*q/(c1*gamma)*eta**j*y*y
            common = (Q(q**(j+1))/(c1*c2)
                      + Q(10,17)/(2*c1*c2)*(1+y*y/(2*gamma))
                      + y*y/2+Q(22,17)*eps+Q(27,17)*rem+normal)
            b = lam*(1+(j+1)*ell+Q(10,17))
            k = (Q(107,103)+Q(3,8)*y)*eta**(j+1)+Q(10,17)*(1-Q(483,824)*y)
            interval = Q(1,max(4,j+2))
            for endpoint in ('minimum','infinity'):
                ratio = b/c4 if endpoint == 'infinity' else (b*amin/c4+k/c3)/(1+amin)
                poly = sp.Poly(sp.expand(analytic-common-xi/c1*ratio),y)
                n = j+2
                assert poly.degree() <= n
                power = [Q(poly.nth(k))*interval**k for k in range(n+1)]
                bernstein = [sum(power[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1))
                             for i in range(n+1)]
                reconstructed = sum(bernstein[i]*comb(n,i)*(y/interval)**i
                                    *(1-y/interval)**(n-i) for i in range(n+1))
                assert sp.expand(reconstructed-poly.as_expr()) == 0
                assert min(bernstein) > finite_bound > Q(1,2)
                total_coefficients += len(bernstein)
                polynomials.append({'step':j,'A0_endpoint':endpoint,'interval_upper':str(interval),
                                    'degree':n,'bernstein_coefficients':list(map(str,bernstein)),
                                    'minimum_coefficient':str(min(bernstein))})
        eta_lower = Q(29,50) if q == 2 else Q(4,9)
        alpha = (2*c5*eta_lower-1/c2)/c1
        constant = (c5*q/(16*c1*gamma)
                    + Q(10,17)/(2*c1*c2)*(1+Q(1,32)/gamma)
                    + Q(1,32)+Q(22,17)*eps+Q(27,17)*rem+normal
                    + xi/c1*(lam*(1+Q(10,17))/c4
                             +(Q(107,103)+Q(10,17))/(c3*(1+amin))))
        slope = xi*lam*ell/(c1*c4)
        value_at_five = alpha*q**6-constant-6*slope
        increment_at_five = alpha*(q-1)*q**6-slope
        assert alpha > 0 and increment_at_five > 0
        assert value_at_five > tail_bound > Q(1,2)
        results.append({'case':name,'finite_lower_bound':str(finite_bound),
                        'finite_polynomials':polynomials,'tail_alpha':str(alpha),
                        'tail_constant':str(constant),'tail_slope':str(slope),
                        'tail_value_at_five':str(value_at_five),
                        'tail_increment_at_five':str(increment_at_five),
                        'tail_lower_bound':str(tail_bound)})
    exponential_bounds = []
    for c, upper in [(Q(27,50),Q(50,29)),(Q(4,5),Q(9,4))]:
        series_upper = sum(c**k/factorial(k) for k in range(7))
        series_upper += c**7/factorial(7)/(1-c/8)
        assert series_upper < upper
        exponential_bounds.append({'exponent':str(c),'series_upper':str(series_upper),
                                   'strict_upper':str(upper),'gap':str(upper-series_upper)})
    assert total_coefficients == 308
    assert Q(725,82944) < Q(1,100)
    assert Q(101,100)*Q(115,48)*Q(27,50)/(Q(7,10)*2) == Q(20907,22400) < Q(15,16)
    assert Q(101,100)*Q(115,48)*Q(4,5)/(Q(7,10)*3) == Q(2323,2520) < Q(15,16)
    return {'state':'exact_uniform_reductions_passed',
            'scope':'All depth-zero integer stages through q^r S, order eta^r T, every r>=3 and every stated field case. No fractional or contracted-stage assertion.',
            'cases':results,'finite_polynomials':56,'bernstein_coefficients':308,
            'exponential_bounds':exponential_bounds,'later_step_gap_lower_bound':'1/2',
            'local_input_upper_bound':'15/16'}


def render(result, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
    ax=axes[0]
    stages=list(range(7));eta=Q(1)-Q(27,50)/7
    ax.plot(stages,[2**j for j in stages],marker='o',color='#175e86',label=r'Radius $2^j S$')
    ax.set_yscale('log',base=2)
    ax.set(xlabel='Integer stage j',ylabel='Radius / S',xticks=stages,
           title='Example: r = 6, q = 2, c5 = 27/50')
    ax.set_yticks([1,2,4,8,16,32,64],labels=['1','2','4','8','16','32','64'])
    right=ax.twinx()
    right.plot(stages,[float(eta**j) for j in stages],marker='s',color='#bd6b22',label=r'Order $\eta^j T$')
    right.set(ylabel='Prepared total order / T',ylim=(.55,1.025))
    ax.yaxis.label.set_color('#175e86');ax.tick_params(axis='y',labelcolor='#175e86')
    right.yaxis.label.set_color('#bd6b22');right.tick_params(axis='y',labelcolor='#bd6b22')
    ax.grid(alpha=.2)
    ax=axes[1]
    labels=[row['case'] for row in result['cases']]
    finite=[min(float(Q(p['minimum_coefficient'])) for p in row['finite_polynomials']) for row in result['cases']]
    tail=[float(Q(row['tail_value_at_five'])) for row in result['cases']]
    xs=list(range(7))
    ax.bar([x-.19 for x in xs],finite,width=.38,label='Steps 1–4: coefficient minimum',color='#267d69')
    ax.bar([x+.19 for x in xs],tail,width=.38,label='Steps ≥5: tail lower bound',color='#175e86')
    ax.axhline(.5,color='#a44436',linestyle='--',label='Common strict gap 1/2')
    ax.set(xticks=xs,xticklabels=labels,ylabel='Gap lower bound / [Zd/(et)]',
           title='Uniform bounds for every later integer step')
    ax.legend(fontsize=8);ax.grid(axis='y',alpha=.2)
    fig.suptitle('Exact zeros on every enlarged integer interval',fontsize=14)
    fig.savefig(output/'yu-second-integer-extension.png',dpi=160)
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
    output=parser.parse_args().output_dir;output.mkdir(parents=True,exist_ok=True)
    result=calculate()
    (output/'second-integer-extension-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    render(result,output)
    print(json.dumps({k:result[k] for k in ['state','finite_polynomials','bernstein_coefficients']}))


if __name__=='__main__':main()

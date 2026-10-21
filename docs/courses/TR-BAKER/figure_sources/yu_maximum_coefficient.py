"""Threshold comparisons and relation elimination for Corollary 10.250.

Independently authored mathematical illustration; CC0.
The rational checks verify the explicit margins used in the proof.
Numerical samples illustrate, and do not replace, its universal inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import math


def exact_checks():
    margins = {
        'log2_lower': F(842, 1215) - F(11, 16),
        'log2_upper': F(3, 4) - F(25, 36),
        'exponential_lower': sum((F(1, math.factorial(k)) for k in range(5)), F(0)) - F(27, 10),
        'log116_below5': F(8, 3)**5 - 116,
        'log52_below4': F(27, 10)**4 - 52,
        'one_base_floor': 4096*F(4, 9)-1000,
        'one_base_threshold': 512*F(4, 9)-1,
        'one_base_residue_term': 16**4*F(4, 9)-24,
        'threshold_polynomial_at2': F(-3*2**2+23*2-10),
        'threshold_polynomial_at7': F(-3*7**2+23*7-10),
        'rank_absorption_margin': F(16)-2,
    }
    assert all(v > 0 for v in margins.values())
    for n in range(2, 8):
        assert F(11*n+47, 4) > F((n+1)*(7*n+5), 2*n)
    # The polynomial is concave, so its endpoint check controls [2,7].
    assert -6 < 0
    beta = [F(3), F(5), F(15)]
    b, k = [1, -1, 1], [-1, -1, 1]
    product = lambda xs, powers: math.prod(x**a for x, a in zip(xs, powers))
    assert product(beta, k) == 1
    reduced = [k[2]*b[i]-k[i]*b[2] for i in range(2)]
    assert reduced == [2, 0]
    assert product(beta, b) == product(beta[:2], reduced) == 9
    assert product([F(6), F(10), F(15)], b) == 9
    assert F(6, 10)-1 == F(-2, 5)
    return {'positive_rational_margins': {k: str(v) for k, v in margins.items()},
            'dependent_example': {'bases': [6,10,15], 'normalized': [3,5,15],
                                  'relation': k, 'reduced_coefficients': reduced,
                                  'product': 9, 'valuation_at_two': 3}}


def parameters(n, d, e, f, p):
    l = math.log(p)
    x, y = math.log(2*n*d), math.log(2*d)
    log_pd_minus1 = d*l + math.log1p(-math.exp(-d*l))
    J = e+d/f
    log_z = ((n+3)*math.log(16)+4+math.log(e*f/(2*J))
             +1.5*math.log(n)+2*math.log(x)+(n+3)*math.log(d)
             +log_pd_minus1-math.log(l))
    log_r = (math.log(n)+n*math.log(d)+2*math.log(f)
             -(n-1)*math.log(e)+log_pd_minus1-f*l+math.log(x/y))
    return log_z, log_r


def sample_checks():
    count = 0
    for n in [2,3,4,5,6,7,8,16,32,64,128]:
        for d in [1,2,3,4,8,16,32]:
            for e in range(1, d+1):
                for f in range(1, d//e+1):
                    for p in [2,3,5,7,101,65537]:
                        z, r = parameters(n,d,e,f,p)
                        assert z > math.log(32)+2+2*math.log(d)
                        assert r >= math.log(n*d)-1e-12
                        assert math.log((n+1)*(7*n+5+math.log(d))) < math.log(2)+r+math.log(z)
                        assert math.log((n+1)*f*math.log(p)) < r+math.log(z)
                        assert z > max(n, math.log(116*d*max(1,math.log(d))))
                        count += 1
    return {'sampled_parameter_tuples': count, 'role': 'Supplementary samples; the lesson proves all ranks, degrees and primes analytically.'}


def draw(path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig, (ax, flow) = plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1,1.15]})
    fig.patch.set_facecolor('white')
    ns = list(range(2,25))
    data = [parameters(n,1,1,1,2) for n in ns]
    ax.plot(ns,[z for z,r in data],color='#176b59',lw=2.6,label=r'$\log Z_n$')
    ax.plot(ns,[(n+1)*(7*n+5)/(2*math.exp(r)) for n,(z,r) in zip(ns,data)],color='#a65b12',lw=2.2,label=r'$(n+1)(7n+5)/(2R_n)$')
    ax.plot(ns,[(n+1)*math.log(2)/math.exp(r) for n,(z,r) in zip(ns,data)],color='#375ca8',lw=2.2,label=r'$(n+1)\log 2/R_n$')
    ax.set(title='The coefficient threshold',xlabel='Number of bases n',ylabel='Logarithmic threshold')
    ax.set_xlim(2,24);ax.set_ylim(bottom=0);ax.grid(alpha=.18)
    ax.legend(loc='upper left',fontsize=11,frameon=False)
    ax.text(.02,-.18,'Samples: d = e = f = 1, p = 2.\nLemma 10.247 proves the inequalities for all parameters.',transform=ax.transAxes,fontsize=11,va='top')
    flow.set(xlim=(0,1),ylim=(0,1));flow.axis('off')
    flow.set_title('The proof for arbitrary bases',pad=18)
    def box(y,text,height=.125,color='#eef5f2'):
        flow.add_patch(FancyBboxPatch((.04,y),.92,height,boxstyle='round,pad=.012',facecolor=color,edgecolor='#91a39d'))
        flow.text(.5,y+height/2,text,ha='center',va='center',fontsize=12)
    box(.80,r'Normalize inside $K$: $\beta_i=\alpha_i^e p^{-v_i}$'+'\n'+r'height $\leq Jw_i$; retain the original degree $d$')
    box(.61,'B ≤ Zₙ log B: use the local height bound\nB > Zₙ log B: absorb the fixed parameters',color='#f5f0e7')
    box(.40,'Independent: the second explicit estimate\nOne base: residue order and local height')
    box(.16,'Dependent: delete a largest-weight circuit base\n'+r'$\log B^{\prime}<2u_x\log B,\quad u_x=Qw_x$'+'\n'+r'$\mathcal{G}_n/(Q\mathcal{G}_{n-1})>16d>2$',height=.16,color='#edf1f9')
    for y1,y2 in [(.79,.75),(.60,.54),(.39,.34)]:
        flow.annotate('',xy=(.5,y2),xytext=(.5,y1),arrowprops={'arrowstyle':'->','color':'#596b65','lw':1.5})
    flow.text(.5,.035,'Exact example at p = 2: (3,5,15), b = (1,−1,1)\n'+r'$3^{-1}\cdot5^{-1}\cdot15=1\ \Rightarrow\ (3,5),\ b^{\prime}=(2,0);\ v_2(9-1)=3$',ha='center',va='center',fontsize=11)
    fig.suptitle('A maximum-coefficient bound without independence',fontsize=18,y=.98)
    fig.subplots_adjust(left=.065,right=.975,top=.87,bottom=.21,wspace=.27)
    fig.savefig(path,dpi=180,facecolor='white');plt.close(fig)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('yu-maximum-coefficient.png'))
    parser.add_argument('--check-output',type=Path)
    args=parser.parse_args()
    result={**exact_checks(),**sample_checks()}
    draw(args.output)
    if args.check_output:
        args.check_output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'exact_margins':len(result['positive_rational_margins']),'sampled_parameter_tuples':result['sampled_parameter_tuples'],'figure':str(args.output)}))

"""Exact checks and illustrations for saturation and contraction depth.

GPT-6 Astra (OpenAI), Ultra. CC0. The accompanying universal proofs
establish the parameter extension, geometric stop and scalar envelope.
This does not certify the still-unproved later zero induction.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json
from yu_second_fractional_profile import case_data


def calculate():
    lam, xi = Q(59, 58), Q(101, 100)
    degree_ratio = Q(9 * 256**2 * 32, 392 * 87 * 5)
    order_ratio = Q(3, 35) * Q(2**15, 5)
    allocation_middle = Q(2**10, 29)
    allocation_full = Q(16**6, 6 * 3 * 4 * 12**3)
    rank_one = Q(9450, 128) * Q(10, 27)**20
    rank_many = 30 * 35**2 * Q(10, 27)**32
    assert degree_ratio > 20 and order_ratio > 4
    assert allocation_middle > 1 and allocation_full == Q(32768, 243) > 31
    assert Q(2, 7) * 2**13 > 2**11
    assert 2**11 * Q(2, 3)**3 > 1
    assert Q(256, 12) * Q(3, 5) > 1
    assert rank_one < Q(1, 10**6) and rank_many < Q(1, 10**6)
    assert 35 * Q(10, 27)**12 < 1
    # Coefficients of exp(x)'s quadratic lower bound minus the scale product.
    assert Q(1, 40) + Q(1, 5) == Q(9, 40) < 1
    assert Q(1, 40 * 5) == Q(1, 200) < Q(1, 2)
    rows = []
    for name,c1,c3,c4,a,q,zeta,amin,dmin,w,nfactor,chi,pref,target in case_data():
        c2 = Q(a, q*q)/zeta
        qmin = 2*Q(173,200)**4 if q == 2 else 3*Q(21,25)**5
        log_q_lower = 2*(qmin-1)/(qmin+1)
        log_integer_upper = Q(7,10) if q == 2 else Q(11,10)
        endpoint = 3*lam*xi*c2*log_integer_upper/(c4*q*q*log_q_lower)
        cap = Q(3,5) if q == 2 else Q(2,5)
        assert endpoint < cap
        assert Q(1,1000)+cap < 1
        assert chi*pref < target
        rows.append({'case':name,'Q_lower':str(qmin),'log_Q_lower':str(log_q_lower),
                     'linear_endpoint_ratio_upper':str(endpoint),
                     'strict_linear_cap':str(cap),
                     'full_endpoint_cap':str(cap+Q(1,1000)),
                     'scaled_constant_prefactor':str(chi*pref),'target_prefactor':target})
    # Rational illustration of the exact cancellations, not a full parameter instance.
    original_D, original_A, original_T = Q(210), Q(7), Q(900)
    x = Q(5); B=original_A+x; g=B/original_A
    assert g*original_D/B == original_D/original_A
    assert g*original_T/(g*original_D) == original_T/original_D
    return {'state':'all_exact_comparisons_passed',
            'scope':'Saturation-buffered selected kernel, geometric and rank-product bounds at Q^I>exp(3B), integer scalar absorption for I log Q<=3B. No all-depth zero claim.',
            'degree_ratio_lower':str(degree_ratio),'order_ratio_lower':str(order_ratio),
            'allocation_middle_lower':str(allocation_middle),'allocation_full_lower':str(allocation_full),
            'rank_one_product_upper':str(rank_one),'rank_many_product_upper':str(rank_many),
            'cases':rows}


def render(result, output):
    import math
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    xs=[i/100 for i in range(801)]
    axes[0].plot(xs,[(1+x/41)*(1+x/6)*math.exp(-x) for x in xs],color='#175e86')
    axes[0].axhline(1,color='#a44436',linestyle='--',label='Proved upper bound 1')
    axes[0].set(xlabel='x = log J',ylabel='(h+x)(A+x) / [h A exp(x)]',
                title='Saturation pays for the larger polynomial scale')
    axes[0].text(.98,.85,'Illustration: h = 41, A = 6\nContinuous x; actual J is a q-power',
                 transform=axes[0].transAxes,ha='right',fontsize=8)
    axes[0].legend(fontsize=8)
    for index,color in [(0,'#175e86'),(6,'#267d69')]:
        name,c1,c3,c4,a,q,zeta,*_ = case_data()[index]
        r,c=(3,.54) if q==2 else (4,.8)
        frac=(1-c/(r+1))**(r+1); Qbase=q*frac
        c2=float(Q(a,q*q)/zeta); B=6
        # vartheta/N is bounded by xi; this plots that upper envelope.
        rho=3*(59/58)*(101/100)*c2*math.log(q)/(c4*q*q*math.log(Qbase))
        us=[i/500 for i in range(501)]
        axes[1].plot(us,[math.exp(-3*B*u)+rho*u for u in us],color=color,
                     label=f'q = {q}, r = {r}')
    axes[1].axhline(1,color='#a44436',linestyle='--',label='Proved endpoint envelope 1')
    axes[1].set(xlabel='Normalized depth I log Q / (3B)',ylabel='Torus plus depth cost, divided by its initial torus cost',
                title='Convexity bounds every intermediate depth')
    axes[1].text(.98,.85,'Illustration: B = 6, j = 1\nSeparate factorial-denominator remainder retained',
                 transform=axes[1].transAxes,ha='right',fontsize=8)
    axes[1].legend(fontsize=8,loc='lower right')
    for ax in axes: ax.grid(alpha=.2)
    fig.savefig(output/'yu-second-depth-buffer.png',dpi=160)
    plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--figure',action='store_true');args=p.parse_args()
    result=calculate();args.output.mkdir(exist_ok=True,parents=True)
    (args.output/'second-depth-buffer-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.figure:render(result,args.output)
    print(json.dumps({k:result[k] for k in ['state','degree_ratio_lower','allocation_full_lower','rank_one_product_upper','rank_many_product_upper']}))

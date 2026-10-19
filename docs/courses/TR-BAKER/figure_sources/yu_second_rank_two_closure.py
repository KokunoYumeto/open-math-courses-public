"""Exact rational comparisons for the unramified-five two-base estimate.

Original CC0 calculation by GPT-6 Astra (OpenAI), Ultra. The accompanying
proof supplies the monotonicity and all-degree arguments; this program
checks their finite rational endpoints, not numerical samples of fields.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys


def unit_log_interval(x, terms=64):
    assert F(1) <= x <= F(2)
    y = (x-1)/(x+1)
    total = 2*sum((y**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    error = 2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
    return total, total+error


def log_interval(x):
    x=F(x); assert x >= 1
    k=0
    while x > 2:
        x/=2; k+=1
    lo,hi=unit_log_interval(x)
    l2,u2=unit_log_interval(F(2))
    return lo+k*l2,hi+k*u2


def certificate():
    checks={}
    def short_gap(gap):
        result=F(gap.numerator*10**9//gap.denominator-1,10**9)
        assert 0 < result < gap
        return str(result)
    def lower(name, actual, bound):
        assert actual > bound, name
        checks[name]={'kind':'strict_lower','bound':str(bound),'strict_gap_lower_bound':short_gap(actual-bound)}
    def upper(name, actual, bound):
        assert actual < bound, name
        checks[name]={'kind':'strict_upper','bound':str(bound),'strict_gap_lower_bound':short_gap(bound-actual)}
    e0=sum((F(1,factorial(j)) for j in range(11)),F(0))
    l2,u2=log_interval(2);l3,u3=log_interval(3);l5,u5=log_interval(5);l7,u7=log_interval(7)
    x_upper=2*(2+u7)+F(471,100)+u2
    g1_upper=2*(2+u7)+F(471,100)+log_interval(x_upper)[1]
    g2_lower=2*(2+l7)+F(199,100)+l3
    upper('G1_constant',g1_upper,F(76,5))
    lower('G2_constant',g2_lower,F(549,50))
    lower('C2_over_C1',F(495,1794)*F(3,8)*e0**2*l5,F(123,100))
    lower('log2',l2,F(69,100));upper('log2_upper',u2,F(7,10))
    lower('log5_lower',l5,F(8,5));upper('log5_upper',u5,F(13,8))
    upper('log_log5',log_interval(F(13,8))[1],F(1,2))
    lower('high_degree_gap',F(123,100)*(F(549,50)+11*F(69,100))-(F(76,5)+11*F(69,100)),F(0))
    lower('log192',log_interval(192)[0],F(26,5))
    upper('log192_upper',log_interval(192)[1],F(53,10))
    upper('log_53_over10',log_interval(F(53,10))[1],F(17,10))
    upper('log64',log_interval(64)[1],F(21,5))
    lower('log6144',log_interval(6144)[0],F(8))
    upper('log6144_upper',log_interval(6144)[1],F(44,5))
    upper('log_44_over5',log_interval(F(44,5))[1],F(11,5))
    lower('B_at_degree65',F(65)*33/F(13,8),F(1200))
    upper('log342048',log_interval(342048)[1],F(13))
    lower('square_root_envelope',F(34,25)**2-F(14,5)**3/12,F(0))
    lower('determinant_gap',F(3848,1125)-(F(1,200)+F(136,75)+F(7,225)+F(13,40)),F(0))
    upper('determinant_coefficient',F(588,25)+F(7,30)+F(1,12),F(24))
    upper('collision_coefficient',F(1,12)+F(49,6000)+F(7,1200),F(1))
    lower('residue_maximum_second_entry',F(19,7)**2*F(8,5)**3/4,F(5))
    small=F(3480)/(218295*F(27,10)**2*F(8,5)**2)*F(64)/F(46,5)*(F(291,5)+6)**2/F(291,5)
    middle=F(696)/(218295*F(27,10)**3*F(8,5)**3)*F(2048,12)*(F(687,10)+F(15,2))**2/F(687,10)
    upper('degree2_through64_ratio',small,F(1,2))
    upper('degree65_through2047_ratio',middle,F(3,5))
    zero=F(34,33)*29/(218295*4*5)+F(464)/(218295*8*2*5*33)
    upper('zero_coefficient_ratio',zero,F(1,1000))
    assert F(13,5)*1200+2 == 3122
    assert (3*F(1,100)*3122).__floor__()+1 == 94
    assert 94*3122 == 293468
    return {'state':'exact_comparisons_passed','checks':checks,'checked_inequalities':len(checks),'exercise87_checked':True,
        'small_degree_ratio_upper':str(small),'middle_degree_ratio_upper':str(middle),
        'all_degree_argument':'d/A(d) and (Gbar(d)+c(d))^2/Gbar(d) increase on each bounded interval; d>=2048 follows from the positive affine coefficient-parameter gap.'}


def figure(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    import numpy as np
    values=certificate()
    fig,ax=plt.subplots(1,2,figsize=(12.8,5),constrained_layout=True)
    left=ax[0]
    small=float(F(values['small_degree_ratio_upper']))
    middle=float(F(values['middle_degree_ratio_upper']))
    left.hlines(1,2,2048,color='#b33d3d',ls='--',label='Target ratio 1')
    left.fill_between([2,64],[small,small],color='#dbeafe')
    left.fill_between([65,2047],[middle,middle],color='#d5eee7')
    left.hlines(small,2,64,color='#275ea5',lw=2.5)
    left.hlines(middle,65,2047,color='#1c7969',lw=2.5)
    left.text(11,.24,'Ordinary height floor\n'+r'$L_i\geq t/d$'+'\nBound < 1/2',ha='center')
    left.text(365,.25,'Tenth-height floor\n'+r'$L_i\geq t/(10d)$'+'\nBound < 3/5',ha='center')
    left.set_xscale('log');left.set_xticks([2,64.5,2047],['2','64 / 65','2047'])
    left.xaxis.set_minor_formatter(NullFormatter())
    left.tick_params(axis='x',labelsize=8);left.set_ylim(0,1.13)
    left.set_xlabel('Global degree d (integer ranges)')
    left.set_ylabel(r'Upper bound for $v_5(\Xi-1)/(C_2\mathsf{h}_2\Omega)$')
    left.set_title('Two determinant bounds; small coefficient parameter')
    left.legend(loc='upper left',fontsize=9);left.grid(alpha=.15)
    right=ax[1];degrees=np.geomspace(2048,8192,160)
    lower=F(511,10000)+F(23,100)*np.log(degrees/2048)
    right.plot(degrees,np.asarray(lower,dtype=float),color='#634a9b',lw=2.5)
    right.axhline(0,color='#b33d3d',ls='--');right.scatter([2048],[float(F(511,10000))],color='#634a9b')
    right.annotate('511/10000 > 0',xy=(2048,float(F(511,10000))),xytext=(2700,.1),arrowprops={'arrowstyle':'->'},fontsize=10)
    right.text(4000,.035,'Increasing for every d ≥ 2048\n'+r'$\mathsf{h}<1.23\mathsf{h}_2$, $C_2/C_1>1.23$',ha='center',fontsize=10)
    right.set_xscale('log');right.set_xticks([2048,4096,8192],['2048','4096','8192'])
    right.xaxis.set_minor_formatter(NullFormatter())
    right.set_xlabel('Global degree d (curve continues)')
    right.set_ylabel('Lower bound for the coefficient-parameter gap / 3')
    right.set_title('Large degrees: the first estimate suffices')
    right.set_ylim(-.02,.42);right.grid(alpha=.15)
    fig.savefig(destination,dpi=170);plt.close(fig)


if __name__=='__main__':
    result=certificate()
    Path(__file__).with_name('second-rank-two-closure-check.json').write_text(json.dumps(result,indent=2)+'\n')
    if '--figure' in sys.argv:
        figure(Path(sys.argv[sys.argv.index('--figure')+1]))
    print(json.dumps({k:result[k] for k in ['state','checked_inequalities','small_degree_ratio_upper','middle_degree_ratio_upper']}))

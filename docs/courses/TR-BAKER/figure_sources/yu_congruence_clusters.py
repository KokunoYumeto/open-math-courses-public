"""Exact congruence-class counts, rounding bounds and Figure 10.52; CC0."""
from fractions import Fraction as F
from math import factorial, exp, floor
from pathlib import Path
import json

ROWS = [('I', F(3, 2), F(12133, 10000), F(5101, 5000)),
        ('II', F(3, 4), F(1641, 1250), F(2083, 2000)),
        ('III', F(1, 2), F(13701, 10000), F(1321, 1250)),
        ('IV', F(2), F(147, 125), F(507, 500))]


def exp_bounds(x):
    assert 0 <= x <= 1
    total = sum(x**j/F(factorial(j)) for j in range(65))
    tail = x**65/F(factorial(65))/(1-x/F(66))
    return total, total+tail


def down(x, scale=10**12):
    return F((x*scale).numerator//(x*scale).denominator, scale)


def up(x):
    return -down(-x)


def certificate():
    rows = []
    for name, a, zeta1, zeta2 in ROWS:
        y = 1/(a+1)
        elo, ehi = exp_bounds(y)
        zlo, zhi = y/(ehi-1), y/(elo-1)
        assert 0 < zlo <= zhi < 1
        h_upper = up(y+zhi)
        f_lower = down(zlo*exp_bounds(1-zlo)[0])
        c = F(2, 5)/(a+F(3, 5))
        forced_lower = down((1+c)/exp_bounds(c)[1])
        forced_height = (a+1)/(a+F(3, 5))
        assert h_upper < zeta1 and forced_height < zeta1
        assert f_lower > 1/zeta2 and forced_lower > 1/zeta2
        rows.append({'case':name, 'A0':str(a), 'zeta1':str(zeta1), 'zeta2':str(zeta2),
            'height_upper':str(h_upper), 'height_gap':str(zeta1-h_upper),
            'rounding_ratio_lower':str(f_lower), 'rounding_gap':str(f_lower-1/zeta2),
            'forced_ratio_lower':str(forced_lower), 'forced_gap':str(forced_lower-1/zeta2),
            'forced_height':str(forced_height)})
    supports = {b: [] for b in range(3)}
    for x in range(6):
        for y in range(6):
            actual = pow(10, x, 27)*pow(19, y, 27) % 27
            residue = ((actual-1)//9) % 3
            assert actual % 9 == 1 and residue == (x+2*y) % 3
            supports[residue].append([x,y])
    assert [len(supports[b]) for b in range(3)] == [12]*3
    even = [[x//2,y//2] for x,y in supports[0] if x%2 == y%2 == 0]
    assert even == [[0,0],[1,1],[2,2]]
    assert all(pow(10,x,27)*pow(19,y,27)%27 == 1 for x,y in even)
    return {'rounding_rows':rows, 'exponential_series_order':64,
        'interval_denominator':10**12, 'supports':supports,
        'compressed_even_class':even,
        'scope':'Finite rational endpoints and exact congruence example. The proofs give all real parameters, all levels and every descent stage.'}


def selected_m(a, rho):
    x0 = 1/rho-a
    assert x0 > .6
    if x0 <= 1:
        return 1
    k = floor(x0)
    threshold = 1/rho-1/(exp(rho)-1)
    return k if x0-k <= threshold else k+1


def draw(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    fig, axes = plt.subplots(1,2,figsize=(12.4,5.0),constrained_layout=True)
    colors = ['#287c8e','#d19836','#8f6eb1']
    ax = axes[0]
    for b,color in enumerate(colors):
        points=[(x,y) for x in range(6) for y in range(6) if (x+2*y)%3==b]
        ax.scatter(*zip(*points),c=color,s=80,label=f'Class {b}: 12 exponents')
    ax.scatter([0,2,4],[0,2,4],facecolors='none',edgecolors='#263342',s=230,
               linewidths=1.5,label=r'Even coordinates in class 0')
    ax.set_xticks(range(6));ax.set_yticks(range(6));ax.set_aspect('equal')
    ax.set_xlabel(r'$\lambda_1$');ax.set_ylabel(r'$\lambda_2$')
    ax.set_title(r'$10^{\lambda_1}19^{\lambda_2}$ modulo $27$; $m_0=2,m=1$')
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.18),ncol=2,frameon=False,fontsize=9)
    ax=axes[1]
    aa=.5
    x0s=np.linspace(.60001,5,1200)
    rhos=1/(aa+x0s)
    ms=np.array([selected_m(aa,float(rho)) for rho in rhos])
    ratios=(aa+ms)*np.exp(-rhos*ms)/((aa+x0s)*np.exp(-rhos*x0s))
    ax.plot(x0s,ratios,color='#287c8e',label=r'$\chi(m)/\chi(x_0)$')
    ax.axhline(1250/1321,color='#b04a3d',linestyle='--',label=r'Proved lower bound $1/1.0568$')
    ax.set_ylim(.94,1.005);ax.set_xlabel(r'$x_0=1/\rho-A$ (scalar model $A=1/2$)')
    ax.set_ylabel('Rounding efficiency');ax.set_title('The integer congruence level')
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.18),frameon=False,fontsize=9)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.13);ax.set_axisbelow(True)
    fig.savefig(destination,dpi=180,bbox_inches='tight');plt.close(fig)


if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    data=certificate()
    (args.output_dir/'yu-congruence-clusters-endpoints.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    draw(args.output_dir/'yu-congruence-clusters.png')
    print(json.dumps({'rounding_rows':data['rounding_rows'],'class_sizes':[len(v) for v in data['supports'].values()]}))

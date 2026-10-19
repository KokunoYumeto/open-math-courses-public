"""Exact envelope checks and the quadratic normalization example; CC0.

The all-rank argument is Lemma 10.238. Endpoint checks are exact rational
arithmetic. The diagram shows those proved upper envelopes, not valuations.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import math

HERE = Path(__file__).resolve().parent
rows = [
    ('Degree >= 2, odd p', F(3627, 1024), F(21, 128), False),
    ('Degree >= 2, p = 2', F(1827, 8192), F(13, 64), False),
    ('Degree 1, p = 3', F(729, 2048), F(21, 128), True),
    ('Degree 1, p >= 5', F(1671, 2048), F(7, 128), True),
]


def mul(x, y):
    """Multiplication in Q[s]/(s^2-2), independently of floating roots."""
    return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def checks():
    results = []
    for name, scalar, base, extra in rows:
        endpoint = scalar*base**2*F(135, 14)*(6 if extra else 1)
        ratio = base*F(64, 27)*(F(7, 6) if extra else 1)
        assert 0 < endpoint < 1 and 0 < ratio < 1
        results.append(dict(case=name, endpoint_upper=str(endpoint),
                            endpoint_margin=str(1-endpoint), ratio_upper=str(ratio)))
    assert [x['ratio_upper'] for x in results] == ['7/18', '13/27', '49/108', '49/324']
    series_e = sum((F(1, math.factorial(j)) for j in range(7)), F(0))
    assert series_e == F(1957, 720) > F(19, 7)
    assert F(19, 7)**4 > 52
    assert F(8, 3)**3 > 16
    assert F(81, 1)/F(8, 3)**3 < 5
    assert F(7, 5)**2 < 2
    # Algebraic identities use pairs, not numerical approximations.
    a1, a2 = (F(7), F(7)), (F(6, 7), F(1, 7))
    b1, b2 = (F(1), F(1)), (F(6), F(1))
    assert mul(a1, a2) == mul(b1, b2) == (F(8), F(7))
    assert mul(b1, (F(1), F(-1))) == (F(-1), F(0))
    assert mul(b2, (F(6), F(-1))) == (F(34), F(0))
    # The derivative at 3 is invertible mod7. A Hensel root mod49
    # checks the exact valuation of Xi-1 separately from its factorization.
    roots49 = [x for x in range(49) if x % 7 == 3 and (x*x-2) % 49 == 0]
    assert roots49 == [10]
    xi_minus_one = (8+7*roots49[0]-1) % 49
    assert xi_minus_one == 28 and xi_minus_one % 7 == 0
    # Verify the two primitive minimal polynomials by exact evaluation.
    assert tuple(mul(a1, a1)[i]-14*a1[i]-(49 if i == 0 else 0) for i in range(2)) == (0, 0)
    assert tuple(49*mul(a2, a2)[i]-84*a2[i]+(34 if i == 0 else 0) for i in range(2)) == (0, 0)
    return dict(state='exact_checks_passed', envelope_endpoints=results,
                exponential_lower_bound=str(series_e),
                example=dict(field='Q(sqrt(2))', prime=7, e=1, f=1,
                             original_valuations=[1, -1], normalized_units=['1+sqrt(2)', '6+sqrt(2)'],
                             product='8+7*sqrt(2)', product_minus_one_valuation=1,
                             hensel_root_mod49=10, nonzero_mod49_remainder=28),
                uniform_scope='Every n>=2 follows from the four exact endpoint and ratio bounds proved in Lemma10.238.',
                excluded_scope='Dependent normalized units and p=2 fields without zeta3 remain unproved here.')


def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.0), gridspec_kw={'width_ratios': [1, 1.1]})
    fig.patch.set_facecolor('#f7f9fc')
    for ax in axes:
        ax.set_facecolor('#f7f9fc')
    ns = list(range(2, 11))
    colors = ['#1b6488', '#a64b2a', '#6d59a4', '#28764f']
    for (name, scalar, base, extra), color in zip(rows, colors):
        ys = [float(scalar)*float(base)**n*(n+1)**3/n**1.5*(n+4 if extra else 1) for n in ns]
        axes[0].semilogy(ns, ys, marker='o', label=name, color=color, linewidth=1.8, markersize=4)
    axes[0].axhline(1, color='#444444', linestyle='--', linewidth=1)
    axes[0].text(9.6, 1.25, 'target ratio = 1', ha='right', fontsize=9)
    axes[0].set(xlabel='Number of bases n', ylabel=r'Proved upper envelope for $2C_2J^n/\mathcal{A}_n$',
                title='The target constant absorbs normalization', xticks=ns, ylim=(1e-10, 3))
    axes[0].grid(True, alpha=.18)
    axes[0].legend(fontsize=8.5, loc='lower left', framealpha=.94)
    ax=axes[1]; ax.axis('off'); ax.set_title(r'Exact example in $\mathbb{Q}(\sqrt{2})$, at $\sqrt{2}\equiv3\ (\mathrm{mod}\ 7)$')
    lines = [
        (0.88, r'$\alpha_1=7(1+\sqrt{2}),\quad\alpha_2=(6+\sqrt{2})/7$', 13),
        (0.76, r'$\operatorname{ord}_{\mathfrak{p}}(\alpha_1)=1,\quad\operatorname{ord}_{\mathfrak{p}}(\alpha_2)=-1$', 12),
        (0.53, r'$\beta_1=1+\sqrt{2},\quad\beta_2=6+\sqrt{2}$', 14),
        (0.42, r'$e=f=1,\quad d=2,\quad J=e+d/f=3$', 12),
        (0.27, r'$\Xi=\alpha_1\alpha_2=\beta_1\beta_2=8+7\sqrt{2}$', 13),
        (0.12, r'$\Xi-1=7(1+\sqrt{2}),\quad\operatorname{ord}_{\mathfrak{p}}(\Xi-1)=1$', 12),
    ]
    for y, text, size in lines:
        ax.text(.5,y,text,ha='center',va='center',fontsize=size,transform=ax.transAxes,color='#17304a')
    ax.annotate('', xy=(.5,.59), xytext=(.5,.70), xycoords='axes fraction', arrowprops=dict(arrowstyle='->',lw=2,color='#1b6488'))
    ax.text(.53,.65,r'$\beta_i=\alpha_i^e7^{-v_i}$', transform=ax.transAxes, fontsize=10,va='center')
    fig.tight_layout(pad=2)
    fig.savefig(HERE/'yu-number-field-refinement.png', dpi=170, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == '__main__':
    data=checks()
    (HERE/'yu-number-field-refinement-check.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    figure()
    print(json.dumps(data))

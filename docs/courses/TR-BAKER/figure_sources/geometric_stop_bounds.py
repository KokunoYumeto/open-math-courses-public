"""Universal geometric stopping bounds (GPT-6.1 Sol, Ultra; CC0)."""
from fractions import Fraction as Q


def bounds():
    """Exact rational bounds; universal monotonicity is proved in the lesson."""
    degree = Q(135143424, 6699000)
    order = Q(47*49*39*32768, 10000*21*44)
    intermediate = Q(72, 725)*Q(2048, 3)/8
    final = 8*Q(192, 125)**2*16**3/(135*2*9)
    assert degree > 20 and order > 4 and intermediate > 8 and final > 31
    return {'degree_comparison_minimum': str(degree),
            'order_comparison_minimum': str(order),
            'intermediate_rank_minimum': str(intermediate),
            'final_rank_minimum': str(final),
            'allocation_lower_bounds': ['36/25', '8', '31'],
            'scope': 'Universal inequalities under10.263–10.264. Does not assert availability of general descent zeros.'}


def draw(data, output):
    """Float conversion only positions the certified rational bounds."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 11, 'mathtext.fontset': 'dejavusans'})
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(10.5, 9))
    fig.subplots_adjust(left=.28, right=.94, top=.89, bottom=.13, hspace=.7)
    y = [3, 2, 1, 0]
    upper = [Q(1, 20), Q(1, 4), Q(1, 4), Q(1, 2)]
    names = ['Any torus coordinate degree', 'Real output order',
             'Rank r', 'Real output order + rank r']
    ax.barh(y, [float(x) for x in upper], height=.48,
            color=['#497ba0', '#2a8785', '#a5793e', '#526576'])
    for yy, x, label in zip(y, upper, ['< 1/20', '< 1/4', '< 1/4', '< 1/2']):
        ax.text(float(x)+.025, yy, label, va='center', fontsize=10)
    ax.axvline(1, color='#b85f46', ls='--', label='Additive polynomial degree')
    ax.set(xlim=(0, 1.12), ylim=(-.65, 3.65), yticks=y, yticklabels=names,
           xlabel='Upper bound divided by the additive degree',
           title='The additive degree dominates every required threshold')
    ax.legend(loc='lower right', fontsize=9, frameon=True,
              facecolor='white', edgecolor='white', framealpha=1)
    bx.barh([2, 1, 0], [float(Q(v)) for v in data['allocation_lower_bounds']],
            height=.48, color=['#497ba0', '#2a8785', '#a5793e'])
    for yy, x, label in zip([2, 1, 0], [Q(36, 25), Q(8), Q(31)],
                             ['> 36/25', '> 8', '> 31']):
        bx.text(float(x)*1.12, yy, label, va='center', fontsize=10)
    bx.axvline(1, color='#b85f46', ls='--', label='Multiplicity threshold: 1')
    bx.set(xscale='log', xlim=(.5, 60), ylim=(-.65, 2.65),
           yticks=[2, 1, 0],
           yticklabels=['Allocation m = 0', 'Every allocation 1 ≤ m < r',
                        'Final allocation m = r'],
           xlabel='Certified lower bound for the multiplicity comparison ratio',
           title='Every allocation inequality has a strict uniform margin')
    bx.legend(loc='lower right', fontsize=9, frameon=False)
    for a in [ax, bx]:
        a.grid(axis='x', alpha=.2)
        a.set_axisbelow(True)
        a.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Uniform conditions for geometric rank reduction', fontsize=15, y=.97)
    fig.text(.5, .925, 'All ranks r ≥ 2 and original field cases; the special a* = 7/2 is retained',
             ha='center', fontsize=10)
    fig.text(.5, .055, 'Given the prepared zeros: r bases → m < r bases in the same field K',
             ha='center', fontsize=11)
    fig.text(.5, .018, 'Proved bounds, not parameter samples.  Theorem 10.100; Corollary 10.101; Solution 42.',
             ha='center', fontsize=9.5)
    fig.savefig(output, dpi=170, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    from pathlib import Path
    import json
    data = bounds()
    print(json.dumps(data, indent=2))
    draw(data, Path(__file__).with_name('geometric-stop-bounds.png'))

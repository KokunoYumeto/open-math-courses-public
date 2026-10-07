"""Certified nested integer-jet and first fractional-node budgets (CC0)."""
from fractions import Fraction
from math import factorial


def compute():
    from initial_scalar_budget import I, B, biglog, log, scalar_data, fineoptimum
    from pointwise_precision_budget import compute as integer_profile
    prior = integer_profile()
    base = scalar_data()
    vals = base['values']
    k, L = base['integers']['degree_factors']
    Da = k*L
    theta = I(Fraction(3, 2))/(1+I(Fraction(1, 4*10**26)))
    eta = I(Fraction(1231, 1500))
    Z = base['Z']
    radii = prior['R']
    orders = prior['T']
    target_order = orders[-1]
    cap = 780000
    multiplicities = [min(cap, t-target_order+1) for t in orders]
    ring_counts = [2*radii[0]+1] + [2*(b-a) for a, b in zip(radii, radii[1:])]
    total = sum(n*m for n, m in zip(ring_counts, multiplicities))
    assert total == 1286383318
    M0 = prior['beta_integer_upper']
    G0 = Da*theta+22*L
    available = 8/log(3)+G0/Z
    required = (total*theta+cap*M0)/Z
    gain = (total*theta-G0)/Z
    assert available.lo > required.hi
    next_real_radius = vals['S']/(eta**3)
    next_floor = next_real_radius.floor()
    X = next_floor+1
    R = X+2*k-1
    Omega = prior['Omega_integer_upper']
    u = fineoptimum(Omega, 3**k, target_order, Da, R)
    H = target_order-u
    def xlogx(x):
        return I(0) if x == 0 else x*biglog(x)
    entropy = xlogx(Da)-xlogx(u)-xlogx(Da-u)
    euler = I(0) if H == 0 else H*(1+biglog(1+I(Omega)/H))
    log_scalar = (Da-u)*biglog(R)-L*biglog(factorial(k))+entropy+u*k*log(3)+euler
    scalar = log_scalar/Z
    c1, c2 = I(Fraction('1.4494')), I(Fraction('1.75'))
    coefficient = I(Fraction(prior['uniform_initial_height'][1]))+base['g8']/2
    vp2_factorial = sum(k//(2**a) for a in range(1, 7))
    assert vp2_factorial == 47
    Xi_max = Da+L*vp2_factorial
    denominator = Xi_max*log(2)/Z
    torus = I(X)/(c1*c2*vals['S'])
    field_degree = 4
    arithmetic = field_degree*(coefficient+scalar+denominator+torus)/log(3)
    gap = gain-arithmetic
    assert gap.lo > 0
    return {
        'state': 'passed',
        'family': prior['family'],
        'radii': radii, 'available_orders': orders,
        'target_order': target_order, 'multiplicity_cap': cap,
        'multiplicities': multiplicities, 'ring_counts': ring_counts,
        'total_multiplicity': total, 'derivative_loss': M0,
        'next_real_radius': next_real_radius.outer_decimal(12),
        'next_floor': next_floor, 'fractional_numerator_radius': 2*X,
        'fractional_absolute_radius': X, 'scalar_factor_radius': R,
        'Omega_upper': Omega, 'peak_additive_order': u, 'peak_euler_order': H,
        'vp2_factorial': vp2_factorial, 'uniform_denominator_exponent': Xi_max,
        'ambient_root_field': 'Q(sqrt(-2),sqrt(-5)); individual values may belong to a proper subfield',
        'ambient_global_degree': field_degree, 'chosen_local_degree': 1,
        'intervals': {name: value.outer_decimal(12) for name, value in {
            'input_available': available, 'input_required': required,
            'input_gap': available-required, 'analytic_gain': gain,
            'scalar_log_over_Z': scalar, 'coefficient_log_over_Z': coefficient,
            'denominator_log_over_Z': denominator, 'torus_log_over_Z': torus,
            'arithmetic_upper': arithmetic, 'strict_gap': gap,
        }.items()},
        'scope': 'Original first fractional range |s|<=2(floor(eta^-3 S)+1), |t|<=floor(eta^3 T), for the whole permitted original rational coefficient family. Quartic global degree and denominator retained. General subsequent descent and final contradiction not asserted.',
    }


def draw(data, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.size': 11.5, 'mathtext.fontset': 'dejavusans'})
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(10.5, 9))
    fig.subplots_adjust(left=.23, right=.96, bottom=.08, top=.94, hspace=.5)
    r = data['radii']
    edges = [-r[3]-.5, -r[2]-.5, -r[1]-.5, -r[0]-.5,
             r[0]+.5, r[1]+.5, r[2]+.5, r[3]+.5]
    weights = data['multiplicities']
    levels = [weights[3], weights[2], weights[1], weights[0],
              weights[1], weights[2], weights[3]]
    ax.stairs(np.array(levels)/10**6, edges, fill=True, color='#487a9e', alpha=.85)
    ax.set(xlim=(-3200, 3200), ylim=(0, 1.16), xlabel='Integer node s',
           ylabel='Divided jets per node, in millions',
           title='Earlier integer steps retain larger inner jet ranges')
    for radius in r[:-1]:
        for sign in [-1, 1]:
            ax.axvline(sign*(radius+.5), color='white', linewidth=.8, alpha=.6)
    ax.set_xticks([-r[3], -r[2], -r[1], -r[0], 0, r[0], r[1], r[2], r[3]])
    ax.tick_params(axis='x', labelsize=9)
    rows = [f'{count} nodes with {mu:,} ' + ('jet' if mu == 1 else 'jets')
            for count, mu in zip(data['ring_counts'], weights)]
    ax.text(0, 1.1, '\n'.join(rows), ha='center', va='top', fontsize=10,
            bbox={'facecolor':'white', 'edgecolor':'#b6c4cf', 'alpha':.96})
    ax.grid(axis='y', alpha=.18)
    v = data['intervals']
    labels = ['Input required: upper bound', 'Input available: lower bound',
              'Analytic gain: lower bound', 'Arithmetic cost: upper bound']
    values = [float(v['input_required'][1]), float(v['input_available'][0]),
              float(v['analytic_gain'][0]), float(v['arithmetic_upper'][1])]
    exact_labels = [v['input_required'][1], v['input_available'][0],
                    v['analytic_gain'][0], v['arithmetic_upper'][1]]
    y = [3, 2, 1, 0]
    bx.barh(y, values, height=.55, color=['#b75d38', '#487a9e', '#253c58', '#298787'])
    for yy, value, label in zip(y, values, exact_labels):
        bx.text(value+.1, yy, label, va='center', fontsize=9)
    bx.set(xlim=(0, 10.0), ylim=(-.7, 3.7), yticks=y, yticklabels=labels,
           xlabel='Budget divided by Z',
           title='The first fractional range keeps the quartic global degree and denominator')
    bx.tick_params(axis='y', labelsize=9)
    bx.grid(axis='x', alpha=.18)
    fig.text(.13, .015, 'Input margin > 0.049635; zero-forcing gap > 2.577685.  Lemmas 10.91/10.94 and Theorem 10.95.',
             fontsize=10)
    fig.savefig(output, dpi=175, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    from pathlib import Path
    import json
    data = compute()
    print(json.dumps(data, indent=2))
    draw(data, Path(__file__).with_name('nested-integer-jets.png'))

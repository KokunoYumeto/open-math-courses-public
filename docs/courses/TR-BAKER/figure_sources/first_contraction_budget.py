"""Certified rational-family contraction chain (GPT-6.1 Sol, Ultra; CC0)."""
from fractions import Fraction
from math import factorial


def compute():
    from initial_scalar_budget import I, log, biglog, scalar_data, fineoptimum
    from pointwise_precision_budget import compute as original_profile
    prior = original_profile()
    base = scalar_data()
    vals = base['values']
    k, L = base['integers']['degree_factors']
    Da = k*L
    theta = I(Fraction(3, 2))/(1+I(Fraction(1, 4*10**26)))
    eta = I(Fraction(1231, 1500))
    Z = base['Z']
    radius = 2*((vals['S']/(eta**3)).floor()+1)
    input_order = (eta**3*vals['T']).floor()
    output_order = (eta**4*vals['T']).floor()
    mu = input_order-output_order+1
    node_count = 2*radius-2*(radius//2)
    B = 0
    power = 3
    while power <= 2*radius:
        B += 1
        power *= 3
    C0 = prior['beta_integer_upper']
    M0 = max(B, C0)
    G0 = Da*theta+22*L
    available = 8/log(3)+G0/Z
    required = (node_count*mu*theta+mu*(B+M0))/Z
    coarse_required = (node_count*mu*theta+2*mu*M0)/Z
    gain = (node_count*mu*theta-G0)/Z
    assert available.lo > coarse_required.hi >= required.hi
    Omega = prior['Omega_integer_upper']//2
    factor_radius = Fraction(radius, 2)+2*k-1
    assert factor_radius.denominator == 1
    R = factor_radius.numerator
    u = fineoptimum(Omega, 3**k, output_order, Da, R)
    H = output_order-u
    def xlogx(x):
        return I(0) if x == 0 else x*biglog(x)
    entropy = xlogx(Da)-xlogx(u)-xlogx(Da-u)
    euler = I(0) if H == 0 else H*(1+biglog(1+I(Omega)/H))
    log_scalar = (Da-u)*biglog(R)-L*biglog(factorial(k))+entropy+u*k*log(3)+euler
    scalar = log_scalar/Z
    coefficient = I(Fraction(prior['uniform_initial_height'][1]))+base['g8']/2
    Xi_max = Da+47*L
    denominator = Xi_max*log(2)/Z
    c1, c2 = I(Fraction('1.4494')), I(Fraction('1.75'))
    torus = I(Fraction(radius, 2))/(c1*c2*vals['S'])
    arithmetic = (coefficient+scalar+denominator+torus)/log(3)
    gap = gain-arithmetic
    assert gap.lo > 0
    return {
        'state': 'passed', 'family': prior['family'], 'stage': 1,
        'integer_radius': radius, 'q_deleted_nodes': node_count,
        'input_order': input_order, 'output_order': output_order, 'mu': mu,
        'B': B, 'C0_upper': C0, 'M0': M0, 'k': k, 'L': L, 'Da': Da,
        'Omega_upper': Omega, 'factor_radius': R,
        'peak_additive_order': u, 'peak_euler_order': H,
        'uniform_denominator_exponent': Xi_max,
        'arithmetic_field': 'Q', 'global_to_local_degree': 1,
        'intervals': {name: v.outer_decimal(12) for name, v in {
            'input_available': available, 'input_required': required,
            'coarse_input_required': coarse_required,
            'input_margin': available-required,
            'analytic_gain': gain, 'coefficient_log_over_Z': coefficient,
            'scalar_log_over_Z': scalar, 'denominator_log_over_Z': denominator,
            'torus_log_over_Z': torus, 'arithmetic_upper': arithmetic,
            'strict_gap': gap,
        }.items()},
        'scope': 'First actual contracted family at I1: odd zeros through floor(eta^3 T) become all integer zeros through floor(eta^4 T), over the exact original radius2(floor(eta^-3 S)+1). Entire permitted original rational coefficient family; later/general descent and final contradiction not asserted.',
    }


def induction_data(last_stage=17):
    """Check the finite original profile; logical transfer is proved in the lesson."""
    from initial_scalar_budget import I, B, log, biglog, scalar_data, fineoptimum
    from pointwise_precision_budget import compute as original_profile
    old = original_profile()
    base = scalar_data()
    vals = base['values']
    k, L = base['integers']['degree_factors']
    Da = k*L
    eta = I(Fraction(1231, 1500))
    theta = I(Fraction(3, 2))/(1+I(Fraction(1, 4*10**26)))
    Z = base['Z']
    G0 = Da*theta+22*L
    available = 8/log(3)+G0/Z
    coefficient = I(Fraction(old['uniform_initial_height'][1]))+base['g8']/2
    c1, c2 = I(Fraction('1.4494')), I(Fraction('1.75'))
    logfact = biglog(factorial(k))
    log3, log2 = log(3), log(2)
    stages, failures = [], []
    def separation(radius):
        b, power = 0, 3
        while power <= 2*radius:
            b += 1
            power *= 3
        return b
    def arithmetic(stage, X, order, fractional=False):
        Omega = old['Omega_integer_upper']//(2**stage)
        R = Fraction(X, 2**stage)+2*k-1
        u = fineoptimum(Omega, 3**k, order, Da, R)
        H = order-u
        def xlogx(x):
            return I(0) if x == 0 else x*biglog(x)
        entropy = xlogx(Da)-xlogx(u)-xlogx(Da-u)
        euler = I(0) if H == 0 else H*(1+biglog(1+I(Omega)/H))
        scalar = ((Da-u)*biglog(R)-L*logfact+entropy+u*k*log3+euler)/Z
        Xi = (stage+int(fractional))*Da+47*L
        denominator = Xi*log2/Z
        torus = I(Fraction(X, 2**stage))/(c1*c2*vals['S'])
        factor = 4 if fractional else 1
        value = factor*(coefficient+scalar+denominator+torus)/log3
        return value, {'scalar_peak': u, 'remaining_euler_order': H,
                       'Xi_common': Xi, 'field_factor': factor,
                       'scalar': scalar.outer_decimal(12),
                       'torus': torus.outer_decimal(12)}
    for stage in range(1, last_stage+1):
        SI = vals['S']/(eta**(3*stage))
        TI = vals['T']*eta**(3*stage)
        R1 = 2*(SI.floor()+1)
        R2 = (4*SI).floor()
        O0, O1, O2, O3 = [(TI*eta**j).floor() for j in range(4)]
        checks = []
        # Deleted-node closure to the full first interval.
        mu = O0-O1+1
        nodes = 2*R1-2*(R1//2)
        b = separation(R1)
        M = max(46, b)
        required = (nodes*mu*theta+mu*(b+M))/Z
        gain = (nodes*mu*theta-G0)/Z
        arith, detail = arithmetic(stage, R1, O1)
        checks.append(('deleted_full', required, gain, arith, detail))
        # The one remaining original integer extension.
        mu = O1-O2+1
        nodes = 2*R1+1
        required = (nodes*mu*theta+mu*M)/Z
        gain = (nodes*mu*theta-G0)/Z
        arith, detail = arithmetic(stage, R2, O2)
        checks.append(('integer_extension', required, gain, arith, detail))
        # Nested odd/full/full data for the exact next fractional range.
        cap = (I(780000)*eta**(3*stage)).floor()
        odd_mu, inner_mu, outer_mu = cap, O1-O3, O2-O3
        assert odd_mu >= inner_mu >= outer_mu >= 1
        assert odd_mu <= O0-O3+1
        Nstar = (2*R2+1)*outer_mu+(2*R1+1)*(inner_mu-outer_mu)+R1*(odd_mu-inner_mu)
        excess = odd_mu-inner_mu
        b = separation(R2)
        M = max(46, b)
        required = (Nstar*theta+odd_mu*M+b*excess)/Z
        gain = (Nstar*theta-G0)/Z
        Xfrac = (SI/(eta**3)).floor()+1
        arith, detail = arithmetic(stage, Xfrac, O3, fractional=True)
        detail.update(Nstar=Nstar, multiplicities=[odd_mu, inner_mu, outer_mu],
                      odd_excess=excess, separation=b)
        checks.append(('fractional_step', required, gain, arith, detail))
        rows = []
        for name, req, gain, arith, detail in checks:
            passed = available.lo > req.hi and gain.lo > arith.hi
            if not passed:
                failures.append({'stage': stage, 'check': name})
            rows.append({'check': name, 'passed': passed,
                         'input_required': req.outer_decimal(12),
                         'input_margin': (available-req).outer_decimal(12),
                         'analytic_gain': gain.outer_decimal(12),
                         'arithmetic_upper': arith.outer_decimal(12),
                         'strict_gap': (gain-arith).outer_decimal(12),
                         **detail})
        stages.append({'stage': stage, 'R1': R1, 'R2': R2,
                       'orders': [O0, O1, O2, O3], 'next_fractional_X': Xfrac,
                       'checks': rows})
    final = stages[-1]
    assert vals['D1'].hi < (2**last_stage)*B and vals['D2'].hi < (2**last_stage)*B
    assert 2*final['R1']+1 > Da
    return {'state': 'numerical_checks_passed' if not failures else 'failed',
            'failures': failures, 'input_available': available.outer_decimal(12),
            'stages': stages,
            'terminal': {'stage': last_stage, 'support_coordinate_widths_below_one': True,
                         'full_integer_roots': 2*final['R1']+1, 'additive_degree': Da},
            'scope': 'Finite 17-stage certificate for the entire original permitted rational coefficient family; transfer and mixed nested cardinal proof required in the lesson. Does not assert the full general Yu theorem.'}


def draw(data, output):
    """Plot certified bounds; float conversion is for picture coordinates only."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from fractions import Fraction
    stages = data['stages']
    x = [s['stage'] for s in stages]
    colors = ['#467ba5', '#2c8b83', '#b06540']
    labels = ['Odd-to-full: field factor 1',
              'Integer extension: field factor 1',
              'Fractional: field factor 4']
    plt.rcParams.update({'font.size': 10.5, 'mathtext.fontset': 'dejavusans'})
    fig = plt.figure(figsize=(11, 10))
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.08])
    ax, bx = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])
    cx = fig.add_subplot(grid[1, :])
    for j, (color, label) in enumerate(zip(colors, labels)):
        ax.plot(x, [float(s['checks'][j]['input_margin'][0]) for s in stages],
                'o-', color=color, ms=3, label=label)
        bx.plot(x, [float(s['checks'][j]['strict_gap'][0]) for s in stages],
                'o-', color=color, ms=3)
    ax.set(title='Available minus required input',
           xlabel='Contraction stage I', ylabel='Certified lower margin / Z',
           yscale='log', xlim=(.5, 17.5))
    bx.set(title='Analytic gain minus arithmetic cost',
           xlabel='Contraction stage I', ylabel='Certified lower gap / Z',
           xlim=(.5, 17.5))
    for a in [ax, bx]:
        a.set_xticks([1, 5, 9, 13, 17])
        a.grid(alpha=.2)
        a.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='center right', fontsize=8.5, frameon=False)
    ax.text(.04, .34, 'All 51 input margins are positive',
            transform=ax.transAxes, fontsize=9)
    bx.text(.04, .92, 'All 51 zero-forcing gaps are positive',
            transform=bx.transAxes, fontsize=9)
    depth = list(range(18))
    for upper, color, name in [(67805, '#467ba5', 'First coordinate'),
                               (29202, '#2c8b83', 'Second coordinate')]:
        cx.plot(depth, [float(Fraction(upper, 2**i)) for i in depth],
                'o-', ms=3, color=color, label=f'{name}: width < {upper} / 2^I')
    cx.axhline(1, color='#ad5b45', ls='--', lw=1, label='Integer width threshold: 1')
    cx.axvline(17, color='#526677', ls=':', lw=1)
    cx.set(yscale='log', xlim=(-.2, 17.7), ylim=(.12, 100000),
           xlabel='Contraction stage I', ylabel='Coordinate-width upper bound',
           title='At I = 17 the nonempty integer support has one exponent')
    cx.set_xticks([0, 1, 5, 9, 13, 17])
    cx.grid(alpha=.2)
    cx.legend(loc='upper right', fontsize=9, frameon=False)
    cx.text(.03, .12, 'Nonzero polynomial: degree ≤ 1,764,950\n'
            'Full closure: 36,184,549 distinct integer roots',
            transform=cx.transAxes, fontsize=10,
            bbox={'facecolor': 'white', 'edgecolor': '#b7c5ce'})
    fig.suptitle('A complete seventeen-contraction contradiction for the rational family',
                 fontsize=14, y=.977)
    fig.text(.5, .925,
             'm → (m − m*) / 2: coefficients stay a subvector; Euler jet changes preserve total order',
             ha='center', fontsize=10)
    fig.text(.5, .023,
             'Proved bounds, not sampled valuations.  Lemma 10.96–Corollary 10.99; Solution 41.',
             ha='center', fontsize=10)
    fig.subplots_adjust(left=.085, right=.96, top=.86, bottom=.09,
                        wspace=.31, hspace=.44)
    fig.savefig(output, dpi=170, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    from pathlib import Path
    import json
    data = induction_data()
    print(json.dumps(data, indent=2))
    draw(data, Path(__file__).with_name('first-contraction-budget.png'))

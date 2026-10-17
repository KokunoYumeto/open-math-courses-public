"""Exact parameter certificate for TR-BAKER 10.184--10.187 and Figure 10.54.

CC0. Fractions, explicit series remainders and outward rounding are used
for all certified quantities. Plot coordinates are illustrations only.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb, gcd
import json

Q = 10**36


class Interval:
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        self.lo = F((lo * Q).numerator // (lo * Q).denominator, Q)
        a = hi * Q
        self.hi = F(-((-a.numerator) // a.denominator), Q)
        assert self.lo <= self.hi

    @staticmethod
    def convert(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, x):
        x = self.convert(x)
        return Interval(self.lo + x.lo, self.hi + x.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, x):
        return self + -self.convert(x)

    def __rsub__(self, x):
        return self.convert(x) - self

    def __mul__(self, x):
        x = self.convert(x)
        vals = [a*b for a in [self.lo, self.hi] for b in [x.lo, x.hi]]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.convert(x)
        assert not x.lo <= 0 <= x.hi
        return self * Interval(1/x.hi, 1/x.lo)

    def __rtruediv__(self, x):
        return self.convert(x) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0 and self.lo >= 0
        return Interval(self.lo**n, self.hi**n)

    def floor(self):
        a, b = self.lo.numerator//self.lo.denominator, self.hi.numerator//self.hi.denominator
        assert a == b, (a, b)
        return a

    def record(self):
        return [str(self.lo), str(self.hi)]


def log_ratio(x):
    x = F(x)
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    total = 2*sum(z**(2*j+1)/F(2*j+1) for j in range(64))
    tail = 2*z**129/(129*(1-z*z))
    return Interval(total, total+tail)


def log_integer(n):
    assert n >= 1
    k = n.bit_length()-1
    return k*log_ratio(2)+log_ratio(F(n, 2**k))


def exp_one():
    total = sum(F(1, factorial(j)) for j in range(65))
    return Interval(total, total+F(1, factorial(65))/(1-F(1, 66)))


def prefactors():
    rows = [
        ('I.1', F(384,5), F(12133,10000), F(7,10), F(6,5), 14, 2, 1438),
        ('I.2', F(192,5), F(12133,10000), F(7,10), F(6,5), 14, 2, 648),
        ('II', F(384,5), F(12133,10000), F(7,10), F(6,5), 14, 2, 690),
        ('III.1', F(512,5), F(1641,1250), F(7,10), F(8,5), 14, 1, 495),
        ('III.2', F(256,5), F(1641,1250), F(7,10), F(8,5), 14, 1, 557),
        ('IV', F(192), F(13701,10000), F(7,10), 3, 14, 2, 2418),
        ('V', F(90), F(147,125), F(41,50), F(3,5), 6, 2, 406),
    ]
    answer = []
    integer_caps = [627, 631, 627, 452, 454, 1763, 343]
    for (case, g, zeta1, c1, c3, c4, ratio, target), integer_cap in zip(rows, integer_caps):
        q = 3 if case == 'V' else 2
        cap = F(101,100)*(2+1/g)*zeta1*F(27,10)*c1*c3*c4*q*q*ratio*(1+F(1,10**26))
        gap = target-cap
        assert gap > 0 and cap < integer_cap < target
        answer.append({'case': case, 'gS_lower': str(g), 'prefactor_upper': str(cap),
                       'target': str(target), 'positive_gap': str(gap), 'strict_integer_cap': integer_cap,
                       'III_common_factor': '1/theta' if case.startswith('III') else '1'})
    assert F(82944,29) > 909 and F(8448,145)-58 == F(38,145)
    return answer


def worked_example():
    r = n = 4
    t, ee = log_integer(3), exp_one()
    logs = [log_integer(a) for a in [2, 5, 7, 11]]
    omega = Interval(1)
    for item in logs:
        omega *= item
    c0, c1, c3, c4 = F(27,10), F(7,10), F(6,5), 14
    zeta2 = F(5101,5000)
    c2 = F(7,4)/zeta2
    tau = F(1, 8*10**26)
    # x0 is between2and3; m=2 follows from 3>(9/7)^4.
    x0 = 4/t-F(3,2)
    assert 2 < x0.lo <= x0.hi < 3 and 3 > F(9,7)**4
    m, N = 2, F(7,2)/(1+tau)
    A = 4+log_integer(5)
    Rsecond = (ee/4)**4*t**5
    assert Rsecond.hi < 3
    R = 3
    h = 150
    gS = c3*2*25
    KS = F(101,100)*(2+1/gS)
    S = c3*2*5*h/t
    D = KS*c0*c1*c4*(N/F(3,2))*(zeta2*c2*2*ee*3)**4*F(5**4,factorial(4))*omega*F(1,2)*R*A*(1+tau)**4
    T = 2*5*D/(c1*N*t)
    k = h
    X = S*D/(c1*c4*(N/F(3,2))*A*k)
    L = X.floor()+1
    Da = k*L
    widths = [D/(c1*c2*4*3*weight) for weight in logs]
    sides = [a.floor()+1 for a in widths]
    # The deep units are -2^3,-5^3,7^3,-11^3.
    units = [-8, -125, 343, -1331]
    residues = [((u-1)//9) % 9 for u in units]
    assert residues == [8, 4, 2, 5]
    counts = [1]+[0]*8
    for length, coefficient in zip(sides, residues):
        bins = [0]*9
        for residue in range(9):
            bins[(coefficient*residue) % 9] += length//9+(residue < length % 9)
        nxt = [0]*9
        for a in range(9):
            for b in range(9):
                nxt[(a+b) % 9] += counts[a]*bins[b]
        counts = nxt
    assert sum(counts) == sides[0]*sides[1]*sides[2]*sides[3]
    phase = max(range(9), key=lambda a: counts[a])
    reference = [(pow(8, -1, 9)*phase) % 9, 0, 0, 0]
    assert all(reference[i] < sides[i] for i in range(4))
    s0, t0 = S.floor(), T.floor()
    Nc = k*L*counts[phase]
    M = (2*s0+1)*comb(t0+4, 4)
    assert 10*Nc > 27*M
    assert T.lo > 101*16 and X.lo > 58
    assert (Interval(Da)/(S*D/(c1*c4*(N/F(3,2))*A))).hi < F(59,58)
    # Verify the first full-node interpolation input budget for unit b_n.
    mu = (T/10).floor()+1
    B, power = 0, 1
    while power*3 <= 2*s0:
        power *= 3
        B += 1
    C0 = 0
    power = 1
    while power*3 <= k:
        power *= 3
        C0 += 1
    U = 2**5*S*D/t
    budget_gap = 1+U+Da*(N+F(1,2))-((2*s0+1)*mu*N+mu*max(B,C0))
    assert budget_gap.lo > 10**15
    assert (1+U-N-F(1,2)).lo > 0
    return {
        'rank': r, 'original_n': n, 'prime':3,'field':'Q','bases':[2,5,7,11],
        'q':2,'P':3,'ramification':1,'residue_degree':1,'theta':'3/2','J':1,'delta':1,
        'h':150,'m':m,'analytic_N':str(N),'phase_count':1,'unit_quotient_order':9,
        'mod81_unit_coefficients':residues,'side_integer_counts':sides,
        'mod9_class_counts':counts,'selected_class':phase,'reference':reference,
        'k':k,'L':L,'polynomial_degree':Da,'integer_node_radius':s0,'integer_jet_budget':t0,
        'columns':Nc,'full_rows':M,'positive_column_gap_10Nc_minus_27M':10*Nc-27*M,
        'S_interval':S.record(),'D_interval':D.record(),'T_interval':T.record(),'X_interval':X.record(),
        'R_second_entry_interval':Rsecond.record(),'R_selected':R,
        'first_step_mu':mu,'node_separation_B':B,'ordinary_jet_loss_C0':C0,
        'first_step_input_budget_gap_interval':budget_gap.record(),
        'finite_scope':'Exact support counts, all stable floors and first local input budget. Full global zero induction is not inferred.'
    }


def figure(rows, example, target):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(11,4.6), layout='constrained')
    ax = axes[0]
    labels = [x['case'] for x in rows]
    values = [float(F(x['prefactor_upper'])/F(x['target'])) for x in rows]
    bars = ax.bar(labels, values, color='#167d8d')
    ax.axhline(1, color='#b33e35', linestyle='--', label='Stated coefficient')
    for bar, v in zip(bars,values):
        ax.text(bar.get_x()+bar.get_width()/2,v+.025,f'{v:.3f}',ha='center',fontsize=9)
    ax.set(ylim=(0,1.16),ylabel='Proved prefactor upper bound / target',title='Every field case; all admissible ranks')
    ax.tick_params(axis='x',labelrotation=25)
    ax.legend(loc='lower right',fontsize=9)
    ax = axes[1]
    ranks = list(range(3,10))
    lower = [float(F(12,29)*(r+1)*12**r/F(r*r)) for r in ranks]
    ax.plot(ranks,lower,marker='o',color='#167d8d',label=r'Proved lower bound for $T/r^2$')
    ax.axhline(101,color='#b33e35',linestyle='--',label='Binomial rounding threshold: 101')
    ax.set(yscale='log',xlabel='Rank r',ylabel=r'$T/r^2$',title='Integer floors retain the row surplus')
    ax.legend(loc='upper left',fontsize=9)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False)
        ax.grid(alpha=.15)
        ax.set_axisbelow(True)
    fig.savefig(target,dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    rows, example = prefactors(), worked_example()
    data = {'prefactor_rows':rows,'worked_example':example,'rounding_denominator':str(Q),
            'proof_scope':'All-rank proofs in Theorems10.184–10.187; finite calculation checks rational endpoints and the example.'}
    (here/'yu-second-scale-certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    figure(rows,example,here/'yu-second-scale.png')
    print(json.dumps({k:example[k] for k in ['m','k','L','polynomial_degree','integer_node_radius',
          'integer_jet_budget','columns','full_rows','first_step_mu','node_separation_B','ordinary_jet_loss_C0']}))

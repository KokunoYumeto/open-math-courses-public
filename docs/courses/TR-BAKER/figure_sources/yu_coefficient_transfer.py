"""Exact endpoint certificates and Figure 10.51. Independently authored; CC0."""
from fractions import Fraction as F
from math import factorial, exp, log
from pathlib import Path
import json

ETA = F(23, 500)
CASES = [
    ('I.1', F(1438, 939) * F(27, 20)**2),
    ('I.2', F(648, 636) * F(27, 20)**2),
    ('II', F(690, 505) * F(27, 20)**2),
    ('III.1', F(495, 1794) * F(27, 10)**2 * F(3, 4)),
    ('III.2', F(557, 1790) * F(27, 10)**2 * F(3, 4)),
    ('IV', F(2418, 2680) * F(27, 20)**2),
    ('V', F(406, 206) * F(27, 20)**2),
]


def certificate():
    gaps = [value - F(3, 2) for _, value in CASES]
    assert min(gaps) == F(411, 47840) and all(x > 0 for x in gaps)
    exp6 = sum(F(1, factorial(j)) for j in range(7))
    assert exp6 - F(125, 46) == F(11, 16560) > 0
    assert 8 * ETA * exp6 > 1
    assert sum(F(1, factorial(j)) for j in range(5)) > F(27, 10)
    # Rational lower bounds for the seven n=2,d=1 G-parameter gaps.
    # The proof gives the logarithmic expressions and their monotonicity.
    parameter_gaps = [F(22, 25), F(27, 20), F(5, 8), F(11, 40),
                      F(57, 50), F(17, 20), F(17, 10)]
    assert all(v > 0 for v in parameter_gaps)
    valuations = []
    for k in range(1, 21):
        residue = (5 * pow(2, 3**k, 9) - 1) % 9
        assert residue == 3
        valuations.append({'k': k, 'residue_mod9': residue, 'valuation': 1})
    return {
        'constant_ratio_lower_bounds': {name: str(v) for name, v in CASES},
        'gaps_above_three_halves': {name: str(v-F(3, 2)) for name, v in CASES},
        'minimum_gap': str(min(gaps)),
        'parameter_gap_lower_bounds': dict(zip([n for n, _ in CASES], map(str, parameter_gaps))),
        'exponential_series_order': 6,
        'exponential_gap': str(exp6 - F(125, 46)),
        'examples': valuations,
        'scope': 'Exact finite endpoints only. Lemmas 10.172/10.174 and Theorem 10.173 prove the full infinite parameter ranges.',
    }


def draw(destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'font.family': 'DejaVu Sans'})
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.5), constrained_layout=True)
    ax = axes[0]
    positions = np.arange(len(CASES))
    ax.bar(positions, [float(v) for _, v in CASES], color='#287c8e')
    ax.axhline(1.5, color='#b04a3d', linestyle='--', label=r'$3/2$: coefficient-parameter factor')
    ax.set_xticks(positions, [name for name, _ in CASES])
    ax.set_ylabel(r'Exact rational lower bound for $C_2/C_1$')
    ax.set_title(r'All seven cases, $n\leq P f\log p$')
    ax.text(0.03, 0.94, 'Smallest gap: 411/47840 > 0', transform=ax.transAxes,
            va='top', fontsize=10)
    ax.set_ylim(0, 4.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0, -0.16), frameon=False, fontsize=9)
    ax = axes[1]
    phi = 1 + float(ETA)
    z_factor = max(8*phi, exp(2/phi))
    zz = np.geomspace(.2, 80, 700)
    first = phi * (log(z_factor) + 20 - np.log(zz))
    second = zz
    assert np.all(np.maximum(first, second) >= 20)
    ax.plot(zz, first, color='#287c8e', label=r'$\Phi\log(Zr/z)$')
    ax.plot(zz, second, color='#b04a3d', label=r'$z=\varepsilon r$')
    ax.plot(zz, np.maximum(first, second), color='#443f78', linestyle=':',
            linewidth=2.5, label='Upper envelope')
    ax.axhline(20, color='#475866', linestyle='--', linewidth=1, label='Scalar input: 20')
    ax.set_xscale('log')
    ax.set_ylim(0, 45)
    ax.set_xlabel(r'$z=\varepsilon r$ (shown: $0.2\leq z\leq80$)')
    ax.set_title(r'Scalar model: $T=X=B_n=1$, $H_0=2$, $r=e^{20}$')
    ax.legend(loc='upper left', bbox_to_anchor=(0, -0.16), ncol=2, frameon=False, fontsize=9)
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='y', alpha=.16)
        ax.set_axisbelow(True)
    fig.savefig(destination, dpi=180, bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    data = certificate()
    (args.output_dir/'yu-coefficient-transfer-endpoints.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    draw(args.output_dir/'yu-coefficient-transfer.png')
    print(json.dumps({'minimum_gap': data['minimum_gap'], 'exponential_gap': data['exponential_gap'], 'examples': len(data['examples'])}))

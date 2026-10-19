"""Exact nearest-power distances for the finite certificate in Theorem 11.4. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    ns = list(range(4, 20))
    below, above = [], []
    for n in ns:
        value = 3**n
        k = value.bit_length() - 1
        below.append(value - 2**k)
        above.append(2**(k+1) - value)
    fig, ax = plt.subplots(figsize=(10.8, 5.8), layout='constrained')
    fig.patch.set_facecolor('#fbfaf7')
    ax.set_facecolor('#fbfaf7')
    ax.plot(ns, below, 'o-', color='#1b5e8c', label=r'$3^n-2^k$ (nearest power below)', lw=1.4)
    ax.plot(ns, above, 's--', color='#b06124', label=r'$2^{k+1}-3^n$ (nearest power above)', lw=1.4)
    ax.axhline(20, color='#9d2334', lw=1.5, label='Allowed distance: 20')
    ax.annotate(r'$(m,n)=(6,4)$: 17', (4,17), xytext=(6.2,3.2),
                arrowprops={'arrowstyle':'->','color':'#1b5e8c'}, color='#1b5e8c', fontsize=11)
    ax.annotate(r'$(m,n)=(8,5)$: 13', (5,13), xytext=(10.3,3.2),
                arrowprops={'arrowstyle':'->','color':'#b06124'}, color='#b06124', fontsize=11)
    ax.set_yscale('log')
    ax.set_ylim(1.5,2e9)
    ax.set_xticks(ns)
    ax.set_xlabel(r'Exponent $n$ of three',fontsize=12)
    ax.set_ylabel('Exact integer distance (logarithmic scale)',fontsize=12)
    ax.set_title(r'Only two distances survive the proved reduction to $4\leq n\leq19$',fontsize=14,pad=14)
    ax.grid(axis='y',alpha=.18)
    ax.legend(loc='upper left',fontsize=10)
    for spine in ('top','right'):ax.spines[spine].set_visible(False)
    # The build recipe keeps this source next to other figure sources.
    base=Path(__file__).resolve().parent
    target=base.parent/'figures/powers-gap-certificate.png' if base.name=='figure_sources' else base/'powers-gap-certificate.png'
    fig.savefig(target,dpi=160)
    plt.close(fig)
    print(target)


if __name__=='__main__':main()

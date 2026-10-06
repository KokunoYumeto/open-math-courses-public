"""Exact expansion bounds and centered row weights. Public domain, CC0.

Proof locators: Lesson 10, Lemmas 10.2 and 10.5, Theorem 10.11,
equations (10.14) and (10.43). Top: proved valuation bounds and exact row
weights. Bottom: calculated height budgets, not measured valuations.
Run from any directory; the PNG is written beside the course's other figures.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    course = Path(__file__).resolve().parents[1]
    output = course / 'figures' / 'padic-determinant-orders.png'
    output.parent.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig = plt.figure(figsize=(11.6, 9.2))
    grid = fig.add_gridspec(2, 2, height_ratios=[1.1, 1])
    axes = [fig.add_subplot(grid[0,0]), fig.add_subplot(grid[0,1]),
            fig.add_subplot(grid[1,:])]

    n = np.arange(13)
    loss = 12 * np.log(12) / np.log(3)
    lower = 54 + (12 - n) ** 2 / 2 - loss
    axes[0].plot(n, lower, 'o-', color='#245b90', linewidth=2)
    axes[0].axhline(54-loss, color='#aa4c23', linestyle='--', linewidth=1.6)
    axes[0].set(xlabel='Number n of ordinary rows (out of 12)',
                ylabel='Lower bound for a summand valuation',
                title='Expansion: errors gain precision')
    axes[0].set_xticks(np.arange(0, 13, 2))
    axes[0].grid(alpha=.17)
    axes[0].set_title('Expansion: errors gain precision\n' +
                      r'$54+(12-n)^2/2-12\ln(12)/\ln(3)$', fontsize=11)
    axes[0].annotate('Minimum at n = 12', xy=(12, 54-loss),
                     xytext=(4.8, 48), arrowprops={'arrowstyle': '->', 'color': '#aa4c23'},
                     color='#aa4c23')
    axes[0].text(.04, .06, 'K = 3, L = 4, p = 3, e = 1, t = 0',
                 transform=axes[0].transAxes, fontsize=10)

    labels = np.repeat(np.arange(4), 2)
    weights = labels - 1.5
    selected = np.where(weights > 0, 2, 0)
    axes[1].bar(np.arange(8), weights,
                color=np.where(weights > 0, '#245b90', '#b97059'), width=.72)
    axes[1].axhline(0, color='#444444', linewidth=1)
    axes[1].set_xticks(np.arange(8), [str(x) for x in labels])
    axes[1].set(xlabel='Row label l (each occurs K = 2 times)',
                ylabel='Centered row weight l − 3/2',
                title='Centering: select the positive weights', ylim=(-2.1, 2.35))
    for j, weight in enumerate(weights):
        axes[1].text(j, weight + (.14 if weight > 0 else -.3),
                     'r = ' + str(selected[j]), ha='center', fontsize=10)
    axes[1].text(.5, .93, r'$\sum (l_i-3/2)r_i=8=NL(R-1)/8$',
                 transform=axes[1].transAxes, ha='center', fontsize=11)
    axes[1].text(.5, .035, 'N = 8, L = 4, R = 3;  0 ≤ r ≤ 2',
                 transform=axes[1].transAxes, ha='center', fontsize=10)

    m = np.arange(1, 13)
    integers = np.array([5**int(j) for j in m], dtype=np.float64)
    product = np.log(1+integers)*np.log(1+2*integers)/np.log(5)**2
    axes[2].plot(m, product, 'o-', color='#245b90', linewidth=2,
                 label=r'Height product: $h_1h_2/(\ln 5)^2$')
    axes[2].plot(m, product/m, 's-', color='#aa4c23', linewidth=2,
                 label=r'With precision $E=m$: $h_1h_2/(m(\ln 5)^2)$')
    axes[2].set(xlabel='m (both bases are 5-adically close to 1)',
                ylabel='Normalized height budget',
                title='Deep units: precision removes one power of m')
    axes[2].set_xticks(m)
    axes[2].grid(alpha=.17)
    axes[2].legend(loc='upper left', framealpha=.95)
    axes[2].text(.02,.55, r'$h_1=\ln(1+5^m),\quad h_2=\ln(1+2\cdot5^m)$',
                 transform=axes[2].transAxes, fontsize=11)
    fig.tight_layout(pad=2)
    fig.savefig(output, dpi=180, facecolor='white')
    plt.close(fig)
    print(output)


if __name__ == '__main__':
    main()

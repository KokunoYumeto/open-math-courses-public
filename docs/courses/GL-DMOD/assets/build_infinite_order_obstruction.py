"""Reproduce Figure IK.2 from its exact coefficient and rational sample data.

The samples illustrate the complete local proof in section IK.9. They do
not assert a distribution boundary value or infer a theorem from a plot.
"""
from pathlib import Path
import argparse
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def build(outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'svg.hashsalt': 'canonical-infinite-order-obstruction-IK30-IK33',
        'axes.spines.top': False, 'axes.spines.right': False,
    })
    data = {
        'proof_locator': 'IK.9, equations IK.30-IK.33',
        'normal_orientation': 'w = s - t',
        'operator_coefficient': 'a_j = 1/(j!)^2',
        'kernel': 'K(w) = exp(1/w)/(2*pi*i*w)',
        'positive_real_slice': True,
        'kernel_plot_quantity': 'log10(abs(2*pi*K(1/k))) = (k+log(k))/log(10)',
        'finite_partial_degrees': [8, 32],
        'coefficients': [
            {'j': j, 'a_j': {'numerator': 1, 'denominator': math.factorial(j)**2},
             'j_factorial_a_j': {'numerator': 1, 'denominator': math.factorial(j)}}
            for j in range(13)
        ],
        'kernel_samples': [
            {'k': k, 'w': {'numerator': 1, 'denominator': k},
             'exact_log10_abs_2pi_K': '(k+log(k))/log(10)',
             'sample_log10_abs_2pi_K': (k + math.log(k))/math.log(10)}
            for k in range(2, 41)
        ],
        'monomial_evaluations': [
            {'m': m, 'full': {'numerator': 1, 'denominator': math.factorial(m)},
             'partial_order_3': {'numerator': 1 if m <= 3 else 0,
                                 'denominator': math.factorial(m) if m <= 3 else 1}}
            for m in range(9)
        ],
        'source_normalization': 'Free HolIII III.2, printed p.883; full proof local.',
        'limitations': 'Real numerical kernel samples; no distribution limit is claimed.',
    }
    (outdir/'infinite-order-obstruction-data.json').write_text(
        json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.4),
                             gridspec_kw={'width_ratios': [1.0, 1.25, 1.12]})
    fig.subplots_adjust(left=.055, right=.985, top=.73, bottom=.25, wspace=.40)
    fig.suptitle('An actual infinite positive head needs a holomorphic kernel class',
                 x=.5, y=.955, fontsize=17, fontweight='bold')
    fig.text(.5, .845, r'$P=\sum_{j\geq0}\partial_t^j/(j!)^2$'
             '    |    '
             r'$K(w)=e^{1/w}/(2\pi i\,w)$,  $w=s-t\ne0$',
             ha='center', fontsize=14)
    js=list(range(13)); ys=[-math.lgamma(j+1)/math.log(10) for j in js]
    axes[0].plot(js, ys, marker='o', color='#126c88', lw=2)
    axes[0].set_title('Complete positive-order coefficients', fontsize=12)
    axes[0].set_xlabel(r'$j$');axes[0].set_ylabel(r'$\log_{10}(j!a_j)=\log_{10}(1/j!)$')
    axes[0].set_xticks([0,3,6,9,12]);axes[0].grid(alpha=.22)
    ks=[r['k'] for r in data['kernel_samples']]
    full=[r['sample_log10_abs_2pi_K'] for r in data['kernel_samples']]
    axes[1].plot(ks,full,color='#126c88',lw=2.4,label='full kernel')
    for degree,color in [(8,'#db8531'),(32,'#8b5295')]:
        vals=[]
        for k in ks:
            partial=sum(k**(j+1)/math.factorial(j) for j in range(degree+1))
            vals.append(math.log10(partial))
        axes[1].plot(ks,vals,lw=1.8,color=color,label=f'partial degree {degree}')
    axes[1].set_title('Normal convergence on punctured compacts',fontsize=12)
    axes[1].set_xlabel(r'$k$  (exact real samples $w=1/k$)')
    axes[1].set_ylabel(r'$\log_{10}|2\pi K(1/k)|$')
    axes[1].legend(fontsize=9,loc='upper left');axes[1].grid(alpha=.22)
    axes[2].set_axis_off();axes[2].set_title('A finite jet cannot give the full action',fontsize=12)
    rows=[]
    for r in data['monomial_evaluations']:
        m=r['m'];den=math.factorial(m)
        val='1' if den==1 else f'1/{den}'
        rows.append([str(m),val if m<=3 else '0',val])
    tab=axes[2].table(cellText=rows,colLabels=[r'$m$',r'$P_3(t^m)(0)$',r'$P(t^m)(0)$'],
                      cellLoc='center',colLoc='center',bbox=[-.02,-.03,1.08,.99],
                      colWidths=[.18,.4,.42])
    tab.auto_set_font_size(False);tab.set_fontsize(11)
    for (r,c),cell in tab.get_celld().items():
        cell.set_edgecolor('#d5dce1');cell.set_linewidth(.6)
        if r==0:cell.set_facecolor('#e3edf2')
        elif r>=5:cell.set_facecolor('#fcf0e3' if c==1 else '#eff6f8')
    fig.text(.055,.115,r'For every $\varepsilon>0$:  '
             r'$a_j\leq e^{1/\varepsilon}\varepsilon^j/j!$.',fontsize=11)
    fig.text(.055,.066,'On every holomorphic germ the full action converges. '
             'Every point-supported ordinary distribution has finite jet order.',fontsize=11)
    fig.text(.055,.025,'Exact rational samples and coefficients are saved with the figure. '
             'IK.9 proves the obstruction; the plot makes no boundary-value assertion.',
             fontsize=9,color='#495564')
    fig.savefig(outdir/'infinite-order-obstruction.png',dpi=170,
                metadata={'Software':'Matplotlib'})
    fig.savefig(outdir/'infinite-order-obstruction.svg',
                metadata={'Date':None,'Creator':'Matplotlib'})
    plt.close(fig)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    build(ap.parse_args().output.resolve())

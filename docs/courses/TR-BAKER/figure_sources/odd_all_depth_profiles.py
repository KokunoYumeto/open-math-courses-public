"""Original Figure 10.32, TR-BAKER-10. CC0.

Exact original III.2 profile from Solution 53, and rational lower gaps from
Lemma 10.138. The diagrams show interpolation data, not function values.
"""
from fractions import Fraction as F
from pathlib import Path
from math import floor
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from odd_depth_endpoints import run


def main():
    data=run()['rows']
    names=['I.1','I.2','II','III.1','III.2','IV.P1','IV.Plarge']
    gaps={name:[min(F(row[key]) for row in data if row['case']==name)
        for key in ['fractional_gap','input_gap','terminal_closure_gap']]
        for name in names}
    lower={name:[F(floor(v*1000),1000) for v in gaps[name]] for name in names}
    c=F('0.5267');eta=1-c/3;H=eta**3;S=F(100);T=F(1000)
    R1=2*(floor(S)+1);R2=floor(4*S);O=floor(H*T)
    cut=[floor(eta*T),floor(eta**2*T)]
    assert (R1,R2,O,cut)==(202,400,560,[824,679])
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(15.5,6.7),constrained_layout=True,
                            gridspec_kw={'width_ratios':[1.07,1]})
    fig.patch.set_facecolor('#fbfcfe')
    ax.fill_between([0,2.02],[O,O],[824,824],color='#267896',alpha=.22)
    ax.fill_between([2.02,4],[O,O],[679,679],color='#ba803c',alpha=.23)
    ax.plot([0,2.02,2.02,4],[824,824,679,679],color='#267896',linewidth=3,
            label='Full original integer cutoffs')
    ax.plot([0,2.02],[1000,1000],color='#ba803c',linestyle='--',linewidth=2.4,
            label='Deleted inner nodes: cutoff 1000')
    ax.plot([0,4],[O,O],color='#3b7c50',linewidth=2.4,
            label='Fractional output: cutoff 560')
    for x in [F(k,100) for k in range(1,203,2)]:
        ax.plot([float(x),float(x)],[824,1000],color='#ba803c',alpha=.13,linewidth=.7)
    ax.text(.98,874,'Full inner cutoff 824',ha='center',fontsize=12)
    ax.text(3.03,722,'Full outer cutoff 679',ha='center',fontsize=12)
    ax.text(2.25,1037,'q = 2; rank 2; c = 0.5267',fontsize=12)
    ax.text(.12,455,'Multiplicities: 441 deleted; 265 inner multiples; 120 outer\n'
            'Node counts: 202; 203; 396.  Total degree: 190397.',fontsize=11)
    ax.set_xlim(0,4.12);ax.set_ylim(410,1110)
    ax.set_xticks([0,2.02,4],['0','2.02 (radius 202)','4 (radius 400)'])
    ax.set_xlabel('Absolute integer radius / Sᵢ')
    ax.set_ylabel('Total derivative order')
    ax.set_title('The original mixed profile supplies every input jet',fontweight='bold',pad=15)
    ax.legend(loc='upper left',fontsize=10,framealpha=.96)
    colors=['#267896','#ba803c','#3b7c50']
    labels=['Fractional mass gap','Fractional input gap','Terminal mass gap']
    for j in range(3):
        x=[k+(j-1)*.24 for k in range(7)]
        vals=[float(lower[name][j]) for name in names]
        bx.bar(x,vals,width=.22,color=colors[j],label=labels[j])
        for xx,v in zip(x,vals):bx.text(xx,v+.02,f'{v:.3f}',ha='center',va='bottom',
                                      fontsize=9,rotation=90)
    bx.set_xticks(range(7),['I.1','I.2','II','III.1','III.2','IV\nP = 1','IV\nP ≥ 7'])
    bx.set_ylim(0,2.15);bx.set_ylabel('Strict rational lower gap')
    bx.set_xlabel('Original coupled field row (all ranks and depths)')
    bx.set_title('Every relevant analytic entry exceeds its cost',fontweight='bold',pad=15)
    bx.legend(loc='upper left',fontsize=10,framealpha=.96)
    for axis in [ax,bx]:axis.grid(axis='y',alpha=.14);axis.set_axisbelow(True)
    fig.savefig(Path(__file__).with_name('odd-all-depth-profiles.png'),dpi=170,
                metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 figure'})
    print({'cutoffs':cut,'output':O,'radii':[R1,R2]})


if __name__=='__main__':main()

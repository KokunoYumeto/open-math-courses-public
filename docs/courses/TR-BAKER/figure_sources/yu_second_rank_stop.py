"""Second-scale multiplicity margins and rank-one budgets; original CC0 figure.

GPT-6 Astra (OpenAI), Ultra. See TR-BAKER-10 Theorem10.191,
Corollary10.192, Proposition10.193 and Solution77 for the full proofs.
Run with Python, matplotlib and numpy; optionally give an output PNG path.
"""
from fractions import Fraction as F
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def certificate():
    result={
        'rank_zero_lower':F(32,11),
        'intermediate_lower':F(2**20,29),
        'full_rank_lower':F(31),
        'profile_upper':F(1050,2**36),
        'logarithmic_rankone_upper':F(1,4000),
        'height_rankone_upper':F(1,100000),
        'rankone_target':F(1,3000),
    }
    assert 2*F(173,200)**4>1 and 3*F(4,5)**4>1
    assert 1+F(27,25)+F(27,25)**2/2>2
    assert 1+F(8,5)+F(8,5)**2/2>3
    assert F(9*256**2*2**15,392*87*5)>20
    assert F(3*2**25,35*5)>4
    assert F(2,7)*256*2**15>2**21
    assert F(16**12,18*12**3)>31
    assert 2**21*F(2,3)**3>1
    assert F(16**4,12)*F(3,4)>1
    assert result['profile_upper']<F(1,10**6)
    assert F(406*49*27,58)==9261 and 8000<9261
    assert 400000<460404
    assert result['logarithmic_rankone_upper']+result['height_rankone_upper']==F(13,50000)<result['rankone_target']
    return result

def draw(path):
    c=certificate()
    plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
    fig=plt.figure(figsize=(12,7.6),layout='constrained')
    gs=fig.add_gridspec(2,2,height_ratios=[1.1,1])
    ax=fig.add_subplot(gs[0,0])
    vals=[float(c[k]) for k in ['rank_zero_lower','intermediate_lower','full_rank_lower']]
    ax.bar(np.arange(3),vals,color=['#217a8a','#2d5b9b','#605899'],width=.6)
    ax.set_yscale('log');ax.set_ylim(.6,2e5)
    ax.axhline(1,color='#a12d35',linestyle='--',label='required ratio > 1')
    ax.set_xticks(range(3),['m = 0','1 ≤ m < r','m = r'])
    ax.set_ylabel('Proved lower bound (log scale)')
    for i,v,label in zip(range(3),vals,[r'$32/11$',r'$2^{20}/29$',r'$31$']):
        ax.text(i,v*1.3,label,ha='center',va='bottom')
    ax.legend(loc='upper left',frameon=False,fontsize=10)
    ax.set_title('All multiplicity allocation ratios',loc='left',weight='bold')
    ax.spines[['top','right']].set_visible(False)

    ax=fig.add_subplot(gs[0,1]);ax.set_axis_off()
    ax.set_title('What the stopping argument establishes',loc='left',weight='bold')
    boxes=[(.5,.83,'Required prepared zeros\n(assumption here)', '#fff2dd'),
           (.5,.50,'All degree and allocation hypotheses\nproved in Theorem 10.191','#e7f1f5'),
           (.5,.16,r'Independent bases of rank $1\leq m<r$'+'\n'+r'$\prod R_i<10^{-6}\Gamma_2^{r-m}(\mathcal{R}_r/\mathcal{R}_m)\Omega_r$','#e7f1f5')]
    for x,y,txt,color in boxes:
        ax.text(x,y,txt,ha='center',va='center',fontsize=10.5,transform=ax.transAxes,
                bbox=dict(boxstyle='round,pad=.65',fc=color,ec='#547084'))
    for ya,yb in [(.72,.62),(.38,.28)]:
        ax.annotate('',xy=(.5,yb),xytext=(.5,ya),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.6,color='#547084'))

    ax=fig.add_subplot(gs[1,:])
    log=float(c['logarithmic_rankone_upper'])*1e6
    height=float(c['height_rankone_upper'])*1e6
    ax.barh([0],[log],color='#217a8a',height=.4,label='logarithmic contribution < 250')
    ax.barh([0],[height],left=[log],color='#dc994b',height=.4,label='height contribution < 10')
    target=float(c['rankone_target'])*1e6
    ax.axvline(target,color='#a12d35',linestyle='--')
    ax.text(130,0,'sum < 260',va='center',ha='center',color='white',weight='bold')
    ax.text(target+3,.1,'target: 1000/3',color='#a12d35')
    ax.set_xlim(0,385);ax.set_ylim(-.6,.6);ax.set_yticks([])
    ax.set_xlabel(r'Contribution divided by $C_2 h\Omega_n$, in units of $10^{-6}$')
    ax.set_title('Rank-one endpoint: 13/50000 < 1/3000',loc='left',weight='bold')
    ax.legend(loc='lower left',bbox_to_anchor=(0,-.04),ncol=2,frameon=False,fontsize=10)
    ax.spines[['top','right','left']].set_visible(False)
    fig.savefig(path,dpi=160,facecolor='white')
    plt.close(fig)

if __name__=='__main__':
    target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('yu-second-rank-stop.png')
    draw(target)
    print('Exact rational endpoints passed; figure written to',target.name)

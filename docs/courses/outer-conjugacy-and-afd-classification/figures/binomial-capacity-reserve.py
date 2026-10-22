"""Exact binomial allocation and its illustrative occupancy plot.

Run with Python, Fraction and matplotlib. The SVG is written beside this file.
All capacity and mass comparisons use exact integers and rational numbers;
conversion to floating point is confined to plotted coordinates.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def allocation():
    n=512; lam=F(1,3); beta=F(3,5); eta=F(1,4)
    rho=lam/(1+lam); a=1/(1+lam); C=1+2*lam
    capacities=[comb(n,k) for k in range(n+1)]
    requests=[int((1-eta)*beta*capacities[k]) if 65<=k<=191 else 0 for k in range(n+1)]
    occupancy=[requests[k]+(2*requests[k-1] if k else 0) for k in range(n+1)]
    ratios=[F(b,c) for b,c in zip(occupancy,capacities)]
    retained=C*sum((requests[k]*lam**k*a**n for k in range(n+1)),F(0))
    tail=F(8,441); rounding=F(855)*a**n; loss_bound=eta+tail+rounding
    assert all(0<=b<=c for b,c in zip(occupancy,capacities))
    assert max(ratios)<=F(99,100)
    assert retained<=1 and retained>F(7,10)
    assert 1-retained<=loss_bound<F(3,10)
    assert [k for k,b in enumerate(occupancy) if b]==list(range(65,193))
    return ratios,{'n':n,'levels_checked':n+1,'all_capacities_hold':True,'proved_occupancy_bound':'99/100','max_occupancy':str(max(ratios)),'retained_mass':str(retained),'loss_bound':str(loss_bound),'retained_above':'7/10','all_comparisons_exact':True}

def render(destination):
    ratios, evidence=allocation()
    plt.rcParams.update({'font.size':17,'svg.fonttype':'none','axes.titlesize':19,'axes.labelsize':17})
    fig,ax=plt.subplots(figsize=(5.6,4.8),layout='constrained')
    fig.patch.set_facecolor('#faf9f5');ax.set_facecolor('#faf9f5')
    ax.plot(range(60,198),[float(ratios[k]) for k in range(60,198)],color='#145a72',linewidth=2.2,label='Requested / available')
    ax.axhline(.99,color='#ae5b26',linestyle='--',linewidth=1.8,label='Bound 99/100')
    ax.axhline(1,color='#333333',linestyle=':',linewidth=1.5)
    ax.set(xlim=(60,197),ylim=(0,1.08),xticks=[65,128,192],yticks=[0,.5,1],xlabel='Weight level ℓ',ylabel='Fraction of capacity',title='Allocation at n = 512')
    ax.grid(axis='y',alpha=.15);ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='lower center',fontsize=14,frameon=False)
    fig.savefig(destination,metadata={'Title':'Binomial level capacities for a three-sheet profile','Description':'Exact integer allocation from Example 1.3; plotting coordinates are rounded.'})
    plt.close(fig)
    return evidence

if __name__=='__main__':
    out=Path(__file__).with_name('binomial-capacity-reserve.svg')
    evidence=render(out)
    print(json.dumps(evidence))

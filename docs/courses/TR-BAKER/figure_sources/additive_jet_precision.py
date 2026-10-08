"""Exact additive-divisibility and integer jet-envelope figure. CC0.

Proof locators: TR-BAKER-10, Lemma10.117, Theorems10.118-10.119,
Corollary10.120, Figure10.27 and Solution47.
"""
from pathlib import Path
import argparse
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def envelope(u, degree=8, multiplicity=7, ell=1, chi=2,
             beta=0, vartheta=Fraction(1), separation=0):
    return min(max(-a*ell, u*ell-chi) + a*separation
               + (multiplicity-1-a)*min(0,vartheta-beta+separation)
               for a in range(min(multiplicity-1,degree-u)+1))


def draw(destination):
    plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,
                         'legend.fontsize':12,'figure.facecolor':'white'})
    fig,axes=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
    a=list(range(7));values=[max(-x,-2) for x in a]
    ax=axes[0]
    ax.plot(a,[-x for x in a], '--',color='#a04b39',label='Divisibility discarded: −a')
    ax.plot(a,values,'o-',color='#176a9b',label='Retained: max{−a, −2}')
    ax.axvline(2,color='#777777',linestyle=':',linewidth=1.2)
    ax.annotate('Breakpoint a = 2',xy=(2,-2),xytext=(2.5,-.6),
                arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=13)
    ax.set(title='The additive loss stops at its breakpoint',xlabel='Additive increment a (integer)',
           ylabel='Contribution to the lower-bound envelope',xticks=a,yticks=list(range(-6,1)),ylim=(-6.4,1.1))
    ax.legend(loc='lower left');ax.grid(alpha=.2)
    ax=axes[1];u=list(range(9));k=[envelope(x) for x in u]
    assert k==list(range(-2,7))
    ax.axhline(-6,color='#a04b39',linestyle='--',label='Common linear loss: −6')
    ax.plot(u,k,'o-',color='#176a9b',label='Exact finite envelope Kᵤ = u − 2')
    for x,y in zip(u,k):
        ax.annotate(str(y),(x,y),xytext=(0,8),textcoords='offset points',ha='center',fontsize=12)
    ax.set(title='Each fixed additive order keeps its own gain',xlabel='Original additive order u (integer)',
           ylabel='Kᵤ(7, 0), added to U − β + Gᵤ',xticks=u,yticks=list(range(-6,7,2)),ylim=(-6.8,7.7))
    ax.legend(loc='upper left');ax.grid(alpha=.2)
    fig.suptitle('p = 3, k = 4, L = 2: degree 8, lcm valuation 1, factorial valuation 2\n'
                 'β = 0, ϑ = 1, separation B = 0, maximum multiplicity M = 7',fontsize=14)
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(destination,dpi=180);plt.close(fig)


if __name__=='__main__':
    here=Path(__file__).resolve().parent
    default=(here.parent/'figures' if here.name=='figure_sources' else here)/'additive-jet-precision.png'
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=default)
    draw(parser.parse_args().output)

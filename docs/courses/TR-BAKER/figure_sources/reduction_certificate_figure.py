"""Illustrate the exact Lesson 21 certificates; plotting is not a proof check."""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',type=Path,default=root/'verification/equation-certificates.json')
    parser.add_argument('--output',type=Path,default=root/'figures/reduction-certificates.png')
    args=parser.parse_args()
    data=json.loads(args.data.read_text())
    case=next(c for c in data['cases'] if c['prime']==5)
    rows=case['nearest_power_rows']
    fig,axes=plt.subplots(1,2,figsize=(12.2,5.1),layout='constrained')
    plt.rcParams.update({'font.family':'DejaVu Sans'})
    blue,orange,green='#225c91','#b65c21','#337456'
    ax=axes[0]
    ns=[r['n'] for r in rows]
    ax.semilogy(ns,[r['distance_below'] for r in rows],'o-',color=blue,label=r'$5^n-2^k$')
    ax.semilogy(ns,[r['distance_above'] for r in rows],'s-',color=orange,label=r'$2^{k+1}-5^n$')
    ax.axhline(20,color=green,linestyle='--',label='allowed distance: 20')
    ax.set(xlabel=r'exponent $n$',ylabel='exact integer distance',
           title=r'Two powers: the entire remaining range',xticks=ns,ylim=(10,3e9))
    ax.text(.04,.93,r'$2^k<5^n<2^{k+1}$',transform=ax.transAxes,va='top')
    ax.legend(loc='lower right',fontsize=9)
    ax=axes[1]
    x=np.linspace(96,124,281)
    ax.semilogy(x,np.exp(-x),color=orange,label=r'assumed upper bound $e^{-X}$')
    ax.axhline(1e-48,color=blue,linewidth=2,label=r'proved lower bound $10^{-48}$')
    ax.axvspan(120,124,color=green,alpha=.12)
    ax.axvline(120,color=green,linestyle='--')
    ax.text(119.3,4e-42,'integer X ≥ 120\nexcluded',ha='right',va='top',color=green)
    ax.set(xlabel=r'coefficient size $X$',ylabel=r'bound for $|\Lambda|$',
           title='Three logarithms: compare both bounds',xlim=(96,124),ylim=(1e-55,1e-41))
    ax.legend(loc='lower left',fontsize=9)
    for ax in axes:
        ax.grid(True,alpha=.18)
        ax.spines[['top','right']].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,dpi=160,metadata={'Software':'Matplotlib; reproducible Lesson 21 figure'})
    plt.close(fig)
    print(args.output)


if __name__=='__main__':
    main()

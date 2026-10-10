"""Exact certificates and figure for Theorems 10.162-10.163 (CC0)."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse
import json


def certificate():
    data = []
    cases = [('I.1',1438,7,25,2,58,1,9),
             ('I.2',648,7,25,1,17,1,14),
             ('II',690,7,25,2,58,1,4),
             ('III.1',495,7,25,2,58,1,3),
             ('III.2',557,7,25,1,17,1,12),
             ('IV',2418,7,25,2,58,1,15),
             ('V',406,13,48,2,58,2,9)]
    for label,c,a,kappa,d,rho,torsion,lower in cases:
        Fn = F(c,rho)*torsion*a*a*F(27,10)**3*81/kappa
        En = F(4*kappa,c*a*a*81)/F(27,10)**2/d
        alpha = (F(1,4000)-F(1,100000))*Fn
        assert alpha > lower >= 3
        assert En < F(1,100000)
        data.append(dict(case=label,F2_lower=str(Fn),
                         alpha2_lower=str(alpha),alpha2_coarse_lower=lower,
                         positive_alpha_gap=str(alpha-lower),
                         E2_over_degree_upper=str(En),
                         positive_height_gap=str(F(1,100000)-En)))
    assert F(13,48)*F(27,10)**2 == F(9477,4800) > F(3,2)
    assert F(48,13)/F(27,10)**2 == F(4800,9477) < F(2,3)
    assert F(58)*F(11,4)/25 < 7
    assert 2*F(58)*F(11,4)/25 < 13
    assert sum(F(8,3)**j/factorial(j) for j in range(7)) > 13
    assert F(8,3)**6 > 192
    assert F(8,3)**2 > 7
    assert F(77*3,30)-7 > 0
    examples=[]
    for k in range(6):
        value=pow(16,5**k)-1;v=0
        while value%5==0:value//=5;v+=1
        assert v==k+1
        examples.append(dict(k=k,valuation=v))
    return dict(state='passed',exact_field_cases=data,exact_examples=examples,
                logarithm_budget='1/4000-1/100000',height_budget='1/100000',
                normalized_logarithm_budget='24/25',normalized_height_budget='1/25',
                all_rank_proof='F consecutive ratio>3 and E ratio<2/3 proved in Lemma10.162; exponent absorption for alln>=3 and the exactn2 alternatives proved in Theorem10.163.',
                original_formula='C2 has (n+1)^(n+1)/(n-1)! with no extra factor n. C2star multiplies it by n+1.',
                degree_retained='wK/D0<=192d; the logarithmic exponent cost includes ln d.',
                scope='Every rank-one indexed list, actual original residue order, all integer coefficients and torsion patterns; rank>=2 not claimed.')


def draw(data,path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(left,right)=plt.subplots(1,2,figsize=(12,6.1),gridspec_kw={'width_ratios':[1,1.12]})
    fig.patch.set_facecolor('white')
    for ax in [left,right]:ax.set_facecolor('#f5f7fb')
    xs=[r['k'] for r in data['exact_examples']];ys=[r['valuation'] for r in data['exact_examples']]
    left.plot(xs,ys,color='#285f9e',marker='o',linewidth=2)
    left.set_xticks(xs);left.set_yticks(range(1,7));left.set_ylim(.65,6.4)
    left.set_xlabel('Exponent parameter k');left.set_ylabel('Exact valuation at five')
    left.set_title(r'$16^{5^k}=4^{2\cdot5^k}$',fontsize=16,pad=14)
    left.grid(color='#d4dce8',linewidth=.7)
    left.spines[['top','right']].set_visible(False)
    right.barh(.0,F(24,25),height=.44,color='#285f9e')
    right.barh(.0,F(1,25),left=F(24,25),height=.44,color='#d58a27')
    right.axvline(1,color='#a62836',linewidth=2)
    right.text(.46,.0,'Exponent <24/25',ha='center',va='center',color='white',fontsize=12)
    right.annotate('Residue height <1/25',xy=(.98,.22),xytext=(.62,.82),
                   ha='center',arrowprops={'arrowstyle':'->','color':'#8f5c1a'},fontsize=12)
    right.set_ylim(-.75,1.35);right.set_xlim(0,1.10)
    right.set_yticks([]);right.set_xlabel(r'Budget normalized by $U/4000$')
    right.set_title('Rank-one lists of length at least two',fontsize=12,pad=14)
    right.spines[['top','right','left']].set_visible(False)
    right.text(.04,-.55,r'$U=(t/d)\mathcal{T}_n^{(2)}$',fontsize=15)
    fig.suptitle('One exact power supplies the second rank-one estimate',x=.07,y=.98,
                 ha='left',fontsize=18,fontweight='bold')
    fig.text(.07,.15,r'Left: $(4,16)$, selected base $4$, original residue order $g=2$, index $\delta_\beta=2$.',fontsize=11)
    fig.text(.07,.105,'Right: both terms are strictly below their allowances, whose exact sum is 1.',fontsize=11)
    fig.text(.07,.04,'Proof: Lemma 10.162 and Theorem 10.163. The modified-height floor and the field-degree cost are retained.',fontsize=10.5)
    fig.subplots_adjust(left=.08,right=.97,top=.79,bottom=.30,wspace=.37)
    fig.savefig(path,dpi=160,metadata={'Software':'Original CC0 mathematical figure'})
    plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--certificate',type=Path);parser.add_argument('--figure',type=Path)
    args=parser.parse_args();data=certificate()
    if args.certificate:args.certificate.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    if args.figure:draw(data,args.figure)
    print(json.dumps(dict(state=data['state'],field_cases=7,exact_examples=len(data['exact_examples']))))

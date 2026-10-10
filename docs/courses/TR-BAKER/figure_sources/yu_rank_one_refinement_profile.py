"""Exact valuation example and universal proof budgets; original figure, CC0.
Written by GPT-6.1 Sol (OpenAI), Ultra. Font glyphs retain their licences.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rankone_endpoints',HERE/'yu_rank_one_refinement_enclosures.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
data=cert.certificate()

def draw(output):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,budget)=plt.subplots(1,2,figsize=(13,6.5),gridspec_kw={'width_ratios':[1.1,1]})
    fig.patch.set_facecolor('white')
    rows=data['example'];xs=[r['k'] for r in rows];ys=[r['exact_v5'] for r in rows]
    ax.plot(xs,ys,'o-',color='#26715d',lw=2,markersize=6)
    ax.set_xticks(xs);ax.set_yticks(ys);ax.set_xlim(-.25,6.25);ax.set_ylim(.5,7.6)
    ax.set_xlabel(r'Integer $k$');ax.set_ylabel(r'Exact valuation $v_5(16^{5^k}-1)$')
    ax.set_title('Dependent indexed list: 4, 16 at five',fontsize=14,pad=18)
    ax.text(.35,6.55,r'$16\cdot4^{-2}=1$'+'\n'+r'$P=1,\quad M=2\cdot5^k$',color='#4b5563',fontsize=12,linespacing=1.7)
    ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
    fig.text(.285,.12,'Selected base 4; original residue order 2\n'+r'$(0,5^k)\;\longmapsto\;4^{2\cdot5^k}$'+'\n'+r'$v_5(16^{5^k}-1)=1+k$',ha='center',fontsize=11,linespacing=1.5)
    shares=[F(data['logarithmic_budget'])*2100,F(data['residue_height_budget'])*2100]
    assert shares==[F(379,400),F(21,400)] and sum(shares)==1
    vals=[float(x) for x in shares]
    budget.barh([0,1],vals,height=.4,color=['#264f88','#b0612f'])
    budget.set_yticks([0,1],['Exponent logarithm','Original-residue height'])
    budget.invert_yaxis();budget.set_xlim(0,1.08)
    budget.text(vals[0]-.02,0,r'$<379/400$',ha='right',va='center',color='white',fontsize=13)
    budget.text(vals[1]+.025,1,r'$<21/400$',ha='left',va='center',color='#17202a',fontsize=13)
    budget.axvline(1,color='#bc4634',ls='--',lw=1.3)
    budget.text(.985,.5,'total threshold 1',ha='right',color='#bc4634',fontsize=11)
    budget.set_xlabel(r'Share of $\mathcal{T}_n/2100$')
    budget.set_title('Every field case and coefficient size',fontsize=14,pad=18)
    budget.grid(axis='x',alpha=.17);budget.set_axisbelow(True);budget.spines[['top','right']].set_visible(False)
    fig.text(.74,.12,'Strict proved envelopes; their sum is 1\n'+r'$(d/t)\log(2|M|)$ and $(2de/t)g h(\beta)$'+'\nfor every rank-one list of length n ≥ 2',ha='center',fontsize=11,linespacing=1.5)
    fig.text(.5,.025,'Lemma 10.157 and Theorem 10.158: exact relations, scalar budgets and complete torsion cases.',ha='center',fontsize=10.5,color='#4b5563')
    fig.tight_layout(rect=(0,.24,1,1));fig.savefig(output,dpi=150,facecolor='white');plt.close(fig)

if __name__=='__main__':
    draw(HERE.parent/'figures/yu-rank-one-refinement.png' if HERE.name=='figure_sources' else HERE/'yu-rank-one-refinement.png')

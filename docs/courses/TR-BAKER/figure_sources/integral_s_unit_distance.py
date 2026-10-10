"""Original exact integral S-unit distance example and figure; CC0.
Written by GPT-6.1 Sol (OpenAI), Ultra.
Theorem 10.159 proves the general bound; this script checks and plots
the worked common-factor and signed examples, not a sample proof.
Human-source context: Kunrui Yu, Acta Math. 211 (2013), Theorem 1,
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6782-11511_2013_Article_106.pdf
"""
from pathlib import Path
from math import gcd
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent

def vp(z,p):
    assert z!=0
    z=abs(z);v=0
    while z%p==0:z//=p;v+=1
    return v

def certificate():
    rows=[]
    for N in range(7):
        x=3**N*25;y=3**N*7;common=gcd(x,y)
        assert common==3**N and x//common==25 and y//common==7
        value=vp(x-y,3);excess=value-vp(common,3)
        assert value==N+2 and excess==2
        rows.append({'N':N,'x':x,'y':y,'common_factor':common,
                     'common_v3':N,'coprime_exponents':[2,-1],
                     'coprime_v3':2,'difference_v3':value})
    group={1}
    while True:
        new=group|{a*b%3 for a in group for b in [2,5%3,7%3]}
        if new==group:break
        group=new
    assert group=={1,2} and (3-1)//len(group)==1
    def gf4_mul(a,b):
        product=0
        while b:
            if b&1:product^=a
            b>>=1;a<<=1
            if a&4:a^=7
        return product
    assert gf4_mul(2,2)==3 and gf4_mul(3,2)==1
    assert vp(25-(-7),2)==5
    return {'state':'passed_exact_worked_examples_with_written_general_proof',
            'common_factor_rows':rows,'odd_residue_group':sorted(group),
            'odd_saturated_index':1,'signed_example':{'x':25,'y':-7,'p':2,
            'list':[-1,5,7],'coefficients':[1,2,-1],'d':2,'e':1,'f':2,
            'q_primary_order':3,'saturated_index':1,'raw_singleton_index':3,
            'floor':'3/544','exact_difference_v2':5},
            'scope':'Exact integer and finite-field examples for159/160. Complete field hypotheses, exponent bounds, sign and n0 clauses are proved in the lesson.'}

def draw(output):
    data=certificate();rows=data['common_factor_rows']
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,units)=plt.subplots(1,2,figsize=(12.5,6),gridspec_kw={'width_ratios':[1.05,1]})
    fig.patch.set_facecolor('white');ns=[r['N'] for r in rows]
    ax.bar(ns,ns,color='#264f88',label=r'Common factor: $v_3(g_0)=N$')
    ax.bar(ns,[2]*len(ns),bottom=ns,color='#26715d',label='Coprime distance: valuation 2')
    for N in ns:ax.text(N,N+2.1,str(N+2),ha='center',fontsize=11)
    ax.set_ylim(0,9.2);ax.set_xticks(ns);ax.set_xlabel(r'Integer $N$')
    ax.set_ylabel(r'Exact valuation $v_3(x-y)$')
    ax.set_title(r'$x=3^N25,\ y=3^N7$',fontsize=15,pad=16)
    ax.legend(loc='upper left',fontsize=10.5);ax.grid(axis='y',alpha=.15)
    ax.set_axisbelow(True);ax.spines[['top','right']].set_visible(False)
    units.axis('off');units.set_xlim(0,1);units.set_ylim(0,1)
    units.set_title('After removing the common factor',fontsize=14,pad=16)
    boxes=[(.82,'One coprime part divisible by p','Excess valuation is exactly 0','#b0612f'),
           (.52,'Both parts are local units',r'$\Xi=\epsilon\prod q_i^{b_i}$; logarithm bound applies','#26715d'),
           (.22,'Signed example at two',r'$25-(-7)=32$; excess valuation is 5','#264f88')]
    for y,title,detail,color in boxes:
        units.text(.5,y,title+'\n'+detail,ha='center',va='center',fontsize=11.5,
                   linespacing=1.6,bbox={'boxstyle':'round,pad=.7','facecolor':'#f4f6f8','edgecolor':color,'linewidth':1.4})
    fig.text(.28,.1,'Prime bases 5, 7; residue index 1 at three\nThe common-factor term cannot be omitted.',ha='center',fontsize=11,linespacing=1.5)
    fig.text(.75,.1,'At two use K = Q(ζ₃), e = 1, f = 2\nSign base −1: length 3, rank 2, floor 3/544.',ha='center',fontsize=11,linespacing=1.5)
    fig.text(.5,.025,'Theorem 10.159 and Corollary 10.160; exact examples checked in Solution 65.',ha='center',fontsize=10.5,color='#4b5563')
    fig.tight_layout(rect=(0,.22,1,1));fig.savefig(output,dpi=150,facecolor='white');plt.close(fig)

if __name__=='__main__':
    draw(HERE.parent/'figures/integral-s-unit-distance.png' if HERE.name=='figure_sources' else HERE/'integral-s-unit-distance.png')
    print(json.dumps(certificate(),indent=2))

"""Exact coefficient-height conversion for TR-BAKER-10 Lemma10.153. CC0.

The written universal enclosure accompanies the finite endpoint calculation;
no decimal sampling is used as its proof. The rank-one rational bounds of
Theorem10.154 are included.
"""
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
from pathlib import Path
import json
SCALE=10**24
ROWS=[('I.1',939,58,F('4.03'),2),('I.2',636,17,F('4.79'),1),
      ('II',505,58,F('3.44'),2),('III.1',1794,58,F('4.71'),2),
      ('III.2',1790,17,F('5.84'),1),('IV',2680,58,F('5.12'),2),
      ('V',206,58,F('2.52'),2)]

def down(x):return F((x*SCALE).numerator//(x*SCALE).denominator,SCALE)
def up(x):return -down(-x)

def basic_log(x):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    lower=2*sum(z**(2*j+1)/(2*j+1) for j in range(32))
    upper=lower+2*z**65/(65*(1-z*z))
    return down(lower),up(upper)

LOG2=basic_log(F(2))
@lru_cache(None)
def log_interval(x):
    x=F(x);assert x>0
    if x<1:
        lo,hi=log_interval(1/x);return -hi,-lo
    shift=0
    while x>=2:x/=2;shift+=1
    lo,hi=basic_log(x)
    return lo+shift*LOG2[0],hi+shift*LOG2[1]

def exp_upper(x):
    x=F(x);assert 0<=x<66
    partial=sum(x**j/factorial(j) for j in range(65))
    return up(partial+x**65/(factorial(65)*(1-x/66)))

def certificate():
    assert exp_upper(F(1))<F(11,4) and exp_upper(F(6))<513
    facts={1:(F(0),F(0))}
    for k in range(2,512):
        lk=log_interval(F(k));old=facts[k-1]
        facts[k]=(old[0]+lk[0],old[1]+lk[1])
    records=[];lam=F(7899,7900)
    for case,c,rho,a1,dmin in ROWS:
        abase=26 if case=='V' else 7 if case.startswith('III.') else 14
        torsion_factor=2 if case=='V' else 1
        assert c*abase>5000 and F(c*abase*torsion_factor,rho)>120
        const=log_interval(lam*c/rho)[0]
        lower=[]
        for n in range(2,512):
            alower=4+log_interval(F((n+1)*dmin))[0]
            value=const+1+(n+2)*log_interval(F(n+1))[0]+(n-1)*log_interval(F(n-1))[0]-2*facts[n][1]-2*n+log_interval(alower)[0]-a1
            assert value>F(5,1000),(case,n)
            lower.append((value,n))
        value,n=min(lower)
        tail=lam*c*10/(rho*F(11,4))-exp_upper(a1)
        assert tail>0
        records.append({'case':case,'finite_checked_ranks':[2,511],
            'minimum_exact_log_margin':str(value),'minimum_rank':n,
            'minimum_margin_decimal':float(value),'infinite_tail_gap_exact':str(tail)})
    return {'state':'passed_exact_finite_endpoints_with_written_infinite_enclosure',
        'finite_endpoints':7*510,'rows':records,
        'uniform_after512':'Concavity of ln gives n!<=e sqrt(n)(n/e)^n. Also (1+1/n)^(n+2)(1-1/n)^(n-1)>1. Thus W/(d exp(a0*n))>(7899/7900)c A_n/(rho*e). At n>=512, A_n>10 and e<11/4; exact positive exponential tails enclose exp(a1).',
        'arithmetic':'Each logarithm uses32positive terms after range reduction to[1,2], a rigorous geometric tail, and outward rounding to10^-24. Every displayed finite margin is a strict lower endpoint.',
        'rank_one':{'log_term_ratio':'<1/2688','residue_term_ratio':'<1/10000','sum_exact':str(F(1,2688)+F(1,10000)),'target':'1/2100','strictly_smaller':F(1,2688)+F(1,10000)<F(1,2100)},
        'source':'Free2013 Section8.1–8.5; the complete lesson proof uses the already-proved singleton height bound10.18 and the large-B branch for its coefficient-height conversion.'}

if __name__=='__main__':
    data=certificate()
    target=Path(__file__).resolve().parent/'yu-application-height-endpoints.json'
    target.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ['state','finite_endpoints','rows']}))

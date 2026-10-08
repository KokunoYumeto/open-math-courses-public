"""Exact endpoints for TR-BAKER-10 Lemma 10.151. CC0.

The lesson proves that these rank-two endpoints enclose every rank.
This program performs only the rational endpoint arithmetic, not that proof.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

# name,c0,c1,c3,c4,q,rho,upper vartheta,a_*,retained g1 lower,target
ROWS = [
    ('I.1','2.66','1.449','1.4647','20.74',2,58,F(3,2),F(7),F(1),939),
    ('I.2','1.9','1.4494','1.3852','20.8',2,17,F(3,2),F(7),F(5),636),
    ('II','2.74','1.4372','0.8412','19',2,58,F(5,4),F(7),F(1),505),
    ('III.1','2.78','1.4341','2.992','18.7',2,58,F(1),F(7,2),F(5),1794),
    ('III.2','2.6','1.432','3.26','18.2757',2,17,F(1),F(7,2),F(509,100),1790),
    ('IV','3','1.4441','3.849','20',2,58,F(7,6),F(7),F(1),2680),
    ('V','2.5','2.5347','0.4757','3.765',3,58,F(2),F(26,3),F(1),206),
]

def budgets(row, r):
    name,c0,c1,c3,c4,q,rho,depth,astar,g1,target=row
    c0,c1,c3,c4=map(F,(c0,c1,c3,c4));a=r+1
    fr=F(r**r*a**r,factorial(r)**2)
    lr=2*c0*c4*q*a*astar**r*fr*g1/(rho*depth)
    if name.startswith('I.'):
        gr=c3*q*a*a*(F(39,10)*r+F(36,5))/F(11,10)
    elif name=='II':
        gr=c3*q*a*a*(F(39,10)*r+F(36,5))*F(20,17)
    elif name=='V':
        gr=c3*q*a*a*(F(39,10)*r+F(36,5))/F(347,500)
    else:
        gr=c3*q*a*a*(1 if name=='III.2' else 2)
    return lr,gr,c0*c1*c3*c4*q*q

def certificate():
    # Independent positive-series certificates for the two tight refinements.
    log3lower=2*sum(F(1,2)**(2*j+1)/(2*j+1) for j in range(3))
    exp17lower=sum(F(17,10)**j/factorial(j) for j in range(5))
    assert log3lower>F(109,100) and exp17lower>5
    out=[]
    for row in ROWS:
        lr,gr,product=budgets(row,2);delta=F(3,2)/lr
        assert 0<delta<1
        upper=(1+F(1,10**26))*(1+delta)**2*(2+1/gr)*product
        gap=row[-1]-upper
        assert gap>F(4,1000)
        floor=(gap*10**6).numerator//(gap*10**6).denominator
        out.append({'case':row[0],'g4_lower':str(lr),'g2_lower':str(gr),
                    'upper_exact':str(upper),'target':row[-1],
                    'gap_exact':str(gap),'strict_gap_per_million':floor,
                    'upper_decimal':float(upper)})
    # These are the universal rational bounds used in the rank-one proof.
    assert F(200*7**2*5,58)>800
    assert F(8,200*7*3**3)<F(1,4000)
    return {'state':'passed_exact_rank_two_endpoints_with_written_all_rank_enclosure',
            'rows':out,'minimum_gap_exact':str(min(F(x['gap_exact']) for x in out)),
            'minimum_gap_decimal':float(min(F(x['gap_exact']) for x in out)),
            'all_rank_proof':'Lemma10.151: delta decreases by more than14 each rank, delta2<1, and g2 lower increases. Thus (1+delta_r)^r(2+1/G_r) decreases.',
            'rank_one_proof':'Theorem10.152: elementary residue/height estimate contributes less than1/400+1/4000 of the stated bound.'}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))

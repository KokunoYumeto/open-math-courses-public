"""Exact endpoints for TR-BAKER-10 Lemma 10.157 and Theorem 10.158.

Written by GPT-6.1 Sol (OpenAI), Ultra; CC0.
The lesson proves every infinite-rank and field quantifier. This program
checks rational endpoints and the exact rational worked example.
Human-source context: Kunrui Yu, Acta Math. 211 (2013), Theorem 1/Section 8,
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6782-11511_2013_Article_106.pdf
"""
from fractions import Fraction as F
from math import factorial
import json

def exp_interval(x, degree=32):
    x=F(x)
    lower=sum((x**j/factorial(j) for j in range(degree+1)),F(0))
    first=x**(degree+1)/factorial(degree+1);ratio=x/F(degree+2)
    assert 0<=ratio<1
    return lower,lower+first/(1-ratio)

def certificate():
    cases=[('I.1',939,14,18,58,1,2),('I.2',636,14,18,17,1,1),
           ('II',505,14,18,58,1,2),('III.1',1794,7,9,58,1,2),
           ('III.2',1790,7,9,17,1,1),('IV',2680,14,18,58,1,2),
           ('V',206,26,34,58,2,2)]
    rows=[]
    for case,c,a,kappa,rho,torsion_ratio,degree_min in cases:
        f2=F(c,rho)*torsion_ratio*F(a*a,kappa)*F(2187,70)
        alpha=f2*(F(1,2100)-F(1,40000))
        target=F(4,3) if case=='II' else F(19,10) if case=='V' else F(9,4)
        height=F(14*kappa,81*c*a*a*degree_min)
        assert alpha>target and height<F(1,40000)
        rows.append({'case':case,'F2_lower':str(f2),'alpha2_lower':str(alpha),
                     'displayed_alpha_lower':str(target),'alpha_gap':str(alpha-target),
                     'height_upper':str(height),'height_gap':str(F(1,40000)-height)})
    ratios=[]
    for n in range(2,6):
        rank_factor=F(n+2,n+1)**(n+3)*F(n+1,n+6)**n*F(n+5,n)**(n-1)
        gap=F(104,51)*rank_factor-3
        assert gap>0
        ratios.append({'n':n,'rank_factor':str(rank_factor),'gap_above_three':str(gap)})
    assert F(1456,459)>3
    assert sum((F(1,factorial(j)) for j in range(6)),F(0))>F(27,10)
    comparisons=[]
    checks=[('e_upper',F(1),F(11,4),'upper'),
            ('ln5_gt_8over5',F(8,5),F(5),'upper'),
            ('ln2_lt_7over10',F(7,10),F(2),'lower'),
            ('ln18_lt_3',F(3),F(18),'lower'),
            ('ln45_lt_4',F(4),F(45),'lower'),
            ('ln8_lt_21over10',F(21,10),F(8),'lower'),
            ('ln16_lt_14over5',F(14,5),F(16),'lower'),
            ('ln319over63_lt_5over3',F(5,3),F(319,63),'lower'),
            ('lnrho_lt_5',F(5),F(58),'lower')]
    for name,x,target,side in checks:
        low,high=exp_interval(x);gap=target-high if side=='upper' else low-target
        assert gap>0
        comparisons.append({'name':name,'exponent':str(x),'target':str(target),
                            'side':side,'positive_gap':str(gap)})
    assert F(32,15)>F(17,8) and F(38,15)>F(17,8) and F(9,4)>F(17,8)
    assert F(88,15)>5 and F(13,2)>F(19,3)
    assert F(136,15)>F(15,2) and F(17,2)>F(15,2)
    assert F(181*3,90)-5>0
    example=[]
    for k in range(7):
        exponent=5**k;difference=pow(16,exponent)-1;valuation=0
        while difference%5==0:difference//=5;valuation+=1
        assert valuation==k+1 and pow(4,2*exponent)==pow(16,exponent)
        example.append({'k':k,'b1':0,'b2':exponent,'B':max(3,exponent),
                        'P':1,'M':2*exponent,'exact_v5':valuation})
    return {'state':'passed_exact_endpoints_with_written_uniform_proof',
            'case_rows':rows,'finite_consecutive_ratios':ratios,
            'infinite_ratio_lower':'1456/459 >3 for every n>=6',
            'exponential_series_checks':comparisons,'example':example,
            'logarithmic_budget':str(F(1,2100)-F(1,40000)),
            'residue_height_budget':'1/40000','total_budget':'1/2100',
            'scope':'Complete direct rank-one refinement158. Infinite quantifiers and exact relation reduction are proved in the lesson; no finite sample is a substitute.'}

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

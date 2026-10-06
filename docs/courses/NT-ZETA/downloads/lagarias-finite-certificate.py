"""Exact rational certificate of strict Lagarias inequalities for 2 <= n <= 5040."""
from fractions import Fraction
from math import factorial
import json
from pathlib import Path
Q=10**6
LIMIT=5040
sigma=[0]*(LIMIT+1)
for d in range(1,LIMIT+1):
    for n in range(d,LIMIT+1,d):sigma[n]+=d
h=0
minimum=None
for n in range(1,LIMIT+1):
    h+=Q//n
    if n==1:continue
    H=Fraction(h,Q)
    z=(H-1)/(H+1)
    log_lower=2*sum((z**(2*j+1)/ (2*j+1) for j in range(20)),Fraction())
    exp_lower=sum((H**j/factorial(j) for j in range(31)),Fraction())
    margin=H+exp_lower*log_lower-sigma[n]
    assert margin>0,(n,margin)
    if minimum is None or margin<minimum[1]:minimum=(n,margin)
report={'range':[2,LIMIT],'passed':True,'count':LIMIT-1,'arithmetic':'Python arbitrary-precision integer and Fraction only; no floating point in predicates','harmonic_lower_denominator':Q,'logarithm_positive_atanh_terms':20,'exponential_positive_Taylor_degree':30,'smallest_margin_n':minimum[0],'smallest_margin_exact':str(minimum[1])}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('All',LIMIT-1,'strict inequalities passed; minimum margin at n =',minimum[0])

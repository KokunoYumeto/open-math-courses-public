"""Finite exact checks for22.203--210; numerical samples are separate."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from math import comb, factorial, prod
from itertools import product
import json
import sympy as sp
import mpmath as mp

base=Path(__file__).resolve().parent
counts=Counter()
def check(name, condition):
    assert condition,name
    counts[name]+=1

check('height_constant_log27648',sum(F(11)**j/factorial(j) for j in range(26))>27648)
check('zero_invariant_radius_constant',1005<2*729)
check('log2_lower',3**3<2**5)
check('period_prefactor_constant',9<12)
check('small_logarithm_constant',F(4,3)>F(10,9))
for g in range(1,101):
    n=g+1; eps=F(1,200*g*g);lam=2*eps;eta=F(1,400*g**3+1)
    check('c4_lower_integer_constant',8*19*85*4**g*n**g>100000)
    check('c7_upper_integer_comparison',28*n+60<65*n)
    check('theta_growth_comparison',100000*n**(2*g+1)>800*g**3*n)
    check('elliptic_degree_growth',n**(2*g-2)>=g**3)
    check('elliptic_degree_floor_margin',F(2000,3)*g**3>400*g**3+1)
    check('additive_degree_floor_margin',69984*8**g*n**(2*g+1)>400*g**3+1)
    check('full_degree_rounding',n*(100*g*g+1)<=400*g**3+1)
    check('subgroup_degree_rounding',g*eta<eps/2)
    check('strict_inside_hyperplane_margin',(1+eps)*(1-eps/2)/(1+eps/4)>1)
    check('outside_hyperplane_M_bound',10**8*n**3>6*n)
    # The minimum admissible theta already bounds every binomial correction.
    theta=800*g**3*n
    p=F(1)
    for q in range(1,g+1):
        p*=1+F(q,theta)
        check('rising_product_rounding',p<1+eps/4)
        hb=g-q
        check('rank_factorial_identity',F(factorial(n),factorial(hb)*factorial(q))==n*comb(g,q))
        check('rank_last_direction_factorial',F(factorial(n),factorial(hb)*factorial(q-1))==n*q*comb(g,q))

def compositions(total, slots):
    if slots==1:
        yield (total,);return
    for first in range(total+1):
        for tail in compositions(total-first,slots-1):yield(first,)+tail

# This checks the product-rule allocation, independently of any local-ring model.
for m in range(1,4):
    for a in range(1,4):
        for outside in range(m):
            for selected in range(min(7,a*(m-outside))):
                for vv in compositions(outside,m):
                    for uu in compositions(selected,m):
                        check('weighted_product_rule',any(vv[j]==0 and uu[j]<a for j in range(m)))

def monomial_count(r,rho,a,m):
    if rho==0:return comb(m+r-1,r)
    if rho==r:return comb(a*m+r-1,r)
    return sum(comb(b+r-rho-1,r-rho-1)*comb(a*(m-b)+rho-1,rho) for b in range(m))

z=sp.symbols('z')
for r in range(1,6):
    for rho in range(r+1):
        for a in range(1,6):
            p=sp.Poly(sp.interpolate([(m,monomial_count(r,rho,a,m)) for m in range(1,r+2)],z),z)
            check('power_count_leading_coefficient',p.degree()==r and p.LC()*factorial(r)==a**rho)
            check('power_count_additional_value',p.eval(r+4)==monomial_count(r,rho,a,r+4))

# Independent enumeration for monomial regular-sequence parameter ideals.
for r in range(1,4):
    for aa in product(range(1,4),repeat=r):
        for m in range(1,4):
            count=sum(sum(v//a for v,a in zip(vv,aa))<m for vv in product(*(range(a*m) for a in aa)))
            check('regular_sequence_power_length',count==prod(aa)*comb(m+r-1,r))
for m in range(1,41):
    check('two_direction_example',monomial_count(2,2,4,m)==8*m*m+2*m)

mp.mp.dps=100
numeric=[]
for g in range(1,9):
    n=g+1;ep=mp.mpf(1)/(200*g*g);la=2*ep
    ag=g*mp.log(4*n)+5*mp.log(n)+15
    jg=12*(13+4*mp.e**2)/(25+4*mp.e**2)*n*mp.log(4*n)+56*mp.log(n)+54
    c4=4**g*n**(g+1)*(1+la)*8*n*ag*jg
    c6=n*2**g
    c7=4*mp.log(4*n)/(13+4*mp.e**2)+(60+20*mp.log(n))/((13+4*mp.e**2)*g)
    c5=c6*c4**(2*g+1)/(factorial(n)*6**g*c7**g)
    for degree in (1,3):
        for h in (1,5):
            vv=[mp.mpf(h)*(1+mp.mpf(g-i-1)/g) for i in range(g)]
            for ell in (mp.mpf(1),mp.mpf(5)*degree*h):
                b=10*h;ll=mp.log(b)+h+mp.log(degree)+ell;rr=b+mp.log(degree)+ell
                ss=mp.floor(c4*degree*ll/ell)
                u0=c5*degree**(2*g+2)*rr*ll**(g+1)*mp.fprod(vv)/ell**(2*g+1)
                theta=u0/(degree*ll)
                ti=[c7*u0/(degree*ss**2*x) for x in vv]
                assert theta>800*g**3*n and theta>=c4 and min(ti)>400*g**3+1
                assert min(theta/x for x in ti)>6*n
                ratio=mp.fprod(theta+j for j in range(1,g+1))*ss/((1+ep)*2**g*factorial(n)*3**g*mp.fprod(ti))/(u0/(c6*degree*rr))
                assert ratio<1
                s0=mp.floor(ss/((1+la)*4**g*n**(g+1)*jg))
                t0=mp.floor(theta/(2*g*(1+la)*4**g*n**(g+1)*jg))
                assert s0>=1 and t0>=1
                numeric.append({'g':g,'field_degree':degree,'h':h,'ell':str(ell),'log10_theta':mp.nstr(mp.log10(theta),16),'point_extremal_ratio':mp.nstr(ratio,20),'sample_count_S0':mp.nstr(s0,12)})

result={'exact':{'total':sum(counts.values()),'families':dict(counts)},'numerical':{'total':len(numeric),'precision_decimal_digits':100,'scope':'Parameter-shape samples satisfying the scalar hypotheses; not additional proofs or realizations by elliptic points.','samples':numeric},'scope':'Local power-count identities, regular-sequence monomial models, derivative allocation, strict rounding margins and parameter identities. General statements are established in the manuscript; the full David logarithm theorem remains unfinished.'}
(base/'elliptic-parameter-balance-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact':result['exact'],'numerical_samples':len(numeric)}))

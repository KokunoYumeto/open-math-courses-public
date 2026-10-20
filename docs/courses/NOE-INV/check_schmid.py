"""Independent finite arithmetic checks; completeness is proved in the lesson."""
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
import json,sympy as s
b=Path(__file__).resolve().parent
def comp(a,c):return tuple(a[c[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
G=list(permutations(range(3)));I=(0,1,2);B=(1,0,2);P=[I,B]
coset=lambda t:frozenset(comp(p,t) for p in P)
representatives={coset(t):min(coset(t)) for t in G}
def transfer(g):
    value=0
    for t in representatives.values():
        tg=comp(t,g);tt=representatives[coset(tg)]
        h=comp(tg,inv(tt));assert h in P
        value^=(h==B)
    return value
assert all(transfer(comp(g,h))==(transfer(g)^transfer(h)) for g,h in product(G,repeat=2))
assert transfer(B)==1
kernel=[g for g in G if transfer(g)==0]
assert len(kernel)==3
def compositions(total,n):
    if n==1:yield (total,);return
    for i in range(total+1):
        for tail in compositions(total-i,n-1):yield (i,)+tail
checked={}
for p,q in [(3,2),(5,2)]:
    counts=0;mixed=0
    @lru_cache(None)
    def factors(c):
        if sum(c)==0:return 0
        best=0
        for sub in product(*(range(e+1) for e in c)):
            if not sum(sub) or sum(i*e for i,e in enumerate(sub))%p:continue
            rest=tuple(e-f for e,f in zip(c,sub))
            best=max(best,1+factors(rest))
        return best
    for c in compositions(p*q,p):
        if sum(i*e for i,e in enumerate(c))%p:continue
        counts+=1
        different=sum(bool(e) for e in c)>1
        if c[0] or different:
            assert factors(c)>=q+1;mixed+=1
        else:assert factors(c)==q
    checked[f'C{p}-degree{p*q}']={'all_zero_sum_multisets':counts,'all_mixed_or_zero_weight_cases':mixed,'checks':'Maximal factor count computed independently by exhaustive submultisets.'}
x,y=s.symbols('x y')
assert s.expand((x**3+y**3)**2-2*(x*y)**3-x**6-y**6)==0
packets=[]
for p,q,r in [(3,2,2),(7,3,2),(11,5,3)]:
    orbit=[pow(r,j,p) for j in range(q)]
    assert len(set(orbit))==q and pow(r,q,p)==1 and sum(orbit)%p==0 and p>=q+1
    packets.append({'p':p,'q':q,'weight_multiplier':r,'weights':orbit,'zero_sum_packet_length':q,'number_of_packets_in_the_norm_monomial':p})
result={'S3_transfer':{'homomorphism_checks':36,'surjective':True,'kernel_order':3},'zero_sum_factorizations':checked,'norm_packets':packets,'S3_Newton_identity':'x^6+y^6=(x^3+y^3)^2-2(xy)^3; exact polynomial check passed.','scope':'Finite examples support and check the independently supplied all-group proof; they do not replace it.'}
(b/'schmid-calculations.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf8'))
print(json.dumps(result))

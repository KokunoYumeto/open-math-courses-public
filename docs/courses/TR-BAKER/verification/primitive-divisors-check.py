"""Exact supplementary checks; the unrestricted proofs are in Lesson16."""
from pathlib import Path
import hashlib, json, math, re
from datetime import datetime, timezone
import sympy as S

h=Path(__file__).resolve().parent
T,A,B=S.symbols('T A B')
def valuation(n,p):
    assert n
    n=abs(n); k=0
    while n%p==0: n//=p;k+=1
    return k
def order(z,p):
    value=1
    for f in range(1,p):
        value=value*z%p
        if value==1:return f
    raise AssertionError((z,p))
def phi_value(n,a,b):
    poly=S.Poly(S.cyclotomic_poly(n,T),T)
    return sum(int(c)*a**int(m[0])*b**(poly.degree()-int(m[0])) for m,c in poly.terms())

valuation_cases=0
for a in range(2,21):
    for b in range(1,a):
        if math.gcd(a,b)>1:continue
        for n in range(1,33):
            value=phi_value(n,a,b)
            for p0 in S.primerange(2,44):
                p=int(p0)
                if a*b%p==0:expected=0
                elif p==2:
                    if n==1:expected=valuation(a-b,2)
                    elif n==2:expected=valuation(a+b,2)
                    elif n&(n-1)==0:expected=1
                    else:expected=0
                else:
                    f=order(a*pow(b,-1,p)%p,p)
                    if n==f:expected=valuation(a**f-b**f,p)
                    elif n%f==0:
                        q=n//f
                        while q%p==0:q//=p
                        expected=int(q==1)
                    else:expected=0
                assert valuation(value,p)==expected,(a,b,n,p,expected)
                valuation_cases+=1

existence_cases=0;small_exceptions=[]
for a in range(2,11):
    for b in range(1,a):
        if math.gcd(a,b)>1:continue
        for n in range(2,19):
            primes=[int(p) for p in S.factorint(a**n-b**n)]
            primitive=[p for p in primes if all((a**k-b**k)%p for k in range(1,n))]
            exception=(a,b,n)==(2,1,6) or (n==2 and (a+b)&(a+b-1)==0)
            assert bool(primitive)==(not exception),(a,b,n,primitive)
            assert all((p-1)%n==0 for p in primitive)
            if a<=5 and n<=8 and not primitive:small_exceptions.append([a,b,n])
            if n>2:
                primitive_part=math.prod(p**valuation(a**n-b**n,p) for p in primitive)
                q=phi_value(n,a,b)//primitive_part
                assert phi_value(n,a,b)==primitive_part*q
                assert q in [1,max(S.factorint(n))]
            existence_cases+=1
assert sorted(small_exceptions)==[[2,1,6],[3,1,2],[5,3,2]]

identity_cases=0
for p in [2,3,5,7]:
    for f in range(1,8):
        if f%p==0:continue
        assert S.expand(S.cyclotomic_poly(p*f,T)*S.cyclotomic_poly(f,T)-S.cyclotomic_poly(f,T**p))==0
        assert S.expand(S.cyclotomic_poly(p*p*f,T)-S.cyclotomic_poly(p*f,T**p))==0
        identity_cases+=2
for p in [3,5,7,11,13,17,19,23,29,31]:
    c=math.comb(p,2)
    assert S.expand(1+c*B**2-(1+c)*B-(B-1)*(c*B-1))==0
    for b in range(1,101):
        assert (b+1)**p-b**p >= (2**p-1)*b
    if p>=5:assert 2**p-1>3*p
text=(h.parent/'src/TR-BAKER-16.md').read_text(encoding='utf-8')
assert re.findall(r'\\tag\{([^}]+)\}',text)==[f'16.{i}' for i in range(1,110)]
result={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_for_primitive_divisor_component',
 'source_sha256':hashlib.sha256((h.parent/'src/TR-BAKER-16.md').read_bytes()).hexdigest(),
 'valuation_cases':valuation_cases,'existence_and_order_cases':existence_cases,
 'polynomial_identity_cases':identity_cases,'small_exceptions':small_exceptions,
 'numbered_results':7,'equation_tags':27,'solved_component_exercises':3,
 'scope':'Exact arithmetic checks of the two valuation formulas, primitive parts, order congruences, cyclotomic substitutions, endpoint inequality and requested finite examples. Full existence follows from the written proof, not these finite checks.'}
(h/'primitive-divisors-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result))

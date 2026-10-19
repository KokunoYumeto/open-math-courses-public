"""Finite exact checks of the representation and finite-character identities."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math
import sympy as sp

HERE=Path(__file__).resolve().parent
def reduced(d):
    forms=[]
    for a in range(1,math.isqrt(d//3)+1):
        for b in range(-a,a+1):
            if (b*b+d)%(4*a): continue
            c=(b*b+d)//(4*a)
            if c<a or math.gcd(math.gcd(a,abs(b)),c)!=1: continue
            if (abs(b)==a or a==c) and b<0: continue
            forms.append((a,b,c))
    return forms

representation_cases=0
coefficient_cases=0
form_lists={}
for d in [3,4,7,8,11,15,19,20,23,43,56,163]:
    forms=reduced(d);form_lists[str(-d)]=forms
    w=6 if d==3 else 4 if d==4 else 2
    for n in range(1,121):
        count=0
        for a,b,c in forms:
            for y in range(-math.isqrt(4*a*n//d),math.isqrt(4*a*n//d)+1):
                bound=(math.isqrt(4*a*n)+abs(b*y))//(2*a)+1
                for x in range(-bound,bound+1):
                    count+=a*x*x+b*x*y+c*y*y==n
        ideal_count=sum(int(sp.kronecker_symbol(-d,m)) for m in sp.divisors(n))
        assert count==w*ideal_count,(d,n,count,ideal_count)
        representation_cases+=1
        for k in [5,8,12,13,21,24,29]:
            if math.gcd(k,d)!=1:continue
            chi=lambda z:int(sp.kronecker_symbol(k,z))
            product_coefficient=sum(chi(n//m)*chi(m)*int(sp.kronecker_symbol(-d,m))
                                    for m in sp.divisors(n))
            assert w*product_coefficient==chi(n)*count
            coefficient_cases+=1
assert form_lists['-11']==[(1,1,3)]
assert form_lists['-19']==[(1,1,5)]
assert form_lists['-43']==[(1,1,11)]

character_cases=0
zero_leading_cases=0
for d in [3,4,7,8,11,15,19,20,23,43,56]:
    for a,b,c in reduced(d):
        for k in [3,5,7,11,15,21,33,35]:
            if math.gcd(k,d)!=1:continue
            for y in range(k):
                left=sum(int(sp.jacobi_symbol(a*j*j+b*j*y+c*y*y,k)) for j in range(k))
                ramanujan=math.prod(p-1 if y%p==0 else -1 for p in sp.factorint(k))
                right=int(sp.jacobi_symbol(a,k))*ramanujan
                assert left==right,(d,a,b,c,k,y,left,right)
                character_cases+=1
                zero_leading_cases+=math.gcd(a,k)>1
assert zero_leading_cases>0
source=HERE.parent/'src/TR-BAKER-17.md'
record={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_finite_exact_checks',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'representation_cases':representation_cases,'twisted_coefficient_cases':coefficient_cases,
        'finite_character_cases':character_cases,'noncoprime_leading_cases':zero_leading_cases,
        'reduced_forms':form_lists,
        'limits':'These finite exact computations check unit factors, coefficients and local characters. The unrestricted proofs and Fourier limit formula are in Lesson17.'}
(HERE/'class-number-product-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in record.items() if k!='reduced_forms'}))

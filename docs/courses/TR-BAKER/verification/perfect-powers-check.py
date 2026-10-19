"""Checks of exact algebra in the exponent and Catalan arguments."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,math,re
import sympy as S

h=Path(__file__).resolve().parent
X,A,B,power=S.symbols('X A B power')
def v(n,p):
    assert n
    n=abs(n);k=0
    while n%p==0:n//=p;k+=1
    return k

signed_factorizations=0
for p in [3,5,7,11,13]:
    for e in [-1,1]:
        quotient=sum(X**(p-1-j)*e**j for j in range(p))
        assert S.expand((X-e)*quotient-X**p+e)==0
        assert quotient.subs(X,e)==p
        for x in range(2,101):
            z=int(quotient.subs(X,x))
            assert math.gcd(x-e,z) in [1,p]
            if (x-e)%p==0:assert v(z,p)==1
            signed_factorizations+=1

roots=[-2,1,5];multiplicities=[1,2,3]
local_ideal_cases=0
for x in range(-40,41):
    if x in roots:continue
    factors=[x-r for r in roots]
    value=math.prod(z**r for z,r in zip(factors,multiplicities))
    primes={int(p):int(t) for p,t in S.factorint(abs(value)).items()}
    for m in range(2,10):
        y=math.prod(p**(t//m) for p,t in primes.items())
        b=value//(y**m)
        for p in set(primes)|{2,3,7}:
            vals=[v(z,p) for z in factors]
            D=max(v(roots[i]-roots[j],p) for i in range(3) for j in range(i))
            c=v(b,p);E=c+sum(multiplicities)*D
            for i,(r,vi) in enumerate(zip(multiplicities,vals)):
                if vi<=D:ei=r*vi;ai=0
                else:
                    assert all(vj<=D for j,vj in enumerate(vals) if j!=i)
                    ei=c-sum(rj*vj for j,(rj,vj) in enumerate(zip(multiplicities,vals)) if j!=i)
                    ai=v(y,p)
                assert r*vi==ei+m*ai and -E<=ei<=E
                local_ideal_cases+=1

unit_rounding_cases=0
for m in range(2,32):
    for exponent in range(-100,101):
        q=(2*exponent+m)//(2*m)
        residue=exponent-m*q
        assert abs(2*residue)<=m and exponent==m*q+residue
        unit_rounding_cases+=1

# Constants used at the start of the monotone ranges.
assert 36*32**4<2**32
for p in range(5,101):
    assert 12*p*p<8*p**3
    assert 2**p>4*p
for j in range(1,13):
    z=S.expand((3+2*S.sqrt(2))**j)
    xx=int(z.coeff(S.sqrt(2),0));yy=int(z.coeff(S.sqrt(2),1))
    assert xx>=2 and yy>=2 and xx*xx-2*yy*yy==1
assert S.expand((A*X-S.Symbol('c')*B)*(A*X+S.Symbol('c')*B)-(A*A*X*X-S.Symbol('c')**2*B*B))==0

names=['../src/TR-BAKER-16.md']
tags=re.findall(r'\\tag\{([^}]+)\}',(h/names[0]).read_text(encoding='utf-8'))
assert tags==[f'16.{i}' for i in range(1,110)]
record={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed_for_drafted_components',
 'source_sha256':{n:hashlib.sha256((h/n).read_bytes()).hexdigest() for n in names},
 'signed_factorization_cases':signed_factorizations,'bounded_ideal_exponent_cases':local_ideal_cases,
 'unit_rounding_cases':unit_rounding_cases,'quadratic_counterexamples':12,
 'equation_tags':109,'proved_numbered_results':10,'solved_exercises':4,
 'limitations':'Finite calculations check algebra and selected margins, not the unrestricted theorems. The unrestricted exponent and Catalan proofs are in Lesson16; modern orientation statements are not proof inputs.'}
(h/'perfect-powers-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['manual_proof_checks','source_sha256']}))

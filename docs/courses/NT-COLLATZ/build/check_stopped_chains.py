"""Finite exact regressions for stopped chains; not a proof of an infinite statement."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from decimal import Decimal, localcontext
import json, random
ROOT=Path(__file__).resolve().parents[1]
counts=defaultdict(int)
def step(n):return (3*n+1)//2 if n%2 else n//2
def envelope(n,p,d):
    x=n;m=n.bit_length()-1
    for k in range(m+1):
        v=(x*(1<<k))**(2*d)
        if not 3**(k*d)*n**(2*(d-p))<=v<=3**(k*d)*n**(2*(d+p)):return False
        x=step(x)
    return True
for p,d in [(1,10),(1,5),(1,2)]:
    assert envelope(1,p,d)
    for m in range(1,25):
        assert not envelope(1<<m,p,d)
        counts['power_of_two_failures']+=1
    for q in range(1,11):
        a,b=1<<(q-1),1<<q
        left={n for n in range(a,b) if not envelope(n,p,d)}
        right={n for n in range(a+1,b+1) if not envelope(n,p,d)}
        if q==1:assert left==set() and right=={2}
        else:
            assert {b if n==a else n for n in left}==right
            assert {a if n==b else n for n in right}==left
        counts['exact_endpoint_exchanges']+=1
# Check the general finite preimage identity for every subset of an explicit target.
f=[0]*6+[1]*3+[2]*2+[3]
for mask in range(16):
    target={i for i in range(4) if mask>>i&1}
    total=sum(v in target for v in f)
    assert total==sum(f.count(v) for v in target)
    assert total<=6*len(target)
    counts['finite_preimage_identities']+=1
# Exact startup: a0 < 4/5 follows from 3^5 < 2^8.
r=F(15,16);p,d=1,16;eta=F(p,d);M0=28
assert 3**5<2**8
assert (r-F(4,5)-eta)*M0>=2+eta
assert r*M0>=1 and r*2**M0>=2*(M0+2)
rng=random.Random(3611)
diagnostics=[]
with localcontext() as ctx:
    ctx.prec=90
    ell=Decimal(2).ln();lam=Decimal(3).ln()/ell;g=1-lam/2
    for M in [*range(28,105,4),*range(128,321,32)]:
        L=max(M0,M//2) if M<128 else max(128,M//2)
        for n in [1<<M,(1<<(M+1))-1]+[(1<<M)+rng.getrandbits(M) for _ in range(24)]:
            x=n;path=[x];blocks=[];odd=0;prod=F(1)
            while x.bit_length()-1>=L:
                m=x.bit_length()-1
                if not envelope(x,p,d):break
                q=r.numerator*m//r.denominator;Y=1<<q;h=0
                while x>Y:
                    old=x;x=step(x);h+=1;path.append(x)
                    if old%2:
                        odd+=1;prod*=F(2*x-1,2*x)
                    assert h<=m
                assert Y//2<x<=Y
                assert all(v>Y for v in path[:-1])
                assert x.bit_length()-1<=q<m
                blocks.append((m,q,h));counts['controlled_blocks']+=1
            h=len(path)-1
            assert h<F(M,1-r)
            assert max(path)**d<=n**(d+p)
            assert F((1<<h)*x,3**odd)*prod==n
            counts['stopped_runs']+=1
            if blocks:
                q=blocks[-1][1]
                loss=sum((F(1,2*path[k+1]) for k in range(h) if path[k]%2),F(0))
                assert (1<<q)*loss < F(2*(q+2),3*r)
                counts['rank_scaled_losses']+=1
            if x.bit_length()-1<L:
                counts['successful_runs']+=1
                j=len(blocks)-1
                assert j>=0
                assert all(blocks[i][0]==blocks[i-1][1]-1 for i in range(1,len(blocks)))
                assert sum(m-q for m,q,hb in blocks)==M-blocks[-1][1]-j
                assert 3**odd<2**(h-M+L)
                ordinary=[n]
                for old,new in zip(path,path[1:]):
                    if old%2:ordinary.append(3*old+1)
                    ordinary.append(new)
                assert len(ordinary)-1==h+odd
                assert max(ordinary)**d<=2**d*n**(d+p)
                rhs=F(M)-r*L+eta*M/(1-r)+(1+eta)*j+3+eta
                assert g*h<Decimal(rhs.numerator)/Decimal(rhs.denominator)
                diagnostics.append(dict(M=M,L=L,blocks=j+1,shortcut=h,odd_inputs=odd))
for L in range(1,21):
    for j in range(60):
        assert F(L+j+1,L+1)<=(j+1)**2
        counts['square_root_majorants']+=1
    for z in [F(1,2),F(2,3),F(9,10)]:
        assert sum((j+1)*z**j for j in range(100))<=1/(1-z)**2
        counts['geometric_majorants']+=1
assert counts['successful_runs']>0 and counts['controlled_blocks']>0
out=dict(passed=True,counts=dict(counts),
         exact_scope="Integer-power orbit envelopes, explicit endpoint bijections, finite preimage identities, rational rank and reverse-product identities, actual stopped paths and clock expansion. Bounded samples only.",
         diagnostics=dict(precision_digits=90,rank_clock_inequalities=len(diagnostics),scope="Decimal logarithm comparisons are numerical diagnostics, not exact or infinite proofs."),
         formal_status="No Lean replay or independent certificate.")
(ROOT/'checks/stopped_chains.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))


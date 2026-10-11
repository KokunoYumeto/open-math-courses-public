"""Exact finite regressions for reverse transport. Not proofs of infinite claims."""
from fractions import Fraction as F
from collections import defaultdict
from math import floor,ceil
import json

def T(n): return n//2 if n%2==0 else (3*n+1)//2
def C(n): return n//2 if n%2==0 else 3*n+1
def path(n,Y,step=T,limit=600):
    xs=[n]
    while xs[-1]>Y and len(xs)<=limit: xs.append(step(xs[-1]))
    return xs if xs[-1]<=Y else None
def data(xs):
    h=len(xs)-1;s=0;b=F(0);L=F(0);P=F(1)
    for x,z in zip(xs,xs[1:]):
        p=x%2
        assert z==T(x)
        s+=p;b=(3**p*b+p)/2
        u=F(p,2*z);L+=u;P*=1-u
    A=F(2**h*xs[-1],3**s)
    assert xs[-1]==F(3**s*xs[0],2**h)+b
    assert xs[0]==A*P
    assert 0<=1-P<=L
    assert 1-P==b/xs[-1]
    return h,s,A,b,L,P
counts=defaultdict(int); groups=defaultdict(list)
Ys=[F(3,2),F(2),F(4),F(8),F(16),F(32),F(64)]
for n in range(2,513):
    for Y in Ys:
        if n<=Y: continue
        xs=path(n,Y)
        assert xs is not None # Finite tested population only.
        h,s,A,b,L,P=data(xs); counts['finite_first_passages']+=1
        assert Y/2<xs[-1]<=Y and xs[-2]%2==0 and s<=h-1
        o=floor(Y)+1
        if o%2==0:o+=1
        assert Y*L<=F(Y*s,3*o+1)<=F(Y*(h-1),3*o+1)<F(h,3)
        M=n.bit_length()-1
        if Y<2**M:
            groups[M,Y].append((n,h,xs[-1],s,A,L,P))
        for k in sorted(set([0,1,h//2,h-1,h])):
            d1=data(xs[:k+1]);d2=data(xs[k:]);Y1=F(5);Y2=F(3,2)
            L1,P1=d1[-2:]; L2,P2=d2[-2:]
            G1=Y1*(1-P1);G2=Y2*(1-P2)
            assert L==L1+L2 and P==P1*P2
            assert Y2*L==Y2/Y1*(Y1*L1)+Y2*L2
            assert Y2*(1-P)==Y2/Y1*G1+G2-G1*G2/Y1
            counts['concatenations']+=1
        if n%2:
            odd=[n];vals=[]
            while odd[-1]>Y:
                v=3*odd[-1]+1;a=0
                while v%2==0:v//=2;a+=1
                vals.append(a);odd.append(v)
            y=xs[-1];d=0;u=y
            while u%2==0:u//=2;d+=1
            assert odd[-1]==u and len(vals)==s and h+d==sum(vals)
            dinv=0
            while 2**(dinv+1)*u<=Y:dinv+=1
            assert dinv==d and 2**d*u==y
            raw=path(n,Y,C)
            assert len(raw)-1==h+s and raw[-1]==y
            p2=F(1);l2=F(0)
            for v in odd[:-1]:p2*=F(3*v,3*v+1);l2+=F(1,3*v+1)
            assert l2==L and p2==P
            counts['exact_clock_records']+=1

for (M,Y),rows in groups.items():
    for eps in [F(0),F(1,24),F(1,12),F(1,6),F(1,3)]:
        fibres=defaultdict(list)
        for row in rows:
            if 1-row[-1]<=eps:fibres[row[1],row[2]].append(row)
        for tag,rs in fibres.items():
            assert len({v[3] for v in rs})==1
            A=rs[0][4]
            candidate=max(0,min(2**(M+1)-1,floor(A))-max(2**M,ceil((1-eps)*A))+1)
            assert len(rs)<=candidate<=1+floor(eps*(2**(M+1)-1))
            counts['nonempty_defect_fibres']+=1
            if len(rs)>1:counts['multiple_source_fibres']+=1
        for time_mod in [1,2,3]:
            S={v[1] for v in rows if v[1]%time_mod==0}
            B={v[2] for v in rows if v[2]%2==0}
            for restricted in [False,True]:
                selected=[v for v in rows if v[1] in S and v[2] in B
                          and v[-2]<=eps and (not restricted or v[0]%3==1)]
                K=len(S)*len(B)*(1+floor(eps*(2**(M+1)-1)))
                assert len(selected)<=K
                counts['restricted_transport_sets']+=1

for n in range(5,513):
    qs=list(range(n.bit_length()-1,0,-1))
    if 2**qs[0]>=n:qs=qs[1:]
    if not qs:continue
    blocks=[];start=n
    for qj in qs:
        xs=path(start,2**qj);assert len(xs)>1
        blocks.append((qj,xs,data(xs)));start=xs[-1]
    r=min(F(qj+1,d[0]+1) for qj,xs,d in blocks)
    for i in range(len(blocks)):
        retained=blocks[:i+1];q=retained[-1][0];Y=2**q
        joined=list(retained[0][1])
        for _,xs,_ in retained[1:]:joined.extend(xs[1:])
        assert joined==path(n,Y)
        E=Y*data(joined)[-2]
        odd_bound=sum(F(Y*d[1],3*2**qj+4) for qj,xs,d in retained)
        weighted=sum(F(d[0],3)*F(2)**(q-qj) for qj,xs,d in retained)
        assert E<=odd_bound<weighted<F(2*(q+2),3)/r
        counts['rank_chain_prefixes']+=1

for M in range(1,10):
    for eps in [F(j,90) for j in range(31)]:
        A=2**(M+1)-1
        assert ceil((1-eps)*A)>=2**M
        assert A-ceil((1-eps)*A)+1==1+floor(eps*A)
        counts['interval_sharpness_cases']+=1
for N in range(31):
    assert sum(F(1,2**d) for d in range(N+1))==2-F(1,2**N)
    assert sum(F(d,2**d) for d in range(N+1))==2-F(N+2,2**N)
    counts['finite_geometric_sums']+=1

d=data(path(3,F(3,2)))
assert d[0:2]==(5,2) and d[2]==F(32,9) and d[3]==F(5,32)
assert 1-d[-1]==F(50,320)<F(51,320)<d[-2]==F(52,320)
assert F(3,2)*(1-d[-1])==F(15,64)
assert len(path(7,4))-1==9 and len(path(7,4,C))-1==14
assert len(path(7,6))-1==7 and len(path(7,6,C))-1==11
assert counts['multiple_source_fibres']>0
print(json.dumps(dict(passed=True,arithmetic="exact integer and Fraction",counts=dict(counts),
    scope="Finite regression tests of the written identities and inequalities. No inference about untested or infinite populations, no Lean replay.",
    exercise_checks=4),indent=2))

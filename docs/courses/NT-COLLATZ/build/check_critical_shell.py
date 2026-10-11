"""Exact bounded regressions for critical shell assembly, not an infinite proof."""
from fractions import Fraction as F
from collections import Counter
from decimal import Decimal,localcontext
import json,random
counts=Counter()
def step(n):return (3*n+1)//2 if n%2 else n//2
def envelope(n,a=1,b=16):
    """eta=a/b: square both sides then raise to b, using integers only."""
    x=n;m=n.bit_length()-1
    for j in range(m+1):
        left=2**(2*b*j)*x**(2*b)
        base=3**(b*j)
        if not base*n**(2*b-2*a)<=left<=base*n**(2*b+2*a):return False
        x=step(x)
    return True
for m in range(1,11):
    bad={n for n in range(2**m,2**(m+1)) if not envelope(n,1,16)}
    band={n for n in range(2**m+1,2**(m+1)+1) if not envelope(n,1,16)}
    assert 2**m in bad and 2**(m+1) in band
    assert (bad-{2**m})|{2**(m+1)}==band
    counts["exact_moving_band_exchanges"]+=1
for M in range(4,1001):
    for r in [F(4,5),F(7,8),F(19,20)]:
        for S in [2,5,17,51]:
            m=M;qs=[]
            while m>=S:
                q=(r*m)//1
                if q<=S:break
                qs.append(q);m=q-1
            assert len(qs)==len(set(qs))
            assert sum(qs)<=r*M/(1-r)
            assert sum(F(2)**(q-M) for q in qs)<1
            lhs=sum(F(2)**(q-M)+4*F(q+2,3)/r for q in qs)
            rhs=1+4/(3*r)*(r*M/(1-r)+2*len(qs))
            assert lhs<=rhs
            counts["exact_rank_charge_bounds"]+=1

rng=random.Random(61011)
records=[]
for M in [256,384,512,768,1024]:
    S=192;L=48;K0=F(2);r=F(7,8)
    starts=[2**M,2**(M+1)-1]+[rng.randrange(2**M,2**(M+1)) for _ in range(24)]
    for n in starts:
        x=n;values=[n];blocks=[];state="active";high=True
        while state=="active":
            m=x.bit_length()-1
            if x<2**L:state="success";break
            if high and not envelope(x):
                state="initial_bad" if not blocks else "high_bad";break
            q=(r*m)//1 if high else ((1-K0/(2*L))*m)//1
            block=[x];bits=[]
            for h in range(1,m+1):
                bits.append(x%2);x=step(x);block.append(x)
                if x<=2**q:break
            else:
                state="high_no_passage" if high else "low_timeout";break
            assert 2**(q-1)<x<=2**q
            assert all(v>2**q for v in values+block[1:-1])
            if blocks:assert q<blocks[-1]["q"]
            blocks.append({"m":m,"q":q,"h":h,"bits":bits,"high":high})
            values+=block[1:];counts["actual_first_passage_blocks"]+=1
            if x==2**q:
                if high and q>S:state="high_endpoint";break
                while x>=2**L:
                    a=x.bit_length()-1; x//=2;values.append(x)
                    blocks.append({"m":a,"q":a-1,"h":1,"bits":[0],"high":False})
                state="success";break
            if high and x.bit_length()-1<S:high=False
        assert state!="high_no_passage",(M,n)
        counts["classified_actual_sources"]+=1
        if state!="success":continue
        k=len(values)-1;s=sum(sum(b["bits"]) for b in blocks)
        raw=[n]
        for v in values[:-1]:
            if v%2:raw.append(3*v+1)
            raw.append(step(v))
        assert len(raw)-1==k+s and raw[-1]==values[-1]
        qf=blocks[-1]["q"];y=values[-1]
        assert F(L)-K0/2-1<=qf<=L and y<2**L
        assert all(v>2**qf for v in values[:-1])
        P=F(1);loss=F(0)
        for v in values[:-1]:
            if v%2:P*=F(3*v,3*v+1);loss+=F(1,3*v+1)
        assert F(n)==F(2**k*y,3**s)*P
        assert 1-P<=loss< F(2*(qf+2),3)/F(1,2)/2**qf
        first=blocks[0];prod=F(1);mx=F(1)
        for bit in first["bits"]:
            prod*=F(3 if bit else 1,2);mx=max(mx,prod)
        rawfirst=[n]
        for v in values[:first["h"]]:
            if v%2:rawfirst.append(3*v+1)
            rawfirst.append(step(v))
        assert max(rawfirst)<=F(7,3)*n*mx
        if M>=2*S+2 and mx<=F(12,7):
            assert max(raw)<=4*n
            counts["complete_relative_height_records"]+=1
        highblocks=[b for b in blocks if b["high"]]
        qent=highblocks[-1]["q"];H=sum(b["h"] for b in highblocks)
        assert L+1<=qent<=S
        V=(S-L)*(S+L-1)//2
        assert k-H<=V+S
        counts["complete_common_endpoint_records"]+=1
        records.append((M,n,k,s,y,P,qent,H))

with localcontext() as ctx:
    ctx.prec=90;D=Decimal
    ln2=D(2).ln();ln3=D(3).ln();lam=ln3/ln2;a0=lam/2;g=1-a0
    tau=D(1)/16;r=D(7)/8;diag=0
    for M,n,k,s,y,P,qent,H in records:
        MM=D(M);V=D(M+2).ln()
        # D_hi=1 and capped t_m=1/16 on all tested ranks, as checked below.
        assert (V/MM).sqrt()>=tau
        J=1+int(MM.ln()/(1/r).ln())
        E=(MM*V).sqrt()/(1-r.sqrt())+(tau+3)*J
        assert abs(g*D(H)-(MM+1-D(qent)))<=E
        assert abs(g*D(k)-MM)<=E+193+g*D((192-48)*(192+48-1)//2+192)
        logP=D(P.numerator).ln()-D(P.denominator).ln()
        rhs=(g*D(k)*ln2-D(n).ln()+D(y).ln()+logP)/ln3
        assert abs(rhs-(D(s)-D(k)/2))<D("1e-80")
        diag+=1
    # Explicit asymptotic inequalities, sampled only as numerical diagnostics.
    p=ln2/ln3;kappa=1+(p*p.ln()+(1-p)*(1-p).ln())/ln2
    Astar=1/(2*kappa)
    for M in [10**3,10**6,10**12,10**24]:
        MM=D(M);V=D(M+2).ln()
        for A in [Astar,Astar+1,2*Astar]:
            w=V.sqrt();L=int((A*(MM*ln2).ln()+w.ln())/ln2)
            e=( (MM+2)*V/D(L+1) ).sqrt()*(-kappa*D(L)*ln2).exp()
            expected=(kappa*ln2).exp()*((MM+2)*V/D(L+1)).sqrt()*(-kappa*A*(MM*ln2).ln()-kappa*w.ln()).exp()
            assert e<=expected+D("1e-80")
            diag+=1
assert counts["complete_common_endpoint_records"]>0
print(json.dumps({"passed":True,"counts":dict(counts),
 "exact_scope":"Exact endpoint-exchange sets, geometric rank charges, actual finite high/low paths, endpoint cases, reverse products, common ordinary/shortcut endpoints and finite height comparison. Tested chains use a fixed rational cap; these samples do not certify asymptotic density.",
 "diagnostics":{"precision_digits":90,"cases":diag,"scope":"Real-valued clock comparisons and rounded critical scales; numerical diagnostics, not formal certificates."},
 "formal_status":"General results are proved in the lesson. No independent review or Lean replay."},indent=2))


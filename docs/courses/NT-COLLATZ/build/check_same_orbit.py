"""Exact finite checks of same-orbit joining; not an asymptotic proof."""
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
from collections import Counter
import json
def valuation(x):
    a=0
    while x%2==0:a+=1;x//=2
    return a
def odd_path(u):
    xs=[u]
    while xs[-1]!=1:
        assert len(xs)<2000
        x=xs[-1];xs.append((3*x+1)//2**valuation(3*x+1))
    xs.extend([1,1,1])
    return xs
def expanded(n,xs):
    a=valuation(n);u=n//2**a
    ts=[n];cs=[n]
    for j in range(a):ts.append(ts[-1]//2);cs.append(cs[-1]//2)
    it=[a];ic=[a];A=[0]
    for x,y in zip(xs,xs[1:]):
        b=valuation(3*x+1)
        assert y==(3*x+1)//2**b
        cs.append(3*x+1);ts.append((3*x+1)//2);cs.append((3*x+1)//2)
        for j in range(b-1):ts.append(ts[-1]//2);cs.append(cs[-1]//2)
        A.append(A[-1]+b);it.append(len(ts)-1);ic.append(len(cs)-1)
    assert all(ts[it[j]]==cs[ic[j]]==x for j,x in enumerate(xs))
    return a,A,it,ic,ts,cs
counts=Counter();diag=Counter()
with localcontext() as ctx:
    ctx.prec=90
    l2=D(2).ln();l3=D(3).ln();drift=l2-l3/2
    for n in range(1,385):
        a=valuation(n);u=n//2**a;xs=odd_path(u)
        a,A,it,ic,ts,cs=expanded(n,xs)
        logn=D(n).ln(); logxs=[D(x).ln() for x in xs]
        logts=[D(x).ln() for x in ts]
        prefix_errors=[];running=D(0)
        for j,lx in enumerate(logts):
            running=max(running,abs(lx-logn+drift*j));prefix_errors.append(running)
        for target in sorted(set([2,3,5,7,11,u,u+1])):
            if target<2:continue
            sig=next(j for j,x in enumerate(xs) if x<=target)
            assert len(set(xs[:sig]))==sig and all(x>target for x in xs[:sig])
            cost=sum((F(1,x) for x in xs[:sig]),F())
            assert cost<=sum((F(1,3+2*j) for j in range(sig)),F())
            counts['distinct_first_entrance_costs']+=1
            for q in range(min(12,len(xs)-1)+1):
                z=xs[q];V=xs[sig]
                assert it[sig]==a+A[sig] and ic[sig]==a+sig+A[sig]
                counts['marked_records']+=1
                if sig<=q:
                    assert it[sig]<=it[q] and ic[sig]<=ic[q]
                    assert max(cs[:ic[sig]+1])<=max(cs[:ic[q]+1])
                    counts['truncations']+=1
                    if sig==q:counts['zero_tails']+=1
                    continue
                r=sig-q;v=A[sig]-A[q]
                product=F(z)
                for x in xs[q:sig]:product*=3+F(1,x)
                assert product==2**v*V and product<=4**r*z
                assert it[sig]-it[q]==v and ic[sig]-ic[q]==r+v
                assert max(cs[ic[q]:ic[sig]+1])<=2**(r+1)*z
                counts['exact_tail_products']+=1
                counts['exact_tail_heights']+=1
                # All below are explicitly numerical logarithmic diagnostics.
                assert D(v)<=2*r+logxs[q]/l2+D('1e-80')
                ep=prefix_errors[it[q]]
                radius=ep+(r+1)*l2+2*logxs[q]+drift*(2*r+logxs[q]/l2)
                actual=prefix_errors[it[sig]]
                assert actual<=radius+D('1e-78')
                diag['whole_path_gluing_bounds']+=1
                Q=logn/(2*drift);E=abs(D(q)-Q);Fup=max(D(0),D(sig)-Q)
                assert D(r)<=E+Fup+D('1e-78')
                diag['difference_of_clock_bounds']+=1
    for X in range(1,4097):
        J=X.bit_length()-1
        assert sum(2**m for m in range(J+1))<2*X
        counts['whole_and_partial_shells']+=1
    ex=odd_path(7);a,A,it,ic,ts,cs=expanded(56,ex)
    assert ex[:6]==[7,11,17,13,5,1]
    assert (it[2],ic[2],it[4],ic[4])==(5,7,10,14)
    assert max(cs[ic[2]:ic[4]+1])==52
    illustration=dict(n=56,odd_values=ex[:5],shortcut_times=it[:5],ordinary_times=ic[:5],
                      mark=2,target=5,first_target_index=4,tail_shortcut=5,tail_ordinary=7,
                      actual_tail_height=52,proved_tail_height_bound=136)
assert counts['exact_tail_products'] and counts['truncations'] and counts['zero_tails']
print(json.dumps(dict(passed=True,counts=dict(counts),illustration=illustration,
 exact_scope='Bounded actual positive-integer paths, exact marked time maps, truncation, continuation products, heights, distinct first-entrance costs and full/partial shell sums.',
 diagnostics=dict(precision_digits=90,counts=dict(diag),scope='Logarithmic path radii and clock subtraction only; numerical diagnostics, not formal certificates.'),
 formal_status='General results have written proofs self-checked by the writing AI. No density statement follows from these finite tests; no new Lean replay or independent review.'),indent=2))


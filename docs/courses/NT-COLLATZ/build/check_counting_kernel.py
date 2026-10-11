"""Exact finite checks for counting kernels and weighted error transfer.

Asymptotic mixing and kernel estimates are proved in the lesson, not inferred
from these samples. Geometric residue laws below include their infinite tails.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import json


def compositions(s,r):
    if r==1:
        if s>=1:
            yield (s,)
        return
    for a in range(1,s-r+2):
        for tail in compositions(s-a,r-1):
            yield (a,)+tail


def floor_log2(value):
    assert value>0
    n,d=value.numerator,value.denominator
    k=n.bit_length()-d.bit_length()
    scale=F(2**k) if k>=0 else F(1,2**(-k))
    return k if scale<=value else k-1


def choose(n,r):
    return comb(n,r) if n>=r else 0


def kernel_term(r,M,Y,U):
    h=floor_log2(F(3**r)*U/M)
    k=floor_log2(F(3**r)*Y/M)
    return F(choose(h,r)-choose(k,r),3**r)


def coordinate(word):
    total=c=0
    for a in word:
        c=3*c+2**total
        total+=a
    return total,c


def good(word,width):
    t=0
    for j,a in enumerate(word,1):
        t+=a
        if abs(t-2*j)>=width:
            return False
    return True


@lru_cache(None)
def histogram(r,s,bad_width=None):
    q=3**r
    out=[0]*q
    for word in compositions(s,r):
        if bad_width is not None and good(word,bad_width):
            continue
        total,c=coordinate(word)
        out[c*pow(2**total,-1,q)%q]+=1
    return tuple(out)


@lru_cache(None)
def rho(k):
    if k==0:
        return (F(1),)
    q=3**k
    period=2*3**(k-1)
    old=rho(k-1)
    out=[F(0)]*q
    for a in range(1,period+1):
        # Sum all positive exponents in this congruence class, not a truncation.
        mass=F(2**(period-a),2**period-1)
        inverse=pow(2**a,-1,q)
        for z,w in enumerate(old):
            out[inverse*(1+3*z)%q]+=mass*w
    assert sum(out)==1
    return tuple(out)


def itinerary(n,r):
    word=[]
    for _ in range(r):
        h=3*n+1
        a=(h & -h).bit_length()-1
        n=h//2**a
        word.append(a)
    return tuple(word),n


def main():
    counts=dict(cutoffs=0,kernel_identities=0,compositions=0,full_residue_laws=0,
                weighted_transfers=0,weighted_pairs=0,bad_word_transfers=0,
                exact_normalizations=0,integer_fibre_counts=0)
    for n in range(1,101):
        for d in range(1,31):
            x=F(n,d)
            k=floor_log2(x)
            lo=F(2**k) if k>=0 else F(1,2**(-k))
            assert lo<=x<2*lo
            counts['cutoffs']+=1
    for r in range(1,5):
        for h in range(-3,20):
            direct=sum(choose(s-1,r-1) for s in range(r,h+1))
            assert direct==choose(h,r)
            if h>=r:
                assert F(choose(h,r),3**r)==F(2**h,3**r)*F(h,r)*F(choose(h-1,r-1),2**h)
            counts['kernel_identities']+=1
        for s in range(r,12):
            assert sum(histogram(r,s))==choose(s-1,r-1)
            counts['compositions']+=1
        for M,Y,U in product([F(1),F(13),F(401)], [F(1),F(100)], [F(1000),F(2048)]):
            h=floor_log2(F(3**r)*U/M)
            direct=sum((F(choose(s-1,r-1),3**r) for s in range(r,h+1)
                        if Y<F(2**s)*M/3**r<=U),F(0))
            assert direct==kernel_term(r,M,Y,U)
            counts['kernel_identities']+=1
    for k in range(5):
        assert sum(rho(k))==1
        if k:
            projected=[sum(rho(k)[z::3**(k-1)]) for z in range(3**(k-1))]
            assert tuple(projected)==rho(k-1)
        counts['full_residue_laws']+=1

    sets=[
        (list(range(401,454,2)),1),
        (sorted(set(range(1,102,4))|set(range(27,101,8))),2),
        (list(range(9,172,18)),10),
    ]
    for (E,P),(Y,U),I in product(sets,[(F(3),F(57)),(F(100),F(1000)),(F(362),F(363))],
                                [(1,2),(2,3)]):
        B=min(E); R=max(I)
        K=sum((2*kernel_term(r,F(M),Y,U)/U for M in E for r in I),F(0))
        pop=F(0); uniform=F(0); weighted=F(0); bad=F(0)
        eps=F(0); delta=F(0)
        for r in I:
            q=3**r
            h=floor_log2(F(q)*U/B)
            for s in range(r,h+1):
                selected=[M for M in E if Y<F(2**s*M,q)<=U]
                if not selected:
                    continue
                N=len(selected); nu=[0]*q
                for M in selected:
                    nu[M%q]+=1
                assert max(abs(n-F(N,q)) for n in nu)<=P
                C=choose(s-1,r-1)
                hist=histogram(r,s)
                k=min(r,2)
                lifted=[rho(k)[z%(3**k)]/3**(r-k) for z in range(q)]
                errors=[F(hist[z],C)-lifted[z] for z in range(q)]
                norm=sum(map(abs,errors))
                eps=max(eps,norm)
                weighted+=2*C/U*sum((nu[z]*abs(errors[z]) for z in range(q)),F(0))
                bhist=histogram(r,s,2)
                fraction=F(sum(bhist),C)
                delta=max(delta,fraction)
                bad+=2/U*sum(n*b for n,b in zip(nu,bhist))
                pop+=2*P*C/U
                uniform+=2*C*F(N,q)/U
                counts['weighted_pairs']+=1
        assert uniform==K
        assert pop<=F(2*P*3**R*len(I),B)
        assert weighted<=eps*(K+pop)
        assert bad<=delta*(K+pop)
        counts['weighted_transfers']+=1
        counts['bad_word_transfers']+=1

    for Y,U in [(F(5),F(59)),(F(11),F(11)),(F(21,2),F(121,2))]:
        inputs=[n for n in range(1,62,2) if Y<=n<=U]
        h=len(inputs)
        assert h>0
        for E in [set(range(1,61,2)),{1,5,13,17,25,41}]:
            actual={M:F(0) for M in E}; scaled=actual.copy()
            for r in range(1,4):
                expected={}
                for n in inputs:
                    word,M=itinerary(n,r)
                    if M in E and good(word,3):
                        expected[(word,M)]=expected.get((word,M),0)+1
                        actual[M]+=F(1,h)
                        scaled[M]+=2/U
                found={}
                # The actual valuation telescope bounds total<=log2(U)+2r.
                top=floor_log2(U)+2*r
                for s in range(r,top+1):
                    for word in compositions(s,r):
                        if not good(word,3):
                            continue
                        _,c=coordinate(word)
                        for M in E:
                            n=F(2**s*M-c,3**r)
                            if n.denominator==1 and n%2==1 and Y<=n<=U:
                                found[(word,M)]=1
                assert found==expected
                counts['integer_fibre_counts']+=1
            distance=sum(abs(actual[M]-scaled[M]) for M in E)
            assert distance<=3*(Y+2)/U
            counts['exact_normalizations']+=1

    example=sum((kernel_term(r,F(13),F(100),F(1000)) for r in (1,2)),F(0))
    assert example==F(10,3)
    words=list(compositions(5,3))
    bad_words=[w for w in words if not good(w,2)]
    assert bad_words==[(1,1,3)]
    assert good((3,1,1),2) and not good((1,1,3),2)
    assert F(coordinate((3,1,1))[1],32)==F(49,32)
    assert F(coordinate((1,1,3))[1],32)==F(19,32)
    assert F(10,10)==1 and F(10,9)*F(1,5)==F(2,9)
    result=dict(passed=True,arithmetic="Exact integers and fractions; complete geometric residue tails",
                counts=counts,
                examples={'kernel':'10/3','nonuniform_weighted_error':'1',
                          'incorrect_average_weight':'2/9','bad_prefix_fraction':'1/6',
                          'forward_offsets':['49/32','19/32']},
                scope="Finite regression of exact kernel identities, counting weights, full residue laws, integer inverses and normalization. The all-parameter analytic estimates are proved in the lesson.",
                lean_certification=False)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()


"""Finite exact regressions and separately labelled 70-digit diagnostics.

No finite enumeration establishes an asymptotic or universal orbit result.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json
import mpmath as mp
mp.mp.dps=70

def step(n):
    v=3*n+1; a=(v&-v).bit_length()-1
    return v>>a,a

def word(n,h):
    states=[n];bs=[]
    for _ in range(h):
        n,a=step(n);states.append(n);bs.append(a)
    return tuple(bs),states

def residue(bs):
    r=1;power=2
    for a in reversed(bs):
        power*=2**a
        r=((2**a*r-1)*pow(3,-1,power))%power
    return r,power

def run():
    counts=dict(cylinder_samples=0,crt_samples=0,first_passage_members=0,
                fibre_partitions=0,interval_checks=0,progression_diagnostics=0,
                sharp_fibre_diagnostics=0,weighted_tail_diagnostics=0)
    ell=mp.log(2);alpha=(1-mp.log(mp.mpf(3)/2))/2;C=alpha+ell
    def real(x):return mp.mpf(x.numerator)/x.denominator
    for h in range(1,5):
        for bs in product(range(1,5),repeat=h):
            r,P=residue(bs);assert P==2**(sum(bs)+1) and r%2
            for j in range(3):
                assert word(r+j*P,h)[0]==bs
                counts['cylinder_samples']+=1
            for q in range(3):
                m=3**q
                for x in range(m):
                    t=((x-r)*pow(P,-1,m))%m if m>1 else 0
                    R=r+P*t
                    assert R%m==x and R%P==r and word(R,h)[0]==bs
                    counts['crt_samples']+=1
    for B in [20,64,256,4096]:
        for h in range(1,4):
            if 2*3**(h-1)>B:continue
            endpoints=[]
            for M in range(1,12001,2):
                bs,states=word(M,h)
                if min(states[:-1])>B and states[-1]<=B:
                    endpoints.append((M,bs));counts['first_passage_members']+=1
            for q in range(3):
                groups={}
                for M,bs in endpoints:groups.setdefault((bs,M%3**q),[]).append(M)
                for x in range(3**q):
                    lhs=sum((F(3**q,M) for M,b in endpoints if M%3**q==x),F())
                    rhs=sum((sum((F(3**q,M) for M in values),F())
                             for (bs,y),values in groups.items() if y==x),F())
                    assert lhs==rhs;counts['fibre_partitions']+=1
                for (bs,x),values in groups.items():
                    s=sum(bs);a=bs[-1];sm=s-a
                    A0=B*2**sm//(2*3**(h-1))+1
                    U=B*2**s//3**h
                    A1=max(A0,2**s//(8*3**(h-1))+1)
                    P=2**(s+1);Q=P*3**q;r,_=residue(bs)
                    for M in values:
                        assert A1<=M<=U and M%P==r
                        assert B*2**sm<2*3**(h-1)*M
                        assert 3**h*M<=B*2**s and 2**s<8*3**(h-1)*M
                        counts['interval_checks']+=1
                    assert 3*U<2**(a+1)*A0
                    mass=sum((F(1,M) for M in values),F())
                    for A in [A0,A1]:
                        bound=mp.mpf(1)/A+mp.log(mp.mpf(U)/A)/Q
                        assert real(mass)<=bound+mp.mpf('1e-60')
                        counts['progression_diagnostics']+=1
                    high=2**(2*s)>B
                    if high or Q<A0:
                        base=(alpha+a*ell/2)/2**s
                        bound=base+(mp.mpf(3)*3**(h+q)/2**s if high else 0)
                        assert 3**q*real(mass)<=bound+mp.mpf('1e-60')
                        counts['sharp_fibre_diagnostics']+=1
    def rate(z):return (1+z)*mp.log(1+z)-(2+z)*mp.log(1+z/2)
    # Exact full-event masses via finite complements, not truncated infinite tails.
    for h in range(2,15):
        for u in [1,3,7]:
            upper=C-sum((mp.mpf(comb(s-1,h-1))/2**s*(alpha+ell*s/(2*h))
                         for s in range(h,2*h+u+1)),mp.mpf(0))
            bound=(C+ell*u/(2*h))*mp.exp(-h*rate(mp.mpf(u)/h))
            assert 0<=upper<=bound+mp.mpf('1e-60')
            counts['weighted_tail_diagnostics']+=1
        for v in [mp.mpf('0.25'),mp.mpf(h-1)/2]:
            k=h-1;threshold=2*k-v
            lower=C*sum((mp.mpf(comb(s-1,k-1))/2**s
                         for s in range(k,int(mp.ceil(threshold)))),mp.mpf(0))
            bound=C*mp.exp(-k*rate(-v/k))
            assert 0<=lower<=bound+mp.mpf('1e-60')
            counts['weighted_tail_diagnostics']+=1
    bs,states=word(33,2);assert bs==(2,2) and states==[33,25,19]
    assert residue(bs)==(1,32) and F(3,33)==F(1,11)
    assert F(1,33)*2==F(2,33)
    return dict(passed=True,counts=counts,
      exact_scope='Integer trajectories, cylinder/CRT classes, inclusive/strict rounding, disjoint fibre sums and worked examples.',
      numerical_scope='70-digit reciprocal/logarithm bounds, sharper fibre envelope, and full weighted upper/lower event masses computed by finite complements. Not interval certificates.',
      theorem_scope='General finite and asymptotic statements are proved in lesson29; no Lean build or infinite-orbit test.',
      constants=dict(total_weight=str(C),exterior_leading=str(2*C)))

if __name__=='__main__':print(json.dumps(run(),indent=2))

"""Finite regression checks for mass-height averaging and sharp kernels.

All-parameter proofs are in the lesson. Exact rational checks are separated
from high-precision numerical diagnostics; neither is Lean certification.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import comb, isqrt
from pathlib import Path
import json
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]

def interval_constant_squared(a):
    return max(F(sum(a[i:j])**2,j-i)
               for i in range(len(a)) for j in range(i+1,len(a)+1))

def profiles(n):
    for peak in range(n):
        w=tuple(F(min(i+1,n-i,peak+1)) for i in range(n))
        yield w
        w=tuple(F(1+min(i,peak)-max(0,i-peak),n+3) if i<=2*peak+1 else F(0)
                for i in range(n))
        # Retain only nonnegative sequences with interval superlevel sets.
        if min(w)>=0:
            yield w
    yield (F(1,n),)*n
    yield tuple(F(i+1,n*n) for i in range(n))
    yield tuple(F(n-i,n*n) for i in range(n))

def exact_checks():
    counts=Counter()
    for n in range(1,17):
        for w in set(profiles(n)):
            if not any(w): continue
            levels=sorted(set(w)|{F(0)})
            H=max(w); M=sum(w)
            layers=[]
            for lo,hi in zip(levels,levels[1:]):
                indices=[i for i,x in enumerate(w) if x>lo]
                assert indices==list(range(min(indices),max(indices)+1))
                layers.append((hi-lo,indices))
            assert sum(d*len(I) for d,I in layers)==M
            for a in [tuple((-1)**i for i in range(n)),
                      tuple((i*i+3*i)%7-3 for i in range(n)),
                      tuple((i%3)-1 for i in range(n))]:
                weighted=sum(x*y for x,y in zip(w,a))
                assert weighted==sum(d*sum(a[i] for i in I) for d,I in layers)
                A2=interval_constant_squared(a)
                assert weighted**2<=A2*H*M
                counts['exact_mass_height_bounds']+=1
                counts['exact_layer_identities']+=1
            counts['profiles']+=1
    for R in range(2,25):
        a=[(-1)**n for n in range(1,2*R+1)]
        w=[F(1,R) if n%2==0 else F(0) for n in range(1,2*R+1)]
        assert sum(w)==1 and max(w)==F(1,R)
        assert sum(x*y for x,y in zip(w,a))==1
        assert interval_constant_squared(a)==1
        assert 1>max(w)*sum(w)
        counts['nonunimodal_counterexamples']+=1
    for r in range(1,20):
        for h in range(r,4*r+1):
            assert F(comb(h,r),2**h)==F(h,r)*F(comb(h-1,r-1),2**h)
            counts['binomial_identities']+=1
    return dict(counts)

def floor_sqrt2_times(d):
    if d==0: return 0
    k=isqrt(2*d*d)
    assert k*k<2*d*d<(k+1)*(k+1)
    return k if d>0 else -k-1

def diagnostics():
    mp.mp.dps=60
    lam=mp.sqrt(2); a=2-lam
    out=[]
    for L in (16,32,64,128,256):
        u=a*L; u0=u-L
        mass=mp.mpf(0)
        for r in range((L+1)//2,2*L+1):
            h=2*L+floor_sqrt2_times(r-L)
            k=h-L
            assert h==int(mp.floor(r*lam+u))
            assert k==int(mp.floor(r*lam+u0))
            upper=comb(h,r) if h>=r else 0
            lower=comb(k,r) if k>=r else 0
            mass+=mp.power(2,-r*lam-u)*(upper-lower)
        target=1/(a*mp.log(2))
        out.append(dict(L=L,scaled_kernel=mp.nstr(mass,22),
                        target=mp.nstr(target,22),error=mp.nstr(mass-target,16),
                        floor_evaluations='exact integer-square-root enclosure'))
    integrals=[]
    for av,zv in [('0.4','3.5'),('0.7','20.125'),('1.2','100.25')]:
        aa=mp.mpf(av); z=mp.mpf(zv)
        g=lambda t: mp.exp(-aa*aa*(t-z)**2/(4*t))/mp.sqrt(mp.pi*t) if t>0 else mp.mpf(0)
        value=mp.quad(g,[0,z/2,z,2*z,mp.inf])
        assert abs(value-2/aa)<mp.mpf('1e-40')
        integrals.append(dict(a=av,z=zv,integral=mp.nstr(value,25),
                              exact_mass=mp.nstr(2/aa,25)))
    return dict(kernel=out,envelope_integrals=integrals,
                scope='Numerical diagnostics only; no inferred infinite rate or Diophantine bound.',
                precision_decimal_digits=60)

def main():
    result=dict(passed=True,scope='Finite exact rational regressions plus separately labelled numerical diagnostics',
                counts=exact_checks(),diagnostics=diagnostics(),
                source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                proof='Unimodal weights and sharp counting kernels, Theorem1 through Theorem5',
                formal_proof=False)
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()


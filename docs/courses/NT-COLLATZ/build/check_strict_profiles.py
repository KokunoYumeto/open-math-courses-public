"""Finite regressions for integer thresholds and weighted phase averages.

Rational checks are exact. Exponential/integral checks use 70-digit arithmetic
and are separately labelled numerical diagnostics, not proof certificates.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb, ceil, floor
from pathlib import Path
import json
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]

def p(n, k):
    return F(comb(k-1, n-1), 2**k) if k >= n else F(0)

def discrepancy(xs, qs):
    z = sum(qs, F(0))
    # Both sides of every jump and both endpoints determine the supremum.
    return max([F(0)] + [abs(sum((q for x,q in zip(xs,qs) if x < t),F(0))-z*t)
                         for t in set(xs)|{F(0),F(1)}]
                       + [abs(sum((q for x,q in zip(xs,qs) if x <= t),F(0))-z*t)
                         for t in set(xs)|{F(0),F(1)}])

def real(q):
    return mp.mpf(q.numerator)/q.denominator

def main():
    c = Counter()
    for j in range(-80,81):
        s = F(j,8)
        for b in [F(9,8),F(5,4),F(3,2),F(7,4),F(15,8)]:
            L,x = floor(s)+1,s-floor(s)
            actual = [k for k in range(floor(s)-1,floor(s)+5) if s < k < s+b]
            predicted = [L]+([L+1] if x>2-b else [])
            assert actual == predicted
            c['strict_rational_intervals'] += 1
    # The actual logarithmic slope, evaluated without floating logarithms.
    for A in range(-10,11):
        for n in range(1,81):
            ratio = F(3**n)*F(2)**A
            k = ratio.numerator.bit_length()-ratio.denominator.bit_length()
            if F(2)**k > ratio: k -= 1
            assert F(2)**k <= ratio < F(2)**(k+1)
            L = k+1
            actual = [a for a in range(k-1,k+5) if ratio < F(2)**a < 3*ratio]
            predicted = [L]+([L+1] if ratio/F(2)**k>F(4,3) else [])
            assert actual == predicted
            c['exact_logarithmic_slope_intervals'] += 1
    for n in range(1,81):
        for k in range(n,5*n+1):
            assert p(n,k+1)/p(n,k) == F(k,2*(k-n+1))
            assert 4*(3*n-2)*p(n,k)**2 <= 1
            c['binomial_ratio_and_point_bounds'] += 1
    for m in range(201):
        v = F(comb(2*m,m),4**m)
        assert (3*m+1)*v*v <= 1
        assert (2*m+2)**2*(3*m+1)-(2*m+1)**2*(3*m+4) == m
        c['central_binomial_bounds'] += 1
    for delta in [F(1,3),F(2,5),F(3,7),F(1,2),F(2,3),F(3,4)]:
        K = ceil(1/delta)
        for A in [F(20),F(121,4),F(80),F(97,2)]:
            for W in [F(1),F(3,2),F(2),F(3)]:
                nmin = max(16,ceil(8*W))
                for sparse in [False,True]:
                    I = [n for n in range(nmin,180) if not sparse or n%3 != 1]
                    q0,q1,common,edge = {},{},[],[]
                    lost,gained=[],[]
                    for n in I:
                        d=floor(A-delta*n)+1
                        L=2*n+d
                        s0,s1=abs(d)<W,abs(d+1)<W
                        q0[n]=p(n,L) if s0 else F(0)
                        q1[n]=p(n,L+1) if s1 else F(0)
                        if s0 and s1:
                            common.append(n)
                            assert abs(q1[n]-q0[n]) <= F(W+2,2*(nmin-W+1))*q0[n]
                        if s0 != s1:
                            edge.append(n)
                            assert d == (ceil(W)-1 if s0 else -ceil(W))
                        if s0 and not s1: lost.append(n)
                        if s1 and not s0: gained.append(n)
                    assert len(lost)<=K and len(gained)<=K
                    z0=sum(q0.values(),F(0))
                    difference=sum((abs(q1[n]-q0[n]) for n in I),F(0))
                    interior=sum((abs(q1[n]-q0[n]) for n in common),F(0))
                    boundary=sum((abs(q1[n]-q0[n]) for n in edge),F(0))
                    assert difference == interior+boundary
                    assert boundary*boundary*(3*nmin-2) <= K*K
                    coefficient=(W+2)/(2*(nmin-W+1))
                    assert coefficient <= 2*W/nmin
                    excess=max(F(0),difference-coefficient*z0)
                    assert excess*excess*(3*nmin-2)<=K*K
                    assert abs(sum(q1.values(),F(0))-z0)<=difference
                    c['neighbor_profile_families'] += 1
    # Discrepancy and the reciprocal comparison are exact rational checks.
    # The corresponding exponential comparison is a separate diagnostic.
    mp.mp.dps=70
    num=0
    for xs in [[F(0),F(1,2),F(3,4)], [F(1,4)]*2+[F(1,2),F(7,8)], []]:
        for seed in range(1,13):
            q0=[F((i*seed+1)%7,16) for i in range(len(xs))]
            q1=[F((i+seed*2)%5,12) for i in range(len(xs))]
            for b in [F(5,4),F(3,2),F(7,4)]:
                z0,z1=sum(q0,F(0)),sum(q1,F(0))
                e0,e1=discrepancy(xs,q0),discrepancy(xs,q1)
                d=sum((abs(u-v) for u,v in zip(q0,q1)),F(0))
                gates=[int(x>2-b) for x in xs]
                h=z0+sum((q*g for q,g in zip(q1,gates)),F(0))
                assert abs(h-z0-(b-1)*z1)<=e1
                assert abs(h-b*z0)<=e0+d
                c['exact_weighted_reciprocal_comparisons'] += 1
                beta=real(b)*mp.log(2)
                ff=sum(real(u)*mp.power(2,1-real(x))+
                       real(v)*g*mp.power(2,2-real(x))
                       for x,u,v,g in zip(xs,q0,q1,gates))
                mean=(real(z0)+(mp.exp(beta)-2)*real(z1))/mp.log(2)
                assert abs(ff-mean)<=real(e0)+(2*mp.exp(beta)-2)*real(e1)+mp.mpf('1e-65')
                mean0=(mp.exp(beta)-1)*real(z0)/mp.log(2)
                assert abs(ff-mean0)<=(2*mp.exp(beta)-1)*real(e0)+mp.exp(beta)*real(d)+mp.mpf('1e-65')
                num+=1
    # Weighted Abel identity, including endpoint atoms and zero weights.
    for seed in range(1,21):
        xs=[F((seed*i)%17,17) for i in range(13)]
        ws=[F((seed+3*i)%9,11) for i in range(13)]
        for t in sorted(set(xs)|{F(0),F(1)}):
            aa=[F(int(x<=t))-t for x in xs]
            prefix=[sum(aa[:i+1],F(0)) for i in range(len(aa))]
            lhs=sum((w*a for w,a in zip(ws,aa)),F(0))
            rhs=ws[-1]*prefix[-1]+sum(((ws[i]-ws[i+1])*prefix[i] for i in range(len(ws)-1)),F(0))
            assert lhs==rhs
            assert abs(lhs)<=max(map(abs,prefix))*(ws[-1]+sum((abs(ws[i]-ws[i+1]) for i in range(len(ws)-1)),F(0)))
            c['weighted_abel_identities']+=1
    for a in [F(0),F(1,10),F(1,4),F(1,2),F(9,10)]:
        for Y in [F(0),F(1,3),F(1),F(5,2)]:
            for e in [F(0),F(1,7),F(3)]:
                R=(Y+e)/(1-a)
                assert abs(Y-R)==e+a*R==(e+a*Y)/(1-a)
                c['sharp_absorption_equalities']+=1
    q=[F(1,3),F(2,3)]
    assert sum((F(7,15)*v for v in q),F(0))==F(7,15)
    assert sum((F(7,15)*v/100 for v in q for _ in range(100)),F(0))==F(7,15)
    result={'passed':True,'counts':dict(c),'numerical_diagnostics':{'weighted_exponential_comparisons':num,'decimal_precision':70},
            'scope':'Exact finite rational regressions and separately labelled numerical diagnostics; not certification of the general written proofs.'}
    (ROOT/'checks/strict_profiles.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

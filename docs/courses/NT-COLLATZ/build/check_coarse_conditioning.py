"""Exact finite checks of packet clocks and the paired likelihood bound.

Logarithms are enclosed by rational series with a proved geometric remainder.
No finite test is offered as a proof of an asymptotic or all-parameter theorem.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import json


def words(n, s):
    if n == 1:
        if s >= 1:
            yield (s,)
        return
    for a in range(1, s-n+2):
        for tail in words(n-1, s-a):
            yield (a,) + tail


def probability(n, s):
    return F(comb(s-1, n-1), 2**s) if s >= n else F(0)


@lru_cache(None)
def log_bounds(q):
    """For rational q>0, enclose log(q), by range reduction and atanh."""
    q = F(q)
    assert q > 0
    power = q.numerator.bit_length() - q.denominator.bit_length()
    reduced = q / F(2)**power
    while reduced < 1:
        reduced *= 2
        power -= 1
    while reduced > 2:
        reduced /= 2
        power += 1

    def small(x):
        z = (x-1)/(x+1)
        count = 24
        lower = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(count)), F(0))
        tail = 2*z**(2*count+1)/((2*count+1)*(1-z*z))
        return lower, lower+tail

    lo, hi = small(reduced)
    lo2, hi2 = small(F(2))
    if power >= 0:
        return lo+power*lo2, hi+power*hi2
    return lo+power*hi2, hi+power*lo2


def packet_checks():
    count = Counter()
    for n in range(1, 7):
        for s in range(n, n+6):
            packet = list(words(n, s))
            size = len(packet)
            assert size == comb(s-1, n-1)
            paths = [(0,)+tuple(sum(a[:k]) for k in range(1, n+1)) for a in packet]
            means = [F(k*s,n) for k in range(n+1)]
            assert sum(F(a[0]**2,size) for a in packet) == F(s*(2*s-n+1),n*(n+1))
            for j in range(n+1):
                for k in range(n+1):
                    got = sum(((p[j]-means[j])*(p[k]-means[k])/size for p in paths), F(0))
                    want = F(s*(s-n)*min(j,k)*(n-max(j,k)),n*n*(n+1))
                    assert got == want
                    count['covariances'] += 1
            for k in range(n-1):
                fibres = defaultdict(list)
                for a,p in zip(packet,paths):
                    fibres[a[:k]].append(p)
                for key,values in fibres.items():
                    current = (F(sum(key))-means[k])/(n-k)
                    future = sum(((F(p[k+1])-means[k+1])/(n-k-1) for p in values),F(0))/len(values)
                    assert current == future
                    count['martingale_fibres'] += 1
            if n >= 2:
                for h in range(n):
                    for level in (F(1,2),F(1),F(2)):
                        actual = F(sum(max(abs(F(p[k])-means[k]) for k in range(h+1)) >= level for p in paths),size)
                        bound = F(s*(s-n)*h,(n+1)*(n-h))/(level*level)
                        assert actual <= bound
                        count['finite_maximal_bounds'] += 1
            for m in range(1,n):
                hist = Counter(sum(a[:m]) for a in packet)
                conditional = {t:F(v,size) for t,v in hist.items()}
                for t in range(m,s-n+m+1):
                    formula = F(comb(t-1,m-1)*comb(s-t-1,n-m-1),comb(s-1,n-1))
                    assert conditional.get(t,0) == formula
                    assert formula == probability(m,t)*probability(n-m,s-t)/probability(n,s)
                    count['likelihood_identities'] += 1
                prefix = Counter(a[:m] for a in packet)
                finite_word = sum((abs(F(v,size)-F(1,2**sum(a))) for a,v in prefix.items()),F(0))
                tail = 1-sum((probability(m,t) for t in conditional),F(0))
                total_distance = sum((abs(q-probability(m,t)) for t,q in conditional.items()),F(0))+tail
                assert finite_word+tail == total_distance
                count['word_total_distance_equalities'] += 1
            count['packets'] += 1
            count['words'] += size
    return count


def analytic_checks():
    count = Counter()
    for k in range(1,201):
        lo,hi = log_bounds(1+F(1,k))
        a = 1-(k+F(1,2))*hi
        b = 1-(k+F(1,2))*lo
        assert -F(1,4*k*k) <= a <= b <= F(1,4*k*k)
        count['factorial_increment_bounds'] += 1
    for n in (8,12,20,40,80,160):
        for m in sorted({1,2,max(1,n//5),n//2}):
            r=n-m
            for d in sorted({-r//3,-1,0,1,r//3}):
                for e in (-3,-1,0,1,3):
                    if abs(d)>F(r,2) or abs(d-e)>F(r,2) or 2*m+e<m:
                        continue
                    w=probability(r,2*r+d-e)/probability(n,2*n+d)
                    lo,hi=log_bounds(w)
                    bound=(F(m,n)+F(4*m*d*d,n*n)+F(4*abs(d*e),n)
                           +F(2*e*e,n)+F(4*abs(e),n)
                           +F(4*abs(d)*m,n*n)+F(8,n))
                    assert -bound <= lo <= hi <= bound,(n,m,d,e,lo,hi,bound)
                    count['paired_likelihood_bounds'] += 1
    return count


def main():
    count=packet_checks()+analytic_checks()
    q=[F(v,35) for v in (5,8,9,8,5)]
    p=[probability(2,t) for t in range(2,7)]
    assert 1-sum(p)==F(7,64)
    distance=sum(abs(a-b) for a,b in zip(q,p))+F(7,64)
    assert distance==F(533,1120)
    print(json.dumps({
        'passed':True,'arithmetic':'Exact integers, fractions and rational logarithm enclosures',
        'counts':dict(count),
        'examples':{'prefix_l1':str(distance),'independent_tail':str(1-sum(p)),
                    'clock_covariance_1_3':'2/5','clock_variance_2':'8/5'},
        'scope':'Finite regression checks of identities and selected analytic inequalities. The all-parameter bounds and asymptotic comparison are proved in the lesson, not inferred from enumeration.',
        'lean_certification':False
    },indent=2))


if __name__=='__main__':
    main()

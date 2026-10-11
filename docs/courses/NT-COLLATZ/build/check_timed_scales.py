"""Finite exact regression checks for scale indices, margins and interval counts.
The concentration and infinite-scale conclusions require the written proofs.
"""
from fractions import Fraction as F
from collections import Counter
import json


def odd_leq(n):
    return max(0, (n+1)//2)


def main():
    checks=Counter()
    alpha=F(1001,1000)
    assert F(2002,2001)**2 < alpha
    assert F(64)*5/12 == F(80,3)
    assert F(80,3)-1 > 20
    assert F(5097587,77645938) < 20
    # Work in logarithmic coordinates so every scale and comparison is exact.
    for a in [alpha,F(3,2),F(2)]:
        for target_log in [F(1),F(2),F(10),F(100)]:
            for ratio in [F(1),F(4,3),F(2),F(10)]:
                source_log=ratio*target_log
                assert a*source_log > target_log
                v=source_log/a
                j=1
                while v >= target_log/a:
                    v /= a
                    j += 1
                    assert j<10000
                assert target_log/a**2 <= v < target_log/a
                z=[v*a**(i-1) for i in range(j+1)]
                assert z[0] >= target_log/a**3 and z[0] < target_log
                assert z[-1] == source_log/a
                assert all(z[i+1] == a*z[i] for i in range(j))
                delta=(1-a**-3)*target_log
                assert target_log-z[0] <= delta
                assert source_log-target_log+delta == source_log-a**-3*target_log
                checks['exact_scale_ladders'] += 1
    # Odd count on (a,b] is O(b)-O(a), while closing a adds at most one.
    for base in range(9,16):
        for levels in range(1,5):
            endpoints=[base**(2**j) for j in range(levels+1)]
            H,X=endpoints[0],endpoints[-1]
            half_total=0
            for lo,hi in zip(endpoints,endpoints[1:]):
                half=odd_leq(hi)-odd_leq(lo)
                closed=odd_leq(hi)-odd_leq(lo-1)
                assert hi-lo>2 and half>=1 and closed<=2*half
                half_total += half
                checks['half_open_interval_counts'] += 1
            assert half_total == odd_leq(X)-odd_leq(H)
            for divisor in [1,3,5,7]:
                def total(n):
                    return max(0,odd_leq(n//divisor)-odd_leq(H//divisor))
                eps=max(F(total(hi)-total(lo-1),odd_leq(hi)-odd_leq(lo-1))
                        for lo,hi in zip(endpoints,endpoints[1:]))
                assert total(X) <= 2*eps*odd_leq(X)
                checks['closed_to_global_bad_counts'] += 1
    assert odd_leq(81)-odd_leq(9)==36
    assert odd_leq(81)-odd_leq(8)==37
    for numerator in range(31,301):
        b=F(numerator,10)
        ceil_b=-(-b.numerator//b.denominator)
        target=ceil_b-1
        assert 2<=target<b and b-target<=1
        checks['strict_integer_targets'] += 1
    # Constant-factor time allocation: lower square-root growth certified above
    # permits B=2001*C2, independent of all target heights.
    for C2 in [F(1,10),F(1),F(17),F(1000)]:
        B=2001*C2
        assert B*F(1,2001)==C2
        for H in [F(2),F(10),F(100)]:
            delta=(1-alpha**-3)*H
            for z in [H/alpha**3,H/alpha**2,H/alpha,H,H*alpha]:
                if z<H:
                    assert H-z<=delta
                for N in [max(H,z)*alpha,max(H,z)*2]:
                    assert N-H+delta==N-alpha**-3*H<=N
                    checks['target_margin_identities'] += 1
    print(json.dumps({'passed':True,'arithmetic':'exact integers and rational logarithmic coordinates',
        'counts':dict(checks),'sqrt_alpha_increment_lower_bound':'1/2001',
        'scope':'Finite scale-index, endpoint, target-margin and strict-threshold checks. '
        'The logarithmic concentration, asymptotic bounds and infinite summation are proved in the lesson; '
        'these finite checks do not establish the natural-density theorem.'},indent=2))


if __name__=='__main__':
    main()

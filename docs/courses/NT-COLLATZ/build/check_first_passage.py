"""Exact finite checks for logarithmic sampling and first passage.

These check arithmetic identities and sample inequalities, not the asymptotic
mixing or entrance theorem. Logarithms use rational upper and lower bounds.
"""
from fractions import Fraction as F
from itertools import product
import json

from check_mixing import affine_law, offset, residue


def log_unit_bounds(x, terms=60):
    assert F(1) <= x <= F(2)
    z = (x-1)/(x+1)
    lo = sum((2*z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    rem = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lo, lo+rem


def log_bounds(x):
    assert x >= 1
    k = 0
    while x > 2:
        x /= 2
        k += 1
    lo, hi = log_unit_bounds(x)
    l2, h2 = log_unit_bounds(F(2))
    return lo+k*l2, hi+k*h2


def word_data(word):
    total = 0
    c = 0
    for a in word:
        c = 3*c+2**total
        total += a
    return total, c, F(c, 2**total)


def step(n):
    v = 3*n+1
    a = (v & -v).bit_length()-1
    return v >> a, a


def itinerary(n, length):
    word = []
    states = [n]
    for _ in range(length):
        n, a = step(n)
        word.append(a)
        states.append(n)
    return tuple(word), states


def main():
    counts = dict(progression_intervals=0, inverse_words=0, actual_orbits=0,
                  chinese_remainder_fibres=0, exact_collapses=0,
                  disjoint_passage_events=0, word_weight_sums=0)
    # Rational enclosures establish the inequality for each listed interval.
    for a, b in [(F(1),F(50)),(F(21,2),F(137,4)),(F(50),F(51)),
                 (F(103,3),F(109,3)),(F(27),F(27)+F(1,10))]:
        lo, hi = log_bounds(b/a)
        for q in range(1,13):
            for h in range(q):
                mass = sum((F(1,n) for n in range(1,int(b)+1)
                            if a <= n <= b and n % q == h),F(0))
                assert mass-hi/q >= -1/a
                assert mass-lo/q <= 1/a
                counts['progression_intervals'] += 1
    for length in range(1,4):
        for word in product(range(1,6),repeat=length):
            total,c,value = word_data(word)
            assert value == offset(tuple(reversed(word)))
            mod = 3**length
            h = residue(value,mod)
            start = h if h%2 else h+mod
            for j in range(5):
                m = start+2*j*mod
                num = 2**total*m-c
                assert num % mod == 0
                n = num//mod
                if n <= 0:
                    continue
                actual,states = itinerary(n,length)
                assert n%2 == 1 and actual == word and states[-1] == m
                assert n % 2**(total+1) == (
                    (2**total-c)*pow(3**length,-1,2**(total+1))) % 2**(total+1)
                counts['inverse_words'] += 1
    for n in range(1,402,2):
        for k in range(1,5):
            w,states = itinerary(n,k)
            total,c,value = word_data(w)
            assert (3**k*n+c) == 2**total*states[-1]
            assert F(2**total*states[-1]-c,3**k) == n
            assert value < 3**k
            counts['actual_orbits'] += 1
    for exponent in range(1,7):
        u = 2**exponent
        for r in range(1,4):
            v = 3**r
            for a in range(1,u,2):
                for b in range(v):
                    z = (a+u*((b-a)*pow(u,-1,v)%v))%(u*v)
                    assert z%u == a and z%v == b
                    # Exactly one representative, checked by the explicit u-fibre.
                    assert [t for t in range(a,u*v,u) if t%v==b] == [z]
                    counts['chinese_remainder_fibres'] += 1
    for m,r in [(1,1),(1,2),(1,3),(2,2),(2,3)]:
        law = affine_law(m,3**m)
        for endpoints in [(5,7,11),(1,3,9,27),(13,29,31,47)]:
            c = [3**r*sum((F(1,n) for n in endpoints if n%3**r==x),F(0))
                 for x in range(3**r)]
            direct = sum((v*F(1,3**(r-m))*law.get(x%3**m,F(0))
                          for x,v in enumerate(c)),F(0))
            collapsed = sum((F(3**m,n)*law.get(n%3**m,F(0))
                             for n in endpoints),F(0))
            assert direct == collapsed
            counts['exact_collapses'] += 1
    # Known finite orbits only; a missing first entry is not called divergent.
    for n in range(1,200,2):
        _,states = itinerary(n,80)
        for x in [5,10,20,50]:
            hits = [j for j,v in enumerate(states) if v<=x]
            if not hits:
                continue
            t = hits[0]
            for m in range(1,t+1):
                r=t-m
                assert states[r]>x
                assert next(j for j,v in enumerate(states[r:]) if v<=x)==m
                counts['disjoint_passage_events'] += 1
    for length in range(1,5):
        for cutoff in [2,4,7]:
            a_sum = sum((F(1,2**a) for a in range(1,cutoff+1)),F(0))
            b_sum = sum((F(b,2**b) for b in range(1,cutoff+1)),F(0))
            direct = sum((F(word[-1],2**sum(word))
                          for word in product(range(1,cutoff+1),repeat=length)),F(0))
            assert direct == a_sum**(length-1)*b_sum <= 2
            # Exact omitted one-dimensional tails, not a convergence guess.
            assert a_sum+F(1,2**cutoff)==1
            assert b_sum+F(cutoff+2,2**cutoff)==2
            counts['word_weight_sums'] += 1
    assert itinerary(11,3) == ((1,2,3),[11,17,13,5])
    assert itinerary(29,2) == ((3,1),[29,11,17])
    assert itinerary(9,5)[1] == [9,7,11,17,13,5]
    assert F(2,5)+F(1,7)+F(2,11) == F(279,385)
    assert F(1001,1000)**3 < F(251,250) and 3**5 < 2**8
    assert F(4,25)-F(1,4)+F(1,100000)==F(-8999,100000)
    print(json.dumps({'passed':True,'counts':counts,
        'arithmetic':'Integers and exact fractions; logarithms bounded by rational positive series with rigorous remainder.',
        'scope':'Finite identities and selected inequalities only. Asymptotic entrance stabilization is proved in the lesson, not inferred from these tests.'},indent=2))


if __name__ == '__main__':
    main()

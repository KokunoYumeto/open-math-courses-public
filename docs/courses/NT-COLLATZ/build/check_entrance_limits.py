"""Exact finite regressions for compatible entrance laws and weighted minima.
General limits and the arithmetic density theorem have written proofs; finite
state examples and finite harmonic identities are not proofs of those theorems.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json

DAGGER = 0  # In this test model only; all actual states are positive.
MAP = {1:1,2:1,3:2,4:3,5:6,6:5}


def passage(x,n):
    seen = set()
    while n != DAGGER and n > x:
        if n in seen:
            return DAGGER
        seen.add(n)
        n = MAP[n]
    return n


def push(fn,law):
    out = defaultdict(F)
    for n,mass in law.items():
        out[fn(n)] += mass
    return dict(out)


def distance(p,q):
    return sum((abs(p.get(n,F(0))-q.get(n,F(0))) for n in p.keys()|q.keys()),F(0))


def law(j):
    return {6:1-F(1,2**j),4:F(1,2**j)}


def main():
    counts = dict(nested_map_identities=0,joint_fibres=0,
                  joint_law_isometries=0,adjacent_and_limit_errors=0,
                  dyadic_weight_identities=0,tight_unbounded_prefixes=0,
                  scale_shift_identities=0,finite_prefix_inclusions=0)
    for x in range(1,7):
        for y in range(x,7):
            for n in range(7):
                assert passage(x,passage(y,n))==passage(x,n)
                assert passage(y,passage(x,n))==passage(x,n)
                counts['nested_map_identities'] += 1
    for thresholds in [(2,4,6),(1,3,6),(2,2,4),(1,2,3,6),(6,)]:
        xmax=thresholds[-1]
        def J(z):
            return tuple(passage(x,z) for x in thresholds)
        coherent = [zs for zs in product(*(range(x+1) for x in thresholds))
                    if all(passage(x,zs[i+1])==zs[i]
                           for i,x in enumerate(thresholds[:-1]))]
        assert set(coherent)=={J(z) for z in range(xmax+1)}
        for z in range(xmax+1):
            assert J(z)[-1]==z
            counts['joint_fibres'] += 1
        for j in range(9):
            projected=push(lambda n:passage(xmax,n),law(j))
            limit=push(lambda n:passage(xmax,n),{6:F(1)})
            joint=push(J,projected)
            direct=push(lambda n:tuple(passage(x,n) for x in thresholds),law(j))
            assert joint==direct
            assert distance(joint,push(J,limit))==distance(projected,limit)
            counts['joint_law_isometries'] += 1
    for j in range(10):
        assert distance(law(j),law(j+1))==F(1,2**j)
        assert distance(law(j),{6:F(1)})==F(2,2**j)
        # Finite telescoping sum plus exact geometric tail.
        finite=sum((F(1,2**h) for h in range(j,j+12)),F(0))
        assert finite+F(2,2**(j+12))==F(2,2**j)
        counts['adjacent_and_limit_errors'] += 1
    def oddpart(n):
        return n//(n & -n)
    for cutoff in range(2,257):
        for residue_class in range(3):
            direct=sum((F(1,n) for n in range(1,cutoff+1)
                        if oddpart(n)%3==residue_class),F(0))
            fibres=sum((F(1,2**a)*sum((F(1,m)
                    for m in range(1,cutoff//2**a+1,2)
                    if m%3==residue_class),F(0))
                    for a in range(cutoff.bit_length())),F(0))
            assert direct==fibres
            counts['dyadic_weight_identities'] += 1
    def g(n):
        return n.bit_length()-1 if n & (n-1)==0 else 0
    for cutoff in range(1,257):
        total=sum((F(1,n) for n in range(1,cutoff+1)),F(0))
        for k in range(9):
            tail=sum((F(1,n) for n in range(1,cutoff+1) if g(n)>k),F(0))
            assert tail/total <= F(1,2**k)
            counts['tight_unbounded_prefixes'] += 1
    alpha=F(1001,1000)
    for k in range(8):
        for j in range(12):
            # Exact logarithmic coordinates; no giant real powers rounded.
            assert (F(7)*alpha**k)*alpha**j == F(7)*alpha**(j+k)
            counts['scale_shift_identities'] += 1
    # Nonmonotone diverging threshold, exact finite-prefix inclusion.
    def f(n):
        return n//4+(-1 if n%2 else 1)
    for k in range(2,9):
        prefix=4*(k+2)
        for n in range(1,257):
            if g(n)>=f(n):
                assert n<=prefix or g(n)>k
            if n>prefix:
                assert f(n)>k
            counts['finite_prefix_inclusions'] += 1
    print(json.dumps({'passed':True,'counts':counts,'arithmetic':'Exact integers and fractions',
       'scope':'Finite nested-passage maps, compatible tuple bijections, exact probability distances, harmonic dyadic fibres, and weighted examples. No asymptotic theorem or Collatz convergence is inferred from finite tests.'},indent=2))


if __name__=='__main__':
    main()

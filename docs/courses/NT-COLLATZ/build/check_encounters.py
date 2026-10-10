"""Exact finite regressions for renewal encounters; not analytic proof certification.

The toy law is ((1,1),(2,2)), each of mass 1/2, not the marked holding law.
Full paths and the stopped recurrence are evaluated separately with rational masses.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json


def main():
    counts = {}
    width = 10
    black = {2, 4, 6, 8}
    def white(x):
        return 1 <= x <= width and x not in black

    @lru_cache(None)
    def paths(x):
        if x > width:
            return (((x,), F(1)),)
        return tuple(((x,) + tail, mass / 2)
                     for step in (1, 2) for tail, mass in paths(x + step))

    def direct(x, n, w):
        total = F(0)
        for path, mass in paths(x):
            entrances = [i for i, pos in enumerate(path) if pos in black]
            if len(entrances) >= n:
                count = sum(white(pos) for pos in path[:entrances[n-1]])
                total += mass * w**count
        return total

    @lru_cache(None)
    def restart(x, n, w):
        if x > width:
            return F(0)
        if x in black:
            if n == 1:
                return F(1)
            # The first positive vertical step crosses this singleton's top.
            return sum((restart(x+d, n-1, w) for d in (1, 2)), F(0))/2
        return w*sum((restart(x+d, n, w) for d in (1, 2)), F(0))/2

    comparisons = inequalities = 0
    for x in range(1, width+2):
        assert sum((mass for _, mass in paths(x)), F(0)) == 1
        for n, w in product(range(1,6), (F(1,2),F(2,3))):
            value = direct(x,n,w)
            assert value == restart(x,n,w)
            comparisons += 1
            # Conditional white probability at each black exit is at least 1/2.
            assert value <= w**white(x)*((1+w)/2)**(n-1)
            for k in range(4):
                event_mass = F(0)
                for path, mass in paths(x):
                    entrances = [i for i,pos in enumerate(path) if pos in black]
                    if len(entrances) >= n:
                        if sum(white(pos) for pos in path[:entrances[n-1]]) <= k:
                            event_mass += mass
                assert event_mass <= w**(-k)*((1+w)/2)**(n-1)
                inequalities += 1
    assert min(sum(F(white(x+d),2) for d in (1,2)) for x in black) == F(1,2)
    counts['path_recurrence_comparisons'] = comparisons
    counts['weighted_event_bounds'] = inequalities
    counts['complete_paths_from_one'] = len(paths(1))

    # A separate count with a nonempty segment inside the first region.
    colours = (False,False,True,True,False)
    for w in (F(1,2),F(2,3)):
        assert w**sum(colours[:4]) == w**sum(colours[:3])*w**sum(colours[3:4]) == w*w
        assert w**sum(colours[:4]) != w**sum(colours[:4])*w**sum(colours[3:4])

    def f(h,x):
        return min(x*x/h,abs(x))
    kernel = 0
    grid = [F(k,2) for k in range(-32,33)]
    for h,x,y in product((F(1),F(3,2),F(4),F(16)),grid,grid):
        assert f(h,x+y) <= 2*f(h,x)+2*f(h,y)
        kernel += 1
    counts['rational_kernel_inequalities'] = kernel

    # Exact common-row geometry in a rational-slope analogue (a=2,b=1).
    # These are rounding/packing tests, not substitutes for the logarithmic proof.
    packing = 0
    for r,h,bottom in product((400,800,1200),(1,2,3),(F(-19,2),F(0),F(3,2),F(6))):
        if bottom > 2*h:
            continue
        row = r//2
        for size in (F(r),F(r+20)):
            top = bottom+size
            assert bottom < row <= top
            length = (F(row)-bottom)/2
            assert length >= F(r,8)
            end = length.numerator//length.denominator
            first = set(range(1,2+end))
            next_left = max(first)+1
            assert next_left-1 >= F(r,16)
            second = set(range(next_left,next_left+end+1))
            assert first.isdisjoint(second)
            packing += 1
    counts['rational_common_row_checks'] = packing

    # Residence-time implication on every binary colour word in two short models.
    residence = 0
    for k,n in ((0,4),(1,3)):
        d = k
        for _ in range(n-1):
            d += 2+k  # every singleton/group top is crossed within two steps
        p = d+1
        for word in product((0,1),repeat=p):
            if sum(word)>k:
                continue
            entrances=[]
            pos=0
            while pos<p:
                while pos<p and word[pos]:
                    pos+=1
                if pos==p:
                    break
                entrances.append(pos)
                pos+=2
            assert len(entrances)>=n
            residence+=1
    counts['finite_residence_words'] = residence

    assert 16*F(5,6)**41 <= F(1,100) < 16*F(5,6)**40
    d=1
    ds=[d]
    for _ in range(2):
        d += (d+1)**2+1
        ds.append(d)
    assert ds == [1,6,56]
    assert d+1 == 57
    # Exact finite total from the square-sum bound; tail <= integral 1/N.
    for n in (1,2,5,10,40):
        assert sum((F(1,q*q) for q in range(1,n+1)),F(0))+F(1,n) <= 2
    print(json.dumps({'passed':True,'counts':counts,
        'arithmetic':'Python Fraction throughout; no floating-point decisions',
        'scope':'Finite path identities, conditional-weight bounds, kernel algebra, rational analogue of row packing, residence endpoints and exercise arithmetic.',
        'limits':'The analytic exit, sparse-target and finite-horizon theorems are established by written proofs, not these finite checks. Toy increments are not the marked holding law.'},indent=2))


if __name__ == '__main__':
    main()

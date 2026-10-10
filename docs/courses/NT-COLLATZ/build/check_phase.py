"""Exact finite regressions for the phase lesson, not infinite proof certificates."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json


def phase(n, xi, j, l):
    q = 3**n
    a = (xi * 3**(2*j-2) * pow(2, 1-l, q)) % q
    if 2*a > q:
        a -= q
    return F(a, q)


def corner(n, xi, j, l, eps):
    assert abs(phase(n, xi, j, l)) <= eps
    while abs(phase(n, xi, j, l+1)) <= eps:
        l += 1
    while j > 1 and abs(phase(n, xi, j-1, l)) <= eps:
        j -= 1
    return j, l


def triangle(n, xi, root, eps):
    j0, l0 = root
    t = abs(phase(n, xi, j0, l0))
    pts = set()
    # Definition uses the exact multiplicative inequality, with no floating logs.
    j = j0
    while t * 9**(j-j0) <= eps:
        l = l0
        while t * 9**(j-j0) * 2**(l0-l) <= eps:
            pts.add((j,l))
            l -= 1
        j += 1
    return pts


def convolve(a, b, q):
    out = defaultdict(F)
    for x, px in a.items():
        for y, py in b.items():
            out[(x+y) % q] += px*py
    return dict(out)


def affine(word, q):
    total = val = 0
    for i, a in enumerate(word):
        total += a
        val += 3**i * pow(2, -total, q)
    return val % q


def run():
    counts = dict(character_relations=0, paired_conditional_laws=0,
                  paired_words=0, phase_cells=0, low_phase_cells=0,
                  triangles=0, interior_corners=0, negative_corner_phases=0,
                  buffer_cells=0, lifting_cells=0)
    for n in range(2,8):
        q = 3**n
        for a in range(-5,6):
            for k in range(6):
                for b in range(-3,4):
                    r = (a * pow(2,-k,q)) % q
                    assert (r + b) % q == ((a+b*2**k)*pow(2,-k,q)) % q
                    assert (r == 0) == (a % q == 0)
                    counts['character_relations'] += 1
        m = n//2
        for bs in product(range(2,6), repeat=m):
            direct = defaultdict(F)
            factored = {0:F(1)}
            total = 0
            for j,b in enumerate(bs):
                total += b
                x = 3**(2*j)*pow(2,-total,q) % q
                local = defaultdict(F)
                for r in range(1,b):
                    local[x*(2**r+3) % q] += F(1,b-1)
                factored = convolve(factored, local, q)
            odd = range(1,5) if n % 2 else [None]
            if n % 2:
                tail = defaultdict(F)
                for a in odd:
                    tail[3**(n-1)*pow(2,-total-a,q) % q] += F(1,2**a)
                factored = convolve(factored, tail, q)
            for rs in product(*(range(1,b) for b in bs)):
                word = []
                mass = F(1)
                for b,r in zip(bs,rs):
                    word.extend([b-r,r])
                    mass /= b-1
                for a in odd:
                    w = word if a is None else word+[a]
                    p = mass if a is None else mass/F(2**a)
                    direct[affine(w,q)] += p
                    counts['paired_words'] += 1
            assert dict(direct) == factored
            assert sum(factored.values()) == (F(15,16) if n%2 else 1)
            counts['paired_conditional_laws'] += 1

    # Rational enclosure of log(2)=2 atanh(1/3), including a tail bound.
    x, terms = F(1,3), 25
    loglo = 2*sum((x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    loghi = loglo+2*x**(2*terms+1)/F(2*terms+1)/(1-x*x)
    h=F(1,100)
    for n,k in [(14,15),(24,15),(24,30),(45,30),(64,60)]:
        eps=F(1,2**k)
        rlo,rhi=F(k,10)*loglo,F(k,10)*loghi
        assert rlo>=1
        radius=int(rhi)+1
        # No squared integer distance straddles this rational enclosure.
        assert int(rlo*rlo)==int(rhi*rhi)
        for xi in (1,2,5,17,3**(n//2)+1,3**(n-4)+1,3**(n-4)-1):
            roots=set()
            for j in range(1,n//2+1):
                for l in range(-120,121):
                    t=phase(n,xi,j,l)
                    assert t and abs(t)>=F(1,3**(n-2*j+2))
                    assert (phase(n,xi,j,l-1)-2*t).denominator==1
                    if j<n//2:
                        assert (phase(n,xi,j+1,l)-9*t).denominator==1
                        v,w=phase(n,xi,j+1,l),phase(n,xi,j,l-1)
                        if abs(t)<=h and (abs(v)<=eps or abs(w)<=eps):
                            assert abs(t)<=eps
                        if abs(v)<=h and abs(w)<=h:
                            assert abs(t)<=h
                        if j>1 and abs(phase(n,xi,j-1,l))<=h and abs(w)<=h:
                            assert abs(t)<=h
                        counts['lifting_cells']+=1
                    counts['phase_cells']+=1
                    if abs(t)<=eps:
                        root=corner(n,xi,j,l,eps)
                        roots.add(root)
                        assert (j,l) in triangle(n,xi,root,eps)
                        assert F(j)<=F(n,2)-rhi
                        counts['low_phase_cells']+=1
            occupied={}
            for root in sorted(roots):
                pts=triangle(n,xi,root,eps)
                counts['interior_corners'] += root[0]>1
                counts['negative_corner_phases'] += phase(n,xi,*root)<0
                for point in pts:
                    j,l=point
                    assert 1<=j<=n//2 and abs(phase(n,xi,j,l))<=eps
                    assert corner(n,xi,j,l,eps)==root
                    assert point not in occupied
                    occupied[point]=root
                candidates=set()
                for j,l in pts:
                    for dj in range(-radius,radius+1):
                        for dl in range(-radius,radius+1):
                            if dj*dj+dl*dl<=rlo*rlo:
                                candidates.add((j+dj,l+dl))
                for j,l in candidates-pts:
                    if 1<=j<=n//2:
                        assert abs(phase(n,xi,j,l))>eps
                        counts['buffer_cells']+=1
                counts['triangles']+=1
    assert counts['interior_corners'] and counts['negative_corner_phases']
    example=triangle(14,1,(1,1),F(1,32768))
    assert example==({(1,l) for l in range(-6,2)}|
                     {(2,l) for l in range(-3,2)}|{(3,1)})
    assert len(example)==14
    assert phase(14,1,4,2)==F(-3280,6561)
    assert phase(2,1,1,3)==F(-2,9)
    assert pow(4,-1,27)==7 and 7*pow(8,-1,27)%27==11
    return {'passed':True,'counts':counts,
            'scope':'Exact finite arithmetic and conditional-distribution regressions only. Odd final variables truncated at four retain mass 15/16 on both sides; this is not an infinite Fourier or renewal proof.',
            'general_proofs':'Lesson Propositions 1, Corollary 2, Lemma 3 and Theorem 4.'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))

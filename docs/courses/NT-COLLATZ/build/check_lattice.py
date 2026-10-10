"""Finite exact regressions for the lattice-probability lesson.

The analytic local/tail estimates have written proofs. Tests here check finite
Fourier identities, integer support certificates, rational changes of weights,
and exact holding-time formula instances; they do not prove infinite bounds.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from check_fourier import Field


def add(x, y):
    return tuple(a+b for a,b in zip(x,y))


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def convolution(p, q):
    out=defaultdict(Q)
    for x,a in p.items():
        for y,b in q.items():
            out[add(x,y)]+=a*b
    return dict(out)


def weight(v, ratios):
    out=Q(1)
    for x,r in zip(v,ratios):
        out*=r**x
    return out


def tilt(p, ratios):
    m=sum(p[v]*weight(v,ratios) for v in p)
    out={v:p[v]*weight(v,ratios)/m for v in p}
    assert sum(out.values())==1 and all(x>0 for x in out.values())
    return m,out


def root(field, k):
    p=[Q(0)]*field.n
    p[k%field.n]=Q(1)
    return field.reduce(p)


def characteristic(field, p, t):
    return field.total(field.scale(root(field,dot(t,v)),a) for v,a in p.items())


def power(field,z,n):
    out=field.one
    for _ in range(n):
        out=field.mul(out,z)
    return out


def main():
    counts=Counter()
    square={v:Q(1,4) for v in product(range(2),repeat=2)}
    laws=[{(0,):Q(1,2),(1,):Q(1,2)},square,
          {(0,0):Q(1,2),(1,0):Q(1,3),(0,1):Q(1,6)}]
    for p in laws:
        dim=len(next(iter(p)))
        for mod in [4,5,7]:
            f=Field(mod)
            grid=list(product(range(mod),repeat=dim))
            chars={t:characteristic(f,p,t) for t in grid}
            for t,phi in chars.items():
                pair_sum=f.zero
                for v,a in p.items():
                    for w,b in p.items():
                        z=root(f,dot(t,tuple(x-y for x,y in zip(v,w))))
                        cosine=f.scale(f.add(z,f.conjugate(z)),Q(1,2))
                        pair_sum=f.add(pair_sum,f.scale(f.add(f.one,f.scale(cosine,-1)),a*b))
                assert pair_sum==f.add(f.one,f.scale(f.norm2(phi),-1))
                counts['characteristic_pair_identities']+=1
            pn={(0,)*dim:Q(1)}
            for n in range(1,4):
                pn=convolution(pn,p)
                # Support lies inside {0,...,n}^dim with n<mod: no aliasing.
                for x in grid:
                    inverse=f.total(f.mul(power(f,chars[t],n),root(f,-dot(t,x))) for t in grid)
                    inverse=f.scale(inverse,Q(1,mod**dim))
                    assert inverse==f.scale(f.one,pn.get(x,Q(0)))
                    counts['finite_inversion_points']+=1
    certificates=[
        {'pairs':[((1,0),(0,0)),((0,1),(0,0))], 'rows':[(1,0),(0,1)],'A':2},
        {'pairs':[((2,8),(2,7)),((2,5),(1,3))], 'rows':[(-2,1),(1,0)],'A':6}]
    for c in certificates:
        differences=[tuple(x-y for x,y in zip(v,w)) for v,w in c['pairs']]
        assert sum(m*m for row in c['rows'] for m in row)==c['A']
        for i,row in enumerate(c['rows']):
            assert tuple(sum(row[j]*differences[j][k] for j in range(len(row))) for k in range(2))==tuple(int(k==i) for k in range(2))
            counts['coordinate_certificates']+=1
        for mod in [3,4,5,7]:
            f=Field(mod)
            for t in product(range(mod),repeat=2):
                for i,row in enumerate(c['rows']):
                    # Exact exponent identity includes negative coefficients.
                    assert root(f,sum(row[j]*dot(t,differences[j]) for j in range(len(row))))==root(f,t[i])
                    counts['certificate_character_identities']+=1
    for p in laws[1:]:
        for ratios in [(Q(1,3),Q(3)),(Q(2),Q(1,2)),(Q(3,4),Q(4,3))]:
            m,pt=tilt(p,ratios)
            mi,back=tilt(pt,tuple(1/r for r in ratios))
            assert back==p and m*mi==1
            _,twice=tilt(pt,ratios)
            _,direct=tilt(p,tuple(r*r for r in ratios))
            assert twice==direct
            counts['inverse_and_composite_tilts']+=1
            pn=qn={(0,0):Q(1)}
            for n in range(1,6):
                pn=convolution(pn,p)
                qn=convolution(qn,pt)
                for x,mass in pn.items():
                    assert mass==m**n/weight(x,ratios)*qn[x]
                    counts['point_weight_changes']+=1
    m,pt=tilt(square,(Q(1,3),Q(3)))
    assert m==Q(4,3)
    pn={(0,0):Q(1)}
    for _ in range(4):
        pn=convolution(pn,pt)
    assert pn[1,3]==Q(27,64)**2
    assert m**4/Q(9)*pn[1,3]==Q(1,16)
    # Exact rational values of the holding-time generating function.
    for r in [Q(1,2),Q(3,4),Q(1),Q(33,32)]:
        bmgf=(r/(2-r))**2
        failure=bmgf-r**3/4
        ratio=r*failure
        assert 0<ratio<1
        whole=r**4/(4*(1-ratio))
        for length in range(1,21):
            partial=r**4/4*sum(ratio**j for j in range(length))
            remainder=r**4/4*ratio**length/(1-ratio)
            assert partial+remainder==whole
            counts['holding_transform_remainders']+=1
    r=Q(33,32)
    assert r<Q(25,24) and r/(2-r)<Q(16,15)
    assert r*((r/(2-r))**2-r**3/4)<Q(799,864)<1
    q=lambda b:Q(b-1,2**b)
    atoms={(1,3):Q(1,4),(2,5):q(2)/4,(2,7):q(4)/4,(2,8):q(5)/4}
    assert list(atoms.values())==[Q(1,4),Q(1,16),Q(3,64),Q(1,32)]
    rho=min(atoms[v]*atoms[w] for v,w in certificates[1]['pairs'])
    assert rho==Q(3,2048) and rho/6==Q(1,4096)
    e_j=Q(1,1-Q(3,4))
    e_bp=(4-3*Q(1,4))/Q(3,4)
    assert e_j==4 and e_bp==Q(13,3) and 3+(e_j-1)*e_bp==16
    print(json.dumps({'passed':True,'arithmetic':'exact integers, fractions and cyclotomic polynomial quotients',
        'counts':dict(counts),'ranges':{'finite_fourier_moduli':[4,5,7],'sum_lengths_for_inversion':[1,3],
        'tilted_sum_lengths':[1,5],'holding_generating_function_partial_lengths':[1,20]},
        'scope':'Finite algebraic regressions and exact geometric-remainder identities. The analytic local and tail estimates, all real frequencies and the infinite holding-time law are justified by the written proofs, not by these tests.'},indent=2))


if __name__=='__main__':
    main()

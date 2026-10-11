"""Exact finite checks for joint residue-total maps, not an infinite mixing proof."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def compositions(n,s):
    if n==0:
        if s==0:
            yield ()
        return
    for cut in combinations(range(1,s),n-1):
        ends=(0,)+cut+(s,)
        yield tuple(ends[i+1]-ends[i] for i in range(n))


def offset(a,modulus):
    total=0
    value=0
    for i,x in enumerate(a):
        total+=x
        value=(value+pow(3,i,modulus)*pow(2,-total,modulus))%modulus
    return value


def p(n,s):
    if n==0:
        return F(int(s==0))
    return F(comb(s-1,n-1),2**s) if s>=n else F(0)


def clean(h):
    return {key:value for key,value in h.items() if value}


def joint(n,cap):
    h=defaultdict(F)
    for s in range(n,cap+1):
        for a in compositions(n,s):
            h[offset(a,3**n),s]+=F(1,2**s)
    return clean(h)


def reduce(h,m):
    out=defaultdict(F)
    for (y,s),v in h.items():
        out[y%3**m,s]+=v
    return clean(out)


def lift(h,m,n):
    out={}
    for (y,s),v in h.items():
        for y2 in range(y,3**n,3**m):
            out[y2,s]=v*F(1,3**(n-m))
    return clean(out)


def convolve(h,j,cap):
    out=defaultdict(F)
    for (y,u),v in h.items():
        for s in range(u,cap+1):
            out[y,s]+=v*p(j,s-u)
    return clean(out)


def minus(a,b):
    return clean({k:a.get(k,F(0))-b.get(k,F(0)) for k in a.keys()|b.keys()})


def norm(h):
    return sum(map(abs,h.values()),F(0))


def run():
    checks=defaultdict(int)
    for n in range(1,6):
        cap=n+7
        mu=joint(n,cap)
        for m in range(1,n+1):
            projected=reduce(mu,m)
            assert projected==convolve(joint(m,cap),n-m,cap)
            lifted=lift(projected,m,n)
            assert reduce(lifted,m)==projected
            assert lift(reduce(lifted,m),m,n)==lifted
            assert norm(lifted)==norm(projected)==norm(mu)
            discrepancy=norm(minus(mu,lifted))
            weighted=F(0)
            for s in range(n,cap+1):
                a={key:v/p(n,s) for key,v in mu.items() if key[1]==s}
                b={key:v/p(n,s) for key,v in lifted.items() if key[1]==s}
                weighted+=p(n,s)*norm(minus(a,b))
            assert discrepancy==weighted
            for a in range(1,m+1):
                assert lift(reduce(mu,a),a,n)==lift(lift(reduce(mu,a),a,m),m,n)
                lhs=minus(mu,lift(reduce(mu,a),a,n))
                term1=minus(mu,lift(projected,m,n))
                term2=lift(minus(projected,lift(reduce(mu,a),a,m)),m,n)
                rhs=defaultdict(F,term1)
                for key,v in term2.items():
                    rhs[key]+=v
                assert lhs==clean(rhs)
                checks['telescoping_and_lift_identities']+=1
            checks['joint_projection_and_conditional_norms']+=1
    signed={(1,0):F(-3,7),(2,1):F(5,9),(4,0):F(1,7)}
    for j in range(4):
        cj=convolve(signed,j,10)
        assert norm(cj)<=norm(signed)
        assert reduce(cj,1)==convolve(reduce(signed,1),j,10)
        assert lift(convolve(reduce(signed,1),j,10),1,3)==convolve(lift(reduce(signed,1),1,3),j,10)
        for k in range(4):
            assert convolve(cj,k,10)==convolve(signed,j+k,10)
            checks['total_convolution_identities']+=1
    for n in range(1,21):
        tail=1-sum(p(n,s) for s in range(n,4*n+1))
        assert tail<=F(81,128)**n
        checks['total_tail_bounds']+=1
    for r in (1,2):
        for N in (1,2,3):
            n=r+N
            modulus=3**n
            for L in range(r,r+4):
                prefixes=[a for a in compositions(r,L) if a[0]%2==1]
                for total in range(N,N+4):
                    tails=list(compositions(N,total))
                    for v in range(N):
                        k=N-v
                        for eta0 in (1,2):
                            xi=3**v*eta0
                            eta=(pow(2,-L,3**k)*eta0)%3**k
                            direct=defaultdict(F)
                            factor=defaultdict(F)
                            for a in prefixes:
                                for b in tails:
                                    phase=xi*offset(a+b,modulus)%modulus
                                    direct[phase]+=F(1,2**(L+total))
                                prefix_phase=xi*offset(a,modulus)%modulus
                                for u in range(k,total+1):
                                    if not p(v,total-u):
                                        continue
                                    for b in compositions(k,u):
                                        tail_phase=3**(n-k)*(eta*offset(b,3**k)%3**k)
                                        phase=(prefix_phase+tail_phase)%modulus
                                        factor[phase]+=F(1,2**(L+u))*p(v,total-u)
                            assert clean(direct)==clean(factor)
                            checks['total_retaining_character_factorizations']+=1
    for m in range(18,61):
        for n in range(m,501,11):
            chain=[m]
            while chain[-1]<n:
                h=chain[-1]
                nxt=min(n,10*h//9)
                assert nxt>h and 10*h>=9*nxt
                if nxt<n:
                    assert F(nxt,h)>=F(19,18)
                chain.append(nxt)
            assert sum((F(1,x*x) for x in chain[:-1]),F(0))<=F(361,37*m*m)
            checks['scale_chains']+=1
    mu=joint(2,3)
    layer={key:v for key,v in mu.items() if key[1]==3}
    lifted=lift(reduce(layer,1),1,2)
    assert layer=={(2,3):F(1,8),(4,3):F(1,8)}
    assert norm(minus(layer,lifted))==F(1,3)
    assert norm(minus(layer,lifted))/p(2,3)==F(4,3)
    assert offset((1,1,1),27)==26
    assert 2*(1-F(1,9))==F(16,9)
    return {
        'passed':True,
        'scope':'Finite exact regression checks only; joint mixing for all parameters is proved in the lesson.',
        'arithmetic':'Python Fraction and integer modular inverses; no floating-point proof tests',
        'counts':dict(checks),
        'joint_law_range':'1 <= n <= 5, totals n through n+7',
        'exercise_masses':{'joint_discrepancy':'1/3','conditional_discrepancy':'4/3',
                           'rare_total_error':'16/9','rare_total_weighted_error':'2/9'},
        'lean_certification':False
    }


if __name__=='__main__':
    print(json.dumps(run(),indent=2))

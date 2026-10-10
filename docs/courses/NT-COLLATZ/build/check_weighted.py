"""Exact finite checks of weighted stopping and character-order identities.

No finite computation here proves arbitrary-power Fourier decay. That result
has an analytic proof in the lesson. The finite toy renewal law is explicitly
different from the marked holding law; residue laws sum geometric tails exactly.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json


def main():
    counts=defaultdict(int)
    law=((1,1),(1,2),(2,1))
    width=6
    def white(x,y):
        return 1<=x<=width and (x+2*y)%4!=0

    @lru_cache(None)
    def q(x,y,w):
        if x>width:
            return F(1)
        return w**white(x,y)*sum((q(x+a,y+b,w) for a,b in law),F(0))/3

    def direct_path_total(x,y,w):
        # Full tree until strip departure, evaluated without calling q.
        if x>width:
            return F(1)
        total=F(0)
        stack=[(x,y,F(1),0)]
        while stack:
            xx,yy,mass,visits=stack.pop()
            if xx>width:
                total+=mass*w**visits
                counts['complete_toy_paths']+=1
            else:
                visits+=white(xx,yy)
                for a,b in law:
                    stack.append((xx+a,yy+b,mass/3,visits))
        return total

    def stopped_total(x,y,s,extra,w):
        # Read through the first strict vertical crossing, then extra increments.
        total=F(0)
        stack=[(x,y,0,None,F(1))]
        while stack:
            xx,yy,height,left,mass=stack.pop()
            if left is None and height>s:
                left=extra
            if left==0:
                total+=mass*q(xx,yy,w)
                counts['stopped_prefixes']+=1
                continue
            # The current position is in the first factor, the endpoint is not.
            weight=w**white(xx,yy)
            for a,b in law:
                stack.append((xx+a,yy+b,height+b,
                              None if left is None else left-1,mass*weight/3))
        return total

    for x,y,w in product((1,3,6,7),(-1,0,2),(F(1,2),F(3,4))):
        expected=direct_path_total(x,y,w)
        assert expected==q(x,y,w)
        for s,extra in product(range(4),range(3)):
            assert stopped_total(x,y,s,extra,w)==expected
            counts['stopped_weight_identities']+=1

    # Integer-power equivalent of log(m/max(m-r,1)) <= r log(m)/(m-1).
    for m in range(2,81):
        for r in range(2*m+1):
            assert m**(m-1) <= m**r*max(m-r,1)**(m-1)
            counts['weight_ratio_inequalities']+=1

    for w,i,y in product((F(1,3),F(1,2),F(3,4)),(0,1),(F(1),F(3,2),F(4),F(20))):
        assert w**i*y <= y-(1-w)*i
        counts['correlated_reward_inequalities']+=1
    assert F(1,2)*(F(1,2)*1+4)==F(9,4)
    assert F(3,4)*F(5,2)==F(15,8)<F(9,4)
    assert 16*(F(1,128)+F(1,2)**7)==F(1,4)

    for r,k in product((F(1),F(33,32),F(17,16),F(9,8)),range(1,33)):
        ratio=3*r/4
        prefix=sum((F(1,4)*F(3,4)**(j-1)*r**j for j in range(1,k+1)),F(0))
        remainder=(r/4)*ratio**k/(1-ratio)
        assert prefix+remainder==r/(4-3*r)
        counts['exact_geometric_moment_remainders']+=1

    # Geometric exponents modulo the exact multiplicative order, not truncation.
    def inverse_power_law(modulus):
        u=pow(2,-1,modulus)
        d=1
        while pow(u,d,modulus)!=1:
            d+=1
        masses={pow(u,a,modulus):F(2**(d-a),2**d-1) for a in range(1,d+1)}
        assert len(masses)==d and sum(masses.values(),F(0))==1
        return masses

    laws={}
    for k in range(1,5):
        modulus=3**k
        invlaw=inverse_power_law(modulus)
        mu={0:F(1)}
        laws[k,0]=mu
        for n in range(1,7):
            nxt=defaultdict(F)
            for x,px in mu.items():
                for inv,pa in invlaw.items():
                    nxt[((3*x+1)*inv)%modulus]+=px*pa
            mu=dict(nxt)
            assert sum(mu.values(),F(0))==1
            laws[k,n]=mu
            counts['full_geometric_residue_laws']+=1

    # Direct reversed-sum state (offset,cumulative inverse) versus affine recursion.
    for k in range(1,4):
        modulus=3**k
        invlaw=inverse_power_law(modulus)
        pairs={(0,1):F(1)}
        for n in range(1,5):
            nxt=defaultdict(F)
            for (x,v),px in pairs.items():
                for inv,pa in invlaw.items():
                    vv=v*inv%modulus
                    nxt[(x+3**(n-1)*vv)%modulus,vv]+=px*pa
            pairs=dict(nxt)
            projected=defaultdict(F)
            for (x,_),mass in pairs.items():
                projected[x]+=mass
            assert dict(projected)==laws[k,n]
            counts['reversed_affine_law_identities']+=1

    for k in range(1,5):
        for n in range(k,7):
            assert laws[k,n]==laws[k,k]
            counts['exact_order_projection_laws']+=1
        for lower in range(1,k+1):
            reduced=defaultdict(F)
            for x,mass in laws[k,k].items():
                reduced[x%(3**lower)]+=mass
            assert dict(reduced)==laws[lower,lower]
            counts['quotient_pushforwards']+=1
    assert laws[1,1]=={1:F(1,3),2:F(2,3)}
    # omega=e^(-2*pi*i/3), omega^2=-1-omega, norm(a+b*omega)=a^2-a*b+b^2.
    aa,bb=F(-2,3),F(-1,3)
    assert aa*aa-aa*bb+bb*bb==F(1,3)
    for w,a,m in product((F(1,2),F(3,4)),(1,2,4),range(1,41)):
        assert F((m+1)**a,m**a)*w == (F((m+1)**a)*w**(m+2))/(F(m**a)*w**(m+1))
        counts['deterministic_weight_ratios']+=1

    print(json.dumps({'passed':True,'counts':dict(counts),
        'arithmetic':'Exact integers and fractions; geometric residue and moment tails summed algebraically, never discarded.',
        'ranges':{'toy_width':6,'vertical_thresholds':[0,3],'extra_steps':[0,2],'ratio_widths':[2,80],'residue_moduli':[3,9,27,81],'offset_lengths':[1,6]},
        'scope':'Finite regressions for stopped identities, algebraic weight inequalities, full-law residue projections and solved examples. The analytic weighted decay theorem and its all-n Fourier application are proved in the lesson, not certified by these finite calculations.'},indent=2))


if __name__=='__main__':main()

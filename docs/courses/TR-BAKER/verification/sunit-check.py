"""Exact certificates for the displayed S-unit example and numerical margins."""
from fractions import Fraction as Q
from math import factorial, gcd
from itertools import product
import json
import sympy as sp

def exp_interval(t, terms=40):
    low=sum((t**k/Q(factorial(k)) for k in range(terms+1)),Q(0))
    first=t**(terms+1)/Q(factorial(terms+1))
    ratio=t/Q(terms+2)
    assert 0<=ratio<1
    return low,low+first/(1-ratio)

def factors23(value):
    value=Q(value)
    if not value:return None
    sign=1 if value>0 else -1
    numerator,denominator=abs(value.numerator),value.denominator
    exponents=[]
    for p in (2,3):
        n=0
        while numerator%p==0:numerator//=p;n+=1
        while denominator%p==0:denominator//=p;n-=1
        exponents.append(n)
    return (sign,*exponents) if numerator==denominator==1 else None

def run():
    assert exp_interval(Q(1))[1]<3
    assert exp_interval(Q(1))[0]>2
    assert exp_interval(Q(1,2))[1]<2
    assert exp_interval(Q(2))[0]>6
    assert exp_interval(Q(5,2))[0]>10
    assert 64800*17*35<4*10**7
    q=10**25
    assert (200*192*4*10**7)**2<q
    assert 99+48*q**7<10**177
    assert 2*50**8*6*2*12<10**17
    assert Q(10**17,10**20)*2/64==Q(1,32000)<Q(1,6)
    assert 93+8+1+50==152
    assert 10**17*(2*152+Q(1,10**20*64))<10**20
    assert 12+6*10**177<10**178
    triples=[(1,1,2),(1,2,3),(1,3,4),(1,8,9)]
    orbits=[]
    for a,b,c in triples:
        t=Q(a,c)
        orbit={t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t}
        assert all(factors23(x) and factors23(1-x) for x in orbit)
        orbits.append(orbit)
    assert [len(row) for row in orbits]==[3,6,6,6]
    expected=set.union(*orbits);assert len(expected)==21
    found={sgn*Q(2)**a*Q(3)**b for sgn,a,b in product([-1,1],range(-3,4),range(-2,3))
           if factors23(1-sgn*Q(2)**a*Q(3)**b)}
    assert found==expected
    assert max(max(abs(x.numerator),x.denominator) for x in expected)==9
    assert max(abs(factors23(x)[1]) for x in expected)==3
    assert max(abs(factors23(x)[2]) for x in expected)==2
    smooth=sorted({2**a*3**b for a in range(13) for b in range(9)})
    smooth_set=set(smooth);sampled=set()
    for a in smooth:
        for b in smooth:
            if a<=b and gcd(a,b)==1 and a+b in smooth_set:sampled.add((a,b,a+b))
    assert sampled==set(triples)
    x,y,t1,t2,t3=sp.symbols('x y t1 t2 t3')
    r1=(x-t1*y)/(x-t3*y);r2=(x-t2*y)/(x-t3*y)
    assert sp.cancel(t1+(t2-t1)*r1/(r1-r2)-x/y)==0
    absorption=0
    for T,c3,L,H,h,epsilon,J,W in product([Q(1),Q(5)], [Q(2),Q(17)],
            [Q(1),Q(3)], [Q(1),Q(2),Q(7)], [Q(0),Q(1,100),Q(1),Q(50)],
            [Q(1,6),Q(2)], [Q(1),Q(13)], [Q(1),Q(4)]):
        tau=min(Q(1,2),epsilon*c3/(T*L));B=1+L*h
        assert T*max(W*H*J,tau*B/c3)<=epsilon*h+(T*W*J+T*tau/c3)*H
        absorption+=1
    degenerate=0
    for n in range(3,13):
        for k in range(13):
            row=[Q(2)**k,-Q(2)**k]+([Q(1)] if n%2 else [Q(2),Q(-1)])
            row.extend([Q(1),Q(-1)]*((n-len(row))//2))
            assert len(row)==n and sum(row)==1 and row[0]+row[1]==0
            assert all(factors23(z) for z in row)
            degenerate+=1
    return {'state':'passed','exact_numerical_margins':13,
            'ordered_sunit_solutions':[[str(x),str(1-x)] for x in sorted(expected)],
            'orbit_sizes':[3,6,6,6],'primitive_positive_triples':triples,
            'diagnostic_smooth_numbers':len(smooth),'height_maximum_argument':9,
            'finite_place_absorption_cases':absorption,'degenerate_cases':degenerate,
            'projective_recovery_identity':True,
            'scope':'Exact displayed solution certificate, rational scalar margins and supplementary cases. Completeness outside the sampled boxes follows from the written congruence proof, not enumeration.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))

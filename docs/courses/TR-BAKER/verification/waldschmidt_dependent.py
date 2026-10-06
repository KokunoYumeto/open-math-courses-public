"""Exact supplementary certificate for the radius-adapted dependent proof.

CC0. Independently authored by OpenAI Codex, GPT-6.1 Sol, Ultra.
All-dimensional and arithmetic arguments are in the lesson.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
import sympy as sy
from laurent_constant import Interval,E
from matveev_weighted_zero import lg

def ceiling(x):
    return -(-x.numerator//x.denominator)

def constants():
    assert lg(11).hi<3
    assert lg(66).hi<5
    assert lg(4160).hi<9
    assert (E**3).lo>20
    assert F(1,192)*F(33,32)+F(7,64)<F(1,8)
    assert 2**15>109
    ratios=[]
    for n in range(2,101):
        cn=2**(n+25)*n**(3*n+9)
        prev=2**(n+24)*(n-1)**(3*n+6)
        assert cn>2*(64*n*n+4)*prev
        assert cn>128*n*n
        assert (n-1)*(n+52)<64*n*n
        ratios.append(F((64*n*n+4)*prev,cn))
    return {"dimensions_checked":99,
            "largest_induction_exponent_ratio":str(max(ratios)),
            "vandermonde_height_fraction":str(F(1,192)*F(33,32)+F(7,64))}

def vandermonde():
    z=sy.Symbol("z")
    polys=0; samples=0
    for M in range(1,9):
        s0=M*(M+1)//2
        s1=M*(M+1)*(M+2)//6
        s2=M*(M-1)*(M+1)//6
        q=sy.prod((z**j-1)**(M+1-j) for j in range(1,M+1))
        qp=sy.Poly(q,z)
        assert qp.degree()==s1
        quotient,remainder=sy.div(qp,sy.Poly((z-1)**s0,z))
        assert remainder.is_zero
        assert quotient.eval(1)==sy.prod(j**(M+1-j) for j in range(1,M+1))
        reverse=sy.Poly((-1)**s0*z**s1*q.subs(z,1/z),z)
        assert qp==reverse
        # Pairwise determinant product verifies the exact extra monomial.
        detprod=sy.prod(z**j-z**i for i in range(M+1) for j in range(i+1,M+1))
        assert sy.Poly(detprod-z**s2*q,z).is_zero
        if M<=4:
            det=sy.Matrix([[z**(i*j) for j in range(M+1)] for i in range(M+1)]).det()
            assert sy.Poly(det-detprod,z).is_zero
        polys+=1
        for zz in [0,F(1,2),-1,sy.Rational(3,5)+sy.I*sy.Rational(4,5),
                   sy.Rational(2,3)+sy.I*sy.Rational(1,4),
                   2,sy.Rational(3,2)+sy.I*sy.Rational(1,2)]:
            val=qp.eval(zz)
            abs2=sy.expand(val*sy.conjugate(val))
            radius2=sy.expand(zz*sy.conjugate(zz))
            bound=(M+1)**(M+1)*max(1,radius2)**s1
            assert bool(abs2<=bound)
            samples+=1
    return {"polynomial_identities":polys,"exact_complex_samples":samples,
            "symbolic_determinants":4}

def adaptive_body():
    cases=0; cost=0
    for D,u in product([10**8,10**9,10**20,10**50,10**100],[F(1),F(2),F(5),F(10)]):
        L=lg(D)
        if L.lo<=16*u:continue
        for y in [1/u,F(1),F(2),F(4),F(10),F(100)]:
            if y<1/u or lg(y).hi>u:continue
            v=D/y
            assert (v-4*L-28*u-4).lo>0
            M=ceiling(64*y*u)
            eta=min(F(1),1/(64*y*M))
            assert M>=64 and M<=65*y*u
            assert lg(M+1).hi<7*u
            assert (D*F(M+2,3)*eta+D*lg(M+1)/M-v/8).hi<0
            assert (v/2-L-lg(M)).lo>0
            for n,t in product(range(2,31),[F(1),F(2),F(100)]):
                r=n-1
                logN=lg(factorial(r))+r*lg((t/y)/eta)
                assert (logN-64*n*n*u*t).hi<0
                cost+=1
            cases+=1
    # Small-degree regime is tested with the degree-only gap.
    small=0
    for D,u,y,n,t in product([1,2,100,10**6],[F(1),F(2)],
                             [F(1),F(2)],range(2,21),[F(1),F(10)]):
        if lg(D).hi>16*u or lg(y).hi>u:continue
        r=n-1
        logN=lg(factorial(r))+r*lg(11*D**3*t/y)
        assert (logN-64*n*n*u*t).hi<0
        small+=1
    return {"large_regime_parameter_cases":cases,
            "large_regime_relation_cost_cases":cost,
            "small_regime_relation_cost_cases":small}

def coefficient_transfer():
    specs=[
        ([1,1,-1],[F(1),F(2),F(3)],F(1)),
        ([1,1,-1],[F(3),F(2),F(1)],F(1)),
        ([1,-2,3],[F(1,2),F(2),F(1)],F(2)),
        ([2,-3,0],[F(2),F(1),F(3)],F(1)),
        ([0,1,-1],[F(2),F(3),F(1)],F(1)),
        ([1,1,-1,0],[F(2),F(3),F(1),F(4)],F(1)),
        ([1,-1,0,0],[F(1),F(2),F(3),F(4)],F(1)),
    ]
    counts={"deleted_last":0,"kept_last":0,"replaced_last":0}
    total=0
    for c,a,y in specs:
        n=len(c); support=[j for j in range(n) if c[j]]
        k=max(support,key=lambda j:(a[j],j))
        N=max(abs(x) for x in c)
        assert min(a)*y>=1
        for b in product(range(-3,4),repeat=n):
            if b[-1]==0:continue
            B=max([F(3)]+[F(abs(b[-1]))/a[j]+F(abs(b[j]))/a[-1] for j in range(n-1)])
            new=[c[k]*b[j]-c[j]*b[k] for j in range(n)]
            assert new[k]==0
            assert all(new[j]-c[k]*b[j]==-c[j]*b[k] for j in range(n))
            active=[j for j in range(n) if j!=k and new[j]]
            if not active:continue
            last=n-1 if k!=n-1 and new[-1] else active[-1]
            remaining=[j for j in range(n) if j!=k]
            Bnew=max([F(3)]+[F(abs(new[last]))/a[j]+F(abs(new[j]))/a[last]
                             for j in remaining if j!=last])
            assert Bnew<=4*N*B*y*a[k]
            label="deleted_last" if k==n-1 else ("kept_last" if new[-1] else "replaced_last")
            counts[label]+=1;total+=1
    assert all(counts.values())
    deletion=0
    for a,y,b in product([[F(1),F(2),F(3)],[F(1,2),F(2),F(1)]],
                          [F(2),F(3)],product(range(-2,3),repeat=3)):
        if b[-1]==0 or min(a)*y<1:continue
        B=max([F(3)]+[F(abs(b[-1]))/a[j]+F(abs(b[j]))/a[-1] for j in range(2)])
        active=[j for j in range(2) if b[j]]
        if not active:continue
        last=active[-1]
        Bnew=max([F(3)]+[F(abs(b[last]))/a[j]+F(abs(b[j]))/a[last]
                         for j in range(2) if j!=last])
        assert Bnew<=2*B*y*a[-1]
        deletion+=1
    return {"integer_eliminations":total,"elimination_branches":counts,
            "distinguished_zero_logarithm_cases":deletion}

def exponent_cancellations():
    D,y,w,u,P,t,C,Cp,wp=sy.symbols("D y w u P t C Cp wp",positive=True)
    a,v=sy.symbols("a v",positive=True)
    for n in range(1,31):
        assert sy.simplify(D**(n+2)*(v/D)**n/v**(n+1)-D**2/v)==0
    phi=C*D*y*w*u*P
    smaller=Cp*D*y*wp*u*P/t
    assert sy.simplify(smaller/phi-Cp/C*wp/w/t)==0
    assert sy.simplify((64*u*t)/(phi)-64*t/(C*D*y*w*P))==0
    return 30

def worked_example():
    assert (E*lg(2)).hi<2
    assert (E*lg(3)).hi<3
    assert (E*lg(6)).hi<5
    assert E.lo>F(5,2)
    c=[1,1,-1];b=[2,-3,4];a=[F(2),F(3),F(5)]
    new=[-b[j]-4*c[j] for j in range(3)]
    assert new==[-6,-1,0]
    oldmax=max(F(4)/a[j]+F(abs(b[j]))/a[2] for j in range(2))
    newmax=F(1,2)+F(6,3)
    assert oldmax==F(12,5) and newmax==F(5,2)
    assert lg(6).lo>lg(3).hi
    return {"transformed_coefficients":new,
            "old_homogeneous_maximum":str(oldmax),
            "new_homogeneous_maximum":str(newmax),
            "algebraic_parameters":[5,6]}

def check():
    return {"status":"passed","constants":constants(),"vandermonde":vandermonde(),
            "adaptive_body":adaptive_body(),"coefficient_transfer":coefficient_transfer(),
            "exponent_identities":exponent_cancellations(),
            "worked_example":worked_example(),
            "scope":"Both dependent Waldschmidt coefficient versions with their original constants. The radius-adapted circuit argument is proved in every dimension; finite checks supplement its nonvanishing-only extension."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))

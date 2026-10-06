"""Exact supplementary checks for the owned weighted zero and rank arguments.

CC0. Authored by OpenAI Codex, GPT-6.1 Sol, Ultra.
The lesson contains the infinite proofs; these finite checks supplement them.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, comb
from functools import lru_cache
import json
import sympy as sy
from laurent_constant import Interval, E, PI

@lru_cache(None)
def lg(x):
    return Interval(x).log()

def gamma_log(nu):
    if nu % 2 == 0:
        return lg(factorial(nu // 2))
    k = (nu + 1) // 2
    return lg(factorial(2*k)) - k*lg(4) - lg(factorial(k)) + lgpi/2

lgpi=PI.log()

def c_log(n,k):
    return (lg(F(16,k))-lg(factorial(n))+n
            +lg(2*n+1+2*k)+lg(n+2)+(n+1)*lg(4*(n+1))
            +k*(1+lg(F(n,2))))

def check():
    # Primitive relation lattices, including full and zero ranks.
    cases=[
        sy.Matrix([[3,-1],[-2,1]]),
        sy.Matrix([[-1,1,0],[-2,0,1],[1,0,0]]),
        sy.Matrix([[3,-1,-1],[-2,-1,1],[0,1,0]]),
        sy.Matrix([[-1,-2,1,0],[-1,1,0,1],[1,0,0,0],[0,1,0,0]]),
        sy.eye(3), sy.eye(3)]
    ranks=[1,1,2,2,0,3]
    subgroup_examples=[]
    minors=0
    t=sy.symbols('t')
    for V,nu in zip(cases,ranks):
        n=V.rows; d=n-nu
        assert abs(V.det())==1
        U=V[:,:nu]; W=V.inv()[nu:,:]
        assert W*U==sy.zeros(d,nu)
        assert W*V[:,nu:]==sy.eye(d)
        D=[1+(j%2) for j in range(n)]
        volume=0
        for I in combinations(range(n),d):
            J=tuple(j for j in range(n) if j not in I)
            wi=abs(W[:,list(I)].det())
            uj=abs(U[list(J),:].det())
            assert wi==uj
            volume+=wi*sy.prod(D[j] for j in I)
            minors+=1
        # Exact character counts for seven dilates, including holes.
        counts=[]
        for scale in range(4,11):
            chars=set()
            rows=[[int(W[i,j]) for j in range(n)] for i in range(d)]
            for exponent in product(*(range(scale*v+1) for v in D)):
                chars.add(tuple(sum(row[j]*exponent[j] for j in range(n))
                                for row in rows))
            counts.append(len(chars))
        polynomial=sy.interpolate([(i+4,counts[i]) for i in range(d+1)],t)
        assert sy.degree(polynomial,t)==d
        assert sy.Poly(polynomial,t).LC()==volume
        for i,count in enumerate(counts):
            assert polynomial.subs(t,i+4)==count
        # Gram determinant in a rational weighted metric.
        weights=[sy.Rational(j+2,j+1) for j in range(n)]
        gram=(U.T*sy.diag(*(v*v for v in weights))*U).det()
        minor_sum=sum((U[list(J),:].det()**2
                       *sy.prod(weights[j]**2 for j in J)
                       for J in combinations(range(n),nu)),sy.Integer(0))
        assert gram==minor_sum
        subgroup_examples.append({"n":n,"relation_rank":nu,
                                  "count_polynomial":str(polynomial),
                                  "leading_volume":int(volume),
                                  "weighted_gram":str(gram)})

    # Sharp positive intersection: Ga times the curve t -> (t^2,t^3).
    # Its relation is Y1^3=Y2^2, of positive degree vector (0,3,2).
    x,y,z=sy.symbols('D0 D1 D2')
    whole=x*y*z
    assert sy.expand(3*sy.diff(whole,y)+2*sy.diff(whole,z)-x*(2*y+3*z))==0
    # Codimension two with torus quotient (2,3,5); common degrees (0,3,2,1).
    D=sy.symbols('D0:4')
    upper=sy.Integer(0)
    for J in combinations(range(4),2):
        degree=[0,3,2,1]
        upper+=2*sy.prod(degree[j] for j in J)*sy.prod(D[i] for i in range(4) if i not in J)
    lower=D[0]*(2*D[1]+3*D[2]+5*D[3])
    assert all(c>=0 for c in sy.Poly(upper-lower,*D).coeffs())
    # Exact jet degree for union of additive cosets, with torus free.
    jet_cases=0
    X=sy.symbols('X')
    for e in range(1,6):
        for s in range(5):
            f=sy.prod((X-j)**(s+1) for j in range(e))
            assert sy.degree(f,X)==e*(s+1)
            for j in range(e):
                for order in range(s+1):
                    assert sy.diff(f,X,order).subs(X,j)==0
            jet_cases+=1

    assert (E**3).hi<21
    assert (E**6).hi<441
    assert (E**5*E.sqrt()).hi<245
    assert (PI*E).hi<9
    assert (4*E**2/(9*PI)).hi<F(6,5)
    assert (Interval(2).sqrt()*2).lo>F(14,5)
    assert lg(1000).hi<7 and lg(2).lo>F(1,2)
    assert F(1,5000)+F(1,10000)+F(71,8000)<F(1,100)

    zero_ratios=0; weight_ratios=0; reduction_ratios=0
    for n in range(2,51):
        # Rational sufficient ratios for all zero-count hypotheses.
        first=F(2**(n+2)*n**5,21*(n+1))
        assert first>8
        ratio=first
        for r in range(1,n+1):
            if r>1: ratio*=F(2*n**5,21*r*r)
            assert ratio>1
            zero_ratios+=1
        full=F(2**(n+1)*n*n,21*factorial(n)*factorial(n+1))*F(3*n**5,21)**n
        assert full>1
        zero_ratios+=1
        for nu in range(1,n):
            logC=(nu*lg(2)+F(nu,2)*(lg(2)+lg(n)-lgpi)
                  +gamma_log(nu)+lg(factorial(nu))+lg(comb(n,nu))/2)
            logq=(3+lg(nu+1)+lg(factorial(nu))+logC
                  -(n+1)*lg(2)-2*lg(n)+nu*(3-lg(3)-5*lg(n)))
            target=-lg(2)+(n-nu)*(lg(4)+2)
            assert (logq-target).hi<0
            if nu>=2:
                logg=(F(11,2)+lg(nu+1)+F(5,4)*lg(nu)
                      -F(2*n+3,2)*lg(2)-2*lg(n)
                      +F(nu,2)*(lg(4)+2+4*lg(nu)-lg(9)-lgpi-8*lg(n)))
                assert (logq-logg).hi<0
                assert (logg+lg(2)).hi<0
            weight_ratios+=1
        for k in [1,2]:
            for r in range(1,n):
                zeta=F(1) if r==1 else F(31,10)**(r-1)*F((r-1)**k,k)
                loggain=c_log(n,k)-(n-r)*(lg(4)+2)-lg(zeta)-lg(1000*n**3)
                assert loggain.lo>0
                ratio_log=c_log(n,k)-c_log(r,k)-(n-r)*(lg(4)+2)
                assert (ratio_log-lg(F(n+1,r+1))).lo>0
                reduction_ratios+=1

    # The source's unused n=nu=2 endpoint is not <=1/2.
    logg22=(F(11,2)+lg(3)+F(5,4)*lg(2)-F(7,2)*lg(2)-2*lg(2)
            +lg(4)+2+4*lg(2)-lg(9)-lgpi-8*lg(2))
    g22=logg22.exp()
    assert g22.lo>2 and g22.hi<3
    # Dyadic rounds cover stages before/after T_s=0 and the strong lower bound.
    rounds=0
    for n in range(2,9):
        eps=F(1,6000); c=2*(n+1)*(1+eps)
        for base in [1000*n**3+1,10**6*n**3,10**20*n**3]:
            for frac in [F(0),F(1,7),F(6,7)]:
                mu=base+frac; L=mu/c
                for stage in [14,18,40,80,120]:
                    T=[int(L/F(2**j)) for j in range(stage+1)]
                    final=int(mu)-(n+1)*sum(T[:-1])-n*T[-1]
                    assert final>=T[-1]+eps*mu/(1+eps)
                    bound=(eps*mu/(1+eps)+(n+2)*L/F(2**stage)
                           +(n+1)*(3+lg(L).hi/lg(2).lo)+n)
                    assert final<=bound
                    if stage>=14: assert final<mu/100
                    rounds+=1
    return {"status":"passed","subgroup_examples":subgroup_examples,
            "complementary_minors":minors,"character_counts":7*len(cases),
            "sharp_intersection_examples":2,"jet_examples":jet_cases,
            "zero_count_ratios":zero_ratios,"weighted_product_cases":weight_ratios,
            "rank_reduction_cases":reduction_ratios,"dyadic_rounds":rounds,
            "source_unused_endpoint_g_2_2":{"lower":str(g22.lo),"upper":str(g22.hi),
                                          "approx":float((g22.lo+g22.hi)/2)},
            "scope":"Finite subgroup, count, product and rank checks supplement the universal weighted-zero proof (8.72–8.83) and final application (8.120–8.130)."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))

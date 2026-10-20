"""Exact elementary contractions for ternary quartics.

Independent implementation of the classical umbral/Clebsch definitions,
with the normalization of Ohno's2007 preprint for the six parameters.
This module does not import or execute source-paper software.
"""
from itertools import product
from math import factorial, comb
import sympy as s

def indices(n):
    return [(i,j,n-i-j) for i in range(n,-1,-1) for j in range(n-i,-1,-1)]

def multiply(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            out[g]=out.get(g,0)+c*d
    return {e:s.expand(c) for e,c in out.items() if c!=0}

def contract(a,b):
    """a(d/dx)b; the two forms occupy dual variable spaces."""
    out={}
    for e,c in a.items():
        for f,d in b.items():
            if any(x>y for x,y in zip(e,f)):continue
            g=tuple(y-x for x,y in zip(e,f))
            factor=1
            for x,y in zip(e,f):factor*=factorial(y)//factorial(y-x)
            out[g]=out.get(g,0)+c*d*factor
    return {e:s.expand(c) for e,c in out.items() if c!=0}

def scale(a,c):return {e:s.expand(v*c) for e,v in a.items()}

def transfer(f):
    """Use F(-vX-wY,uX,uY), then divide by u^4 and u^6.

    The associated plane basis has cross product u(u,v,w).
    sigma = binaryI2/12, psi = binaryI3/432.
    """
    u,v,w=s.symbols('u v w')
    c=[s.Integer(0)]*5
    for (i,j,k),a in f.items():
        for q in range(i+1):
            c[q+j]+=a*(-1)**i*comb(i,q)*v**q*w**(i-q)*u**(j+k)
    e,d,h,b,a=c
    p2=s.Poly(s.expand(12*a*e-3*b*d+h*h),u,v,w)
    p3=s.Poly(s.expand(72*a*h*e-27*a*d*d-27*b*b*e+9*b*h*d-2*h**3),u,v,w)
    assert all(i>=4 for (i,j,k),c in p2.terms())
    assert all(i>=6 for (i,j,k),c in p3.terms())
    sigma={(i-4,j,k):s.expand(c/s.Integer(12)) for (i,j,k),c in p2.terms()}
    psi={(i-6,j,k):s.expand(c/s.Integer(432)) for (i,j,k),c in p3.terms()}
    return sigma,psi

def quadratic(a):
    return s.Matrix([[a.get((2,0,0),0),a.get((1,1,0),0)/s.Integer(2),a.get((1,0,1),0)/s.Integer(2)],
                     [a.get((1,1,0),0)/s.Integer(2),a.get((0,2,0),0),a.get((0,1,1),0)/s.Integer(2)],
                     [a.get((1,0,1),0)/s.Integer(2),a.get((0,1,1),0)/s.Integer(2),a.get((0,0,2),0)]])

def parameters(f):
    sigma,psi=transfer(f)
    rho=scale(contract(f,psi),s.Rational(1,144))
    tau=scale(contract(rho,f),s.Rational(1,12))
    a,b=quadratic(tau),quadratic(rho)
    basis=indices(2)
    normalized={e:s.Rational(factorial(e[0])*factorial(e[1])*factorial(e[2]),factorial(4))*c for e,c in f.items()}
    catalecticant=s.Matrix([[normalized.get(tuple(x+y for x,y in zip(e,g)),0) for g in basis] for e in basis])
    return {'I3':s.expand(contract(f,sigma).get((0,0,0),0)/72),
            'I6':s.expand(catalecticant.det()),
            'I9':s.expand(s.trace(a*b)),
            'I12':s.expand(b.det()),
            'I15':s.expand(a.det()),
            'I18':s.expand(s.trace(a.adjugate()*b.adjugate()))}

def from_expr(expr,variables):return dict(s.Poly(expr,*variables).terms())

def cubic_koszul_matrices(f):
    """Selected degree-seven and complementary degree-one matrices.

    Inputs are ordinary quartic coefficients. Both matrices depend linearly
    on them; their normalized determinant quotient is the discriminant on
    the chart where the complementary determinant is nonzero.
    """
    basis=indices(4);monomials=indices(7)
    column={e:i for i,e in enumerate(monomials)}
    owner=[next(i for i in range(3) if e[i]>=3) for e in monomials]
    selected=[15*i+basis.index(tuple(e[j]-3*(i==j) for j in range(3)))
              for e,i in zip(monomials,owner)]
    complement=[i for i in range(45) if i not in selected]
    gradient=[{tuple(e[j]-(i==j) for j in range(3)):e[i]*c
               for e,c in f.items() if e[i]} for i in range(3)]
    m=[[0]*36 for _ in range(36)]
    for row,(e,i) in enumerate(zip(monomials,owner)):
        multiplier=tuple(e[j]-3*(i==j) for j in range(3))
        for a,c in gradient[i].items():
            target=tuple(a[j]+multiplier[j] for j in range(3))
            m[row][column[target]]=c
    k=[[0]*9 for _ in range(45)]
    for pair,(i,j) in enumerate(((0,1),(0,2),(1,2))):
        for h,linear in enumerate(indices(1)):
            for slot,poly,sign in ((i,gradient[j],1),(j,gradient[i],-1)):
                for e,c in poly.items():
                    target=tuple(e[r]+linear[r] for r in range(3))
                    k[15*slot+basis.index(target)][3*pair+h]+=sign*c
    return m,[k[i] for i in complement],selected,complement

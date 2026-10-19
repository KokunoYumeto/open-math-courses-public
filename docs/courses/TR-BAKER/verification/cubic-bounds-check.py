"""Exact algebra checks for Lesson 13; not a full Thue-solution certificate."""
from fractions import Fraction as Q
from math import factorial
import json
import sympy as s

def run():
    x, y, z, w = s.symbols("x y z w")
    th = s.symbols("t1:4")
    beta = [x-t*y for t in th]
    assert s.expand((th[0]-th[1])*beta[2]+(th[1]-th[2])*beta[0]+
                    (th[2]-th[0])*beta[1]) == 0
    modulus = z**3-2
    assert s.rem((z-1)*(1+z+z*z)-1, modulus, z) == 0
    assert s.rem((x-z*y)*(x*x+z*x*y+z*z*y*y)-(x**3-2*y**3),modulus,z) == 0
    # Trace directly from multiplication matrices, not a floating-point root computation.
    Mz=s.Matrix([[0,0,2],[1,0,0],[0,1,0]])
    Mw=s.Matrix([[0,-1],[1,-1]])
    basis=[s.kronecker_product(Mw**j,Mz**i) for j in range(2) for i in range(3)]
    gram=s.Matrix(6,6,lambda i,j:s.trace(basis[i]*basis[j]))
    assert gram.det()==-314928
    assert s.det(Mz-s.eye(3))==1
    # The scalar simplification must retain homogeneity's scale term.
    Z=s.symbols("Z")
    B=3*Z+8; E=1+3*(2*B+2); C=1+E+3*B
    assert s.expand(2*C)==54*Z+160
    # Independently compare the specialization to the general Lesson 12 formulas.
    d=6; delta=314928; c=2*delta; J=c**(d*(d*d+1))
    V=8*d**5*c*J
    assert V==8*6**5*629856**223
    P=d*d*(2*3**d+1)**d
    L=d*factorial(d)*V**d*(2*d*d*P)**d
    S=d*(d*V+5)+5; C0=64800*d*d*S*(2*S+1)
    q=(1600*C0*L*(d+1))**2
    G=d*V*(8*L+4*(d+5)*q**(2*d+1))+4*d+3
    assert G==6*V*(8*L+44*((11200*C0*L)**2)**13)+27
    T=1+3+1+2*V; W=4+2+2*T; Z0=2*T+G*W
    B=3*Z0+2+3+3; E=1+3*(2*B+1+1); C=1+E+3*B
    N=2*C
    assert N==54*Z0+160
    # Rational root enclosure gives rho<2 and the factor constant 25.
    assert Q(5,4)**3<2<Q(4,3)**3<8
    assert (1+2*Q(4,3))**2 <25
    for pair in [(1,0),(-1,-1)]:
        assert pair[0]**3-2*pair[1]**3==1
    # The Pell sequence demonstrates unboundedness without using a solver.
    a,b=1,0
    for k in range(1,41):
        old=a
        a,b=3*a+4*b,2*a+3*b
        assert a*a-2*b*b==1 and a>old
    return {"state":"passed","trace_gram_determinant":-314928,
            "N0_bit_length":N.bit_length(),"exact_cubic_solution_substitutions":2,
            "pell_recurrence_checks":40,
            "scope":"Exact identities, order discriminant, full constant substitution, and stated examples. No exhaustive cubic solution claim."}

if __name__=="__main__":
    print(json.dumps(run(),indent=2))

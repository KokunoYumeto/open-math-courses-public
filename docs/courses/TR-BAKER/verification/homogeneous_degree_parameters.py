"""Exact checks of the homogeneous binomial basis and weighted parameters."""
from fractions import Fraction as F
import json
from math import comb
import sympy as sp
from degree_capacity_parameters import constants
from laurent_constant import Interval, E


def check():
    x,z=sp.symbols("x z")
    basis_checks=0
    derivative_checks=0
    for bm in [-3,2]:
        mons=[x**a*z**b for a in range(4) for b in range(4-a)]
        polys=[x**a/sp.factorial(a)*sp.prod(bm*z-j for j in range(b))
               /sp.factorial(b) for a in range(4) for b in range(4-a)]
        matrix=sp.Matrix([[sp.Poly(p,x,z).coeff_monomial(v) for v in mons]
                          for p in polys])
        assert matrix.det() != 0
        # Check actual integer-value evaluations, including negative arguments.
        for value in range(-8,9):
            for b in range(5):
                evaluated=sp.prod(value-j for j in range(b))/sp.factorial(b)
                assert evaluated.is_integer
                basis_checks+=1
    # Compute the differential operator directly on X^a exp(tX)/a!.
    # Compare with the derivative of its polynomial symbol at t.
    for sigma in range(7):
        q=sp.prod(z+j for j in range(sigma))/sp.factorial(sigma)
        coeffs=sp.Poly(q,z)
        for a in range(5):
            for t in [-2,-1,0,1,2]:
                f=x**a*sp.exp(t*x)/sp.factorial(a)
                actual=sum(coeffs.coeff_monomial(z**j)
                           *sp.diff(f,x,j).subs(x,0) for j in range(sigma+1))
                expected=sp.diff(q,z,a).subs(z,t)/sp.factorial(a)
                assert sp.simplify(actual-expected)==0
                derivative_checks+=1
    weighted_checks=0
    for m,root in [(1,1),(4,2),(9,3)]:
        n,c=constants(m)
        for degree,v in [(1,1),(19,1),(2,14)]:
            y=F(degree,v)
            le=max(F(1),y,1/y)
            lb=2*max(le,F(10))
            b1=37*m*root*lb
            b2=10*root*le
            for r in [1,5,100]:
                a=F(v*r,degree)
                u=c*degree*y*b1*b2*r**m
                xsize=u/(degree*b1)
                t0=(xsize/2).__floor__()
                t1=(n*y*b1).__floor__()
                sj=(u/(degree*(t1+1)*a)).__floor__()
                h=(b1/(6*m)).__floor__()
                # b_m=3, every other b_j=-2; the empty maximum is zero.
                cross=0 if m==1 else 5*sj
                rhs=E+F(2*m*(m+1),t0)*E*cross
                assert rhs.log().hi < b1
                assert h*Interval(3).log().hi < b1
                assert 4*sj<t0
                weighted_checks+=1
    return {
        "status":"passed","integer_basis_evaluations":basis_checks,
        "basis_change_scope":"all total-degree<=3 polynomials in two variables; b_m=-3 or2; exact determinant",
        "normalized_operator_checks":derivative_checks,
        "weighted_parameter_checks":weighted_checks,
        "weighted_scope":"m1,4,9; D,v=(1,1),(19,1),(2,14); r=1,5,100; integer coefficients3,-2 and empty maximum",
        "limits":"Supplementary parameter checks for the full homogeneous proof (8.198–8.201). Universal arguments and the dependent extension are proved in the lesson."
    }


if __name__=="__main__":
    print(json.dumps(check(),indent=2))

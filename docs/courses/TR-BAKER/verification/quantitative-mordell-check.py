"""Exact symbolic checks for the quantitative Mordell reduction.

The inequalities and covering argument are proved in the lesson.
This program checks the polynomial identities and transformation signs.
"""
import json
import sympy as sp

S, T, a, b, c, d = sp.symbols("S T a b c d")
p, q, r, s = sp.symbols("p q r s")
u, v, x, y, k, a0 = sp.symbols("u v x y k a0")
F = a*S**3 + b*S**2*T + c*S*T**2 + d*T**3


def hessian_form(f):
    return sp.expand(
        (sp.diff(f, S, T)**2 - sp.diff(f, S, 2)*sp.diff(f, T, 2))/4
    )


def jacobian_form(f):
    h = hessian_form(f)
    return sp.expand(sp.diff(f, S)*sp.diff(h, T)
                     - sp.diff(f, T)*sp.diff(h, S))


checks = []


def same(label, lhs, rhs):
    assert sp.expand(lhs-rhs) == 0, label
    checks.append(label)


P, Q, R = b*b-3*a*c, b*c-9*a*d, c*c-3*b*d
U = 2*b**3-9*a*b*c+27*a*a*d
disc = sp.discriminant(F.subs(T, 1), S)
same("cubic discriminant",
     disc, b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d)
same("Hessian formula", hessian_form(F), P*S*S+Q*S*T+R*T*T)
same("Hessian discriminant", Q*Q-4*P*R, -3*disc)
same("seminvariant identity", 4*P**3, U*U+27*a*a*disc)

trans = {S:p*S+q*T, T:r*S+s*T}
G = sp.expand(F.subs(trans, simultaneous=True))
det = p*s-q*r
same("Hessian covariance, arbitrary matrix",
     hessian_form(G), det**2*hessian_form(F).subs(trans, simultaneous=True))
same("Jacobian covariance, arbitrary matrix",
     jacobian_form(G), det**3*jacobian_form(F).subs(trans, simultaneous=True))

alpha, z, t = sp.symbols("alpha z t", real=True)
root_cubic = a*(S-alpha)*(S*S-2*z*S+z*z+t*t)
same("one real and two conjugate roots: discriminant",
     sp.discriminant(sp.expand(root_cubic), S),
     -4*a**4*t*t*((alpha-z)**2+t*t)**2)

rho = sp.symbols("rho0:3")
all_real = sp.Poly(a*sp.prod(S-ri for ri in rho), S)
aa, bb, cc, dd = all_real.all_coeffs()
same("positive Hessian root formula", bb*bb-3*aa*cc,
     a*a*sum((rho[i]-rho[j])**2 for i in range(3) for j in range(i+1,3))/2)

theta = sp.symbols("theta")
integral_polynomial = theta**3+b*theta**2+a*c*theta+a*a*d
same("integral factor norm",
     sp.resultant(integral_polynomial, a*u-theta*v, theta),
     a*a*F.subs({S:u,T:v}))

ph = [u-ri*v for ri in rho]
same("three-root identity",
     (rho[1]-rho[2])*ph[0]+(rho[2]-rho[0])*ph[1]+(rho[0]-rho[1])*ph[2], 0)
same("small-quantity numerator",
     (rho[2]-rho[0])*ph[1]-(rho[1]-rho[0])*ph[2],
     -(rho[1]-rho[2])*ph[0])

mordell = S**3-3*x*S*T*T-2*y*T**3
same("Mordell discriminant", sp.discriminant(mordell.subs(T,1),S),
     -108*(y*y-x**3))
same("Mordell x recovery", hessian_form(mordell).subs({S:1,T:0}), 9*x)
same("Mordell y recovery", jacobian_form(mordell).subs({S:1,T:0}), 54*y)
same("reducible Mordell factorization",
     (a0**3-3*x*a0)**2-4*x**3,
     (a0*a0-x)**2*(a0*a0-4*x))
same("reducible root recovery",
     4*(a0*a0-x)-(a0*a0-4*x), 3*a0*a0)

a1,a2,a3,a4,a6 = sp.symbols("a1 a2 a3 a4 a6")
weierstrass = y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6
cubic = 4*x**3+(a1*a1+4*a2)*x*x+(2*a1*a3+4*a4)*x+a3*a3+4*a6
same("general Weierstrass completion of square",
     (2*y+a1*x+a3)**2-cubic,4*weierstrass)

print(json.dumps({"state":"passed","exact_identities":len(checks),
                  "checks":checks},indent=2))

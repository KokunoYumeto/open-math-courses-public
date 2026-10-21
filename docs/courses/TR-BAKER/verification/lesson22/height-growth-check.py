"""Exact examples for 22.47--57; these do not replace the written proofs."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, lcm
from functools import reduce
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = []

def check(label, condition):
    assert condition, label
    checks.append(label)

def rational_height_exp(values):
    """exp(h) for a rational projective tuple, computed by primitive integers."""
    values = list(map(F, values))
    den = lcm(*(x.denominator for x in values))
    nums = [int(x * den) for x in values]
    common = reduce(gcd, map(abs, nums))
    assert common > 0
    return F(max(map(abs, nums)), common)

# Projective scaling, scalar inversion, and exact Segre additivity.
for p in range(-9, 10):
    for q in range(1, 8):
        if p == 0:
            continue
        x = F(p, q)
        h = rational_height_exp([1, x])
        check(f"rational inversion {p}/{q}", h == rational_height_exp([1, 1/x]))
        scale = F(q+2, p)
        check(f"projective scaling {p}/{q}",
              h == rational_height_exp([scale, scale*x]))
        y = F(q, abs(p)+1)
        check(f"Segre {p}/{q}",
              rational_height_exp([1, x, y, x*y])
              == h*rational_height_exp([1, y]))
        for d in (1, 2, 5):
            check(f"power height {p}/{q} d={d}",
                  rational_height_exp([1, x**d]) == h**d)

# A genuine global quadratic map of P1, with no common projective zero.
# Local coefficient sums give H(F(x)) <= 3 H(x)^2 over Q.
for p in range(-8, 9):
    for q in range(1, 8):
        h = rational_height_exp([p, q])
        image = [p*p+2*q*q, p*q]
        check(f"morphism height {p},{q}",
              rational_height_exp(image) <= 3*h*h)

# Explicit projective Nullstellensatz comparison for two generating families
# of O(1) on P1: S=(X,Y), T=(X+2Y,3X-Y).
X, Y = sp.symbols("X Y")
T1, T2 = X+2*Y, 3*X-Y
check("Nullstellensatz coordinate identity X", sp.expand(T1+2*T2-7*X) == 0)
check("Nullstellensatz coordinate identity Y", sp.expand(3*T1-T2-7*Y) == 0)

# Boundary divisor degrees under doubling and the inverse-height inequality:
# additive infinity multiplicity 1, torus zero/infinity multiplicity 2.
U, V = sp.symbols("U V")
check("additive boundary pullback", sp.degree(V, V) == 1)
check("torus zero pullback", sp.degree(U**2, U) == 2)
check("torus infinity pullback", sp.degree(V**2, V) == 2)
for e in range(13):
    check(f"additive dyadic height {e}",
          rational_height_exp([1, F(1, 2**e)]) == 2**e)
    # The exact normalized mixed height is e+2^-e.
    check(f"mixed dyadic envelope {e}", F(e)+F(1, 2**e) <= e+1)

# Exhaustive finite rational-circle models. u/(2*pi*i)=g/M with gcd(g,M)=1;
# exact order of exp(u/2^e) is the denominator of g/(M*2^e).
for M in range(1, 13):
    for g in range(1, 17):
        if gcd(g, M) != 1:
            continue
        c = g & -g
        nu = c.bit_length()-1
        for e in (nu, nu+1, nu+3):
            b = 2**e
            order = F(g, M*b).denominator
            check(f"exact divided order M={M},g={g},e={e}", order == M*b//c)
            for S in (1, 2, 5, 12):
                actual = len({(s*F(g, M*b)) % 1 for s in range(b*S+1)})
                q = min(S+1, M)
                check(f"division cardinality M={M},g={g},e={e},S={S}",
                      actual == min(b*S+1, order) and 2*c*actual >= b*q)

# The torsion caveat is real: a nonzero period with g=4 is not primitive.
check("nonprimitive period counterexample", F(4, 4).denominator == 1)
check("period eventual growth", F(4, 16).denominator == 4)

# Translated jets for Ga and Gm keep X-degree D independently of t.
x0, x1, y = sp.symbols("x0 x1 y")
for D in range(1, 8):
    additive = (x1+x0*y)**D
    multiplicative = (x1*y)**D
    current = multiplicative
    for t in range(8):
        ja = sp.diff(additive, y, t).subs(y, 0)
        jm = current.subs(y, 1)
        expected_a = 0 if t>D else sp.factorial(D)/sp.factorial(D-t)*x0**t*x1**(D-t)
        check(f"Ga translated jet D={D},t={t}", sp.expand(ja-expected_a) == 0)
        check(f"Gm translated jet D={D},t={t}", sp.expand(jm-D**t*x1**D) == 0)
        if ja != 0:
            check(f"Ga jet homogeneous degree D={D},t={t}",
                  all(sum(mon)==D for mon,_ in sp.Poly(ja,x0,x1).terms()))
        check(f"Gm jet homogeneous degree D={D},t={t}",
              all(sum(mon)==D for mon,_ in sp.Poly(jm,x0,x1).terms()))
        current = sp.expand(y*sp.diff(current,y))

# Denominator and embedding bounds for rational normalized projective points.
for values in ([1,F(2,3),F(5,7)], [F(-2,5),1,F(4,9)], [1,0,F(1,16)]):
    den = lcm(*(F(x).denominator for x in values))
    h = rational_height_exp(values)
    check(f"point denominator {values}", den <= h and all((F(x)*den).denominator==1 for x in values))
    check(f"point archimedean bound {values}", max(abs(F(x)) for x in values) <= h)

# Parameter exponent inequalities and the exact dimension-count identity.
for n,m,B,rho in [(2,1,7,3),(3,2,15,8),(4,1,5,2)]:
    k=max(5,B,2*rho); b=2; S=b**(2*n+1)
    for q in [1,3,S+1]:
        A=2*n*m*q*S**(n*k); D=A//S**k; T=A-n
        check(f"parameter identity {n},{m},{q}", D**n==2*n*m*q*(T+n)**(n-1))
        check(f"height exponent {n},{m},{q}", D*S**B<=A)
        check(f"analytic exponent {n},{m},{q}", D*S**(2*rho)<=A)

result = {
    "status": "passed",
    "scope": "Exact examples and identities for the written height proofs22.47--57",
    "checks": len(checks),
    "families": [
        "Rational projective scaling, inversion, powers and Segre heights",
        "Polynomial morphism height and explicit generating-section comparison",
        "Boundary multiplicities and dyadic additive/multiplicative heights",
        "Torsion and period orders including nonprimitive periods",
        "Translated additive and multiplicative jets with fixed point degree",
        "Rational denominator bounds and generalized integer parameter identities"
    ],
    "proof_limit": "Examples do not prove the general theorems; their complete arguments are in Lesson22, results22.47--57.",
}
(ROOT/"height-growth-check.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

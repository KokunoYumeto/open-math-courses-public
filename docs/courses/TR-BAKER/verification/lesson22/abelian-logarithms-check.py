"""Exact examples for 22.67--76; these do not replace the written proofs."""
from pathlib import Path
from fractions import Fraction
import datetime
import json
import sympy as s

checks = {}
x, y, z = s.symbols("x y z")
F = y*y*z-x**3+x*z*z
assert s.expand(F.subs({x:-x, y:s.I*y}, simultaneous=True)+F) == 0
assert s.simplify(-1/s.I-s.I) == 0
assert s.gcd(s.Poly(x**3-x,x),s.Poly(3*x*x-1,x)).degree() == 0
assert s.diff(F,z).subs({x:0,y:1,z:0}) == 1
checks["smooth_cubic_and_differential_automorphism"] = 4

# Multiplication by i on the actual integral basis (Omega,i Omega).
J=s.Matrix([[0,-1],[1,0]])
assert J**2 == -s.eye(2)
assert J.det() == 1
assert s.Matrix([[1,s.I]])*J == s.I*s.Matrix([[1,s.I]])
checks["integral_CM_action"] = 3

# Exact Gaussian division: ties use floor(q+1/2), still giving norm <= 1/2.
def nearest(q):
    return (q+Fraction(1,2)).numerator // (q+Fraction(1,2)).denominator
count=0
for a in range(-3,4):
    for b in range(-3,4):
        for c in range(-2,3):
            for d in range(-2,3):
                if c==d==0: continue
                norm=c*c+d*d
                qr=nearest(Fraction(a*c+b*d,norm))
                qi=nearest(Fraction(b*c-a*d,norm))
                rr=a-(qr*c-qi*d); ri=b-(qr*d+qi*c)
                assert 2*(rr*rr+ri*ri) <= norm
                assert rr*rr+ri*ri < norm
                count+=1
checks["Gaussian_Euclidean_remainders"] = count

# Coordinate relation in Exercise22.76, over Q(i) and hence over Qbar.
M=s.Matrix([[1,s.I,0],[0,1,1]])
kernel=s.Matrix([-s.I,1,-1])
assert M.rank()==2
assert M*kernel==s.zeros(2,1)
assert s.Matrix.hstack(*M.nullspace(),kernel).rank()==1
aug=s.diag(s.eye(2),M)
assert aug.rank()==4
checks["complete_CM_relation_space"] = 4

# Branch changes add rational periods. The Q(i)-span of {u,Omega}
# is unchanged under u -> u+(a+b i)Omega, with exact determinant 1.
count=0
for a in range(-8,9):
    for b in range(-8,9):
        T=s.Matrix([[1,0],[a+b*s.I,1]])
        assert T.det()==1
        assert T.inv()*T==s.eye(2)
        count+=1
checks["branch_basis_changes"] = count

# Clear rational denominators in a fractional Gaussian ideal.
# This verifies the concrete rescaling used in the lattice argument.
count=0
for n in range(1,9):
    for a,b in [(1,0),(0,1),(1,1),(2,-1),(-3,2)]:
        alpha=(s.Integer(a)+s.I*b)/n
        T=s.Matrix([[s.re(alpha),-s.im(alpha)],
                    [s.im(alpha),s.re(alpha)]])
        assert T.det()==s.Rational(a*a+b*b,n*n)
        assert n*T==s.Matrix([[a,-b],[b,a]])
        assert T*J==J*T
        count+=1
checks["rational_CM_lattice_rescalings"] = count

result={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "state":"passed","checks":checks,"total":sum(checks.values()),
        "scope":"Exact cubic, Gaussian-lattice and CM-relation examples; "
                "the general logarithm and period theorems are checked "
                "by their written proofs and programme dependencies.",
        "not_proved_by_computation":["analytic subgroup theorem",
            "Poincare reducibility","general period dimension formula"]}
dest=Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

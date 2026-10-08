"""Exact finite checks of the displayed gauge, correction and energy identity.

These checks supplement the complete proofs, not their functional-analytic scope.
Run with Python and SymPy. Independent new code: CC0-1.0.
"""
from pathlib import Path
import hashlib, json
import sympy as s

ROOT = Path(__file__).resolve().parent
x, z = s.symbols("x z", real=True)
I = s.I
star = lambda a: a.conjugate().T
pair = lambda a, b: (star(b) * a)[0]
zero = lambda a: all(s.simplify(e) == 0 for e in a)
groups = []

def add(name, cases, scope):
    groups.append({"name": name, "cases": cases, "passed": True, "scope": scope})

# Nilpotent ordered gauge, including a variable tangential parameter.
E = s.Matrix([[0, 1], [0, 0]])
cases = 0
for t in [-2, -1, 0, 1, 2]:
    K = 2*I*t*E
    S = s.eye(2)+x*t*E
    H = s.eye(2)-x*t*E
    M = s.Matrix([[I, 1+z], [0, -2]])
    L = K-M
    Ds = -I*S.diff(x)
    kappa = H*(M-L)*S/2
    assert zero(2*Ds+K*S) and zero(H*S-s.eye(2))
    assert zero(H*M*S+H*Ds-kappa)
    assert zero(H*L*S+H*Ds+kappa)
    if t == 1:
        assert zero(kappa-s.Matrix([[I, 1+z-I+x*(2+I)], [0, -2]]))
    cases += 1
add("Ordered gauge and both normal form coefficients", cases, "Symbolic identities in x,z; five exact matrix choices.")

# Check the full two-slot transformation at arbitrary finite complex jets.
cases = 0
for t in range(1, 7):
    S = s.Matrix([[1, I*t], [0, 2]])
    H = S.inv()
    U = star(H)
    derivatives = [s.Matrix([[I, t], [1, -I]]), s.Matrix([[t, 1-I], [I, 2]])]
    dH = [-H*d*S.inv() for d in derivatives]  # D(H) = -H(D S)H.
    dU = [-star(d) for d in dH]
    g = [[s.Integer(1), s.Integer(0)], [s.Integer(0), s.Integer(t+1)]]
    L = [s.Matrix([[I, 1], [t, 2-I]]), s.Matrix([[1, I], [2, -t]])]
    M = [s.Matrix([[2, t-I], [I, -1]]), s.Matrix([[I, 2], [t, 1]])]
    c = s.Matrix([[t, I], [1-I, 2]])
    u = s.Matrix([1+I, t]); p = s.Matrix([2, 1-I])
    du = [s.Matrix([I, 2]), s.Matrix([t, 1+I])]
    dp = [s.Matrix([1, -I]), s.Matrix([2-I, t])]
    vp, fp = [S*du[j]+derivatives[j]*u for j in range(2)], [U*dp[j]+dU[j]*p for j in range(2)]
    original = sum(pair(g[i][j]*vp[j], fp[i]) for i in range(2) for j in range(2))
    original += sum(pair(L[j]*vp[j], U*p)+pair(M[j]*S*u, fp[j]) for j in range(2))+pair(c*S*u, U*p)
    lp = [H*L[j]*S-sum((dH[i]*g[i][j]*S for i in range(2)), s.zeros(2)) for j in range(2)]
    mp = [H*M[i]*S+sum((H*g[i][j]*derivatives[j] for j in range(2)), s.zeros(2)) for i in range(2)]
    cp = H*c*S+sum((H*L[j]*derivatives[j]-dH[j]*M[j]*S for j in range(2)), s.zeros(2))
    cp -= sum((dH[i]*g[i][j]*derivatives[j] for i in range(2) for j in range(2)), s.zeros(2))
    transformed = sum(pair(g[i][j]*du[j], dp[i]) for i in range(2) for j in range(2))
    transformed += sum(pair(lp[j]*du[j], p)+pair(mp[j]*u, dp[j]) for j in range(2))+pair(cp*u, p)
    assert s.simplify(original-transformed) == 0
    cases += 1
add("Complete transformed weak form", cases, "Both differentiated slots, all lower terms and complex conjugation.")

# Exact Gaussian boundary correction on single Fourier modes.
eps, beta = s.symbols("epsilon beta", positive=True)
assert s.simplify((-I*s.diff(-I*x*beta, x)).subs(x, 0)+beta) == 0
for n in range(-8, 9):
    jn, jnext = s.exp(-eps**2*n**2), s.exp(-eps**2*(n+1)**2)
    defect = jn-jnext
    assert s.simplify(-jnext+jn-defect) == 0
add("Gaussian Robin correction", 17, "Exact Fourier multipliers and the sign of the normal derivative.")

# An exact finite tangential model with noncommuting self-adjoint operators.
# Multiplying by exp(-x) reduces every integral to a polynomial moment.
def integrate_exp2(poly):
    return s.simplify(sum(co*s.factorial(k[0])/2**(k[0]+1) for k,co in s.Poly(s.expand(poly), x).terms()))

A0 = s.Matrix([[1, I], [-I, 2]])
A1 = s.Matrix([[0, 1], [1, -1]])
C0 = s.Matrix([[2, 1+I], [1-I, -2]])
R0 = s.Matrix([[3, I], [-I, 1]])
R1 = s.Matrix([[1, 2-I], [2+I, -1]])
cases = 0
for t in [-1, 1, 2]:
    A = (1+x)*A0+t*x*x*A1
    C = (2-t*x)*C0
    Rh, Ra = (3+x)*R0, (1-t*x)*R1
    B = C-I*A.diff(x)/2
    S0, J0 = (A*Rh+Rh*A)/2, (A*Rh-Rh*A)/2
    E11 = 2*A.diff(x)
    E10 = B.diff(x)+I*J0-A*Ra
    E01 = star(E10)
    E00 = (A*Rh.diff(x)+Rh.diff(x)*A)/2+I*(C*Rh-Rh*C)-(star(B)*Ra+Ra*B)
    assert zero(E00-star(E00))
    p = s.Matrix([1+(1+I)*x, I+t*x*x])
    D = lambda p: -I*(p.diff(x)-p)
    u1 = D(p)
    Pu, Qu = D(u1)-(Rh+I*Ra)*p, A*u1+B*p
    lhs = integrate_exp2(2*s.im(pair(Pu, Qu)))
    volume = integrate_exp2(pair(E11*u1,u1)+pair(E10*p,u1)+pair(E01*u1,p)+pair(E00*p,p))
    boundary = (pair(A*u1,u1)+2*s.re(pair(B*p,u1))+pair(S0*p,p)).subs(x,0)
    assert s.simplify(lhs-volume-boundary) == 0
    cases += 1
add("Noncommuting finite tangential energy model", cases, "Independent exact integration with all normal coefficient derivatives; not a PDE discretization theorem.")

# Oriented scalar profiles, retaining the complex lower coefficient.
cases = 0
for p in [s.Integer(1), x, 1+x]:
    for t in [-2, 0, 1]:
        for r, b, c in [(2, 0, 0), (-1, 2, 3), (0, -2, -1)]:
            D = lambda p: t*p-I*(s.diff(p,x)-p)
            u1 = D(p)
            lhs = integrate_exp2(2*s.im((D(u1)-(r+I*b)*p)*s.conjugate(-u1+c*p)))
            f0, df0 = p.subs(x,0), (s.diff(p,x)-p).subs(x,0)
            boundary = (-t*t+2*c*t-r)*f0*f0-df0*df0
            volume = 2*b*(t-c)*integrate_exp2(p*p)
            assert s.simplify(lhs-volume-boundary) == 0
            cases += 1
add("Oriented scalar profiles", cases, "Three profiles, three oscillations and three lower-coefficient choices.")

source = ROOT/"matrix-normal-gauge-and-boundary-commutator.md"
result = {"passed": True, "groups": groups, "total_cases": sum(g["cases"] for g in groups),
          "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "finite_checks_do_not_replace_proofs": True}
(ROOT/"model-check.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"groups":len(groups),"cases":result["total_cases"],"passed":True}))

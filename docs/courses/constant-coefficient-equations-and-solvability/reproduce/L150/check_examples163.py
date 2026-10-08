"""Independent physical disk integrals, real Hessians and characteristic checks."""
from pathlib import Path
import json
import math
import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
mp.mp.dps = 65
checks = []

def equal(name, actual, expected, tolerance=2e-10):
    error = abs(complex(actual)-complex(expected))
    limit = tolerance*(1+abs(complex(expected)))
    checks.append(dict(name=name, absolute_error=error, allowed_error=limit, passed=error<=limit))
    assert error <= limit, (name, actual, expected, error)

def bound(name, lhs, rhs, tolerance=1e-12):
    lhs, rhs = float(lhs), float(rhs)
    checks.append(dict(name=name, lhs=lhs, rhs=rhs, passed=lhs<=rhs+tolerance*(1+abs(rhs))))
    assert checks[-1]["passed"], (name, lhs, rhs)

# Gauss-Legendre radius and independent periodic angle integration use the
# actual complex exponential and complex density, not its moment formula.
nodes, weights = np.polynomial.legendre.leggauss(64)
theta = np.arange(128)*2*np.pi/128
a = 1+.5j
for s in [.2, .5]:
    radius = (nodes+1)*s/2
    w = radius[:, None]*np.exp(1j*theta)[None, :]
    area_weights = (weights*s/2*radius)[:, None]*(2*np.pi/len(theta))
    for degree in [0, 1, 2]:
        density = math.factorial(degree)*(degree+1)/(1j**degree*np.pi*s**(2*degree+2))*np.conj(w)**degree
        norm = np.sum(np.abs(density)**2*area_weights)
        equal(f"disk-density-norm-s{s}-degree{degree}", norm,
              math.factorial(degree)**2*(degree+1)/(np.pi*s**(2*degree+2)))
        for x in [-2, -.25, 0, 1.7]:
            actual = np.sum(density*np.exp(1j*x*(a+w))*area_weights)
            equal(f"physical-disk-exponential-s{s}-degree{degree}-x{x}",
                  actual, x**degree*np.exp(1j*a*x))

# Direct high-precision differentiation of the defining jet norm is compared
# with the separately expanded real polynomial and its calculus.
def jet_log(x, y, T):
    z = mp.mpc(x, y)
    M2 = T*T+y*y
    return mp.log(mp.sqrt(abs(z*z-1)**2+abs(2*z)**2*M2+4*M2*M2))

for T in [2, 8, 32]:
    for x, y in [(0, 0), (1, 0), (mp.mpf(".4"), mp.mpf("1.3")), (2, 5)]:
        A = x**4+(6*y*y+4*T*T-2)*x*x+9*y**4+(12*T*T+2)*y*y+4*T**4+1
        Ax = 4*x**3+2*(6*y*y+4*T*T-2)*x
        Ay = 12*y*x*x+36*y**3+2*(12*T*T+2)*y
        Axx = 12*x*x+12*y*y+8*T*T-4
        Ayy = 12*x*x+108*y*y+24*T*T+4
        equal(f"jet-defining-value-T{T}-at{x},{y}", mp.exp(2*jet_log(x,y,T)), A)
        equal(f"physical-log-jet-x-derivative-T{T}-at{x},{y}",
              mp.diff(lambda b: jet_log(b,y,T),x), Ax/(2*A))
        equal(f"physical-log-jet-y-derivative-T{T}-at{x},{y}",
              mp.diff(lambda b: jet_log(x,b,T),y), Ay/(2*A))
        physical = (mp.diff(lambda b: jet_log(b,y,T),x,2)
                    +mp.diff(lambda b: jet_log(x,b,T),y,2))/4
        expanded = ((Axx+Ayy)/A-(Ax*Ax+Ay*Ay)/(A*A))/8
        equal(f"physical-Levi-jet-T{T}-at{x},{y}", physical, expanded)
    equal(f"jet-at-simple-zero-T{T}", mp.exp(2*jet_log(1,0,T)), 4*T*T+4*T**4)

# Away-zero jet comparison uses actual polynomial derivative values at complex
# points and the explicit Cauchy constant in NV14.
r = 1
cauchy = [(math.factorial(j)*(4/r)**j*(1.5)**2) for j in range(3)]
C = np.linalg.norm(cauchy)
for z in [0, 2, 3j, -2+1j, .1+.7j]:
    distance = min(abs(z-1), abs(z+1))
    assert distance >= r/2
    J = math.sqrt(abs(z*z-1)**2+abs(2*z)**2+4)
    bound(f"away-root-jet-comparison-{z}", J, C*abs(z*z-1))

for T in [2, 8, 32, 4096]:
    f = lambda y: (1+y*y)**mp.mpf(".75")/(T*T+y*y)
    peak = mp.sqrt(3*T*T-4)
    equal(f"physical-ratio-derivative-at-peak-T{T}", mp.diff(f,peak), 0)
    equal(f"physical-ratio-peak-T{T}", f(peak),
          mp.power(3,mp.mpf(".75"))/4/mp.power(T*T-1,mp.mpf(".25")))
    for q in [0, .25, 1, 2, 6, 50]:
        bound(f"uniform-curvature-ratio-T{T}-q{q}",
              f(mp.mpf(str(q))*T), mp.power(2,mp.mpf(".75"))/mp.sqrt(T))
bound("explicit-half-curvature-budget", 2**.75/64, 1/36)

# Actual differentiated solution, rather than a reused symbol identity.
aa = mp.mpc(1,.5)
u = lambda x: (1+x)*mp.exp(1j*aa*x)
for x in [-1, 0, mp.mpf(".6")]:
    actual = -mp.diff(u,x,2)+2j*aa*mp.diff(u,x)+aa*aa*u(x)
    equal(f"physical-double-root-ODE-at{x}", actual, 0)
equal("physical-compact-transpose-pairing", -mp.diff(u,0,2)+2j*aa*mp.diff(u,0)+aa*aa*u(0), 0)
bound("inner-cutoff-radius", .4, 5*.8/8)
bound("strict-outer-cutoff-radius", 7*.8/8, .8)

# Nonreal Laplace characteristic vectors have orthogonal real/imaginary parts
# of equal length. Perturbations test the full tube regularity estimate.
for length, angle in [(0,0), (.3,.7), (2,1.1), (7,2.2)]:
    xi = length*np.array([np.cos(angle),np.sin(angle)])
    eta = length*np.array([-np.sin(angle),np.cos(angle)])
    z = xi+1j*eta
    equal(f"actual-Laplace-complex-characteristic-{length},{angle}", np.sum(z*z), 0)
    for exponent in [0, .5, 3]:
        bound(f"characteristic-weight-{length}-s{exponent}",
              (1+np.dot(xi,xi))**(exponent/2), (1+np.linalg.norm(eta))**exponent)
        perturb = np.array([.2+.3j, -.1+.15j])
        assert np.linalg.norm(perturb)<1
        zz = z+perturb
        bound(f"tube-weight-{length}-s{exponent}",
              (1+np.dot(zz.real,zz.real))**(exponent/2),
              3**exponent*(1+np.linalg.norm(zz.imag))**exponent)

result = dict(schema="AN02-L150-independent-example-checks163/v1", status="PASS",
              checks=len(checks), records=checks,
              maximum_equality_error=max(row.get("absolute_error",0) for row in checks),
              scope="Independent actual disk exponential/norm quadratures, high-precision real jet Hessians and radial extrema, physical double-root ODE, complex characteristic and tube weights.",
              calculations_are_proof_supplements=True, general_proof_or_recursive_closure_inferred=False)
(HERE/"independent-example-checks163.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:result[k] for k in ["status","checks","maximum_equality_error","scope"]},ensure_ascii=False))

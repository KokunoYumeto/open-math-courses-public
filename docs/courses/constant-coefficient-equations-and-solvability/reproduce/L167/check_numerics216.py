"""Supplementary algebra, physical Gaussian integrals and carrier checks.

These probes do not replace the general proofs or an independent review.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 65
records = []

def record(name, error, tolerance, **details):
    value = float(error)
    assert value <= tolerance, (name, str(error), tolerance)
    records.append({"probe": name, "absolute_error": value,
                    "absolute_tolerance": tolerance, **details})

# A two-variable colliding-root example checks the actual contour quotient.
# The boundary remains free of zeros even when the two interior roots collide.
rho = mp.mpf(1)
for s in [0, mp.mpf("0.1"), -mp.mpf("0.2"), mp.mpc("0.1", "0.2")]:
    for t in [0, mp.mpf("0.3"), mp.mpc("-0.2", "0.25")]:
        total = 0
        count = 256
        for k in range(count):
            theta = 2*mp.pi*k/count
            w = rho*mp.exp(1j*theta)
            denominator = w*w-s
            assert abs(denominator) >= mp.mpf("0.7")
            numerator = denominator*(1+s+w*w)
            total += numerator/denominator * w/(w-t)
        quotient = total/count
        record("Cauchy quotient through colliding roots",
               abs(quotient-(1+s+t*t)), 1e-50,
               s=str(s), t=str(t), trapezoid_points=count)

# The finite-jet identity is compared with a physical derivative distribution,
# using an entire exponential divisor rather than a polynomial divisor.
a = mp.mpf(3)/4
b = mp.mpf(1)/2
for degree in range(7):
    for zeta in [mp.mpf(0), mp.mpc("0.2", "0.3"), mp.mpc("-0.7", "-0.1")]:
        f = lambda x: sum(mp.mpf(k+1)*x**k for k in range(degree+1))
        A = lambda z: -1j*z*mp.exp(-1j*(b-a)*z)
        jet_value = sum(mp.mpf(k+1)*(1j**k)*mp.diff(A,zeta,k)
                        for k in range(degree+1))
        physical = mp.diff(lambda x: f(x)*mp.exp(-1j*x*zeta), b-a)
        record("reflected derivative and entire finite-jet product",
               abs(jet_value-physical), 1e-55, degree=degree, frequency=str(zeta))

# Geometry is checked from all physical Minkowski vertices, independently of
# the prelisted pentagon and the figure's support formula.
rect = np.array([[-.5,-.25],[.5,-.25],[.5,.25],[-.5,.25]])
minus = np.array([[0,0],[-2,0],[0,-1]])
physical_sums = (rect[:,None,:]+minus[None,:,:]).reshape(-1,2)
hull = np.array([[-2.5,-.25],[-.5,-1.25],[.5,-1.25],[.5,.25],[-2.5,.25]])
for angle in np.linspace(0,2*np.pi,401):
    eta = np.array([np.cos(angle),np.sin(angle)])
    physical = max(physical_sums@eta)
    predicted = .5*abs(eta[0])+.25*abs(eta[1])+max(0,-2*eta[0],-eta[1])
    record("Minkowski carrier support from twelve physical vertices",
           abs(physical-predicted), 2e-14, angle=float(angle))
    record("five-vertex convex hull has the same support",
           abs(max(hull@eta)-physical), 2e-14, angle=float(angle))
domain_lower = np.max(np.array([[-3,-2],[-1,-2],[-3,-1]]),axis=0)
domain_upper = np.min(np.array([[1,1],[3,1],[1,2]]),axis=0)
assert np.array_equal(domain_lower,[-1,-1]) and np.array_equal(domain_upper,[1,1])
assert np.all(hull>[-3,-2]) and np.all(hull<[1,1])
assert np.all(rect>domain_lower) and np.all(rect<domain_upper)
record("exact open erosion and strict compact carrier containment",0,0)

# Exact rational side exponents, with no numerical maximization.
x = Q(2,5); eta = Q(1,5)
right = -(x-2)**2+eta**2
left = -(x+2)**2+eta**2
assert right == -Q(63,25) and left == -Q(143,25)
assert right < -Q(15,16) and left < -Q(15,16)
record("exact rational Gaussian vertical-side exponents",0,0,
       right=str(right),left=str(left),general=str(-Q(15,16)))

# Physical real-line integrals of a compact smooth function which is analytic
# near the observation points. The uncut polynomial Gaussian average is
# 1+z^2+1/(2j). The cutoff error has the independently derived real-tail bound.
def step(t):
    if t <= 0: return mp.mpf(0)
    if t >= 1: return mp.mpf(1)
    u=mp.exp(-1/t)
    v=mp.exp(-1/(1-t))
    return u/(u+v)

def cutoff(t):
    q=abs(t)
    if q<=2: return mp.mpf(1)
    if q>=3: return mp.mpf(0)
    return step(3-q)

for j in [2,8,32]:
    for real,imaginary in [("0","0"),("0.4","0.2"),("-0.5","0.1"),("0.3","-0.2")]:
        z=mp.mpc(real,imaginary)
        physical=mp.sqrt(j/mp.pi)*mp.quad(
            lambda t:mp.exp(-j*(z-t)**2)*cutoff(t)*(1+t*t),
            [-3,-2,mp.re(z),2,3])
        polynomial=1+z*z+mp.mpf(1)/(2*j)
        # For |Re z|<=1/2 and |Im z|<=1/5, exterior distance is >=3/2.
        # Splitting the real Gaussian exponent in half bounds the error by
        # sqrt(2)*(3/2+2/j)*exp(-j*(9/8-1/25)) <=5 exp(-217j/200).
        tail_bound=5*mp.exp(-mp.mpf(217)*j/200)
        error=abs(physical-polynomial)
        assert error<=tail_bound
        record("compact analytic germ, physical complex Gaussian integral",
               error,float(tail_bound),j=j,observation=str(z),
               analytic_average=str(polynomial))
        record("convergence to the nonzero analytic germ",
               abs(physical-(1+z*z)),float(1/mp.mpf(2*j)+tail_bound),
               j=j,observation=str(z))

report={
    "status":"PASS","observed_at_utc":datetime.now(timezone.utc).isoformat(),
    "probe_count":len(records),"mpmath_decimal_digits":mp.mp.dps,
    "maximum_absolute_error":max(x["absolute_error"] for x in records),
    "maximum_algebra_or_geometry_error":max(x["absolute_error"] for x in records
        if "Gaussian integral" not in x["probe"] and
           "analytic germ" not in x["probe"]),
    "maximum_compact_cutoff_vs_exact_polynomial_gaussian_error":max(
        x["absolute_error"] for x in records if "Gaussian integral" in x["probe"]),
    "finite_gaussian_germ_bias_is_expected":"The finite-j Gaussian average of 1+z^2 is 1+z^2+1/(2j); its nonzero bias is checked against the proved rate, rather than treated as quadrature error.",
    "meaning":"Supplementary physical integrals, exact signs, colliding roots, carrier geometry and rational contour bounds. General proofs are in the formal lesson; no independent review claimed.",
    "records":records,
}
path=ROOT/"independent-example-probes216.json"
path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:report[k] for k in ["status","probe_count","mpmath_decimal_digits","maximum_absolute_error"]}))

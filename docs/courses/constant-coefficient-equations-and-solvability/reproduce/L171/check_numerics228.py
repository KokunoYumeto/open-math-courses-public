"""Supplementary example checks; these do not replace the mathematical proofs."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import mpmath as mp

OWN = Path(__file__).resolve().parent
mp.mp.dps = 65
counts = {}
largest = mp.mpf(0)


def test(kind, condition):
    assert condition, kind
    counts[kind] = counts.get(kind, 0)+1


def equal(kind, left, right):
    global largest
    error = abs(left-right)
    largest = max(largest, error)
    test(kind, error < mp.mpf("1e-61"))


harmonic = Fraction(0)
for n in range(1, 257):
    harmonic += Fraction(1, n)
    value = mp.mpf(harmonic.numerator)/harmonic.denominator
    test("harmonic_integral_bounds",
         mp.log(n+1) <= value <= 1+mp.log(n))
for base in (3, 5):
    r = mp.mpf(1)/(base*base)
    equal("integrated_geometric_identity",
          mp.quad(lambda t: 1/(1-t), [0, r]), -mp.log(1-r))
    for n in range(1, 33):
        tail = mp.quad(lambda t: t**n/(1-t), [0, r])
        upper = mp.power(base, -2*n)/((base*base-1)*(n+1))
        test("image_tail_upper_bound", tail > 0 and tail <= upper)

for j in range(1, 17):
    x = [complex(Fraction(k-j, 7), Fraction(k+j, 11))
         for k in range(j+2)]
    a = [complex(Fraction(2*k+1, 9), Fraction(j-k, 13))
         for k in range(j)]
    left = sum(a[k]*x[k+1] for k in range(j))
    right = sum(v*w for v,w in zip([0]+a, x))
    test("bilinear_product_shift", abs(left-right) < 1e-12)

def f(x):
    return mp.exp(x)+2*x**3+mp.sin(3*x)

for k in range(1, 22):
    x = mp.mpf(2)/3+mp.mpf(3)*k/22
    y = x-mp.mpf(2)/3
    for order in range(5):
        equal("translated_smooth_forcing",
              mp.diff(lambda t:f(t+mp.mpf(2)/3), y, order),
              mp.diff(f, x, order))

def primitive(x):
    return x**3/3+1-mp.cos(x)

for k in range(-7, 8):
    x = mp.mpf(k)/5
    for order in range(7):
        equal("smooth_antiderivative",
              mp.diff(primitive, x, order+1),
              mp.diff(lambda t:t*t+mp.sin(t), x, order))

for k in range(-80, 81):
    xi = mp.mpf(k)/4
    zeta = xi+1j
    test("slow_decrease_window_radius", 1 <= 2*mp.log(2+abs(xi)))
    test("derivative_slow_decrease", abs(1j*zeta) >= (2+abs(xi))**-2)
    test("difference_slow_decrease",
         abs(1-mp.exp(-1j*zeta)) >= (2+abs(xi))**-2)

parameters = [mp.mpf(-2), mp.mpf("-.5"), mp.mpf(".5"), mp.mpf(2),
              mp.mpc(".3", "1.2")]
for lam in parameters:
    for k in range(-8, 9):
        x = mp.mpf(k)/4
        u = lambda t:mp.exp(lam*t)/(1-mp.exp(-lam))
        equal("nonresonant_difference_solution", u(x)-u(x-1), mp.exp(lam*x))
for k in range(-3, 4):
    lam = 2*mp.pi*1j*k
    for j in range(-8, 9):
        x = mp.mpf(j)/4
        u = lambda t:t*mp.exp(lam*t)
        equal("resonant_difference_solution", u(x)-u(x-1), mp.exp(lam*x))

equal("fourier_weight_integral",
      2*mp.quad(lambda t:(1+t)**2/(1+t*t)**2, [0, 1, mp.inf]),
      mp.pi+2)
radius = mp.mpf(1)/4
raw = lambda t:mp.exp(-1/(1-16*t*t)) if abs(t)<radius else mp.mpf(0)
mass = mp.quad(raw, [-radius, 0, radius])
rho = lambda t:raw(t)/mass
equal("probability_bump_mass", mp.quad(rho, [-radius, 0, radius]), 1)
equal("probability_bump_first_moment",
      mp.quad(lambda t:t*rho(t), [-radius, 0, radius]), 0)
left_mass = -mp.quad(lambda x:rho(x+mp.mpf(1)/2),
                    [-mp.mpf(3)/4, -mp.mpf(1)/2, -mp.mpf(1)/4])
right_mass = mp.quad(lambda x:rho(x-mp.mpf(1)/2),
                    [mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4])
equal("zero_mass_adjoint_family", left_mass+right_mass, 0)
equal("primitive_plateau_mass", -left_mass, 1)
test("shifted_interval_margins",
     min(Fraction(2)-Fraction(1,2), Fraction(7,2)-Fraction(3))
     == min(Fraction(5,2)-1, 4-Fraction(7,2)) == Fraction(1,2))
for j in range(1, 65):
    a = Fraction(1, 2**j)
    test("nonextendible_forcing_test_support",
         0 < 1-Fraction(5,4)*a < 1-Fraction(3,4)*a < 1)
    test("nonextendible_forcing_lower_exponent",
         Fraction(1)/(Fraction(5,4)*a)**2 == Fraction(16,25)/a**2)

report = {
    "status": "PASS", "decimal_precision": 65,
    "probe_count": sum(counts.values()), "probe_kinds": counts,
    "largest_numerical_identity_error": str(largest),
    "exact_rational_geometry_and_harmonic_sums": True,
    "proof_replacement": False,
    "source_code_sha256": hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest().upper(),
}
(OWN/"supplementary-example-probes228.json").write_text(
    json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report))

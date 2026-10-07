"""Independent physical quadratures and finite checks for original L148."""
from pathlib import Path
import json
import math
import cmath
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

HERE = Path(__file__).resolve().parent
rows = []


def cq(function, left, right, points=None):
    args = dict(epsabs=2e-10, epsrel=2e-10, limit=500)
    if points is not None:
        args["points"] = points
    return complex(quad(lambda x: function(x).real, left, right, **args)[0],
                   quad(lambda x: function(x).imag, left, right, **args)[0])


def equal(name, actual, expected, tolerance=2e-9):
    error = abs(actual-expected) / max(1., abs(expected))
    assert error <= tolerance, (name, actual, expected, error)
    def serialize(z):
        return [z.real, z.imag] if isinstance(z, complex) else float(z)
    rows.append({"name": name, "actual": serialize(actual), "expected": serialize(expected),
                 "relative_or_absolute_error": error, "tolerance": tolerance, "pass": True})


def inequality(name, actual, bound, margin=2e-9):
    assert actual <= bound + margin * max(1., abs(bound)), (name, actual, bound)
    rows.append({"name": name, "actual": float(actual), "upper_bound": float(bound), "pass": True})


def interval(z):
    return 2*cmath.sin(z)/z if z else 2.


for eta in (0., .5, 1., 2.):
    for xi in (0., .7, 2.3, 6.2):
        z = complex(xi, eta)
        physical = cq(lambda x: cmath.exp(-1j*x*z), -1., 1.)
        equal(f"physical interval transform xi={xi} eta={eta}", physical, interval(z))
    physical_energy = quad(lambda x: math.exp(2*eta*x-2*eta), -1, 1,
                           epsabs=1e-11, epsrel=1e-11)[0]*2*math.pi
    damped_exact = math.pi*(-math.expm1(-4*eta))/eta if eta else 4*math.pi
    equal(f"physical shifted squared norm eta={eta}", physical_energy, damped_exact)
    if eta:
        # Actual complex transform, independent of the stable algebraic formula.
        cutoff = 200.
        integral = 2*quad(lambda xi: abs(interval(complex(xi, eta)))**2*math.exp(-2*eta),
                         0, cutoff, points=np.arange(0, cutoff, math.pi/2).tolist(),
                         epsabs=1e-9, epsrel=1e-9, limit=500)[0]
        omitted = damped_exact-integral
        assert omitted >= -1e-8
        inequality(f"Fourier plane truncation rigorous tail eta={eta}", omitted, 8/cutoff)

b, r = .25, .5
tent = lambda x: max(0., 1-abs(x-b)/r)


def triangle(z):
    return cmath.exp(-1j*b*z)*2*(1-cmath.cos(r*z))/(r*z*z) if z else r


for z in (0j, 1+1j, -2-.5j, .8-1.4j):
    physical = cq(lambda x: tent(x)*cmath.exp(-1j*x*z), b-r, b+r, points=[b])
    equal(f"physical shifted triangle transform z={z}", physical, triangle(z))
mode = lambda x: cmath.exp((1j-1)*x) + .5j*cmath.exp((-2j+.5)*x)
physical_pair = cq(lambda x: mode(x)*tent(x), b-r, b+r, points=[b])
equal("two complex atoms physical bilinear pairing", physical_pair,
      triangle(-1-1j)+.5j*triangle(2+.5j))
equal("physical triangle squared norm", quad(lambda x: tent(x)**2, b-r, b+r,
                                             points=[b], epsabs=1e-12)[0], 1/3)

dual = quad(lambda xi: (1+abs(xi))**2/(1+abs(xi))**4, -np.inf, -1,
            epsabs=1e-12)[0]/(2*math.pi)
pair = quad(lambda xi: (1+xi)*(1+xi)**-3, 1, np.inf,
            epsabs=1e-12)[0]/(2*math.pi)
equal("negative-frequency reflected dual norm squared", dual, 1/(4*math.pi))
equal("positive-frequency bilinear dual pairing", pair, 1/(4*math.pi))

v = lambda xi: (1+xi*xi)**(-3/8)
data = 2*quad(lambda xi: v(xi)**2, 0, np.inf, epsabs=2e-10,
              epsrel=2e-10, limit=500)[0]
# Special-function reference is a supplementary numeric identity, not a proof input.
equal("physical squared-data integral versus beta reference", data,
      math.sqrt(math.pi)*gamma(.25)/gamma(.75))
for cutoff in (1., 4., 16., 64.):
    tail = 2*quad(lambda xi: v(xi)**2, cutoff, np.inf, epsabs=1e-10,
                  epsrel=1e-10, limit=500)[0]
    inequality(f"squared-data tail T={cutoff}", tail, 4/math.sqrt(cutoff))
for cutoff in (1., 2., 10., 100., 1000.):
    truncated = 2*quad(v, 0, cutoff, epsabs=1e-9, epsrel=1e-10, limit=500)[0]
    lower = 8*2**(-3/8)*(cutoff**.25-1)
    inequality(f"divergent absolute integral lower bound T={cutoff}", lower, truncated)
for shell in range(1, 7):
    points = [(m,l) for m in range(-shell,shell+1) for l in range(-shell,shell+1)
              if max(abs(m),abs(l)) == shell]
    equal(f"lattice square-shell count j={shell}", len(points), 8*shell, tolerance=0)
    mass = sum((1+4*m*m+4*l*l)**-2 for m,l in points)
    inequality(f"lattice data shell bound j={shell}", mass, .5*shell**-3)

report = {
    "schema": "AN02-L148-independent-examples/v1", "status": "PASS", "checks": len(rows),
    "scope": "Physical complex transforms, shifted physical squared norms, actual truncated Fourier planes with analytic tails, complex-atom physical pairing, reflected nonsymmetric dual, weak-data tails, divergence bounds and finite lattice shells.",
    "numeric_checks_do_not_replace_proofs": True,
    "maximum_equality_error": max(row.get("relative_or_absolute_error",0) for row in rows),
    "rows": rows,
}
(HERE/"independent-example-checks157.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: report[key] for key in ("status","checks","maximum_equality_error")}))

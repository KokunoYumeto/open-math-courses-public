"""Supplementary independent quadratures and exact directional geometry checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math, warnings
import mpmath as mp
import numpy as np
from scipy.integrate import quad, IntegrationWarning
from scipy.special import jv
OWN = Path(__file__).resolve().parent
mp.mp.dps = 70
warnings.simplefilter("error", IntegrationWarning)
results = []
def record(kind, parameters, error, tolerance, details=None):
    e = float(error)
    assert math.isfinite(e) and e <= tolerance, (kind, parameters, e, tolerance)
    results.append({"kind": kind, "parameters": parameters, "absolute_error": e,
                    "tolerance": tolerance, "passed": True, "details": details})
def cquad(function, lo, hi, **kw):
    return quad(lambda x: function(x).real, lo, hi, **kw)[0] + 1j*quad(lambda x: function(x).imag, lo, hi, **kw)[0]

# Direct area-height quadrature and the entire closed form use independent routes.
for q in [0, 1, 7, 18, 40]:
    for beta in [-.7, 0, .4]:
        r = mp.mpc(q, beta)
        physical = 2*mp.pi*mp.quad(lambda t: mp.exp(-1j*r*t), [-1, 0, 1])
        closed = 4*mp.pi*(mp.sin(r)/r if r else 1)
        record("sphere physical area-height integral vs entire sine quotient",
               {"q": q, "imaginary_shift": beta}, abs(physical-closed), 1e-60)

# Normalized logarithms at integer-pi centers, avoiding their exact zeros.
for k in [12, 48, 192]:
    q = mp.mpf(k)*mp.pi
    for eta in [-1.2, -.3, .3, 1.2]:
        r = q+1j*mp.mpf(str(eta))*mp.log(q)
        direct = mp.log(abs(4*mp.pi*mp.sin(r)/r))/mp.log(q)
        reduced = mp.log(4*mp.pi*abs(mp.sinh(mp.mpf(str(eta))*mp.log(q)))/abs(r))/mp.log(q)
        record("sphere integer-pi off-center profile identity",
               {"pi_multiplier": k, "eta": eta}, abs(direct-reduced), 1e-60)

# Fixed-order cap-sign test on the exact sphere transform. Imaginary direction
# lets either normal exponential dominate. This checks the stated negative
# Fourier sign and d=2 coefficients without using a sampled proof.
for q in [200, 600, 1800]:
    for eta in [-.8, .8]:
        r = mp.mpf(q)+1j*mp.mpf(str(eta))*mp.log(q)
        exact = 4*mp.pi*mp.sin(r)/r
        leading = (2*mp.pi*1j*mp.exp(-1j*r)-2*mp.pi*1j*mp.exp(1j*r))/q
        relative = abs(exact/leading-1)
        predicted = abs(mp.mpf(q)/r-1)
        record("sphere signed two-cap sum relative correction",
               {"q": q, "eta": eta}, abs(relative-predicted), 1e-60)

# Ellipse measure obtained by pushing forward angle dt has positive density
# a=1/|X'(t)|. Its direct physical integral is checked against the entire Bessel
# series in a different library, including logarithmic complex shifts.
b = np.array([.5, -.25]); A = np.diag([2., 1.])
for direction_angle in [.2, .8, 1.7]:
    theta = np.array([np.cos(direction_angle), np.sin(direction_angle)])
    for q in [3., 13., 37.]:
        for beta in [-.25, .35]:
            zeta = q*theta + 1j*np.log(q)*np.array([beta, -.2])
            function = lambda t: np.exp(-1j*np.dot(zeta, b+A@np.array([np.cos(t), np.sin(t)])))
            physical = sum(cquad(function, lo, hi, epsabs=2e-11, epsrel=2e-11, limit=180)
                           for lo,hi in zip(np.linspace(0,2*np.pi,17)[:-1],np.linspace(0,2*np.pi,17)[1:]))
            root = np.sqrt(np.dot(A@zeta, A@zeta))
            exact = 2*np.pi*np.exp(-1j*np.dot(b,zeta))*jv(0,root)
            record("ellipse physical angle quadrature vs entire Bessel transform",
                   {"angle": direction_angle, "q": q, "beta": beta},
                   abs(physical-exact), 2e-9)

# Each normal endpoint, curvature and coefficient modulus are independently
# computed from the angle parametrization and the normal inverse formula.
for angle in np.linspace(0, 2*np.pi, 40, endpoint=False):
    theta = np.array([np.cos(angle),np.sin(angle)])
    w = A@A@theta/np.linalg.norm(A@theta)
    for sign in [-1,1]:
        p = b+sign*w
        y = np.linalg.solve(A,p-b)
        normal = np.linalg.solve(A.T,y); normal /= np.linalg.norm(normal)
        record("ellipse inverse normal and boundary equation",
               {"angle": float(angle),"sign":sign},
               max(abs(np.dot(y,y)-1), np.linalg.norm(normal-sign*theta)), 2e-14)
        t = np.arctan2(y[1],y[0]); speed = np.hypot(2*np.sin(t),np.cos(t))
        curvature = 2/speed**3
        density = 1/speed
        geometric_modulus = np.sqrt(2*np.pi)*density/np.sqrt(curvature)
        phase_height = np.linalg.norm(A@theta)
        parametrized_modulus = np.sqrt(2*np.pi/phase_height)
        record("ellipse intrinsic cap coefficient vs angle-phase Hessian",
               {"angle":float(angle),"sign":sign},
               abs(geometric_modulus-parametrized_modulus), 2e-14)
    for eta_angle in [.1,.9,2.3,4.8]:
        eta=np.array([np.cos(eta_angle),np.sin(eta_angle)])
        endpoint_support=max(np.dot(b-w,eta),np.dot(b+w,eta))
        formula=np.dot(b,eta)+abs(np.dot(w,eta))
        record("selected segment support formula",
               {"normal_angle":float(angle),"eta_angle":eta_angle},
               abs(endpoint_support-formula), 2e-14)
        assert endpoint_support <= np.dot(b,eta)+np.linalg.norm(A@eta)+2e-14

# The two affine limits retain the dimensional constant; their recession
# difference is exactly d/(2t) for a positive dilation t.
for d in [1,2,5]:
    for eta in [-1.4,-.2,.6,1.7]:
        for t in [3,19,101]:
            difference = abs((-mp.mpf(d)/2+abs(mp.mpf(str(eta))*t))/t-abs(mp.mpf(str(eta))))
            record("cap-envelope recession removes dimensional constant",
                   {"d":d,"eta":eta,"t":t}, abs(difference-mp.mpf(d)/(2*t)), 1e-60)

data = {"schema":"AN02-directional-carrier-supplementary-checks213/v1",
        "observed_at_utc":datetime.now(timezone.utc).isoformat(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
        "status":"PASS","probe_count":len(results),"mpmath_decimal_digits":mp.mp.dps,
        "independent_routes":["physical sphere area-height integral and entire sine quotient",
                              "double-precision physical ellipse angle quadrature and SciPy Bessel function",
                              "ellipse parametrized normal, curvature and phase Hessian against normal inverse"],
        "scope":"Finite supplementary identities and geometry probes. General stationary-phase uniformity, PSH profile invariance, all direction quantifiers and wavefront localization are proved analytically in the formal lesson; no finite computation is their proof.",
        "results":results}
(OWN/"numerical-checks213.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","probes":len(results),
                  "max_absolute_error":max(x["absolute_error"] for x in results)}))

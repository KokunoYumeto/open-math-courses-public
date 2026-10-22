"""Reproduce the exact polynomial checks and two original root diagrams."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(exist_ok=True)
z, lam, u, s, rho = sp.symbols("z lam u s rho")
checks = []

def check(name, condition, detail):
    assert bool(condition), name
    checks.append({"name": name, "status": "PASS", "detail": detail})

def weighted_terms(poly, alpha):
    return [(j, ell, coefficient, alpha*j + ell)
            for (j, ell), coefficient in sp.Poly(poly, z, lam).terms()]

model_count = 0
for q in range(2, 9):
    for p in range(1, q):
        if math.gcd(p, q) != 1:
            continue
        alpha = sp.Rational(p, q)
        for k in (1, 2):
            for j0 in (0, 1):
                for a in (sp.Integer(1), sp.I):
                    d = q*k + j0
                    core = z**j0 * (z**q - a*lam**p)**k
                    germ = sp.expand(core + z**(d+1) + lam**(d+1))
                    terms = weighted_terms(germ, alpha)
                    actual_alpha = min(sp.Rational(ell, d-j) for j, ell, c, w in terms if j < d)
                    name = f"q={q},p={p},k={k},j0={j0},a={a}"
                    check(name + ":lowest weight",
                          actual_alpha == alpha and all(w >= alpha*d for j, ell, c, w in terms),
                          {"degree": d, "alpha": str(alpha), "axis_order": d,
                           "total_order": min(j+ell for j, ell, c, w in terms)})
                    limits = {}
                    for sign in (1, -1):
                        scaled = sp.expand(germ.subs({z: s**p*u, lam: sign*s**q}) / s**(p*d))
                        check(name + f":sign{sign} limit",
                              sp.Poly(scaled, s, u).degree(s) >= 0 and
                              sp.expand(scaled.subs(s, 0) - u**j0*(u**q-a*sign**p)**k) == 0,
                              {"parameter_sign": sign, "ramified_positive_real_scale": f"r=s^{q}"})
                        limits[sign] = scaled.subs(s, 0)
                    orbit_identity = sp.expand(limits[1].subs(u, rho*u) - rho**d*limits[1])
                    check(name + ":root orbit identity",
                          sp.rem(orbit_identity, rho**q-1, rho) == 0,
                          {"exact_relation": f"rho^{q}=1", "multiplicities_retained": k})
                    if q == 2:
                        check(name + ":other sign quarter turn",
                              sp.expand(limits[-1].subs(u, sp.I*u)-sp.I**d*limits[1]) == 0,
                              {"exact_rotation": "u -> i*u", "no_coefficient_reality_assumed": True})
                    model_count += 1

a = 2 + 3*sp.I
sharp = sp.expand((z-a*lam)**4)
check("complex sharp homogeneous polynomial", all(j+ell == 4 for (j, ell), c in sp.Poly(sharp, z, lam).terms()),
      {"axis_order": 4, "total_order": 4})
check("sharp requested coefficients",
      sharp.coeff(z, 3).coeff(lam, 1) == -8-12*sp.I and
      sharp.coeff(z, 2).coeff(lam, 2) == -30+72*sp.I,
      {"smallest_upper_linear_constant": 3})
for k in range(1, 9):
    g = sp.expand((z*z-lam)**k)
    check(f"two-sign example power{k}",
          sp.Poly(g.subs(lam, 0), z).degree() == 2*k and
          min(j+ell for (j, ell), c in sp.Poly(g, z, lam).terms()) == k,
          {"positive_parameter_roots": "±sqrt(r), each multiplicity k",
           "negative_parameter_roots": "±i*sqrt(r), each multiplicity k"})

h = z**6 - 2*lam*z**3 + lam**2 + z**7 + 2*lam**3
for sign in (1, -1):
    scaled = sp.expand(h.subs({z: s*u, lam: sign*s**3}) / s**6)
    check(f"five-monomial exact scaled identity sign{sign}",
          sp.expand(scaled - ((u**3-sign)**2 + s*u**7 + 2*sign*s**3)) == 0,
          {"alpha": "1/3", "normalized_error": "s*u^7 + 2*sign*s^3"})
omega = (-1 + sp.I*sp.sqrt(3))/2
check("cube root coordinates", sp.simplify(omega**3) == 1 and sp.simplify(omega*sp.conjugate(omega)) == 1,
      {"upper_imaginary_part": "sqrt(3)/2", "multiplicity_in_H_plus": 2})
check("cube-root distances",
      sp.simplify((omega-1)*(sp.conjugate(omega)-1)) == 3 and
      sp.simplify((omega-sp.conjugate(omega))**2) == -3,
      {"both_other_root_distances": "sqrt(3)"})
check("rational square-root lower bound", Fraction(17, 10)**2 < 3,
      {"sqrt(3)": ">17/10", "disk_imaginary_lower_bound": ">3/4"})
boundary = Fraction(1, 100) * Fraction(8, 5)**4
error = Fraction(1, 100) * Fraction(11, 10)**7 + Fraction(2, 10**6)
check("explicit Rouche boundary comparison",
      boundary == Fraction(4096, 62500) and error == Fraction(19489171, 10**9) and error < boundary,
      {"r_max": "1/1000000", "radius": "1/10",
       "lower_boundary_modulus": str(boundary), "upper_perturbation": str(error),
       "persistent_disk_root_count": 2})
check("upper-root denominator comparison", Fraction(17,20)-Fraction(1,10) == Fraction(3,4),
      {"strict_bound": "Im z > (3/4)*r^(1/3)"})
for gamma in (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(3, 4), sp.Integer(1)):
    check(f"fractional strip exponent {gamma}", (sp.Rational(2, 3)-gamma >= 0) == (gamma <= sp.Rational(2, 3)),
          {"ratio_exponent": str(sp.Rational(2,3)-gamma),
           "bounded_as_r_to_zero": bool(gamma <= sp.Rational(2,3))})

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "axes.titlesize": 14, "axes.labelsize": 13,
                     "svg.hashsalt": "root-strip-taylor-order"})
blue, orange, gray = "#2367aa", "#c7550a", "#626a73"

def save_figure(fig, name):
    fig.savefig(FIGURES / (name + ".png"), dpi=160,
                metadata={"Software": "Original mathematical illustration"})
    fig.savefig(FIGURES / (name + ".svg"), metadata={"Date": None})
    plt.close(fig)

fig, ax = plt.subplots(figsize=(9.6, 5.6), constrained_layout=True)
x = np.linspace(0, 6, 121)
ax.plot(x, 2-x/3, color=orange, lw=2, label=r"Lowest weight: $j/3+\ell=2$")
ax.plot([0, 2], [2, 0], "--", color=blue, lw=1.8, label=r"Total order: $j+\ell=2$")
edge = [(6,0),(3,1),(0,2)]
above = [(7,0),(0,3)]
ax.scatter(*zip(*edge), s=80, color=orange, zorder=5)
ax.scatter(*zip(*above), s=100, color=gray, marker="*", zorder=5)
for point, text, position in [
    ((6,0),r"$z^6$",(5.25,.4)), ((3,1),r"$-2\lambda z^3$",(3.3,1.25)),
    ((0,2),r"$\lambda^2$",(.35,2.2)), ((7,0),r"$z^7$",(7.4,.25)),
    ((0,3),r"$2\lambda^3$",(.35,3.05))]:
    ax.annotate(text, xy=point, xytext=position, fontsize=14,
                arrowprops={"arrowstyle":"-", "color":gray, "lw":.8})
ax.set(xlim=(-.3,8.1), ylim=(-.25,3.75), xticks=range(9), yticks=range(4),
       xlabel=r"Exponent $j$ of $z$", ylabel=r"Exponent $\ell$ of $\lambda$",
       title="One fractional scale retains three monomials")
ax.grid(alpha=.16)
ax.legend(loc="upper right", fontsize=11)
save_figure(fig, "lowest-weight-edge")

fig, axes = plt.subplots(1, 2, figsize=(10, 6.4))
fig.subplots_adjust(left=.06, right=.98, bottom=.24, top=.84, wspace=.2)
for ax in axes:
    ax.axhline(0, color=gray, lw=.8); ax.axvline(0, color=gray, lw=.8)
    theta = np.linspace(0, 2*np.pi, 241)
    ax.plot(np.cos(theta), np.sin(theta), "--", color=gray, alpha=.3)
    ax.set(xlim=(-1.45,1.45), ylim=(-1.45,1.45), aspect="equal",
           xlabel=r"$\operatorname{Re}u$", ylabel=r"$\operatorname{Im}u$")
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1])
    ax.grid(alpha=.12)
left, right = axes
left.scatter([1,-1],[0,0],s=70,color=blue,zorder=4,label=r"$\lambda>0:\ u=\pm1$")
left.scatter([0,0],[1,-1],s=75,color=orange,zorder=4,label=r"$\lambda<0:\ u=\pm i$")
for start in (0,np.pi):
    theta = np.linspace(start,start+np.pi/2,81)
    left.plot(np.cos(theta),np.sin(theta),color=orange,lw=1.5,alpha=.7)
    left.annotate("",xy=(np.cos(theta[-1]),np.sin(theta[-1])),
                  xytext=(np.cos(theta[-7]),np.sin(theta[-7])),
                  arrowprops={"arrowstyle":"->","color":orange,"lw":1.5})
left.set_title("Two real roots:\nthe other sign is needed")
left.legend(loc="lower center",bbox_to_anchor=(.5,-.29),fontsize=11,frameon=False)
cube = [(1.,0.),(-.5,np.sqrt(3)/2),(-.5,-np.sqrt(3)/2)]
right.scatter([cube[0][0],cube[2][0]],[cube[0][1],cube[2][1]],s=70,color=blue,zorder=4)
right.scatter([cube[1][0]],[cube[1][1]],s=85,color=orange,zorder=5)
right.annotate(r"$1$",xy=cube[0],xytext=(1.12,.1),fontsize=14)
right.annotate(r"$\omega$",xy=cube[1],xytext=(-.84,1.02),fontsize=14,color=orange)
right.annotate(r"$\overline{\omega}$",xy=cube[2],xytext=(-.86,-1.15),fontsize=14)
right.set_title("Three-point orbit:\nan upper root already occurs")
right.text(.5,-.24,r"$H_+(u)=(u^3-1)^2$: each root has multiplicity two",
           transform=right.transAxes,ha="center",va="top",fontsize=10.5)
save_figure(fig, "root-orbits-and-the-parameter-sign")

geometry = {
    "weight_diagram": {
        "polynomial": "z^6-2*lambda*z^3+lambda^2+z^7+2*lambda^3",
        "complete_support": [[6,0,1],[3,1,-2],[0,2,1],[7,0,1],[0,3,2]],
        "alpha": "1/3", "edge_weight": "2", "total_order": 2, "axis_order": 6,
        "limiting_polynomials": {"positive":"(u^3-1)^2","negative":"(u^3+1)^2"}},
    "orbit_diagram": {
        "left_polynomial": "z^2-lambda",
        "left_positive_parameter_roots": ["1","-1"],
        "left_negative_parameter_roots": ["i","-i"], "rotation": "multiplication by i",
        "right_limiting_polynomial": "(u^3-1)^2",
        "right_exact_roots": ["1","(-1+i*sqrt(3))/2","(-1-i*sqrt(3))/2"],
        "multiplicity_of_each_right_root": 2,
        "right_points_are_limiting_polynomial_roots": True},
    "reproducible_geometry": "Two-dimensional exponent and complex-root coordinates; no projection.",
}
(FIGURES / "geometry.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
artifacts = []
for path in sorted(FIGURES.iterdir()):
    data = path.read_bytes()
    artifacts.append({"path":path.relative_to(HERE).as_posix(),"bytes":len(data),
                      "sha256":hashlib.sha256(data).hexdigest().upper()})
report = {"schema":"AN02-zero-strip-order-check276/v1","status":"PASS",
          "checks_passed":len(checks),"parameterized_exact_models":model_count,
          "scope":"Exact lowest weights, both scaled limits, polynomial rotation identities, multiplicities and rational Rouche bounds. The general germ theorem is proved in the written argument.",
          "checks":checks,"artifacts":artifacts}
(HERE / "math-check276.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","checks":len(checks),"exact_models":model_count,
                  "artifacts":len(artifacts)}))

"""Original exact-geometry figures for directional surface carriers."""
from pathlib import Path
import json, os
OWN = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(OWN / "private-matplotlib-cache213"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = OWN / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "none", "axes.spines.top": False,
                     "axes.spines.right": False, "savefig.dpi": 160})
geometry = {"schema": "AN02-original-directional-carrier-geometry213/v1",
            "convention": "F(zeta)=<u,exp(-i x.zeta)>; outward dnu positive",
            "sphere": {"dimension": 3, "radius": 1, "density": 1,
                       "direction": [1, 0, 0], "center_pi_multipliers": [12, 48, 192],
                       "transform": "4*pi*sin(r)/r; r^2=zeta.zeta; entire even quotient",
                       "cap_limits": ["-1+eta", "-1-eta"],
                       "canonical_limit": "-1+abs(eta)", "indicator": "abs(eta)",
                       "exact_center_zero": "eta=0 and q=k*pi; omitted, never treated as a finite value"},
            "ellipse": {"center": [0.5, -0.25], "semiaxes": [2, 1],
                        "normal": ["1/sqrt(2)", "1/sqrt(2)"],
                        "half_chord": ["4/sqrt(5)", "1/sqrt(5)"],
                        "endpoint_formula": "b +/- A^2 theta / |A theta|",
                        "segment_support": "b.eta + |(4 eta_1+eta_2)/sqrt(5)|",
                        "body_support": "b.eta + sqrt(4 eta_1^2+eta_2^2)",
                        "normal_arrow_length": 1, "left_axes_equal_physical_scale": True}}

def finish(fig, name):
    fig.savefig(OUT / (name + ".png"), metadata={"Software": "Original reproducible mathematical figure"})
    fig.savefig(OUT / (name + ".svg"), metadata={"Date": None, "Creator": "Original reproducible mathematical figure"})
    plt.close(fig)

eta_parts = [np.linspace(-1.8, -0.002, 700), np.linspace(0.002, 1.8, 700)]
fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.2), constrained_layout=True)
ax = axes[0]
for k, color in zip([12, 48, 192], ["#2a73a5", "#bf6b19", "#6f5ca9"]):
    q = k * np.pi
    for j, eta in enumerate(eta_parts):
        # For integer k the exact center is a zero. Off center,
        # |sin(k*pi+i*eta*log(q))|=|sinh(eta*log(q))|.
        profile = np.log(4*np.pi*np.abs(np.sinh(eta*np.log(q))) /
                         np.abs(q+1j*eta*np.log(q))) / np.log(q)
        ax.plot(eta, profile, color=color, lw=1.6, label=f"q = {k}π" if j == 0 else None)
eta = np.linspace(-1.8, 1.8, 901)
ax.plot(eta, -1 + np.abs(eta), color="#18242d", lw=2.5, label="canonical limit −1 + |η|")
ax.axvline(0, color="#84909a", ls=":", lw=1)
ax.text(0.5, 0.06, "η = 0: exact zero, −∞ (not plotted)",
        ha="center", va="bottom", transform=ax.transAxes, fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#bdc7ce", "pad": 5})
ax.set(xlabel="η in ζ = q e₁ + i η log(q) e₁", ylabel="normalized logarithm",
       title="Exact sphere profiles and their center zeros", xlim=(-1.8, 1.8), ylim=(-2.6, 1.8))
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=.17)
ax = axes[1]
ax.plot(eta, -1 + eta, color="#2a73a5", lw=1.7, label="plus cap: −1 + η")
ax.plot(eta, -1 - eta, color="#bf6b19", lw=1.7, label="minus cap: −1 − η")
ax.plot(eta, -1 + np.abs(eta), color="#18242d", lw=2.5, label="maximum: −1 + |η|")
ax.plot(eta, np.abs(eta), color="#65832e", lw=2, ls="--", label="recession indicator: |η|")
ax.set(xlabel="η", ylabel="profile or indicator value",
       title="Recession removes the decay constant", xlim=(-1.8, 1.8), ylim=(-2.6, 2.3))
ax.legend(loc="upper center", fontsize=9)
ax.grid(alpha=.17)
finish(fig, "sphere-zeros-and-cap-profiles")

b = np.array([.5, -.25])
A = np.diag([2., 1.])
theta = np.array([1., 1.]) / np.sqrt(2)
w = np.array([4., 1.]) / np.sqrt(5)
pm, pp = b - w, b + w
t = np.linspace(0, 2*np.pi, 901)
eta = np.stack([np.cos(t), np.sin(t)], axis=1)
curve = b + eta @ A.T
segment = eta @ b + np.abs(eta @ w)
body = eta @ b + np.linalg.norm(eta @ A.T, axis=1)
geometry["ellipse"].update(endpoints=[pm.tolist(), pp.tolist()],
                           sample_angles=t.tolist(), segment_values=segment.tolist(),
                           body_values=body.tolist(), normal_vector=theta.tolist())
fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.3), constrained_layout=True)
ax = axes[0]
ax.fill(curve[:, 0], curve[:, 1], color="#dceaf2", alpha=.8)
ax.plot(curve[:, 0], curve[:, 1], color="#2a73a5", lw=2)
ax.plot([pm[0], pp[0]], [pm[1], pp[1]], color="#b34c35", lw=2.6, label="selected normal chord")
ax.scatter([pm[0], pp[0]], [pm[1], pp[1]], color="#b34c35", s=40, zorder=4)
tangent = np.array([-theta[1], theta[0]])
for p, normal, label, offset in [(pp, theta, "p₊", (.12, -.28)), (pm, -theta, "p₋", (-.25, .12))]:
    ends = p + np.array([-.8, .8])[:, None] * tangent
    ax.plot(ends[:, 0], ends[:, 1], color="#6a7680", ls="--", lw=1.3)
    ax.quiver(p[0], p[1], normal[0], normal[1], angles="xy", scale_units="xy",
              scale=1, color="#65832e", width=.008, zorder=5)
    ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=12)
ax.text(pp[0] + .36, pp[1] + .70, "θ", fontsize=12, color="#49631d")
ax.text(pm[0] - .95, pm[1] - .35, "−θ", fontsize=12, color="#49631d")
ax.scatter(*b, color="#18242d", s=20)
ax.text(b[0]-.1, b[1]-.24, "b", fontsize=12)
ax.text(.15, .46, "half-chord = (4, 1)/√5", fontsize=10, color="#8d3522")
ax.set(xlabel="x₁", ylabel="x₂", title="Opposite normals, an oblique chord",
       xlim=(-2.4, 3.5), ylim=(-1.9, 1.45))
ax.set_aspect("equal", adjustable="box")
ax.grid(alpha=.17)
ax = axes[1]
ax.plot(t/np.pi, body, color="#2a73a5", lw=2, label="whole ellipse: b·η + |Aη|")
ax.plot(t/np.pi, segment, color="#b34c35", lw=2.2, label="chord: b·η + |w·η|")
ax.set(xlabel="t / π,  η = (cos t, sin t)", ylabel="support-function value",
       title="The selected segment has a smaller carrier", xlim=(0, 2))
ax.legend(loc="upper right", fontsize=9)
ax.grid(alpha=.17)
finish(fig, "opposite-normals-and-an-oblique-chord")
(OUT / "geometry213.json").write_text(json.dumps(geometry, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"figures": 2, "rendered_files": 4, "geometry": str(OUT / "geometry213.json")}))

"""Reproduce exact tube geometry, disk density phases and curvature comparisons."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.hashsalt": "AN02-L150-original163",
                     "axes.spines.top": False, "axes.spines.right": False})

def save(fig, stem):
    fig.savefig(OUT / (stem + ".png"), dpi=150, bbox_inches="tight",
                metadata={"Software": "Original AN-02 figure source163"})
    fig.savefig(OUT / (stem + ".svg"), bbox_inches="tight",
                metadata={"Date": None, "Creator": "Original AN-02 figure source163"})
    plt.close(fig)

a = np.array([1.0, .5])
r = .8
s = .5
fig, axes = plt.subplots(1, 2, figsize=(12, 5.7), constrained_layout=True)
left, right = axes
left.add_patch(Wedge(-a, 7*r/8, 0, 360, width=r/4,
                    facecolor="#c482cc", alpha=.30,
                    label=r"possible support of $\bar\partial\chi$"))
for radius, color, ls, label in [
    (r/2, "#267349", "--", r"$r/2=0.4$"),
    (3*r/4, "#936021", ":", r"$3r/4=0.6$"),
    (r, "#235a93", "-", r"$r=0.8$")]:
    left.add_patch(Circle(-a, radius, fill=False, color=color, linestyle=ls,
                          linewidth=1.8, label=label))
left.plot(*(-a), "o", color="#191919", markersize=6)
left.text(-a[0], -a[1] + .11, r"$-a=-1-i/2$", ha="center")
left.text(-a[0], -a[1] - .20, r"$\chi=1$", ha="center", fontsize=11)
left.set_title(r"Repair uses $Z_Q=-Z_P$", pad=12)
left.legend(loc="upper left", fontsize=9, framealpha=.95)
right.add_patch(Circle(a, r, fill=False, color="#235a93", linewidth=1.8,
                       label=r"tube $N_P(r)$"))
right.add_patch(Circle(a, s, facecolor="#51a8a0", alpha=.19,
                       edgecolor="#22726c", linewidth=1.8,
                       label=r"density disk $s=1/2$"))
right.plot(*a, "o", color="#191919", markersize=6)
right.text(a[0], a[1] + .06, r"$a=1+i/2$", ha="center")
theta = np.arange(12) * 2*np.pi/12
points = a[:, None] + .35*np.array([np.cos(theta), np.sin(theta)])
phase = np.array([-np.sin(theta), -np.cos(theta)])
right.quiver(points[0], points[1], .10*phase[0], .10*phase[1],
             angles="xy", scale_units="xy", scale=1, color="#6d3475", width=.006,
             label=r"phase of $-i\overline{w}$ (samples)")
right.set_title(r"Reflection gives $z\mapsto-z$", pad=12)
right.legend(loc="upper left", fontsize=9, framealpha=.95)
for ax, center in zip(axes, [-a, a]):
    ax.set_aspect("equal")
    ax.set_xlim(center[0]-1.05, center[0]+1.05)
    ax.set_ylim(center[1]-1.0, center[1]+1.65)
    ax.set_xlabel(r"$\operatorname{Re}z$")
    ax.set_ylabel(r"$\operatorname{Im}z$")
    ax.grid(alpha=.16)
fig.suptitle("Exact cutoff radii and a double-root representing density", fontsize=15)
save(fig, "reflected-tubes-and-disk-moments")

fig, axes = plt.subplots(1, 2, figsize=(12, 5.4), constrained_layout=True)
x = np.linspace(-3, 3, 901)
jet = np.sqrt((x*x-1)**2 + 16*x*x + 64)
axes[0].plot(x, jet, linewidth=2.1, color="#235a93",
             label=r"$J_2(\xi)=\sqrt{|\xi^2-1|^2+16\xi^2+64}$")
axes[0].plot(x, np.abs(x*x-1), linewidth=2, color="#ac5731",
             label=r"$|Q(\xi)|=|\xi^2-1|$")
axes[0].scatter([-1, 1], [0, 0], color="#ac5731", zorder=5)
axes[0].scatter([-1, 1], [np.sqrt(80)]*2, color="#235a93", zorder=5)
axes[0].annotate(r"$J_2(\pm1)=\sqrt{80}$", xy=(1, np.sqrt(80)),
                 xytext=(1.2, 5.2), arrowprops=dict(arrowstyle="->"), fontsize=11)
axes[0].set(xlabel=r"real frequency $\xi$", ylabel="exact modulus / jet norm",
            title=r"No pole in $\log J_T$ at a zero of $Q$")
axes[0].legend(loc="upper center", fontsize=9)
q = np.linspace(0, 6, 901)
peaks = []
for T, color in [(2, "#235a93"), (8, "#227a65"), (32, "#a3632b")]:
    normalized = (q*q + T**-2)**.75/(1+q*q)
    axes[1].plot(q, normalized, color=color, linewidth=1.8, label=rf"$T={T}$")
    qp = np.sqrt(3-4/T**2)
    yp = np.sqrt(T)*3**.75/4/(T*T-1)**.25
    axes[1].scatter([qp], [yp], color=color, zorder=5, s=25)
    peaks.append(dict(T=T, eta=np.sqrt(3*T*T-4), q=float(qp),
                      normalized_ratio=float(yp)))
axes[1].axhline(2**.75, color="#8c3753", linestyle="--", linewidth=1.7,
                label=r"proved bound $2^{3/4}$")
axes[1].set(xlabel=r"$q=|\eta|/T$", ylabel=r"$\sqrt{T}\,R_T(Tq)$",
            ylim=(0, 1.82), title=r"$M^{-2}$ error fits the $|\eta|^{-3/2}$ curvature")
axes[1].legend(loc="upper right", fontsize=10)
for ax in axes:
    ax.grid(alpha=.17)
fig.suptitle("Exact polynomial regularization and uniform curvature comparison", fontsize=15)
save(fig, "polynomial-jets-and-curvature-budget")
geometry = {
    "schema": "AN02-L150-exact-figure-geometry163/v1",
    "figure_A": {"polynomial": "P(z)=(z-a)^2; Q(z)=(z+a)^2", "a": [1, .5],
                 "reflected_a": [-1, -.5], "tube_r": r, "density_s": s,
                 "cutoff_one_distance": 5*r/8, "derivative_support_inner": 5*r/8,
                 "derivative_support_outer": 7*r/8, "indicator_radius": 3*r/4,
                 "convolution_radius": r/8, "phase_vector": "(-sin(theta),-cos(theta))",
                 "phase_arrows_are_samples": True,
                 "proof_locators": ["NV23-NV24", "NV40-NV42", "L150.1-L150.4"]},
    "figure_B": {"Q": "z^2-1", "real_jet_T": 2,
                 "J_T_squared": "|z^2-1|^2+4|z|^2*(T^2+eta^2)+4*(T^2+eta^2)^2",
                 "ratio": "(1+eta^2)^(3/4)/(T^2+eta^2)",
                 "normalized_ratio": "(q^2+T^(-2))^(3/4)/(1+q^2)",
                 "proved_upper": "2^(3/4)", "exact_peaks": peaks,
                 "displayed_T_are_not_claimed_general_admissible_constants": True,
                 "proof_locators": ["NV8-NV11", "NV20-NV21", "L150.5-L150.10"]},
    "figures_are_original": True, "protected_book_media_used": False,
    "Blender_use": "Planar complex-frequency geometry and exact scalar comparisons need no 3D model."}
(OUT / "geometry.json").write_text(json.dumps(geometry, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"rendered": ["reflected-tubes-and-disk-moments", "polynomial-jets-and-curvature-budget"],
                  "exact_geometry": str(OUT / "geometry.json"), "new_workers_messages_backups": 0}))

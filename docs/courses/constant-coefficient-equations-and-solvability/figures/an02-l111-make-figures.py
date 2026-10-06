"""Original reproducible contour and exponent figure for CH15, CH25--CH31.

Human mathematical source: Lars Hormander, The Analysis of Linear Partial
Differential Operators I, Theorem 8.6.7, printed pp. 310--311.
The coordinates below illustrate the exact contour equations; numerical
values are schematic and are not universal constants of the theorem.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

OUT = Path(__file__).resolve().parent
R, c, T = 1.4, 2.6, 6.0
alpha, beta, theta0 = 0.5, 0.75, 1.8
phi = np.arccos(c / T)
psi = np.pi - np.arcsin(R / T)
assert np.pi / 2 < theta0 < min(np.pi, np.pi / (2 * beta))
assert phi < theta0 < psi
assert R < c < T

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.titlesize": 15, "axes.labelsize": 12,
    "svg.fonttype": "none",
})
fig = plt.figure(figsize=(14.7, 7.6), facecolor="white")
gs = fig.add_gridspec(1, 2, width_ratios=[1.22, 1],
                     left=.045, right=.975, bottom=.22, top=.88, wspace=.24)
ax = fig.add_subplot(gs[0, 0])
ay = fig.add_subplot(gs[0, 1])
blue, red, teal, purple = "#1864ab", "#c92a2a", "#087f8c", "#7b2cbf"
gray = "#ecedf0"

ax.add_patch(Rectangle((-6.65, -R), 6.65, 2*R,
                       facecolor=gray, edgecolor="none", zorder=0))
ax.add_patch(Circle((0, 0), R, facecolor=gray, edgecolor="#868e96",
                    linewidth=1.1, zorder=1))
ax.axhline(0, color="#a0a5ab", lw=.8, zorder=0)
ax.axvline(0, color="#a0a5ab", lw=.8, zorder=0)
ax.plot([-6.65, 0], [0, 0], "--", color="#495057", lw=1.4, zorder=2)
ax.text(-5.9, .22, "negative-real cut", fontsize=11, color="#495057")
ax.text(-.68, -.30, r"$|w|\leq R$", fontsize=11, color="#495057")

ax.plot([c, c], [-6.35, 6.35], color=blue, lw=2.6, zorder=4)
ax.annotate("", (c, 4.3), (c, 3.45),
            arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2.6})
ax.text(c+.20, 1.95, r"$\mathrm{Re}\,w=c$", color=blue, fontsize=12)

left = -np.sqrt(T*T-R*R)
ax.plot([-6.65, 0], [-R, -R], color=red, lw=2.6, zorder=4)
ax.plot([-6.65, 0], [R, R], color=red, lw=2.6, zorder=4)
angles = np.linspace(-np.pi/2, np.pi/2, 180)
ax.plot(R*np.cos(angles), R*np.sin(angles), color=red, lw=2.6, zorder=4)
ax.annotate("", (-3.0, -R), (-4.1, -R),
            arrowprops={"arrowstyle": "-|>", "color": red, "lw": 2.6})
ax.annotate("", (-4.1, R), (-3.0, R),
            arrowprops={"arrowstyle": "-|>", "color": red, "lw": 2.6})
ax.annotate("", (R*np.cos(.45), R*np.sin(.45)),
            (R*np.cos(-.12), R*np.sin(-.12)),
            arrowprops={"arrowstyle": "-|>", "color": red, "lw": 2.1})
ax.text(-4.9, -R-.48, r"$w=-t-iR,\quad t:\infty\to0$",
        color=red, fontsize=11)
ax.text(-4.9, R+.26, r"$w=-t+iR,\quad t:0\to\infty$",
        color=red, fontsize=11)
ax.text(.08, -2.65, r"$\Gamma_R$: right semicircle",
        color=red, fontsize=11)
ax.annotate("", (.88, -.99), (.88, -2.31),
            arrowprops={"arrowstyle": "->", "color": red, "lw": 1})

for sign in [-1, 1]:
    th = np.linspace(phi, theta0, 120)
    ax.plot(T*np.cos(th), sign*T*np.sin(th), ":", color=teal, lw=2.5)
    th = np.linspace(theta0, psi, 150)
    ax.plot(T*np.cos(th), sign*T*np.sin(th), ":", color=purple, lw=2.5)
    ax.plot([0, T*np.cos(theta0)], [0, sign*T*np.sin(theta0)],
            "--", color="#adb5bd", lw=.9, zorder=0)
    ax.plot([c, left], [sign*np.sqrt(T*T-c*c), sign*R],
            linestyle="none", marker="o", ms=4.5, color="#495057", zorder=6)
ax.text(-1.15, 4.12, r"$\theta_0$", fontsize=12, color="#495057")
ax.text(-4.9, 4.6, r"$|w|=T$", fontsize=12, color="#495057")
ax.text(-.55, 6.30, "near vertical: " + r"$-k_0T^\beta/2$",
        color=teal, fontsize=11, ha="center")
ax.text(-4.55, -5.8, "far left: " + r"$-ab_0T/2$",
        color=purple, fontsize=11, ha="center")
ax.set_xlim(-6.7, 4.6)
ax.set_ylim(-6.6, 6.65)
ax.set_aspect("equal")
ax.set_xticks([-6, -3, 0, 3])
ax.set_yticks([-6, -3, 0, 3, 6])
ax.set_xlabel(r"$\mathrm{Re}\,w$")
ax.set_ylabel(r"$\mathrm{Im}\,w$")
ax.set_title("The exact contour deformation", pad=18)
ax.spines[["top", "right"]].set_visible(False)

tt = np.geomspace(1, 1000, 400)
ay.loglog(tt, tt**alpha, color="#d9480f", lw=2.6,
          label=r"root order: $T^{1/2}$")
ay.loglog(tt, tt**beta, color=teal, lw=2.6,
          label=r"vertical damping: $T^{3/4}$")
ay.loglog(tt, tt, color=purple, lw=2.6, label=r"left decay: $T$")
ay.set_xlabel(r"$T$ (illustrative scale)")
ay.set_ylabel("Power, with unit coefficient")
ay.set_title("Why both decay mechanisms work", pad=18)
ay.grid(True, which="major", color="#dee2e6", lw=.7)
ay.spines[["top", "right"]].set_visible(False)
ay.legend(loc="upper left", frameon=False, fontsize=11)
ay.text(.52, .22, r"$\alpha<\beta<1$" "\n" r"$T^\alpha\ll T^\beta\ll T$",
        transform=ay.transAxes, fontsize=15, ha="center",
        bbox={"boxstyle": "round,pad=.5", "facecolor": "white",
              "edgecolor": "#dee2e6"})

fig.suptitle("Exact characteristic-halfspace solutions: contours and decay",
             fontsize=18, y=.975)
fig.text(.045, .088,
         "Proof locators: CH15, CH25–CH31. Example dimensions: "
         "R=1.4, c=2.6, T=6, θ₀=1.8; illustrative exponents α=1/2, β=3/4.",
         fontsize=10.6)
fig.text(.045, .05,
         "Human source: Hörmander I, Theorem 8.6.7, printed pp. 310–311. "
         "Original receiving derivation and reproducible figure; schematic coefficients.",
         fontsize=10.6)
for ext in ["png", "svg"]:
    fig.savefig(OUT / f"characteristic-halfspace-contours.{ext}",
                dpi=180, metadata={"Title": "Characteristic halfspace contour proof"})
plt.close(fig)

geometry = {
    "R": R, "c": c, "T": T, "alpha": alpha, "beta": beta,
    "theta0": theta0, "phi_T": float(phi), "psi_T": float(psi),
    "vertical_endpoints": [[c, -float(np.sqrt(T*T-c*c))],
                           [c, float(np.sqrt(T*T-c*c))]],
    "left_ray_endpoints": [[float(left), -R], [float(left), R]],
    "k0": float(np.cos(beta*theta0)), "b0": float(-np.cos(theta0)),
    "equations": ["vertical Re w=c upward",
                  "lower ray w=-t-iR, t from infinity to 0",
                  "right semicircle w=R exp(i theta), -pi/2 to pi/2",
                  "upper ray w=-t+iR, t from 0 to infinity"],
    "interpretation": "Illustrative parameters; exact contour equations and proof locators.",
}
(OUT / "geometry.json").write_text(json.dumps(geometry, indent=2) + "\n",
                                  encoding="utf-8")
print(json.dumps({"generated": ["characteristic-halfspace-contours.png",
                              "characteristic-halfspace-contours.svg",
                              "geometry.json"]}))

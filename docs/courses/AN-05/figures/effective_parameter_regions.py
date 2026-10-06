"""Exact parameter-region schematic for convexification C15--C24."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

epsilon = 0.5  # illustrative; the actual admissible choice is C15
delta = 1 / epsilon
t_star = 1 / np.sqrt(1 + delta**2)
eta_star = delta / np.sqrt(1 + delta**2)
assert abs(t_star / eta_star - epsilon) < 1e-14
assert abs(eta_star**2 + t_star**2 - 1) < 1e-14

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, (left, right) = plt.subplots(1, 2, figsize=(12.8, 6.8))
fig.subplots_adjust(left=0.075, right=0.975, top=0.79, bottom=0.25,
                    wspace=0.27)

rho = np.linspace(0, 2, 501)
left.fill_between(rho, 0, epsilon*rho, color="#d9eaf4")
left.fill_between(rho, epsilon*rho, 2, color="#fce5c9")
left.plot(rho, epsilon*rho, color="#485764", lw=2)
left.set(xlim=(0, 2), ylim=(0, 2), xlabel=r"$\rho=|\xi|$", ylabel=r"$s$",
         title="Exact projection to the effective parameter plane")
left.text(1.12, 0.24, r"$0<s\leq\varepsilon\rho$"+"\nSmall ratio: C16--C18",
          ha="center", color="#165d87")
left.text(0.88, 1.48, r"$\rho\leq\delta s$"+"\nComplement: C19--C24",
          ha="center", color="#8a520e")
left.text(1.55, 0.98, r"$s=\varepsilon\rho$"+"\n"+r"$\delta=1/\varepsilon$",
          ha="center", color="#485764")
point = np.array([1.45, 1.35])
radius = np.sqrt(np.sum(point**2))
unit = point / radius
left.plot([0, point[0]], [0, point[1]], ls="--", color="#916f49", lw=1.4)
left.scatter(*point, s=35, color="#8a520e", zorder=5)
left.text(point[0]+0.04, point[1]+0.08, r"$(\rho,s)=r(|\eta|,t)$", fontsize=11)

angle = np.linspace(0, np.pi/2, 501)
threshold_angle = np.arctan(epsilon)
small_angle = angle[angle <= threshold_angle]
complement_angle = np.linspace(threshold_angle, np.pi/2, 501)
right.plot(np.cos(small_angle), np.sin(small_angle), color="#1673a1", lw=5)
right.plot(np.cos(complement_angle), np.sin(complement_angle), color="#be7829", lw=5)
right.plot([0, eta_star], [0, t_star], color="#485764", lw=1.6)
right.scatter([eta_star, 0], [t_star, 1], color="#485764", s=38, zorder=5)
right.scatter([1], [0], facecolor="white", edgecolor="#1673a1", s=44, zorder=6)
right.scatter(unit[0], unit[1], s=35, color="#8a520e", zorder=5)
right.axhline(t_star, color="#485764", ls=":", lw=1.3)
right.text(0.03, t_star+0.025, r"$t_*=1/\sqrt{1+\delta^2}$", fontsize=11)
right.text(0.16, 0.92, r"$t\geq t_*>0$", color="#8a520e")
right.text(0.84, 0.25, "Small ratio", ha="center", color="#165d87")
right.text(0.8, 0.05, r"$t=0$ excluded", ha="center", fontsize=10, color="#165d87")
right.text(0.07, 1.02, r"$\xi=0$ is included", fontsize=11)
right.set(xlim=(0, 1.1), ylim=(0, 1.1), xlabel=r"$|\eta|=|\xi|/r$",
          ylabel=r"$t=s/r$", title=r"Compact normalization: $|\eta|^2+t^2=1$")
right.set_aspect("equal", adjustable="box")
for ax in (left, right):
    ax.grid(alpha=0.15)

fig.suptitle("Reciprocal regions cover every positive effective parameter\n"
             r"Illustrative $\varepsilon=1/2$, $\delta=2$; actual choice in C15",
             fontsize=15, y=0.98)
fig.text(0.5, 0.14,
         r"Compact constraint penalty: $F_+ + A_+(|P_0|^2+|B_0|^2)\geq\gamma_+>0$ (C22)",
         ha="center", fontsize=12)
fig.text(0.5, 0.09,
         r"Actual coefficients: $r^2/s=s/t^2\geq s$ for $|P_0|^2$, and $\lambda$ for $|B_0|^2$ (C23)",
         ha="center", fontsize=12)
fig.text(0.5, 0.025,
         "Exact parameter projection and normalization; no sampled symbol-positivity assertion.\n"
         "Source: Hörmander IV, Proposition 28.3.3, printed pp. 240--241; receiving proof C15--C24.",
         ha="center", fontsize=10)
output = Path(__file__).with_name("effective-parameter-regions.png")
fig.savefig(output, dpi=180, bbox_inches="tight", metadata={
    "Title": "Reciprocal effective parameter regions for exponential convexification",
    "Description": "Exact schematic of receiving proof C15--C24",
    "Software": "Matplotlib",
})
plt.close(fig)
print(output.resolve())

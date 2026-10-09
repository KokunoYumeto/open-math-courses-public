"""Reproduce the exact support and norm-bound figure in NS-FLUID-05."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
fig, (a, b) = plt.subplots(1, 2, figsize=(13, 5.2), constrained_layout=True)
for center in (-3, 3):
    a.add_patch(Circle((center, 0), 1/4, facecolor="#cbdff8",
                      edgecolor="#2361a1", linewidth=2))
    a.annotate(f"centre ({center}, 0, 0)", (center, 0), (center, 0.7),
               ha="center", arrowprops={"arrowstyle": "->", "color": "#2361a1"})
a.axhline(0, color="#777777", linewidth=0.7)
a.axvline(0, color="#777777", linewidth=0.7)
a.set(xlim=(-4, 4), ylim=(-1.4, 1.4), xlabel=r"$\xi_1$",
      ylabel=r"$\xi_2$", title="Containing balls for the Fourier support\n"
      r"$N=3$, radius $1/4$; section $\xi_3=0$")
a.set_aspect("equal")
a.text(0, -1.05, r"$\widehat w_N=(2\pi i/N^2)(\xi\times e_3)"
       r"[\psi(\xi-Ne_1)+\psi(\xi+Ne_1)]$", ha="center", fontsize=10)

N = np.arange(1, 33, dtype=float)
nu, T = 1.0, 1.0
r_minus, r_plus = N-1/4, N+1/4
d = 4*np.pi**2*nu*r_minus**2
u_coefficient = 2*np.pi*np.sqrt(2)*r_plus/N**2
v_coefficient = 4*np.pi*r_plus/N**2
A = u_coefficient/np.sqrt(2*d)
B = np.sqrt(T)*(2*np.pi*r_plus*u_coefficient*v_coefficient)/(2*d)
lower = np.full_like(N, 9*np.pi*np.sqrt(2)/8)
b.loglog(N, lower, "-", color="#993c28", linewidth=2.3,
         label=r"initial $H^1_{\rm src}$ lower bound / $\|\psi\|_2$")
b.loglog(N, A, "o-", color="#2361a1", markersize=3,
         label=r"$A_N$: coefficient of $\|\psi\|_2$")
b.loglog(N, B, "s-", color="#257154", markersize=3,
         label=r"$B_N$: coefficient of $\|\psi\|_1\|\psi\|_2$")
b.set(xlabel="integer frequency N", ylabel="exact bound coefficient",
      title=r"Full linear input: $\|F_N\|_{L^2_tL^2_x}"
      r"\leq A_N\|\psi\|_2+B_N\|\psi\|_1\|\psi\|_2$"
      "\n" r"$\nu=1$, $T=1$; the source trace bound stays positive")
b.grid(which="both", alpha=.18)
b.legend(loc="lower left", fontsize=9)
fig.savefig(HERE/"strong-solution-stability.png", dpi=180)
fig.savefig(HERE/"strong-solution-stability.svg")
plt.close(fig)

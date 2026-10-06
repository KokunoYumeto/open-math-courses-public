"""Exact two-by-two modular orbit and the opposite time-reversal sign."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

d = Path(__file__).resolve().parent
omega = np.log(4.0)
period = 2*np.pi/omega
theta = np.linspace(0, 2*np.pi, 501)
quarter = np.arange(4)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 6.1))
fig.subplots_adjust(left=.08, right=.97, top=.83, bottom=.21, wspace=.28)
fig.suptitle("The opposite modular operator reverses time", fontsize=18, fontweight="bold")
for ax, sign, color, title in zip(
        axes, [-1, 1], ["#176d80", "#b65d1d"],
        [r"$[\sigma_t^\varphi(h)]_{12}=\frac{1}{5} e^{-it\log4}$",
         r"$[\sigma_t^\rho(R_h)]_{\rm right,12}=\frac{1}{5} e^{+it\log4}$"]):
    z = .2*np.exp(sign*1j*theta)
    ax.plot(z.real, z.imag, color=color, lw=2.5)
    for k in range(4):
        p = .2*np.exp(sign*1j*(np.pi/2*k+.38))
        q = .2*np.exp(sign*1j*(np.pi/2*k+.66))
        ax.annotate("", xy=(q.real,q.imag), xytext=(p.real,p.imag),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=17))
    pts = .2*np.exp(sign*1j*quarter*np.pi/2)
    ax.scatter(pts.real, pts.imag, color=color, s=43, zorder=4)
    for k,p in enumerate(pts):
        label = ["0", "T/4", "T/2", "3T/4"][k]
        ax.text(1.20*p.real, 1.20*p.imag, label,
                ha="center", va="center", fontsize=12, color=color)
    ax.set_title(title, fontsize=14, pad=14)
    ax.axhline(0, color="#9aa6ad", lw=.8)
    ax.axvline(0, color="#9aa6ad", lw=.8)
    ax.set_xlim(-.29,.29); ax.set_ylim(-.29,.29)
    ax.set_aspect("equal")
    ax.set_xticks([-.2,0,.2]); ax.set_yticks([-.2,0,.2])
    ax.set_xlabel("Real part"); ax.set_ylabel("Imaginary part")
    ax.grid(alpha=.15)
fig.text(.5,.11, r"$D=\mathrm{diag}(1,4),\quad h_{11}=h_{22}=1/2,\quad h_{12}=h_{21}=1/5,"
         r"\quad T=2\pi/\log4$", ha="center", fontsize=13)
fig.text(.5,.048, r"$JU_t=U_tJ,\qquad \Delta_\rho=\Delta_\varphi^{-1},\qquad"
         r"\sigma_t^\rho(j(a))=j(\sigma_{-t}^\varphi(a))$", ha="center", fontsize=14)
fig.savefig(d/"assets"/"modular-opposite-time.png", dpi=180, bbox_inches="tight")
fig.savefig(d/"assets"/"modular-opposite-time.svg", bbox_inches="tight")
plt.close(fig)
(d/"modular-opposite-figure-numerics.json").write_text(json.dumps({
    "omega":float(omega), "period":float(period), "radius":.2,
    "quarter_times":(quarter*period/4).tolist(),
    "left_offdiagonal":[[float(v.real),float(v.imag)] for v in .2*np.exp(-1j*quarter*np.pi/2)],
    "right_coefficient_offdiagonal":[[float(v.real),float(v.imag)] for v in .2*np.exp(1j*quarter*np.pi/2)],
    "phi_h":2.5, "rho_Rh":2.5,
    "scope":"All displayed trajectories are exact formulas; arrays give only quarter-period numeric samples."
}, indent=2)+"\n",encoding="utf-8")

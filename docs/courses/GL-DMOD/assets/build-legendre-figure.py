"""Exact Legendre/time/Legendre factorization and finite-box period calibration."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
out = parser.parse_args().output_dir
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.hashsalt": "GL-DMOD-LI-exact-Legendre-v1"})
ink, blue, green, muted = "#152640", "#155ca5", "#17765d", "#52627a"
fig = plt.figure(figsize=(16, 11), facecolor="#f5f8fc")
fig.text(.5, .97, "A quadratic contact shear factors through a Legendre incidence", ha="center", va="top", fontsize=25, color=ink)
fig.text(.5, .919, r"$d=1,\ C=1,\ \varphi(y)=-y^2/2,\ t=0$ for the plotted slices", ha="center", fontsize=19, color=muted)
axes = [fig.add_axes([.07+i*.315, .515, .265, .31]) for i in range(3)]
values = [F(-1, 2), F(-1, 4), F(0), F(1, 4), F(1, 2)]
rows = []
colors = plt.cm.viridis(np.linspace(.05, .95, len(values)**2))
for i, (x, z) in enumerate((x, z) for x in values for z in values):
    first = (x*z, z, -x)
    middle = (x*z+z*z/2, z, -x-z)
    final = (-z*z/2, x+z, z)
    assert middle[0]+middle[1]*middle[2] == final[0]
    assert -middle[2] == final[1] and middle[1] == final[2]
    for ax, pair in zip(axes, [(first[1], first[2]), (middle[1], middle[2]), (final[1], final[2])]):
        ax.scatter(float(pair[0]), float(pair[1]), color=colors[i], s=65, edgecolor="white", linewidth=.7, zorder=3)
    rows.append({"x": str(x), "z": str(z), "after_L": list(map(str, first)),
                 "after_time": list(map(str, middle)), "after_inverse_L": list(map(str, final))})
titles = [r"$\ell:\ (x,z)\mapsto(y,w)=(z,-x)$",
          r"$F_\varphi:\ (y,w)\mapsto(y,w-y)$",
          r"$\ell^{-1}:\ (y,w-y)\mapsto(x+z,z)$"]
labels = [("y", "w"), ("y", "w-y"), ("x+z", "z")]
for ax, title, lab in zip(axes, titles, labels):
    ax.set_title(title, fontsize=15, pad=14)
    ax.set_xlabel("$"+lab[0]+"$", fontsize=17)
    ax.set_ylabel("$"+lab[1]+"$", fontsize=17)
    ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
    ax.axhline(0, color=muted, lw=.6); ax.axvline(0, color=muted, lw=.6)
    ax.grid(alpha=.15); ax.set_aspect("equal", adjustable="box")
fig.text(.5, .445, r"Final time: $t'=t-z^2/2$. Colors identify the same exact rational sample through all three maps.", ha="center", fontsize=16, color=green)
fig.text(.5, .408, "The full all-dimensional factorization is LI.9-LI.18; no invertibility assumption on C is needed.", ha="center", fontsize=14, color=muted)

left = fig.add_axes([.065, .10, .49, .26]); left.axis("off")
left.text(0, 1, "The simple-pole normalization retains the ordered inverse term", fontsize=16, color=ink, va="top")
left.text(.02, .72, r"$K=(s-t-x\cdot y)^{-1},\qquad \alpha=0$", fontsize=21, color=blue)
left.text(.02, .45, r"$L_0^{-1}(t)=s+(E_y+d)\sigma^{-1}$", fontsize=22, color=green)
left.text(.02, .18, r"$L_0^2(t)=t-dD_t^{-1}$", fontsize=22, color=blue)
left.text(.02, -.07, "LI.3-LI.8 prove both identities in the localized polynomial algebra.", fontsize=12.5, color=muted)

ax = fig.add_axes([.67, .12, .275, .24])
eps, a = F(1, 3), F(2)
samples = []
for k in range(-20, 21):
    b = F(k, 20)
    exact = 2*eps/(a*a-eps*eps*b*b)
    samples.append({"b": str(b), "minus_I1": str(exact)})
ax.plot([float(F(x["b"])) for x in samples], [float(F(x["minus_I1"])) for x in samples], color=blue, lw=2.3)
ax.scatter([float(F(x["b"])) for x in samples[::5]], [float(F(x["minus_I1"])) for x in samples[::5]], color=green, s=26, zorder=3)
ax.set_xlabel("$b$"); ax.set_ylabel("$-I_1(2,b)$")
ax.set_title(r"Exact box period: $a=2,\ \epsilon=1/3$", fontsize=15)
ax.grid(alpha=.18)
fig.text(.8075, .055, r"$-I_1(a,b)=2\epsilon/(a^2-\epsilon^2b^2)$", ha="center", fontsize=16, color=green)
fig.text(.5, .014, "Kernel identities and compact periods do not establish the whole real-stalk inverse. That supported-cochain proof remains required (LI.6).", ha="center", fontsize=13, color=muted)
fig.savefig(out/"legendre-contact-factorization.png", dpi=150, facecolor=fig.get_facecolor())
fig.savefig(out/"legendre-contact-factorization.svg", metadata={"Date": None})
plt.close(fig)
fig = plt.figure(figsize=(16, 10), facecolor="#f5f8fc")
fig.text(.5, .96, "The open projective incidence has a complete topological inverse", ha="center", va="top", fontsize=25, color=ink)
fig.text(.5, .90, r"$K=\mathbb{C}_\Omega,\quad T=Rj_*\mathbb{C}_{\Omega^{op}}[2n],\quad K*T\simeq\mathbb{C}_\Delta$", ha="center", fontsize=23, color=blue)
ax = fig.add_axes([.06, .20, .36, .59])
grid = np.linspace(-2.3, 2.3, 501)
xx, yy = np.meshgrid(grid, grid)
rr = np.sqrt(xx*xx+yy*yy)
density = np.zeros_like(rr)
inside = (rr > 1) & (rr < 2)
r = rr[inside]
log_ratio = -1/(r-1)+1/(2-r)
chi = 1/(1+np.exp(np.clip(log_ratio, -700, 700)))
density[inside] = chi*(1-chi)*(1/(r-1)**2+1/(2-r)**2)/(2*np.pi*r)
im = ax.imshow(density, extent=[-2.3, 2.3, -2.3, 2.3], origin="lower", cmap="YlGnBu")
theta = np.linspace(0, 2*np.pi, 601)
for radius, style in [(.5, "-"), (1, "--"), (2, "--")]:
    ax.plot(radius*np.cos(theta), radius*np.sin(theta), color=green if radius == .5 else muted, ls=style, lw=1.8)
ax.annotate("", xy=(.5*np.cos(.9), .5*np.sin(.9)), xytext=(.5*np.cos(.35), .5*np.sin(.35)), arrowprops={"arrowstyle": "->", "color": green, "lw": 2})
ax.text(0, .06, r"$\eta=d\theta/(2\pi)$", ha="center", color=green, fontsize=15)
ax.set_xlabel(r"$\Re z$"); ax.set_ylabel(r"$\Im z$")
ax.set_title(r"Normal plane: $-d\chi\wedge\eta$ has integral 1", fontsize=17, pad=16)
fig.colorbar(im, ax=ax, fraction=.045, pad=.03, label="Two-form density relative to area")
fig.text(.23, .135, r"$\chi=1$ for $r\leq1$,  $\chi=0$ for $r\geq2$", ha="center", fontsize=16, color=green)
fig.text(.23, .095, r"$\int(-d\chi\wedge\eta)=-\int_0^\infty\chi'(r)\,dr=1$", ha="center", fontsize=16, color=blue)
ax = fig.add_axes([.51, .20, .45, .59]); ax.axis("off")
ax.text(0, .98, "Off the diagonal: distinct projective points", fontsize=19, color=ink, va="top")
ax.text(.03, .84, r"$A=\mathbb{C}^n,\qquad A\cap B=\mathbb{C}^n\setminus\mathbb{C}^{n-1}$", fontsize=21, color=blue)
ax.text(.03, .69, r"$R\Gamma_c(A;Rj_*\mathbb{C}_{A\cap B})[2n]$", fontsize=21, color=blue)
ax.text(.12, .54, r"$\mathbb{C}\ \overset{1}{\longrightarrow}\ \mathbb{C}\quad\Longrightarrow\quad0$", fontsize=26, color=green)
ax.text(.15, .445, "degree -1              degree 0", fontsize=15, color=muted)
ax.text(0, .30, "On the diagonal: the affine complement is unchanged", fontsize=18, color=ink)
ax.text(.03, .15, r"$R\Gamma_c(\mathbb{C}^n;\mathbb{C})[2n]\simeq\mathbb{C}$", fontsize=23, color=blue)
ax.text(.03, .01, "Complex orientation glues these groups along the diagonal.", fontsize=15, color=green)
fig.text(.5, .035, "LI.8 proves both entire topological convolution kernels. A compatible holomorphic microkernel and full real operator action remain to be constructed.", ha="center", fontsize=13, color=muted)
fig.savefig(out/"open-incidence-topological-inverse.png", dpi=150, facecolor=fig.get_facecolor())
fig.savefig(out/"open-incidence-topological-inverse.svg", metadata={"Date": None})
plt.close(fig)
data = {"scope": "Exact real phase-space projections at t=0 for d=1,C=1; all-dimensional statements are proved in LI.1-LI.3.",
        "samples": rows, "period_parameters": {"a": str(a), "epsilon": str(eps)},
        "period_samples": samples, "numerical_plot_coordinates_only": True,
        "topological_inverse": {"dimension": "arbitrary n >= 0", "cutoff": "chi(r)=b(2-r)/(b(2-r)+b(r-1)), b(s)=exp(-1/s) for s>0 and zero otherwise", "normal_2form": "-d chi wedge d theta/(2 pi)", "normal_integral": "1 by the exact fundamental theorem of calculus", "off_diagonal_after_shift": {"degrees": [-1, 0], "matrix": [[1]], "cohomology": "zero"}, "diagonal_after_shift": {"degree": 0, "cohomology": "C"}, "holomorphic_microkernel_inverse_proved": False},
        "whole_real_kernel_inverse_claimed": False}
(out/"legendre-contact-factorization-exact-data.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"outputs": 5, "phase_samples": len(rows), "exact_period_samples": len(samples)}))

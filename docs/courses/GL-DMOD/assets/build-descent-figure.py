"""Exact hyperplane descent, source degrees and a bounded parameter path."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

root = Path(__file__).resolve().parent
out = root if root.name == "assets" else root / "assets"
out.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "svg.hashsalt": "full-hyperplane-descent",
    "axes.spines.top": False, "axes.spines.right": False,
})
fig, axes = plt.subplots(2, 2, figsize=(14, 11), dpi=180)
fig.subplots_adjust(left=.075, right=.965, top=.90, bottom=.22,
                    wspace=.30, hspace=.55)
blue, purple, red = "#195d8a", "#715299", "#a43d40"
epsilon, r = Fraction(1, 4), Fraction(1, 32)
d = 3

ax = axes[0, 0]
ax.set_title("A  Every lower intersection, N = 4", loc="left", weight="bold")
ax.set_axis_off()
entries = [
    (r"$G^{(0)}$", "(Čech 0, anti 2)"),
    (r"$G^{(1)}$", "(Čech 1, anti 1)"),
    (r"$G^{(2)}$", "(Čech 2, anti 0)"),
]
for i, (label, degree) in enumerate(entries):
    x = .015 + .335 * i
    ax.add_patch(FancyBboxPatch((x, .51), .29, .30,
        boxstyle="round,pad=.012", facecolor="#edf4f8",
        edgecolor=blue, transform=ax.transAxes))
    ax.text(x+.145, .72, label, ha="center", transform=ax.transAxes,
            fontsize=18, color=blue)
    ax.text(x+.145, .58, degree, ha="center", transform=ax.transAxes,
            fontsize=10.5)
ax.text(.02, .31, r"$D_{\rm tot}G=T^{(3)}-\mathrm{aug}(\beta_4)$",
        transform=ax.transAxes, fontsize=16)
ax.text(.02, .12, r"$T^{(3)}=r_4\varphi,\quad G=\sum_{k=0}^{2}G^{(k)}$",
        transform=ax.transAxes, fontsize=15)
ax.text(.02, -.02, "Intermediate components cancel by HP.8; top determinant: HP.5–HP.6.",
        transform=ax.transAxes, fontsize=10)

ax = axes[0, 1]
ax.set_title("B  A generating segment crosses ξ₀ = 0", loc="left", weight="bold")
lam = np.linspace(0, 1, 401)
ax.plot(lam, 32*(1-2*lam), color=blue, lw=2.4, label=r"$a_0(\lambda)=32(1-2\lambda)$")
ax.axhline(0, color="#666666", lw=.8)
ax.axvline(.5, color=red, lw=1.2, ls="--")
ax.scatter([.5], [0], color=red, zorder=3)
ax.annotate(r"$a(1/2)=(0,-4)$", xy=(.5, 0), xytext=(.57, 16),
            arrowprops={"arrowstyle":"->", "color":red}, color=red)
ax.set_xlim(0, 1)
ax.set_ylim(-35, 35)
ax.set_xlabel(r"Affine parameter $\lambda$")
ax.set_ylabel(r"Zeroth coordinate $a_0$")
ax.legend(frameon=False, fontsize=11, loc="lower left")
ax.text(0, -.36, r"$\varepsilon=1/4,\ r=1/32,\ w=(1/32,-1/4)$; exact data: HP.11.",
        transform=ax.transAxes, fontsize=10)

ax = axes[1, 0]
ax.set_title("C  A curved path stays in the local y-chart", loc="left", weight="bold")
t = np.linspace(0, 1, 401)
y = float(epsilon)/2*(1-np.exp(1j*np.pi*t))
ax.add_patch(Circle((0, 0), float(epsilon), fill=False, ec="#9baaba", ls="--"))
ax.plot(y.real, y.imag, color=purple, lw=2.7)
ax.scatter([0, float(epsilon)], [0, 0], color=purple, zorder=3)
ax.scatter([float(epsilon)/2], [0], color=red, marker="x", s=70, zorder=4)
ax.annotate("Incidence point ε/2", xy=(.125, 0), xytext=(-.14, .10),
            arrowprops={"arrowstyle":"->", "color":red}, color=red, fontsize=10)
ax.annotate("", xy=(y[240].real, y[240].imag),
            xytext=(y[210].real, y[210].imag),
            arrowprops={"arrowstyle":"->", "color":purple, "lw":2})
ax.text(.04, -.30, r"$y(t)=\frac{\varepsilon}{2}(1-e^{i\pi t}),\quad |y(t)|\leq|\varepsilon|$",
        fontsize=13, transform=ax.transAxes)
ax.text(.04, -.47, r"$\langle(1,y(t)),w\rangle=r e^{i\pi t}\ne0$",
        fontsize=13, transform=ax.transAxes)
ax.axhline(0, color="#aab3ba", lw=.7)
ax.axvline(0, color="#aab3ba", lw=.7)
ax.set_aspect("equal")
ax.set_xlim(-.28, .30)
ax.set_ylim(-.19, .17)
ax.set_xlabel(r"$\operatorname{Re}y$")
ax.set_ylabel(r"$\operatorname{Im}y$")

ax = axes[1, 1]
ax.set_title("D  Source roofs and coefficient degrees", loc="left", weight="bold")
ax.set_axis_off()
texts = [
    (.83, r"$\mu\mathrm{hom}(L*L^{\rm op}[2N],F)$"
           "\n" r"$\simeq\mu\mathrm{hom}(\mathbf{C}_{\Delta},F)$",
     "Off zero; finite constant source cones vanish."),
    (.49, r"$\mathrm{Tr}:I[N]\longrightarrow I_{\rm target}$",
     "Complex middle dimension N; real orientation shift is 2N."),
    (.15, r"$\mu\mathrm{hom}(\mathbf{C}_{\Delta}[-N],F)"
           r"=\mu\mathrm{hom}(\mathbf{C}_{\Delta},F)[N]$",
     "Degree zero is the degree-N diagonal operator group."),
]
for yy, equation, caption in texts:
    ax.text(.02, yy, equation, fontsize=14 if yy>.2 else 12.5,
            transform=ax.transAxes, color=blue)
    ax.text(.02, yy-.13, caption, fontsize=10.5, transform=ax.transAxes)

fig.suptitle("Full hyperplane descent and the actual parameter domain",
             fontsize=21, weight="bold")
fig.text(.065, .025,
         "HP.5–HP.10 gives the complete descent; HP.11–HP.12 checks chart containment explicitly.  "
         "SN.5–SN.11 gives source roofs and finite witnesses.\n"
         "These statements do not identify either analytic incidence composition with the diagonal unit.",
         fontsize=10, color="#334a58")
stem = "hyperplane-descent-and-chart"
fig.savefig(out/(stem+".png"), dpi=180)
fig.savefig(out/(stem+".svg"), metadata={"Date":None})
plt.close(fig)
data = {
    "dimension_N_for_panel_A": 4,
    "cochain_bidegrees": [[0,2],[1,1],[2,0]],
    "source_roof_real_shift": "2N",
    "coefficient_trace_complex_shift": "N",
    "epsilon": str(epsilon), "r": str(r),
    "normal_w": ["1/32", "-1/4"],
    "affine_vertices": [["32","0"],["-32","-8"]],
    "affine_midpoint": ["0","-4"],
    "projective_path": "y(t)=epsilon*(1-exp(i*pi*t))/2",
    "exact_denominator": "r*exp(i*pi*t)",
    "path_bound": "abs(y(t))<=abs(epsilon)",
    "general_chart_containment_proved": False,
    "analytic_inverse_product_proved": False,
}
(out/(stem+"-exact-data.json")).write_text(
    json.dumps(data, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
target = out / Path(__file__).name
if Path(__file__).resolve() != target.resolve():
    target.write_bytes(Path(__file__).read_bytes())
print(json.dumps({"figure":stem,"pixels":[2520,1980],"output_files":4}))

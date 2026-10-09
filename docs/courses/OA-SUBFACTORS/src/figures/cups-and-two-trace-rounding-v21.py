"""Reproducible exact algebraic diagram for CTR.5--CTR.17. CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="cups-and-two-trace-rounding-v21"
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15.6, 9.0))
fig.patch.set_facecolor("#fbfcfe")
ax.set(xlim=(0, 15.6), ylim=(0, 9))
ax.axis("off")

def box(x, y, w, h, text, color="#e9f1fa", size=16):
    patch = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.08,rounding_size=0.10",
                          linewidth=1.6, edgecolor="#38546b", facecolor=color)
    ax.add_patch(patch)
    ax.text(x+w/2, y+h/2, text, ha="center", va="center",
            fontsize=size, linespacing=1.40, color="#163248")

def arrow(x1, y1, x2, y2):
    ax.annotate("", (x2, y2), (x1, y1),
                arrowprops=dict(arrowstyle="->", lw=2.0, color="#38546b"))

ax.text(7.8, 8.63, "Actual cups control the total two-trace rounding loss",
        ha="center", va="center", fontsize=24, weight="bold", color="#163248")
ax.text(7.8, 8.12,
        "Any proper finite-index II₁ inclusion · all three rows · exact prescribed prefix and cups",
        ha="center", fontsize=14.5, color="#486276")

box(0.45, 6.34, 4.28, 1.35,
    "Two adjacent actual cups\n"
    r"$efe=d^{-1}e,\quad fef=d^{-1}f$"+"\n"
    r"$\tau(e)=\rho(e)=1/d$", size=16)
box(5.45, 6.34, 4.27, 1.35,
    r"$C=M_2(P)\oplus\mathbb{C}(1-P)$"+"\n"
    r"$\tau(P)=\rho(P)=2/d$"+"\n"
    "Minimal weights: 1/d and 1 − 2/d", size=15.5)
box(10.45, 6.34, 4.27, 1.35,
    "Separated copies after m\n"
    r"$F_m^L\otimes C^{\otimes h}\subset F_{m+3h}^L$"+"\n"
    "Both original finite traces are products", size=15)
arrow(4.8, 7.02, 5.35, 7.02)
arrow(9.8, 7.02, 10.35, 7.02)

ax.text(7.8, 5.83,
        r"Total minimal weights:  $\beta_{m+3h}^{L,\sigma}\leq"
        r"\beta_m^{L,\sigma}(1-1/d)^h$",
        ha="center", fontsize=20, weight="bold", color="#163248")
ax.text(7.8, 5.38, r"$L=M,N,N_k\ ;\quad \sigma=\tau,\rho$"
        "     ·     each weight belongs to its original trace system",
        ha="center", fontsize=14.5, color="#486276")

ax.text(7.8, 4.92, "Exact subalgebra example: d = 3, h = 2",
        ha="center", fontsize=18, weight="bold", color="#163248")
labels = [
    r"$M_4$"+"\nrank 4\nminimal weight 1/9\nunit mass 4/9",
    r"$M_2$"+"\nrank 2\nminimal weight 1/9\nunit mass 2/9",
    r"$M_2$"+"\nrank 2\nminimal weight 1/9\nunit mass 2/9",
    r"$\mathbb{C}$"+"\nrank 1\nminimal weight 1/9\nunit mass 1/9",
]
for a, label in enumerate(labels):
    box(0.65+3.72*a, 3.17, 3.10, 1.42, label, "#edf6ed", 15)
ax.text(7.8, 2.77,
        "Unit masses sum to 1.  Minimal weights sum to 4/9 = (1 − 1/3)².",
        ha="center", fontsize=15.5, color="#315b38")

box(0.65, 0.95, 6.75, 1.31,
    "Integer loss in an actual feasible allocation\n"
    r"$\mathrm{extra\ loss}_\sigma\leq r\,\beta_m^\sigma(1-1/d)^h$"+"\n"
    "Exact canonical complement → genuine full physical residual",
    "#e9f1fa", 15)
box(8.08, 0.95, 6.75, 1.31,
    "The remaining unrestricted selection problem\n"
    r"$C_j^\tau=\sum_{i,b}\omega_{j,b}^\tau(h_{i,b}-a_{i,b})$"+"\n"
    "Small fractional physical cut loss is still unproved",
    "#fff1dc", 15)
ax.text(7.8, 0.39,
        "CTR.5–CTR.17.  Schematic box sizes; all ranks and traces are explicit.  "
        "No numerical grouping or zero-cost state is assumed.",
        ha="center", fontsize=12.5, color="#486276")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig(ROOT/"cups-and-two-trace-rounding-v21.svg",metadata={"Date":None})
fig.savefig(ROOT/"cups-and-two-trace-rounding-v21.png", dpi=160)
plt.close(fig)

svg_path=ROOT/"cups-and-two-trace-rounding-v21.svg"
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")

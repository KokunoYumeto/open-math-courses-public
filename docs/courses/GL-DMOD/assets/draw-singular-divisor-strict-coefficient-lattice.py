"""Reproducible exact coefficient-lattice diagram for GL-DMOD-13, §§5.27.3–5.27.11."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BASE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig = plt.figure(figsize=(17, 11.8), facecolor="#f7f9fc")
grid = fig.add_gridspec(3, 3, height_ratios=[1.25, 1.3, .60],
                       left=.045, right=.975, top=.86, bottom=.07,
                       hspace=.36, wspace=.16)
ink, blue, red = "#162d48", "#1261a0", "#aa402c"
fig.text(.045, .955, "An actual coherent strict lattice across a singular analytic divisor",
         fontsize=23, color=ink, weight="bold")
fig.text(.045, .915, "Theorem 5.27: finite analytic presentations, normalized divisorial lattices, and a sheaf double dual.",
         fontsize=13, color=ink)

ax = fig.add_subplot(grid[0, 0])
t = np.linspace(-1.15, 1.15, 900)
ax.plot(t*t, t*t*t, color=blue, lw=2.4, label=r"$q_1=y^2-x^3=0$")
ax.plot([-0.35, 1.42], [0, 0], color="#588632", lw=2.4, label=r"$q_2=y=0$")
ax.scatter([0], [0], s=80, color=red, zorder=6)
ax.annotate("singular point", (0, 0), (-.20, -.55), color=red,
            arrowprops={"arrowstyle": "->", "color": red})
ax.set(xlim=(-.35, 1.42), ylim=(-1.60, 1.60), xlabel=r"$x$", ylabel=r"$y$")
ax.set_aspect("equal")
ax.set_title("Exact real slice of a complex divisor", color=ink, fontsize=13)
ax.legend(loc="upper left", fontsize=10, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.text(.03, .025, r"$Y:\ y(y^2-x^3)=0$ in $\mathbb{C}^2$."+"\n"+
        "The proof covers all complex strata\nin any dimension.",
        transform=ax.transAxes, fontsize=8.5, color=ink, va="bottom",
        bbox={"facecolor": "#f7f9fc", "edgecolor": "none", "alpha": .9})

def panel(ax, title):
    ax.axis("off")
    ax.text(0, 1.02, title, color=ink, fontsize=13, weight="bold", va="bottom")
def box(ax, x, y, w, h, text, face="#e6eff8", fontsize=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=.025",
                               facecolor=face, edgecolor="#b2c6dc", linewidth=1))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", color=ink,
            fontsize=fontsize, linespacing=1.5)
def arrow(ax, a, b):
    ax.annotate("", b, a, arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 1.8})

ax = fig.add_subplot(grid[0, 1])
panel(ax, "1. Normalize each divisor prime\n(§§5.27.4–5.27.6)")
box(ax, .03, .62, .88, .26,
    r"$H_i=H_{(q_i)},\quad \Theta_i=q_i\nabla_{v_i}$"+"\n"+
    r"$L_i$ finite free, $\Theta_iL_i\subset L_i$")
box(ax, .03, .20, .88, .25,
    r"$e'=q_i^k e \quad\Longrightarrow\quad \lambda'=\lambda+k$"+"\n"+
    r"$0\leq\mathrm{Re}(\lambda')<1$; nilpotents retained.")
arrow(ax, (.47,.59), (.47,.48))
ax.text(.04, .02, "Finite cyclic relation + actual Fuchs bounds.\nOnly finitely many shifts are required.",
        color=ink, fontsize=11)

ax = fig.add_subplot(grid[0, 2])
panel(ax, "2. Build one finite sheaf\n(§§5.27.7–5.27.8)")
box(ax, .03, .63, .88, .25,
    r"$F_0\subset E,\quad (F_0)_{(q_i)}=L_i$"+"\n"+
    r"$F_0[f^{-1}]=E$")
box(ax, .03, .18, .88, .28,
    r"$\mathscr{L}_\Sigma=\mathscr{F}_0^{**}$"+"\n"+
    "Coherent sheaf duals on one neighbourhood")
arrow(ax, (.47,.60), (.47,.49))
ax.text(.04, -.01, "The infinite intersection is a stalk membership\nformula for this already coherent finite sheaf.",
        color=ink, fontsize=11)

ax = fig.add_subplot(grid[1, 0])
panel(ax, "3. Membership at every point\n(§§5.27.8–5.27.10)")
box(ax, .01, .55, .91, .30,
    r"$L=\bigcap_{\mathrm{ht}(\mathfrak{p})=1}(F_0)_{\mathfrak{p}}\ \subset E_K$"+"\n"+
    r"$(F_0)_{(q_i)}=L_i$; $(F_0)_{\mathfrak{p}}=E_{\mathfrak{p}}$ if $f\notin\mathfrak{p}$",
    fontsize=11)
box(ax, .01, .10, .91, .28,
    r"$s\in L$ iff $s\in E$ and $s$ is strict on $Y_{\rm reg}$."+"\n"+
    r"$q^\lambda\sum_j(\log q)^j a_j(q,w)$, all $a_j$ holomorphic.",
    fontsize=11)
arrow(ax, (.47,.52), (.47,.41))

ax = fig.add_subplot(grid[1, 1])
panel(ax, "4. Saturation at singular points\n(§5.27.11)")
box(ax, .03, .53, .88, .30,
    r"$g\notin(q_i)\ \forall i,\quad s\in E,\quad g^m s\in L$"+"\n"+
    r"$g$ is a unit in every $H_{(q_i)}$.")
box(ax, .03, .09, .88, .24,
    r"$s\in L_i\ \forall i\quad\Longrightarrow\quad s\in L$",
    face="#e6f1e0")
arrow(ax, (.47,.49), (.47,.36))
ax.text(.04, -.035, "The primes away from Y are fixed by E.\nReflexivity alone would not imply saturation.",
        color=ink, fontsize=11)

ax = fig.add_subplot(grid[1, 2])
panel(ax, "5. Logarithmic stability\n(§§5.27.6, 5.27.9)")
box(ax, .03, .56, .88, .27,
    r"$-mI+\mathrm{ad}(B_0)$ is invertible for $m\geq1$."+"\n"+
    r"$\mathrm{Re}(\beta-\alpha)\in(-1,1)$")
box(ax, .03, .09, .88, .30,
    r"$\eta(f)\in(f)\quad\Longrightarrow\quad\nabla_\eta L\subset L$"+"\n"+
    "Tangential pole cancellation\n+ the intersection formula", fontsize=11)
arrow(ax, (.47,.52), (.47,.43))
ax.text(.04, -.035, "All Jordan blocks are included.\nThe assertion holds at every singular point.",
        color=ink, fontsize=11)

ax = fig.add_subplot(grid[2, :])
panel(ax, "The general characteristic cutoff is still an open step (§5.27.12)")
box(ax, .01, .15, .96, .55,
    "Arbitrary regular holonomic microlocal module\n"+
    "→ actual contact / finite D-type realization → coefficient lattice above\n"+
    "→ proved order correspondence and full characteristic-operator stability",
    face="#fff0df", fontsize=13)

fig.text(.045, .031,
         "Proof locators: GL-DMOD-13, §§5.27.4–5.27.11; open obligations §5.27.12.  "
         "Human context: Kashiwara–Kawai, Holonomic Systems III (1981), §§1–2, 5.1.6.",
         fontsize=10, color=ink)
fig.savefig(BASE / "singular-divisor-strict-coefficient-lattice.png", dpi=160, facecolor=fig.get_facecolor())
fig.savefig(BASE / "singular-divisor-strict-coefficient-lattice.svg", facecolor=fig.get_facecolor())
print("Rendered singular-divisor-strict-coefficient-lattice.png and .svg")

"""CC0. Exact planar cone section and all-degree module-lift diagram."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch

root = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                    "svg.hashsalt": "canonical-derived-action-20261009"})
data = {
    "epsilon": "1/4", "diamond_R": "1/2", "Omega_vertex_real_time": "1/5",
    "omega_level_real_time": "-1/10", "S_level_real_time": "-1/40",
    "geometry": "Exact N=1 complex-time section; no spatial coordinates",
    "A": [[0, 1], [0, 0]], "B": [[0, 0], [1, 0]],
    "AB_minus_BA": [[1, 0], [0, -1]],
    "Koszul_lift_composition": [[-1, 0], [0, 1]],
    "proof_loci": ["DL.2-DL.9", "DL.11-DL.22", "DL.26-DL.27"]
}
f = lambda s: float(Fraction(s))
eps, R, vertex, wlevel, slevel = [f(data[k]) for k in
    ["epsilon", "diamond_R", "Omega_vertex_real_time",
     "omega_level_real_time", "S_level_real_time"]]
fig, axes = plt.subplots(2, 2, figsize=(15.6, 9.4))
fig.subplots_adjust(left=.06, right=.97, top=.94, bottom=.07,
                    hspace=.33, wspace=.18)
ax = axes[0, 0]
ax.add_patch(Polygon([(-R, 0), (0, eps*R), (R, 0), (0, -eps*R)],
                    fill=False, edgecolor="#556270", lw=2, ls="--"))
def triangle(level, color, alpha):
    ax.add_patch(Polygon([(level, eps*(vertex-level)), (vertex, 0),
                         (level, -eps*(vertex-level))],
                        facecolor=color, edgecolor=color, alpha=alpha))
triangle(wlevel, "#437cc1", .25)
triangle(slevel, "#dc7544", .48)
ax.plot([-.52, vertex], [eps*(vertex+.52), 0], color="#14604b", lw=2, ls="--")
ax.plot([-.52, vertex], [-eps*(vertex+.52), 0], color="#14604b", lw=2, ls="--")
ax.axvline(wlevel, color="#437cc1", ls=":", lw=1.6)
ax.axvline(slevel, color="#dc7544", ls=":", lw=1.6)
ax.scatter([0], [0], c="black", s=20)
ax.scatter([vertex], [0], facecolors="white", edgecolors="#14604b", s=40, zorder=5)
ax.text(vertex+.025, .005, r"$\Omega$ vertex $1/5$", fontsize=10)
ax.text(-.34, .105, r"$D_{1/2}$: round diamond", fontsize=10,
        bbox={"facecolor": "white", "alpha": .85, "edgecolor": "none"})
ax.annotate(r"$S_*=\Omega\setminus\omega$", (-.03, .04), (-.43, .045),
            arrowprops={"arrowstyle": "->", "color": "#437cc1"}, color="#285a99")
ax.annotate(r"$S\subset S_*$", (.11, -.007), (.27, -.07),
            arrowprops={"arrowstyle": "->", "color": "#a85226"}, color="#a85226")
ax.text(-.49, -.145,
        r"$\omega:\ \mathrm{Re}\,t<-1/10;\quad S:\ \mathrm{Re}\,t\geq-1/40$",
        fontsize=10)
ax.set(xlim=(-.55, .55), ylim=(-.17, .17),
       xlabel=r"$\mathrm{Re}\,t$", ylabel=r"$\mathrm{Im}\,t$",
       title="Exact cone-topology support geometry (N = 1)")
ax.grid(alpha=.18)

def panel(ax, title):
    ax.set_axis_off(); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0, 1.01, title, fontsize=13, weight="bold")
def box(ax, xy, txt, color="#eaf0f7", fs=11):
    ax.text(*xy, txt, fontsize=fs, ha="center", va="center",
            bbox={"boxstyle": "round,pad=.6", "facecolor": color,
                  "edgecolor": "#8495a7"})
def arrow(ax, a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13,
                                color="#3a5068", lw=1.5))

ax = axes[0, 1]; panel(ax, "All input degrees: cup and shifted trace")
box(ax, (.48, .81), r"$m_T(a,b)=(Ta,(-1)^N Tb)$")
arrow(ax, (.48, .70), (.48, .60))
box(ax, (.48, .49),
    r"$Q_N(a,b)=(\mathrm{Tr}_q a,(-1)^N\mathrm{Tr}_{q-1}b)$"+"\n"+
    r"$\mathrm{Tr}_q=(-1)^{N(q-N)}I_q$", fs=11)
arrow(ax, (.48, .35), (.48, .24))
box(ax, (.48, .14), r"$\mathcal{A}_T=Q_N L_\eta m_T,\qquad d\mathcal{A}_T=\mathcal{A}_Td$",
    color="#e7f3e9", fs=11)

ax = axes[1, 0]; panel(ax, "Auxiliary concentration supplies a genuine module lift")
box(ax, (.48, .84), r"$R\Gamma_{S_*}(q_{G*}\mathcal{O})\simeq\mathcal{F}[-1]$"+"\n"+
    r"$\mathcal{F}=H^1_{S_*}(q_{G*}\mathcal{O})$: an actual $R$-module", fs=11)
arrow(ax, (.48, .70), (.48, .60))
box(ax, (.48, .49),
    r"$\mathcal{Q}_R=\Gamma_S I_{\mathbf{C}}^{\bullet}(\mathcal{F})[-1]$"+"\n"+
    r"$\mathcal{Q}_R\in D(R\mathrm{-Mod})$", color="#e7f3e9")
arrow(ax, (.48, .35), (.48, .24))
box(ax, (.48, .13),
    "Underlying object and canonical action:\n"+r"$R\Gamma_S(q_{G*}\mathcal{O})$",
    fs=11)
ax.text(.03, -.06, "Explicit barriers + weighted existence prove concentration; DL.15–DL.22.",
        fontsize=9)

ax = axes[1, 1]; panel(ax, "Why chosen derived endomorphism lifts are insufficient")
box(ax, (.48, .81), "Contractible C:  C² → C², differential = identity\n"+
    "A = [[0, 1], [0, 0]],   B = [[0, 0], [1, 0]]", fs=11)
box(ax, (.48, .49), "Koszul lift composition:\n"+
    r"$-AB+BA=\mathrm{diag}(-1,1)\neq0$", color="#fff0e5", fs=12)
arrow(ax, (.48, .35), (.48, .24))
box(ax, (.48, .13), "Valid Hom contraction on the actual module model:\n"+
    r"$H\phi=(-1)^k\phi h,\qquad dH+Hd=1$", color="#e7f3e9", fs=11)
fig.suptitle("Canonical all-degree action: exact supports, module lift and contraction signs",
             fontsize=16, y=.992)
fig.savefig(root/"derived-action-module-lift.png", dpi=200,
            metadata={"Software": "CC0 reproducible mathematical figure"})
fig.savefig(root/"derived-action-module-lift.svg", metadata={"Date": None,
            "Creator": "CC0 reproducible mathematical figure"})
(root/"derived-action-figure-data.json").write_text(
    json.dumps(data, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"png": str(root/"derived-action-module-lift.png"),
                  "source": str(Path(__file__).resolve())}))

"""Original exact RCC model diagram. Run with Python 3 and Matplotlib."""
from pathlib import Path
import json
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-relative-commutants-central-cocycles-20261009-v1"
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Polygon

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "data.json").read_text(encoding="utf-8"))
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "none",
    "axes.unicode_minus": True,
})
INK = "#142c40"
MUTED = "#486274"
BLUE = "#2674a8"
TEAL = "#00877d"
ORANGE = "#c76527"
BG = "#f4f7fa"

fig = plt.figure(figsize=(18, 13.3), facecolor=BG)
fig.text(.045, .958, DATA["title"], fontsize=24, weight="bold", color=INK)
fig.text(.045, .927,
         "Whole-algebra identities, exact phases, and finite samples of infinite limits",
         fontsize=14.5, color=MUTED)

def panel(rect, title):
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1,
        boxstyle="round,pad=0.006,rounding_size=0.02",
        transform=ax.transAxes, facecolor="white", edgecolor="#ccd8e1",
        linewidth=1.2, clip_on=False))
    ax.text(.035, .945, title, color=INK, fontsize=17, weight="bold",
            ha="left", va="top")
    return ax

def txt(ax, x, y, text, size=13.5, color=INK, **kw):
    return ax.text(x, y, text, fontsize=size, color=color, **kw)

def arrow(ax, a, b, color=BLUE):
    ax.annotate("", xy=b, xytext=a,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                        shrinkA=12, shrinkB=12, mutation_scale=13))

a = panel([.045, .515, .438, .378], "A  |  Shear away from zero")
txt(a, .045, .83, r"$T^ng(r,q)=e^{nr}\rho(2r+3)\rho(q-nr)$")
plot = a.inset_axes([.13, .255, .77, .48])
colors = [BLUE, TEAL, ORANGE]
for sample, color in zip(DATA["shear"]["samples"], colors):
    plot.add_patch(Polygon(sample["vertices_r_q"], closed=True,
        facecolor=color, edgecolor=color, alpha=.22, linewidth=1.5))
    r, q = sample["center_r_q"]
    plot.scatter([r], [q], s=33, color=color, zorder=3)
    n = sample["n"]
    plot.annotate(f"n = {n}", (r, q), xytext=(10, 4),
                  textcoords="offset points", fontsize=11, color=color,
                  weight="bold")
plot.set(xlim=(-2.3, -.65), ylim=(-9.6, 1.65),
         xlabel=r"$r$", ylabel=r"$q$")
plot.set_xticks([-2, -1.5, -1])
plot.set_yticks([-9, -6, -3, 0])
plot.grid(alpha=.17)
plot.spines[["right", "top"]].set_visible(False)
plot.tick_params(labelsize=10.5)
txt(a, .045, .137,
    r"$\|T^ng\|_1+\|\partial_r^2T^ng\|_1\leq C_g(1+n)^2e^{-n}\to0$",
    size=13)
txt(a, .045, .057, "Every marked value is positive; only three supports are drawn.",
    size=11.6, color=MUTED)

b = panel([.517, .515, .438, .378], "B  |  State corners form a net")
txt(b, .045, .83,
    r"$Q=\ell^\infty(I),\quad I\ \mathrm{uncountable},\quad \psi(a)=\sum_{i\in I}a_i$")
net = b.inset_axes([.08, .25, .84, .52])
net.set(xlim=(0, 1), ylim=(.1, .95))
net.axis("off")
nodes = {v["id"]: v for v in DATA["finite_net"]["sample_nodes"]}
labels = {"A": r"$\{\alpha\}$",
          "B": r"$\{\alpha,\beta\}$",
          "C": r"$\{\alpha,\gamma\}$",
          "D": r"$\{\alpha,\beta,\gamma\}$"}
for u, v in DATA["finite_net"]["sample_edges"]:
    x0, y0 = nodes[u]["xy"]
    x1, y1 = nodes[v]["xy"]
    dx, dy = x1-x0, y1-y0
    net.annotate("", xy=(x1-.22*dx, y1-.22*dy),
        xytext=(x0+.22*dx, y0+.22*dy),
        arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.8,
                        shrinkA=0, shrinkB=0, mutation_scale=13))
for key, value in nodes.items():
    x, y = value["xy"]
    net.text(x, y, labels[key], ha="center", va="center", fontsize=14,
         color=INK, bbox=dict(boxstyle="round,pad=.32",
                            facecolor="#ecf6f5", edgecolor=TEAL))
txt(b, .045, .17, r"$p_F\uparrow1\ \mathrm{strongly},\qquad"
    r"A_F=\sum_{i\in F}p_i\otimes M_{f_i}\longrightarrow\bigoplus_i M_{f_i}$",
    size=12.7)
txt(b, .045, .09, "Four finite subsets only: the diagram does not exhaust I.",
    size=11.7, color=MUTED)
txt(b, .045, .039, "No faithful normal state and no sequence of finite corners suffice.",
    size=11.7, color=MUTED)

c = panel([.045, .095, .438, .378], "C  |  The centralizing matrix factor")
txt(c, .045, .83, r"$h=\mathrm{diag}(1,4),\quad \varphi(x)=\mathrm{Tr}(hx),"
    r"\quad t_0=\pi/(2\log4)$", size=13.5)
txt(c, .075, .69,
    r"$\lambda(t_0)\pi_\varphi(E_{12})=-i\,\pi_\varphi(E_{12})\lambda(t_0)$",
    size=15)
txt(c, .075, .57,
    r"$\pi_\varphi(h^{-it_0})\pi_\varphi(E_{12})"
    r"=i\,\pi_\varphi(E_{12})\pi_\varphi(h^{-it_0})$", size=14)
txt(c, .5, .455, "The phases cancel:  i (−i) = 1", size=13.5,
    color=TEAL, ha="center", weight="bold")
txt(c, .5, .335, r"$z_t=\pi_\varphi(h^{-it})\lambda(t)$",
    size=18, ha="center", color=BLUE)
txt(c, .12, .18, r"$z_t$", size=17, ha="center")
arrow(c, (.18, .20), (.39, .20))
arrow(c, (.58, .20), (.74, .20))
txt(c, .285, .245, r"$F$", size=13, color=BLUE, ha="center")
txt(c, .48, .18, r"$I\otimes T_t$", size=16, ha="center")
txt(c, .66, .245, r"$I\otimes\mathcal{F}$", size=12, color=BLUE, ha="center")
txt(c, .85, .18, r"$I\otimes M_{e^{-itq}}$", size=14.2, ha="center")
txt(c, .045, .038, r"$F\xi(r)=h^{ir}\xi(r)$; the final characters generate the full center.",
    size=11.5, color=MUTED)

d = panel([.517, .095, .438, .378], "D  |  A central coboundary is inner")
txt(d, .045, .83,
    r"$\theta_sf(q)=f(q-s),\quad\tau(f)=\int e^{-q}f(q)\,dq$", size=14)
txt(d, .045, .72, r"$\tau\circ\theta_s=e^{-s}\tau,\qquad v_b(q)=e^{ibq}$",
    size=14)
txt(d, .045, .635, r"Shown: $s>0$. The identities hold for every real $s$.",
    size=11.5, color=MUTED)
d.plot([.16, .83], [.54, .54], color="#bccad5", linewidth=2)
d.scatter([.23, .76], [.54, .54], s=50, color=[TEAL, BLUE], zorder=3)
arrow(d, (.29, .54), (.69, .54), TEAL)
txt(d, .5, .575, r"$+s$", ha="center", color=TEAL)
txt(d, .23, .46, r"$q-s$", size=14, ha="center")
txt(d, .76, .46, r"$q$", size=14, ha="center")
txt(d, .5, .335,
    r"$v_b(q)\,\overline{v_b(q-s)}=e^{ibq}e^{-ib(q-s)}=e^{ibs}$",
    size=14, ha="center")
txt(d, .5, .22, r"$M_{e^{iby}}L_sM_{e^{-iby}}=e^{ibs}L_s$",
    size=15, ha="center", color=BLUE)
txt(d, .045, .1,
    r"$P\cong B(L^2(\mathbb{R})),\qquad N'\cap P=N,\qquad Z(P)=\mathbb{C}1$",
    size=12.8)
txt(d, .045, .039, "The multiplication algebra is its own relative commutant.",
    size=11.7, color=MUTED)

fig.text(.045, .047,
    "Proofs: RCC7.h–RCC7.o, RCC7.p–RCC7.w, RCC7.x–RCC7.aa; solved diagnostics RCC8.",
    fontsize=12, color=MUTED)
fig.text(.045, .024,
    "Original diagram and source: CC0. Exact data and reproducible script accompany the figure.",
    fontsize=11, color=MUTED)
fig.savefig(HERE / "rcc-models.png", dpi=180, facecolor=BG)
fig.savefig(HERE / "rcc-models.svg", facecolor=BG, metadata={"Date": None})
plt.close(fig)
font_license = Path(font_manager.findfont("DejaVu Sans")).parent / "LICENSE_DEJAVU"
if not font_license.is_file():
    raise FileNotFoundError("The installed DejaVu license must be retained.")
shutil.copyfile(font_license, HERE / "FONT-LICENSE.txt")
print("Rendered rcc-models.png and rcc-models.svg; retained FONT-LICENSE.txt.")

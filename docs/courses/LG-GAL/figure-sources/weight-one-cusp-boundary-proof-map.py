"""Reproduce the exact cusp-boundary mechanism of Proposition 3.2A."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root = Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
fig, ax = plt.subplots(figsize=(5, 11), dpi=180)
ax.set(xlim=(0, 5), ylim=(0, 11))
ax.axis("off")
ax.text(2.5, 10.65, "Weight one at the cusps", ha="center",
        fontsize=20, weight="bold")
ax.text(2.5, 10.24, "Every level N and odd character; every good prime p",
        ha="center", fontsize=10)

panels = [
    (8.93, "#edf4ff", "1  All cusp constant terms", [
        r"$C:M_1(\Gamma_0(N),\varepsilon)\longrightarrow\mathcal{B}_\varepsilon$",
        r"$\ker C=S_1(\Gamma_0(N),\varepsilon)$",
        "Noncuspidal f gives a nonzero cusp function.",
        "Primitive columns modulo N; orientation and (16B–16C)."]),
    (6.55, "#fff4dc", "2  The p + 1 Hecke cosets", [
        r"$p\ \mathrm{cosets}:\ D=1,\quad \mathrm{weight}=1/p$",
        r"$1\ \mathrm{coset}:\ D=p,\quad \mathrm{weight}=1$",
        r"$C_{T_pf}(a,c)=C_f(a,pc)+C_f(p^{-1}a,c)$",
        r"$T_p=R_p+S_p\quad$" + "on cusp functions; (16D–16F)."]),
    (4.14, "#edf8ef", "3  One finite character component", [
        r"$R_uS_u=\varepsilon(u)I\quad(u\in U_N)$",
        r"$R_u C_\alpha=\alpha(u)C_\alpha,\quad C_\alpha\ne0$",
        r"$S_u C_\alpha=\varepsilon(u)\alpha(u)^{-1}C_\alpha$",
        "Choose this component once for all primes; (16G)."]),
    (1.78, "#edf4ff", "4  The reducible Galois representation", [
        r"$\chi_1=\alpha,\qquad\chi_2=\varepsilon\alpha^{-1}$",
        r"$a_p=\chi_1(p)+\chi_2(p),\quad\chi_1\chi_2=\varepsilon$",
        r"$\rho_f=\chi_{1,G}\oplus\chi_{2,G}$",
        "Finite, odd, unramified outside N; (16A), Lemma 0.1."]),
]
for y, color, title, lines in panels:
    ax.add_patch(FancyBboxPatch((0.18, y-0.91), 4.64, 1.82,
        boxstyle="round,pad=.06", facecolor=color,
        edgecolor="#27445f", linewidth=1.3))
    ax.text(2.5, y+0.65, title, ha="center", fontsize=13, weight="bold")
    for offset, line in zip([0.26, -0.10, -0.46, -0.76], lines):
        ax.text(2.5, y+offset, line, ha="center", va="center",
                fontsize=11 if offset != -0.76 else 8.9)
for a, b in zip(panels, panels[1:]):
    ax.add_patch(FancyArrowPatch((2.5, a[0]-0.99), (2.5, b[0]+0.99),
        arrowstyle="-|>", mutation_scale=17, color="#27445f", linewidth=1.4))
ax.text(2.5, 0.29, "Proof map of Proposition 3.2A.\n"
        "It does not assert that every boundary function is realized.", ha="center",
        va="center", fontsize=9)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
p = root / "assets/weight-one-cusp-boundary-proof-map.png"
fig.savefig(p, facecolor="white", metadata={"Software": "Matplotlib"})
plt.close(fig)
with Image.open(p) as im:
    im.copy().save(p)

"""CC0-1.0. Reproducible schematic for FWT.1--FWT.30."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="full-weighted-endpoint-tail-v20"
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
fig = plt.figure(figsize=(14, 8), facecolor="white")
ax = fig.add_axes([0.04, 0.06, 0.92, 0.88])
ax.set(xlim=(0, 14), ylim=(0, 8))
ax.axis("off")
ax.text(0, 7.7, "The full WM.22 endpoint tail is the final lamp configuration",
        fontsize=19, weight="bold")
ax.text(0, 7.26,
        r"Actual $H$ endpoint $(C_{2n},V_{2n},M_{2n})$; "
        r"$M_{2n}\equiv\sum C_{2n}\ (\mathrm{mod}\ 2)$; physical character $\lambda^{M_{2n}}$",
        fontsize=12)

def box(x, y, w, h, text, color="#eaf3fc", fs=12):
    patch = FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.12", fc=color, ec="#38516d", lw=1.2)
    ax.add_patch(patch)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fs, linespacing=1.6)
    return patch

box(.15, 5.55, 4.1, 1.1,
    r"$V_{2n}/n\to\delta(1,1,1),\quad \delta<0$" + "\n" +
    r"$h(V_{2n})/n\to\gamma=3\delta<0$" + "\n" +
    r"$M_{2n}/n\to\kappa=-4\delta>0$")
box(5, 5.55, 8.5, 1.1,
    r"$c_n=\eta\,1_{\{h\geq\lfloor\gamma n\rfloor\}}$ is finite" + "\n" +
    r"$\Pi_n(\eta)=(c_n,v_n,m_n)\in H$" + "\n" +
    r"$v_n\approx\delta n(1,1,1)$; $m_n\approx\kappa n$, with exact lamp parity")

# The time coordinate is schematic; vertical coordinates encode no heights.
ax.plot([.5, 13.1], [4.7, 4.7], color="#32475a", lw=1.8)
ax.axvspan(4.3, 9.4, ymin=.46, ymax=.66, color="#fff1c2", alpha=.7)
for x, label in [(1, "0"), (4.3, "2k"), (6.8, "2n"), (9.4, "2l")]:
    ax.plot([x, x], [4.55, 4.85], color="#32475a")
    ax.text(x, 4.23, label, ha="center", fontsize=13)
ax.text(6.8, 5.04, "Only toggles in this window can differ", ha="center",
        fontsize=12, weight="bold")
ax.text(2.25, 3.65, "Earlier toggles are high:\nretained twice, cancel",
        ha="center", fontsize=11)
ax.text(6.8, 3.65,
        "Past low toggles + future high toggles\n"
        r"$C_{2n}+c_n(\eta)$, in $\mathbb{F}_2$",
        ha="center", fontsize=11)
ax.text(11.35, 3.65, "Later toggles are low:\nretained by neither",
        ha="center", fontsize=11)
ax.text(6.8, 3.10,
        r"$k=\lfloor(1-\epsilon)n\rfloor,\quad"
        r"l=\lceil(1+\epsilon)n\rceil,\quad l-k\leq2\epsilon n+2$",
        ha="center", fontsize=12)

box(.15, 1.75, 6.15, .92,
    "Follow the finite spatial path, select the toggles;\n"
    r"correct the even integer error using $z^2=(az)^2$." + "\n" +
    r"$|G_{2n}^{-1}\Pi_n(\eta)|\leq12\epsilon n+12+o(n)$",
    color="#e8f5e8", fs=11.5)
box(7.2, 1.75, 6.15, .92,
    r"$H(G_{2n}\mid\eta)=o(n)$" + "\n" +
    "Finite-marked criterion AB.4, both phases:\n" +
    r"full endpoint tail $=\sigma(\eta)$",
    color="#e8f5e8", fs=12)
ax.annotate("", xy=(7.02, 2.21), xytext=(6.48, 2.21),
            arrowprops={"arrowstyle":"->", "lw":1.6})
ax.text(6.9, 1.07,
    r"Actual $U,V$ are the full configuration algebras; "
    r"$R_i=w_i^+\,d(s_i)_*m_U/dm_V$ for all five branches.",
    ha="center", fontsize=12, weight="bold")
ax.text(6.9, .52,
    "FWT.1–FWT.30. Schematic positions and sizes encode no trace mass or metric.\n"
    "This full-tail theorem alone does not determine the original invariant-state cost minimum.",
    ha="center", fontsize=10.5)
fig.savefig(ROOT / "full-weighted-endpoint-tail-v20.png", dpi=180, bbox_inches="tight")
fig.savefig(ROOT / "full-weighted-endpoint-tail-v20.svg", bbox_inches="tight", metadata={"Date":None})
print(str(ROOT / "full-weighted-endpoint-tail-v20.png"))

# Normalize serializer whitespace while retaining every SVG coordinate and label.
svg_path=ROOT / "full-weighted-endpoint-tail-v20.svg"
svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")

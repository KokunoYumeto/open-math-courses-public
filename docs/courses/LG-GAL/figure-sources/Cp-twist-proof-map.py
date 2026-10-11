"""Reproduce the signed rational-base Tate-twist proof mechanism."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

root = Path(__file__).resolve().parents[1]
(root/"assets").mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":15})
fig, ax = plt.subplots(figsize=(5,12), dpi=180)
ax.set(xlim=(0,5), ylim=(0,12))
ax.axis("off")
ax.text(2.5,11.65,"Signed Tate twists",ha="center",fontsize=21,weight="bold")
ax.text(2.5,11.2,r"$C_p(w)^{G_{\mathbf{Q}_p}}=0\quad(w\neq0)$",
        ha="center",fontsize=18)
ax.text(2.5,10.8,"Every prime p, including p = 2",ha="center",fontsize=12)
boxes = [
    (9.6, r"$g(x)=\chi_p(g)^{-w}x$", "Invariant coefficient; w is a nonzero integer", "#edf4ff"),
    (7.55, "x lies in the closure of\n"+r"$F_\infty=\bigcup_m\mathbf{Q}_p(\zeta_{p^m})$",
     r"Kernel of $\chi_p$ fixes x; CI10, CI13", "#edf4ff"),
    (5.5, r"$R_nx\in F_n,\quad |R_nx|\leq p|x|$",
     "Equivariant normalized traces; CI14–CI17", "#edf8ef"),
    (3.45, r"$R_nx=(1+p^a)^{-w}R_nx=0$",
     "Choose a ≥ n (a ≥ 2 at p = 2); g fixes "+r"$F_n$", "#edf8ef"),
    (1.4, r"$R_nx\longrightarrow x\quad\Longrightarrow\quad x=0$",
     "Density and the uniform trace bound; CI18", "#fff4dc"),
]
for y, body, locator, colour in boxes:
    ax.add_patch(FancyBboxPatch((.3,y-.58),4.4,1.16,boxstyle="round,pad=.12",
                               facecolor=colour,edgecolor="#27445f",linewidth=1.3))
    ax.text(2.5,y+.13,body,ha="center",va="center",linespacing=1.5)
    ax.text(2.5,y-.43,locator,ha="center",fontsize=10,color="#37516a")
for upper, lower in zip([9.6,7.55,5.5,3.45],[7.55,5.5,3.45,1.4]):
    ax.add_patch(FancyArrowPatch((2.5,upper-.73),(2.5,lower+.73),
        arrowstyle="-|>",mutation_scale=18,color="#27445f",linewidth=1.4))
ax.text(2.5,.35,"General finite K: the coset product CI19–CI20\nreduces to the rational-base twist wd ≠ 0.",
        ha="center",fontsize=11)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
target = root/"assets/Cp-twist-proof-map.png"
fig.savefig(target,facecolor="white",metadata={"Software":"Matplotlib"})
plt.close(fig)
with Image.open(target) as image:
    image.copy().save(target)

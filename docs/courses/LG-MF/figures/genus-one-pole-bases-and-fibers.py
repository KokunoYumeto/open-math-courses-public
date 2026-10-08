"""CC0-1.0: reproduce the pole bases and fibers in Theorem 3.0, (G1)–(G11)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).with_suffix(".png")
fig = plt.figure(figsize=(15, 7))
ink, blue, red = "#193450", "#eaf2f9", "#b83b39"
ax = fig.add_axes([.035, .07, .30, .84]); ax.axis("off")
ax.set_title("G1–G4: exact pole-order bases", fontsize=17, pad=14)
table = ax.table(cellText=[
    ["1", "1", "0"], ["2", "1, x", "0, 2"],
    ["3", "1, x, y", "0, 2, 3"],
    ["4", "1, x, y, x²", "0, 2, 3, 4"],
    ["5", "1, x, y, x², xy", "0, 2, 3, 4, 5"],
    ["6", "1, x, y, x², xy, x³", "0, 2, 3, 4, 5, 6"]],
    colLabels=["n", "basis of L(nP)", "pole orders"],
    colWidths=[.08, .58, .34], loc="upper center", cellLoc="left")
table.auto_set_font_size(False); table.set_fontsize(11); table.scale(1, 2)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("#a5b7c8")
    if row == 0: cell.set_facecolor(ink); cell.set_text_props(color="white")
    elif row % 2: cell.set_facecolor(blue)
ax.text(.5, .29, r"$\omega$ is nowhere zero" + "\n" + r"locally at $P$: $\omega=dt$" + "\n\n" +
        r"$x=t^{-2}+O(t^2)$" + "\n" + r"$y=dx/\omega=-2t^{-3}+O(t)$" + "\n\n" +
        r"$y^2=4x^3-ax-b$", ha="center", va="center", fontsize=16, color=ink,
        bbox=dict(boxstyle="round,pad=.8", facecolor=blue, edgecolor="#a5b7c8"))

ax = fig.add_axes([.38, .09, .59, .82]); ax.set_xlim(-.3, 10.1); ax.set_ylim(0, 8); ax.axis("off")
ax.set_title(r"G9–G11: fibers of $x:X\longrightarrow\mathbb{P}^1$", fontsize=18, pad=14)

def box(x, y, w, h, content, fontsize=14):
    ax.add_patch(FancyBboxPatch((x,y), w,h, boxstyle="round,pad=.12", facecolor=blue,
                               edgecolor="#9eb3c6", linewidth=1.2))
    ax.text(x+w/2,y+h/2,content,ha="center",va="center",fontsize=fontsize,color=ink)

def arrow(start, end):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=18,
                                linewidth=1.8,color=ink))

box(.0,5.5,3.9,1.7,r"$Q_+,\ Q_-$" + "\n" + r"$y=+\sqrt{p(u)},\ -\sqrt{p(u)}$" + "\n" +
    "two simple zeros of x − u", fontsize=13)
box(6.0,5.5,3.8,1.7,r"$u\in\mathbb{C},\ p(u)\ne0$" + "\n" + "nonbranch value", fontsize=15)
arrow((4.15,6.35),(5.8,6.35))
box(.0,2.8,3.9,1.7,r"one point $Q_r$" + "\n" + r"$\mathrm{ord}_{Q_r}(x-r)=2$" + "\n" +
    r"$\mathrm{ord}_{Q_r} y=1$; coordinate $y$", fontsize=13)
box(6.0,2.8,3.8,1.7,r"$r:\ p(r)=0$" + "\n" + "three distinct finite branch values", fontsize=13)
arrow((4.15,3.65),(5.8,3.65))
box(.0,.1,3.9,1.7,r"one point $P$" + "\n" + r"$\mathrm{ord}_P x=-2$" + "\n" +
    r"$x/y=-t/2+O(t^5)$", fontsize=14)
box(6.0,.1,3.8,1.7,r"$\infty\in\mathbb{P}^1$" + "\n" + r"$\Phi(P)=O=[0:1:0]$", fontsize=15)
arrow((4.15,.95),(5.8,.95))
fig.text(.5,.018,"Exact symbolic fibers and pole orders for the constructed functions.",
         ha="center",fontsize=12,color=ink)
fig.savefig(OUT,dpi=160,facecolor="white",bbox_inches="tight")
plt.close(fig)
print(OUT)

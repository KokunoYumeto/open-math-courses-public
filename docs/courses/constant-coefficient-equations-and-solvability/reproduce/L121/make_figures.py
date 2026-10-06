"""Original exact coordinate diagrams; no imported images or private paths.

Run with Python, matplotlib and numpy. Optional --output-dir supports replay.
"""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "figures")
args = parser.parse_args()
out = args.output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.hashsalt": "AN02-PR036-coordinate-diagrams"})
BLUE, ORANGE, RED = "#176b9b", "#d57b23", "#b12834"

def save(fig, stem):
    fig.savefig(out / f"{stem}.png", dpi=180, facecolor="white")
    fig.savefig(out / f"{stem}.svg", facecolor="white",
                metadata={"Date": None, "Creator": "Original AN02 coordinate diagram"})
    plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(14, 6.0), gridspec_kw={"width_ratios": [1.15, 1]})
ax = axes[0]
ax.set_facecolor("#edf7fc")
for a in [-1, 1]:
    ax.add_patch(Rectangle((a-.65, -2.8), 1.3, 2.8, color=ORANGE, alpha=.18))
    ax.plot([a, a], [-2.8, 0], linestyle="--", color="black", linewidth=1.5)
    ax.plot(a, 0, marker="x", color="black", markersize=9, markeredgewidth=2)
    theta = np.linspace(0, 2*np.pi, 401)
    ax.plot(a+.45*np.cos(theta), .45*np.sin(theta), color=RED, linewidth=2)
    for t in [.4*np.pi, 1.4*np.pi]:
        ax.annotate("", xy=(a+.45*np.cos(t+.16), .45*np.sin(t+.16)),
                    xytext=(a+.45*np.cos(t), .45*np.sin(t)),
                    arrowprops={"arrowstyle": "->", "color": RED, "lw": 1.8})
    ax.text(a-.34, -1.45, r"$L_{%s}$" % ("-" if a<0 else "+"), color=BLUE, ha="center")
    ax.text(a+.34, -1.45, r"$R_{%s}$" % ("-" if a<0 else "+"), color=BLUE, ha="center")
    ax.text(a, -2.35, r"$B_{%s}$" % ("-" if a<0 else "+"), color=ORANGE, ha="center")
    ax.text(a, .64, rf"$a={a}$", ha="center")
ax.text(0, 1.08, r"$A$: plane minus downward rays", color=BLUE, ha="center")
ax.axhline(0, color="#888888", lw=.6)
ax.set(xlim=(-2.3, 2.3), ylim=(-2.8, 1.5), xlabel=r"$\operatorname{Re}t$",
       ylabel=r"$\operatorname{Im}t$")
ax.set_aspect("equal")
ax.set_title("Exact open cover of a punctured plane", pad=14, fontsize=14)
ax = axes[1]
matrix = np.array([[1,1,1,1],[-1,-1,0,0],[0,0,-1,-1]])
ax.imshow(matrix, cmap="coolwarm", vmin=-1, vmax=1)
for i in range(3):
    for j in range(4):
        ax.text(j, i, str(matrix[i,j]), ha="center", va="center", fontsize=19,
                color="white" if matrix[i,j] else "#303030")
ax.set_xticks(range(4), [r"$L_-$", r"$R_-$", r"$L_+$", r"$R_+$"])
ax.set_yticks(range(3), [r"$A$", r"$B_-$", r"$B_+$"])
ax.tick_params(length=0)
ax.set_title("Integral intersection map", pad=14, fontsize=14)
ax.text(.5, -.20, "Kernel basis:  (1, −1, 0, 0)  and  (0, 0, 1, −1)",
        transform=ax.transAxes, ha="center", fontsize=11)
ax.text(.5, -.33, "Positive circles give these left-minus-right vectors.",
        transform=ax.transAxes, ha="center", fontsize=11)
fig.suptitle(r"$S=\{-1,1\}$,  $\delta=0.65$,  circle radius $0.45$  |  PR11–PR15",
             fontsize=14, y=.97)
fig.subplots_adjust(top=.85, bottom=.22, wspace=.32)
save(fig, "punctured-plane-cover")

fig, axes = plt.subplots(1, 2, figsize=(14, 6.2))
ax = axes[0]
ax.add_patch(Rectangle((0,0), 2*np.pi, 2*np.pi, facecolor="#edf7fc", edgecolor=BLUE, linewidth=1.5))
ax.annotate("", xy=(2*np.pi,0), xytext=(0,0),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 3})
ax.annotate("", xy=(0,2*np.pi), xytext=(0,0),
            arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 3})
ax.text(np.pi, -.8, "normal-circle variable first", color=ORANGE, ha="center", fontsize=11)
ax.set(xlim=(-1, 7.4), ylim=(-1.2,7.2), xlabel=r"$\phi$", ylabel=r"$\theta$")
ax.set_xticks([0,np.pi,2*np.pi], ["0",r"$\pi$",r"$2\pi$"])
ax.set_yticks([0,np.pi,2*np.pi], ["0",r"$\pi$",r"$2\pi$"])
ax.set_title(r"Input: $h=\varepsilon e^{i\phi}$, $w=e^{i\theta}$", fontsize=14)
ax.set_aspect("equal")
ax = axes[1]
vertices = 2*np.pi*np.array([[0,0],[-1,-1],[0,-1],[1,0]])
ax.add_patch(Polygon(vertices, facecolor="#edf7fc", edgecolor="#444444", linewidth=1.5))
ax.annotate("", xy=(-2*np.pi,-2*np.pi), xytext=(0,0),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 3})
ax.annotate("", xy=(2*np.pi,0), xytext=(0,0),
            arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 3})
ax.text(-3.9,-2.4, r"$\phi\mapsto(-\phi,-\phi)$", color=ORANGE, rotation=40, fontsize=11)
ax.text(3.1,.45, r"$\theta\mapsto(\theta,0)$", color=BLUE, ha="center", fontsize=11)
ax.axhline(0,color="#999999",lw=.6); ax.axvline(0,color="#999999",lw=.6)
ax.set(xlim=(-7.4,7.4), ylim=(-7.2,1.7), xlabel=r"$\alpha_1=\theta-\phi$", ylabel=r"$\alpha_2=-\phi$")
ax.set_xticks([-2*np.pi,0,2*np.pi], [r"$-2\pi$","0",r"$2\pi$"])
ax.set_yticks([-2*np.pi,0], [r"$-2\pi$","0"])
ax.set_title(r"Output: $t_1=L e^{i(\theta-\phi)}$, $t_2=L e^{-i\phi}$", fontsize=14)
ax.set_aspect("equal")
fig.suptitle(r"Normal tube for $d=2$: columns $( -1,-1)$ and $(1,0)$; determinant $+1$",
             fontsize=14, y=.97)
fig.text(.5,.035, r"All phases are modulo $2\pi$. The target is an unwrapped angle diagram.  |  PR21–PR24",
         ha="center", fontsize=12)
fig.subplots_adjust(top=.84, bottom=.20, wspace=.37)
save(fig, "normal-tube-phase-map")

fig, axes = plt.subplots(1, 3, figsize=(15, 5.5), gridspec_kw={"width_ratios": [4,1.25,2]})
labels = ["(−1, 0)", "(−1, 2)", "(1, 0)", "(1, 2)"]
ax=axes[0]
ax.imshow(np.eye(4), cmap="Blues", vmin=0, vmax=1)
for i in range(4):
    for j in range(4):
        ax.text(j,i,str(int(i==j)),ha="center",va="center",fontsize=20,
                color="white" if i==j else "#333333")
ax.set_xticks(range(4), labels); ax.set_yticks(range(4), labels)
ax.set_xlabel(r"Cycle $T_{\mathbf{b}}$"); ax.set_ylabel(r"Form $\Omega_{\mathbf{a}}$")
ax.tick_params(length=0)
ax.set_title(r"Normalized periods: $(2\pi i)^{-2}\int\Omega$", fontsize=14, pad=15)
ax=axes[1]
ax.imshow(np.ones((4,1)), cmap="Greens", vmin=0,vmax=1)
for i in range(4): ax.text(0,i,"1",ha="center",va="center",fontsize=20,color="white")
ax.set_xticks([0],[r"$\tau[B]$"]); ax.set_yticks([])
ax.tick_params(length=0); ax.set_title("Tube",fontsize=14,pad=15)
ax=axes[2]
sample=np.array([2,-1,0,3])
ax.barh(np.arange(4),sample,color=[BLUE,ORANGE,"#aaaaaa",BLUE],height=.6)
ax.invert_yaxis(); ax.set_yticks(np.arange(4),labels); ax.set_xlim(-1.5,3.8)
for i,v in enumerate(sample):
    ax.text(v+.13 if v>=0 else v/2,i,str(v),ha="left" if v>=0 else "center",
            va="center",fontsize=13,color="#222222" if v>=0 else "white")
ax.axvline(0,color="#333333",lw=.6)
ax.set_title("Sample cycle coordinates",fontsize=14,pad=15)
ax.set_xlabel("Its normalized periods")
fig.suptitle(r"$S_1=\{-1,1\}$, $S_2=\{0,2\}$: four independent cycles; primitive tube $(1,1,1,1)$",
             fontsize=14,y=.97)
fig.text(.5,.035,r"Unnormalized period matrix: $(2\pi i)^2I_4=-4\pi^2I_4$.  |  PR6, PR17, PR25–PR26",
         ha="center",fontsize=12)
fig.subplots_adjust(top=.80,bottom=.21,wspace=.55)
save(fig, "period-basis-and-tube")

geometry = {
    "scope": "Original coordinate diagrams, not numerical proofs or ambient embeddings",
    "figure1": {"punctures": [-1,1], "strip_delta": .65, "positive_circle_radius": .45,
                "rays": "x=a, y<=0 excluded from A; y<0 lies in B",
                "matrix": [[1,1,1,1],[-1,-1,0,0],[0,0,-1,-1]],
                "kernel_basis": [[1,-1,0,0],[0,0,1,-1]], "proof": ["PR11","PR12","PR15"]},
    "figure2": {"dimension_d": 2, "input_order": ["phi","theta"],
                "output_order": ["alpha1","alpha2"], "matrix": [[-1,1],[-1,0]],
                "determinant": 1, "angle_identification": "modulo 2pi",
                "coordinate_formula": ["h=epsilon exp(i phi)","w=exp(i theta)",
                    "t1=L exp(i(theta-phi))","t2=L exp(-i phi)"],
                "proof": ["PR21","PR23","PR24"]},
    "figure3": {"ordered_pairs": [[-1,0],[-1,2],[1,0],[1,2]],
                "normalized_period_matrix": np.eye(4,dtype=int).tolist(),
                "normalization": "(2pi i)^(-2)", "tube_vector": [1,1,1,1],
                "sample_cycle_and_normalized_periods": [2,-1,0,3],
                "proof": ["PR6","PR17","PR25","PR26"]},
    "source_credit": "Original diagrams from the written PR036 calculation; human context ABG I p187, ABG II p163 and p176; finite-chain context Hatcher Algebraic Topology Chapter 2",
    "blender_assessment": "Coordinate cover, phase map and exact matrix are explained directly by 2D vector diagrams; a 3D ambient scene would not represent these complex complements",
}
(out/"geometry.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"outputs": [p.name for p in sorted(out.iterdir())]},indent=2))

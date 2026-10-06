"""CC0-1.0. Exact M_2 example from WS-6; no numerical infinite truncation."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
ASSETS.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "svg.hashsalt": "oa-flow-normal-weight-sum-ws6",
})
BLUE, RED, GREEN, GREY = "#24588C", "#AD3D37", "#267052", "#52606D"
fig = plt.figure(figsize=(15, 7.2), facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 15), ylim=(0, 7.2))
ax.axis("off")
ax.text(.55, 6.8, "A GNS multiplier controls the finite domain; a functional sum controls all values",
        fontsize=18, weight="bold", color="#17293A")
ax.text(.55, 6.38, r"$M=M_2(\mathbb{C}),\quad K=\mathbb{C}^2,\quad e=e_{11},\quad q=e_{22}$",
        fontsize=16)

def box(x, y, w, h, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle="round,pad=0.03,rounding_size=0.12",
                 facecolor=color, edgecolor="#D4DEE7", lw=1))

box(.55, 2.8, 6.5, 3.1, "#F0F5FB")
box(7.4, 2.8, 7.05, 3.1, "#F1F8F4")
ax.text(.82, 5.57, "Finite domain and its GNS space", color=BLUE, fontsize=16, weight="bold")
ax.text(.82, 5.03, r"$N=Me,\qquad \Lambda(x)=x\delta_1\in H=\mathbb{C}^2$", fontsize=15)
ax.text(.82, 4.54, r"$\pi(a)=a,\qquad g(a)=a_{11},\qquad t_g=1_H$", fontsize=15)
ax.text(.82, 3.94, r"$g(e_{22})=0$", fontsize=20, color=BLUE)
ax.text(3.8, 3.94, r"$\varphi(e_{22})=\infty$", fontsize=20, color=RED)
ax.text(3.23, 3.94, r"$\ne$", fontsize=20, color=GREY)
ax.text(.82, 3.28, "The identity multiplier still misses the infinite value.", fontsize=12.7, color=GREY)

ax.text(7.68, 5.57, "The actual functional sum repairs it", color=GREEN, fontsize=16, weight="bold")
ax.text(7.68, 5.03, r"$h_n(a)=a_{22}\quad(n\geq1),\qquad t_{h_n}=0$", fontsize=15)
ax.text(7.68, 4.45, r"$\varphi(a)=g(a)+\sum_{n\geq1}h_n(a)\qquad(a\geq0)$", fontsize=18, color=GREEN)
ax.text(7.68, 3.8, r"$a_{22}=0:\quad \sum_n h_n(a)=0$", fontsize=15)
ax.text(7.68, 3.27, r"$a_{22}>0:\quad \sum_n h_n(a)=\infty$", fontsize=15)

columns = [r"$a$", r"$g(a)$", r"$\sum h_n(a)$", r"$\varphi(a)$"]
rows = [
    [r"$e_{11}$", r"$1$", r"$0$", r"$1$"],
    [r"$e_{22}$", r"$0$", r"$\infty$", r"$\infty$"],
    [r"$1_M$", r"$1$", r"$\infty$", r"$\infty$"],
    [r"$vv^*,\ v=\delta_1+\delta_2$", r"$1$", r"$\infty$", r"$\infty$"],
]
table = ax.table(cellText=rows, colLabels=columns, cellLoc="center",
                 colWidths=[.44, .15, .22, .19], bbox=[.056, .078, .881, .27])
table.auto_set_font_size(False)
table.set_fontsize(15)
for (r, c), cell in table.get_celld().items():
    cell.set_edgecolor("#C7D4DF")
    cell.set_facecolor("#E9EFF5" if r == 0 else "white")
    if r == 0:
        cell.set_text_props(weight="bold", color="#17293A")
ax.text(.82, .2, "Exact example WS19 and WS20. Repetition gives infinity; no finite truncation is depicted.",
        fontsize=11.5, color=GREY)
fig.savefig(ASSETS / "normal-weight-sum-domain.png", dpi=180,
            metadata={"Software": "CC0 original WS-6 figure"})
fig.savefig(ASSETS / "normal-weight-sum-domain.svg",
            metadata={"Date": None, "Creator": "CC0 original WS-6 figure"})
plt.close(fig)
data = {
    "proof": "NORMAL_WEIGHT_SUM_PROOF.md#oa-flow.weight-sum.ws6",
    "equations": ["WS19", "WS20"],
    "dimension": 2,
    "algebra": "M_2(C)",
    "e": [[1, 0], [0, 0]],
    "q": [[0, 0], [0, 1]],
    "gns": {"finite_ideal": "M e", "Lambda_x": "x delta_1", "H": "C^2", "pi": "identity"},
    "functionals": {"g": "a_11", "h_n": "a_22 for every n>=1",
                    "t_g": "I_H", "t_h_n": "0"},
    "samples": [
        {"a": [[1, 0], [0, 0]], "g": 1, "sum_h": 0, "phi": 1},
        {"a": [[0, 0], [0, 1]], "g": 0, "sum_h": "infinity", "phi": "infinity"},
        {"a": [[1, 0], [0, 1]], "g": 1, "sum_h": "infinity", "phi": "infinity"},
        {"a": [[1, 1], [1, 1]], "g": 1, "sum_h": "infinity", "phi": "infinity"},
    ],
    "scope": "proved nonsemifinite matrix example; no assertion of WS-FR or the general sum theorem",
    "license": "CC0-1.0 to the extent of rights held",
}
(HERE / "figure-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"assets": [str(ASSETS / "normal-weight-sum-domain.png"),
                            str(ASSETS / "normal-weight-sum-domain.svg")]}))

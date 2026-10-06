"""Reproduce exact coordinate partition and faithful-state tail mechanism."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = Path(__file__).resolve().parent
(D / "assets").mkdir(exist_ok=True)
matplotlib.rcParams["svg.hashsalt"] = "oa-projection-comparison-20261004"
colors = ["#176d80", "#bd6b24", "#6b4991", "#39815b", "#a24253", "#57759b"]
coords = list(range(32))
def valuation(n):
    j = 0
    while n % 2 == 0:
        j += 1
        n //= 2
    return j
rows = [valuation(n+1) for n in coords]
N = list(range(7))
tail = [Fraction(1, 2**(2**n)-1) for n in N]
assert all((n+1) % 2**rows[n] == 0 and ((n+1)//2**rows[n]) % 2 == 1 for n in coords)
assert tail[2] > Fraction(1,100) > tail[3]

fig, axs = plt.subplots(1, 2, figsize=(15, 6), layout="constrained")
fig.suptitle("Countable equivalent copies can fill the unit and leave small nonzero tails",
             fontsize=17, fontweight="bold")
ax = axs[0]
ax.set_title(r"Exact coordinate partition in $B(\ell^2(\mathbb{N}_0))$", fontsize=13)
for j in range(6):
    xs = [n for n in coords if rows[n] == j]
    ax.scatter(xs, [j]*len(xs), marker="s", s=110, c=colors[j], zorder=3)
ax.set_xlim(-1, 32)
ax.set_ylim(-.6, 5.7)
ax.set_xticks(list(range(0, 32, 4)))
ax.set_xticks(coords, minor=True)
ax.set_yticks(range(6), [rf"$q_{j}$" for j in range(6)])
ax.set_xlabel(r"Basis coordinate $n$; exactly one $q_j$ keeps $\delta_n$", fontsize=11)
ax.set_ylabel("Projection coordinate set", fontsize=11)
ax.grid(axis="x", which="minor", alpha=.10)
ax.grid(axis="y", alpha=.20)
ax.axhspan(2.5, 5.6, color="#edf3f0", zorder=0)
ax.text(.02, .95, r"$R_3$ keeps the rows $j\geq3$ (shaded).",
        transform=ax.transAxes, fontsize=11, va="top",
        bbox=dict(boxstyle="round,pad=.4", fc="white", ec="#b8c9ce"))
ax.text(.5, -.22,
        r"$V_j\delta_k=\delta_{\,2^j(2k+1)-1},\quad V_j^*V_j=1,\quad q_j=V_jV_j^*$"
        "\n" r"$\sum_{j\geq0}q_j=1,\quad q_j\sim1;\quad 0\leq n\leq31$ plotted.",
        transform=ax.transAxes, ha="center", va="top", fontsize=12)

ax = axs[1]
vals = [float(x) for x in tail]
ax.set_title("A faithful normal state makes every filling tail small", fontsize=13)
ax.plot(N, vals, "o-", c="#176d80", lw=2.4, ms=7,
        label=r"$\rho(R_N)=1/(2^{2^N}-1)$")
ax.axhline(.01, c="#bd6b24", lw=1.8, ls="--", label=r"$\varepsilon=1/100$")
ax.set_yscale("log")
ax.set_xticks(N)
ax.set_ylim(1e-20, 12)
ax.set_xlabel(r"Tail index $N$, where $R_N=\sum_{j\geq N}q_j$", fontsize=11)
ax.set_ylabel(r"Exact state value $\rho(R_N)$ (logarithmic axis)", fontsize=11)
ax.grid(axis="y", alpha=.20)
ax.legend(fontsize=11, loc="lower left")
for n in range(4):
    ax.annotate(str(tail[n]), (n, vals[n]), xytext=(6, 10),
                textcoords="offset points", fontsize=11)
ax.text(.97, .82, r"$\rho(R_3)=1/255<1/100$"
        "\n" r"$R_N\neq0,\quad R_N\sim1\quad(N\geq0)$",
        transform=ax.transAxes, ha="right", va="top", fontsize=12,
        bbox=dict(boxstyle="round,pad=.5", fc="#f8fafb", ec="#b8c9ce"))
ax.text(.5, -.22,
        r"$\rho(x)=\sum_{n\geq0}2^{-(n+1)}\langle x\delta_n,\delta_n\rangle$"
        "\n" "This exact type I example illustrates the mechanism; PC-8 proves the type III case.",
        transform=ax.transAxes, ha="center", va="top", fontsize=11)

fig.savefig(D/"assets/projection-tail-mechanism.png", dpi=170, bbox_inches="tight",
            metadata={"Software":"OA-FLOW original reproducible figure"})
fig.savefig(D/"assets/projection-tail-mechanism.svg", bbox_inches="tight",
            metadata={"Date":None, "Creator":"OA-FLOW original reproducible figure"})
plt.close(fig)
(D/"figure-data.json").write_text(json.dumps({
    "coordinate_sample":coords, "unique_projection_indices":rows,
    "tail_indices":N, "exact_tail_fractions":[str(x) for x in tail],
    "epsilon":"1/100", "first_selected_tail_below_epsilon":3,
    "formula":"S_j={2^j(2k+1)-1:k>=0}; rho(R_N)=1/(2^(2^N)-1)",
    "proof_locators":["PC-8","PC9","PC10"],
    "domain":"B(l2(N_0)); illustrated algebra is type I, not type III",
    "license":"CC0-1.0 to the extent of rights held"
},indent=2)+"\n",encoding="utf-8")

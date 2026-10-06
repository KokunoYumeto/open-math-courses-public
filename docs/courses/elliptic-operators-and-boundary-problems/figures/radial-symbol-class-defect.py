"""Exact U039 symbol-class defect and operator-ideal regimes.

Written and dedicated to the public domain by Codex, October 2026 (CC0).
The complete programme proofs are RS30--RS34 of the associated lesson.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
                     "svg.hashsalt": "an03-u039-symbol-class-defect-264"})
fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
fig.subplots_adjust(left=.025, right=.975, bottom=.025, top=.975)
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.axis("off")
ax.text(.5, .96, "The exact class defect persists through all three operator ideals",
        ha="center", va="top", fontsize=15)
nodes = [(.17, r"$S(1,g)$"), (.50, r"$S(1,G)$"), (.83, r"$\mathcal{Q}$")]
for x, label in nodes:
    ax.text(x, .785, label, ha="center", va="center", fontsize=19,
            bbox={"boxstyle": "round,pad=.45", "fc": "#e9eff7", "ec": "#526b83"})
for x1, x2, label in [(.23, .44, r"$\iota$"), (.56, .77, r"$\pi$")]:
    ax.annotate("", xy=(x2, .785), xytext=(x1, .785),
                arrowprops={"arrowstyle": "->", "lw": 1.7, "color": "#365777"})
    ax.text((x1+x2)/2, .84, label, ha="center", fontsize=15)
ax.text(.035, .785, r"$0$", ha="center", fontsize=15)
ax.annotate("", xy=(.11, .785), xytext=(.06, .785),
            arrowprops={"arrowstyle": "->", "lw": 1.4})
ax.text(.965, .785, r"$0$", ha="center", fontsize=15)
ax.annotate("", xy=(.94, .785), xytext=(.89, .785),
            arrowprops={"arrowstyle": "->", "lw": 1.4})
ax.text(.5, .69, r"$\iota u=u,\quad p_k(u;1,G)\leq p_k(u;1,g),\quad"
        r"\pi u=[u],\quad\mathcal{Q}=S(1,G)/\iota S(1,g)$",
        ha="center", fontsize=11.5)
ax.text(.5, .595,
        r"$v_\delta(x,\xi)=\zeta(x)e^{x_1}\langle\xi\rangle^{-\delta}I_\nu,"
        r"\quad\delta>0,\quad[v_\delta]\ne0$"
        "\n"
        r"$\zeta\geq0$ is compact and smooth, $\zeta=1$ near $x=0$; "
        "the diagram below uses n = 1.",
        ha="center", fontsize=11.5, linespacing=1.6)

x0, xunit = .31, .27
def px(delta):
    return x0+xunit*delta

for y, start, colour, label in [
    (.43, 0, "#486e9e", "Compact"),
    (.325, .5, "#59889c", "Hilbert–Schmidt"),
    (.22, 1, "#398363", "Trace class"),
]:
    ax.text(.265, y, label, ha="right", va="center", fontsize=12.5)
    ax.annotate("", xy=(px(2.25), y), xytext=(px(start), y),
                arrowprops={"arrowstyle": "->", "lw": 3.1, "color": colour})
    ax.plot([px(start)], [y], "o", ms=8, mfc="white", mec=colour, mew=1.6)
    ax.text(px(start)+.025, y+.03, r"$\delta>"+str(start)
            +r"$", color=colour, fontsize=11)
for delta in [0, .5, 1, 2]:
    ax.plot([px(delta), px(delta)], [.17, .46], color="#c5cbd3",
            lw=.8, linestyle=":", zorder=0)
    ax.text(px(delta), .125, str(delta), ha="center", fontsize=11)
ax.text(.94, .125, r"$\delta$", fontsize=14, ha="center")
ax.text(.5, .06,
        "Open circles exclude the threshold. Each arrow continues to larger exponents.\n"
        "RS31–RS34 prove exactness, the infinite-dimensional quotient and every ideal classification.",
        ha="center", fontsize=10.5, linespacing=1.3)
fig.savefig(ROOT/"radial-symbol-class-defect.png", dpi=200)
fig.savefig(ROOT/"radial-symbol-class-defect.svg",
            metadata={"Date": None, "Creator": "Codex; reproducible CC0 programme proof diagram"})
(ROOT/"radial-symbol-class-defect.parameters.json").write_text(json.dumps({
    "license": "CC0-1.0",
    "source": "Complete original programme proofs RS30--RS34.",
    "configuration_dimension_in_chart": 1,
    "original_symbols": "zeta(x)*exp(x_1)*<xi>^(-delta)*I_nu",
    "zeta": "nonnegative compact smooth cutoff, one near x=0",
    "parameter_domain": "delta > 0",
    "compact": "delta > 0",
    "hilbert_schmidt": "delta > 1/2",
    "trace_class": "delta > 1",
    "quotient_class": "nonzero for every delta > 0",
    "quotient_type": "algebraic vector quotient; no closed-range assertion",
    "exact_sequence": "0 -> S(1,g) -> S(1,G) -> Q -> 0",
    "all_positive_exponent_distinct_classes": "every finite subset is linearly independent",
    "shown_exponent_ticks": [0, .5, 1, 2],
    "open_boundaries": True,
    "arrows_continue_right": True,
    "proof_locators": ["RS31", "RS33", "RS34"],
}, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
plt.close(fig)

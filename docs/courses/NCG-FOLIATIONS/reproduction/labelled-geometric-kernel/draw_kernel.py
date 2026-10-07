"""CC0 reproducible labelled-kernel figure, exact data with declared samples."""
from pathlib import Path
import argparse
import json
import math
import os

HERE = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(HERE / "runtime-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyBboxPatch
from finite_checks import fibonacci

REG = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans-Bold.ttf"))
INK, BLUE, GREEN, RED = "#17354b", "#165f92", "#08795e", "#b44639"


def txt(ax, x, y, value, size=13, bold=False, **kw):
    return ax.text(x, y, value, fontsize=size,
                   fontproperties=BOLD if bold else REG,
                   color=kw.pop("color", INK), **kw)


def box(ax, x, y, w, h, value, size=12):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                              boxstyle="round,pad=.012", facecolor="#edf5f9",
                              edgecolor=BLUE, linewidth=1.4))
    txt(ax, x, y, value, size, True, ha="center", va="center")


def arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 1.8})


def render(out):
    plt.rcParams.update({"svg.hashsalt": "labelled-geometric-kernel-gk2-gk8",
                         "axes.edgecolor": INK, "axes.labelcolor": INK,
                         "xtick.color": INK, "ytick.color": INK})
    out.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(16, 10), facecolor="white")
    title = fig.add_axes([.04, .91, .92, .07]); title.axis("off")
    txt(title, .0, .65, "Return jets can converge while arrow labels escape", 22, True)
    txt(title, .0, .13, "Actual irrational-rotation holonomy; original anchor T = R/Z.  GK.1–GK.8", 14)
    alpha = (math.sqrt(5)-1)/2

    ax = fig.add_axes([.05, .49, .32, .38]); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.45, 2.05); ax.set_ylim(-1.3, 1.35)
    ax.add_patch(Circle((0, 0), 1, fill=False, color=BLUE, lw=2))
    ax.plot([1], [0], "o", color=INK, ms=7)
    txt(ax, 1.12, .08, "x = 0\nunit arrow label 0", 12)
    samples = []
    for m, lab_y in ((4, -.66), (8, -.27), (12, .65)):
        n = fibonacci(m)
        error = (-1)**(m-1)*alpha**m
        v = (math.cos(2*math.pi*error), math.sin(2*math.pi*error))
        ax.plot([v[0]], [v[1]], "o", color=GREEN, ms=7)
        ax.annotate(f"F{m} = {n}\nreturn error −α^{m}", xy=v, xytext=(-1.3, lab_y),
                    fontproperties=REG, fontsize=11, color=GREEN,
                    arrowprops={"arrowstyle": "->", "color": GREEN})
        samples.append({"m": m, "label": n,
                        "return_error_exact": f"(-1)^({m}-1)*alpha^{m}",
                        "return_error_sample": error,
                        "circle_coordinates_sample": list(v)})
    txt(ax, -1.35, -1.19, "Metric dx²; derivative 1 for every labelled arrow", 11)

    graph = fig.add_axes([.45, .51, .49, .33])
    ms = list(range(2, 19))
    ns = [fibonacci(m) for m in ms]
    label_kernel = [n*n for n in ns]
    # Evaluate by the exact reduced return error, avoiding large-angle error.
    jet_kernel = [4*math.sin(math.pi*alpha**m)**2 for m in ms]
    graph.semilogy(ms, label_kernel, "o-", color=GREEN, lw=2, label="label kernel Fₘ²")
    graph.semilogy(ms, jet_kernel, "o-", color=RED, lw=2, label="jet kernel 4 sin²(πFₘα)")
    graph.set_xticks([2, 4, 8, 12, 16, 18])
    graph.set_xlabel("Fibonacci index m", fontproperties=REG, fontsize=12)
    graph.set_ylabel("squared displacement (log scale)", fontproperties=REG, fontsize=12)
    graph.grid(True, which="both", alpha=.18)
    graph.legend(prop=REG, loc="upper left", fontsize=12)
    for label in graph.get_xticklabels()+graph.get_yticklabels(): label.set_fontproperties(REG)
    graph.set_title("α = (√5−1)/2; exact identity Fₘα−Fₘ₋₁ = (−1)ᵐ⁻¹αᵐ", fontproperties=BOLD, fontsize=12)

    ax2 = fig.add_axes([.05, .13, .90, .29]); ax2.set_xlim(0, 1); ax2.set_ylim(0, 1); ax2.axis("off")
    txt(ax2, 0, .96, "The proved compact-fibre construction requires the actual labelled coarse input", 16, True)
    box(ax2, .13, .61, .23, .30, "k on G ×ₛ G\ncontinuous CND\nuniform upper/lower control")
    box(ax2, .43, .61, .23, .30, "A ⊂ C_b(G)\nY = Spec(A)\np:Y → T proper, onto")
    box(ax2, .76, .61, .30, .30, "G ⋉ Y with ψ\ncontinuous, CND, proper\n||b(g,y)||² = ψ(g,y)")
    arrow(ax2, (.26, .61), (.30, .61)); arrow(ax2, (.56, .61), (.60, .61))
    txt(ax2, .13, .34, "GK.4: geometric input", 12, ha="center")
    txt(ax2, .43, .34, "GK.5: y₀(x) = ev₁ₓ", 12, ha="center")
    txt(ax2, .76, .34, "GK.6–GK.7: exact affine cocycle", 12, ha="center")
    txt(ax2, 0, .16, "GK.8 supplies actual actions; EG/EK in Section 11AF prove the general eligible-holonomy input.", 13, color=RED)
    txt(ax2, 0, .025, "At label 55: derivative = 1, determinant phase = 1, inverse central phase = −1. The full coefficient is retained.", 12)
    caption = fig.add_axes([.04, .01, .92, .08]); caption.axis("off")
    txt(caption, 0, .78, "Circle coordinates and graph values are numerical samples of the exact displayed identities; the lower panel is a typed schematic.", 11)
    txt(caption, 0, .35, "Neither bounded jet geometry nor this finite illustration proves general pseudogroup globalization. Proof: GK.2, GK.4–GK.9.", 11)

    notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
    desc = "Original CC0 figure. Exact proof locators GK.2, GK.4-GK.9.\n"+notice
    fig.savefig(out / "labelled-geometric-kernel.png", dpi=150,
                metadata={"Title": "Labelled geometric kernel", "Description": desc})
    fig.savefig(out / "labelled-geometric-kernel.svg",
                metadata={"Title": "Labelled geometric kernel", "Description": desc, "Date": None})
    plt.close(fig)
    data = {"schema": "labelled-geometric-kernel-figure/v1",
            "alpha_exact": "(sqrt(5)-1)/2", "metric_exact": "dx^2 on R/Z",
            "fibonacci_identity": "F_m*alpha-F_(m-1)=(-1)^(m-1)*alpha^m",
            "circle_samples": samples,
            "graph_samples": [{"m": m, "label": n, "label_kernel_exact": n*n,
                               "jet_kernel_exact": f"4*sin(pi*alpha^{m})^2",
                               "jet_kernel_sample": j}
                              for m, n, j in zip(ms, ns, jet_kernel)],
            "inverse_character_55": {"central_exponent_mod_10": 5,
                                     "determinant_exponent_mod_10": 0,
                                     "derivative": 1},
            "schematic_scope": "GK.4 conditional input; GK.5-GK.7 proved implication; GK.8 actual actions; GK.9 general eligible geometry proved by EG/EK in Section 11AF",
            "proof_locators": ["GK.2", "GK.4", "GK.5", "GK.6", "GK.7", "GK.8", "GK.9"]}
    (out / "labelled-geometric-kernel-data.json").write_text(
        json.dumps(data, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"png": str(out / "labelled-geometric-kernel.png"),
                      "samples": len(ms)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "figures")
    render(parser.parse_args().out)

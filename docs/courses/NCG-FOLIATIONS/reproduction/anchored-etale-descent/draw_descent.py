"""Original CC0 typed diagram for actual anchored etale descent, DS.1--DS.23."""
from pathlib import Path
import os
import argparse
import json

HERE = Path(__file__).resolve().parent
os.environ["MPLCONFIGDIR"] = str(HERE / "runtime-cache")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch

REG = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans-Bold.ttf"))
INK, BLUE, GREEN, PALE = "#17354b", "#165f92", "#08795e", "#edf5f9"


def txt(ax, x, y, value, size=15, bold=False, **kw):
    return ax.text(x, y, value, fontsize=size, color=kw.pop("color", INK),
                   fontproperties=BOLD if bold else REG, **kw)


def arrow(ax, start, end, color=BLUE):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 2.2, "color": color})


def box(ax, x, y, width, height, value, size=15):
    ax.add_patch(FancyBboxPatch((x-width/2, y-height/2), width, height,
                              boxstyle="round,pad=.009", facecolor=PALE,
                              edgecolor=BLUE, linewidth=1.6))
    txt(ax, x, y, value, size, True, ha="center", va="center")


def panel(fig, rect):
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def render(out):
    out.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({"svg.hashsalt": "actual-anchored-etale-descent-DS-20261006",
                                "svg.fonttype": "path"})
    fig = plt.figure(figsize=(18, 12), facecolor="white")
    fig.text(.04, .956, "Descent retains the actual arrows, coefficient modules and products",
             fontproperties=BOLD, fontsize=23, color=INK)
    fig.text(.04, .923, "Hausdorff second-countable LCH étale G ⇉ T; all original coefficients and cycles are C₀(T)-linear.",
             fontproperties=REG, fontsize=14, color=INK)

    a = panel(fig, [.045, .565, .425, .33])
    txt(a, 0, .94, "DS.1 / DS.13   Range-fibre tensor sum", 18, True)
    pos = {"x": (.15, .37), "y": (.82, .37), "z": (.48, .70)}
    for label, point in pos.items():
        a.scatter([point[0]], [point[1]], s=55, color=INK)
        txt(a, point[0], point[1]-.09, label, 16, True, ha="center")
    arrow(a, (.19, .42), (.43, .66))
    arrow(a, (.78, .42), (.53, .66))
    arrow(a, (.20, .37), (.77, .37), GREEN)
    txt(a, .14, .64, "g : x → z", 14)
    txt(a, .65, .64, "h : y → z", 14)
    txt(a, .48, .30, "k = h⁻¹g : x → y", 14, True, ha="center")
    txt(a, .01, .13, "r(h) = r(g) = z;  ξ(h) ∈ E₁,z;  η(k) ∈ E₂,y.", 14)
    txt(a, .01, .025, "U₂,h transports η(k) into E₂,z before tensor balancing.", 13)

    b = panel(fig, [.535, .565, .425, .33])
    txt(b, 0, .94, "DS.6–DS.8   Reduced source-column matrix", 18, True)
    box(b, .14, .64, .22, .16, "source x", 14)
    box(b, .67, .77, .26, .14, "g : x → z", 14)
    box(b, .67, .48, .26, .14, "l : x → y", 14)
    arrow(b, (.27, .67), (.52, .77))
    arrow(b, (.27, .61), (.52, .48))
    txt(b, .49, .62, "gl⁻¹ : y → z", 14, True)
    txt(b, 0, .29, "entry (g,l) = πₓ(αg⁻¹(a(gl⁻¹))) : Eₓ → Eₓ", 15, True)
    txt(b, 0, .15, "The PN regular coefficient is represented on Eₓ.", 14)
    txt(b, 0, .025, "‖Λπ,r(a)‖ ≤ ‖λA(a)‖; finite matrices cover degenerate πₓ.", 13)

    fig.text(.06, .525, "Wτ(ξ ⊗ η)(g) = Σr(h)=r(g) ξ(h) ⊗ U₂,h η(h⁻¹g)",
             fontproperties=BOLD, fontsize=18, color=GREEN)
    fig.text(.06, .497, "Exact inner-product identity gives an even onto unitary for τ = full or reduced (DS.13–DS.14).",
             fontproperties=REG, fontsize=13, color=INK)

    c = panel(fig, [.045, .115, .425, .325])
    txt(c, 0, .96, "DS.3 / DS.17   Compact extension and positivity", 17, True)
    box(c, .22, .76, .37, .14, "K_B(E)", 16)
    box(c, .78, .76, .40, .14, "K_Bτ(XE,τ)", 16)
    arrow(c, (.42, .76), (.56, .76), GREEN)
    txt(c, .5, .865, "K ↦ K ⊗ 1", 13, True, ha="center")
    txt(c, .02, .58, "θeb,fc ⊗ 1 = θ(e ⊗ iB b),(f ⊗ iB c)", 14, True)
    txt(c, .02, .47, "iB(B) lies in Bτ, so both rank-one vectors are actual.", 13)
    box(c, .22, .29, .37, .13, "L(E) / K(E)", 13)
    box(c, .78, .29, .40, .13, "L(XE,τ) / K(XE,τ)", 12)
    arrow(c, (.42, .29), (.56, .29), GREEN)
    txt(c, .5, .405, "positivity", 12, True, ha="center")
    txt(c, .02, .10, "z iA(an) → z transfers the product compression to Λ(z).", 12.5)
    txt(c, .02, .01, "The closed positive cone gives DS.17 on both completions.", 12.5)

    d = panel(fig, [.535, .115, .425, .325])
    txt(d, 0, .96, "DS.20–DS.21   The coefficient quotient square", 17, True)
    for x, y, label in [(.18, .73, "A_m"), (.79, .73, "B_m"),
                         (.18, .29, "A_r"), (.79, .29, "B_r")]:
        box(d, x, y, .21, .12, label, 17)
    arrow(d, (.30, .73), (.66, .73), GREEN)
    arrow(d, (.30, .29), (.66, .29), GREEN)
    arrow(d, (.18, .65), (.18, .38))
    arrow(d, (.79, .65), (.79, .38))
    txt(d, .49, .83, "jm(x)", 14, True, ha="center")
    txt(d, .49, .16, "jr(x)", 14, True, ha="center")
    txt(d, .06, .49, "[qA]", 13, True)
    txt(d, .84, .49, "[qB]", 13, True)
    txt(d, .485, .49, "commutes in KK(A_m,B_r)", 12.5, True, ha="center")
    txt(d, 0, .005, "XE,m ⊗qB B_r ≅ XE,r; the operator is the same pointwise F.", 12.5)

    fig.text(.045, .064, "Typed schematic, not a geometric model of G. Complete proofs: DS.1–DS.23; product existence input: anchored KG.1–KG.4.",
             fontproperties=REG, fontsize=12, color=INK)
    fig.text(.045, .043, "Original CC0 diagram. Human-source orientation: Alistair Miller, Functors between Kasparov categories from étale groupoid correspondences, §2.4.",
             fontproperties=REG, fontsize=10.5, color=INK)
    notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
    fig.savefig(out / "anchored-etale-descent.png", dpi=200,
                metadata={"Software": "Matplotlib; original CC0 typed diagram", "Description": notice})
    fig.savefig(out / "anchored-etale-descent.svg",
                metadata={"Date": None, "Creator": "Original CC0 anchored etale descent diagram", "Description": notice})
    plt.close(fig)
    data = {"proof_locators": ["DS.1", "DS.3", "DS.6", "DS.7", "DS.8", "DS.13", "DS.14", "DS.17", "DS.20", "DS.21", "DS.23"],
            "standing_scope": "Hausdorff second-countable locally compact etale groupoids; original C0(T) anchors",
            "range_sum": {"g": "x->z", "h": "y->z", "h^-1g": "x->y", "common_range": "z",
                          "xi_h_fibre": "E1_z", "eta_hinv_g_fibre": "E2_y", "transported_eta_fibre": "E2_z"},
            "source_matrix": {"g": "x->z", "l": "x->y", "g l^-1": "y->z",
                              "entry": "pi_x(alpha_g^-1(a(g l^-1)))", "domain": "E_x", "codomain": "E_x"},
            "compact_extension": "theta_(e b),(f c) tensor 1 = theta_(e tensor i_B b),(f tensor i_B c)",
            "quotient_square": "[q_A] tensor j_r(x) = j_m(x) tensor [q_B] in KK(A_m,B_r)",
            "module_base_change": "X_E,m tensor_(B_m,q_B) B_r is isomorphic to X_E,r",
            "diagram_coordinates": "Normalized page layout only, no mathematical metric coordinates asserted",
            "not_inferred": ["reduced exactness", "global norm-continuity of unlocalized F", "coefficient-free quotient inverse", "original-unit Dirac factors"],
            "product_existence_provider": "ANCHORED-KK-FOUNDATIONS.md KG.1-KG.4"}
    (out / "anchored-etale-descent-data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=HERE / "figures")
    render(parser.parse_args().output_dir.resolve())

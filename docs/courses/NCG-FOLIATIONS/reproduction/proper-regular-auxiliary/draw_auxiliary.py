"""Original CC0 diagram of RA.2--RA.18 and the invariant-section lemma.

All text uses the two bundled, unmodified DejaVu Sans fonts. Glyph terms
are retained in both outputs. No mathematical source-page pixels are used.
"""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager

HERE = Path(__file__).resolve().parent
for name in ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf"):
    fontManager.addfont(str(HERE / "fonts" / name))
REG = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(HERE / "fonts" / "DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype": "path", "svg.hashsalt": "regular-auxiliary-v1"})
BLUE = "#175d76"
ORANGE = "#a94c15"


def text(ax, x, y, s, size=12, bold=False, **kwargs):
    return ax.text(x, y, s, fontsize=size,
                   fontproperties=BOLD if bold else REG, **kwargs)


def arrow(ax, a, b, color=BLUE):
    ax.annotate("", xy=b, xytext=a,
                arrowprops={"arrowstyle": "->", "lw": 2, "color": color})


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", default=str(HERE / "figures"))
    out = Path(p.parse_args().output_dir)
    out.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(15.4, 10.6))
    fig.subplots_adjust(left=.055, right=.985, top=.845, bottom=.075,
                        wspace=.15, hspace=.29)
    fig.suptitle("Regular norm, scalar index and equivariant class are separate interfaces",
                 y=.975, fontsize=19, fontproperties=BOLD)
    fig.text(.5, .93, "An exact reduced replacement preserves the ordinary normal class when the auxiliary unit index is +1.",
             ha="center", fontsize=12, fontproperties=REG)
    for ax in axes.flat:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
    a, b, c, d = axes.flat

    text(a, 0, 1.02, "A. Exact regular diagonal map (RA.2–RA.5)", 14, True)
    text(a, .17, .84, "A ⋊ᵣ Γ", 17, True, ha="center")
    text(a, .78, .84, "(A ⋊ₘ Γ) ⊗ C*ᵣΓ", 16, True, ha="center")
    arrow(a, (.32, .85), (.56, .85))
    text(a, .44, .91, "Δᵣ", 13, True, ha="center")
    text(a, .5, .66, "a_g u_g ↦ a_g u_g ⊗ λ_g", 15, ha="center")
    text(a, .5, .48, "W(ξ ⊗ δ_h) = U_h⁻¹ξ ⊗ δ_h", 14, ha="center")
    text(a, .5, .34, "W(U_g ⊗ λ_g)W* = 1 ⊗ λ_g", 14, ha="center")
    text(a, .5, .17, "‖Δᵣ(p)‖ = ‖p‖ᵣ for every finite polynomial p", 12, True, ha="center")
    text(a, .5, .035, "The original geometric representation need not be reduced.", 11, ha="center")

    text(b, 0, 1.02, "B. The precise preserved restriction (RA.6–RA.11)", 14, True)
    text(b, .5, .86, "κ([1]) = +1   ⇒   dᵣ = Δᵣ*(dₘ ⊠ κ)", 15, True, ha="center")
    text(b, .5, .68, "iᵣ*dᵣ = iₘ*dₘ   in ordinary KK(A, ℂ)", 14, ha="center")
    text(b, .5, .53, "Original local Bott product: +1", 13, True, ha="center", color=BLUE)
    text(b, .5, .36, "Normal phase: z⁻¹; determinant: z⁻²", 13, ha="center")
    text(b, .5, .23, "Πᵏ C_q; generators (−1)ᵏ⁺¹ L_tⱼ; k = q(q−1)/2", 12, ha="center")
    text(b, .5, .08, "Equivariant equality needs dᴳ_N ⊗ e_κ = dᴳ_N.", 12, True, ha="center", color=ORANGE)

    text(c, 0, 1.02, "C. An invariant metric section is a compact witness", 14, True)
    c.add_patch(plt.Rectangle((.17, .43), .64, .42,
                             facecolor="#f3f6f8", edgecolor="#9baeb9"))
    c.plot([.21, .77], [.61, .61], color=BLUE, lw=4)
    text(c, .48, .71, "s(N) = {g_n : n ∈ N}", 13, ha="center")
    for x in (.30, .47, .64):
        c.add_patch(plt.Circle((x, .61), .015, color=BLUE))
        arrow(c, (x-.055, .47), (x, .59), ORANGE)
    text(c, .91, .65, "P", 16, True, ha="center")
    text(c, .5, .35, "m(γ,p) = (γp,p)", 13, ha="center")
    text(c, .5, .21, "m⁻¹(s(N) × s(N)) = Γ × s(N)", 13, True, ha="center")
    text(c, .5, .09, "Infinite Γ ⇒ noncompact inverse image ⇒ action not proper", 11, True, ha="center")
    text(c, .5, -.035, "Schematic section; three representative returns, not the whole metric fibre.", 10, ha="center")

    text(d, 0, 1.02, "D. Regular multiplicity and balanced confinement", 14, True)
    for i in range(4):
        y = .80-i*.11
        text(d, .14, y, "δ_g"+str(i+1), 12, ha="center")
        arrow(d, (.25,y), (.48,y))
        text(d, .74, y, "Kv ⊗ δ_g"+str(i+1), 12, ha="center")
    text(d, .5, .31, "K ≠ 0: these images are orthogonal with fixed norm.", 11, ha="center")
    text(d, .5, .19, "K ⊗ 1 is not compact on an infinite regular factor.", 12, True, ha="center")
    text(d, .5, .055, "Paired proper length: eigenvalues ±(1 + ℓ(g)); index 0.", 11, True, ha="center", color=ORANGE)

    notice = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
    credit = "Original diagram and generator: CC0 1.0. Bundled glyph terms follow.\n" + notice
    fig.savefig(out / "regular-auxiliary.png", dpi=150,
                metadata={"Software": "draw_auxiliary.py", "Description": credit})
    fig.savefig(out / "regular-auxiliary.svg",
                metadata={"Date": None, "Creator": "draw_auxiliary.py", "Description": credit})
    svg=out / "regular-auxiliary.svg"
    svg.write_text(svg.read_text(encoding="utf-8"),encoding="utf-8",newline="\n")
    plt.close(fig)


if __name__ == "__main__":
    main()

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


OUT = Path(__file__).with_suffix(".png")


def main() -> None:
    fig, (ax0, ax1) = plt.subplots(
        1,
        2,
        figsize=(14, 6.5),
        gridspec_kw={"width_ratios": [1.0, 1.35]},
    )
    fig.patch.set_facecolor("#fbfaf6")

    ax0.set_aspect("equal")
    ax0.set_xlim(-1.35, 1.35)
    ax0.set_ylim(-1.35, 1.35)
    ax0.axis("off")
    ax0.add_patch(Circle((0, 0), 1.0, facecolor="#e4eef6", edgecolor="#2b5d7d", lw=2.2))
    ax0.add_patch(Circle((0, 0), 0.58, facecolor="#fbfaf6", edgecolor="#2b5d7d", lw=2.0))
    ax0.text(0, 0.08, r"$\chi_R=\varphi_R^8=1$", ha="center", fontsize=15)
    ax0.text(0, -0.15, r"fixed ball, then $R\to\infty$", ha="center", fontsize=11)
    ax0.text(0, 0.78, r"transition annulus", ha="center", fontsize=14, color="#193f56")
    ax0.text(
        0,
        0.62,
        r"$\nabla\chi_R=8R^{-1}\varphi_R^7(\nabla\varphi)(x/R)$",
        ha="center",
        fontsize=11,
        color="#193f56",
    )
    ax0.add_patch(
        FancyArrowPatch(
            (-0.88, -0.52),
            (-1.22, -0.84),
            arrowstyle="-|>",
            mutation_scale=15,
            lw=1.8,
            color="#9b3a2c",
        )
    )
    ax0.text(-1.22, -1.02, r"pressure and transport flux", ha="center", fontsize=11, color="#7b2d23")
    ax0.set_title("Where every cutoff error is produced", fontsize=16, pad=14)

    ax1.axis("off")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    rows = [
        (0.90, r"local Riesz terms", r"$R^{-1}A_R^{3/2}$ and $R^{-1}A_R^{1/2}$", "#2b5d7d"),
        (0.72, r"commutator kernel", r"$\|K_R\|_{4/3}=C R^{-3/4}$", "#72549a"),
        (0.54, r"commutator flux", r"$R^{-7/4}A_R^{3/4}$", "#72549a"),
        (0.34, r"Young remainders", r"$R^{-4},\ R^{-4/3},\ R^{-14/5}$", "#9b3a2c"),
        (0.14, r"dominant expanding-cutoff error", r"$C_T R^{-4/3}$", "#9b3a2c"),
    ]
    for y, label, formula, color in rows:
        ax1.text(0.03, y, label, fontsize=12, color="#252525", va="center")
        ax1.text(0.98, y, formula, fontsize=14, color=color, ha="right", va="center")
        if y > 0.15:
            ax1.add_patch(
                FancyArrowPatch(
                    (0.72, y - 0.055),
                    (0.72, y - 0.125),
                    arrowstyle="-|>",
                    mutation_scale=13,
                    lw=1.4,
                    color="#666666",
                )
            )
    ax1.text(
        0.5,
        0.015,
        "Proof: lemma_10_5_reaudit.md (14)–(45); OpenAI, Lemma 10.5, pp. 121–123",
        ha="center",
        fontsize=9,
        color="#444444",
    )
    ax1.set_title("Exact powers retained through absorption", fontsize=16, pad=14)

    fig.suptitle("Whole-space comparison: cutoff geometry and the retained remainder", fontsize=18, y=0.98)
    fig.tight_layout(rect=(0, 0.02, 1, 0.94))
    fig.savefig(OUT, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    fig.savefig(OUT.with_suffix(".svg"), bbox_inches="tight", facecolor=fig.get_facecolor())
    print(OUT.name)


if __name__ == "__main__":
    main()

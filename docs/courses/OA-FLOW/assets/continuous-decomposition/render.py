"""Render the exact countable-absorption coordinate diagram.

Original figure and renderer: CC0-1.0 to the extent of rights held.
Requires Python 3 and Matplotlib. Run this file from any working directory.
The formulas prove the bijection; the finite checks below validate diagram data.
"""

from pathlib import Path
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle


OUT = Path(__file__).resolve().parent


def beta(j, k):
    assert j >= 0 and k >= 0
    return (2**j) * (2*k + 1) - 1


def inverse(n):
    assert n >= 0
    odd = n + 1
    j = 0
    while odd % 2 == 0:
        odd //= 2
        j += 1
    return j, (odd - 1) // 2


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(4096):
        assert beta(*inverse(n)) == n
    for j in range(10):
        for k in range(64):
            assert inverse(beta(j, k)) == (j, k)
    assert beta(1, 2) == 9 and beta(2, 1) == 11

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 14,
        "mathtext.fontset": "dejavusans",
        "svg.fonttype": "none",
        "savefig.facecolor": "#f8fafc",
    })
    blue, orange = "#1662a2", "#b24e0f"
    ink, muted = "#14283d", "#475569"
    fig = plt.figure(figsize=(16, 7.2), facecolor="#f8fafc")
    fig.text(.045, .935, "Countable absorption: an exact coordinate map",
             fontsize=25, weight="bold", color=ink)
    fig.text(.045, .88,
             r"$\beta(j,k)=2^j(2k+1)-1$     and     "
             r"$U(\delta_k\otimes\delta_j)=\delta_{\beta(j,k)}$",
             fontsize=21, color=ink)

    left = fig.add_axes([.045, .22, .49, .55])
    left.set_xlim(-.8, 6)
    left.set_ylim(-.1, 5)
    left.axis("off")
    left.text(-.7, 4.85, "FINITE SAMPLE OF THE PARTITION", fontsize=14,
              weight="bold", color=muted)
    left.text(-.6, 4.15, r"$j\backslash k$", color=muted, fontsize=17,
              ha="center", va="center")
    for k in range(6):
        left.text(k+.5, 4.15, str(k), fontsize=17, color=muted,
                  ha="center", va="center")
    for j in range(4):
        y = 3-j
        left.text(-.6, y+.45, str(j), fontsize=17, color=muted,
                  ha="center", va="center")
        for k in range(6):
            n = beta(j, k)
            color = blue if n == 11 else orange if n == 9 else ink
            fill = "#dceefe" if n == 11 else "#ffebd8" if n == 9 else "#e9eef5"
            left.add_patch(Rectangle((k+.035, y+.035), .93, .83,
                                     facecolor=fill, edgecolor="white", lw=1.5))
            left.text(k+.5, y+.45, str(n), fontsize=21, color=color,
                      ha="center", va="center", weight="bold" if n in (9, 11) else "normal")
    left.text(-.65, -.08, "Rows and columns continue; the formula covers every n ≥ 0.",
              fontsize=12, color=muted, va="top")

    right = fig.add_axes([.575, .22, .385, .55])
    right.set_xlim(0, 1)
    right.set_ylim(0, 1)
    right.axis("off")
    right.text(0, .97, "ONE MATRIX UNIT, TWO COORDINATES", fontsize=14,
               weight="bold", color=muted)
    right.text(.18, .82, "SOURCE", ha="center", color=blue, fontsize=12,
               weight="bold")
    right.text(.83, .82, "DESTINATION", ha="center", color=orange,
               fontsize=12, weight="bold")
    right.text(.18, .68, r"$\delta_1\otimes\delta_2$", ha="center",
               va="center", fontsize=24, color=blue)
    right.text(.83, .68, r"$\delta_2\otimes\delta_1$", ha="center",
               va="center", fontsize=24, color=orange)
    right.annotate("", xy=(.66, .68), xytext=(.35, .68),
                   arrowprops=dict(arrowstyle="->", lw=2, color=ink))
    right.text(.5, .76, r"$E_{2,1}\otimes e_{1,2}$", ha="center",
               fontsize=19, color=ink)
    for x in (.18, .83):
        right.annotate("", xy=(x, .32), xytext=(x, .57),
                       arrowprops=dict(arrowstyle="->", lw=2, color=ink))
        right.text(x-.075, .445, r"$U$", fontsize=22, ha="center", color=ink)
    right.text(.18, .22, r"$\delta_{11}$", ha="center", va="center",
               fontsize=27, color=blue)
    right.text(.83, .22, r"$\delta_9$", ha="center", va="center",
               fontsize=27, color=orange)
    right.annotate("", xy=(.68, .22), xytext=(.32, .22),
                   arrowprops=dict(arrowstyle="->", lw=2, color=ink))
    right.text(.5, .295, r"$E_{9,11}$", ha="center", fontsize=22, color=ink)
    right.text(.5, .025, r"$\Xi(E_{2,1}\otimes e_{1,2})=E_{9,11}$",
               ha="center", fontsize=20, color=ink)

    fig.text(.045, .10,
             r"Inverse:  $\nu(n)=v_2(n+1),\quad "
             r"\kappa(n)=\left((n+1)/2^{\nu(n)}-1\right)/2,\quad "
             r"U^*\delta_n=\delta_{\kappa(n)}\otimes\delta_{\nu(n)}$",
             fontsize=18, color=ink)
    fig.text(.045, .038,
             "Exact formulas: CDEC.7.a–g.  The model B(ℓ²) is properly infinite and semifinite; rank-one projections are finite.",
             fontsize=13, color=muted)

    fig.savefig(OUT / "absorption-map.png", dpi=160)
    fig.savefig(OUT / "absorption-map.svg")
    plt.close(fig)
    data = {
        "formula": "beta(j,k)=2^j(2k+1)-1",
        "domain": "j,k in N_0; output in N_0",
        "inverse": {"nu": "v_2(n+1)", "kappa": "((n+1)/2^nu(n)-1)/2"},
        "table": [{"j": j, "values": [beta(j, k) for k in range(6)]} for j in range(4)],
        "source": {"k": 1, "j": 2, "n": 11},
        "destination": {"k": 2, "j": 1, "n": 9},
        "matrix_unit": {"input": "E_{2,1} tensor e_{1,2}", "output": "E_{9,11}"},
        "map": "Xi(X)=U X U*",
        "inverse_map": "Xi^{-1}(y)=U* y U; (i,j) entry V_i* y V_j",
        "proof_locators": ["CDEC.7.a", "CDEC.7.b", "CDEC.7.c", "CDEC.7.d", "CDEC.7.e", "CDEC.7.f", "CDEC.7.g"],
        "finite_validation": {"inverse_n_checked": 4096, "j_checked": 10, "k_checked": 64},
        "finite_validation_is_not_a_proof": True,
    }
    (OUT / "data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    font = Path(font_manager.findfont("DejaVu Sans"))
    license_path = font.parent / "LICENSE_DEJAVU"
    if license_path.is_file():
        shutil.copyfile(license_path, OUT / "FONT-LICENSE.txt")
    print(json.dumps({"rendered": ["absorption-map.png", "absorption-map.svg"],
                      "data": "data.json", "validation": "passed"}))


if __name__ == "__main__":
    main()

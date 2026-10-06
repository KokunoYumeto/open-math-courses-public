"""Reproduce exact mathematical figures and rational checks for H2 Examples 13.6.10/12.

Original expression, GPT-6.1 Sol (OpenAI), Ultra, October 2026; CC0.
The plots visualize inequalities proved in ../draft.md; they do not prove
nonuniqueness outside the displayed constructions or close theorem prerequisites.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
BLUE = "#23689b"
LIGHT_BLUE = "#d6e9f5"
ORANGE = "#d46c1d"
INK = "#203040"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.labelsize": 12, "axes.titlesize": 14,
    "axes.spines.top": False, "axes.spines.right": False,
    "text.color": INK, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK,
    "savefig.facecolor": "white",
})

def family10(a, b):
    assert a >= 2 and 0 <= b <= 2*a and 2*b > 3*a+1
    c = (F(3*a+1, 4*a)+F(b, 2*a))/2
    lower = (2*a*c-a)/(a+1)
    upper = (2*a*c-a-1)/(a-1)
    gamma = (lower+upper)/2
    k = 2*a*c-a-a*gamma
    d = 2*a*c-b
    assert F(3*a+1, 4*a) < c < F(b, 2*a) <= 1
    assert lower < gamma < upper < 2*c-1 < 1
    assert k > 0 and gamma > 0
    assert d < 0 and k-gamma < 0 and 1-k-gamma < 0
    assert 1+gamma-2*c < 0
    return {"family": 10, "a": a, "b": b, "c": c,
            "lower": lower, "upper": upper, "gamma": gamma, "k": k,
            "ratio_exponent": d, "K_over_T_exponent": k-gamma,
            "height_over_TK_exponent": 1-k-gamma,
            "eta_exponent": gamma-1,
            "small_window_exponent": 1+gamma-2*c}

def family12(a, b):
    assert a >= 2 and 1 <= b <= a and 2*b > a+3
    lower, upper = F(b-1, a+1), F(b-2, a-1)
    gamma = (lower+upper)/2
    k = b-1-a*gamma
    assert lower < gamma < upper < F(b-1, a) < 1
    assert k > 0 and gamma > 0
    assert k-gamma < 0 and 1-k-gamma < 0
    return {"family": 12, "a": a, "b": b, "c": None,
            "lower": lower, "upper": upper, "gamma": gamma, "k": k,
            "ratio_exponent": F(-1),
            "K_over_T_exponent": k-gamma,
            "height_over_TK_exponent": 1-k-gamma,
            "eta_exponent": gamma-1,
            "small_window_exponent": -k}

CASES = [family10(2, 4), family10(4, 7), family10(5, 9),
         family12(4, 4), family12(6, 5), family12(7, 6)]
EXPECTED = [
    (F(15, 16), F(7, 12), F(3, 4), F(2, 3), F(5, 12)),
    (F(27, 32), F(11, 20), F(7, 12), F(17, 30), F(29, 60)),
    (F(17, 20), F(7, 12), F(5, 8), F(29, 48), F(23, 48)),
    (None, F(3, 5), F(2, 3), F(19, 30), F(7, 15)),
    (None, F(4, 7), F(3, 5), F(41, 70), F(17, 35)),
    (None, F(5, 8), F(2, 3), F(31, 48), F(23, 48)),
]
for row, expected in zip(CASES, EXPECTED):
    assert tuple(row[key] for key in ("c", "lower", "upper", "gamma", "k")) == expected

def threshold_figure():
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.1))
    aa = np.linspace(1.7, 8.4, 800)
    for ax, family in zip(axes, (10, 12)):
        lower = (3*aa+1)/2 if family == 10 else (aa+3)/2
        upper = 2*aa if family == 10 else aa
        ax.fill_between(aa, lower, upper, where=lower < upper,
                        color=LIGHT_BLUE, label="Permitted continuous region")
        ax.plot(aa, lower, color=BLUE, linestyle="--", linewidth=1.8,
                label="Strict threshold (excluded)")
        ax.plot(aa, upper, color=INK, linewidth=1.6,
                label="Order bound (included)")
        points = [(a, b) for a in range(2, 9)
                  for b in range(1, (2*a if family == 10 else a)+1)
                  if (2*b > (3*a+1 if family == 10 else a+3))]
        ax.scatter([p[0] for p in points], [p[1] for p in points],
                   color=BLUE, s=24, zorder=4, label="Admissible integer pair")
        first = (4, 7) if family == 10 else (6, 5)
        ax.scatter(*first, marker="*", color=ORANGE, s=175, zorder=5,
                   edgecolors="white", linewidths=.5, label="First lower-order pair")
        ax.annotate(f"First lower order\n(a,b) = {first}",
                    xy=first, xytext=((2.1, 11.1) if family == 10 else (4.1, 2.0)),
                    arrowprops={"arrowstyle": "-", "color": ORANGE},
                    color=ORANGE, fontsize=10,
                    bbox={"boxstyle": "round,pad=.25", "fc": "white", "ec": ORANGE})
        ax.set_xlim(1.7, 8.4)
        ax.set_ylim(1, 17.4 if family == 10 else 8.6)
        ax.set_xticks(range(2, 9))
        ax.set_yticks(range(2, 18, 2) if family == 10 else range(1, 9))
        ax.set_xlabel("Integer multiplicity a")
        ax.set_ylabel("Perturbation order b")
        ax.grid(alpha=.18)
        ax.set_axisbelow(True)
        ax.set_title("Example 13.6.10" if family == 10 else "Example 13.6.12")
        formula = r"$\frac{3a+1}{2}<b\leq 2a$" if family == 10 else r"$\frac{a+3}{2}<b\leq a$"
        ax.text(.97, .03, formula, transform=ax.transAxes, ha="right", va="bottom",
                fontsize=14, bbox={"boxstyle": "round,pad=.2", "fc": "white", "ec": "none"})
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=3, loc="lower center",
               bbox_to_anchor=(.5, .075), frameon=False, fontsize=9)
    fig.suptitle("Strict window thresholds and the required polynomial orders", y=.99)
    fig.text(.5, .017,
             "Proof: EX10-18–22, EX12-11–12.  Source: Hörmander II, §13.6, printed pp. 212–214.\n"
             "Shading visualizes inequalities; only integer points define the polynomial families.",
             ha="center", va="bottom", fontsize=9)
    fig.subplots_adjust(left=.065, right=.985, top=.90, bottom=.22, wspace=.24)
    fig.savefig(HERE / "threshold-regions.png", dpi=170)
    fig.savefig(HERE / "threshold-regions.svg")
    plt.close(fig)

def scale_figure():
    fig, ax = plt.subplots(figsize=(11.8, 7.0))
    for y, row in enumerate(reversed(CASES)):
        lower, upper, gamma = map(float, (row["lower"], row["upper"], row["gamma"]))
        color = BLUE if row["family"] == 10 else ORANGE
        ax.plot([lower, upper], [y, y], color=color, linewidth=3)
        ax.scatter([lower, upper], [y, y], facecolor="white", edgecolor=color,
                   s=70, linewidth=1.7, zorder=5)
        ax.scatter([gamma], [y], color=color, s=38, zorder=6)
        ax.text(lower-.002, y-.13, str(row["lower"]), ha="right", va="top",
                fontsize=11, color=color)
        ax.text(upper+.002, y-.13, str(row["upper"]), ha="left", va="top",
                fontsize=11, color=color)
        ax.text(gamma, y+.13, "γ = " + str(row["gamma"]), ha="center", va="bottom",
                fontsize=11, color=color)
    names = []
    for row in reversed(CASES):
        extra = f", c={row['c']}" if row["c"] is not None else ""
        names.append(f"Example {row['family']}: (a,b)=({row['a']},{row['b']}){extra}")
    ax.set_yticks(range(len(CASES)), labels=names)
    ax.tick_params(axis="y", length=0, pad=14)
    ax.set_xlim(.50, .81)
    ax.set_ylim(-.6, len(CASES)-.4)
    ax.set_xlabel("Scale exponent γ in Tν = ν^γ")
    ax.grid(axis="x", alpha=.18)
    ax.set_axisbelow(True)
    ax.set_title("Open permitted scale intervals and exact rational midpoint choices", pad=18)
    ax.spines["left"].set_visible(False)
    fig.text(.5, .065,
             "Left endpoint: Kν/Tν fails to decay.    Right endpoint: (1+ν)/(TνKν) fails to decay.\n"
             "Open circles exclude both endpoints.  Filled dots are the exact chosen midpoints.",
             ha="center", fontsize=10)
    fig.text(.5, .015,
             "Proof: EX10-10–15, EX12-6–9.  Source: Hörmander II, printed pp. 212, 214.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=.345, right=.98, top=.88, bottom=.17)
    fig.savefig(HERE / "scale-intervals.png", dpi=170)
    fig.savefig(HERE / "scale-intervals.svg")
    plt.close(fig)

def validate_exact_algebra():
    a, b, c = sp.symbols("a b c", real=True)
    L, U = (2*a*c-a)/(a+1), (2*a*c-a-1)/(a-1)
    ell, u = (b-1)/(a+1), (b-2)/(a-1)
    rho, nu, T, z = sp.symbols("rho nu T z", real=True)
    identities = {
        "EX10_interval_width": sp.simplify(U-L-(4*a*c-3*a-1)/(a*a-1)) == 0,
        "EX10_small_window_implication": sp.simplify(U-(2*c-1)-2*(c-1)/(a-1)) == 0,
        "EX12_interval_width": sp.simplify(u-ell-(2*b-a-3)/(a*a-1)) == 0,
        "EX12_window_implication": sp.simplify(u-(b-1)/a-(b-a-1)/(a*(a-1))) == 0,
        "EX10_exact_circle_quadric": sp.expand(rho*rho+(nu*nu-rho*rho)
                  +(-sp.I*nu+T*z)**2-(T*T*z*z-2*sp.I*nu*T*z)) == 0,
        "universal_derivative_phase": sp.simplify(
            sp.exp(sp.I*(sp.pi-a*sp.pi/2+(a-3)*sp.pi/2))+sp.I) == 0,
    }
    assert all(identities.values())
    count10 = count12 = 0
    first10 = first12 = None
    for ai in range(2, 41):
        for bi in range(0, 2*ai+1):
            admissible = 2*bi > 3*ai+1
            if admissible:
                family10(ai, bi)
                count10 += 1
                if bi < 2*ai and first10 is None:
                    first10 = [ai, bi]
        for bi in range(1, ai+1):
            if 2*bi > ai+3:
                family12(ai, bi)
                count12 += 1
                if bi < ai and first12 is None:
                    first12 = [ai, bi]
    assert first10 == [4, 7] and first12 == [6, 5]
    expected_coefficients = [8, -32, 64*sp.I, -1, 1, -sp.I]
    explicit_signs = []
    for row, expected_coefficient in zip(CASES, expected_coefficients):
        ai, family = row["a"], row["family"]
        coefficient = -2*(-2*sp.I)**ai if family == 10 else -(-sp.I)**ai
        z0 = sp.exp(sp.I*sp.pi*sp.Rational(ai-3, 2*(ai-1)))
        derivative = sp.simplify(ai*coefficient*z0**(ai-1))
        expected_derivative = -sp.I*ai*(2**(ai+1) if family == 10 else 1)
        assert sp.simplify(coefficient-expected_coefficient) == 0
        assert sp.simplify(derivative-expected_derivative) == 0
        explicit_signs.append({"family": family, "a": ai,
                               "limiting_coefficient": str(coefficient),
                               "derivative_at_z0": str(derivative)})
    def serialize(row):
        return {k: str(v) if isinstance(v, F) else v for k, v in row.items()}
    return {
        "type": "author mathematical validation",
        "exact_symbolic_identities": identities,
        "rational_cases": [serialize(row) for row in CASES],
        "bounded_integer_scan": {"a": [2, 40], "admissible_family10_pairs": count10,
                                "admissible_family12_pairs": count12},
        "first_lower_order_pairs": {"family10": first10, "family12": first12},
        "explicit_polynomial_signs": explicit_signs,
        "scope": "Exact calculations validate displayed identities and chosen paths; "
                 "the general proofs and relative theorem dependency scope remain in ../draft.md.",
    }

if __name__ == "__main__":
    results = validate_exact_algebra()
    threshold_figure()
    scale_figure()
    results["sha256"] = {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest().upper()
        for name in ["make_figures.py", "threshold-regions.png", "threshold-regions.svg",
                     "scale-intervals.png", "scale-intervals.svg"]
    }
    (HERE / "figure-validation.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps({"exact_identities_pass": all(results["exact_symbolic_identities"].values()),
                      "cases": len(CASES),
                      "bounded_integer_scan": results["bounded_integer_scan"]}))

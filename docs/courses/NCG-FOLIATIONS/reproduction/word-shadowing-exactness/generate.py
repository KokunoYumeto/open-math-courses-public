#!/usr/bin/env python3
"""Generate the exact word-shadowing schematic and its symbolic data.

Original expression: CC0-1.0. Python standard library only.
The integer display coordinates are schematic, not Riemannian coordinates.
"""

from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
WIDTH, HEIGHT = 900, 1400
INK = "#153046"
MUTED = "#516777"
BLUE = "#176cb6"
GREEN = "#16745d"
ORANGE = "#a8590e"

DATA = {
    "schema": "word-shadowing-exactness-schematic/v1",
    "expression_license": "CC0-1.0",
    "canonical_section": "11BQ",
    "canonical_theorem": "11BQ.1",
    "equation_prefix": "IX",
    "dimensions_px": {"width": WIDTH, "height": HEIGHT},
    "geometry_kind": "schematic placement, not an embedded model or numerical sample",
    "original_metric": "the given, possibly incomplete, Riemannian metric",
    "notation_translation": {"source_report_x": "y_0", "source_report_z": "x_0"},
    "hypotheses": [
        "G is the actual local-isometry germ groupoid with original local domains",
        "C is one fixed compact symmetric actual arrow test",
        "K=s(C) union r(C)",
        "F=T\\U is closed invariant, and x_0 lies in F",
        "d(y_0,x_0)<delta<epsilon/2",
        "one radius epsilon applies to every composable C-word, at every length",
    ],
    "geometry": {
        "display_centres": [
            {"index": "0", "y": [145, 260], "x": [145, 288]},
            {"index": "1", "y": [345, 260], "x": [345, 288]},
            {"index": "2", "y": [545, 260], "x": [545, 288]},
            {"index": "n", "y": [770, 260], "x": [770, 288]},
        ],
        "display_ball_radius_px": 64,
        "display_comparison_length_px": 28,
        "display_lengths_not_metric_values": True,
        "solid_arrows": "same original buffered local-isometry representatives g_k on both paths",
        "dashed_segments": "short original normal geodesics and their isometric images, without arrowheads",
        "F_background": "membership badge only; no topology or manifold shape is asserted",
        "word": "w=g_n...g_1; y_k=g_k...g_1(y_0); x_k=g_k...g_1(x_0)",
        "distance_bound": "d(y_k,x_k)<=d(y_0,x_0)<delta<epsilon/2 for all k",
        "germ_equality": "[u]_(y_0)=[v]_(y_0) iff [u]_(x_0)=[v]_(x_0)",
        "germ_reason": "connected-normal-ball uniqueness of actual local isometries",
        "isotropy": "distinct original isotropy germs remain distinct under evaluation",
        "locators": ["IX.2", "IX.3", "IX.4", "IX.5"],
    },
    "coset_and_hilbert": {
        "h": "h:s(h)->y_0 is arbitrary; its original domain is never extended",
        "right_translation": "R(h')=h'h^(-1)",
        "right_translation_scope": "exact onto basis isometry from one supported component P to W subset W_(y_0)(C)",
        "V": "V:ell^2(W)->ell^2((G|F)_(x_0)); e_[w]_(y_0)->e_[w]_(x_0)",
        "A": "A_(y_0)=P_W lambda_(y_0)(f) P_W",
        "compression": "V* lambda_(x_0)(f) V",
        "D": "D e_w=b(r(w))e_w, 0<=D<=1",
        "transported_D": "V D V* has the same original weights on image vertices and is zero off the image",
        "cutoff_not_reevaluated": True,
        "locators": ["IX.5", "IX.6", "IX.7", "IX.8", "Section 11BQ arbitrary source-fibre cosets"],
    },
    "edge_check": {
        "p": "p=r(w)",
        "p_shadow": "p'=r(J(w))",
        "coefficient_modulus": "|a_i(p)-a_i(p')|<=omega(delta), with continuous zero extension",
        "nonzero_original_case": "if a_i(p)!=0, the buffered original i-arrow is in C; a shadow edge J(w)->J(v) gives J(g_i(p)w)=J(v), and all-word injectivity forces g_i(p)w=v",
        "zero_original_case": "if a_i(p)=0, an extra shadow coefficient has absolute value <=omega(delta); no original arrow is asserted",
        "original_only_case": "a nonzero original supported edge has its actual shadow arrow; if the shadow coefficient is zero, its original coefficient is <=omega(delta)",
        "matrix_support": "each i-summand has at most one entry per row and per column in each of the two compressed matrices",
        "full_row_column_bound": "both absolute row and column sums of E=A_(y_0)-V*lambda_(x_0)(f)V are <=2m omega(delta)",
        "Schur_bound": "||E||<=2m omega(delta) on the entire ell^2 component",
        "locators": ["IX.6", "IX.7"],
    },
    "norm_and_rank": {
        "cutoff": "||bfb||_r<=||f|_(G|F)||_r+eta, where 2m omega(delta)<eta",
        "ideal": "I_U=C_r^*(G|U) is the actual embedded open ideal; f-bfb belongs to I_U",
        "quotient": "||f+I_U||=||f|_(G|F)||_r",
        "restriction_exactness": "0->C_r^*(G|U)->C_r^*(G)->C_r^*(G|F)->0",
        "rank_bound": "Q=q(q+1)/2",
        "rank_opens": "U_j={x:k(x)>=j}, U_0=T, U_(Q+1)=empty",
        "rank_layers": "S_j=U_j\\U_(j+1)",
        "rank_sequence": "0->C_r^*(G|U_(j+1))->C_r^*(G|U_j)->C_r^*(G|S_j)->0, 0<=j<=Q",
        "scope": [
            "closed invariant strata need not be manifolds",
            "original incomplete metric and original isotropy are preserved",
            "ordinary scalar reduced norm exactness supplies no physical graph class, Spin-c coefficient, disk pairing or KK transfer compatibility",
        ],
        "locators": ["IX.1", "IX.8", "IX.9", "IX.10", "IX.11", "IX.12"],
    },
    "human_sources": [
        {"credit": "Alain Connes", "use": "historical graph-normal question only", "title": "A survey of foliations and operator algebras", "url": "https://alainconnes.org/wp-content/uploads/foliationsfine.pdf"},
        {"credit": "Kevin Aguyar Brix, Toke Meier Carlsen and Aidan Sims", "use": "inner-exactness terminology only", "title": "Some results regarding the ideal structure of C*-algebras of etale groupoids", "locator": "Section 2, equation (2.1)", "url": "https://eprints.gla.ac.uk/316431/2/316431.pdf"},
    ],
    "caption": "Schematic geometry with exact proof content: one compact C and one actual normal-ball radius for every word length (IX.2-IX.5); arbitrary coset right translation and unchanged cutoff weights (IX.6-IX.8 and Section 11BQ); full infinite-matrix Schur estimate, exact quotient and rank restriction (IX.7-IX.12). Dashed comparisons are original short normal geodesics, not holonomy arrows. The complete mathematical argument remains in the accompanying source report and canonical Section 11BQ.",
}


def svg() -> str:
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">']
    out += [
        '<title id="title">Actual compact-word shadowing and reduced rank exactness</title>',
        f'<desc id="desc">{escape(DATA["caption"])}</desc>',
        '<metadata>Original schematic expression CC0-1.0. No external images, font bytes, glyph outlines or software bundles.</metadata>',
        '<defs>',
        f'<marker id="blue-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{BLUE}"/></marker>',
        f'<marker id="green-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{GREEN}"/></marker>',
        f'<marker id="ink-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker>',
        '</defs>',
        '<rect width="900" height="1400" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;} .math{font-family:"Cambria Math",Georgia,serif;} .label{font-weight:600;}</style>',
    ]

    def rect(x, y, w, h, fill, stroke="none", radius=12, **attrs):
        extra = " ".join(f'{k.replace("_", "-")}="{escape(str(v))}"' for k, v in attrs.items())
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>')

    def text(x, y, value, size=17, color=INK, weight="400", anchor="start", cls="", **attrs):
        extra = " ".join(f'{k.replace("_", "-")}="{escape(str(v))}"' for k, v in attrs.items())
        content = escape(value)
        content = re.sub(r'_(\[w\][ᵧₓ]₀|\(G\|F\)|[UwW])', lambda m: f'<tspan baseline-shift="sub" font-size="{size*0.72:g}">{m.group(1).strip("()")}</tspan>', content)
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" class="{cls}" {extra}>{content}</text>')

    def line(x1, y1, x2, y2, color=INK, width=2, marker=None, dash=None):
        extras = (f' marker-end="url(#{marker})"' if marker else "") + (f' stroke-dasharray="{dash}"' if dash else "")
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extras}/>')

    def panel(y, h, letter, title, locators):
        rect(28, y, 844, h, "#f7fafc", "#d4e0e7")
        rect(46, y+17, 28, 28, INK, radius=7)
        text(60, y+37, letter, 17, "#fff", "700", "middle")
        text(88, y+37, title, 20, weight="700")
        text(847, y+37, locators, 15, MUTED, anchor="end")

    text(28, 43, "Actual compact-word shadowing", 30, weight="700")
    text(28, 74, "One radius for every word length → the original reduced quotient and rank exactness", 18, MUTED)

    panel(100, 354, "A", "Uniform actual geometry", "IX.2–IX.5")
    text(48, 162, "Fixed compact symmetric arrow test C;  K = s(C) ∪ r(C).", 18)
    text(48, 185, "Every C-word w = gₙ⋯g₁ has one common normal-ball radius ε.", 18)
    rect(74, 275, 755, 59, "#e4f2ed", radius=9)
    for node in DATA["geometry"]["display_centres"]:
        cx, cy = node["y"]
        out.append(f'<circle cx="{cx}" cy="{cy}" r="64" fill="none" stroke="#95b6cc" stroke-width="1.5"/>')
    for x1, x2, label in [(145, 345, "g₁"), (345, 545, "g₂"), (649, 770, "gₙ")]:
        line(x1+7, 260, x2-10, 260, BLUE, 2.5, "blue-arrow")
        line(x1+7, 288, x2-10, 288, GREEN, 2.5, "green-arrow")
        text((x1+x2)//2, 247, label, 19, BLUE, anchor="middle", cls="math")
        text((x1+x2)//2, 317, label, 19, GREEN, anchor="middle", cls="math")
    text(598, 263, "⋯", 22, BLUE, anchor="middle")
    text(598, 291, "⋯", 22, GREEN, anchor="middle")
    line(145, 260, 103, 212, "#95b6cc", 1.5)
    text(96, 229, "ε", 20, MUTED, cls="math")
    for node in DATA["geometry"]["display_centres"]:
        cx, cy = node["y"]
        xx, xy = node["x"]
        idx = node["index"]
        line(cx, cy+4, xx, xy-4, MUTED, 1.8, dash="3 3")
        for ay, color in [(cy, BLUE), (xy, GREEN)]:
            out.append(f'<circle cx="{cx}" cy="{ay}" r="5" fill="{color}"/>')
        text(cx+9, cy-10, "y" + {"0":"₀","1":"₁","2":"₂","n":"ₙ"}[idx], 19, BLUE, weight="600", cls="math")
        text(cx+9, xy+16, "x" + {"0":"₀","1":"₁","2":"₂","n":"ₙ"}[idx], 19, GREEN, weight="600", cls="math")
    text(78, 351, "x₀,…,xₙ ∈ closed invariant F; the green badge marks membership only.", 16, GREEN)
    text(48, 378, "d(yₖ,xₖ) ≤ d(y₀,x₀) < δ < ε/2, for every k and every length n.", 20, cls="math")
    text(48, 404, "Dashed segments: short normal geodesics; solid arrows: the same original maps.", 16, MUTED)
    text(48, 428, "[u]ᵧ₀ = [v]ᵧ₀  ⇔  [u]ₓ₀ = [v]ₓ₀  by connected-ball uniqueness.", 19, cls="math")
    text(48, 451, "Distinct original isotropy germs remain distinct. The original metric may be incomplete.", 15, MUTED)

    panel(472, 218, "B", "Every source-fibre component", "IX.5–IX.8")
    rect(48, 530, 345, 55, "#fff5e9", "#e7c69e", radius=9)
    text(65, 553, "h : s(h) → y₀ is arbitrary", 19, ORANGE, cls="math")
    text(65, 576, "Its domain is never extended.", 16, ORANGE)
    line(406, 557, 449, 557, INK, 2, "ink-arrow")
    rect(464, 530, 384, 55, "#eaf0f8", "#bdd0e3", radius=9)
    text(479, 553, "R(h′) = h′h⁻¹ ∈ W ⊂ Wᵧ₀(C)", 19, cls="math")
    text(479, 576, "Exact onto basis right translation.", 16, MUTED)
    text(48, 612, "V : ℓ²(W) ↪ ℓ²((G|F)ₓ₀),     e_[w]ᵧ₀ ↦ e_[w]ₓ₀", 22, cls="math")
    text(48, 640, "Aᵧ₀ = P_W λᵧ₀(f) P_W;   compare with V* λₓ₀(f) V.", 20, cls="math")
    text(48, 664, "0 ≤ D ≤ 1:  D e_w = b(rw)e_w.  VDV* carries the same original weights;", 16)
    text(48, 687, "zero off the image. No cutoff re-evaluation or cutoff modulus is used.", 15, MUTED)

    panel(708, 215, "C", "Extra shadow edges and the full matrix bound", "IX.6–IX.7")
    text(48, 771, "For each i:  p = r(w),  p′ = r(Jw),  d(p,p′) ≤ δ.", 18, cls="math")
    text(48, 798, "aᵢ(p) ≠ 0:  a shadow i-edge Jw → Jv forces the original i-edge w → v.", 17)
    text(48, 824, "aᵢ(p) = 0:  any extra shadow coefficient is ≤ ω(δ) in absolute value.", 17)
    text(48, 847, "Use the continuous zero extension; do not invent an absent original arrow.", 16, MUTED)
    text(48, 873, "Each i has ≤ 1 entry per row and column in each compressed matrix.", 17)
    text(48, 902, "E = Aᵧ₀ − V*λₓ₀(f)V:  row sums, column sums, and ‖E‖ ≤ 2mω(δ).", 20, cls="math")
    text(48, 920, "Absolute sums on the entire infinite component; the last bound is the Schur estimate.", 15, MUTED)

    panel(941, 145, "D", "The actual ideal and exact quotient norm", "IX.8–IX.10")
    text(48, 1005, "Choose 2mω(δ) < η; take the supremum over every component of every fibre.", 16)
    text(48, 1028, "‖bfb‖ᵣ ≤ ‖f|F‖ᵣ + η;   I_U = Cᵣ*(G|U),   f − bfb ∈ I_U.", 20, cls="math")
    rect(48, 1048, 800, 30, "#e4f2ed", radius=6)
    text(448, 1070, "‖f + I_U‖ = ‖f|F‖ᵣ   (f|F = f|_(G|F))", 23, GREEN, "700", "middle", "math")

    panel(1104, 192, "E", "The original finite Killing-rank sequence", "IX.1, IX.11–IX.12")
    text(48, 1164, "Uⱼ = {x : k(x) ≥ j},  Sⱼ = Uⱼ ∖ Uⱼ₊₁,  Q = q(q+1)/2;  0 ≤ j ≤ Q.", 20, cls="math")
    text(450, 1201, "0 → Cᵣ*(G|Uⱼ₊₁) → Cᵣ*(G|Uⱼ) → Cᵣ*(G|Sⱼ) → 0", 22, GREEN, "600", "middle", "math")
    text(48, 1230, "These are the actual reductions with their original reduced norms.", 17)
    text(48, 1256, "Closed strata need not be manifolds; the original incomplete metric is preserved.", 16, MUTED)
    text(48, 1282, "Norm exactness supplies no scalar graph class, physical phase, disk pairing or KK compatibility.", 16, MUTED)

    text(28, 1320, "Figure 11BQ.1. Schematic geometry; exact proof locators: IX.2–IX.5 (balls and injection),", 15, MUTED)
    text(28, 1340, "IX.6–IX.8 (cosets, coefficients and weights), IX.7–IX.12 (Schur bound, quotient and rank).", 15, MUTED)
    text(28, 1360, "Connes: historical graph-normal question. Brix–Carlsen–Sims: inner-exactness terminology only.", 15, MUTED)
    text(28, 1381, "Original diagram expression: CC0 1.0. Full argument retained in the source report and Section 11BQ.", 14, MUTED)
    out.append('</svg>')
    return "\n".join(out) + "\n"


def main() -> None:
    (HERE / "data.json").write_text(json.dumps(DATA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (HERE / "word-shadowing-exactness.svg").write_text(svg(), encoding="utf-8")
    print("Generated data.json and word-shadowing-exactness.svg (900 × 1400).")


if __name__ == "__main__":
    main()

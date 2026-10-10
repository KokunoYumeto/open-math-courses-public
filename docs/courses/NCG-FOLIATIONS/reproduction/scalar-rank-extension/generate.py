#!/usr/bin/env python3
"""Portable original mathematical SVG generator. Expression: CC0-1.0.
Python standard library only. Display coordinates are schematic.
No external images, fonts, outlined glyphs or software are bundled.
"""
from pathlib import Path
from html import escape
import json
import re

DATA = json.loads(r'''{
  "schema": "original-exact-mathematical-schematic/v1",
  "slug": "scalar-rank-extension",
  "title": "Scalar extension across actual rank jumps",
  "expression_license": "CC0-1.0",
  "dimensions_px": {
    "width": 900,
    "height": 1700
  },
  "geometry_kind": "schematic, not a numerical approximation or asserted embedding",
  "claims": {
    "section": "11BR",
    "figure": "11BR.1",
    "scalar_obstruction": "partial_r tensor_(I_r) x_I in KK^(q+1)(Q_r,C), at a separable semisplit actual extension",
    "q4": {
      "geometry": "T={w in L^tensor2:||w||<4}; F={||w||<=1}; E=T\\F, actual point foliation",
      "projection": "e([z])=zz*/(z*z), e_A=e compose p, e_I=e_A|E, e_Q=e_A|F",
      "modules": [
        "e_A A^2",
        "e_I I^2",
        "e_Q Q^2"
      ],
      "normal": "H_M=L2(T,M tensor S_inv,dvol_g)=e_A L2(T,S_inv,dvol_g)^2; full inverse central line and right Cl4 last",
      "weight": "R=(16-||w||^2)^(-1), alpha=(1+|dR|_g^2)^(-1/2), D=alpha^(1/2)N_M alpha^(1/2)",
      "whole_domain": "u in H_M, u in H1_loc, D u in L2 distributionally; no global unweighted H1 or new boundary condition",
      "disk": "original b_U=i_*b_V and b_U tensor x_A=+1",
      "distinction": "M=1 gives original untwisted class; M=p*L gives selected sign twist"
    },
    "q3": {
      "metric": "g=dt2+exp(2u)(dx2+dy2), u=epsilon exp(-1/(1-t2)) for |t|<1, zero otherwise; epsilon>0",
      "units": "T3=(R/Z)^2 x (-2,2), actual unit groupoid, full=reduced=supremum norm",
      "ranks": "3 on closed [-1,1], 6 on open exteriors",
      "H": "[[I3,N],[0,I3]]",
      "N": [
        [
          "n",
          0,
          0
        ],
        [
          "-m",
          0,
          0
        ],
        [
          0,
          "-m",
          "-n"
        ]
      ],
      "group": "Gamma6=Z4 x Z, H(a+c/sqrt2,b+d/sqrt2) with discrete label topology",
      "single_auxiliary": "kappa=epsilon1+kappa_Dhat; Dhat+=-i/(2pi)d_theta1+1/(2pi)d_theta2; periodic full H1 domain; V=exp(2pi i(a theta1+b theta2))",
      "returns": "one common auxiliary returns 1 on E- and 1+b on E+",
      "family": "all modes (k-x)+i(l-y), zero mode -x-iy, positive winding +1",
      "boundary": "[1_Q3]partial3=(hat_s-,-hat_s+), hat_s+/-=[1_X] external_product s+/-, s+/- in KK1(C,C0(J+/-)), J-=(-2,-1), J+=(1,2); both increasing interval inverse pairings +1",
      "scalar": "[1_Q3]partial3 xI3=0-1=-1 in KK4(C,C)",
      "disk": "every original positive disk still pairs +1"
    },
    "scalar_KK_proof_locators": [
      "KT-KK-10 Theorem2.3 and Corollary2.4 for full scalar KK readback",
      "KT-KK-12 Propositions8.1-8.2, with actual simultaneous suspension in8.2"
    ],
    "scope": "No refutation of original untwisted global class and no universal whole-Theta gate."
  },
  "caption": "Figure 11BR.1. Schematic of the exact scalar boundary criterion, the literal q=4 shared tautological projection and weighted original normal domain, and the q=3 one-auxiliary scalar countertest. Proof: Section 11BR, SE.1-SE.35, with full-homotopy scalar and simultaneous-suspension proof locators. The boundary classes hat_s+/- retain their torus coefficients. Local disk +1 does not erase the quotient-unit obstruction -1; the original untwisted class is not refuted.",
  "drawing": [
    [
      "text",
      28,
      43,
      "Scalar extension across actual rank jumps",
      30,
      "#153046",
      "700",
      "start",
      false
    ],
    [
      "text",
      28,
      74,
      "A boundary test, one literal global extension, and one normalized-choice countertest",
      18,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      100,
      190,
      "A",
      "The scalar obstruction, at its actual hypotheses",
      "SE.1–SE.5"
    ],
    [
      "text",
      48,
      168,
      "Actual separable extension 0 → Iᵣ → Aᵣ → Qᵣ → 0, with a cpc section.",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      204,
      "o(x_{I}) = ∂ᵣ ⊗_{Iᵣ} x_{I} ∈ KK^{q+1}(Qᵣ, ℂ)",
      25,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      241,
      "o(x_{I}) = 0  ⇔  ∃ x_{A} ∈ KK^{q}(Aᵣ, ℂ):  iᵣ^{*}x_{A} = x_{I}.",
      21,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      275,
      "The odd boundary stays on the left; the original final right Cl_q block stays last.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      308,
      448,
      "B",
      "q = 4: the same genuine bundle on A, I and Q",
      "SE.6–SE.22"
    ],
    [
      "text",
      48,
      372,
      "T = {w ∈ L^{⊗2}: ‖w‖ < 4},  F = {‖w‖ ≤ 1},  E = T ∖ F;  point foliation.",
      18,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      405,
      "e([z]) = zz*/(z*z),  z ≠ 0;   e² = e = e*.   M = p*L.",
      22,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      433,
      "e_{A} = e ∘ p,      e_{I} = e_{A}|_{E},      e_{Q} = e_{A}|_{F}.",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "rect",
      48,
      454,
      244,
      60,
      "#eaf0f8",
      "#bdd0e3",
      10
    ],
    [
      "rect",
      328,
      454,
      244,
      60,
      "#e4f2ed",
      "#bad9ce",
      10
    ],
    [
      "rect",
      608,
      454,
      240,
      60,
      "#fff5e9",
      "#e7c69e",
      10
    ],
    [
      "text",
      170,
      480,
      "e_{A}A²",
      23,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      450,
      480,
      "e_{I}I²",
      23,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      728,
      480,
      "e_{Q}Q²",
      23,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      170,
      508,
      "multiplier projection",
      15,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      450,
      508,
      "same bundle restriction",
      15,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      728,
      508,
      "closed-set restriction",
      15,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      48,
      537,
      "C(F) ≃ C(S²); split sphere + Bott inverses give KK⁵(Q, ℂ) = 0.",
      21,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      566,
      "H_{M} = L²(T, M ⊗ S_{inv}, dvol_g) = e_{A}L²(T, S_{inv}, dvol_g)².",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      595,
      "R = (16 − ‖w‖²)^{-1};    α = (1 + |dR|_g²)^{-1/2};    D_{M}^{α} = α^{1/2}N_{M}α^{1/2}.",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      625,
      "Dom D_{M}^{α} = {u ∈ H_{M}: u ∈ H¹_{loc}, D_{M}^{α}u ∈ L² distributionally}.",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      654,
      "Whole original inverse coefficient S_inv, inverse central line and right Cl₄ retained.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      683,
      "The given metric remains the symbol datum; positive speed supplies the whole domain.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      716,
      "Original b_{U} = i_*b_{V};    b_{U} ⊗_{A} x_{A} = +1.",
      24,
      "#16745d",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      746,
      "Identity line: original d_T.  M = p*L: selected sign twist, kept distinct globally.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      774,
      650,
      "C",
      "q = 3: one auxiliary, two different exterior returns",
      "SE.23–SE.35"
    ],
    [
      "text",
      48,
      840,
      "T₃ = (ℝ/ℤ)² × (−2,2),     g = dt² + e^{2u(t)}(dx² + dy²).",
      21,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      872,
      "u(t) = ε e^{-1/(1−t²)} for |t| < 1;   u = 0 for |t| ≥ 1;   ε > 0.",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "rect",
      80,
      890,
      185,
      38,
      "#eaf0f8",
      "none",
      0
    ],
    [
      "rect",
      265,
      890,
      370,
      38,
      "#e4f2ed",
      "none",
      0
    ],
    [
      "rect",
      635,
      890,
      185,
      38,
      "#eaf0f8",
      "none",
      0
    ],
    [
      "text",
      172.5,
      916,
      "E₋: rank 6",
      17,
      "#176cb6",
      "400",
      "middle",
      false
    ],
    [
      "text",
      450,
      916,
      "F₃: rank 3, including ±1",
      17,
      "#16745d",
      "400",
      "middle",
      false
    ],
    [
      "text",
      727.5,
      916,
      "E₊: rank 6",
      17,
      "#176cb6",
      "400",
      "middle",
      false
    ],
    [
      "circle",
      80,
      890,
      4,
      "#fff",
      "#176cb6"
    ],
    [
      "text",
      80,
      947,
      "−2",
      17,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "circle",
      265,
      890,
      4,
      "#16745d",
      "#16745d"
    ],
    [
      "text",
      265,
      947,
      "−1",
      17,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "circle",
      635,
      890,
      4,
      "#16745d",
      "#16745d"
    ],
    [
      "text",
      635,
      947,
      "1",
      17,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "circle",
      820,
      890,
      4,
      "#fff",
      "#176cb6"
    ],
    [
      "text",
      820,
      947,
      "2",
      17,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      48,
      975,
      "Actual units; omitted ends ±2 have finite original distance.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1020,
      "H(m,n) =",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "matrix",
      207,
      1003,
      [
        [
          "1₃",
          "N(m,n)"
        ],
        [
          "0",
          "1₃"
        ]
      ],
      93,
      27,
      20,
      "#153046"
    ],
    [
      "text",
      454,
      1020,
      "N(m,n) =",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "matrix",
      615,
      990,
      [
        [
          "n",
          "0",
          "0"
        ],
        [
          "−m",
          "0",
          "0"
        ],
        [
          "0",
          "−m",
          "−n"
        ]
      ],
      62,
      27,
      20,
      "#153046"
    ],
    [
      "text",
      48,
      1076,
      "Γ₆ = ℤ⁴ × ℤ;  matrix labels H(a + c/√2, b + d/√2), with discrete label topology.",
      18,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1103,
      "One auxiliary sees (a,b); the left basis is scaled by √2, so its (c,d) labels act trivially.",
      16,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1135,
      "D̂^{+} = −i/(2π) ∂_{θ₁} + 1/(2π) ∂_{θ₂};   full periodic domain H¹(X̂).",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1166,
      "V_{(a,b,c,d,j)} = exp(2πi(aθ₁+bθ₂));   κ = ε₁ + κ_{D̂},   [1]κ = 1.",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1198,
      "Whole plus-family modes: (k − x) + i(ℓ − y), (k,ℓ) ∈ ℤ²; zero-mode winding +1.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "rect",
      48,
      1216,
      390,
      61,
      "#eaf0f8",
      "#bdd0e3",
      10
    ],
    [
      "rect",
      458,
      1216,
      390,
      61,
      "#fff5e9",
      "#e7c69e",
      10
    ],
    [
      "text",
      243,
      1242,
      "Left return: 1",
      22,
      "#176cb6",
      "700",
      "middle",
      false
    ],
    [
      "text",
      653,
      1242,
      "Right return: 1 + b = [B]",
      22,
      "#a8590e",
      "700",
      "middle",
      false
    ],
    [
      "text",
      243,
      1266,
      "[1_X] d_X = 0",
      18,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      653,
      1266,
      "b d_X = +1;  [B]d_X = +1",
      18,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      450,
      1290,
      "ŝ_{±} = [1_X] ⊠ s_{±};   s_{±} ∈ KK¹(ℂ, C₀(J_{±})).",
      17,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "text",
      450,
      1318,
      "[1_{Q₃}]∂₃ = (ŝ₋, −ŝ₊),     s₋d₋ = s₊d₊ = +1.",
      20,
      "#153046",
      "400",
      "middle",
      true
    ],
    [
      "rect",
      48,
      1325,
      800,
      42,
      "#fbeceb",
      "#e4bdb9",
      10
    ],
    [
      "text",
      448,
      1354,
      "[1_{Q₃}] ∂₃ x_{I₃} = [1_X]d_X − [B]d_X = 0 − 1 = −1 ∈ KK⁴(ℂ,ℂ).",
      21,
      "#a83d35",
      "700",
      "middle",
      true
    ],
    [
      "text",
      48,
      1396,
      "Every original positive three-disk still pairs +1; this selected x_{I₃} cannot extend.",
      18,
      "#16745d",
      "400",
      "start",
      true
    ],
    [
      "panel",
      1442,
      170,
      "D",
      "The surviving original-class scope",
      "11BR.7–11BR.8"
    ],
    [
      "text",
      48,
      1508,
      "The untwisted d₃ still extends on this actual unit geometry; it is not refuted.",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1537,
      "Normalized auxiliary unit index and local disk +1 do not force scalar coherence.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1566,
      "No universal whole-Θ identity is imposed as a gate for the original graph-normal class.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1595,
      "Arbitrary nonunit variable-rank realization requires its actual excision and coherent cycle.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1640,
      "Figure 11BR.1. Exact degree, projection, domain and boundary signs: SE.1–SE.35.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1663,
      "Full-homotopy scalar readback: KT-KK-10 Theorem 2.3 / Corollary 2.4; suspension: KT-KK-12 8.1–8.2.",
      14,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1686,
      "Original expression CC0 1.0. Connes is credited for the historical graph-normal question only.",
      15,
      "#516777",
      "400",
      "start",
      false
    ]
  ],
  "font_and_software_terms": "No font bytes, glyph outlines, external images or software bundles. Installed fonts/software retain their actual terms."
}''')
HERE=Path(__file__).resolve().parent


def render():
    width,height=DATA['dimensions_px']['width'],DATA['dimensions_px']['height']
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
         '<title id="title">'+escape(DATA['title'])+'</title>',
         '<desc id="desc">'+escape(DATA['caption'])+'</desc>',
         '<metadata>Original expression CC0-1.0. Installed fonts and external software retain their actual terms.</metadata>',
         '<style>text{font-family:Arial,Helvetica,sans-serif;} .math{font-family:"Cambria Math",Georgia,serif;}</style>',
         '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#153046"/></marker></defs>',
         f'<rect width="{width}" height="{height}" fill="#fff"/>']
    def text(x,y,value,size=18,color='#153046',weight='400',anchor='start',math=False):
        content=escape(str(value))
        content=re.sub(r'([_^])\{([^{}]+)\}',lambda m: f'<tspan baseline-shift="{"sub" if m.group(1)=="_" else "super"}" font-size="{size*.72:g}">{m.group(2)}</tspan>',content)
        content=re.sub(r'_([A-Za-z][A-Za-z0-9]*)',lambda m: f'<tspan baseline-shift="sub" font-size="{size*.72:g}">{m.group(1)}</tspan>',content)
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" class="{"math" if math else ""}">{content}</text>')
    def rect(x,y,w,h,fill,stroke='none',radius=10):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
    def line(x1,y1,x2,y2,color='#153046',width=2,arrow=False,dash=None):
        ext=(' marker-end="url(#arrow)"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{ext}/>')
    for item in DATA['drawing']:
        kind=item[0]; a=item[1:]
        if kind=='text': text(*a)
        elif kind=='rect': rect(*a)
        elif kind=='line': line(*a)
        elif kind=='circle':
            x,y,r,fill,stroke=a
            out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        elif kind=='panel':
            y,h,letter,title,locator=a
            rect(28,y,844,h,'#f7fafc','#d4e0e7',12)
            rect(46,y+17,28,28,'#153046','none',7)
            text(60,y+37,letter,17,'#fff','700','middle')
            text(88,y+37,title,20,'#153046','700')
            text(847,y+37,locator,15,'#516777','400','end')
        elif kind=='matrix':
            x,y,rows,colw,rowh,size,color=a
            nrows,ncols=len(rows),len(rows[0]); left=x-colw/2-9; right=x+(ncols-.5)*colw+9
            top=y-size-3; bottom=y+(nrows-1)*rowh+5
            out.append(f'<path d="M{left+6} {top} H{left} V{bottom} H{left+6} M{right-6} {top} H{right} V{bottom} H{right-6}" fill="none" stroke="{color}" stroke-width="1.8"/>')
            for r,row in enumerate(rows):
                for c,value in enumerate(row): text(x+c*colw,y+r*rowh,value,size,color,'400','middle',True)
        else: raise ValueError(kind)
    out.append('</svg>')
    return '\n'.join(out)+'\n'


def main():
    (HERE/'data.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (HERE/(DATA['slug']+'.svg')).write_text(render(),encoding='utf-8')
    print('Generated '+DATA['slug']+'.svg and data.json')

if __name__=='__main__': main()

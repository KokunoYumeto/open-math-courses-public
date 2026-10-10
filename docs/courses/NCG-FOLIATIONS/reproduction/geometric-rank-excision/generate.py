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
  "slug": "geometric-rank-excision",
  "title": "Geometric cpc sections at rank restrictions",
  "expression_license": "CC0-1.0",
  "dimensions_px": {
    "width": 900,
    "height": 1700
  },
  "geometry_kind": "schematic, not a numerical approximation or asserted embedding",
  "claims": {
    "section": "11BS",
    "figure": "11BS.1",
    "route1": {
      "inputs": "actual continuous functor R:G|W->G|F, rho:W->F, identity on F; R_x bijects every whole source fibre",
      "support": "for each compact L and delta>0, {g:R(g)inL,chi(rg)>=delta,chi(sg)>=delta} compact",
      "core": "sigma(f)(g)=sqrt(chi(rg)chi(sg)) f(R(g))",
      "matrix": "lambda_x sigma(f)=D_x V_x* lambda_rho(x)(f) V_x D_x",
      "D": "D_x delta_h=sqrt(chi(rh))delta_h",
      "taper": "I-norm error <=2sqrt(delta)||f||_I"
    },
    "route2": {
      "input": "genuine smooth proper global Lie-isometry H action; actual germ-faithful countable Gamma subgroup",
      "Kaverage": "S_j^K=int_Kj alpha_k S_j0 alpha_k^-1 dk, compact normalized Haar only",
      "induction": "L_j(f)([h,s])=S_j^K(z->phi_j(z)f(hz))(s); Sf=sum_j w_j L_jf",
      "tails": "compact slice phi, locally finite enlarged quotient cover and proper transporter compactness prove C0 range",
      "matrix": "lambda_x Shat(q)=int_F lambda_z(q) dmu_x(z) on whole ell2(Gamma), all isotropy",
      "measure": "mu subprobability, mu_gamma x=gamma_*mu_x, mu_x=delta_x on F"
    },
    "route3": {
      "groupoid": "G=Hcal x J actual product, J=(-2,2) passive units; B=Cr*(Hcal)",
      "norm": "A=C0(J,B), Q=C0(K,B), exact supremum regular norm",
      "gap": "E b(t)=(c-t)/(c-a)b(a)+(t-a)/(c-a)b(c)",
      "outer_left": "(t+2)/(c+2)b(c)",
      "outer_right": "(2-t)/(2-a)b(a)",
      "scope": "all matrix sizes and accumulating gaps; no B nuclearity assumption or deterministic retraction"
    },
    "singular": {
      "K": "{0} union_n>=1 [2^-n,(5/4)2^-n]",
      "bump": "u_n=2^-n exp(-1/((t-a_n)(c_n-t))) on (a_n,c_n),0 elsewhere; u=sum_n u_n",
      "metric": "dt2+exp(2u)g_roundS2 on S2 x (-2,2), incomplete original metric",
      "ranks": "3 on S2 x K,4 on complement",
      "rotationA": [
        [
          1,
          0,
          0
        ],
        [
          0,
          "-3/5",
          "-4/5"
        ],
        [
          0,
          "4/5",
          "-3/5"
        ]
      ],
      "rotationB": [
        [
          "-3/5",
          0,
          "4/5"
        ],
        [
          0,
          1,
          0
        ],
        [
          "-4/5",
          0,
          "-3/5"
        ]
      ],
      "quaternions": [
        "(1+2i)/sqrt5",
        "(1+2j)/sqrt5"
      ],
      "source": "Section 11BS, KEF.1-KEF.4: elementary primitive modulo-five reduced-word proof and irrational-angle circle density",
      "arrows": "actual (x,t)->(A x,t) or (B x,t), preserving t; no new closure arrows",
      "display_coordinate_map": "t -> 160+1000*t, exact rational interval endpoints for n=1..6; remaining intervals only stated to accumulate"
    },
    "limits": "No universal semisplitting for arbitrary local domains, no jet globalization, no final scalar or physical normal cycle."
  },
  "caption": "Figure 11BS.1. Three sufficient geometric cpc providers with their real inputs: actual whole-source-fibre retraction and support, a genuine proper global H action with compact K averaging and C0 tails, and an actual product with a passive interval and full B-valued interpolation. The singular incomplete S2 example uses the exact K, bumps, rank3/4 and nonunit rotation arrows preserving t. Explicit A and B use the elementary quaternion proof in Section 11BS, KEF.1-KEF.4. No universal cpc or final scalar-cycle conclusion is inferred.",
  "drawing": [
    [
      "text",
      28,
      43,
      "Geometric cpc sections at rank restrictions",
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
      "Three conditional providers; a singular incomplete layer with actual nonunit arrows",
      18,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      100,
      92,
      "A",
      "Start with the actual reduced extension",
      "IX.1–IX.12; KE.1–KE.2"
    ],
    [
      "text",
      48,
      168,
      "0 → I → A → Q → 0 is exact; norm exactness alone supplies no cpc section.",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "panel",
      210,
      240,
      "B",
      "Route 1: a whole-source-fibre retraction",
      "KE.3–KE.8"
    ],
    [
      "text",
      48,
      276,
      "Supply an actual functor R:G|W → G|F, ρ:W → F, with R|F = identity.",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      305,
      "Every R_x is a bijection on the entire source fibre, including original isotropy.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      334,
      "0 ≤ χ ≤ 1, χ|F = 1; compact inverse images after both endpoint cutoffs ≥ δ.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      373,
      "λ_x(σ(f)) = D_x V_x* λ_{ρ(x)}(f) V_x D_x,   D_x δ_h = √χ(rh) δ_h.",
      22,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      407,
      "Whole regular matrices give cpc at every size; tapers give I-norm error ≤ 2√δ ‖f‖_I.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      436,
      "The actual retraction and support condition are inputs; compact-word injection is insufficient.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      468,
      276,
      "C",
      "Route 2: a supplied proper global H action",
      "KE.9–KE.14"
    ],
    [
      "text",
      48,
      534,
      "A genuine smooth proper global Lie-isometry action H on the original manifold T.",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      563,
      "Compact stabilizers K_j, original normal slices, and a locally finite quotient partition.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      594,
      "S_j^{K} = ∫_{K_j} α_k S_j⁰ α_{k⁻¹} dk;    average over compact K_j only.",
      21,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      628,
      "Compact slice cutoffs φ_j → induction L_j → positive quotient sum S = Σ_j w_jL_j.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      657,
      "Proper transporter compactness + local finiteness prove S(C₀(F)) ⊂ C₀(T).",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      694,
      "λ_x(Ŝ(q)) = ∫_F λ_z(q) dμ_x(z),   μ_x(F) ≤ 1,   μ_x = δ_x on F.",
      22,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      724,
      "Use the actual germ-faithful Γ subgroup and the whole ℓ²(Γ) basis; isotropy retained.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "panel",
      762,
      234,
      "D",
      "Route 3: an actual passive interval parameter",
      "KE.15–KE.17"
    ],
    [
      "text",
      48,
      828,
      "G = ℋ × J, J = (−2,2);  B = Cᵣ*(ℋ);  A = C₀(J,B),  Q = C₀(K,B).",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      864,
      "(Eb)(t) = (c−t)/(c−a) b(a) + (t−a)/(c−a) b(c),   a < t < c.",
      22,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      897,
      "Outer gaps taper to zero: (t+2)/(c+2)b(c), or (2−t)/(2−a)b(a).",
      18,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      928,
      "Retain b on K; convex B-valued endpoint evaluations are cpc at every matrix size.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      958,
      "Accumulating-gap continuity and C₀ tails are proved; no nuclearity of B is assumed.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      986,
      "This probability interpolation need not come from a neighbourhood retraction.",
      16,
      "#16745d",
      "400",
      "start",
      false
    ],
    [
      "panel",
      1014,
      465,
      "E",
      "An exact singular layer with nonunit rotations",
      "KE.18–KE.21; KEF.1–4"
    ],
    [
      "text",
      48,
      1080,
      "K = {0} ∪ ⋃_{n≥1}[a_n,c_n],   a_n = 2^{-n},   c_n = (5/4)2^{-n}.",
      21,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1113,
      "u_n(t) = 2^{-n} exp(−1/((t−a_n)(c_n−t))) on (a_n,c_n), zero elsewhere.",
      18,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1146,
      "u = Σ_n u_n;   g = dt² + e^{2u(t)}g_{S²} on S² × (−2,2), with original round g_{S²}.",
      19,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "text",
      48,
      1179,
      "k = 3 on F = S² × K;  k = 4 outside F.  Both omitted ends are at finite distance.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "line",
      120,
      1230,
      838,
      1230,
      "#176cb6",
      3,
      false,
      null
    ],
    [
      "circle",
      160,
      1230,
      5,
      "#16745d",
      "#16745d"
    ],
    [
      "text",
      160,
      1260,
      "0",
      17,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "rect",
      660.0,
      1221,
      125.0,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      660.0,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      785.0,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "rect",
      410.0,
      1221,
      62.5,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      410.0,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      472.5,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "rect",
      285.0,
      1221,
      31.25,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      285.0,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      316.25,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "rect",
      222.5,
      1221,
      15.625,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      222.5,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      238.125,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "rect",
      191.25,
      1221,
      7.8125,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      191.25,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      199.0625,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "rect",
      175.625,
      1221,
      3.90625,
      18,
      "#b7dece",
      "none",
      0
    ],
    [
      "circle",
      175.625,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "circle",
      179.53125,
      1230,
      3,
      "#16745d",
      "#16745d"
    ],
    [
      "text",
      410,
      1260,
      "1/4",
      16,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      472.5,
      1260,
      "5/16",
      16,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      660,
      1260,
      "1/2",
      16,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      785,
      1260,
      "5/8",
      16,
      "#516777",
      "400",
      "middle",
      false
    ],
    [
      "text",
      48,
      1289,
      "Exact interval endpoints shown; the remaining intervals accumulate at 0. F is singular.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      83,
      1361,
      "A =",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "matrix",
      164,
      1332,
      [
        [
          "1",
          "0",
          "0"
        ],
        [
          "0",
          "−3/5",
          "−4/5"
        ],
        [
          "0",
          "4/5",
          "−3/5"
        ]
      ],
      72,
      27,
      20,
      "#153046"
    ],
    [
      "text",
      495,
      1361,
      "B =",
      20,
      "#153046",
      "400",
      "start",
      true
    ],
    [
      "matrix",
      578,
      1332,
      [
        [
          "−3/5",
          "0",
          "4/5"
        ],
        [
          "0",
          "1",
          "0"
        ],
        [
          "−4/5",
          "0",
          "−3/5"
        ]
      ],
      72,
      27,
      20,
      "#153046"
    ],
    [
      "text",
      48,
      1422,
      "A ↔ (1+2i)/√5;  B ↔ (1+2j)/√5.  Γ = ⟨A,B⟩ is free and dense in SO(3).",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1452,
      "Actual arrows (x,t) → (Ax,t) or (Bx,t) preserve t and the exact warped metric.",
      18,
      "#16745d",
      "400",
      "start",
      false
    ],
    [
      "panel",
      1497,
      126,
      "F",
      "Dependence and limits",
      "KE.22–KE.24"
    ],
    [
      "text",
      48,
      1563,
      "A proved cpc route gives the actual ideal/cone KK inverse at separable hypotheses.",
      17,
      "#153046",
      "400",
      "start",
      false
    ],
    [
      "text",
      48,
      1592,
      "No formal jet closure is globalized; no final scalar normal/physical cycle is inferred.",
      16,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1648,
      "Figure 11BS.1. Whole matrices, compact global slices and B-valued interpolation: KE.3–KE.17.",
      15,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1670,
      "Singular K, exact metric and ranks: KE.18–KE.21. Explicit rotation proof: KEF.1–KEF.4.",
      15,
      "#516777",
      "400",
      "start",
      false
    ],
    [
      "text",
      28,
      1692,
      "Original expression CC0 1.0. Full proof remains in Section 11BS; all arrows and domains are actual.",
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

"""Original CC0 diagram. Numerical cone/occupation samples are identified explicitly."""
from pathlib import Path
import argparse, base64, html, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=HERE / "figures")
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
FONT = HERE / "fonts/DejaVuSans.ttf"
NOTICE = (HERE / "FONT-NOTICE.txt").read_text(encoding="utf-8")
W, H = 2400, 1550
im = Image.new("RGB", (W, H), "#f8fafc")
draw = ImageDraw.Draw(im)
fonts, used = {}, set()
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>Coarse geometry, proper cone and the coefficient oscillator identity</title>",
    "<desc>Six panels: faithful rational-function linearization; kernel and probability base; exact one-dimensional cone translation; exact two-mode confining oscillator energies; integrable phase bound; distinction between coefficient identity and the missing proper scalar factorization.</desc>",
    "<metadata>" + html.escape("Original diagram and generator: CC0-1.0.\nUnmodified font terms:\n" + NOTICE) + "</metadata>",
    "<style>@font-face{font-family:AuxiliarySans;src:url(data:font/ttf;base64," + base64.b64encode(FONT.read_bytes()).decode() + ")}text{font-family:AuxiliarySans}</style>",
    f'<rect width="{W}" height="{H}" fill="#f8fafc"/>',
]

def text(x, y, value, size=27, color="#17283c"):
    used.update(value)
    if size not in fonts:
        fonts[size] = ImageFont.truetype(str(FONT), size, layout_engine=ImageFont.Layout.BASIC)
    draw.text((x, y), value, font=fonts[size], fill=color, anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(value)}</text>')

def line(x, y, xx, yy, color="#62758d", width=3):
    draw.line((x, y, xx, yy), fill=color, width=width)
    svg.append(f'<path d="M{x},{y} L{xx},{yy}" stroke="{color}" stroke-width="{width}" fill="none"/>')

def box(x, y, w, h, fill="#ffffff", border="#c9d5e3"):
    draw.rectangle((x, y, x+w, y+h), fill=fill, outline=border, width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def dot(x, y, r=7, color="#245fad"):
    draw.ellipse((x-r, y-r, x+r, y+r), fill=color)
    svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')

def arrow(x, y, xx, yy, color="#245fad"):
    line(x, y, xx, yy, color, 4)
    angle = math.atan2(yy-y, xx-x)
    pts = [(xx, yy)] + [(xx-16*math.cos(angle+a), yy-16*math.sin(angle+a)) for a in [-.5, .5]]
    draw.polygon(pts, fill=color)
    svg.append('<polygon points="' + " ".join(f"{a:.3f},{b:.3f}" for a,b in pts) + f'" fill="{color}"/>')

def curve(points, color="#16764b", width=4):
    draw.line(points, fill=color, width=width)
    svg.append('<polyline points="' + " ".join(f"{x:.3f},{y:.3f}" for x,y in points) + f'" fill="none" stroke="{color}" stroke-width="{width}"/>')

text(50, 35, "From compact-Lie subgroups to a proper Hilbert-field cone", 46)
text(50, 108, "The scalar unit construction still needs a proper Bott/Dirac factorization. The coefficient oscillator alone does not supply it.", 28)
for x in [50, 830, 1610]:
    for y in [185, 820]:
        box(x, y, 740, 600)

text(76, 208, "1. All finitely generated subgroups", 32)
text(78, 267, "Γ ⊂ GL(n,K),    [K:Q(t₁,…,tᵣ)] = b", 28)
arrow(397, 318, 397, 370)
box(91, 389, 650, 102, "#edf4ff")
text(110, 411, "Faithful action on Kⁿ over Q(t₁,…,tᵣ)", 26)
text(110, 451, "Γ ↪ GL(nb,Q(t₁,…,tᵣ))", 28)
arrow(397, 505, 397, 548)
text(91, 568, "Countable values + positive Gram kernels", 27)
text(91, 617, "F(g) = ⊕ⱼ (2⁻ʲ/Aⱼ) Fⱼ(g)", 28)
text(91, 672, "Bounded differences ⇒ finitely many g", 26)
text(91, 736, "Uniform embedding: Section 11N; UE.1–15", 21)

text(856, 208, "2. Kernels create the correct base", 32)
text(857, 268, "a_g(x) = ‖f(x) − f(xg)‖²", 29)
arrow(1177, 317, 1177, 363)
text(866, 383, "Y = spectrum of the countable kernel algebra", 25)
text(866, 435, "X = Prob(Y),    K(μ,g) = ∫ k(y,g) dμ", 27)
box(872, 501, 654, 106, "#eef9f1")
text(890, 522, "Every finite F has an F-fixed μ_F.", 27)
text(890, 565, "No Γ-fixed probability is asserted.", 27)
text(868, 644, "‖e_g(μ)‖² = K(μ,g) ≥ ρ₋(|g|)²", 29)
text(868, 699, "μ labels a varying Hilbert fibre H_μ.", 26)
text(868, 736, "Coarse interface: CI.2–12", 22)

text(1636, 208, "3. Exact cone translation: one fibre", 32)
text(1638, 262, "Sample Γ = Z, f(n) = n; ρ₋(r) = r", 25)
# Sample t >= v². Equal horizontal units; vertical unit = 58 pixels.
ox, oy, sx, sy = 1930, 632, 105, 58
line(ox-252, oy, ox+252, oy)
line(ox, oy+8, ox, oy-285)
curve([(ox+sx*v, oy-sy*v*v) for v in [i/100 for i in range(-200,201)]])
line(ox-210, oy-4*sy, ox+210, oy-4*sy, "#245fad")
text(ox+226, oy-4*sy-15, "t=4", 21)
text(ox+258, oy-17, "v", 24)
text(ox+12, oy-278, "t", 24)
dot(ox-1.5*sx, oy-3*sy)
dot(ox+1.5*sx, oy-3*sy, color="#d06a21")
arrow(ox-1.5*sx+13, oy-3*sy, ox+1.5*sx-13, oy-3*sy, "#d06a21")
text(1652, 661, "(−1.5,3) → (1.5,3),  g=3; excess=0.75", 23)
text(1652, 705, "t′=t+2gv+g²; both heights≤R ⇒ |g|≤2√R", 23)
text(1652, 744, "General weak-fibre cone: CI.13–18", 22)

text(76, 843, "4. Confinement and the even vacuum", 32)
text(78, 899, "C_s = sD³ + B(1+sΘ),    D² = 2N", 29)
text(78, 950, "C_s² = 2 Σᵢ (1+2sN+sλᵢ)² Nᵢ", 28)
text(80, 1000, "Exact two-mode sample: s=1, λ=(1,3)", 25)
energies = [((0,0),0), ((1,0),32), ((0,1),72), ((2,0),144), ((1,1),200), ((0,2),256)]
for j,(occupation,energy) in enumerate(energies):
    yy = 1054 + 43*j
    text(89, yy, f"Nᵢ={occupation}", 23)
    length = energy*1.52
    if energy:
        line(270, yy+15, 270+length, yy+15, "#245fad", 12)
    else:
        dot(270, yy+15, 6, "#16764b")
    text(284+length, yy+2, str(energy), 22)
text(83, 1338, "Vacuum: even, kernel rank one; all other energies >0.", 23)
text(83, 1383, "Weighted field: WF.6–12", 22)

text(856, 843, "5. Why the phase error is compact", 32)
text(859, 899, "Linear error: order D; translation cube: order D².", 23)
text(859, 944, "C² ≥ D⁶ makes both errors strictly lower order.", 25)
text(859, 990, "Resolvent tail bound: a^(p−2), p<1", 27)
# Integrable shape for p=2/3; not a measured operator norm.
x0, y0, ww, hh = 934, 1255, 465, 198
line(x0, y0, x0+ww+20, y0)
line(x0, y0, x0, y0-hh-15)
curve([(x0+ww*t/8, y0-hh*(1+t*t)**(-2/3)) for t in [i/25 for i in range(201)]])
text(941, 1267, "0", 21)
text(1379, 1267, "8", 21)
text(1430, 1243, "t", 25)
text(901, 1039, "(1+t²)^(−2/3)", 24, "#16764b")
text(860, 1321, "Illustrated bound shape; not a computed defect norm.", 23)
text(860, 1383, "Weighted field: WF.14–20", 22)

text(1636, 843, "6. The identity and the missing interface", 30)
box(1653, 909, 652, 102, "#eef9f1")
text(1671, 930, "[coefficient oscillator] = 1_C(X)", 29)
text(1671, 974, "KK^Γ(C(X),C(X)); complete homotopy proved", 23)
text(1650, 1050, "A point evaluation is equivariant only at a fixed point.", 23)
text(1650, 1100, "Still needed: η:C→P and d:P→C with", 26)
text(1650, 1145, "P proper,   forget(η⊗d)=+1.", 28)
box(1653, 1207, 652, 112, "#fff5e9", "#d3ab7d")
text(1671, 1228, "If supplied: κ = j_rη · q_P⁻¹ · j_max d · ε_max", 24)
text(1671, 1275, "κ([1])=+1; no equivariant γ=1 is inferred.", 24)
text(1650, 1383, "Scalar theorem 11J.3; identity Theorem 11P.3", 20)

text(50, 1465, "Sources: Guentner–Higson–Weinberger (2003), §§2–4; Tu (1999), §§6–9; Tu (2004), Theorem 3.3.", 23)
text(50, 1505, "Original proofs and diagram: CC0. Exact hypotheses, domains and remaining factorization are stated in the accompanying texts.", 23)
svg.append("</svg>")
im.save(args.output / "coarse-field-unit.png", compress_level=9)
(args.output / "coarse-field-unit.svg").write_text("\n".join(svg)+"\n", encoding="utf-8", newline="\n")
(args.output / "render-data.json").write_text(json.dumps({
    "size":[W,H], "font_files":["fonts/DejaVuSans.ttf"],
    "layout_engine":"Pillow BASIC", "glyphs":sorted(used),
    "cone_sample":{"g":3,"v":-1.5,"t":3,"v_out":1.5,"t_out":3,"excess":.75},
    "occupation_sample":{"s":1,"lambda":[1,3],"energies":[[list(a),b] for a,b in energies]},
    "phase_bound_shape":{"p":2/3,"formula":"(1+t^2)^(-2/3)","not_actual_defect_norm":True}
}, indent=2)+"\n", encoding="utf-8", newline="\n")

# A second exact coordinate projection illustrates the strict half-mass argument.
W, H = 2300, 980
im = Image.new("RGB", (W,H), "#f8fafc")
draw = ImageDraw.Draw(im)
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>The half-mass properness test and the cutoff probability map</title>",
    "<desc>The left panel is only the coordinate projection a=mu(E), b=mu(h inverse E) under the disjoint-set hypothesis: a+b at most one cannot meet a,b strictly greater than one half. The right panel gives the exact locally finite square-cutoff probabilities and their equivariant push to a compact probability base.</desc>",
    "<metadata>" + html.escape("Original diagram and generator: CC0-1.0.\nUnmodified font terms:\n" + NOTICE) + "</metadata>",
    "<style>@font-face{font-family:AuxiliarySans;src:url(data:font/ttf;base64,"+base64.b64encode(FONT.read_bytes()).decode()+")}text{font-family:AuxiliarySans}</style>",
    f'<rect width="{W}" height="{H}" fill="#f8fafc"/>',
]
text(50,35,"A universal proper measure base: the strict half-mass mechanism",44)
text(50,105,"M uses weak-* coordinates and 1/2 < total mass ≤ 1. Total mass need not be continuous.",28)
box(50,175,1060,690)
box(1150,175,1100,690)
text(76,203,"1. If E and h⁻¹E are disjoint",34)
text(76,257,"a=μ(E),  b=μ(h⁻¹E)  ⇒  a+b≤1",30)
ox,oy,scale=275,755,435
points=[(ox,oy),(ox+scale,oy),(ox,oy-scale)]
draw.polygon(points,fill="#e5f5eb")
svg.append('<polygon points="'+' '.join(f"{x},{y}" for x,y in points)+'" fill="#e5f5eb"/>')
box(ox+scale/2,oy-scale,scale/2,scale/2,"#fff0df","#d09b66")
line(ox,oy,ox+scale+40,oy)
line(ox,oy,ox,oy-scale-30)
line(ox,oy-scale,ox+scale,oy,"#16764b",5)
for v in [.5,1]:
    line(ox+scale*v,oy-7,ox+scale*v,oy+7)
    text(ox+scale*v-20,oy+15,str(v),22)
    line(ox-7,oy-scale*v,ox+7,oy-scale*v)
    text(ox-66,oy-scale*v-13,str(v),22)
text(ox+scale+55,oy-15,"a",26)
text(ox+12,oy-scale-45,"b",26)
text(ox+39,oy-116,"a+b≤1",28,"#16764b")
text(ox+scale/2+18,oy-scale+24,"a>1/2",25,"#a05518")
text(ox+scale/2+18,oy-scale+66,"b>1/2",25,"#a05518")
text(773,459,"No common",28)
text(773,504,"point in the",28)
text(773,549,"strict orange",28)
text(773,594,"region.",28)
text(81,827,"This is a coordinate projection, not a picture of all of M.",23)
text(1177,205,"2. Properness gives the finite probability map",31)
box(1182,287,1035,101,"#edf4ff")
text(1205,307,"For compact K⊂M choose one finite E with μ(E)>1/2.",28)
text(1205,351,"μ∈K and hμ∈K  ⇒  E∩h⁻¹E≠∅  ⇒  h∈EE⁻¹.",28)
arrow(1683,405,1683,459)
text(1194,485,"Square cutoff:   Σ_g c(g⁻¹z)² = 1",31)
text(1194,543,"μ_z(g)=c(g⁻¹z)² ∈ M",31)
arrow(1683,596,1683,644)
text(1194,671,"Φ(z)=Σ_g c(g⁻¹z)² δ_(g·y₀) ∈ Prob(Y)",30)
text(1194,737,"Locally finite on compact supports; Φ(hz)=hΦ(z).",27)
text(1194,808,"No equivariant scalar evaluation or Dirac inverse is inferred.",25)
text(50,912,"Proper probability base: PM.1–5. Source comparison: Tu (2004), pp.276 and 282–284.",25)
text(50,949,"Original argument and illustration: CC0. Exact cutoff hypotheses and weak-* limits are stated in the complete proof.",23)
svg.append("</svg>")
im.save(args.output/"proper-probability-base.png",compress_level=9)
(args.output/"proper-probability-base.svg").write_text("\n".join(svg)+"\n",encoding="utf-8", newline="\n")
record=json.loads((args.output/"render-data.json").read_text(encoding="utf-8"))
record["glyphs"]=sorted(used)
record["figures"]={"coarse-field-unit":[2400,1550],"proper-probability-base":[2300,980]}
(args.output/"render-data.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8", newline="\n")

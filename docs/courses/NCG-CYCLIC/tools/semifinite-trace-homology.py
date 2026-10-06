"""Reproduce the original R1-R3 schematic using SVG and Pillow; no TeX."""
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont
HERE=Path(__file__).resolve().parent.parent/"public/assets"
HERE.mkdir(parents=True,exist_ok=True)
STEM="semifinite-trace-homology"
W,H=1680,1020
im=Image.new("RGB",(W,H),"#f7f7f2");d=ImageDraw.Draw(im)
fonts=Path("C:/Windows/Fonts")
def font(size,bold=False):
 name="arialbd.ttf" if bold else "seguisym.ttf"
 return ImageFont.truetype(str(fonts/name),size)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',f'<rect width="{W}" height="{H}" fill="#f7f7f2"/>']
def text(x,y,s,size=25,bold=False):
 d.text((x,y),s,font=font(size,bold),fill="#173245")
 svg.append(f'<text x="{x}" y="{y+size}" font-size="{size}" font-family="Segoe UI Symbol,Arial,sans-serif" font-weight="{700 if bold else 400}" fill="#173245">{escape(s)}</text>')
def box(x,y,w,h,title,lines,color):
 d.rounded_rectangle((x,y,x+w,y+h),radius=15,fill=color,outline="#456171",width=2)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{color}" stroke="#456171" stroke-width="2"/>')
 text(x+20,y+20,title,29,True)
 for i,line in enumerate(lines):text(x+20,y+73+36*i,line,25)
def arrow(x1,y1,x2,y2):
 d.line((x1,y1,x2,y2),fill="#375666",width=4)
 if x2>x1: pts=[(x2,y2),(x2-13,y2-9),(x2-13,y2+9)]
 elif x2<x1:pts=[(x2,y2),(x2+13,y2-9),(x2+13,y2+9)]
 else:pts=[(x2,y2),(x2-9,y2+13),(x2+9,y2+13)]
 d.polygon(pts,fill="#375666")
 svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#375666" stroke-width="4"/>')
 svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="#375666"/>')
text(45,30,"Trace homology: exact domains and scaling signs",41,True)
box(45,132,475,253,"R1: the source domain",["E = D ∩ L²(τ) is norm dense","F₀ = span(EE) ⊂ L¹ ∩ L²","δ(x)(y) + δ(y)(x) = τ(xy)","No star stability of D is added."],"#e5edfa")
box(605,132,475,253,"The integrable graph F",["||x||F = ||x|| + ||x||₁","             + ||x||₂ + ||δx||","F⁺ is matrix inverse closed.","K₀(F) ≅ K₀(A)"],"#e5edfa")
box(1165,132,470,253,"Idempotents give zero",["δ⁺(P)(P) = 0","τ(P − Q) = 0","All relative K₀ classes.","Proof: R.6–R.7"],"#e5edfa")
arrow(535,260,590,260);text(525,93,"R.2–R.5",22)
arrow(1095,260,1150,260);text(1080,93,"R.6–R.7",22)
box(45,500,700,220,"R2: an actual dual-valued derivation",["τ ϑt = e^tτ; smooth L¹ ∩ L² vectors","d = (d/dt)|₀ ϑt; δ(x)(a) = τ((dx)a)","|δ(x)(a)| ≤ ||dx||₁ ||a||","Homology identity: R.8–R.11"],"#e1f0e7")
box(930,500,705,220,"R3: restrict the existing core trace",["h^(it) = λ(t); τN = Φ_{h^-1}","τN θs = e^(-s)τN; ϑt = θ−t","a f(P_A) ∈ A ⋊ ℝ; J(a f(P_A)) = π(a)f(P).","Proof: R.12–R.15"],"#fff0d9")
arrow(915,600,760,600);text(755,451,"reverse time",23)
arrow(285,475,285,404);text(310,424,"R.11",23)
box(45,810,1590,148,"Finite frequency cutoffs give the C* density",["P = log h; f ∈ C_c^∞(ℝ):  τN(|J(a f(P_A))|²) ≤ ||a||² (1/2π) ∫ e^(-r) |f(r)|² dr < ∞","These integrated kernels span a norm-dense subspace. Proof: R.13–R.14. Boxes are schematic."],"#f2eee5")
text(45,975,"Original diagram. Proof: R1–R3. Human context: Connes, transverse fundamental class, author PDF p.10.",23)
svg.append("</svg>")
(HERE/(STEM+".svg")).write_text("\n".join(svg)+"\n",encoding="utf-8")
im.save(HERE/(STEM+".png"))

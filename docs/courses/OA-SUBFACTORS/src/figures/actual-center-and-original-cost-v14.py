"""CC0 reproducible, exact-label schematic for C13.1-C13.24."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont
import math

HERE = Path(__file__).resolve().parent
W, H = 2100, 1580
im = Image.new("RGB", (W,H), "#f5f7fa")
dr = ImageDraw.Draw(im)
def font(size, bold=False):
    names = ("segoeuib.ttf", "DejaVuSans-Bold.ttf", "arialbd.ttf") if bold else ("segoeui.ttf", "DejaVuSans.ttf", "arial.ttf")
    for name in names:
        try: return ImageFont.truetype(name, size)
        except OSError: pass
    raise RuntimeError("Install Segoe UI, DejaVu Sans or Arial to reproduce this diagram.")
fonts = {n: font(n) for n in (27,30,34,38,42,48,56)}
bolds = {n: font(n, True) for n in (30,34,38,42,48,56)}
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<rect width="2100" height="1580" fill="#f5f7fa"/>']

def text(x,y,s,n=34,color="#182c40",bold=False):
    f = bolds[n] if bold else fonts[n]
    dr.text((x,y),s,font=f,fill=color)
    svg.append(f'<text x="{x}" y="{y+n}" font-family="Segoe UI, sans-serif" font-size="{n}" fill="{color}" font-weight="{700 if bold else 400}">{escape(s)}</text>')

def box(x,y,w,h,fill="#ffffff",border="#58718a"):
    dr.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline=border,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def arrow(x1,y1,x2,y2,color="#58718a"):
    dr.line((x1,y1,x2,y2),fill=color,width=6)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2),(x2-21*math.cos(a-.5),y2-21*math.sin(a-.5)),(x2-21*math.cos(a+.5),y2-21*math.sin(a+.5))]
    dr.polygon(pts,fill=color)
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="6"/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{color}"/>')

text(70,42,"Actual center return and original cost",56,bold=True)
text(70,116,"Fixed physical parameter λ from WM.22; both canonical traces and P0 retained.",30)

box(70,195,890,255)
text(102,215,"Actual core centers U = Z(S), V = Z(R)",38,bold=True)
text(102,278,"All final lamp signs are central unitaries.",34)
text(102,329,"Countable equality tests recover p0, ..., p4.",34)
text(102,384,"D0 = U join V = direct sum of p_i U       C13.1–C13.8",30)
box(1130,195,900,255)
text(1162,215,"Actual coefficient center Z = Z(W)",38,bold=True)
text(1162,278,"Normal full-corner maps: ζ_U, ζ_V",34)
text(1162,329,"ζ_U ϑ_i(v) = β_i^(-1) ζ_V(v)",34)
text(1162,384,"Original joint lift: diag(β_i ζ_U(t_i))       C13.10–11",30)
arrow(960,320,1130,320)

box(70,535,890,255,fill="#eaf4f1",border="#3a7b69")
text(102,555,"Any H-invariant state ω on actual Z",38,bold=True)
text(102,619,"Prescribe Γ(z) = ω(z)1, Γ|P = identity.",34)
text(102,670,"Finite physical corner → matrix entries → Følner return",30)
text(102,728,"Γ β_g = α_g Γ; Γ: W → P       C13.12",34)
box(1130,535,900,255,fill="#eaf4f1",border="#3a7b69")
text(1162,555,"Original compatible physical state",38,bold=True)
text(1162,619,"F: B → M,  E_N F = F E_A,  ψ = τ F",34)
text(1162,670,"ψ|M = τ; ψ is M-central.",34)
text(1162,728,"Every compatible ψ gives invariant ω.       C13.13",30)
arrow(1580,450,1580,497)
arrow(1580,497,515,497)
arrow(515,497,515,535)
arrow(960,660,1130,660,color="#3a7b69")

box(70,875,1960,242)
text(102,893,"Exact original quantities: R_i = ζ_V(r_i),  r_i = E_V(p_i)",38,bold=True)
text(102,954,"Discrepancy:  ||α − α P0|| = sum_i ω(|R_i − w_i|)                       C13.17",38)
text(102,1017,"Original cost:  ψ(a) = sum_i ω(|R_i^(-1) − 1/w_i|)                       C13.19",38)
arrow(1580,790,1580,875)

box(70,1200,1210,272,fill="#eaf4f1",border="#3a7b69")
text(102,1218,"Proved fixed-model bounds",38,bold=True)
text(102,1281,"1/(4λ+1) ≤ ω(R1) ≤ λ/(4+λ)",38)
text(102,1341,"0 ≤ ψ(a) ≤ 2(4+λ)(λ²−1) / λ^(3/2)",38)
text(102,1406,"C13.20–C13.23; no change of physical inclusion",30)
box(1370,1200,660,272,fill="#fff4df",border="#b68431")
text(1402,1218,"Unproved endpoint",38,bold=True)
text(1402,1283,"Can an invariant ω attain",34)
text(1402,1334,"ω(R1) = λ/(4+λ) ?",38)
text(1402,1406,"Equivalent to original zero cost: C13.24",27)
arrow(1070,1117,1070,1160)
arrow(1070,1160,675,1160)
arrow(675,1160,675,1200)
arrow(1070,1160,1700,1160)
arrow(1700,1160,1700,1200)
text(70,1506,"CC0 schematic. C13.1–C13.24 contain complete proofs. No zero-state or positive universal floor is asserted.",27)
svg.append("</svg>")
im.save(HERE/"actual-center-and-original-cost-v14.png")
(HERE/"actual-center-and-original-cost-v14.svg").write_text("\n".join(svg),encoding="utf-8")
print("Wrote 2100 x 1580 PNG and reproducible SVG.")

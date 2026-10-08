"""CC0 schematic of exact actual height conditioning and its obstruction."""
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont
import math

here=Path(__file__).resolve().parent
W,H=2100,1840
im=Image.new("RGB",(W,H),"#f5f7fa")
dr=ImageDraw.Draw(im)
def font(size,bold=False):
    names=("segoeuib.ttf","DejaVuSans-Bold.ttf","arialbd.ttf") if bold else ("segoeui.ttf","DejaVuSans.ttf","arial.ttf")
    for name in names:
        try:return ImageFont.truetype(name,size)
        except OSError:pass
    raise RuntimeError("Install Segoe UI, DejaVu Sans or Arial to reproduce this diagram.")
fonts={n:font(n) for n in (27,30,34,38,42,48,56)}
bolds={n:font(n,True) for n in (30,34,38,42,48,56)}
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="#f5f7fa"/>']

def text(x,y,s,n=34,color="#182c40",bold=False):
    dr.text((x,y),s,font=bolds[n] if bold else fonts[n],fill=color)
    svg.append(f'<text x="{x}" y="{y+n}" font-family="Segoe UI, sans-serif" font-size="{n}" fill="{color}" font-weight="{700 if bold else 400}">{escape(s)}</text>')

def box(x,y,w,h,fill="#ffffff",border="#58718a"):
    dr.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline=border,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def arrow(x1,y1,x2,y2,color="#58718a"):
    dr.line((x1,y1,x2,y2),fill=color,width=6)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2),(x2-22*math.cos(a-.5),y2-22*math.sin(a-.5)),(x2-22*math.cos(a+.5),y2-22*math.sin(a+.5))]
    dr.polygon(pts,fill=color)
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="6" fill="none"/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{color}"/>')

text(65,35,"Actual height conditioning fails lamp invariance",48,bold=True)
text(65,106,"Same fixed physical λ and inclusion; h(x) = x1+x2+x3. Original normal center traces are used.",30)
box(65,180,1970,435)
text(100,197,"Condition on E_K: a final lit lamp has height at least K.",38,bold=True)
text(100,258,"Exact normal tails: μ_U(E_K) = p λ^(−K),  μ_V(E_K) = A p λ^(−K)",38)
text(100,309,"A = (1+4λ)/(4+λ),  p > 0; E_K ↓ 0 strongly.       T15.7–T15.11",34)
dr.line((160,400,1920,400),fill="#b68431",width=4)
svg.append('<path d="M160,400 L1920,400" stroke="#b68431" stroke-width="4"/>')
text(1660,352,"First hit: h = K",30,color="#956617")
arrow(190,535,720,400,color="#3a7b69")
arrow(720,400,1450,548,color="#58718a")
text(105,547,"Exact conditional prefix law",34,color="#3a7b69")
text(935,547,"Original suffix conditioned on a high lamp",34)
text(1550,450,"Return to fixed origin",27)
text(1550,492,"has probability → 0.",27)

box(65,700,960,350,fill="#eaf4f1",border="#3a7b69")
text(100,717,"Actual singular center state ρ",38,bold=True)
text(100,777,"ρ_K(t) = μ_V(E_K t) / μ_V(E_K)",34)
text(100,836,"ρ(R0) = 1/(1+4λ)",38)
text(100,893,"ρ(R_i) = λ/(1+4λ),  i = 1,...,4",38)
text(100,965,"Different from original w_i+; exact T15.13.",30)
box(1115,700,920,350,fill="#fff0e9",border="#b96d51")
text(1150,717,"Finite obstruction to invariance",38,bold=True)
text(1150,786,"ρ(L0) = h_tilde+(λ) > b/2 > 0",38)
text(1150,850,"Actual β1 flips L0 to −L0.",38)
text(1150,920,"Every invariant state must have ω(L0)=0.",30)
text(1150,977,"Therefore every height-tail ρ fails.       T15.20",30)
arrow(1025,875,1115,875,color="#b96d51")
arrow(770,615,540,700)

box(65,1140,1970,270,fill="#edf0f8",border="#626c9b")
text(100,1157,"Actual translation logarithmic means",42,bold=True)
text(100,1221,"ℓ_j = ω(log D_(j+1)); all group relations leave a spatial character.",34)
text(100,1281,"0 ≤ ℓ_1+ℓ_2+ℓ_3 ≤ 3 log λ.       T15.1–T15.6",38)
text(100,1341,"Zero sum would give original zero cost. Attainment is still unproved.",34)

box(65,1500,1970,243)
text(100,1517,"The original whole Jones ideal is already annihilated",42,bold=True)
text(100,1584,"Every compatible physical state kills norm-closed span(B e_R^M B).",38)
text(100,1650,"Actual SC.2–SC.3 bounded cuts and finite B/A expansion apply.       E14.12a",34)
text(65,1780,"CC0 schematic; no distance or probability is encoded by arrows. Height-tail states are not compatible physical returns.",27)
svg.append("</svg>")
im.save(here/"translation-height-obstruction-v16.png")
(here/"translation-height-obstruction-v16.svg").write_text("\n".join(svg),encoding="utf-8")
print("Wrote 2100x1840 PNG and SVG.")

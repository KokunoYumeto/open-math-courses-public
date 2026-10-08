"""CC0 exact-label schematic of E14.1-E14.18; endpoint strip has no metric."""
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont
import math

here=Path(__file__).resolve().parent
W,H=2100,1720
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
    dr.text((x,y),s,font=(bolds[n] if bold else fonts[n]),fill=color)
    svg.append(f'<text x="{x}" y="{y+n}" font-family="Segoe UI, sans-serif" font-size="{n}" fill="{color}" font-weight="{700 if bold else 400}">{escape(s)}</text>')

def box(x,y,w,h,fill="#ffffff",border="#58718a"):
    dr.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline=border,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{border}" stroke-width="3"/>')

def arrow(x1,y1,x2,y2,color="#58718a"):
    dr.line((x1,y1,x2,y2),fill=color,width=6)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2),(x2-22*math.cos(a-.5),y2-22*math.sin(a-.5)),(x2-22*math.cos(a+.5),y2-22*math.sin(a+.5))]
    dr.polygon(pts,fill=color)
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="6"/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{color}"/>')

text(65,35,"Actual center constraints at fixed λ",56,bold=True)
text(65,110,"Original physical τ, E_A, P0 and both canonical traces retained.",34)
box(65,190,1970,310)
text(100,212,"Three actual four-label words: phases +, −, +, −",42,bold=True)
text(105,278,"(0, 0, 0, 0) → 1",38)
text(770,278,"(1, 0, 1, 0) → z²",38)
text(1420,278,"(0, 1, 0, 1) → z^(−2)",38)
text(105,337,"probability 1/d²",34)
text(770,337,"probability λ²/d²",34)
text(1420,337,"probability λ^(−2)/d²",34)
text(105,410,"TV(endpoint law, its z² shift) ≤ min(1, 77/sqrt(n) + 3888/n)       E14.1–E14.4",38)

box(65,590,960,248,fill="#eaf4f1",border="#3a7b69")
text(100,610,"Whole-center action identity",42,bold=True)
text(100,677,"β_(z²)|Z = identity       E14.5",38)
text(100,737,"Original physical α_(z²) still scales by λ².",34)
text(100,786,"Only the center action forgets z².",30)
box(1115,590,920,248,fill="#eaf4f1",border="#3a7b69")
text(1150,610,"Original trace-density constraint",38,bold=True)
text(1150,677,"D1 = R1 / (λ R0),  D1 β1(D1) = 1",34)
text(1150,737,"ω(log R1) − ω(log R0) = log λ",38)
text(1150,786,"Actual two measures retained.       E14.13–15",30)
arrow(520,500,520,590)
arrow(1025,710,1115,710,color="#3a7b69")

box(65,930,1970,225,fill="#edf0f8",border="#626c9b")
text(100,947,"All actual invariant center states are purely singular",42,bold=True)
text(100,1008,"Finite lamp probabilities are 2^(−|F|); F_L ↑ 1 strongly but ω(F_L) = 0 for every L.",34)
text(100,1063,"F_L: all sites outside [−L,L] on one actual lattice line are unlit.       E14.10–12",34)
text(100,1110,"No normal positive functional lies below ω; all compatible returns kill J_e.       E14.12a",30)
arrow(520,838,520,930)

box(65,1260,1970,340)
text(100,1278,"Proved exclusion at the lower root; upper root still unproved",42,bold=True)
dr.line((185,1430,1870,1430),fill="#58718a",width=7)
svg.append('<path d="M185,1430 L1870,1430" stroke="#58718a" stroke-width="7"/>')
dr.rectangle((185,1408,480,1452),fill="#d98b84")
svg.append('<rect x="185" y="1408" width="295" height="44" fill="#d98b84"/>')
dr.ellipse((1858,1418,1882,1442),fill="#ffffff",outline="#b68431",width=4)
svg.append('<circle cx="1870" cy="1430" r="12" fill="white" stroke="#b68431" stroke-width="4"/>')
text(100,1345,"Excluded interval",34,color="#914f49")
text(1550,1345,"Zero-cost endpoint?",34,color="#956617")
text(100,1477,"1/(4λ+1)",38)
text(440,1477,"+ δ",38)
text(1630,1477,"λ/(4+λ)",38)
text(100,1535,"δ = (log λ)²/(16d^5); actual R_i ≥ 1/d       E14.18a",34)
arrow(1600,838,2070,838)
arrow(2070,838,2070,1203)
arrow(2070,1203,1620,1203)
arrow(1620,1203,1620,1260)
text(65,1640,"CC0 exact-label schematic. Endpoint strip encodes no metric. No upper-endpoint attainment or separation is proved.",27)
svg.append("</svg>")
im.save(here/"actual-center-action-and-singularity-v15.png")
(here/"actual-center-action-and-singularity-v15.svg").write_text("\n".join(svg),encoding="utf-8")
print("Wrote 2100 x 1720 PNG/SVG.")

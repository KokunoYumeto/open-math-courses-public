"""Reproduce nonunital-action-index.png/svg for Theorem 7.3a; no TeX."""
from pathlib import Path
from html import escape
from PIL import Image,ImageDraw,ImageFont

OUT=Path(__file__).resolve().parent.parent/"public/assets"
OUT.mkdir(parents=True,exist_ok=True)
W,H=1680,1140
im=Image.new("RGB",(W,H),"#f7f7f2")
d=ImageDraw.Draw(im)
fonts=Path("C:/Windows/Fonts")
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="#f7f7f2"/>']
def text(x,y,s,size=26,bold=False):
 # Arial Bold lacks several mathematical superscripts and double-struck glyphs.
 # Use the complete symbol font for every label containing a non-ASCII glyph.
 name="arialbd.ttf" if bold and all(ord(c)<128 for c in s) else "seguisym.ttf"
 f=ImageFont.truetype(str(fonts/name),size)
 d.text((x,y),s,font=f,fill="#173245")
 svg.append(f'<text x="{x}" y="{y+size}" font-family="Segoe UI Symbol,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="#173245">{escape(s)}</text>')
def box(x,y,title,line,color):
 d.rounded_rectangle((x,y,x+445,y+128),radius=16,fill=color,outline="#456171",width=2)
 svg.append(f'<rect x="{x}" y="{y}" width="445" height="128" rx="16" fill="{color}" stroke="#456171" stroke-width="2"/>')
 text(x+23,y+20,title,31,True);text(x+23,y+73,line,24)
def arrow(x1,y1,x2,y2,color="#375666"):
 d.line((x1,y1,x2,y2),fill=color,width=4)
 if x2>x1:pts=[(x2,y2),(x2-14,y2-10),(x2-14,y2+10)]
 elif x2<x1:pts=[(x2,y2),(x2+14,y2-10),(x2+14,y2+10)]
 elif y2>y1:pts=[(x2,y2),(x2-10,y2-14),(x2+10,y2-14)]
 else:pts=[(x2,y2),(x2-10,y2+14),(x2+10,y2+14)]
 d.polygon(pts,fill=color)
 svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="4"/>')
 svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="'+color+'"/>')

text(45,25,"The nonunital index: take the exact scalar kernels",40,True)
text(45,86,"All n ≥ 1; A⁺ is the external coefficient unitization. Three exact symbol rows.",25)
xs=[70,615,1160]
text(45,139,"Unitalized coefficient calculus",27,True)
box(xs[0],185,"B(A⁺)","A⁺ ⋊ ℝⁿ","#e5edfa")
box(xs[1],185,"E(A⁺)","Completed order-zero calculus","#e5edfa")
box(xs[2],185,"C(Sⁿ⁻¹,A⁺)","Principal symbols","#e5edfa")
arrow(530,250,600,250);arrow(1075,250,1145,250)
text(23,233,"0",24);arrow(43,250,60,250)
arrow(1620,250,1640,250);text(1645,233,"0",24)
for i in range(3):
 x=xs[i]+180
 arrow(x,330,x,507)
 arrow(x+72,507,x+72,330,"#368261")
 text(xs[i]+55,366,["q_B","q_E","q_S"][i],27,True)
 text(xs[i]+270,405,["s_B","s_E","s_S"][i],27,True)
box(xs[0],517,"B(ℂ)","C*(ℝⁿ) = C₀(ℝⁿ)","#fff0d9")
box(xs[1],517,"E(ℂ)","C(Xₙ), radial compactification","#fff0d9")
box(xs[2],517,"C(Sⁿ⁻¹)","Scalar principal symbols","#fff0d9")
arrow(530,582,600,582);arrow(1075,582,1145,582)
text(23,565,"0",24);arrow(43,582,60,582)
arrow(1620,582,1640,582);text(1645,565,"0",24)
text(45,674,"Take the kernels of q_B, q_E, q_S: the coefficient-A row",27,True)
box(xs[0],727,"B(A) = ker q_B","(7.U3): split ideal sequence","#e1f0e7")
box(xs[1],727,"E(A) = ker q_E","Step 2: actual A-symbol closure","#e1f0e7")
box(xs[2],727,"C(Sⁿ⁻¹,A) = ker q_S","(7.U5): lift, then subtract s_B(c)","#e1f0e7")
arrow(530,792,600,792);arrow(1075,792,1145,792)
text(23,775,"0",24);arrow(43,792,60,792)
arrow(1620,792,1640,792);text(1645,775,"0",24)
text(45,899,"Step 3: E(A) restricts faithfully into M(B(A)).  Step 4: K-theory ideal maps are injective.",26,True)
text(45,948,"i_B* ∂A[u] = Φ(A⁺) Ψ(A⁺)⁻¹ i_S* red[u] = i_B* Φ(A) Ψ(A)⁻¹ red[u]",27)
text(45,994,"Cancel i_B*: the same ordered index identity holds in K₀(B(A)). Proof: (7.U6)–(7.U7).",26)
text(45,1058,"Original diagram. Proof: Theorem 7.3a, steps 1–4, (7.U1)–(7.U7).",24)
text(45,1092,"Human context: Connes, C*-algebras and Differential Geometry, author English edition p.7.",24)
svg.append("</svg>")
(OUT/"nonunital-action-index.svg").write_text("\n".join(svg)+"\n",encoding="utf-8")
im.save(OUT/"nonunital-action-index.png")

"""Editable original SVG: smoothing, closure and all trefoil states. CC0."""
from pathlib import Path
from html import escape
OUT=Path(__file__).with_suffix(".svg")
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="560" height="1590" viewBox="0 0 560 1590" role="img" aria-labelledby="title desc">',
 '<title id="title">From a crossing to the Jones polynomial</title>',
 '<desc id="desc">The northeast to southwest overstrand is positive when both strands point down. Its A smoothing is vertical. Closing a new strand multiplies the bracket by delta, while closing a cup cap contributes no new circle. All eight trefoil states and the exact operator trace normalization are displayed.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10" fill="#17466b"/></marker></defs>',
 '<rect width="560" height="1590" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#142b3e;white-space:pre}.head{font-size:25px;font-weight:bold}.math{font-family:Georgia,serif;font-size:23px}.small{font-size:18px}.line{fill:none;stroke:#17466b;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}.panel{fill:#f4f8fb;stroke:#b8cddd;stroke-width:1.5}</style>']
sup=dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿʷ","0123456789−nw"))
sub=dict(zip("₀₁₂₃₄₅₆₇₈₉₋ᵢₙ₊","0123456789−in+"))
def formatted(s):
 # Explicit tspans avoid dependence on a font's Unicode superscript glyphs.
 result=[];i=0
 while i<len(s):
  if s[i] in sup or s[i] in sub:
   mapping=sup if s[i] in sup else sub;shift="super" if mapping is sup else "sub"
   j=i
   while j<len(s) and s[j] in mapping: j+=1
   result.append(f'<tspan baseline-shift="{shift}" font-size="70%">'+escape("".join(mapping[c] for c in s[i:j]))+"</tspan>")
   i=j
  elif s[i:i+2]=="gβ":
   result.append('g<tspan baseline-shift="sub" font-size="70%">β</tspan>');i+=2
  else: result.append(escape(s[i]));i+=1
 return "".join(result)
def text(x,y,s,cls="",anchor="start"):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" xml:space="preserve">{formatted(s) if cls=="math" else escape(s)}</text>')
def path(d,arrow=False):
 parts.append(f'<path class="line" d="{d}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def panel(y,h): parts.append(f'<rect class="panel" x="12" y="{y}" width="536" height="{h}" rx="12"/>')
def crossing(x,y,size=70,arrows=False):
 # Understrand NW-SE has a real gap; NE-SW overstrand is continuous.
 s=size/2;g=9
 path(f"M{x-s} {y-s} L{x-g} {y-g}")
 path(f"M{x+g} {y+g} L{x+s} {y+s}",arrows)
 path(f"M{x+s} {y-s} L{x-s} {y+s}",arrows)
def vertical(x,y):
 path(f"M{x-35} {y-35} L{x-35} {y+35}")
 path(f"M{x+35} {y-35} L{x+35} {y+35}")
def cupcap(x,y):
 path(f"M{x-35} {y-35} Q{x} {y+3} {x+35} {y-35}")
 path(f"M{x-35} {y+35} Q{x} {y-3} {x+35} {y+35}")
text(280,37,"From a crossing to a polynomial","head","middle")
panel(57,270)
text(30,93,"1. Fix the crossing and its two channels","head")
crossing(107,173,74,True);vertical(285,173);cupcap(452,173)
text(107,238,"positive B","math","middle")
text(285,238,"A · I","math","middle")
text(452,238,"A⁻¹ · U","math","middle")
text(30,280,"B = A I + A⁻¹ U","math")
text(30,309,"δ = −A² − A⁻²       U² = δ U","math")
panel(341,325)
text(30,378,"2. Close the added strand","head")
vertical(112,460)
path("M147 425 C227 399 227 521 147 495")
cupcap(365,460)
path("M400 425 C480 399 480 521 400 495")
text(113,532,"I gives δ · I","math","middle")
text(370,532,"U gives I","math","middle")
text(30,580,"Cₙ₊₁(x) = δ Cₙ(x)","math")
text(30,613,"Cₙ₊₁(x Uₙ) = Cₙ(x)","math")
text(30,645,"Positive curl: Aδ + A⁻¹ = −A³","math")
panel(680,585)
text(30,718,"3. Close the positive three-crossing braid","head")
x1,x2=92,162
for y in [788,858,928]: crossing(127,y,70)
path("M92 753 C28 710 28 1003 92 963")
path("M162 753 C217 710 217 1003 162 963")
text(127,1009,"σ₁³, writhe 3","math","middle")
text(259,768,"state","small");text(352,768,"circles","small");text(441,768,"weight","small")
rows=[("III",2,"A³δ"),("IIU",1,"A"),("IUI",1,"A"),("UII",1,"A"),
      ("IUU",2,"A⁻¹δ"),("UIU",2,"A⁻¹δ"),("UUI",2,"A⁻¹δ"),("UUU",3,"A⁻³δ²")]
for i,(s,l,w) in enumerate(rows):
 y=807+30*i
 text(263,y,s,"math");text(380,y,str(l),"math","middle");text(474,y,w,"math","middle")
text(30,1081,"All 8 states: A³δ + 3A + 3A⁻¹δ + A⁻³δ²","math")
text(30,1119,"Bracket = −A⁵ − A⁻³ + A⁻⁷","math")
text(30,1157,"Multiply by (−A³)⁻³ = −A⁻⁹","math")
text(30,1195,"F(A) = A⁻⁴ + A⁻¹² − A⁻¹⁶","math")
text(30,1235,"t = A⁻⁴       V(t) = t + t³ − t⁴","math")
panel(1279,279)
text(30,1318,"4. The exact operator trace conversion","head")
text(30,1360,"δ₀ = √d = −A₀² − A₀⁻²","math")
text(30,1400,"gᵢ = A₀ · 1 + A₀⁻¹ δ₀ eᵢ₋₁","math")
text(30,1444,"V(A₀⁻⁴) = (−A₀³)⁻ʷ δ₀ⁿ⁻¹ τ(gβ)","math")
text(30,1487,"n strands; w is the signed crossing sum.")
text(30,1523,"Trace gives an evaluation of the polynomial.","small")
text(280,1582,"Proofs: 45.1–45.4; trefoil: 45.5. Original figure · CC0","small","middle")
parts.append("</svg>")
OUT.write_text("\n".join(parts)+"\n",encoding="utf-8")
print(OUT.name)

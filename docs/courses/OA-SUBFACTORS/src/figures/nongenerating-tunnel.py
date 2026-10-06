"""Original editable figure for the index-nine tunnel argument. CC0."""
from pathlib import Path
from html import escape
sup=dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿʷ","0123456789−nw"))
sub=dict(zip("₀₁₂₃₄₅₆₇₈₉₋ᵢₙ₊","0123456789−in+"))
def formatted(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] in sup or s[i] in sub:
            mapping = sup if s[i] in sup else sub
            shift = 'super' if mapping is sup else 'sub'
            j = i
            while j < len(s) and s[j] in mapping:
                j += 1
            result.append(f'<tspan baseline-shift="{shift}" font-size="70%">' + escape(''.join((mapping[c] for c in s[i:j]))) + '</tspan>')
            i = j
        elif s[i:i + 2] == 'gβ':
            result.append('g<tspan baseline-shift="sub" font-size="70%">β</tspan>')
            i += 2
        else:
            result.append(escape(s[i]))
            i += 1
    return ''.join(result)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="560" height="1510" viewBox="0 0 560 1510" role="img" aria-labelledby="title desc" style="max-width:100%;height:auto">',
 '<title id="title">A boundary survives in an index-nine tunnel</title>',
 '<desc id="desc">The root of the infinite three regular tree has branch values two thirds, one sixth and one sixth for an explicit harmonic function. A rank one cup in two three dimensional matrix factors has trace one ninth. The central martingale retains variance at least one eighteenth, so no tunnel closure is a factor. The adjacency norm squared is eight, below index nine.</desc>',
 '<style>text{font:20px Arial,sans-serif;fill:#162e43;white-space:pre}.head{font-size:24px;font-weight:bold}.math{font:23px Georgia,serif}.small{font-size:18px}.node-label{paint-order:stroke;stroke:#f5f8fb;stroke-width:6px;stroke-linejoin:round}.panel{fill:#f5f8fb;stroke:#bfd0dd;stroke-width:1.5}.edge{stroke:#51718c;stroke-width:3;fill:none}.chosen{stroke:#c27121;stroke-width:4;fill:none}</style>',
 '<rect width="560" height="1510" fill="white"/>']
def text(x,y,s,cls="",anchor="start"):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" xml:space="preserve">{formatted(s) if "math" in cls.split() else escape(s)}</text>')
def panel(y,h): parts.append(f'<rect class="panel" x="12" y="{y}" width="536" height="{h}" rx="10"/>')
def edge(x1,y1,x2,y2,chosen=False):
 parts.append(f'<path class="{"chosen" if chosen else "edge"}" d="M{x1} {y1} L{x2} {y2}"/>')
def node(x,y,label,value,chosen=False):
 parts.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{"#c27121" if chosen else "#51718c"}"/>')
 text(x,y+32,label,"math node-label","middle");text(x,y+61,value,"math node-label","middle")
text(280,35,"A boundary survives in a tunnel","head","middle")
panel(54,420);text(30,90,"1. The infinite 3-regular endpoint tree","head")
edge(280,122,94,202,True);edge(280,122,280,202);edge(280,122,466,202)
for x,parent,chosen in [(57,94,True),(131,94,True),(243,280,False),(317,280,False),(429,466,False),(503,466,False)]:
 edge(parent,202,x,332,chosen)
parts.append('<circle cx="280" cy="122" r="9" fill="#51718c"/>')
text(280,154,"root 1: h = 1/3","small node-label","middle")
node(94,202,"1","h = 2/3",True);node(280,202,"a","h = 1/6");node(466,202,"b","h = 1/6")
for x,label,value,chosen in [(57,"a⁻¹","5/6",True),(131,"b⁻¹","5/6",True),(243,"a","1/12",False),(317,"ab⁻¹","1/12",False),(429,"b","1/12",False),(503,"ba⁻¹","1/12",False)]:
 node(x,332,label,value,chosen)
text(30,443,"Parities: even root → odd → even; branches continue.","small")
panel(488,300);text(30,526,"2. An actual Jones cup","head")
cell=16
for i in range(9):
 for j in range(9):
  color="#357294" if i in [0,4,8] and j in [0,4,8] else "#fff"
  parts.append(f'<rect x="{32+j*cell}" y="{551+i*cell}" width="{cell}" height="{cell}" fill="{color}" stroke="#b6cad7" stroke-width="0.7"/>')
text(238,582,"p² = p","math");text(238,624,"τ(p) = 1/9","math")
text(238,664,"Rank one in M₃ ⊗ M₃","small")
text(30,728,"φ₊φ₋(R) ⊂ φ₊(R) ⊂ R","math")
text(30,765,"Each of the 9 colored entries is 1/3.","small")
panel(802,400);text(30,839,"3. The first central value already varies","head")
for x,value,chosen in [(50,"2/3",True),(218,"1/6",False),(386,"1/6",False)]:
 parts.append(f'<rect x="{x}" y="864" width="124" height="64" fill="{"#fff1df" if chosen else "#e9f2f8"}" stroke="#90aebe"/>')
 text(x+62,905,value,"math","middle")
text(30,970,"z₁ in D₀ = ℂ³; each block has trace 1/3.","small")
text(30,1013,"E(Dₙ₋₁)(zₙ₊₁) = zₙ","math")
text(30,1055,"0 ≤ zₙ ≤ 1        zₙ → z in L²","math")
text(30,1097,"z ∈ Z(C),    τ(z) = 1/3","math")
text(30,1141,"‖z − (1/3)1‖₂² ≥ 1/18","math")
text(30,1180,"C = closure of the tunnel relative commutants.","small")
panel(1216,259);text(30,1254,"4. The two infinite-depth tests fail","head")
text(30,1298,"Graph: ‖Γ‖² = (2√2)² = 8 < 9","math")
text(30,1342,"Inclusion: [R : φ₊(R)] = 9","math")
text(30,1385,"Every tunnel has the same traced closure.","small")
text(30,1423,"Its nonscalar center prevents generation.","small")
text(280,1500,"Proofs 46.1–46.8 · finite truncation of an infinite tree · CC0","small","middle")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")
print("nongenerating-tunnel.svg")

"""A nonfactor Markov example makes the normal pull-down map explicit."""
from pathlib import Path
from html import escape
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1000" role="img" aria-labelledby="title desc">',
         '<title id="title">Pull-down assembles columns of a matrix</title>',
         '<desc id="desc">For diagonal C2 inside M2, the basic construction is two copies of M2. The Jones projection selects column one in the first block and column two in the second. The Markov coefficient is one half. Pull-down forms the common matrix with column one from X and column two from Y. Taking X=E11 and Y=E12 gives norm square two, attaining the square root two bound.</desc>',
         '<rect width="560" height="1000" fill="#ffffff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#15283b}.small{font-size:17px}.body{font-size:20px}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}</style>']
def text(x,y,value,cls="body",anchor="start"):
    label = escape(value).replace("e_A", 'e<tspan baseline-shift="sub" font-size="70%">A</tspan>')
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{label}</text>')
def box(y,h,color="#edf4fb"):
    parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
def matrix(x,y,labels,colors):
    for i in range(2):
        for j in range(2):
            parts.append(f'<rect x="{x+75*j}" y="{y+45*i}" width="75" height="45" fill="{colors[j]}" stroke="#9cb4cd"/>')
            text(x+75*j+37.5,y+45*i+28,labels[i][j],"body","middle")
text(280,38,"Pull-down assembles bounded columns","head","middle")
box(62,151)
text(40,97,"A = diagonal C²  ⊂  B = M₂","label")
text(40,133,"B₁ = M₂ ⊕ M₂,     x ∈ B ↦ (x,x)")
text(40,168,"e_A = (E₁₁,E₂₂),    λ = 1/2","label")
text(40,196,"Minimal-projection trace weight: 1/4 in each block","small")
box(236,208,"#f0f7f0")
text(40,271,"Two basic-construction blocks","label")
text(147,301,"X","label","middle")
text(407,301,"Y","label","middle")
matrix(72,318,[["x₁₁","x₁₂"],["x₂₁","x₂₂"]],["#a8d2e9","#e3edf2"])
matrix(332,318,[["y₁₁","y₁₂"],["y₂₁","y₂₂"]],["#e3edf2","#f0c9aa"])
text(40,428,"Block products: XE₁₁ and YE₂₂ retain columns 1 and 2.","small")
box(468,196,"#fff5e8")
text(40,504,"R(X,Y) = XE₁₁ + YE₂₂","label")
matrix(205,522,[["x₁₁","y₁₂"],["x₂₁","y₂₂"]],["#a8d2e9","#f0c9aa"])
text(40,646,"R(X,Y)e_A = (XE₁₁,YE₂₂) = (X,Y)e_A","small")
box(687,139,"#f2eefb")
text(40,724,"Norm bound attained","label")
text(40,759,"X = E₁₁,   Y = E₁₂,   ‖(X,Y)‖ = 1","small")
text(40,796,"R = E₁₁ + E₁₂,     RR* = 2E₁₁,     ‖R‖ = √2","small")
box(849,104)
text(40,885,"Direct sums retain the same scalar λ = 1/2.","label")
text(40,920,"Original component masses can be 1/3 and 2/3.","small")
text(40,981,"Proposition 8.8 and Exercise 8.5","small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

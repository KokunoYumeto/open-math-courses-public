"""Exact row and multiplicity compression, with the dimension uniqueness bounds."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1110" role="img" aria-labelledby="title desc">',
 '<title id="title">Rows and multiplicity columns use different dimension normalizations</title>',
 '<desc id="desc">M3 acts on C3 tensor C5. A three by five coordinate array has dimension five thirds over M3. A rank two algebra projection keeps two rows, giving dimension five halves over M2. A rank two commutant projection keeps two columns, giving dimension two thirds over M3. Algebra trace two thirds divides the old dimension; commutant trace two fifths multiplies it. The bottom panel gives floor nt over n less than or equal to D(H) less than or equal to ceil nt over n, an interval of width at most one over n, from the two reducing module embeddings in Theorem 2.10.</desc>',
 '<rect width="560" height="1110" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#15283b}.head{font-size:22px;font-weight:bold}.label{font-size:19px;font-weight:bold}.small{font-size:17px}</style>']
def text(x,y,value,cls="small",anchor="start"):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,h,color):
 parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
def grid(y,mode):
 for j in range(5): text(68+43*j,y-9,str(j+1),"small","middle")
 for i in range(3):
  text(35,y+35*i+23,str(i+1),"small","middle")
  for j in range(5):
   selected=mode=="all" or (mode=="rows" and i<2) or (mode=="columns" and j<2)
   color=("#d8ebfa" if mode!="columns" else "#ffe4be") if selected else "#f1f1f1"
   parts.append(f'<rect x="{47+43*j}" y="{y+35*i}" width="43" height="35" fill="{color}" stroke="#627c94" stroke-width="0.7"/>')
   if not selected:
    parts.append(f'<path d="M {52+43*j} {y+35*i+5} l 33 25" stroke="#b8b8b8"/>')
 text(298,y+31,"Rows: algebra coordinates")
 text(298,y+68,"Columns: multiplicity")
text(280,35,"Two compressions, two normalizations","head","middle")
box(59,228,"#edf4fb")
text(40,96,"Original:  M₃ on ℂ³ ⊗ ℂ⁵","label")
grid(135,"all")
text(40,269,"dim = 5/3; ordinary Hilbert dimension = 15")
box(307,230,"#f0f7f0")
text(40,345,"Algebra projection e: keep two rows","label")
grid(384,"rows")
text(40,516,"M₂ on ℂ² ⊗ ℂ⁵;  dim = (5/3)/(2/3) = 5/2")
box(557,230,"#fff5e8")
text(40,595,"Commutant projection q: keep two columns","label")
grid(634,"columns")
text(40,766,"M₃ on ℂ³ ⊗ ℂ²;  dim = (2/5)(5/3) = 2/3")
box(807,225,"#f2eefb")
text(40,846,"Additivity and normalization force uniqueness","label")
text(40,884,"t = dimₚ H;  aₙ = floor(nt);  bₙ = ceil(nt)")
text(40,921,"aₙ standard copies  ↪  n copies of H  ↪  bₙ copies")
text(40,958,"aₙ/n ≤ D(H) ≤ bₙ/n;  interval width ≤ 1/n")
text(40,996,"All finite factors; arbitrary Hilbert multiplicity")
text(40,1068,"Proposition 2.9; Theorem 2.10; Example 2.11")
text(40,1094,"Equations (2.4)–(2.7); row and column ranks both two")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

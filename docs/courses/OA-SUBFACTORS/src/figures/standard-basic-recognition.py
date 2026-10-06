"""The exact corner and conjugation maps in the standard recognition proof."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1080" role="img" aria-labelledby="title desc">',
 '<title id="title">A full corner determines the standard upper algebra</title>',
 '<desc id="desc">For P inside Q inside R on a standard space, compression gives a faithful normal expectation. The conditions on e imply P prime inside J R J and equality of their e corners. Full central support in P prime supplies bounded finite cutoffs converging strongly to one. These recover every operator from the corner and prove J R J equals P prime, hence R equals J P prime J.</desc>',
 '<rect width="560" height="1080" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#15283b}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}.small{font-size:17px}</style>']
def text(x,y,value,cls="small",anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,h,color):
    parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
def arrow(y): text(280,y,"↓","head","middle")
text(280,38,"A full corner determines the upper algebra","head","middle")
box(62,162,"#edf4fb")
text(40,99,"P ⊂ Q ⊂ R;  Q standard on H,  JQJ = Q′","label")
text(40,137,"e ∈ R ∩ P′;  P = Q ∩ {e}′;  Pe = eRe")
text(40,176,"z of e in P′ = 1;  JeJ = e")
text(40,208,"No factor, trace, finite-index or state assumption")
arrow(251)
box(266,129,"#f0f7f0")
text(40,304,"Compression gives E: Q → P","label")
text(40,342,"θ(p) = pe is faithful and normal;  E(x) = θ⁻¹(exe)")
text(40,374,"E is normal, completely positive, unital and faithful")
arrow(423)
box(438,158,"#fff5e8")
text(40,476,"Conjugation compares two commutant algebras","label")
text(40,516,"A = P′ ⊂ B = JRJ;  e ∈ A has full central support")
text(40,555,"eBe = J(eRe)J ⊂ eQ′e ⊂ eAe ⊂ eBe")
text(40,582,"Therefore eBe = eAe")
arrow(624)
box(639,223,"#f2eefb")
text(40,677,"Bounded finite cutoffs recover each x ∈ B","label")
text(40,716,"T = Σ ueu*;  h = T(T + ε1)⁻¹;  0 ≤ h ≤ 1")
text(40,755,"h = Σ aᵤeaᵤ*;  aᵤ = (T + ε1)⁻¹ᐟ²u")
text(40,794,"hxh = Σ aᵤ[e(aᵤ*xaᵥ)e]aᵥ* ∈ A")
text(40,833,"h → 1 strongly;  ‖hxh‖ ≤ ‖x‖;  hence x ∈ A")
arrow(891)
box(906,120,"#edf4fb")
text(40,947,"P′ = JRJ;  R = JP′J = ⟨Q,e⟩","label")
text(40,986,"The corner witnesses the algebra in its standard position")
text(40,1057,"Lemmas 43.1–43.2 and Theorem 43.3; (43.2)–(43.11)")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

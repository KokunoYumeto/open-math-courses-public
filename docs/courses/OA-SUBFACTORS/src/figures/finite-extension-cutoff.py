"""The central parts and exact finite path cutoff of Theorem 44.2."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1020" role="img" aria-labelledby="title desc">',
 '<title id="title">The extra scalar block at the finite path cutoff</title>',
 '<desc id="desc">For r at least four, lambda is one over four cosine squared pi over r. Compression recognizes the basic-construction part of B. A scalar common-kernel block s is allowed in B. The canonical new scalar block exists for k at most r minus four, disappears at k equals r minus three, and the old projection join forces s zero for k at least r minus two. At r four and k one, two rank-one projections supported on the first two coordinates of C cubed satisfy the half sandwich relations. Their target is M2 plus C, while the canonical source is M2.</desc>',
 '<rect width="560" height="1020" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#15283b}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}.small{font-size:17px}</style>']
def text(x,y,value,cls="small",anchor="start"):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,h,color):
 parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
text(280,38,"A finite extension sees two central parts","head","middle")
box(62,175,"#edf4fb")
text(40,98,"r ≥ 4;  λ = 1 / [4 cos²(π/r)];  Aₖ = Pₖ₊₁","label")
text(40,135,"f ∈ Aₖ₋₁′;  z of f in Aₖ₋₁′ = 1")
text(40,173,"fqₖf = λf;  qₖfqₖ = λqₖ")
text(40,211,"B = ⟨Aₖ,f⟩;  s = 1 − (q₁ ∨ ··· ∨ qₖ ∨ f)")
text(280,264,"↓","head","middle")
box(280,153,"#f0f7f0")
text(40,318,"Recognized ideal:  B(1−s) ≅ (Aₖ)₁","label")
text(40,356,"fxf = Eₖ(x)f;  old algebra and Jones projection preserved")
text(40,395,"Complement:  Bs = ℂs;  every projection is zero there")
box(453,240,"#fff5e8")
text(40,491,"When does Aₖ₊₁ map onto B?","label")
text(40,534,"k ≤ r−4:   new scalar frontier exists; map always exists")
text(40,564,"                   s = 0 kills that frontier; s ≠ 0 preserves it")
text(40,607,"k = r−3:   frontier disappears; map exists iff s = 0")
text(40,650,"k ≥ r−2:   old join is already 1; s = 0 automatically")
box(713,229,"#f2eefb")
text(40,751,"Cutoff example:  r = 4,  k = 1,  λ = 1/2","label")
text(40,790,"H = ℂ³;  q₁ projects onto (1,0,0)")
text(40,829,"f projects onto (1,1,0)/√2;  s projects onto (0,0,1)")
text(40,868,"A₀′ = M₃:  f has full central support")
text(40,910,"Canonical source M₂;  target M₂ ⊕ ℂ;  no onto map")
text(40,982,"Theorem 44.2; Proposition 44.3; equations (44.5)–(44.14)")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

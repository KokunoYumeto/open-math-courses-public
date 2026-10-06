"""The actual block ranges in the index-four II1 tensor inclusion."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1320" role="img" aria-labelledby="title desc">',
 '<title id="title">One shared vector specifies the embedded fusion range</title>',
 '<desc id="desc">For N equal to one tensor Q in M2 tensor Q, index four, the basic construction is M4 tensor Q. The four rank-one coordinate projections resolve the identity. The old M acts by two identical blocks X,X. Independent vectors in the four fusion terms allow independent blocks X1,X2. The conditional expectation averages those two blocks. The witness E11,0 has expectation E11 over two in both blocks, with squared L2 distance one eighth. The bounded matrix coordinates are displayed; Hilbert ranges are their L2 closures with Q coefficients.</desc>',
 '<rect width="560" height="1320" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#15283b}.head{font-size:22px;font-weight:bold}.label{font-size:19px;font-weight:bold}.small{font-size:17px}</style>']
def text(x,y,value,cls="small",anchor="start"):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,h,color):
 parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
def blockmatrix(x,y,independent=False):
 labels=[["a","b","0","0"],["c","d","0","0"],
         ["0","0","w" if independent else "a","x" if independent else "b"],
         ["0","0","y" if independent else "c","z" if independent else "d"]]
 for i in range(4):
  for j in range(4):
   fill="#ffffff" if i//2!=j//2 else "#ffe4be" if independent and i>=2 else "#d8ebfa"
   parts.append(f'<rect x="{x+30*j}" y="{y+30*i}" width="30" height="30" fill="{fill}" stroke="#627c94" stroke-width="0.7"/>')
   text(x+30*j+15,y+30*i+22,labels[i][j],"small","middle")
text(280,36,"One shared vector fixes the fusion range","head","middle")
box(61,155,"#edf4fb")
text(40,99,"N = 1 ⊗ Q ⊂ M = M₂ ⊗ Q;  d = 4,  λ = 1/4","label")
text(40,137,"B = M₄ ⊗ Q;  uᵢⱼ = √2 Eᵢⱼ ⊗ 1")
text(40,174,"pᵢⱼ = uᵢⱼ e uᵢⱼ*;  Σ pᵢⱼ = 1")
text(40,199,"Basis order:  v₁₁, v₂₁ | v₁₂, v₂₂")
box(238,309,"#f0f7f0")
text(40,277,"Correlated: one ξ in every term","label")
text(40,316,"Sξ = (1/2) Σ (ξuᵢⱼ) ⊠ uᵢⱼ*")
text(40,355,"Under V:  Σ ξpᵢⱼ = ξ")
text(40,389,"Old bounded matrices:  diag(X,X)")
blockmatrix(60,409)
text(224,441,"The same a,b,c,d in both blocks")
text(224,482,"a,b,c,d ∈ Q: four coefficients")
text(224,523,"Closed range: L²(M)")
box(568,300,"#fff5e8")
text(40,607,"Independent: a separate ξᵢⱼ in each term","label")
text(40,646,"Under V:  Σ ξᵢⱼpᵢⱼ; bounded matrices diag(X₁,X₂)")
blockmatrix(60,679,independent=True)
text(224,712,"a,b,c,d and w,x,y,z ∈ Q")
text(224,751,"Two independent blocks")
text(224,790,"Eight coefficients; range L²(C)")
text(40,839,"The eight entries can vary independently")
text(280,899,"↓  orthogonal projection onto L²(M)","label","middle")
box(922,126,"#edf4fb")
text(40,961,"diag(X₁,X₂) ↦ diag((X₁+X₂)/2,(X₁+X₂)/2)")
text(40,1002,"The old range requires the two blocks to agree")
box(1069,155,"#f2eefb")
text(40,1108,"Witness:  p₁₁ = diag(E₁₁,0) ⊗ 1","label")
text(40,1147,"Projection:  diag(E₁₁/2,E₁₁/2) ⊗ 1")
text(40,1186,"Squared L² distance:  1/4 − 1/8 = 1/8 > 0")
text(40,1261,"Lemma 6.8; Propositions 6.9 and 6.11; (6.5)–(6.13)")
text(40,1287,"Bounded matrices shown; Hilbert ranges are their L² closures")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

"""Typed alternating words, conjugate reversal, and the unequal odd traces."""
from pathlib import Path
from html import escape
import re
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1400" role="img" aria-labelledby="title desc">',
 '<title id="title">Two fusion directions and their different roots</title>',
 '<desc id="desc">The right sequence H begins at the N unit, fixes left N, and has endomorphism blocks A n minus one. The left sequence L begins at the M unit, fixes right M, and has blocks opposite B n. Its left endomorphism factors are opposite M n. The dual right sequence K is conjugated to L by reversing the word and taking adjoints. The linear map C a star C inverse reverses products and preserves the dual tower trace. H and L share their odd words, giving A two j isomorphic to opposite B two j plus one. Their even roots differ. In the actual diagonal corner inclusion with t one third and index nine halves, the same odd projection has right endomorphism trace one third and left endomorphism trace two thirds.</desc>',
 '<rect width="560" height="1400" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#15283b}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}.small{font-size:17px}.word{font-size:18px}</style>']
def text(x,y,value,cls="small",anchor="start"):
 value=re.sub(r"_([NM])",lambda m:f'<tspan baseline-shift="sub" font-size="70%">{m[1]}</tspan>',escape(value))
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{value}</text>')
def box(y,h,color):
 parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')
def rows(y,values):
 text(40,y,"Word","label");text(292,y,"Outer factors","small");text(445,y,"Bimod. End","small")
 for i,(word,outer,end) in enumerate(values):
  pos=y+38*(i+1)
  text(40,pos,word,"word");text(305,pos,outer,"word");text(459,pos,end,"word")
text(280,36,"The two fusion directions","head","middle")
box(58,287,"#edf4fb")
text(40,94,"Right fusion: fixed left N, root 1_N","label")
rows(127,[("H₀ = 1_N","N–N","ℂ"),("H₁ = X","N–M","A₀"),
          ("H₂ = X ⊠_M X̄","N–N","A₁"),("H₃ = X ⊠_M X̄ ⊠_N X","N–M","A₂")])
text(40,315,"Right End: T₀ = N;  Tₙ = Mₙ₋₁ for n ≥ 1")
box(366,287,"#f0f7f0")
text(40,402,"Left fusion: fixed right M, root 1_M","label")
rows(435,[("L₀ = 1_M","M–M","B₀ᵒᵖ"),
          ("L₁ = X","N–M","B₁ᵒᵖ"),("L₂ = X̄ ⊠_N X","M–M","B₂ᵒᵖ"),
          ("L₃ = X ⊠_M X̄ ⊠_N X","N–M","B₃ᵒᵖ")])
text(40,623,"Left End: Mₙᵒᵖ at every level n ≥ 0")
box(674,261,"#f2eefb")
text(40,710,"Dual right sequence and conjugate reversal","label")
text(40,748,"K₀ = 1_M;  K₁ = X̄;  K₂ = X̄ ⊠_N X")
text(40,783,"K₃ = X̄ ⊠_N X ⊠_M X̄;  outer factors M–Pₙ")
text(40,818,"Cₙ: Kₙ → Lₙ is antiunitary; reverses words")
text(40,853,"θₙ(a) = Cₙ a* Cₙ⁻¹;  θₙ(ab) = θₙ(b)θₙ(a)")
text(40,891,"θₙ preserves the dual tower trace")
box(956,162,"#fff5e8")
text(40,992,"Shared odd words, two even categories","label")
text(40,1027,"H₁ = L₁ = X;  H₃ = L₃ = X ⊠_M X̄ ⊠_N X")
text(40,1062,"A₂ⱼ ≅ B₂ⱼ₊₁ᵒᵖ;  even roots 1_N and 1_M")
text(40,1097,"Right and left inclusions act at different ends")
box(1139,167,"#fceeed")
text(40,1175,"Actual diagonal corners: t = 1/3, d = 9/2","label")
text(40,1211,"The same p on X has right End trace 1/3")
text(40,1247,"Left End trace: 1/(dt) = 2/3")
text(40,1283,"Odd algebra identification need not preserve traces")
text(40,1345,"X̄ is the conjugate bimodule;  1_N = L²(N), 1_M = L²(M)")
text(40,1375,"Theorem 19.5; Corollary 19.6; Proposition 19.7")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

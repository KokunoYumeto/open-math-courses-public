"""Reproducible exact endpoint, density and weighted-spin diagram."""
from pathlib import Path
from html import escape

W,H=760,1120
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
       '<title id="title">Two-step Jones cups and composed densities</title>',
       '<desc id="desc">Five consecutive factors A through E, blocked triple A C E, normalized four-cup projection, inverse dual density cancellation, exact index, and four-site weighted-spin coefficients.</desc>',
       '<rect width="760" height="1120" fill="#f8fafc"/>']
def text(x,y,value,size=19,color="#142b43",anchor="start",weight="normal"):
    parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>')
def line(x1,y1,x2,y2,color="#365b80",width=2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
def box(x,y,w,h,fill="#ffffff",stroke="#a8bed2"):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{stroke}"/>')
text(30,38,"Two-step Jones cups",28,weight="bold")
text(30,66,"64.1–64.3: actual factors, projections, expectations and index",18)
text(30,99,"Every adjacent index is d; λ = 1/d.",18)
xs=[86,233,380,527,674]
for x,name in zip(xs,"ABCDE"):
    box(x-54,116,108,58)
    text(x,149,name,25,anchor="middle",weight="bold")
for x,y in zip(xs[:-1],xs[1:]):
    line(x+58,145,y-58,145)
    text((x+y)/2,141,"⊂",23,anchor="middle")
text(xs[2],204,"p₀ ∈ C",19,anchor="middle")
text(xs[3],204,"p₁ ∈ D",19,anchor="middle")
text(xs[4],204,"p₂ ∈ E",19,anchor="middle")
for x in [xs[0],xs[2],xs[4]]: line(x,224,x,248,"#0f766e",3)
line(xs[0],248,xs[4],248,"#0f766e",3)
text(380,277,"Blocked triple: A ⊂ C ⊂ E",22,"#0f766e",anchor="middle",weight="bold")
box(30,299,700,130)
text(50,330,"q = d p₁ p₀ p₂ p₁",23,weight="bold")
text(50,362,"q² = q     E_C(q) = λ²1     E = ⟨C, q⟩",21)
text(50,397,"[C : A] = [E : C] = d²;    τ_E(q) = λ²",21)
box(30,449,700,196,fill="#edf7f5",stroke="#79b8ad")
text(50,480,"Canonical adjacent cups and their cancellation",21,weight="bold")
text(50,514,"κ₀ ∈ A′∩B,   κ₁ ∈ B′∩C,   κ₂ = η₁(κ₁⁻¹) ∈ C′∩D",19)
text(50,548,"K = κ₀κ₁;   τ_C(K) = 1;   H = F₀ ∘ F₁",21)
text(50,582,"q′ = d r₁ r₀ r₂ r₁ = K½ q K½",22,weight="bold")
text(50,617,"E_C(q′) = λ²K;    sharp index of H is d²",21)
text(30,679,"64.5: the exact four-site spin projections",22,weight="bold")
text(30,708,"p + q = 1; r = √(pq); d = 1/(pq).",19)
box(30,724,700,150)
text(52,755,"Basis state",19,weight="bold")
for x,label in [(283,"0011"),(405,"0101"),(527,"1010"),(649,"1100")]:
    text(x,755,label,19,anchor="middle",weight="bold")
text(52,796,"Old vector ξ",19)
text(52,837,"Modified vector ζ",19)
for x,old,new in [(283,"q","p"),(405,"r","r"),(527,"r","r"),(649,"p","q")]:
    text(x,796,old,22,anchor="middle")
    text(x,837,new,22,"#0f766e",anchor="middle")
text(30,908,"Both vectors have norm 1 and weight 2; both cup traces are p²q².",18)
text(30,940,"K on the last two sites: diag((q/p)², 1, 1, (p/q)²).",19)
box(30,961,700,111,fill="#eaf0f8")
text(50,991,"At p = 1/4 and q = 3/4:",20,weight="bold")
text(50,1023,"d² = 256/9;  τ(G) = 9/256;  K = diag(9, 1, 1, 1/9)",19)
text(50,1055,"E_last two(G) = diag(81, 9, 9, 1)/256",19)
text(30,1100,"Finite blocking is proved. The general shifted comparison remains separate.",17)
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

"""The exact finite-window mechanism of Lemmas42.4–42.5 and Theorem42.6."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1090" role="img" aria-labelledby="title desc">',
         '<title id="title">A forbidden parameter gap bounds the length of a projection sequence</title>',
         '<desc id="desc">For a gap between a ell plus one and a ell, a long sequence has a first stalled kernel K n equal K n plus one, with two at most n at most ell minus one. Compression by K n minus two leaves a nonzero tail with orthogonal distant terms. That tail has at most ell minus one terms, so the original sequence has at most two ell minus three terms. At parameter two thirds the three projections e,f,e attain this bound.</desc>',
         '<rect width="560" height="1090" fill="#ffffff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#15283b}.small{font-size:17px}.body{font-size:20px}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}</style>']

def text(x,y,value,cls="body",anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y,h,color="#edf4fb"):
    parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')

def arrow(y):
    parts.append(f'<path d="M280,{y} v17 m-6,-6 l6,6 6,-6" fill="none" stroke="#52738e" stroke-width="2"/>')

text(280,38,"A gap gives a finite-length bound","head","middle")
box(62,133)
text(40,96,"aᵣ = 1 / (4 cos²(π/r)),     ℓ ≥ 3","label")
text(40,132,"aℓ₊₁ < λ < aℓ")
text(40,168,"P₀,…,Pℓ₋₁ > 0,      Pℓ < 0","small")
arrow(202)
box(228,159,"#f0f7f0")
text(40,263,"Long-sequence case: L ≥ ℓ","label")
text(40,299,"Kⱼ = 1 − (q₁ ∨ ⋯ ∨ qⱼ),    K₀ = 1","small")
text(40,334,"First stall: Kₙ = Kₙ₊₁,    2 ≤ n ≤ ℓ − 1","label")
text(40,369,"qₙ₊₁ ≤ q₁ ∨ ⋯ ∨ qₙ₋₁","small")
arrow(394)
box(420,158,"#fff5e8")
text(40,455,"Compress by Kₙ₋₂","label")
text(40,491,"rᵢ = qₙ₊ᵢ Kₙ₋₂ ≠ 0")
text(40,526,"Same adjacent relation, parameter λ","small")
text(40,558,"rᵢ rⱼ = 0 whenever |i − j| ≥ 2","small")
arrow(585)
box(610,163,"#f2eefb")
text(40,646,"Tail length = L − n + 1 ≤ ℓ − 1","label")
text(40,684,"A second stalled containment would make","small")
text(40,713,"a nonzero tail term orthogonal to its own range.","small")
text(40,750,"Therefore L ≤ n + ℓ − 2 ≤ 2ℓ − 3","label")
box(797,243)
text(40,833,"First gap example: λ = 2/3,   ℓ = 3","label")
text(40,872,"q₁ = q₃ = e,     q₂ = f,     efe = (2/3)e","small")
text(40,909,"K₁ = 1 − e,    K₂ = K₃ = 0","small")
text(40,946,"n = 2; compressed tail has 2 terms.","small")
text(40,986,"L = 3 = 2ℓ − 3","label")
text(40,1020,"Sharp here; no sharpness claim in later gaps.","small")
text(40,1070,"Lemmas 42.4–42.5; Theorem 42.6; equation 42.20","small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n",encoding="utf-8")

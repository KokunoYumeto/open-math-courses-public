"""Reproducible exact operator schematic for Figure81.1; standard library."""
from pathlib import Path
from html import escape
W,H=1000,1400
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="1000" height="1400" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182738}.title{font-size:25px;font-weight:700}.head{font-size:20px;font-weight:700}.text{font-size:18px}.small{font-size:16px}.blue{fill:#d9e9fa;stroke:#376fa3}.red{fill:#f7d8da;stroke:#a83f47}.green{fill:#d9eee3;stroke:#3e8260}.panel{fill:#fff;stroke:#aab8c9}</style>']
def text(x,y,s,cls='text'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def rect(x,y,w,h,cls):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>')
def panel(y,h,title):
 rect(24,y,952,h,'panel');text(44,y+34,title,'head')
text(28,38,'Relative norm averages → exact central density','title')
text(28,69,'Finite-index II₁ factors N ⊂ M; all finite expectations preserve the inherited trace τ.','small')
panel(92,268,'A. Spectral spike and its smaller-factor cover — Lemma 81.1')
rect(52,156,260,85,'blue');text(66,187,'q = 1{|b| > η} in M');text(66,218,'τ(q) ≤ ‖b‖₂² / η²')
text(331,204,'→','title')
rect(375,156,548,85,'green');text(391,187,'e = 1{Eₙ(q) ≥ θ} in N');text(391,218,'τ(e) ≤ 1/k;  ‖q(1 − e)‖ ≤ √(dθ)')
text(44,283,'Required input: ‖b‖ ≤ R and ‖b‖₂² ≤ η²θ/k.')
text(44,318,'The spike q need not lie in N. No commutation of q and e is assumed.')
panel(382,265,'B. Orthogonal images of e spread the covered spike — 81.3 and 81.6')
for j in range(4):
 x=60+214*j;rect(x,449,176,69,'blue');text(x+15,478,f'e{j+1} = u{j+1} e u{j+1}*');text(x+15,504,'in N; orthogonal','small')
text(44,561,'Schematic shows k = 4; the proof allows every positive integer k.')
text(44,601,'Final norm ≤ R/k + η + 2R√(dθ).')
text(504,601,'small block + remainder + endpoints','small')
panel(669,280,'C. Actual branch means follow the ambient expectation — Theorem 81.4')
rect(52,736,248,76,'blue');text(66,764,'g = Σᵢ aᵢ* aᵢ in R');text(66,793,'common basis; τ(g) = d')
text(319,782,'→','title')
rect(366,736,245,76,'green');text(381,764,'z = E꜀(g), C = N′ ∩ M');text(381,793,'z ∈ A′ ∩ B')
text(630,782,'→','title')
rect(677,736,246,76,'green');text(690,764,'Ψⱼ(z) = â′ⱼ');text(690,793,'a′ⱼ = E꜀ₛ(zqⱼ)')
text(44,855,'Ψⱼ(y) = Eₐ(xⱼ y xⱼ) is contractive and N-equivariant.')
text(44,893,'One common finite N-average sends every Hⱼ = Ψⱼ(g) to â′ⱼ in norm.')
text(44,928,'Here Cₛ = Z(S); xⱼ is a canonical lift, not an asserted physical element of M.','small')
panel(971,281,'D. The desired target agrees exactly when the normal densities agree — 81.5')
rect(52,1039,360,70,'blue');text(67,1067,'desired aⱼ = E꜀ₛ(gqⱼ)');text(67,1096,'proved mean a′ⱼ = E꜀ₛ(zqⱼ)')
rect(450,1039,474,70,'red');text(466,1067,'inf ‖average(Hⱼ) − âⱼ‖ = ‖a′ⱼ − aⱼ‖');text(466,1096,'Exact distance, not a claimed counterexample.','small')
text(44,1153,'All branch gaps vanish ⇔ Eᴅ₀(g) = Eᴅ₀(E꜀(g)).')
text(44,1192,'D₀ = Z(S) ∨ Z(R); general amenability ⇒ this identity remains unproved here.')
text(28,1291,'Rectangles and arrows are schematic; widths do not represent traces or spectral weights.','small')
text(28,1326,'Proof locators: 81.2–81.6 (spreading), 81.7–81.10 (norm mean), 81.13–81.16 (density).','small')
text(28,1361,'Human source: S. Popa (1999), relative Dixmier theorem, printed p.743; proof given here.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(parts)+'\n').encode())

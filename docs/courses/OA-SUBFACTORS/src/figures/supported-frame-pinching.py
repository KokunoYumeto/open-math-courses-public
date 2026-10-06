"""Reproduce Figure54.1: polar completion, trace capacity and pinching."""
from pathlib import Path
from html import escape

OUT=Path(__file__).with_suffix('.svg')
parts=[
 '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1530" viewBox="0 0 640 1530" role="img" aria-labelledby="title desc">',
 '<title id="title">Supported frame completion and simultaneous pinching</title>',
 '<desc id="desc">Polar completion retains the initial projection q and fills its missing spectral support inside p. Two orthogonal ranges of trace 51 over 100 exceed the trace of the unit. Simultaneous phase displacement removes off-diagonal blocks and reduces the sum of squared L2 errors by three quarters per refinement. The matrix examples and the abstract bounds are labelled separately.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
 '<rect width="640" height="1530" fill="#f9fcfe"/>']

def text(y,s,size=20,color='#163c50',weight='normal',x=320):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="middle" font-weight="{weight}">{escape(s)}</text>')
def box(y,h,fill='#eaf3f8'):
 parts.append(f'<rect x="24" y="{y}" width="592" height="{h}" rx="8" fill="{fill}" stroke="#6b96ad"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#315b70" stroke-width="2" marker-end="url(#arrow)"/>')

text(38,'Complete the support; pinch the errors',25,weight='bold')
text(71,'Normalized trace · exact hypotheses · squared energies',18)
box(94,465)
text(129,'1 · Polar completion inside pMq',23,weight='bold')
text(166,'y = w h½;  h = y*y;  s = support(h) ≤ q',20)
text(204,'Missing initial support',19,x=173)
text(204,'Available final support',19,x=467)
text(237,'q − s',23,weight='bold',x=173)
text(237,'p − ww*',23,weight='bold',x=467)
arrow(246,231,380,231)
text(268,'τ(p − ww*) ≥ τ(q − s) · comparison gives w₁',18)
text(310,'v = w + w₁;  v*v = q;  vv* ≤ p',22,weight='bold')
text(344,'‖v − y‖₂² = τ((q − h½)²) ≤ ‖h − q‖₂²',19)
parts.append('<line x1="45" y1="367" x2="595" y2="367" stroke="#6b96ad"/>')
text(397,'Actual M₄ example · Exercise 54.1',20,weight='bold')
text(433,'q = E₁₁ + E₂₂;   p = E₃₃ + E₄₄;   y = 2E₃₁',18)
text(467,'w = E₃₁;   w₁ = E₄₂;   v = E₃₁ + E₄₂',19)
text(502,'Initial: E₁₁ → final E₃₃;  E₂₂ → final E₄₄',18)
text(535,'Squared distance ½ ≤ Gram error 5/2 · (54.1)–(54.4)',17)

box(584,337,'#fff3ea')
text(620,'2 · Trace capacity cannot be perturbed away',22,'#713d26','bold')
text(657,'n orthogonal ranges equivalent to q need n τ(q) ≤ 1.',18,'#713d26')
# The bars represent cumulative trace of two proposed orthogonal ranges.
# Their lengths are exactly .51 and .51 against the unit of length500.
parts.append('<rect x="62" y="698" width="500" height="42" fill="#fff" stroke="#713d26"/>')
parts.append('<rect x="62" y="698" width="255" height="42" fill="#719bb3"/>')
parts.append('<rect x="317" y="698" width="255" height="42" fill="#d99c72"/>')
parts.append('<line x1="562" y1="689" x2="562" y2="753" stroke="#713d26" stroke-width="3"/>')
text(726,'51/100',19,'#fff','bold',x=188)
text(726,'51/100',19,'#482617','bold',x=440)
text(778,'Unit capacity = 1;  proposed total = 102/100',19,'#713d26')
text(813,'In M₁₀₀ ⊗ W, cross-Gram squared error = 2/100',18,'#713d26')
text(847,'(1/5)² τ(q) = 51/2500 > 2/100',19,'#713d26')
text(884,'Gram input passes; orthogonal output is impossible.',18,'#713d26')

box(946,443,'#e5f1e7')
text(983,'3 · One partition treats the whole finite tuple',23,weight='bold')
text(1020,'C = B′ ∩ M;  D = B ∨ C;  E_D(x) = 0 for every target',17)
text(1058,'E = Σₓ ‖Φ_P(x)‖₂² > 0',22,weight='bold')
text(1092,'Least-norm orbit hull contains the zero tuple.',18)
text(1126,'Choose u with summed squared displacement > E.',18)
arrow(320,1140,320,1170)
text(1201,'u₀ = Σⱼ λⱼeⱼ;  |λⱼ| = 1;  refine by eⱼpᵢ',19)
text(1235,'Orthogonal blocks: |λᵢ λ̄ⱼ − 1|² ≤ 4',19)
text(1271,'E < displacement ≤ 4(E − E_new)',21,weight='bold')
text(1306,'Therefore E_new < (3/4) E · (54.26)–(54.29)',19)
text(1352,'Diagonal B ⊂ M₂: E₁₂,E₂₁ have E = 1 → E_new = 0.',17)
text(1427,'Bars are trace schematics; the matrix examples are exact.',17)
text(1460,'Proofs: 54.1–54.5 · Popa, Appendix A.1.1 and A.2.1',17)
text(1493,'Printed pages 244–246, 249–251 · corrected support/capacity',16)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT)

"""Exact reproducible schematic for Figure83.1; standard library only."""
from pathlib import Path
from html import escape
W,H=1000,1320
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
f'<rect width="{W}" height="{H}" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182738}.title{font-size:25px;font-weight:700}.head{font-size:20px;font-weight:700}.text{font-size:18px}.small{font-size:16px}.blue{fill:#d9e9fa;stroke:#376fa3}.red{fill:#f7d8da;stroke:#a83f47}.green{fill:#d9eee3;stroke:#3e8260}.panel{fill:#fff;stroke:#aab8c9}</style>']
def text(x,y,s,cls='text'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def rect(x,y,w,h,cls):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>')
def panel(y,h,title):
 rect(24,y,952,h,'panel');text(44,y+34,title,'head')
text(28,38,'Normal on the smaller center → zero canonical cost','title')
text(28,69,'Actual N ⊂ M and core S ⊂ R; no normality of the whole represented algebra is assumed.','small')
panel(92,314,'A. The actual compatible state gives the full joint balance — 83.9–83.14')
rect(52,160,410,88,'blue');text(67,190,'φ = φ Eₐ, φ is M-central');text(67,223,'φ(ŝ) = τ(μs), μ in L¹(Z(S))₊')
rect(507,160,415,88,'green');text(522,190,'βμ = E꜀ᵣ(μ), Cᵣ = Z(R)');text(522,223,'kjoint βμ = ℓjoint μ')
text(44,291,'kjoint = Eᴅ₀(g)/d; ℓjoint = Eᴅ₀(E꜀(g))/d; C = N′ ∩ M.')
text(44,333,'Both marginals of kjoint are 1; its smaller ℓjoint marginal is also 1.')
text(44,375,'Smaller marginal → Tμ = μ → μ = βμ → μv = 0,  v = d(kjoint − ℓjoint).')
panel(428,430,'B. Conditional Jensen controls the full joint norm — 83.1–83.8')
rect(52,496,280,89,'blue');text(67,526,'f in L¹(U)₊');text(67,559,'β = Pf, P = Eᵥ')
text(351,543,'→','title')
rect(391,496,244,89,'blue');text(406,526,'Tf = Q(wβ)');text(406,559,'Q = Eᵤ')
text(654,543,'→','title')
rect(695,496,227,89,'green');text(710,526,'δ = ‖f − Tf‖₁');text(710,559,'Qw = Pw = 1')
text(44,630,'χL(t) = t² for t ≤ L; χL(t) = 2Lt − L² for t > L.')
text(44,674,'0 ≤ τ(χL(f)) − τ(χL(β)) ≤ τ(χL(f)) − τ(χL(Tf)) ≤ 2Lδ.')
text(44,718,'‖f − Pf‖₁ ≤ √(2Lδ) + rf(L) + 2rf(L/2);  rf(L) = τ(f 1{f > L}).')
text(44,761,'Uniform integrability: choose one L controlling all tails, then decrease δ.')
text(44,805,'Exact fixed point: δ = 0; let L → ∞. Thus f = Pf in the full joint algebra.')
panel(880,276,'C. What the additional hypotheses supply — 83.14–83.16')
rect(52,949,870,67,'green');text(67,977,'Central normality → φ(b̂) = 0 → positive-cost Følner projections inside A.');text(67,1006,'Faithful central restriction → v = 0 everywhere; joint normal density matching.','small')
text(44,1060,'Uniformly integrable normalized projection dimensions + basis stationarity → joint localization.')
text(44,1105,'General relative amenability has not yet supplied either additional hypothesis.')
text(28,1197,'Rectangles and arrow positions are schematic; they encode no dimensions or trace sizes.','small')
text(28,1241,'Proof locators: 83.3–83.7 (convexity/tails), 83.12–83.14 (actual state), 83.15–83.16 (cost).','small')
text(28,1285,'Human context: Popa 1994, Sections3.2 and4.2, printed205–206 and211–214. Full proofs retained.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(parts)+'\n').encode())

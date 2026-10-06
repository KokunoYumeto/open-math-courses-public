"""Reproducible operator and spectral schematic for Figure82.1; standard library."""
from pathlib import Path
from html import escape
W,H=1000,1480
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="1000" height="1480" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182738}.title{font-size:25px;font-weight:700}.head{font-size:20px;font-weight:700}.text{font-size:18px}.small{font-size:16px}.blue{fill:#d9e9fa;stroke:#376fa3}.red{fill:#f7d8da;stroke:#a83f47}.green{fill:#d9eee3;stroke:#3e8260}.panel{fill:#fff;stroke:#aab8c9}</style>']
def text(x,y,s,cls='text'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def rect(x,y,w,h,cls):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>')
def panel(y,h,title):
 rect(24,y,952,h,'panel');text(44,y+34,title,'head')
text(28,38,'Actual densities → one positive cost → projections in A','title')
text(28,69,'Finite-index II₁ inclusion N ⊂ M, actual core S ⊂ R, canonical expected pair A ⊂ B.','small')
panel(92,260,'A. Restrict the finite cup density to the actual commutants — 82.1–82.5')
rect(52,161,240,77,'blue');text(66,189,'kꜰ in Z(F), F = K₁′ ∩ K');text(66,218,'finite dimensional')
text(309,208,'→','title')
rect(353,161,265,77,'green');text(367,189,'k₀ = E꜀₀(kꜰ)');text(367,218,'C₀ = S′ ∩ R')
text(636,208,'→','title')
rect(682,161,240,77,'green');text(696,189,'k = E꜀(k₀)');text(696,218,'C = N′ ∩ M')
text(44,285,'C ⊂ C₀; D₀ = Z(S) ∨ Z(R) ⊂ Z(C₀). C₀ can be diffuse.')
text(44,325,'Modified core expectation F₀ uses k₀; ambient restriction uses k. Equality ⇔ k₀ = k.')
panel(374,270,'B. The remaining weighted branch gap is a fixed positive cost — 82.11–82.13')
rect(52,444,450,78,'blue');text(67,473,'v = d Eᴅ₀(k₀ − k)');text(67,502,'b = E꜀ₛ(|v|), Cₛ = Z(S)')
rect(538,444,384,78,'green');text(553,473,'b̂ in Z(A); e b̂ e = b e');text(553,502,'canonical lift, not left multiplication','small')
text(44,566,'Σⱼ ‖(aⱼ − a′ⱼ) ζ‖₁ = τ(ζ b) = Tr(p b̂),   ζ = Cₐ(p).')
text(44,605,'The exact normal density identity is b = 0; a selected state can instead annihilate b̂.')
panel(666,384,'C. Spectral extraction preserves the smaller algebra — Theorem 82.7')
rect(52,735,396,77,'blue');text(67,764,'positive h in L¹(A), Tr(h) = 1');text(67,793,'small L¹ commutators + Tr(h b̂)')
text(466,782,'→','title')
rect(518,735,404,77,'green');text(533,764,'pₜ = 1{h > t} in A');text(533,793,'0 < Tr(pₜ) < ∞ at a selected t')
text(44,858,'∫ Tr(pₜ) dt = 1;   ∫ Tr(pₜ b̂) dt = Tr(h b̂).')
text(44,900,'∫ ‖[pₜ,u]‖₂² dt ≤ 2 √‖h − uhu*‖₁,   u in the prescribed ambient M-tests.')
text(44,942,'Average the nonnegative squared commutator errors and positive cost together.')
text(44,986,'One threshold has their normalized sum below the integrated error budget.')
text(44,1023,'No claim of arbitrary signed test values, cyclic integer rounding or a common-support basis.','small')
panel(1072,262,'D. Exact state alternative and remaining source obligation — Corollary 82.8')
rect(52,1142,870,69,'green');text(67,1170,'M-central state φ = φ Eₐ,  φ(b̂) = 0');text(67,1199,'⇔ projections p in A with all finite Følner errors and normalized b̂-cost → 0')
text(44,1257,'Compatible hypertrace Φ supplies such a state if Φ(b̂) = 0.')
text(44,1300,'General relative amenability ⇒ this annihilation has not yet been proved here.')
text(28,1372,'Rectangles are schematic; widths encode neither module dimensions nor traces.','small')
text(28,1410,'Proof locators: 82.4–82.10 (densities), 82.12 (cost), 82.15–82.19 (spectral criterion).','small')
text(28,1448,'Human context: Popa 2023, printed p.189; Popa 1994, Theorem4.2.2. Full proofs retained.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(parts)+'\n').encode())

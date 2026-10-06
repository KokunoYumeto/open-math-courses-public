"""Exact domains, fixed endpoints and finite recovery of the initial commutant."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="800" viewBox="0 0 740 800"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs><rect width="740" height="800" fill="white"/>']
def text(x,y,s,size=17,bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb'):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')
def arrow(x,y,u,v):
 out.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#365c78" stroke-width="2" marker-end="url(#a)"/>')
text(26,40,'Recovering the initial bicommutant at a finite stage',23,True)
text(26,73,'Bⱼ = Mⱼ′ ∩ T;  Cⱼ = Bⱼ′ ∩ T. Fixed-endpoint proofs: 62.3–62.6.',17)
rect(18,96,704,202)
text(36,130,'A normal trace-preserving anti-isomorphism γ, with j ≥ 1:',17,True)
rect(40,151,230,47,'white');text(65,181,'M₋ⱼ₊₁',21)
rect(481,151,218,47,'white');text(540,181,'Bⱼ₋₁',21)
arrow(280,174,470,174);text(366,165,'γ',21)
rect(40,218,230,47,'white');text(65,249,'M₋ⱼ',21)
rect(481,218,218,47,'white');text(540,249,'Bⱼ',21)
arrow(280,242,470,242);text(366,232,'γ',21)
text(36,286,'γ(gⱼ) = eⱼ;  E_(M₋ⱼ′ ∩ M₋ⱼ₊₁)(gⱼ) = λ1.',17)
rect(18,318,704,171,'#eef8f4')
text(36,355,'E_Cⱼ(eⱼ) lies in Cⱼ ∩ Bⱼ₋₁, because Mⱼ₋₁ ⊂ Cⱼ.',18)
text(36,394,'Transport the relative expectation through γ: E_Cⱼ(eⱼ) = λ1.',17)
text(36,432,'Collapse stages starting at M₁:  E_C₁(Mⱼ₊₁) ⊂ E_C₁(Mⱼ).',17)
text(36,470,'Normality closes the union and gives C₁ = M₁.',18,True)
rect(18,509,704,172,'#fff7ea')
text(36,545,'M ⊂ C₀ ⊂ C₁ = M₁.',20,True)
text(36,583,'Each y ∈ C₀ commutes with J Dₖ J at every finite level.',17)
text(36,621,'The generating union Dₖ is dense in M, so y commutes with JMJ.',17)
text(36,659,'Only M₁ acts here on L²(M):  y ∈ (JMJ)′ = M. Thus C₀ = M.',17)
text(26,722,'Generation also gives tower injection via 61.7–61.8.',18)
text(26,755,'With C₀ = M, compression in 61.6 gives E_N F = F E. Proof: 62.5.',17)
text(26,787,'Human source: Popa, DOI 10.1007/BF02392646, §4.5.1, pp. 223–224.',15)
out.append('</svg>')
(R/'scalar-commutant-collapse.svg').write_text('\n'.join(out),encoding='utf-8')

"""Exact local-index budgets and scalar-relative-expectation projection."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="680" viewBox="0 0 740 680"><rect width="740" height="680" fill="white"/>']
def text(x,y,s,size=17,bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb'):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')
text(26,40,'A scalar relative expectation has a precise budget',24,True)
text(26,72,'N ⊂ M; A = N′ ∩ M; d = [M:N]; λ = 1/d. Proof: 62.1.',17)
rect(18,94,704,186)
text(36,128,'Minimal fᵢ ∈ A:  tᵢ = τ(fᵢ),  δᵢ = [fᵢMfᵢ:Nfᵢ].',18)
text(36,167,'rᵢ = δᵢ/(d tᵢ),  Σrᵢ = 1; choose sᵢ ∈ N with τ(sᵢ) = rᵢ.',18)
text(36,207,'qᵢ ≤ fᵢsᵢ,  τ(qᵢ) = λ;  vᵢⱼ are their matrix units.',18)
text(36,250,'z = Σ√(tᵢtⱼ) vᵢⱼ is rank one in this finite matrix corner.',18)
rect(18,300,704,176,'#eef8f4')
text(36,334,'An actual nonextremal example: t₁ = 1/4, t₂ = 3/4; δ₁ = δ₂ = 1.',17,True)
text(45,373,'i',18,True);text(140,373,'tᵢ',18,True);text(260,373,'rᵢ',18,True);text(390,373,'tᵢ²/δᵢ',18,True);text(540,373,'τ(qᵢ)',18,True)
for y,vals in [(412,['1','1/4','3/4','1/16','3/16']),(450,['2','3/4','1/4','9/16','3/16'])]:
 for x,s in zip([45,140,260,390,540],vals):text(x,y,s,19)
rect(18,496,704,107,'#fff7ea')
text(36,534,'E_A(z) = (3/16)1;   E_N(z) = (1/16)s₁ + (9/16)s₂.',20,True)
text(36,576,'τ(z) = 3/16. The two expectation targets have different coefficients.',17)
text(26,638,'The general construction and all off-diagonal identities are proved in 62.1.',16)
text(26,668,'Human source: Pimsner–Popa, DOI 10.24033/asens.1504, pp. 83–84.',15)
out.append('</svg>')
(R/'scalar-flat-projections.svg').write_text('\n'.join(out),encoding='utf-8')

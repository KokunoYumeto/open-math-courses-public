"""Reproducible proof figure for factor local quantization, Lemmas55.2/55.4 andTheorem55.7."""
from pathlib import Path
from html import escape
out=Path(__file__).with_suffix('.svg')
p=['<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1510" viewBox="0 0 640 1510" role="img" aria-labelledby="title desc">',
 '<title id="title">Finite matrix construction for factor local quantization</title>',
 '<desc id="desc">A MASA partition is converted into equal-trace cells, with a precisely bounded small remainder. A matrix algebra with this diagonal has nearly scalar commutant expectations. Fourier conjugation by independent fourth-root diagonal phases has exact off-diagonal variance divided by the square of its matrix dimension. One finite phase choice treats all targets. A further pinching refinement and summed-error selection produce one local corner.</desc>',
 '<rect width="640" height="1510" fill="#f9fcfe"/>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>']
def text(y,s,size=19,color='#163c50',bold=False,x=320):
 p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" text-anchor="middle" fill="{color}" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def box(y,h,fill='#eaf3f8'):p.append(f'<rect x="24" y="{y}" width="592" height="{h}" rx="8" fill="{fill}" stroke="#6b96ad"/>')
def arrow(y1,y2):p.append(f'<line x1="320" y1="{y1}" x2="320" y2="{y2}" stroke="#315b70" stroke-width="2" marker-end="url(#arrow)"/>')
text(39,'Finite matrices give one local corner',25,bold=True)
text(72,'A II₁ factor B inside a finite tracial algebra M',17)
box(95,400)
text(132,'1 · A diffuse MASA supplies equal-trace cells',22,bold=True)
text(171,'Old weights: 1/3, 1/5, 7/15;  choose d = 10.',19)
text(208,'Good cells: 3, 2, 4; remainder trace = 1/10.',19)
colors=['#719bb3']*3+['#8ab18e']*2+['#ad98be']*4
for j,color in enumerate(colors):
 p.append(f'<rect x="{50+54*j}" y="237" width="54" height="40" fill="{color}" stroke="#fff"/>')
# Last equal-trace cell comprises old leftovers 1/30 and 1/15.
p.append('<rect x="536" y="237" width="18" height="40" fill="#719bb3" stroke="#fff"/>')
p.append('<rect x="554" y="237" width="36" height="40" fill="#ad98be" stroke="#fff"/>')
text(309,'Each new cell has trace 1/10; the last combines old leftovers.',16)
text(343,'Reordered trace coordinates; refinement fails only on r.',17)
text(377,'Generally τ(r) < m/d for m old cells.',21,bold=True)
text(413,'Extend these d equal cells to F = M_d by comparison.',18)
text(449,'T = F′ ∩ B;  ‖E_T(b) − τ(b)1‖₂ < α',21,bold=True)
text(478,'Good-cell error < 2δ; remainder error ≤ ‖b‖ √(m/d).',16)
arrow(502,532)
box(544,420,'#e5f1e7')
text(582,'2 · Fourier bases with finite independent phases',22,bold=True)
text(618,'U = diag(ζ₀,…,ζ_d−1) F_d;  ζⱼ ∈ {1, i, −1, −i}',18)
text(653,'pᵢ = U eᵢᵢ U*;  Φ(b) = Σᵢ pᵢ b pᵢ',21)
text(691,'Write b = (bⱼₖ) over A₀ = e₀₀ B e₀₀.',19)
text(725,'τ₀ = d τ on A₀;  m_b = (1/d) Σⱼ bⱼⱼ',18)
text(766,'Mean squared noise = (1/d²) Σⱼ≠ₖ ‖bⱼₖ‖₂,τ₀²',20,bold=True)
text(802,'≤ ‖b‖₂² / d',22,bold=True)
text(841,'Squared scalar error = commutant error² + noise².',18)
text(879,'Sum over ALL targets before taking the finite phase mean.',17)
text(918,'One of the 4^d choices makes that summed energy small.',18)
text(946,'The coefficients bⱼₖ may be noncommuting operators.',16)
arrow(972,1002)
box(1014,365,'#fff3ea')
text(1052,'3 · Refine and select one common projection',22,bold=True)
text(1089,'C = B′ ∩ M;  D = B ∨ C;  y = E_D(y) + (y − E_D(y))',16)
text(1128,'Finite products bc approximate E_D(y).',20)
text(1165,'First partition: product-part error < 3ρ.',19)
text(1200,'Theorem 54.5 refinement: kernel-part error < ρ.',18)
text(1238,'ρ = ε/(4√K);  K = number of targets.',20,bold=True)
text(1276,'Σᵢ,ᵧ ‖qᵢ y qᵢ − E_C(y)qᵢ‖₂² < ε²',20,bold=True)
text(1314,'Choose ONE qᵢ with all-target error < ε² τ(qᵢ).',18)
text(1355,'Small trace: Theorem 55.7, final small-trace paragraph.',17)
text(1420,'Nonfactor B: Theorem 56.5, central local quantization.',16)
text(1453,'Proof: Lemmas 55.2, 55.4 and Theorem 55.7',16)
text(1485,'Human source: Popa, Appendix A.1.2, pp. 246–248',16)
p.append('</svg>');out.write_text('\n'.join(p)+'\n',encoding='utf-8');print(out)

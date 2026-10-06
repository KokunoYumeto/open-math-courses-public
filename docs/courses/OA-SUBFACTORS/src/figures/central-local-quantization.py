"""Original center-coordinate figure; all dimensions are exact conditional traces."""
from pathlib import Path
from html import escape
from fractions import Fraction

out = Path(__file__).with_suffix('.svg')
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="1580" viewBox="0 0 740 1580" role="img" aria-labelledby="title desc">',
    '<title id="title">Central counts assemble equal-dimensional global cells</title>',
    '<desc id="desc">Two central pieces have old cell dimensions two sevenths and five sevenths, and four fifths and one fifth. At matrix dimension five their count vectors are one and three plus one remainder, and four and one with no remainder. The five globally assembled cells each have center-valued dimension one fifth on both pieces. Central coefficients, finite Fourier variance and summed-error selection produce a common quantized corner.</desc>',
    '<rect width="740" height="1580" fill="#f8fbfd"/>']

def text(y, value, size=19, bold=False, x=370, color='#183f51'):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{escape(value)}</text>')

def rect(x,y,w,h,fill,stroke='#ffffff'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>')

def panel(y,h,fill):
    parts.append(f'<rect x="20" y="{y}" width="700" height="{h}" rx="10" fill="{fill}" stroke="#8facbc"/>')

red, blue = '#dfad91', '#95bdd5'
text(38, 'Central dimensions produce one common corner', 25, True)
text(71, 'B need not be a factor; the containing M is finite with trace τ.', 18)
panel(93,292,'#edf3f8')
text(130,'1 · The old count vector changes across the center',23,True)
text(163,'Example: B = W ⊕ W, with scalar trace weights 1/3 and 2/3.',18)
text(198,'Left central piece: T(q₁) = 2/7;  T(q₂) = 5/7',19)
rect(80,214,580*float(Fraction(2,7)),42,red)
rect(80+580*float(Fraction(2,7)),214,580*float(Fraction(5,7)),42,blue)
text(242,'q₁',19,x=80+580/7)
text(242,'q₂',19,x=float(80+580*Fraction(9,14)))
text(291,'Right central piece: T(q₁) = 4/5;  T(q₂) = 1/5',19)
rect(80,307,464,42,red)
rect(544,307,116,42,blue)
text(335,'q₁',19,x=312)
text(335,'q₂',19,x=602)
text(372,'Bars use normalized center-trace coordinates, not physical position.',16)

panel(408,410,'#e9f3ec')
text(447,'2 · Cut the center before choosing the five cells',23,True)
text(482,'d = 5;  n_l = floor(d T(q_l));  k = d − Σ_l n_l',20)
text(520,'Left: counts (1, 3); k = 1',19)
for j in range(5):
    if j<4:
        rect(80+116*j,538,116,48,red if j==0 else blue)
    else:
        rect(80+116*j,538,116*float(Fraction(3,7)),48,red)
        rect(80+116*j+116*float(Fraction(3,7)),538,116*float(Fraction(4,7)),48,blue)
    text(569,f'p{j}',18,x=138+116*j)
text(611,'Last cell combines 3/35 of q₁ and 4/35 of q₂.',18)
text(650,'Right: counts (4, 1); k = 0',19)
for j in range(5):
    rect(80+116*j,667,116,48,red if j<4 else blue)
    text(698,f'p{j}',18,x=138+116*j)
text(747,'Assemble cells by column: T(pⱼ) = (1/5, 1/5), τ(pⱼ) = 1/5.',19,True)
text(780,'For a′ = (2q₁ − q₂)(1 − r), the coefficient lists are',18)
text(807,'left (2, −1, −1, −1, 0); right (2, 2, 2, 2, −1).',18)

panel(841,315,'#eff0fa')
text(880,'3 · Average over a finite Fourier ensemble',23,True)
text(917,'Equivalent global cells extend to F = M_d(ℂ) ⊂ B.',19)
text(952,'H = F′ ∩ B contains Z(B);  E_H(a′) = T(a′).',20,True)
text(988,'‖E_H(b) − T(b)‖₂ < α for the chosen finite family.',19)
text(1023,'U = diag(ζ₀,…,ζ_d−1) F_d;  ζⱼ ∈ {1, i, −1, −i}',18)
text(1060,'Mean ‖Φ_P(b) − E_H(b)‖₂²',20,True)
text(1093,'= d⁻² Σⱼ≠ₖ ‖bⱼₖ‖₂,τ₀² ≤ ‖b‖₂² / d',20,True)
text(1129,'τ₀ = d τ on e₀₀Be₀₀; coefficients may be noncommuting.',17)

panel(1180,324,'#fff2e8')
text(1219,'4 · Sum every target’s error before choosing a cell',23,True)
text(1256,'C = B′ ∩ M;  E_C(bc) = T(b)c;  D = B ∨ C',19)
text(1291,'Control E_D(y) by central Fourier pinching.',19)
text(1326,'Remove y − E_D(y) by the common refinement of 54.5.',18)
text(1364,'Σᵢ Σ_y ‖qᵢyqᵢ − E_C(y)qᵢ‖₂² < ε² Σᵢ τ(qᵢ)',20,True)
text(1402,'One qᵢ satisfies every relative error bound.',20,True)
text(1438,'Split once more and use the same sum to arrange τ(q) ≤ t₀.',18)
text(1476,'The central trace T(b) is retained throughout.',19,True)
text(1533,'Exact example: (56.33)–(56.35). Construction: Lemmas 56.1–56.2.',17)
text(1562,'Variance: (56.21)–(56.22). Common corner: Theorem 56.5. Original · CC0.',17)
parts.append('</svg>')
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(out.name)

"""Exact two-dimensional diagrams for Lemma86.1 and Theorems86.2,86.4,86.6."""
from pathlib import Path
from html import escape
from fractions import Fraction as F

R = Path(__file__).resolve().parent
out = R / 'common-finite-capacity-and-uniform-rounding.svg'
W, H = 1000, 1320
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
         '<title id="title">A common finite-capacity region and uniform integer rounding</title>',
         '<desc id="desc">Finite central units transfer to finite larger-center units. The maximal finite region is common, and bounded truncations prove equality of capacities. The final bar uses theta five halves, trace weight two fifths and matrix size three; its exact removed trace is one fifth.</desc>',
         '<rect width="1000" height="1320" fill="#f5f8fc"/>']

def rect(x, y, w, h, fill='#ffffff', stroke='#adbed2', radius=6):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

def text(x, y, s, size=16, bold=False, color='#172b42'):
    weight = ' font-weight="700"' if bold else ''
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}"{weight}>{escape(s)}</text>')

text(28, 36, 'The common finite-capacity region', 26, True)
text(28, 68, 'Actual N ⊂ M; canonical A ⊂ B; physical centers U, V and W = U ∩ V.', 17)
rect(24, 91, 952, 315)
text(44, 125, 'A. Transfer finite units, then compare the maximal regions — 86.1–86.6', 20, True)
rect(44, 150, 270, 78, '#dbeafe', '#5683b3')
text(58, 181, 'ẑ ∈ Z(A),  Tr(ẑ) = t < ∞')
text(58, 208, 'I(ẑ) = Σ aᵢ ẑ aᵢ*,  a₁ = 1')
text(330, 191, '→', 32, True)
rect(372, 150, 275, 78, '#e3eefb', '#5683b3')
text(385, 181, 'r̂ = support I(ẑ) ∈ Z(B)')
text(385, 208, 'ẑ ≤ r̂ ≤ I(ẑ);  Tr(r̂) ≤ dt')
text(664, 191, '→', 32, True)
rect(706, 150, 248, 78, '#def3e7', '#4c9574')
text(718, 181, 'maximal fA ≤ maximal fB')
text(718, 208, 'The individual r need not be common.', 13)
text(44, 263, 'Reverse: y = E_A(r̂) is positive central, integrable; finite spectral cuts cover its support.')
text(44, 294, 'E_A(r̂(1 − f̂A)) = 0; faithfulness gives r̂ ≤ f̂A.')
text(44, 330, 'Thus f̂A = f̂B and fA = fB = f ∈ W.', 19, True)
text(44, 365, 'Every nonzero finite represented central unit has trace ≥ 1 (85.1).')
text(44, 391, 'Hats denote represented operators; physical labels are identified by the full Jones corner.', 14)

rect(24, 423, 952, 337)
text(44, 459, 'B. Infinite total trace is allowed — bounded truncations carry the proof', 20, True)
text(44, 497, 'K_B = E_V(K_A);  on f, K_A = E_U(κ K_B).  Therefore T(K_A f) = K_A f.')
text(44, 533, 'For a = K_A f and a_L = min(a, Lf):  T(a_L) ≤ a_L, and both bounded integrals agree.')
text(44, 569, 'Faithfulness gives T(a_L) = a_L; 83.3 gives a_L ∈ W. Let L increase.', 17, True)
rect(44, 592, 455, 96, '#def3e7', '#4c9574')
text(57, 623, 'K_A = K_B = K, affiliated with W')
text(57, 652, 'w_j = 1{K ≤ j} ∈ W; Tr(ŵ_j) ≤ j')
text(57, 678, 'K = ∞ on 1 − f; finite cuts w_j ↑ f.', 14)
rect(520, 592, 434, 96, '#fff1dc', '#c09b5c')
text(532, 622, 'Diagnostic: m_j = 2⁻ʲ, K(j) = 2ʲ')
text(532, 651, 'Each atom has unit trace 1; total trace = ∞.')
text(532, 678, 'A probability example; no actual core construction.', 13)
text(44, 723, 'On each nonzero w_j: a normal compatible trace state has density Kw_j / Tr(ŵ_j).')
text(44, 749, 'It gives fv = fb = 0 for the joint discrepancy and canonical positive cost (86.11–86.12).', 14)

rect(24, 777, 952, 398)
text(44, 813, 'C. Round a common finite block; control every ambient unitary — 86.13–86.14', 19, True)
text(44, 851, 'Choose a common atom z ≤ w_j. Example arithmetic: θ = 5/2, τ(z) = 2/5, n = 3.')
text(44, 888, 'New dimension = n²θ = 45/2; k = 22; removed dimension r_n = 1/2.')
text(44, 925, 'Unit p = ẑ commutes with every u ∈ M. Prescribe q ≤ p with dimension kz.')

theta, m, n = F(5,2), F(2,5), 3
newdim = n*n*theta
k = int(newdim)
remainder = newdim-k
scale_x, scale_y = 20, 80
bar_x, bar_y = 90, 970
rect(bar_x, bar_y, float(k*scale_x), float(m*scale_y), '#dbeafe', '#5683b3', 0)
rect(bar_x+float(k*scale_x), bar_y, float(remainder*scale_x), float(m*scale_y), '#f7d9dd', '#ca6573', 0)
text(90, 958, 'retained q: dimension 22')
text(567, 987, 'removed: dimension 1/2')
text(90, 1032, 'retained trace = 44/5', 16, True)
text(420, 1032, 'removed trace = 1/5', 16, True)
text(44, 1070, 'Widths: 20 pixels per dimension unit; height: 80 × τ(z) = 32 pixels.')
text(44, 1105, 'δ_u(q) ≤ 2√(r_n/k) = 1/√11 in this arithmetic; choose k > 4/ε² in general.', 17, True)
text(44, 1141, 'One integer and one projection work for every ambient unitary. No amenability input is used.', 15)
text(28, 1210, 'Scope: finite-capacity rounding is complete when f ≠ 0; the residual case has K_A = K_B = ∞.')
text(28, 1240, 'Nonzero support does not prove near-one common BF, exact full partition or unrestricted generation.', 15)
text(28, 1272, 'Proof locators: 86.1–86.14; exact providers 52, 68, 83 and 85. Bars encode dimension and trace.')
text(28, 1302, 'Human context: Popa 1994, Theorem 4.2.2, printed pp.213–214. Reproducible schematic; no 3D geometry.', 14)
parts.append('</svg>')
out.write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
assert F(k,1)*m == F(44,5) and remainder*m == F(1,5)
assert newdim*m == 9
print(out.name)

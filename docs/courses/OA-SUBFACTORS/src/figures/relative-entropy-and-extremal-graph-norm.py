"""Exact, reproducible two-dimensional proof diagram for Lesson77."""
from pathlib import Path
from html import escape

W, H = 1000, 1790
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10" fill="#45647e"/></marker></defs>',
         '<rect width="1000" height="1790" fill="#f4f7fb"/>']

def text(x, y, value, size=21, color='#18334b', weight='normal', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

def rect(x, y, w, h, fill='#ffffff', stroke='#bccddd', radius=14):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

def line(x1, y1, x2, y2, arrow=False, color='#45647e', width=2):
    marker = ' marker-end="url(#arrow)"' if arrow else ''
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{marker}/>')

def card(y, h, title):
    rect(30, y, 940, h)
    text(52, y+36, title, 24, weight='bold')

text(35, 42, 'Relative entropy reaches the extremal graph bound', 30, weight='bold')
text(35, 74, 'Actual trace • complete finite square • retained residual • no separability', 20)

card(100, 305, '1. The matrix sectors are the two coordinates of an isometry')
text(55, 177, 'Hⱼ = ⊕ᵢ (ℂ^(nᵢ) ⊗ ℂ^(gᵢⱼ))', 25)
line(410, 169, 545, 169, True)
text(565, 177, 'Hₐ ⊗ Hₑ,ⱼ', 25)
text(395, 205, 'Vⱼ : |i,a,b〉 ↦ |i,a〉 ⊗ |i,b〉', 22)
rect(60, 227, 400, 113, '#eaf2fb')
rect(535, 227, 395, 113, '#eaf7f2')
text(80, 259, 'Trace out the multiplicity coordinate', 20, weight='bold')
text(80, 289, 'σℓⱼ = ⊕ᵢ Tr_mult((yℓⱼ)ᵢᵢ)', 23)
text(80, 321, '(Eᴅ xℓzⱼ)ᵢ = σℓⱼ,ᵢ / sᵢ', 23)
text(555, 259, 'Trace out the matrix coordinate', 20, weight='bold')
text(555, 289, 'ωₑ,ⱼ = ⊕ᵢ (nᵢ/mⱼ) I_(gᵢⱼ)', 23)
text(555, 321, 'Σℓ(Sσℓⱼ − Syℓⱼ) ≤ pⱼ Sωₑ,ⱼ', 21)
text(55, 376, 'The two sector labels agree in VⱼHⱼ. Off-sector terms vanish under either partial trace.', 20)
text(790, 395, '77.1–77.2; (77.8)–(77.12)', 16, anchor='middle')

card(425, 275, '2. The actual trace gives a joint probability on the edges')
text(55, 503, 'Example L = 2', 22, weight='bold')
text(55, 537, 'D = Mat₂ ⊕ ℂ', 23)
text(55, 569, 'Q = Mat₃ ⊕ ℂ', 23)
text(55, 606, 'G = [1  0; 1  1]', 24)
text(380, 503, 'q = (1/2, 1/2)', 23)
text(690, 503, 'p = (3/4, 1/4)', 23)
text(380, 549, 'r = [1/2  0; 1/4  1/4]', 25)
text(380, 587, 'rᵢⱼ = nᵢgᵢⱼtⱼ;  row sums q, column sums p', 20)
text(55, 650, 'H(Q|D) ≤ Σ rᵢⱼ log(mⱼsᵢ/nᵢtⱼ) ≤ 2 log Σ gᵢⱼ√(qᵢpⱼ) ≤ log ‖G‖²', 21)
text(55, 682, 'Scalar log concavity, then pairing two unit vectors through G.  (77.5), (77.6), (77.13)', 19)

card(720, 310, '3. Keep every finite block, including the residual')
rect(55, 782, 535, 92, '#eaf2fb')
rect(620, 782, 325, 92, '#fff4df')
text(75, 815, 'Selected whole-stage pieces', 21, weight='bold')
text(75, 849, 'rBₘr ⊂ rAₘr : corner matrix norm ≤ β', 23)
text(640, 815, 'Exact residual corner', 21, weight='bold')
text(640, 849, 'fB₀ ⊂ fA₀ : same G₀', 23)
line(270, 883, 430, 925, True)
line(780, 883, 565, 925, True)
text(55, 916, 'β = ‖Γ‖', 24, weight='bold')
text(365, 961, 'Q ⊂ P ⊂ M,  EₙEₚ = Eᵩ', 26)
text(55, 997, 'For each positive partition x:  Eₚx → x in L², so H(M|N) ≤ log β².', 23)
text(735, 1019, '77.3, 77.5, 77.6; (77.30)', 17, anchor='middle')

card(1050, 350, '4. Extremality makes the factor entropy equal log d')
text(55, 1129, 'Eₙ(e) = Eₙ′∩ₘ(e) = c1,  c = 1/d', 26)
line(670, 1120, 925, 1120, True)
text(695, 1160, 'average by N-unitaries', 20)
text(55, 1204, 'y = (cn)⁻¹ Σ uᵢeuᵢ* → 1 in L²;   p = 1[0,1+a](y)', 24)
text(55, 1242, 'eᵢ′ = p ∧ uᵢeuᵢ*,   xᵢ = eᵢ′/[(1+a)cn],   x₀ = 1 − Σxᵢ ≥ 0', 23)
text(55, 1280, 'Removed trace ≤ ε²/a²; first ε → 0, then a → 0.  (77.20)–(77.25)', 22)
rect(55, 1308, 890, 58, '#eaf7f2')
text(500, 1347, 'log d = H(M|N) ≤ log ‖Γ‖² ≤ log d   ⇒   ‖Γ‖² = d', 27, weight='bold', anchor='middle')
text(55, 1383, 'Principal and dual norms agree by rooted closed-walk growth; finite weights need not agree.', 20)

card(1420, 275, '5. Scalar dimension mass alone cannot replace that entropy proof')
text(55, 1495, 'For every L ≥ 1, the same G has ‖G‖² = (3 + √5)/2 < 3.', 23)
text(55, 1533, 'Canonical density = (3,2);  total mass = 3 − 1/(L+2) → 3.', 23)
line(80, 1598, 915, 1598, False, '#5d758c', 3)
for x, label, color in [(120,'(3+√5)/2','#a34145'),(235,'8/3','#315b96'),(400,'11/4','#315b96'),(735,'35/12','#315b96'),(902,'3','#315b96')]:
    parts.append(f'<circle cx="{x}" cy="1598" r="5" fill="{color}"/>')
    text(x, 1575, label, 20, color, anchor='middle')
text(235, 1631, 'L=1', 19, anchor='middle')
text(400, 1631, 'L=2', 19, anchor='middle')
text(735, 1631, 'L=10', 19, anchor='middle')
text(902, 1631, 'limit', 19, anchor='middle')
text(55, 1672, 'Number-line positions are schematic; values are exact. Abstract finite pair, not a subfactor counterexample.', 18)

text(35, 1730, 'Proof locators: Lesson77.  Sources: Pimsner–Popa (1986, 1991); Popa (1994), 4.4.1(3).', 19)
text(35, 1762, 'Reproducible SVG • GPT-6.1 Sol (OpenAI) • Ultra • CC0 • October 2026', 18)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts) + '\n', encoding='utf-8')

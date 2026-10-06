"""Reproduce Figure 51.1: exact tail alignment and an index-four obstruction.

Arrows show algebra maps and proof stages, not numerical approximations.
The Bell example uses the actual adjacent-site tunnel of Proposition 51.6.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).with_suffix('.svg')
parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1080" viewBox="0 0 640 1080" role="img" aria-labelledby="title desc">',
    '<title id="title">Transported tails and their full core closure</title>',
    '<desc id="desc">A specified pair isomorphism transports Jones cups. Full tensor tails become first-leg commutants; coherent unitaries identify their closure. An index-four Bell tunnel shows why an arbitrary infinite common factor cannot always be removed.</desc>',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
    '<rect width="640" height="1080" fill="#f9fcfe"/>',
]
def text(x, y, s, size=19, color='#163c50', weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="middle" font-weight="{weight}">{escape(s)}</text>')
def line(x1, y1, x2, y2, arrow=False):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#315b70" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def box(y, title, detail):
    parts.append(f'<rect x="40" y="{y}" width="560" height="78" rx="9" fill="#eaf3f8" stroke="#6b96ad"/>')
    text(320, y+30, title, 23, weight='bold')
    text(320, y+59, detail, 18)

text(320, 35, 'A specified tensor map realizes a core', 26, weight='bold')
text(320, 66, 'σ : (S ⊗ P ⊂ R ⊗ P) → (S ⊂ R)', 23)
text(320, 94, 'P = Mₙ or ℛ · normal and trace preserving', 18)
box(116, 'fⱼ = σ(gⱼ ⊗ 1) ∈ Bⱼ', 'Bⱼ = σ(Aⱼ ⊗ P) = R ∩ Lⱼ⁰;  Aⱼ = R ∩ Lⱼ')
line(320, 195, 320, 222, True)
box(229, 'Lⱼ₊₂⁰ = Lⱼ₊₁⁰ ∩ {fⱼ}′', 'E(Lⱼ₊₁⁰)(fⱼ) = λ1;  λ = 1 / [M:N]')
text(320, 336, 'Recognized ambient Jones tunnel · 51.13–51.15', 18)
line(320, 348, 320, 375, True)
box(382, 'uⱼ ∈ Bⱼ₊₁;  wⱼ = uⱼ ··· u₀', 'wⱼ gᵢ wⱼ* = fᵢ for every 0 ≤ i ≤ j')
text(320, 488, 'Eⱼ = Aⱼ′ ∩ R  →  Fⱼ = Bⱼ′ ∩ R', 23)
text(320, 518, 'Fⱼ = σ(Eⱼ ⊗ 1): the commutant removes the leg', 18)
line(320, 530, 320, 556, True)
box(563, 'α(x) = wⱼ₋₂ x wⱼ₋₂* for x ∈ Eⱼ, j ≥ 2', 'Later uᵢ lie in Bⱼ and fix this value exactly')
text(320, 672, 'α(R) = (⋃ Fⱼ)″ = σ(R ⊗ 1) = R⁰', 22, weight='bold')
text(320, 704, 'α(Lⱼ′ ∩ M) = (Lⱼ⁰)′ ∩ M;  E_N(R⁰) = S⁰', 19)
text(320, 732, 'Both entire core closures · 51.18–51.21', 18)
line(35, 756, 605, 756)
text(320, 790, 'An arbitrary infinite leg can fail', 25, '#713d26', 'bold')
text(320, 822, 'M = ⊗ᵣ≥₁ M₂;  N = 1 ⊗ ⊗ᵣ≥₂ M₂', 21)
text(320, 854, 'gⱼ is the Bell projection on sites j+1 and j+2', 18)
for i in range(5):
    x = 85+i*112
    parts.append(f'<rect x="{x-28}" y="878" width="56" height="38" rx="5" fill="#f5e8dc" stroke="#a68165"/>')
    text(x, 904, str(i+1), 20)
line(85, 872, 197, 872)
text(141, 904, 'g₀', 16)
line(197, 926, 309, 926)
text(253, 946, 'g₁', 16)
text(320, 977, '[M:N] = 4;  E_N(g₀) = ¼1;  core = N ⊂ M', 20)
text(320, 1010, 'D = N gives D′ ∩ S = ℂ and D′ ∩ R = M₂', 20, '#713d26')
text(320, 1040, 'Tensor splitting holds; the finite pair cannot be a core.', 18, '#713d26')
text(320, 1069, 'Theorem 51.4 · finite deletion 51.5 · obstruction 51.6', 16)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n', encoding='utf-8')
print(OUT)

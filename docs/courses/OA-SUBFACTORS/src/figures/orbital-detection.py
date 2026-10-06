"""Proof mechanism for Theorems 17.4–17.6; no numerical approximation. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="725" viewBox="0 0 500 725" role="img" aria-labelledby="title desc">',
         '<title id="title">Why every bounded vector is detected</title>',
         '<desc id="desc">Failure of the uniform orbital test gives a unit vector orthogonal to all conjugates of R in the ultrapower. Matrix approximation puts Q and its commutant join in their span. Corner pinching preserves orthogonality under multiplication by Q. A uniformly bounded finite basis spans the whole ultrapower, contradicting norm one.</desc>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#415b78"/></marker></defs>',
         '<rect width="500" height="725" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.main{font-size:18px}.detail{font-size:15px}</style>']

def label(x, y, value, cls='main'):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="{cls}">{escape(value)}</text>')

label(250, 33, 'A missed vector cannot exist', 'title')
boxes = [
    (60, 'Failure of the orbital test', 'x ∈ M^ω, ‖x‖₂ = 1; equation (17.11)'),
    (180, 'x is orthogonal to W', 'W = closed span of uR^ωu*; equation (17.4)'),
    (300, 'The commuting join lies in W', 'Q ∨ (Q′ ∩ M^ω) ⊆ W; Lemma 17.2'),
    (420, 'Corner pinching preserves orthogonality', 'a x b ∈ W⊥ for a, b ∈ Q; Lemma 17.3'),
    (540, 'The finite basis spans every bounded vector', 'M^ω = Σⱼ uⱼ R^ω, uⱼ ∈ Q; equation (17.13)'),
]
for i, (y, main, detail) in enumerate(boxes):
    parts.append(f'<rect x="20" y="{y}" width="460" height="82" rx="9" fill="#edf3fa" stroke="#6686aa"/>')
    label(250, y + 30, main, 'main' if i != 4 else 'detail')
    label(250, y + 60, detail, 'detail')
    if i < len(boxes) - 1:
        parts.append(f'<line x1="250" y1="{y + 84}" x2="250" y2="{y + 112}" stroke="#415b78" stroke-width="2" marker-end="url(#arrow)"/>')
parts.append('<line x1="250" y1="624" x2="250" y2="652" stroke="#415b78" stroke-width="2" marker-end="url(#arrow)"/>')
label(250, 679, 'Then x ⟂ M^ω, contradicting ‖x‖₂ = 1.', 'main')
label(250, 710, 'Q is the ultraproduct of the late factors.', 'detail')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts) + '\n', encoding='utf-8')

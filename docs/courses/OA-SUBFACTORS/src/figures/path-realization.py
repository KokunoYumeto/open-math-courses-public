"""Exact implications identifying the path-tail invariant, Theorem 25.3. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="650" viewBox="0 0 540 650" role="img" aria-labelledby="title desc">',
         '<title id="title">From a generating tail to the full path graph</title>',
         '<desc id="desc">For the discrete A_(r-1) model with r at least four, original generators q_i have sufficiently late commuting tails. Their tunnel is generating. Finite-depth trace-preserving reflection maps q_i to upward Jones projections e_i for i at least one and identifies the entire relative-commutant limit with their closure. Finite tower expectations take the Jones algebra C_m into C_k, so L2 contraction forces B_k equal C_k equal P_k. Self-duality then gives the principal as well as dual graph A_(r-1).</desc>',
         '<rect width="540" height="650" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}.box{fill:#edf3fb;stroke:#7c9bbd;stroke-width:1.5}</style>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#426987"/></marker></defs>']

def text(x, y, value, cls='label', anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y, title, first, second):
    parts.append(f'<rect x="24" y="{y}" width="492" height="105" rx="8" class="box"/>')
    text(270, y+29, title, 'heading', 'middle')
    text(270, y+58, first, 'label', 'middle')
    text(270, y+86, second, 'small', 'middle')

def arrow(y1, y2):
    parts.append(f'<line x1="270" y1="{y1}" x2="270" y2="{y2}" stroke="#426987" stroke-width="2" marker-end="url(#arrow)"/>')

text(24, 34, 'Realize the full path invariant', 'title')
text(24, 63, 'δ = 2 cos(π/r),   r ≥ 4;   index δ² < 4', 'label')
box(86, 'The tail tunnel generates M', 'qᵢ commutes with M₋ₐ for a ≥ i + 1.', 'Proposition 25.2; each qᵢ lies in a finite commutant.')
arrow(198, 227)
box(237, 'Reflection preserves the tower trace', 'qᵢ ↦ eᵢ,  i ≥ 1;   B∞ = {e₁, e₂, …}″', 'Finite depth and (25.7–8); e₀ is a separate projection.')
arrow(349, 378)
box(388, 'Finite expectations force equality', 'E_Bₖ(Cₘ) ⊂ Cₖ;   Bₖ = Cₖ = Pₖ', 'Lemma 25.1: density plus L² contraction (25.4).')
arrow(500, 529)
text(270, 556, 'Both rooted graphs are Aᵣ₋₁, by self-duality.', 'label', 'middle')
text(270, 588, 'Both invariant rows: Aₖ = Pₖ₊₁,  Bₖ = Pₖ.', 'label', 'middle')
text(24, 627, 'Theorem 25.3 and Corollary 25.4: existence and uniqueness.', 'small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n', encoding='utf-8')

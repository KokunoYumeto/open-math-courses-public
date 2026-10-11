"""Reproduce the diagram for the complete finite-trace corner construction.

New diagram and code: CC0. Mathematical labels refer to TC3–TC7 of
hypertraces-finite-injectivity.md#semifinite-trace-corner-bootstrap.
"""
from pathlib import Path
from html import escape


def make_svg():
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 1020" role="img" aria-labelledby="title desc">
<title id="title">Finite-trace corners yield models of the whole algebra</title>
<desc id="desc">In an injective algebra N with a faithful normal semifinite trace, finite-trace projections e F increase strongly to one. Normal completely positive contraction maps compress N to the corner and map it to a matrix algebra. Completely positive contractions return it to the corner and include it into N. The normal functional error is bounded by the compression error plus the corner model error, each less than epsilon over two.</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 1 L8 5 L0 9" fill="none" stroke="#146665" stroke-width="1.8"/></marker></defs>
<rect width="400" height="1020" fill="#fafaf7"/>
<g font-family="Arial,sans-serif" fill="#202730" text-anchor="middle">
<text x="200" y="34" font-size="23" font-weight="bold">Finite trace → finite models</text>
<text x="200" y="65" font-size="18">N injective; τ faithful, normal, semifinite</text>
<text x="200" y="94" font-size="19">0 &lt; τ(e<tspan baseline-shift="sub" font-size="13">F</tspan>) &lt; ∞; e<tspan baseline-shift="sub" font-size="13">F</tspan> ↑ 1 strongly</text>''']
    boxes = [(130, 'N', 'the whole algebra'), (285, 'eꜰ N eꜰ', 'τꜰ = τ / τ(eꜰ)'), (440, 'Mₙ(ℂ)', 'a finite matrix algebra'), (595, 'eꜰ N eꜰ', 'the same corner'), (750, 'N', 'the whole algebra')]
    for y, title, subtitle in boxes:
        parts.append(f'<rect x="42" y="{y}" width="316" height="80" rx="10" fill="#e9f2f1" stroke="#146665" stroke-width="1.5"/>')
        parts.append(f'<text x="200" y="{y+32}" font-size="25">{escape(title)}</text><text x="200" y="{y+60}" font-size="18">{escape(subtitle)}</text>')
    arrows = [(210,285,'x ↦ eꜰ x eꜰ','normal cpc'),(365,440,'S','normal cpc'),(520,595,'R','cpc'),(675,750,'ιꜰ : corner inclusion','cpc')]
    for y,z,title,subtitle in arrows:
        parts.append(f'<path d="M78 {y+6} V{z-9}" stroke="#146665" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
        parts.append(f'<text x="229" y="{y+28}" font-size="20">{escape(title)}</text><text x="229" y="{y+53}" font-size="17">{escape(subtitle)}</text>')
    parts.append('''<text x="200" y="863" font-size="20" font-weight="bold">For every tested x and normal f</text>
<text x="200" y="896" font-size="19">|f(ιꜰ RS(eꜰ x eꜰ) − x)|</text>
<text x="200" y="927" font-size="18">≤ corner model error + compression error</text>
<text x="200" y="956" font-size="21">&lt; ε/2 + ε/2 = ε</text>
<text x="200" y="992" font-size="16">TC3–TC7 · finite-trace corner construction</text>
</g></svg>''')
    return '\n'.join(parts)+'\n'


if __name__ == '__main__':
    Path(__file__).with_name('semifinite-trace-corner-bootstrap.svg').write_text(make_svg(),encoding='utf-8',newline='\n')

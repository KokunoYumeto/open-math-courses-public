"""Exact implication diagram for the affine orbit-envelope comparison."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
rows = [
    (36, 'Parity deviation', ['n ∈ I_M, 0 ≤ k ≤ M', '|d_k| ≤ h']),
    (168, 'Exact affine coordinates', ['Tᵏ(n)/(ρᵏn) = 3ᵈᵏ(1 + Q_k/n)', '0 ≤ Q_k/n ≤ 1/6']),
    (300, 'Both sides of the envelope', ['3⁻ʰ ≤ Tᵏ(n)/(ρᵏn) ≤ (7/6)3ʰ', 'β = log₂(7/6),  h = (ηM − β)/λ']),
    (432, 'A retained integer trajectory', ['n⁻η ≤ Tᵏ(n)/(ρᵏn) ≤ nη', 'ηM ≥ β; every prefix is included']),
]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="450" height="570" viewBox="0 0 450 570" role="img" aria-labelledby="title desc">',
 '<title id="title">The fixed affine allowance</title>',
 '<desc id="desc">Equation 20: exact affine coordinates transfer a maximal parity barrier to both sides of the integer orbit envelope.</desc>',
 '<rect width="450" height="570" fill="#fff"/>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#426273"/></marker></defs>']
for y,title,lines in rows:
    parts.append(f'<rect x="14" y="{y}" width="422" height="106" rx="10" fill="#eef5f8" stroke="#426273"/>')
    parts.append(f'<text x="225" y="{y+26}" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="bold">{escape(title)}</text>')
    for j,line in enumerate(lines):
        # Explicit exponent markup prevents plain adjacent letters from hiding powers.
        text=escape(line).replace('3ᵈᵏ','3<tspan baseline-shift="super" font-size="12">dₖ</tspan>').replace('n⁻η','n<tspan baseline-shift="super" font-size="12">−η</tspan>').replace('nη','n<tspan baseline-shift="super" font-size="12">η</tspan>')
        for symbol,index in [('I','M'),('d','k'),('Q','k')]:
            text=text.replace(symbol+'_'+index,symbol+'<tspan baseline-shift="sub" font-size="12">'+index+'</tspan>')
        parts.append(f'<text x="225" y="{y+55+26*j}" text-anchor="middle" font-family="Georgia,serif" font-size="17">{text}</text>')
    if y<432:
        parts.append(f'<path d="M225,{y+108} L225,{y+129}" stroke="#426273" stroke-width="2" marker-end="url(#arrow)"/>')
parts.append('</svg>')
(ROOT/'figures/affine-envelope.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

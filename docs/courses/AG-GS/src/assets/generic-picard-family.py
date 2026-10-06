"""Reproduce Figure G.1's exact map schematic. Independently written, CC0."""
from pathlib import Path

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="535" viewBox="0 0 380 535" role="img" aria-labelledby="title description">
<title id="title">Rational Albanese and positive-power Picard family</title>
<desc id="description">The detecting curve maps to its Jacobian and to the smooth locus. Both map compatibly to the rational Albanese. Restriction of a parameter family maps S to J zero. The reverse isogeny maps J zero to P, producing t, with v composed with iota equal to multiplication by n.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#245378"/></marker></defs>
<rect width="380" height="535" rx="12" fill="#f8fafc"/>
<g font-family="Arial, sans-serif" fill="#182c40" font-size="17" text-anchor="middle">
<text x="190" y="29" font-size="18" font-weight="bold">Curve detection</text>
<text x="53" y="78" font-size="24">C</text><text x="311" y="78" font-size="24">J_C</text>
<text x="53" y="184" font-size="24">U</text><text x="311" y="184" font-size="24">A</text>
<text x="185" y="62">j_C</text><text x="93" y="132">inclusion</text>
<text x="340" y="132">q₀</text><text x="185" y="168">α</text>
<text x="190" y="223" font-size="15">C: smooth projective detecting curve</text>
<text x="190" y="246" font-size="15">U: smooth locus of normal projective Y</text>
<text x="190" y="269" font-size="15">A: rational Albanese; q₀ surjective</text>
<text x="190" y="307" font-size="18" font-weight="bold">Whole-family comparison</text>
<text x="53" y="352" font-size="24">S</text><text x="311" y="352" font-size="24">J₀</text>
<text x="53" y="452" font-size="24">P</text>
<text x="185" y="333">r: restriction to C</text><text x="92" y="402">t</text>
<text x="169" y="385">v</text><text x="314" y="460">ι</text>
<text x="190" y="492" font-size="15">P = Aᵗ; J₀ = image of ι</text>
<text x="190" y="516" font-size="15">t = v ∘ r; v ∘ ι = [n]_P, n = deg(ι) &gt; 0</text>
</g>
<g fill="none" stroke="#245378" stroke-width="2.3" marker-end="url(#arrow)">
<path d="M 73 71 H 276"/><path d="M 53 90 V 157"/><path d="M 311 90 V 157"/><path d="M 73 177 H 287"/>
<path d="M 73 345 H 286"/><path d="M 53 364 V 425"/>
<path d="M 292 361 L 78 430"/>
<path d="M 73 445 H 261 Q 352 445 352 375 Q 352 358 333 354"/>
</g>
</svg>
'''

if __name__ == '__main__':
    Path(__file__).with_suffix('.svg').write_text(SVG, encoding='utf-8')

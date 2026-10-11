"""Original map diagram for timeout coding; reproducible vector source."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="650" viewBox="0 0 440 650" role="img" aria-labelledby="title desc">
<title id="title">Two maps in the timeout count</title>
<desc id="desc">A bounded-fibre first-passage map retains time and landing. A separate parity bijection codes the landing shell. Timeout words lie inside a survival event by the affine comparison.</desc>
<defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#273b50"/></marker></defs>
<rect width="440" height="650" fill="#fff"/>
<g font-family="Georgia,serif" fill="#172d40" text-anchor="middle">
<text x="220" y="29" font-size="21">Count the original integers</text>
<rect x="22" y="49" width="396" height="68" rx="9" fill="#eaf3f9" stroke="#315573"/>
<text x="220" y="78" font-size="19">Sources n in I<tspan baseline-shift="sub" font-size="13">M</tspan></text>
<text x="220" y="101" font-size="16">Retained chain, then first low timeout</text>
<path d="M407 119V178" stroke="#273b50" stroke-width="2" marker-end="url(#a)"/>
<text x="220" y="144" font-size="15" fill="#9a3e12">First passage: bounded fibres</text>
<text x="220" y="166" font-size="15" fill="#9a3e12">Keep the threshold p and the time H</text>
<rect x="22" y="190" width="396" height="78" rx="9" fill="#fff2e5" stroke="#9a3e12"/>
<text x="220" y="221" font-size="19">Tags (p, H, y)</text>
<text x="220" y="248" font-size="16">H in one short interval; y in C<tspan baseline-shift="sub" font-size="12">L,p</tspan></text>
<path d="M407 270V334" stroke="#273b50" stroke-width="2" marker-end="url(#a)"/>
<text x="220" y="296" font-size="15">Fix p and count its landing set</text>
<text x="220" y="319" font-size="15">m = p − 1, y in I<tspan baseline-shift="sub" font-size="12">m</tspan></text>
<rect x="22" y="346" width="396" height="80" rx="9" fill="#e9f5ed" stroke="#286646"/>
<text x="220" y="375" font-size="19">Landing y ↔ its m parity bits</text>
<text x="220" y="400" font-size="16">Exact bijection on the whole shell</text>
<text x="220" y="419" font-size="14">Inverse: y = 2ᵐ + the word's residue</text>
<path d="M407 429V501" stroke="#273b50" stroke-width="2" marker-end="url(#a)"/>
<text x="220" y="456" font-size="15">Timeout words form a subset</text>
<text x="220" y="480" font-size="15">Use Tʲ(y) ≤ (7/6)y exp(Z<tspan baseline-shift="sub" font-size="12">j</tspan>)</text>
<rect x="22" y="513" width="396" height="72" rx="9" fill="#eaf3f9" stroke="#315573"/>
<text x="220" y="542" font-size="19">Every prefix has Z<tspan baseline-shift="sub" font-size="13">j</tspan> &gt; −B</text>
<text x="220" y="568" font-size="16">Fair mass ≤ C<tspan baseline-shift="sub" font-size="12">B</tspan> m<tspan baseline-shift="super" font-size="12">−3/2</tspan> 2<tspan baseline-shift="super" font-size="12">−κm</tspan></text>
<text x="220" y="614" font-size="15">Theorems 2 and 5 give the count.</text>
<text x="220" y="636" font-size="15">No fresh random law at a landing.</text>
</g></svg>'''
(ROOT/'figures/timeout-word-map.svg').write_text(svg,encoding='utf-8')
print('Wrote figures/timeout-word-map.svg')


"""Exact candidate interval and CRT class for lesson29, Exercise1."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="370" viewBox="0 0 920 370" role="img" aria-labelledby="title desc">
<title id="title">A word, an interval and a congruence</title>
<desc id="desc">For B equals twenty and the word two two, the enclosing interval is fourteen to thirty-five. The word class is one modulo thirty-two. Imposing residue zero modulo three selects thirty-three modulo ninety-six. Only thirty-three remains in the interval. Its first passage is thirty-three to twenty-five to nineteen.</desc>
<rect width="920" height="370" fill="#fff"/>
<g font-family="Georgia,serif" fill="#182b3a">
<text x="35" y="36" font-size="24">Exact arithmetic candidates for the word (2, 2)</text>
<text x="35" y="67" font-size="18">B = 20     h = 2     q = 1     x = 0     Q = 96</text>
<rect x="137.5" y="99" width="157.5" height="150" fill="#e4f2ed" stroke="#2d705c"/>
<text x="157" y="120" font-size="17">14 ≤ M ≤ 35</text>
<line x1="40" x2="880" y1="167" y2="167" stroke="#637585" stroke-width="2"/>
<g fill="#777"><circle cx="40" cy="167" r="5"/><circle cx="520" cy="167" r="5"/><circle cx="760" cy="167" r="5"/></g>
<circle cx="280" cy="167" r="8" fill="#1b6b54"/>
<g font-size="18" text-anchor="middle"><text x="40" y="198">1</text><text x="280" y="198">33</text><text x="520" y="198">65</text><text x="760" y="198">97</text></g>
<text x="385" y="133" font-size="18">Word class: M ≡ 1 (mod 32)</text>
<text x="385" y="231" font-size="18">Combined class: M ≡ 33 (mod 96)</text>
<path d="M280 250 V272 H400" stroke="#1b6b54" stroke-width="2" fill="none"/>
<text x="410" y="279" font-size="23">33 → 25 → 19</text>
<text x="410" y="309" font-size="17">Above 20 before time 2; at most 20 at time 2</text>
<text x="35" y="349" font-size="17">One retained integer. Its residue coefficient is 3 / 33 = 1 / 11. Lemmas 1–3.</text>
</g></svg>'''
(ROOT/'figures/endpoint-fibres.svg').write_text(svg,encoding='utf-8')

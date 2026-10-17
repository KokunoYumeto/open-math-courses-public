"""Reproduce the exact scalar encoding and output-support diagram."""
from pathlib import Path
import xml.etree.ElementTree as ET
p=Path(__file__).with_name('global-output-reserve-assembly.svg')
p.write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650" role="img" aria-labelledby="title desc">
<title id="title">One scalar norm from a genuine boundary output reserve</title><desc id="desc">Overlapping source charts are encoded by a larger atlas frame and flat isometries into separated boxes of an unused boundary patch. The full elliptic output avoids that patch, so the two scalar outputs are orthogonal. Full normal ratios and all input variables are retained.</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#315d6a" stroke-width="1.4"/></marker></defs>
<rect width="1100" height="650" rx="12" fill="#f3f7f8"/>
<g font-family="Arial,sans-serif" fill="#152d3a"><text x="35" y="42" font-size="25">An unused boundary patch gives one scalar test</text>
<text x="35" y="76" font-size="18">Reserve hypothesis: ∂X ∖ π(K) is nonempty; boundary dimension d ≥ 1.</text>
<rect x="50" y="115" width="220" height="78" rx="8" fill="white" stroke="#7da2af"/><text x="160" y="149" text-anchor="middle" font-size="22">full residual output S f</text><text x="160" y="177" text-anchor="middle" font-size="16">all source charts/components</text>
<rect x="370" y="115" width="220" height="78" rx="8" fill="white" stroke="#7da2af"/><text x="480" y="149" text-anchor="middle" font-size="22">finite atlas frame L</text><text x="480" y="177" text-anchor="middle" font-size="16">L*L = α; α = 1 near K₀</text>
<rect x="720" y="105" width="320" height="220" rx="8" fill="#fff2df" stroke="#ba8c42"/><text x="880" y="137" text-anchor="middle" font-size="21">reserve patch O</text>
<rect x="750" y="162" width="110" height="90" fill="white" stroke="#ba8c42"/><rect x="900" y="162" width="110" height="90" fill="white" stroke="#ba8c42"/>
<text x="805" y="199" text-anchor="middle" font-size="20">V₁ h₁</text><text x="955" y="199" text-anchor="middle" font-size="20">V₂ h₂</text>
<text x="880" y="280" text-anchor="middle" font-size="17">separated boxes; flat cell maps</text><text x="880" y="307" text-anchor="middle" font-size="17">W = 𝒱 L; ‖W S f‖ = ‖S f‖</text>
<g stroke="#315d6a" stroke-width="2" fill="none" marker-end="url(#arrow)"><path d="M270 155 L360 155"/><path d="M590 155 L710 155"/></g>
<text x="625" y="135" font-size="18">𝒱</text>
<rect x="50" y="255" width="540" height="90" rx="8" fill="#e1eff7" stroke="#5b8da5"/><text x="320" y="289" text-anchor="middle" font-size="22">full elliptic output Q f</text><text x="320" y="320" text-anchor="middle" font-size="18">support outside the whole reserve neighborhood V</text>
<text x="60" y="405" font-size="20">Normal v = log x is unchanged; every input variable and normal ratio is retained.</text>
<text x="60" y="452" font-size="23">A = Q + S̃;    ‖A f‖₂² = ‖Q f‖₂² + ‖S f‖₂²</text>
<text x="60" y="499" font-size="20">‖Tₗ,ₐ Dₐ u‖₂ ≤ C ( ‖A Dₐ u‖₂ + ‖u‖_ℬ )</text>
<text x="60" y="545" font-size="17">Only genuine flat-input errors use the original Banach norm. All corners remain tested.</text>
<text x="60" y="586" font-size="17">Map and support schematic. Proof: E0–E2, K0–K1, A0; identities OR13–OR20.</text>
<text x="60" y="620" font-size="16">Two reserve boxes are shown; any finite number fits because d ≥ 1.</text></g></svg>''','utf-8')
ET.parse(p);print(p.name)

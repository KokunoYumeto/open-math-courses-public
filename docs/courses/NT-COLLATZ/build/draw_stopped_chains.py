"""Reproducible schematic of actual stopping rules and first-failure transport."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 550" width="440" height="550" role="img" aria-labelledby="title desc">
<title id="title">First failure in a stopped chain</title>
<desc id="desc">An initial source either fails its first test or executes controlled first passages. At each landing the rank test is made before a new envelope test. A low rank gives success. A high first failure is counted by its original source, cumulative time and landing.</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#216576"/></marker></defs>
<rect width="440" height="550" rx="10" fill="#f4f8fa"/>
<g fill="#173342" font-family="Georgia,serif" text-anchor="middle">
<text x="220" y="29" font-size="19">One source, successive tests</text>
<rect x="75" y="48" width="290" height="55" rx="6" fill="#e0edf2" stroke="#719bab"/>
<text x="220" y="71" font-size="17">Start n in the shell I_M</text>
<text x="220" y="92" font-size="15">rank M ≥ terminal rank L</text>
<path d="M220 104V137" stroke="#216576" stroke-width="2" marker-end="url(#arrow)"/>
<text x="220" y="162" font-size="17">Initial envelope test</text>
<path d="M130 169L57 196" stroke="#a55739" stroke-width="2"/>
<text x="55" y="219" font-size="14">fails</text>
<text x="69" y="240" font-size="14">count in I_M</text>
<path d="M246 174L283 206" stroke="#216576" stroke-width="2" marker-end="url(#arrow)"/>
<text x="318" y="196" font-size="14">passes</text>
<rect x="150" y="213" width="260" height="63" rx="6" fill="#e0edf2" stroke="#719bab"/>
<text x="280" y="239" font-size="16">Controlled first-passage blocks</text>
<text x="280" y="260" font-size="15">strictly decreasing threshold ranks</text>
<path d="M280 277V313" stroke="#216576" stroke-width="2" marker-end="url(#arrow)"/>
<text x="280" y="338" font-size="17">Inspect a landing y</text>
<path d="M239 348L122 385M302 348L341 385" stroke="#216576" stroke-width="2" marker-end="url(#arrow)"/>
<text x="102" y="410" font-size="16">rank &lt; L</text>
<text x="102" y="434" font-size="16">success</text>
<text x="334" y="410" font-size="16">rank ≥ L</text>
<text x="334" y="434" font-size="15">test y again</text>
<text x="330" y="458" font-size="14">pass: continue blocks</text>
<text x="330" y="480" font-size="14">fail: first bad landing</text>
<rect x="28" y="498" width="384" height="36" rx="5" fill="#fff" stroke="#719bab"/>
<text x="220" y="521" font-size="14">Count the failed tag (q, h, y) back in the original shell</text>
</g></svg>'''
(ROOT/'figures/stopped-chain.svg').write_text(svg,encoding='utf-8')
print("stopped-chain.svg")


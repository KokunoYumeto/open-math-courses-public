"""Original exact-coordinate diagram for the ordered integral minors."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def pt(x,y): return 110+160*(x-2), 390-160*(y-2)
x0,y0=pt(2,4)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="490" viewBox="0 0 800 490">
<title>Ordered integration intervals give positive minors</title>
<desc>The open rectangle 2 less than x less than 3 and 3 less than y less than 4 lies above the diagonal y equals x. There x to the j times y to the j times the difference y to the k minus j minus x to the k minus j is positive when k is greater than j.</desc>
<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="#243748"/></marker></defs>
<rect width="800" height="490" fill="white"/>
<g font-family="Arial, sans-serif" fill="#172c3d">
<text x="50" y="35" font-size="23">Positivity from the order of two intervals</text>
<rect x="{x0}" y="{y0}" width="160" height="160" fill="#dbefe6" stroke="#176349" stroke-width="2" stroke-dasharray="6 4"/>
<path d="M110,390 H465" stroke="#243748" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<path d="M110,390 V48" stroke="#243748" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<path d="M110,390 L430,70" stroke="#576579" stroke-width="2"/>
<text x="365" y="159" font-size="19">y = x</text>
<text x="469" y="397" font-size="20">x</text><text x="96" y="52" font-size="20">y</text>
'''
for v in (2,3,4):
    x,y=pt(v,v)
    svg+=f'<path d="M{x},385 v10 M105,{y} h10" stroke="#243748"/><text x="{x-5}" y="420" font-size="18">{v}</text><text x="81" y="{y+6}" font-size="18">{v}</text>\n'
svg+='''<text x="145" y="133" font-size="19">x ∈ (2, 3)</text>
<text x="145" y="161" font-size="19">y ∈ (3, 4)</text>
<text x="153" y="195" font-size="22" fill="#14563f">x &lt; y</text>
<text x="490" y="215" font-size="21">For j &lt; k:</text>
<text x="490" y="250" font-size="20">x<tspan baseline-shift="super" font-size="14">j</tspan><tspan baseline-shift="baseline">y</tspan><tspan baseline-shift="super" font-size="14">k</tspan><tspan baseline-shift="baseline"> − x</tspan><tspan baseline-shift="super" font-size="14">k</tspan><tspan baseline-shift="baseline">y</tspan><tspan baseline-shift="super" font-size="14">j</tspan><tspan baseline-shift="baseline"> &gt; 0</tspan></text>
<text x="490" y="285" font-size="18">The positive weights preserve</text>
<text x="490" y="311" font-size="18">this sign under integration.</text>
<text x="50" y="465" font-size="18">Theorem mechanism: each minor Δⱼₖ in (9) is strictly positive.</text>
</g></svg>'''
(ROOT/'figures/logarithmic-minors.svg').write_text(svg,encoding='utf-8')
print('figures/logarithmic-minors.svg')

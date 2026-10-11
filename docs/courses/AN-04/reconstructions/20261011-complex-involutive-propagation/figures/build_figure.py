"""Exact model leaf geometry and logarithmic comparison coefficient. CC0-1.0."""
from pathlib import Path
import math,json,hashlib
r=Path(__file__).resolve().parents[1];out=r/'figures/complex-leaf-comparison.svg'
points=' '.join(f'{620+420*(rho-.25)/.75:.3f},{410-240*math.log(1/rho)/math.log(4):.3f}' for rho in [.25+.75*j/400 for j in range(401)])
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="580" viewBox="0 0 1100 580" role="img" aria-labelledby="title desc">
<title id="title">Complex characteristic leaf and harmonic comparison</title><desc id="desc">A unit disk in one characteristic leaf, with an illustrative boundary collar of radii 0.9 and 1.1. A second plot shows log(1/rho)/log(4) between radii one quarter and one, with value one half at radius one half.</desc>
<rect width="1100" height="580" fill="#f7fafb"/><g font-family="sans-serif" fill="#183344">
<text x="35" y="43" font-size="25" font-weight="bold">Regularity compares across a two-dimensional leaf</text>
<text x="35" y="79" font-size="17">M1: localize the boundary and source</text><text x="610" y="79" font-size="17">P2: an exact harmonic minorant</text>
<circle cx="255" cy="280" r="165" fill="#f3d9aa"/><circle cx="255" cy="280" r="135" fill="#d9edf1"/>
<circle cx="255" cy="280" r="150" fill="none" stroke="#146575" stroke-width="3"/>
<path d="M75 280H440 M255 465V100" fill="none" stroke="#7a8e99" stroke-width="1.5"/>
<path d="M255 280H330l-8 -5m8 5l-8 5 M255 280V205l-5 8m5 -8l5 8" fill="none" stroke="#183344" stroke-width="2.5"/>
<text x="290" y="306" font-size="18">∂x₁</text><text x="267" y="226" font-size="18">∂x₂</text>
<text x="119" y="378" font-size="18">g is L² microlocally on K</text>
<text x="40" y="477" font-size="17">v is L² in a boundary collar</text>
<text x="40" y="508" font-size="17">K = &#123; |z| ≤ 1 &#125;; y and ξ fixed</text>
<path d="M620 150V410H1040" stroke="#183344" stroke-width="2" fill="none"/>
<path d="M620 290H1040" stroke="#cbd9de" stroke-dasharray="5 5"/>
<polyline points="{points}" fill="none" stroke="#146575" stroke-width="3"/>
<circle cx="760" cy="290" r="5" fill="#b75b28"/>
<text x="786" y="277" font-size="18">(1/2, 1/2)</text>
<text x="626" y="130" font-size="19">log(1/ρ) / log 4</text>
<text x="590" y="176" font-size="17">1</text><text x="580" y="296" font-size="17">1/2</text><text x="592" y="416" font-size="17">0</text>
<text x="605" y="440" font-size="17">1/4</text><text x="747" y="440" font-size="17">1/2</text><text x="1033" y="440" font-size="17">1</text>
<text x="960" y="473" font-size="18">radius ρ</text>
<text x="610" y="508" font-size="17">v ≥ −M + (N + M) · coefficient</text>
<text x="35" y="554" font-size="16">At every fixed interior radius the coefficient is positive: letting N grow forces v = +∞.</text>
</g></svg>'''
out.write_text(svg,'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'geometry':{'disk_radius':1,'illustrative_collar_radii':[.9,1.1],'barrier_inner_radius':.25,'barrier_outer_radius':1,'midpoint':[.5,.5],'samples':401},'proof_locators':['M1','P2','X3'],'actually_inspected':False,'exact_coordinate_review_complete':False}
(r/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8')
print(json.dumps(check))

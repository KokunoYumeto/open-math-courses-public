"""Reproduce an exact algebraic diagram; arrows carry no spatial or time scale."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
svg=root/'figures/interior-orders-and-matrix-pulses.svg'
text='''<svg xmlns="http://www.w3.org/2000/svg" width="780" height="460" viewBox="0 0 780 460" role="img" aria-labelledby="title desc">
<title id="title">Exact interior orders and ordered matrix pulses</title>
<desc id="desc">Solution three b-orders over H1 is ordinary H4. Source four b-orders over the energy dual is ordinary H3. For pulse integrals one and one, (0,h) maps to (h,h) and then (h,2h). Both matrices have determinant one. These are algebraic states, not physical trajectories.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#246979"/></marker></defs>
<rect width="780" height="460" rx="12" fill="#f4f7fb"/>
<g font-family="Arial,sans-serif" fill="#132e47">
<text x="24" y="33" font-size="22" font-weight="bold">Interior regularity: retain both orders and matrix order</text>
<rect x="24" y="51" width="732" height="121" rx="8" fill="white" stroke="#8aa0b9"/>
<text x="42" y="78" font-size="17" font-weight="bold">Exact fixed-order requirement (IP11), (IP18), Exercise 1</text>
<text x="42" y="112" font-size="18">Solution: 3 b-orders over V = H¹</text>
<path d="M366 107H427" fill="none" stroke="#246979" stroke-width="2" marker-end="url(#arrow)"/>
<text x="449" y="112" font-size="18">ordinary H⁴</text>
<text x="42" y="148" font-size="18">Source: 4 b-orders over V*</text>
<path d="M366 143H427" fill="none" stroke="#246979" stroke-width="2" marker-end="url(#arrow)"/>
<text x="449" y="148" font-size="18">ordinary H³</text>
<text x="24" y="203" font-size="18" font-weight="bold">Two successive pulses with integrals a = b = 1 (IP23)</text>
<text x="61" y="233" font-size="15">Before either pulse</text>
<text x="309" y="233" font-size="15">Between the pulses</text>
<text x="568" y="233" font-size="15">After both pulses</text>
<g fill="white" stroke="#8aa0b9"><rect x="32" y="247" width="189" height="67" rx="8"/><rect x="294" y="247" width="189" height="67" rx="8"/><rect x="555" y="247" width="193" height="67" rx="8"/></g>
<g font-size="25" text-anchor="middle"><text x="126" y="289">(0, h)</text><text x="388" y="289">(h, h)</text><text x="651" y="289">(h, 2h)</text></g>
<g stroke="#246979" stroke-width="2" fill="none" marker-end="url(#arrow)"><path d="M225 281H287"/><path d="M487 281H548"/></g>
<g font-size="15" text-anchor="middle"><text x="255" y="266">I + N₁</text><text x="517" y="266">I + N₂</text></g>
<text x="32" y="342" font-size="17">Each map is invertible: determinant 1. The full vector stays singular.</text>
<text x="32" y="370" font-size="17">Its first component changes from 0 to h. Here h is any singular distribution.</text>
<path d="M24 393H756" stroke="#8aa0b9"/>
<text x="24" y="417" font-size="14">Arrows: exact linear maps, with no duration or physical trajectory asserted.</text>
<text x="24" y="441" font-size="13">Proof: IP11, IP18, IP23. Sources: Vasy PDF3; programme matrix conjugation GT3–GT17.</text>
</g></svg>'''
svg.write_text(text,'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=dict(schema='AN04-interior-front-figure/v1',svg=svg.relative_to(root).as_posix(),svg_sha256=sha(svg),
 generator_sha256=sha(Path(__file__)),width=780,height=460,proof_locators=['IP11','IP18','IP23'],
 exact_orders={'solution_b':3,'solution_ordinary':4,'source_b':4,'source_ordinary':3},
 pulse_integrals=[1,1],states=[[0,1],[1,1],[1,2]],states_are_coefficients_of_h=True,
 arrows_are_exact_linear_maps=True,no_physical_trajectory_or_duration_claimed=True,
 source_credit='Vasy, Propagation of singularities, PDF3; graph-operator lesson GT3–GT17 and its approved Hörmander source route.',
 new_expression_licence='CC0-1.0',actual_render_visually_inspected=False)
(root/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'exact_algebraic_figure':True,'states':3,'canvas':[780,460]}))

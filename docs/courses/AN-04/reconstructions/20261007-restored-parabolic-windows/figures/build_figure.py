"""Exact position section of RW14–RW17; no embedded font or external asset."""
from pathlib import Path
r = Path(__file__).resolve().parents[1]
f = r / 'figures/parabolic-window-direction.svg'
f.parent.mkdir(parents=True, exist_ok=True)
# Same 220 pixels per coordinate unit on both axes; alpha=1/4, time=1.
x0, y0, scale = 420, 190, 220
def point(y1, y2):
    return x0 + scale*y1, y0 - scale*y2
a, b = point(-1.3, -1.3/4), point(1.3, 1.3/4)
center, witness = point(-1, 0), point(-1, -1/4)
assert center == (200, 190) and witness == (200, 245)
f.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="400" viewBox="0 0 760 400" role="img" aria-labelledby="title desc">
<title id="title">A linear window admits the wrong first-order direction</title><desc id="desc">Position section r=rho=eta1=0, eta2=1 of p=rho squared minus eta1 eta2. The closed set is y2=y1/4. From the origin, the genuine time-one gliding center is (-1,0); the selected point on the closed set is (-1,-1/4), inside the radius-one-half linear window. Both coordinate axes use the same scale.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#284e6c"/></marker></defs>
<rect width="760" height="400" fill="#fff"/><g font-family="Arial, sans-serif" font-size="17" fill="#24333c">
<text x="25" y="31" font-size="20" font-weight="bold">A linear window permits the wrong direction</text>
<circle cx="{center[0]}" cy="{center[1]}" r="110" fill="#f2f6fa" stroke="#8ca7bd" stroke-dasharray="7 5" stroke-width="2"/>
<text x="65" y="65">Radius 1/2 at t = 1</text><line x1="146" y1="72" x2="154" y2="91" stroke="#8ca7bd"/>
<path d="M80 190H731M420 59V328" fill="none" stroke="#a6afb5" stroke-width="1.4"/>
<text x="735" y="195">y₁</text><text x="430" y="62">y₂</text>
<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" fill="none" stroke="#257b68" stroke-width="3"/>
<text x="529" y="99" fill="#216953">F: y₂ = y₁/4</text>
<path d="M420 190H200" fill="none" stroke="#284e6c" stroke-width="3" marker-end="url(#arrow)"/>
<text x="301" y="166" fill="#284e6c">Gliding</text>
<path d="M200 190V245" stroke="#9a5b37" stroke-width="2" stroke-dasharray="4 3"/>
<text x="210" y="226" fill="#9a5b37">Gap 1/4</text>
<circle cx="420" cy="190" r="5" fill="#24333c"/><text x="434" y="212">q = (0,0)</text>
<circle cx="200" cy="190" r="5" fill="#284e6c"/><text x="111" y="151" fill="#284e6c">Center (−1,0)</text>
<circle cx="200" cy="245" r="5" fill="#257b68"/><text x="103" y="281" fill="#216953">Witness (−1,−1/4)</text>
<path d="M200 185V195M640 185V195M415 80H425M415 300H425" stroke="#a6afb5"/>
<text x="638" y="215" font-size="14">1</text><text x="431" y="84" font-size="14">1/2</text><text x="431" y="305" font-size="14">−1/2</text>
<text x="490" y="283" font-size="13">Horizontal arrow: true gliding direction</text><text x="490" y="308" font-size="13">Sloping line: closed characteristic set</text>
<text x="25" y="360" font-size="15">r = ρ = η₁ = 0, η₂ = 1; position section at t = 1.</text><text x="25" y="384" font-size="15">Both coordinate axes have the same Euclidean scale. See Exercise 2 and (RW14)–(RW17).</text>
</g></svg>''', encoding='utf8')
print({'figure': f.relative_to(r).as_posix(), 'same_scale': scale, 'exact_center': center, 'exact_witness': witness})

import json,hashlib
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={'origin':[x0,y0],'center':list(center),'witness':list(witness),'equal_axis_scale':scale,'window_radius':110,'witness_gap':55}
assert 110/scale==1/2 and 55/scale==1/4
(r/'figure-check.json').write_text(json.dumps({'asset':'figures/parabolic-window-direction.svg','sha256':sha(f),'script_sha256':sha(Path(__file__)),'source_sha256':sha(r/'parabolic-wavefront-windows-and-rays.md'),'exact_coordinate_checks':checks,'original_geometry_preserved':True,'layout_only_change':'Fit long legend lines within the original canvas.','actually_inspected':False},indent=2)+'\n',encoding='utf-8')

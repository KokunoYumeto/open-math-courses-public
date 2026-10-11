"""Exact affine phase-coordinate projection and labelled logical dependency diagram."""
from pathlib import Path
import math
out=Path(__file__).with_name('airy-solution-matching.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="650" viewBox="0 0 1080 650">',
 '<rect width="1080" height="650" fill="#f8fafc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b}.title{font-size:23px;font-weight:bold}.label{font-size:17px}.small{font-size:15px}.box{fill:white;stroke:#c6d3dc;stroke-width:2}</style>',
 '<text x="30" y="38" class="title">Incoming matching at a strict diffractive point</text>',
 '<text x="30" y="70" class="label">Affine model: μ = 0, λ = 1. Exact (s,q) projection.</text>']
def text(x,y,t,cl='label'):parts.append(f'<text x="{x}" y="{y}" class="{cl}">{t}</text>')
sx=lambda s:270+180*s
qy=lambda q:445-285*q
parts+=['<path d="M 55 445 H 485 M 270 460 V 130" stroke="#778897" fill="none"/>',
 '<path d="M 55 373.75 H 485" stroke="#83949f" stroke-dasharray="6 5"/>']
text(463,470,'s');text(280,137,'q');text(278,467,'0','small')
text(46,365,'q₁ = 1/4','small')
for eps,color in [(1,'#086e8c'),(-1,'#ba5935')]:
    # Parameter t=sqrt(q) makes the central contact regular in the plotted parameter.
    pts=[(sx(-eps*i/100),qy((i/100)**2)) for i in range(101)]
    parts.append('<polyline fill="none" stroke="'+color+'" stroke-width="3" points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)+'"/>')
    parts.append(f'<circle cx="{sx(-eps*.5)}" cy="{qy(.25)}" r="6" fill="{color}"/>')
text(45,112,'Positive branch T₊','small');text(317,112,'Negative branch T₋','small')
text(38,498,'sε(q) = −ε√q;   ρε(q) = ε√q')
text(38,525,'Omitted coordinate: tε(q) = −(2ε/3)q³ᐟ²')
text(38,554,'At q₁: sε = −ε/2, tε = −ε/12, ρε = ε/2','small')
text(38,594,'ASM:I0, X1, V0. No physical-time arrows are asserted.','small')
boxes=[
 (102,'1. Actual weak Cauchy trace','Q₁(Dq − A₊)u(q₁) ∈ H⁻¹ᐟ²','ASM:C0'),
 (220,'2. Incoming coefficient','β₀ ∈ H¹ᐟ³ → α ∈ H⁵ᐟ⁶','ASM:C1–C2; α₀ = 2β₀'),
 (338,'3. Actual boundary match','v ∈ H_L;   γU − γu is regular','ASM:B0–B1'),
 (456,'4. Finite-order comparison','u − U ∈ Xₘ for every m on W₀','ASM:R0; source and cap verified')]
for y,title,body,loc in boxes:
    parts.append(f'<rect x="555" y="{y}" width="490" height="94" rx="8" class="box"/>')
    text(573,y+26,title);text(573,y+53,body);text(573,y+78,loc,'small')
    if y<456:parts.append(f'<path d="M800 {y+95} V{y+114} m-5 -6 l5 6 5 -6" fill="none" stroke="#496477" stroke-width="2"/>')
text(560,589,'H_w membership still requires the displaced input norm.','small')
text(560,614,'ASM:R1, X2. Tangential regularity ≠ normal smoothness.','small')
parts.append('</svg>')
out.write_text('\n'.join(parts)+'\n','utf-8')
print(out)

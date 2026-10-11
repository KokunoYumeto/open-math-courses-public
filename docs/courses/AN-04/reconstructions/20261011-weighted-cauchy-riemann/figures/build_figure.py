"""Reproduce the exact quadratic-gap and normalized-peak diagram. CC0-1.0."""
from pathlib import Path
import math
out=Path(__file__).resolve().parent/'weighted-cauchy-riemann.svg'
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650" role="img" aria-labelledby="title desc">',
 '<title id="title">The curvature gap and a normalized holomorphic peak</title>',
 '<desc id="desc">Exact circles around z0=1/2 with radii 1/4 and 1/2, and exact normalized modulus profiles exp(-4r squared) and exp(-16r squared).</desc>',
 '<rect width="1100" height="650" fill="#f7f9fc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#143149}.title{font-size:24px;font-weight:bold}.label{font-size:17px}.small{font-size:15px}.axis{stroke:#9caebc;stroke-width:1.5}</style>']
def text(x,y,value,cls='label'):parts.append(f'<text x="{x}" y="{y}" class="{cls}">{value}</text>')
def line(x1,y1,x2,y2,extra='class="axis"'):parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {extra}/>')
text(28,38,'Weighted Cauchy–Riemann construction: curvature and correction','title')
text(38,83,'Exact quadratic example: φ(z)=|z|², z₀=1/2.')
parts.append('<circle cx="285" cy="285" r="100" fill="#f4dac8" stroke="#b75a30" stroke-width="2"/>')
parts.append('<circle cx="285" cy="285" r="50" fill="#f7f9fc" stroke="#b75a30" stroke-width="2"/>')
line(140,285,425,285);line(185,135,185,425)
text(420,277,'x');text(193,145,'y')
text(177,310,'0','small');text(272,310,'1/2','small');text(377,310,'1','small')
text(147,190,'1/2','small');text(140,390,'−1/2','small')
parts.append('<circle cx="285" cy="285" r="4" fill="#00728c"/>')
text(256,269,'z₀','small')
line(285,285,320.355,249.645,'stroke="#b75a30"')
text(308,235,'r=1/4','small')
text(343,180,'r=1/2','small')
text(36,448,'Cutoff derivative: 1/4 ≤ |z−z₀| ≤ 1/2.')
text(36,477,'Gap φ−Re g = |z−z₀|² ≥ 1/16.')
text(36,505,'g(z)=z−1/4; Fₜ(z)=tᵍ⁽ᶻ⁾ needs no correction.','small')
text(570,83,'Exact normalized modulus |Fₜ| / tᵠ = e⁻⁽ˡᵒᵍ ᵗ⁾ʳ².')
x0,y0,width,height=605,402,420,245
line(x0,y0,x0+width,y0);line(x0,y0-height,x0,y0)
for v in [0,.25,.5,.6]:
 xx=x0+width*v/.6;line(xx,y0,xx,y0+5);text(xx-10,y0+25,str(v),'small')
for v in [0,.5,1]:
 yy=y0-height*v;line(x0-5,yy,x0,yy);text(x0-32,yy+5,str(v),'small')
for exponent,color in [(4,'#08758d'),(16,'#b6532d')]:
 points=' '.join(f'{x0+width*i/180:.3f},{y0-height*math.exp(-exponent*(.6*i/180)**2):.3f}' for i in range(181))
 parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
text(849,155,'t=e⁴','small');line(814,150,839,150,'stroke="#08758d" stroke-width="3"')
text(849,184,'t=e¹⁶','small');line(814,179,839,179,'stroke="#b6532d" stroke-width="3"')
text(1050,421,'r','small')
text(571,448,'At r=1/4: ratios e⁻¹⁄⁴ and e⁻¹.')
text(571,477,'Ratio to the weight; not an interior maximum.')
text(571,505,'Exact profiles, sampled only for rendering.','small')
parts.append('<rect x="28" y="535" width="1044" height="91" rx="8" fill="white" stroke="#bacbd8"/>')
text(46,563,'Curvature controls the solution: ∫|u|²e⁻ᶲ ≤ 4∫|f|²e⁻ᶲ/(ΔΦ).  WCR:W0–W1, X1.')
text(46,593,'Radius 1/log t controls the weight; each derivative costs (log t).  WCR:P1–P2, X2–X3.')
parts.append('</svg>')
out.write_text('\n'.join(parts)+'\n','utf-8')
print(out.name)

"""Exact Hamilton projection and the complete glancing estimate dependency chain. CC0."""
from pathlib import Path
from html import escape
from math import sqrt
r=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590">',
'<rect width="1040" height="590" fill="white"/>',
'<style>text{font-family:Arial,sans-serif;fill:#172c3e}.small{font-size:15px}.label{font-size:18px}.title{font-size:21px;font-weight:bold}</style>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#536c80"/></marker><marker id="ray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#ad3556"/></marker></defs>']
def text(x,y,value,cls='label',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def line(x1,y1,x2,y2,color='#536c80',width=2,marker=None):
 extra=f' marker-end="url(#{marker})"' if marker else ''
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>')
def box(x,y,w,h,color):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{color}" stroke="#b4c4ce"/>')
zx=lambda z:263+183*z/(sqrt(2)/4)
xx=lambda x:474-338*x/(1/32)
text(35,38,'A full ray at nonradial glancing','title')
text(554,38,'All terms reach the actual data','title')
parts.append('<rect x="80" y="104" width="366" height="370" fill="#eaf3fb"/>')
line(68,474,475,474,marker='arrow');line(263,486,263,90,marker='arrow')
text(483,480,'z₁');text(272,95,'x')
line(80,136,446,136,'#b5c7d4',1)
text(250,141,'1/32','small','end')
pts=[]
for j in range(161):
 tau=-.25+j*.5/160
 pts.append(f'{zx(-sqrt(2)*tau):.5f},{xx(tau*tau/2):.5f}')
parts.append('<polyline points="'+' '.join(pts)+'" fill="none" stroke="#ad3556" stroke-width="3"/>')
for t0,t1 in [(-.20,-.17),(.17,.20)]:
 line(zx(-sqrt(2)*t0),xx(t0*t0/2),zx(-sqrt(2)*t1),xx(t1*t1/2),'#ad3556',3,'ray')
parts.append('<circle cx="263" cy="474" r="5" fill="#ad3556"/>')
text(96,121,'τ = 1/4','small')
text(353,121,'τ = −1/4','small')
text(285,205,'x = z₁² / 4')
text(95,82,'Arrows: increasing τ','small')
text(80,503,'−√2/4','small','middle');text(263,503,'0','small','middle');text(446,503,'√2/4','small','middle')
text(82,542,'ρ = τ/2; ζ = xρ = τ³/4','small')
text(82,568,'Projection of the exact trajectory (GI31).','small')
box(552,74,452,83,'#eaf3fb')
text(572,105,'v = Sₐ⁻¹Hu,  γ₀v = 0')
text(572,132,'Gauge retained; coarse Xₛ comes from B and f.','small')
line(779,158,779,185,marker='arrow')
box(552,187,452,91,'#fff0d0')
text(572,219,'Finite half gains on the same final region')
text(572,247,'Keep incoming, source and coarse terms.','small')
text(572,270,'Mⱼ₊₁ ≤ Cⱼ (Mⱼ + Iⱼ + Fⱼ + coarse)','small')
line(779,279,779,307,marker='arrow')
box(552,309,452,94,'#eaf4ef')
text(572,342,'One fixed incoming observation')
text(572,369,'O = G Aobs + R; retain the full residual R.','small')
text(572,393,'Its bound uses the original equation Pu = f.','small')
line(779,404,779,432,marker='arrow')
box(552,434,452,95,'#f0edf9')
text(572,466,'One scalar source test for the full union')
text(572,493,'Tf = Bₜ A f, including every residual family.','small')
text(572,519,'‖Cu‖ ≤ C (‖Af‖ + ‖Aobs u‖ + ‖u‖ℬ)','small')
text(573,565,'No ordinary normal derivative of f is required.','small')
parts.append('</svg>')
(r/'glancing-source-interface.svg').write_text('\n'.join(parts)+'\n','utf-8')
print('Wrote the exact Hamilton projection and estimate diagram.')

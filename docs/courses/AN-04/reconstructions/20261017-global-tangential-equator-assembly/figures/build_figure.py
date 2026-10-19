"""Reproduce the operator and exact normal-support diagram."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="660" viewBox="0 0 1100 660" role="img" aria-labelledby="title desc"><title id="title">Global tangential-equator scalar assembly</title><desc id="desc">A bounded positive operator Q and a residual sandwich S have a smooth interior commutator. The normal cutoff margin and its interior error interval are exact.</desc><rect width="1100" height="660" fill="#f7f9fc"/>']
def text(x,y,t,size=20,color='#162942'):parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(t)}</text>')
def box(x,y,w,h,title,sub):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#355a85" stroke-width="2"/>');text(x+15,y+30,title,22);text(x+15,y+59,sub,17)
text(30,39,'One scalar test on the whole manifold',28)
text(30,73,'Allowed cone contains every boundary tangential direction; full corner kernels remain.',18)
box(30,105,320,86,'Q = B²,   R = I − Q','Q bounded, positive; elliptic on K')
box(390,105,320,86,'P = χ p(Dv) χ','Bounded positive normal operator')
box(750,105,320,86,'S = R P R','Positive full boundary residual')
text(34,229,'Q(κ) − I is tangentially smoothing, with polynomial κ bounds.',21)
text(34,265,'[Q,S] has a smooth kernel with both projections compactly interior.',21)
box(80,295,940,87,'A = (Q + iS) Lᴹ','The commutator quadratic form is bounded by C ‖u‖²B; both test norms are recovered.')
text(30,424,'Exact support buffer in logarithmic normal distance',23)
text(30,460,'χ = 1 for x ≤ a₀;  χ = 0 for x ≥ 2a₀.    2a₀ exp(4HQ + 2Hp) < ε₀.',20)
parts.append('<line x1="70" y1="512" x2="1030" y2="512" stroke="#62748b" stroke-width="3"/><rect x="250" y="492" width="580" height="40" fill="#d8e9f5" stroke="#355a85"/>')
text(50,563,'x = 0',17);text(205,563,'a₀ exp(−Hp − 2HQ)',18);text(690,563,'2a₀ exp(Hp + 2HQ)',18)
text(250,607,'Support of the output-cutoff error: a fixed interior annulus.',20)
text(30,643,'See Q0–Q2, S0–S3 and P0–P1 for full kernels, densities and exact support arguments.',17)
parts.append('</svg>');Path(__file__).with_name('global-tangential-equator-assembly.svg').write_text(''.join(parts),'utf-8')

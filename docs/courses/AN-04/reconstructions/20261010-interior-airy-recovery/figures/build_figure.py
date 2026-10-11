"""Exact affine ray projection and sampled normalized Airy boundary layer."""
from pathlib import Path
import math
import mpmath as mp
mp.mp.dps=45
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="600" viewBox="0 0 1080 600">',
'<rect width="1080" height="600" fill="#f3f7fa"/>',
'<style>text{font-family:Arial,Helvetica,sans-serif;fill:#18364d}.small{font-size:14px}.body{font-size:17px}</style>',
'<text x="25" y="35" font-size="23" font-weight="bold">Interior recovery separates the branches; the boundary weight needs more</text>',
'<text x="50" y="78" class="body">Exact affine ray projection: μ = 0, w = 0</text>',
'<text x="580" y="78" class="body">Exact normalized Airy modulus: λ = 256</text>']
qx=lambda q:430-q*850
yx=lambda y:280+y*320
for left,right in [(75,485),(620,1020)]:
 if left==75:
  parts.append(f'<rect x="{left}" y="{qx(.30):.1f}" width="{right-left}" height="{qx(.18)-qx(.30):.1f}" fill="#e1ece8"/>')
 else:
  parts.append(f'<rect x="{620+.18/.34*400:.1f}" y="115" width="{.12/.34*400:.1f}" height="315" fill="#e1ece8"/>')
for q0 in [0,.1,.2,.3]:
 yy=qx(q0)
 parts.append(f'<path d="M75 {yy:.1f} H485" stroke="#d4dde5"/><text x="40" y="{yy+5:.1f}" class="small">{q0:.1f}</text>')
for ep,col in [(1,'#086b91'),(-1,'#aa5524')]:
 pts=' '.join(f'{yx(-ep*math.sqrt(q)):.2f},{qx(q):.2f}' for q in [j*.34/170 for j in range(171)])
 parts.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3"/>')
parts+=['<path d="M75 108 V430 H495" fill="none" stroke="#6c8191"/>',
'<text x="40" y="105" class="body">q</text><text x="492" y="454" class="body">y₁</text>',
'<text x="77" y="463" class="small">−0.6</text><text x="275" y="463" class="small">0</text><text x="465" y="463" class="small">0.6</text>',
'<text x="84" y="143" class="small">ε = +1, ρ = +λ√q</text>',
'<text x="315" y="143" class="small">ε = −1, ρ = −λ√q</text>',
'<text x="182" y="410" class="small">fold at q = 0</text>',
'<text x="192" y="239" class="small">observed slab</text>']
R=mp.mpf(256);a=mp.mpf('.04');k=R**(mp.mpf(2)/3);b=a*k
mod=lambda t:mp.sqrt(mp.airyai(t)**2+mp.airybi(t)**2)
den=mod(b)
x=lambda q:620+q/.34*400
y=lambda z:115-z*220
for z in [0,-.5,-1]:
 parts.append(f'<path d="M620 {y(z):.1f} H1020" stroke="#d4dde5"/><text x="574" y="{y(z)+5:.1f}" class="small">10^{z:g}</text>')
pts=[]
for j in range(341):
 q=j/1000
 val=float(mp.log10(mod(b-mp.mpf(str(q))*k)/den))
 pts.append(f'{x(q):.2f},{y(val):.2f}')
parts+=['<polyline points="'+' '.join(pts)+'" fill="none" stroke="#7650a2" stroke-width="3"/>',
'<path d="M620 108 V430 H1030" fill="none" stroke="#6c8191"/>']
for q0 in [0,.1,.2,.3]:
 parts.append(f'<text x="{x(q0)-10:.1f}" y="454" class="small">{q0:.1f}</text>')
parts+=[f'<path d="M{x(.04):.1f} 115 V430" stroke="#b37932" stroke-dasharray="5 4"/>',
'<text x="672" y="150" class="small">turning point q = a = 0.04</text>',
'<text x="824" y="398" class="small">observed slab</text>',
'<text x="1032" y="454" class="body">q</text>',
'<text x="583" y="486" class="small">Logarithmic scale; |F(b − q λ^(2/3)) / F(b)|</text>',
'<text x="53" y="486" class="small">Projection only; y_d and spectator coordinates omitted.</text>',
'<text x="25" y="534" class="body">IR10–IR15: recover α in H^(5/6). IR17–IR21: interior data alone cannot recover v in H_w.</text>',
'<text x="25" y="570" class="small">The finite-frequency Airy samples illustrate the proved bounds; they are not evidence for the asymptotic theorem.</text>',
'</svg>']
Path(__file__).with_name('interior-airy-recovery.svg').write_text('\n'.join(parts),'utf-8')
print('Wrote exact affine projections and 341 normalized Airy samples.')

"""Draw the exact normal window and scaled polynomial trace kernels."""
from pathlib import Path
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="600" viewBox="0 0 1080 600">',
'<rect width="1080" height="600" fill="#f3f7fa"/>',
'<style>text{font-family:Arial,Helvetica,sans-serif;fill:#18364d}.small{font-size:14px}.body{font-size:17px}</style>',
'<text x="25" y="35" font-size="23" font-weight="bold">A normal integration window matched to the boundary frequency</text>',
'<text x="50" y="78" class="body">Exact scaled interval: 0 ≤ q ≤ τ / κ</text>',
'<text x="590" y="78" class="body">Exact kernels cancel the unknown v′(0)</text>']
xx=lambda b:75+(b+8)*26.25
yy=lambda q:430-q*290
curve=[(b,(1+b*b)**(-.25)) for b in [-8+j/20 for j in range(321)]]
pts=' '.join(f'{xx(b):.2f},{yy(q):.2f}' for b,q in curve)
parts.append(f'<polygon points="75,430 {pts} 495,430" fill="#dceee7"/>')
for val in [0,.25,.5,.75,1]:
 parts.append(f'<path d="M75 {yy(val):.1f} H495" stroke="#d4dde5"/><text x="30" y="{yy(val)+5:.1f}" class="small">{val:g}</text>')
parts+=[f'<polyline points="{pts}" fill="none" stroke="#087d67" stroke-width="3"/>',
'<path d="M75 115 V430 H505" fill="none" stroke="#6c8191"/>',
'<text x="48" y="108" class="small">q ℓ^(2/3) / τ</text>']
for b in [-8,-4,0,4,8]:
 parts.append(f'<text x="{xx(b)-7:.1f}" y="454" class="small">{b}</text>')
parts+=['<text x="510" y="454" class="body">b</text>',
'<text x="155" y="328" class="body">q κ ≤ τ</text>',
'<text x="120" y="482" class="small">Top curve = (1 + b²)^(−1/4) = L / ℓ^(4/3)</text>']
sx=lambda t:620+t*400
sy=lambda a:340-a*185
for val in [-.5,0,.5,1]:
 parts.append(f'<path d="M620 {sy(val):.1f} H1020" stroke="#d4dde5"/><text x="577" y="{sy(val)+5:.1f}" class="small">{val:g}</text>')
for fun,col,dash in [(lambda t:1-1.5*t,'#aa5524',''),(lambda t:6.75*t*(1-t)**2,'#086b91','5 3')]:
 ps=' '.join(f'{sx(j/200):.2f},{sy(fun(j/200)):.2f}' for j in range(201))
 parts.append(f'<polyline points="{ps}" fill="none" stroke="{col}" stroke-width="3" stroke-dasharray="{dash}"/>')
parts+=['<path d="M620 115 V433 H1030" fill="none" stroke="#6c8191"/>',
'<text x="627" y="123" class="small">ψ(s) / 4 = 1 − 3s/2</text>',
'<text x="797" y="148" class="small">27s(1 − s)² / 4</text>']
for t in [0,.25,.5,.75,1]:
 parts.append(f'<text x="{sx(t)-8:.1f}" y="455" class="small">{t:g}</text>')
parts+=['<text x="1032" y="455" class="body">s</text>',
'<text x="605" y="482" class="small">Actual moments: ∫ψ = 1, ∫sψ = 0</text>',
'<text x="25" y="532" class="body">BT4–BT7: trace identity. BT9–BT12: the equation is bounded on this exact frequency window.</text>',
'<text x="25" y="569" class="small">BT21 controls the boundary-layer trace of actual energy solutions. It does not assert recovery of the full stable Airy weight.</text>',
'</svg>']
Path(__file__).with_name('boundary-layer-trace.svg').write_text('\n'.join(parts),'utf-8')
print('Wrote exact window and polynomial-kernel illustration.')

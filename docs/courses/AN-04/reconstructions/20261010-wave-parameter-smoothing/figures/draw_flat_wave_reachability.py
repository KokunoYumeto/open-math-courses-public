"""Exact covector slice of H_a>0; original SVG, CC0-1.0."""
import math
from pathlib import Path
W,H=1100,590
x0,x1,y0,y1=100,1050,90,485
X=lambda th:x0+(th+math.pi)/(2*math.pi)*(x1-x0)
Y=lambda T:y1-(T+.8)/1.6*(y1-y0)
pts=[(X(-math.pi+2*math.pi*j/720),Y(-.5*math.cos(-math.pi+2*math.pi*j/720))) for j in range(721)]
curve=' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)
poly=f'{x0},{y0} {x1},{y0} '+' '.join(f'{x:.3f},{y:.3f}' for x,y in reversed(pts))
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Exact flat-wave reachable covector slice">',
'<rect width="1100" height="590" fill="white"/>',
'<style>text{font-family:Arial,sans-serif;fill:#183246;font-size:20px}.small{font-size:18px}</style>',
'<text x="100" y="36" font-size="25">Which characteristic directions return from a forward cone?</text>',
'<text x="100" y="65" class="small">q = (1/2, 0), τ = 1, ξ = (cos θ, sin θ), T = t − a</text>',
f'<polygon points="{poly}" fill="#d9edf7"/>']
for T in [-.5,0,.5]:
 y=Y(T);s += [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#bdcbd3" stroke-dasharray="5 5"/>',f'<text x="53" y="{y+7}">{T:g}</text>']
s += [f'<polyline points="{curve}" fill="none" stroke="#146575" stroke-width="3"/>',f'<path d="M{x0} {y0} V{y1} H{x1}" fill="none" stroke="#183246" stroke-width="2"/>']
for th,label in [(-math.pi,'−π'),(-math.pi/2,'−π/2'),(0,'0'),(math.pi/2,'π/2'),(math.pi,'π')]:
 x=X(th);s += [f'<text x="{x}" y="520" text-anchor="middle">{label}</text>']
s += ['<text x="1080" y="520">θ</text>','<text x="65" y="85">T</text>',
'<text x="420" y="140">Hₐ &gt; 0: reachable</text>',
'<text x="440" y="435">Hₐ &lt; 0: excluded</text>',
'<text x="100" y="560" class="small">Boundary: T = −(cos θ)/2. Strict inequality excludes the curve Hₐ = 0.</text>','</svg>']
Path(__file__).with_name('flat-wave-reachable-covectors.svg').write_text('\n'.join(s)+'\n','utf-8')

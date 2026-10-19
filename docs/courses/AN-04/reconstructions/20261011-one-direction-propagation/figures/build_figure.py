"""Exact directional regularity regions and sampled coefficients. CC0-1.0."""
from pathlib import Path
import math,json,hashlib,html
root=Path(__file__).resolve().parent.parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="780" viewBox="0 0 1100 780">','<rect width="1100" height="780" fill="white"/>']
def text(x,y,t,size=19,c='#193247'):parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-family="sans-serif" fill="{c}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,c='#8897a5',w=1):parts.append(f'<path d="M{x1:.3f},{y1:.3f} L{x2:.3f},{y2:.3f}" stroke="{c}" stroke-width="{w}" fill="none"/>')
def curve(points,c):parts.append('<path d="M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="3"/>')
blue='#176d91';red='#b43753';green='#27794b'
text(35,37,'A. Flat damping: P = Dₜ − i a(t)Dᵧ',24)
X=lambda t:190+140*t;Y=lambda a:286-120*a
line(X(-1),Y(0),X(2),Y(0));line(X(0),Y(0),X(0),Y(1))
for t in [-1,0,1,2]:line(X(t),Y(0)-4,X(t),Y(0)+4);text(X(t)-8,Y(0)+27,str(t),16)
for val in [.5,1]:line(X(0)-4,Y(val),X(0)+4,Y(val));text(X(0)-37,Y(val)+6,str(val),16)
text(483,293,'t');text(169,144,'a(t)')
def a(t):return 2*t**-3*math.exp(-1/t**2) if t>0 else 0
curve([(X(t),Y(a(t))) for t in [-1+3*i/600 for i in range(601)]],blue)
text(215,108,'a(t) = 2t⁻³e⁻¹/ᵗ² for t > 0',19,blue)
text(50,354,'a = 0 on t ≤ 0; a > 0 on t > 0.',19)
text(565,37,'B. Exact regions of the solution',24)
parts.append('<rect x="600" y="106" width="185" height="176" fill="#f8e9ee"/><rect x="785" y="106" width="245" height="176" fill="#e7f2ec"/>')
line(600,194,1030,194);line(785,98,785,292)
line(610,194,785,194,red,4);text(613,150,'singular at y = 0',19,red)
text(848,151,'smooth',23,green);text(733,319,'t = 0',18);text(1042,201,'t',19);text(779,84,'y',19)
line(625,344,1000,344,blue,3);line(1000,344,987,336,blue,3);line(1000,344,987,352,blue,3)
text(665,380,'f ≤ 0: increasing-time propagation',19,blue)
text(35,428,'C. A zero Hessian inside the quadratic extension N₁₂ᵉ',24)
CX=lambda t:555+190*t;CY=lambda q:492-22*q
line(CX(-2),CY(0),CX(2),CY(0));line(CX(0),CY(-8),CX(0),CY(0))
for t in [-2,-1,0,1,2]:line(CX(t),CY(0)-4,CX(t),CY(0)+4);text(CX(t)-7,CY(0)-16,str(t),16)
for q in [-2,-4,-6,-8]:line(CX(0)-4,CY(q),CX(0)+4,CY(q));text(CX(0)-34,CY(q)+6,str(q),16)
curve([(CX(t),CY(-2*t*t)) for t in [-2+4*i/500 for i in range(501)]],blue)
parts.append(f'<circle cx="{CX(0)}" cy="{CY(0)}" r="5" fill="{red}"/>')
text(760,456,'Qₜ = −2t² dx²',21,blue);text(950,499,'t',19);text(200,708,'Q₀ = 0, but the same curve meets Qₜ ≠ 0: it is not in N₁₃.',20)
text(35,758,'Proofs: ODP:X2–X3. Boundaries and formulas are exact; smooth curves are numerical samples.',18)
parts.append('</svg>');p=root/'figures/one-direction-propagation.svg';p.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d={'svg':'figures/'+p.name,'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'sample_counts':[601,501],'ranges':{'damping_time':[-1,2],'hessian_time':[-2,2]},'source_proof_locators':['ODP:X2','ODP:X3','ODP:V0'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                         }
(root/'figure-check.json').write_text(json.dumps(d,indent=2)+'\n','utf-8');print(json.dumps({'figure_sha256':d['svg_sha256']}))

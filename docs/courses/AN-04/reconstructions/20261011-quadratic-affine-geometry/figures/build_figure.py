"""Coordinate plots of the proved flat and radial models. CC0-1.0."""
from pathlib import Path
import math,html,json,hashlib
root=Path(__file__).resolve().parent.parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="900" viewBox="0 0 1100 900">','<rect width="1100" height="900" fill="white"/>']
def text(x,y,t,size=20,color='#193247'):
    parts.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,color='#8090a0',width=1):
    parts.append(f'<path d="M{x1:.3f},{y1:.3f} L{x2:.3f},{y2:.3f}" stroke="{color}" stroke-width="{width}" fill="none"/>')
def curve(points,color):
    d='M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in points)
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3"/>')
def E(s):return math.exp(-1/s**2) if s>0 else 0.0
def B(s):return s*E(s)-math.sqrt(math.pi)*math.erfc(1/s) if s>0 else 0.0
def h(t):return E(t-1)+E(-t-1)
def primitive(t):return B(t-1)-B(-t-1)
X1=lambda t:80+(t+3)*70;X2=lambda t:610+(t+3)*70
text(35,40,'A. Flat coefficient h(t)',23);text(575,40,'B. Affine coordinate u(t) = ∫₀ᵗ h',23)
for X,base in [(X1,265),(X2,180)]:
    line(X(-3),base,X(3),base)
    for t in [-3,-1,0,1,3]:
        line(X(t),base-4,X(t),base+4);text(X(t)-8,base+26,str(t),17)
    text(X(3)+14,base+7,'t',18)
line(80,90,80,265);line(610,80,610,280)
text(55,75,'h',18);text(582,76,'u',18)
for value in [0.5,1]:
    yy=265-170*value;line(76,yy,84,yy);text(37,yy+6,str(value),16)
for value in [-0.5,0.5]:
    yy=180-115*value;line(606,yy,614,yy);text(558,yy+6,str(value),16)
curve([(X1(-3+6*i/600),265-170*h(-3+6*i/600)) for i in range(601)],'#166a8b')
curve([(X2(-3+6*i/600),180-115*primitive(-3+6*i/600)) for i in range(601)],'#166a8b')
line(X1(-1),265,X1(1),265,'#b03b54',5);line(X2(-1),180,X2(1),180,'#b03b54',5)
text(193,236,'h = 0',18,'#b03b54');text(775,153,'u = 0',18,'#b03b54')
text(45,335,'Both plots have the exact zero interval [−1, 1]; the affine quotient collapses it.',20)
text(45,400,'C. Radial characteristic: ξ₁ = e⁻ᵗ and u = −ξ₁',23)
RX=lambda k:140+110*k;RY=lambda val:500-45*val
line(RX(0),RY(0),RX(8),RY(0));line(RX(0),RY(-8),RX(0),RY(0))
for k in [0,2,4,6,8]:
    line(RX(k),RY(0)-4,RX(k),RY(0)+4);text(RX(k)-8,RY(0)-14,str(k),17)
for val in [-2,-4,-6,-8]:
    line(RX(0)-4,RY(val),RX(0)+4,RY(val));text(RX(0)-39,RY(val)+6,str(val),17)
text(1040,505,'ξ₁',21);text(84,454,'u',21)
curve([(RX(math.exp(-t)),RY(-math.exp(-t))) for t in [-2+4*i/400 for i in range(401)]],'#166a8b')
for t in [-2,0,2]:
    k=math.exp(-t);parts.append(f'<circle cx="{RX(k):.3f}" cy="{RY(-k):.3f}" r="5" fill="#b03b54"/>')
text(RX(math.exp(2))-120,RY(-math.exp(2))+32,'t = −2',19,'#b03b54')
line(RX(1),RY(-1)+6,RX(1)+28,RY(-1)+40,'#b03b54')
text(RX(1)+38,RY(-1)+58,'t = 0',19,'#b03b54')
line(RX(math.exp(-2))+6,RY(-math.exp(-2))+2,390,530,'#b03b54')
text(401,535,'t = 2',19,'#b03b54')
text(590,600,'Increasing t moves toward ξ₁ = 0.',20)
text(590,637,'The affine relation u = −ξ₁ is exact.',20)
parts.append('</svg>');p=root/'figures/quadratic-affine-geometry.svg';p.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'svg':'figures/'+p.name,'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),
 'sample_counts':[601,601,401],'ranges':{'flat_time':[-3,3],'radial_time':[-2,2]},
 'primitive_evaluation':'B(s)=s exp(-1/s^2)-sqrt(pi) erfc(1/s) for s>0, zero otherwise; u=B(t-1)-B(-t-1). This evaluates the integral in X1. Differentiate B to obtain E; its limit at zero is zero.',
 'source_proof_locators':['QAF:X1','QAF:X2','QAF:V0'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                         }
(root/'figure-check.json').write_text(json.dumps(r,indent=2)+'\n','utf-8');print(json.dumps({'figure_sha256':r['svg_sha256']}))

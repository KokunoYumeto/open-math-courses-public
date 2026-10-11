"""Exact semidefinite model formulas, numerically sampled curves. CC0-1.0."""
from pathlib import Path
import math,html,json,hashlib
root=Path(__file__).resolve().parent.parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="660" viewBox="0 0 1100 660">','<rect width="1100" height="660" fill="white"/>']
def text(x,y,t,size=19,color='#193247'):
 parts.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}">{html.escape(t)}</text>')
def line(x1,y1,x2,y2,c='#8090a0',width=1):
 parts.append(f'<path d="M{x1:.3f},{y1:.3f} L{x2:.3f},{y2:.3f}" stroke="{c}" stroke-width="{width}" fill="none"/>')
def curve(points,c):
 parts.append('<path d="M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="3"/>')
def E(w):return math.exp(-1/w**2) if w>0 else 0.
blue='#176d91';red='#b43753';green='#27794b'
text(30,38,'A. The quotient correction at t = 1',24)
text(565,38,'B. Exact division is impossible',24)
X=lambda w:100+400*w;Y=lambda h:250-650*h
line(X(-.15),Y(0),X(1),Y(0));line(X(0),Y(-.4),X(0),Y(.15))
for v in [0,.5,1]:
 line(X(v),Y(0)-4,X(v),Y(0)+4);text(X(v)-7,Y(0)+28,str(v),16)
for val in [-.3,-.1,.1]:
 line(X(0)-4,Y(val),X(0)+4,Y(val));text(43,Y(val)+6,str(val),16)
text(510,257,'w');text(110,139,'quotient')
curve([(X(w),Y(-E(w))) for w in [1*i/400 for i in range(401)]],red)
line(X(-.12),Y(0),X(1),Y(0),green,4)
text(240,210,'corrected h = 0',20,green)
text(222,439,'preliminary H = −E(w)',20,red)
text(35,548,'Add Φ = E(w); every jet at w = 0 stays zero.',19)
text(35,580,'The remainder becomes E(w)(1 − w³) at u = 0.',18)
a=math.exp(-4);RX=lambda v:615+(v+.03)/.095*415;RY=lambda f:443-f/.0055*335
line(RX(-.03),RY(0),RX(.065),RY(0));line(RX(0),RY(0),RX(0),RY(.0055))
for val in [-.02,0,.02,.04,.06]:
 line(RX(val),RY(0)-4,RX(val),RY(0)+4);text(RX(val)-15,RY(0)+26,str(val),15)
for val in [.002,.004]:
 line(RX(0)-4,RY(val),RX(0)+4,RY(val));text(RX(0)-59,RY(val)+6,str(val),15)
vals=[-.03+.095*i/500 for i in range(501)]
curve([(RX(v),RY(v*v)) for v in vals],blue)
curve([(RX(v),RY((v-a)**2)) for v in vals],red)
text(628,83,'x = 1/2, t = 1; a = e⁻⁴',19)
text(799,114,'G = v²',20,blue);text(798,143,'F = (v − a)²',20,red)
text(1040,450,'v')
parts.append(f'<circle cx="{RX(0):.3f}" cy="{RY(a*a):.3f}" r="5" fill="{red}"/>')
line(RX(0)+6,RY(a*a),820,208,red)
text(816,192,'F(0) = e⁻⁸ > 0',19,red)
text(590,548,'G(0) = 0: a nonzero remainder is necessary.',19)
text(35,635,'Proofs: SQD:X1–X3. All formulas and marked values are exact; curves are numerical samples.',19)
parts.append('</svg>');p=root/'figures/semidefinite-division.svg';p.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'svg':'figures/'+p.name,'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'sample_counts':[401,501,501],'ranges':{'left_w':[0,1],'right_v':[-.03,.065]},'source_proof_locators':['SQD:X1','SQD:X2','SQD:X3','SQD:V0'],'actually_inspected':False,'exact_coordinate_review_complete':False}
(root/'figure-check.json').write_text(json.dumps(r,indent=2)+'\n','utf-8');print(json.dumps({'figure_sha256':r['svg_sha256']}))

"""Exact imaginary-phase contours for the flat adjoint model in PSN:X3."""
from pathlib import Path
import math,hashlib,json
from html import escape
MOD=Path(__file__).resolve().parents[1]
def E(s):return math.exp(-1/s**2) if s>0 else 0.0
def H(t):return E(t-1)+E(-t-1)
def G(t):return H(t)-H(t)**2/2
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="555" viewBox="0 0 1100 555"><rect width="1100" height="555" fill="white"/>','<style>text{font-family:Arial,sans-serif;fill:#183146}.title{font-size:21px;font-weight:bold}.label{font-size:18px}.small{font-size:16px}</style>']
def text(x,y,s,cls='label',anchor='start',color=None):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"'+(f' style="fill:{color}"' if color else '')+f'>{escape(s)}</text>')
def path(points,color,width=2.5):
 d=' '.join(('M' if k==0 else 'L')+f'{x:.5f},{y:.5f}' for k,(x,y) in enumerate(points))
 parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>')
left,right=75,590;span=440
xx=lambda t,l:l+(t+2)*span/4
yy=lambda g:385-850*g
text(left,32,'Imaginary phase along the center','title');text(left,64,'G(t) = H(t) − H(t)²/2')
parts.append(f'<path d="M {left} 98 V 390 H {left+span}" fill="none" stroke="#81909d"/>')
for v in [0,.1,.2,.3]:text(left-12,yy(v)+5,f'{v:g}','small','end')
path([(xx(-2+k/200,left),yy(G(-2+k/200))) for k in range(801)],'#146d81',3)
path([(xx(-1,left),385),(xx(1,left),385)],'#a33c23',5)
text(xx(0,left),340,'all time derivatives vanish','small','middle')
text(xx(0,left),367,'G = 0 on [−1,1]','small','middle')
text(right,32,'Transverse confinement','title');text(right,64,'G(t) + x²/2 = c')
cy=255;ys=lambda x:cy-290*x
parts.append(f'<path d="M {right} 98 V 390 M {right} {cy} H {right+span}" fill="none" stroke="#81909d"/>')
for x in [-.4,-.2,0,.2,.4]:text(right-10,ys(x)+5,f'{x:g}','small','end')
text(right-20,100,'x','small','end')
for c,col in [(.005,'#bc6e18'),(.02,'#7b54a3'),(.08,'#146d81')]:
 # Solve G(t)=c at the ends analytically; sample only inside the exact contour.
 h=1-math.sqrt(1-2*c);end=1+math.sqrt(-1/math.log(h))
 for sign in [-1,1]:
  pts=[]
  for k in range(801):
   t=-end+2*end*k/800;x=sign*math.sqrt(max(0,2*(c-G(t))))
   pts.append((xx(t,right),ys(x)))
  path(pts,col)
path([(xx(-1,right),cy),(xx(1,right),cy)],'#a33c23',5)
for base in [left,right]:
 for t in [-2,-1,0,1,2]:text(xx(t,base),420,str(t),'small','middle')
 text(base+span+8,421,'t','small')
text(left,456,'Zero segment: t ∈ [−1,1], x = 0','label')
for j,(c,col) in enumerate([(.005,'#bc6e18'),(.02,'#7b54a3'),(.08,'#146d81')]):text(right+j*150,456,f'c = {c:g}','small',color=col)
text(550,496,'The real center covector is η(t) = 1 − H(t) > 0 on −2 < t < 2.','label','middle')
text(550,532,'Exact functions and proof: X1, X3 and V0. Curves are numerical samples, not proof.','small','middle')
parts.append('</svg>');p=MOD/'figures/flat-adjoint-phase-and-confinement.svg';p.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(MOD/'figure-check.json').write_text(json.dumps({'svg':'figures/'+p.name,'svg_sha256':sha(p),'generator_sha256':sha(Path(__file__)),'exact_functions':'H(t)=E(t-1)+E(-t-1), E(s)=exp(-1/s^2) for s>0, else 0; G=H-H^2/2; contours G+x^2/2=c.','domain':[-2,2],'contour_levels':[.005,.02,.08],'sampling':{'samples_per_curve':801,'contour_endpoints':'±(1+sqrt(-1/log(1-sqrt(1-2*c))))'},'coordinates':{'left_x':[75,515],'right_x':[590,1030],'center_phase_zero_y':385,'center_phase_value_scale':850,'transverse_zero_y':255,'transverse_scale':290},'proof_locators':['PSN:X1','PSN:X3','PSN:V0'],'finite_samples_are_not_proof':True,'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'},indent=2)+'\n','utf-8')
print(json.dumps({'svg_sha256':sha(p),'samples_per_curve':801}))

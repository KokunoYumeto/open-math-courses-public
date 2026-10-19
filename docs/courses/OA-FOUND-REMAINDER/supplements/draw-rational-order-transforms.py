"""Reproduce rational-order-transforms.svg. Original illustration, CC0.

Mathematics: Monotone approximation and semicontinuous operators,
Lemmas 1.1 and 1.2. Author: GPT-6 Astra (OpenAI).
"""
from pathlib import Path
from html import escape

out = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="650" viewBox="0 0 1000 650" role="img" aria-labelledby="title desc">',
       '<title id="title">Rational order transforms and an eventual spectral bound</title>',
       '<desc id="desc">On the plotted interval minus 0.4 to 3, f2 is below f1, and both are below the identity. The common full domain is t greater than minus one half. An increasing open cover of the compact quasi-state space has a single covering member, which gives a uniform spectral lower bound on a tail of the operator net.</desc>',
       '<rect width="1000" height="650" fill="#fff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#22313b}.small{font-size:17px}.label{font-size:21px}.title{font-size:25px;font-weight:bold}</style>']

def text(x, y, value, cls='small', **attrs):
    extra=' '.join(f'{k.replace("_","-")}="{v}"' for k,v in attrs.items())
    out.append(f'<text x="{x}" y="{y}" class="{cls}" {extra}>{escape(value)}</text>')

def line(x1,y1,x2,y2,color='#cbd5dc',width=1,extra=''):
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>')

text(45,40,'Rational order transforms', 'title')
text(45,70,'fα(t) = t / (1 + αt)     •     common domain for α = 1, 2:  t > −1/2')
x0,y0,w,h=85,100,650,300
xmin,xmax,ymin,ymax=-0.4,3,-2.2,3.2
X=lambda t:x0+(t-xmin)*w/(xmax-xmin)
Y=lambda t:y0+h-(t-ymin)*h/(ymax-ymin)
for v in (-2,-1,0,1,2,3):
    line(x0,Y(v),x0+w,Y(v));text(x0-28,Y(v)+6,str(v))
for v in (0,1,2,3):
    line(X(v),y0,X(v),y0+h);text(X(v)-5,y0+h+25,str(v))
line(x0,Y(0),x0+w+10,Y(0),'#43515c',1.5)
line(X(0),y0,X(0),y0+h,'#43515c',1.5)
text(x0+w+17,Y(0)+7,'t','label')
for alpha,color,label in ((0,'#687783','t'),(1,'#167687','f₁(t)'),(2,'#b84f22','f₂(t)')):
    pts=[]
    for j in range(501):
        t=xmin+(xmax-xmin)*j/500
        pts.append(f'{X(t):.3f},{Y(t/(1+alpha*t)):.3f}')
    out.append(f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{" ".join(pts)}"/>')
    yy=135+alpha*55
    line(790,yy,840,yy,color,3);text(855,yy+7,label,'label')
text(790,325,'f₂ ≤ f₁ ≤ t','label')
text(790,355,'Lemma 1.1')
text(85,447,'The common spectral domain on a tail', 'title')
text(85,479,'−1/α < c < min{0, m}     and     x ≥ m1     (Lemma 1.2)')
boxes=[(45,300,['Q(A) compact','Vᵢ = {φ : φ(aᵢ) > c}','increasing open cover']),
       (375,270,['Finite subcover','Directedness gives j','Vⱼ = Q(A)']),
       (675,280,['State detection of order','aᵢ ≥ aⱼ ≥ c1  for i ≥ j','fα(aᵢ) ↑ fα(x) in A'])]
for x,width,labels in boxes:
    out.append(f'<rect x="{x}" y="505" width="{width}" height="115" rx="9" fill="#eff5f7" stroke="#95b5c0"/>')
    for k,label in enumerate(labels):text(x+15,535+29*k,label)
for x in (350,650):
    line(x,562,x+19,562,'#43515c',2)
    out.append(f'<path d="M{x+14} 557 l5 5 -5 5" fill="none" stroke="#43515c" stroke-width="2"/>')
out.append('</svg>')
Path(__file__).with_name('rational-order-transforms.svg').write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n')

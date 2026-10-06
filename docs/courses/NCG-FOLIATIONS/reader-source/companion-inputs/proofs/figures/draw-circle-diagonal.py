"""Original circle diagonal in its product torus. Pillow; CC0-1.0.
Written by GPT-6.1 Sol (OpenAI), at Ultra.
Coordinates are periods in R/Z. Opposite square sides are identified.
The tangent and normal arrows are exactly one fifth of (1,1) and (-1,1).
Proof: Manifold duality, the diagonal and Wu classes, (4.2), Theorem4.1,
and Exercise6.4. This depicts S1 in S1xS1, not a higher-dimensional diagonal.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import math,json,hashlib,html
OUT=Path(__file__).resolve().parent
W,H=940,1040;BG='#f7f7ef';INK='#203d3b';BLUE='#147fa6';GREEN='#237044';ORANGE='#b55920';GREY='#8b9692'
im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<title>The circle diagonal in the product torus</title>','<desc>A unit square with opposite sides identified. Its diagonal represents theta1 equals theta2 modulo one. Tangent and normal arrows are one fifth of (1,1) and (-1,1). All four vertices represent the same diagonal point. The positive dual class is a2 minus a1.</desc>',f'<rect width="{W}" height="{H}" fill="{BG}"/>']
def font(n):return ImageFont.truetype('C:/Windows/Fonts/arial.ttf',n)
def text(x,y,s,n=30,color=INK):
 d.text((x,y),s,font=font(n),fill=color)
 svg.append(f'<text x="{x}" y="{y+n}" font-family="Arial, sans-serif" font-size="{n}" fill="{color}">{html.escape(s)}</text>')
def line(a,b,color=INK,width=3):
 d.line((*a,*b),fill=color,width=width)
 svg.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="{width}"/>')
def arrow(a,b,color,width=6):
 line(a,b,color,width);v=(b[0]-a[0],b[1]-a[1]);q=math.hypot(*v);v=(v[0]/q,v[1]/q)
 back=(b[0]-18*v[0],b[1]-18*v[1]);p=[b,(back[0]-8*v[1],back[1]+8*v[0]),(back[0]+8*v[1],back[1]-8*v[0])]
 d.polygon(p,fill=color)
 svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in p)+f'" fill="{color}"/>')
def point(a,color):
 x,y=a;d.ellipse((x-7,y-7,x+7,y+7),fill=color)
 svg.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>')
def xy(x,y):return (150+640*x,820-640*y)
text(38,24,'The circle diagonal in S¹ × S¹',42)
text(38,86,'Unit periods; identify each pair of opposite sides.',30)
for a,b in [((0,0),(1,0)),((1,0),(1,1)),((1,1),(0,1)),((0,1),(0,0))]:line(xy(*a),xy(*b),GREY,4)
for y in (0,1):arrow(xy(.13,y),xy(.28,y),GREY,4)
for x in (0,1):arrow(xy(x,.13),xy(x,.28),GREY,4)
line(xy(0,0),xy(1,1),BLUE,7)
for p in [(0,0),(1,0),(0,1),(1,1)]:point(xy(*p),BLUE)
arrow(xy(.5,.5),xy(.7,.7),GREEN,7)
arrow(xy(.5,.5),xy(.3,.7),ORANGE,7)
text(622,380,'tangent (1, 1)',30,GREEN)
text(170,300,'normal (−1, 1)',30,ORANGE)
text(488,655,'θ1 = θ2 mod 1',30,BLUE)
text(440,834,'θ1',34);text(97,478,'θ2',34)
text(121,826,'0',28);text(789,826,'1',28);text(114,158,'1',28)
text(38,900,'All four corners are one point in the quotient.',30)
text(38,949,'Dual class: U = a2 − a1.   On the diagonal: Δ*U = 0.',30)
text(38,994,'Arrow scale 1/5; det[tangent, normal] = 2 > 0.',27)
svg.append('</svg>')
im.save(OUT/'circle-diagonal.png',optimize=True)
(OUT/'circle-diagonal.svg').write_text('\n'.join(svg),encoding='utf-8')
data={'space':'(R/Z)^2','square':[0,1],'diagonal':'theta1=theta2 modulo1','vertex_identification':'all four vertices are the same diagonal point','arrow_base':[.5,.5],'arrow_scale':'1/5','tangent':[1,1],'normal':[-1,1],'orientation_determinant':2,'positive_dual_class':'a2-a1','diagonal_pullback':0,'proof_locus':'Section4 equation4.2, Theorem4.1 and Exercise6.4','dimensions':[W,H]}
(OUT/'circle-diagonal-data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
print('ORIGINAL_CIRCLE_DIAGONAL',W,H,hashlib.sha256((OUT/'circle-diagonal.png').read_bytes()).hexdigest())

from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import html
own=Path(__file__).resolve().parent
W,H=1800,1510
im=Image.new('RGB',(W,H),'#f7f8fb');d=ImageDraw.Draw(im)
fontdir=Path('C:/Windows/Fonts')
def font(n,bold=False):
    return ImageFont.truetype(str(fontdir/('arialbd.ttf' if bold else 'arial.ttf')),n)
svg=[]
def text(x,y,s,n=29,color='#17243b',bold=False):
    d.text((x,y),s,font=font(n,bold),fill=color)
    svg.append(f'<text x="{x}" y="{y+n}" fill="{color}" font-family="Arial" font-size="{n}" font-weight="{700 if bold else 400}">{html.escape(s)}</text>')
def box(x,y,w,h,fill,outline='#a8b5ca'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline=outline,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{outline}" stroke-width="3"/>')
def arrow(x1,y1,x2,y2,color='#3f658d'):
    d.line((x1,y1,x2,y2),fill=color,width=5)
    if x2>x1: pts=[(x2,y2),(x2-17,y2-10),(x2-17,y2+10)]
    else: pts=[(x2,y2),(x2-10,y2-17),(x2+10,y2-17)]
    d.polygon(pts,fill=color)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="5"/><polygon points="{" ".join(str(x)+","+str(y) for x,y in pts)}" fill="{color}"/>')

text(65,38,'Probability normalization does not force a zero RN character',45,bold=True)
text(65,101,'Exact amenable H action on K = F2((t)); beta_g F(x) = F(g^-1 x)',29)
box(65,161,1670,222,'#e8f0fc')
text(95,184,'Explicit faithful probability  [NZ.2–NZ.4]',33,bold=True)
text(95,235,'dmu = (2/3) f dm;  m(O) = 1;  f = 1 on O,  f = |x|^-2 outside O',30)
text(95,286,'mu(O) = 2/3;   mu(K \\ O) = 1/3;   integral f dm = 3/2',30)
text(95,334,'T: x -> t^-1 x expands the norm by 2.  az: x -> x+1 preserves this probability.',28)
box(65,419,793,257,'#edf7ef','#8bb799')
text(94,442,'Normal RN derivative  [NZ.8–NZ.9]',32,bold=True)
text(94,494,'D_T = 1/2 on O;  D_T = 2 outside O',30)
text(94,549,'mu(D_T) = (1/2)(2/3) + 2(1/3) = 1',28)
text(94,603,'All fixed-word derivatives are boundedly invertible.',25)
box(920,419,815,257,'#fff1e7','#c8a17f')
text(950,442,'Every invariant state  [NZ.10–NZ.11]',32,bold=True)
text(950,494,'omega(1_B_N) = 0 for every compact ball B_N',27)
text(950,549,'omega(log D_T) = log 2 > 0',34,bold=True)
text(950,603,'Three actual translation labels: total = 3 log 2.',27)
arrow(858,546,920,546)
text(70,715,'Compact-ball inclusions and disjoint translations  [NZ.10]',31,bold=True)
for x,label in ((90,'O'),(385,'B_1 = t^-1 O'),(680,'B_2 = t^-2 O')):
    box(x,773,257,72,'#ffffff')
    text(x+18,787,label,29)
arrow(347,809,385,809);arrow(642,809,680,809)
text(999,780,'Haar volumes: 1, 2, 4, ...',29)
text(999,822,'Inclusions only; no metric scale encoded.',24)
text(95,880,'For each N, arbitrarily many disjoint b+B_N exist with b in F2[t,t^-1].',28)
text(95,925,'Finite additivity: r omega(1_B_N) <= 1 for every r; therefore omega(1_B_N) = 0.',28)

box(65,1001,1670,339,'#f0edf9','#b4a4cb')
text(94,1026,'Separate fixed weighted center Z(W)  [NZ.6]',34,bold=True)
text(94,1084,'Actual plane-parity lamps give X = sum_r b_r t^-r, normally in K.',29)
text(94,1134,'Full original derivative D_g',29)
text(978,1134,'Affine factor derivative Dbar_g',29)
arrow(531,1155,931,1155,'#755a9d')
text(563,1179,'normal E_muU(. | X)',25,color='#755a9d')
text(94,1232,'Invariant states also escape all compact X-balls.  The two normal laws remain distinct.',27)
text(94,1282,'log Dbar_g is not asserted equal to E(log D_g | X); singular means need not commute with E.',26)
text(65,1391,'The explicit action disproves the general forcing principle; it is not the fixed subfactor model.',29,bold=True)
text(65,1444,'The original zero-translation endpoint still requires a proof on full Z(W), with its two trace identities.',27)
im.save(own/'normalization-obstruction-v17.png')
(own/'normalization-obstruction-v17.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#f7f8fb"/>'+''.join(svg)+'</svg>',encoding='utf-8')
print(f'rendered {W}x{H}')

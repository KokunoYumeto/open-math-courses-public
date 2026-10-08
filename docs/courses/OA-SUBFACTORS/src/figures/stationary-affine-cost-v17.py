"""Exact region and likelihood diagram for AC.3–AC.18."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import html
own=Path(__file__).resolve().parent;W,H=1700,1160
im=Image.new('RGB',(W,H),'#f7f8fb');draw=ImageDraw.Draw(im);svg=[]
def text(x,y,s,n=29,bold=False,color='#17243b'):
 f=ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),n)
 draw.text((x,y),s,font=f,fill=color)
 svg.append(f'<text x="{x}" y="{y+n}" fill="{color}" font-family="Arial" font-size="{n}" font-weight="{700 if bold else 400}">{html.escape(s)}</text>')
def box(x,y,w,h,fill):
 draw.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline='#a8b5ca',width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="#a8b5ca" stroke-width="3"/>')
text(65,38,'Two stationary probabilities do not force zero likelihood cost',40,True)
text(65,100,'K = F2((t));  |t| = 1/2;  a(x) = x+1;  T(x) = tx;  beta_g f(x) = f(g^-1 x)',27)
box(65,157,1570,203,'#e8f0fc')
text(95,180,'Exact probability equations  [AC.3–AC.8]',31,True)
text(95,233,'mu_V = (1/4) mu_U + (1/4) a_*mu_U + (1/2) T_*mu_U',30)
text(95,285,'mu_U = (2/5) mu_V + (2/5) a_*mu_V + (1/5) T^-1_*mu_V',30)
text(80,407,'Region',28,True);text(480,407,'mu_U mass',28,True);text(755,407,'mu_V mass',28,True)
text(1025,407,'(R0, R1, R2)',28,True);text(1430,407,'D_T',28,True)
rows=[
 (474,'|x| <= 1/2','3/7','9/14','(1/6, 1/6, 2/3)','2','#edf7ef'),
 (574,'|x| = 1','3/7','15/56','(2/5, 2/5, 1/5)','1/4','#fff1e7'),
 (674,'|x| > 1','1/7','5/56','(2/5, 2/5, 1/5)','1/4','#fff1e7')]
for y,region,u,v,r,d,fill in rows:
 box(65,y,1570,80,fill)
 for x,s in [(95,region),(480,u),(755,v),(1025,r),(1430,d)]:text(x,y+19,s,28)
box(65,800,1570,223,'#f0edf9')
text(95,823,'Every invariant state  [AC.12–AC.18]',31,True)
text(95,875,'omega(1_O) = 0: arbitrarily many disjoint Laurent-polynomial translates of O.',28)
text(95,924,'omega(log D_T) = -log 4;   sum_i omega(Ri^-1) = 10',30)
text(95,974,'Reciprocal cost = |5/2-4| + |5/2-4| + |5-2| = 6',30,True)
text(65,1070,'Exact measurable action; no ordinary-core identification or subfactor counterexample asserted.',27,True)
im.save(own/'stationary-affine-cost-v17.png')
(own/'stationary-affine-cost-v17.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#f7f8fb"/>'+''.join(svg)+'</svg>',encoding='utf-8')
print(f'rendered {W}x{H}')

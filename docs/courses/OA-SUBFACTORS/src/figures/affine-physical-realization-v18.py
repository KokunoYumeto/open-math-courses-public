"""Accurate schematic of AH.1–AH.20; boxes encode objects, not trace areas."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import html
D=Path(__file__).resolve().parent;W,H=1850,1460
im=Image.new('RGB',(W,H),'#f7f8fb');d=ImageDraw.Draw(im);svg=[]
def text(x,y,s,n=29,bold=False,color='#17243b'):
 f=ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),n)
 d.text((x,y),s,font=f,fill=color)
 svg.append(f'<text x="{x}" y="{y+n}" fill="{color}" font-family="Arial" font-size="{n}" font-weight="{700 if bold else 400}">{html.escape(s)}</text>')
def box(x,y,w,h,fill):
 d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline='#a8b5ca',width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="#a8b5ca" stroke-width="3"/>')
def arrow(x1,y,x2):
 d.line((x1,y,x2,y),fill='#3f658d',width=5);d.polygon([(x2,y),(x2-15,y-10),(x2-15,y+10)],fill='#3f658d')
 svg.append(f'<path d="M{x1},{y} H{x2}" stroke="#3f658d" stroke-width="5"/><polygon points="{x2},{y} {x2-15},{y-10} {x2-15},{y+10}" fill="#3f658d"/>')
text(65,36,'An actual index-ten affine inclusion and its Laurent observable',43,True)
text(65,101,'G = F2[t,t^-1] + semidirect Z;  s0 = 1, s1(x) = x+1, s2(x) = tx;  |t| = 1/2',28)
box(65,163,820,275,'#e8f0fc');box(965,163,820,275,'#edf7ef')
text(95,185,'Stable expected Jones triple  [AH.4–AH.6]',30,True)
text(95,240,'phi_+ phi_-(P)  subset  phi_+(P)  subset  P',29)
text(95,291,'p_+ = |sqrt(2/5)00 + sqrt(2/5)11',29)
text(95,334,'                  + sqrt(1/5)22><same|',29)
text(95,386,'E_+(p_+) = 1/10; full cup corner and spanning.',28)
arrow(885,303,965)
text(995,185,'Common finite compression  [AH.7–AH.9]',30,True)
text(995,240,'h1 = phi_+(e), Tr(e) = 1, Tr(h1) = 4/3',29)
text(995,291,'N = h1 L1 h1  subset  M = h1 P h1',29)
text(995,342,'II1 factors; [M:N] = 10; cup trace = 1/10',29)
text(995,392,'Coherent finite stages retain every marked cup.',28)
box(65,481,1720,260,'#fff1e7')
text(95,504,'Full finite relative commutants and both inherited traces  [AH.10–AH.11]',32,True)
text(95,561,'Endpoint blocks: E_IJ occurs exactly when g(I) = g(J) in the actual group G.',29)
text(95,613,'Even words, length 2m:  tau(q_I) = 2^n(g)/10^m;  rho(q_I) = 2^-n(g)/10^m',29)
text(95,665,'First branch weights: (1/4,1/4,1/2);  dual weights: (2/5,2/5,1/5); kC = (8/5,8/5,2/5)',28)
box(65,782,1720,258,'#f0edf9')
text(95,805,'Every smooth representation and the actual normal observable  [AH.12–AH.20]',31,True)
text(95,862,'Actual right Folner sets give F: represented V -> M, UCP, F|M = id, E_N F = F E.',28)
text(95,914,'Pair height drift = 3/10 > 0;  X = limit b_k lies in K = F2((t)).',30)
text(95,966,'Start plus law = mu_V; start minus law = mu_U.  Distinct x, x+1, tx recover p0,p1,p2.',28)
box(65,1083,1720,210,'#ffffff')
text(95,1106,'Full normal center isomorphisms, with separate laws  [AH.18, AB.31]',31,True)
text(95,1163,'j_U: L-infinity(K,mu_U) -> Z(S)          j_V: L-infinity(K,mu_V) -> Z(R)',30)
text(95,1218,'Full joint center: Z(S) join Z(R) = direct sum_i p_i Z(S).',30)
text(65,1334,'Every compatible physical central state has joint discrepancy 3/5 and reciprocal cost 6.  [AO.3]',29,True)
text(65,1390,'All maps and constants are exact; layout is schematic and encodes no metric lengths or trace areas.',27)
im.save(D/'affine-physical-realization-v18.png')
(D/'affine-physical-realization-v18.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#f7f8fb"/>'+''.join(svg)+'</svg>',encoding='utf-8')
print(f'rendered {W}x{H}')

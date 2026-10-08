"""Reproducible exact finite-pole and natural-comparison diagram."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
from matplotlib.font_manager import FontProperties, findfont

ROOT = Path(__file__).resolve().parent
S = 2
im = Image.new("RGB", (1630*S, 1000*S), "#f4f8fb")
d = ImageDraw.Draw(im)
def text(x, y, label, size=25, bold=False):
    face = findfont(FontProperties(family="DejaVu Sans",weight="bold" if bold else "normal"))
    if y<100 or y>780: bound=1548-x
    elif x<700: bound=650-x
    elif 790<=x<1100: bound=1100-x
    elif x>=1230: bound=1545-x
    else: bound=1560-x
    font=ImageFont.truetype(face,size*S)
    while d.textlength(label,font=font)>bound*S and size>15:
        size-=1
        font=ImageFont.truetype(face,size*S)
    d.text((x*S,y*S),label,font=font,fill="#163347")
def box(x1,y1,x2,y2,color="#ffffff",stroke="#8aa0ad"):
    d.rounded_rectangle((x1*S,y1*S,x2*S,y2*S), radius=14*S,
                        fill=color, outline=stroke, width=2*S)
def arrow(x1,y1,x2,y2,color="#237a9b"):
    d.line((x1*S,y1*S,x2*S,y2*S), fill=color, width=3*S)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2*S,y2*S)]
    for delta in [-0.5,0.5]:
        pts.append(((x2-13*math.cos(a+delta))*S,
                    (y2-13*math.sin(a+delta))*S))
    d.polygon(pts, fill=color)

text(44,28,"Algebraic de Rham comparison: finite poles, actual periods, and global descent",32,True)
text(44,80,"All smooth separated finite-type complex varieties; the coefficient connection is d.",25)
box(35,134,695,755)
box(727,134,1591,755)
text(62,161,"Finite added-pole layers",29,True)
text(62,211,"F_N = product(z_j^(-N_j)) Omega(log D)",23)
box(85,280,620,360,"#e7eff7")
text(112,301,"F_(N-e_i)  included in  F_N;  N_i=n>0",25)
arrow(353,374,353,416)
text(380,385,"quotient on D_i",22)
box(85,432,620,517,"#f3eafb")
text(113,451,"Lie_(z_i partial_i) = -n on the quotient",23)
text(113,484,"Other pole exponents stay fixed.",22)
arrow(353,530,353,568)
box(85,582,620,678,"#e5f4eb")
text(113,601,"h = -iota_i / n",28,True)
text(113,642,"d h + h d = 1: the layer is contractible.",23)
text(63,705,"Finite induction, then exact filtered union.",23)

text(758,161,"The natural proper-pair comparison",29,True)
box(777,253,1108,356,"#e7eff7")
box(1220,253,1550,356,"#e7eff7")
text(795,276,"R Gamma(P, Omega_alg",23)
text(795,314,"                    (log D))",23)
text(1237,276,"R Gamma(P^an, Omega_an",22)
text(1237,314,"                         (log D))",22)
arrow(1121,301,1208,301)
text(1113,228,"GAGA",20,True)
text(755,395,"finite pole layers",20)
text(755,426,"affine j",20)
text(1160,395,"SNC periods",20)
text(1160,426,"factor (2pi i)^p",20)
arrow(947,369,947,485)
arrow(1384,369,1384,485)
box(777,500,1108,601,"#e5f4eb")
box(1220,500,1550,601,"#e5f4eb")
text(795,525,"R Gamma(U, Omega_alg)",23)
text(1237,525,"R Gamma(U^an, C)",23)
arrow(1121,551,1208,551)
text(1115,607,"gamma_U",20,True)
text(758,652,"All four arrows are the proved natural maps.",23)
text(758,692,"Their square commutes before cohomology.",23)

box(35,787,1591,955)
text(63,810,"Arbitrary X: choose a finite affine cover and its affine intersections U_I.",26,True)
text(63,855,"Each U_I has a smooth projective SNC compactification; its natural comparison is proved above.",24)
text(63,897,"Finite Cech descent gives gamma_X, including nonproper and nonquasiprojective X.",25)
text(63,927,"Exact proof locators: (5.3d)-(5.3f), natural square (5.3x), finite descent (5.3y)-(5.3aa).",18)
im.save(ROOT/"grothendieck-comparison.png")
print(str(ROOT/"grothendieck-comparison.png"))

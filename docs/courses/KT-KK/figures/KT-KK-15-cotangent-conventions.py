from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
base=Path(__file__).resolve().parent
im=Image.new("RGB",(1280,820),"#ffffff");d=ImageDraw.Draw(im)
fontfile="C:/Windows/Fonts/segoeui.ttf"
def font(n):return ImageFont.truetype(fontfile,n)
def txt(x,y,t,n=24,c="#15364a"):d.text((x,y),t,font=font(n),fill=c)
def arrow(a,b,c="#15364a",width=4):
    d.line((a,b),fill=c,width=width)
    v=(b[0]-a[0],b[1]-a[1]);l=math.hypot(*v);v=(v[0]/l,v[1]/l)
    p=(-v[1],v[0]);s=13
    d.polygon([b,(b[0]-s*v[0]+s*.48*p[0],b[1]-s*v[1]+s*.48*p[1]),(b[0]-s*v[0]-s*.48*p[0],b[1]-s*v[1]-s*.48*p[1])],fill=c)
txt(45,25,"Cotangent conventions and the Gaussian inverse",35)
for left,title,sgn,color in ((45,"J+ : complex x + iξ",1,"#296a96"),(660,"J− : complex x − iξ",-1,"#a44734")):
    d.rounded_rectangle((left,95,left+575,410),radius=16,fill="#f4f8fb",outline="#cbdbe5",width=2)
    txt(left+25,115,title,28,color)
    ox,oy=left+200,270
    arrow((ox-105,oy),(ox+140,oy))
    arrow((ox,oy+100),(ox,oy-95))
    txt(ox+109,oy+8,"x",23);txt(ox+10,oy-118,"ξ",23)
    arrow((ox,oy),(ox+88,oy),color)
    arrow((ox,oy),(ox,oy-sgn*78),color)
    txt(left+340,195,"J(ex) = "+("eξ" if sgn==1 else "−eξ"),25,color)
    txt(left+340,245,"σ(dx) = f",24)
    txt(left+340,288,"σ(dξ) = "+("−c" if sgn==1 else "c"),24)
    txt(left+25,365,"f = i(ε − ι),   c = ε + ι       [CI.14, CI.28]",21)
d.rounded_rectangle((45,440,1235,710),radius=16,fill="#f5faf6",outline="#cbded0",width=2)
txt(70,455,"All ranks: the inverse keeps its grading and its source action",27,"#245d39")
txt(95,520,"Cl(T*M)",26);txt(560,520,"C₀(T*M)",26);txt(1090,520,"C",26)
arrow((255,541),(525,541),"#245d39");txt(335,503,"xV",24,"#245d39")
arrow((525,566),(255,566),"#245d39");txt(335,573,"yV",24,"#245d39")
arrow((750,541),(1050,541),"#245d39");txt(785,503,"Dolbeault J−",24,"#245d39")
arrow((255,625),(1050,625),"#245d39");txt(440,635,"xV · Dolbeault J− = Clifford Dirac    [CI.29]",23,"#245d39")
txt(70,745,"Rank 1 Gaussian: w = (1 tensor 1 + i e₁ tensor e₁)/√2; even, f₁w = w e₁.  [CI.24–25]",23)
txt(70,782,"General correction: Dolbeault J− = (−1)ⁿ · det(TM_C) · Dolbeault J+.  [CI.32]",23)
im.save(base/"KT-KK-15-cotangent-conventions.png")

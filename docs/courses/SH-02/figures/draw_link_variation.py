"""Independently authored CC0-1.0 diagram of CV18--CV23. No topology of a
general complex-analytic link is inferred from this disk calibration."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

OUT = (Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == "figures" else Path(__file__).resolve().parent)
img = Image.new('RGB', (1440, 880), '#ffffff')
d = ImageDraw.Draw(img)

def font(size, bold=False):
    name = 'segoeuib.ttf' if bold else 'segoeui.ttf'
    return ImageFont.truetype(name, size)
f30, f25, f22, f18 = font(30, True), font(25), font(22), font(18)
ink, blue, orange, green, gray = '#172334', '#1262a5', '#b34a16', '#11654b', '#5b6370'
def text(x, y, s, ft=f22, fill=ink):
    d.text((x, y), s, font=ft, fill=fill)
def arrow(a, b, color=ink, width=4):
    d.line((a,b), fill=color, width=width)
    dx,dy=b[0]-a[0],b[1]-a[1]
    n=math.hypot(dx,dy); dx/=n; dy/=n
    d.polygon([b,(b[0]-15*dx+7*dy,b[1]-15*dy-7*dx),
                 (b[0]-15*dx-7*dy,b[1]-15*dy+7*dx)], fill=color)

text(55, 35, 'CL-VAR: actual localization and the disk sign', f30)
text(55, 80, 'Disk calibration g(z)=z; F=j!V; base ray at angle π; T is one positive full turn.', f22)

cx, cy, rr = 315, 320, 165
box=(cx-rr,cy-rr,cx+rr,cy+rr)
d.ellipse(box, outline='#c9ced5', width=3)
d.line((cx-210,cy,cx+235,cy), fill='#d9dde3', width=2)
d.line((cx,cy-205,cx,cy+200), fill='#d9dde3', width=2)
d.arc(box,270,450,fill=blue,width=12)
arrow((cx+rr,cy+50),(cx+rr,cy-30),blue,5)
d.arc((cx-rr+22,cy-rr+22,cx+rr-22,cy+rr-22),180,360,fill=orange,width=5)
arrow((cx+110,cy-92),(cx+126,cy-72),orange,4)
d.arc((cx-rr+39,cy-rr+39,cx+rr-39,cy+rr-39),0,180,fill=green,width=5)
arrow((cx+91,cy+88),(cx+111,cy+62),green,4)
d.ellipse((cx-rr-8,cy-8,cx-rr+8,cy+8),fill=ink)
d.ellipse((cx+rr-8,cy-8,cx+rr+8,cy+8),fill=blue)
text(63,310,'V−',f25)
text(cx+rr+23,310,'V+',f25,blue)
text(240,170,'U',f25,orange)
text(238,440,'UT',f25,green)
text(285,520,'Re(z)>0: positive arc',f22,blue)
text(290,120,'right endpoint',f18)
text(290,485,'left endpoint',f18)

text(675,175,'The interval connecting map',f25)
text(675,225,'right: Uv',f25,orange)
text(675,270,'left: UTv',f25,green)
text(675,330,'right − left = U(1−T)v',f25,blue)
text(675,382,'Chosen upper transport back: U⁻¹',f22)
arrow((870,423),(870,472),blue)
text(675,490,'variation = 1−T : V−[−1] → V−[−1]',f25,blue)

d.line((55,580,1385,580),fill='#d9dde3',width=2)
text(60,610,'Actual support-localization triangle on the original normal slice',f25)
text(100,680,'i₀!F',f30)
arrow((250,705),(365,705))
text(385,680,'N(F)',f30)
arrow((545,705),(685,705),blue)
text(557,652,'var',f22,blue)
text(710,680,'RΓc(L°; F)[−1]',f30)
arrow((1095,705),(1210,705))
text(1230,680,'+1',f25)
text(60,785,'CV18 supplies the point costalk. CV15–CV17 supply the cap map by universal dual pairings.',f22)
text(60,830,'Disk picture only; the proof retains the original Whitney slice, radial ball, and arbitrary bounded weak coefficients.',f18,gray)
img.save(OUT/'link-variation-calibration.png')

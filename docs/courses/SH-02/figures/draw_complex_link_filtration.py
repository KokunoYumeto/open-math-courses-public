from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

W=(Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == "figures" else Path(__file__).resolve().parent)
scale=2
img=Image.new('RGB',(1900*scale,1120*scale),'white')
d=ImageDraw.Draw(img)
font_path='arial.ttf'
def font(n):return ImageFont.truetype(str(font_path),n*scale)
def text(x,y,s,size=27,fill='#13263b'):
 d.multiline_text((x*scale,y*scale),s,font=font(size),fill=fill,spacing=8*scale)
def line(points,fill='#345a7c',width=3):
 d.line([(x*scale,y*scale) for x,y in points],fill=fill,width=width*scale)
def rect(x1,y1,x2,y2,fill,outline='#d2dee9'):
 d.rounded_rectangle((x1*scale,y1*scale,x2*scale,y2*scale),radius=14*scale,fill=fill,outline=outline,width=2*scale)
def arrow(x1,y1,x2,y2,fill='#345a7c'):
 line([(x1,y1),(x2,y2)],fill)
 import math
 a=math.atan2(y2-y1,x2-x1)
 for off in(-.5,.5):line([(x2,y2),(x2-15*math.cos(a+off),y2-15*math.sin(a+off))],fill)

text(55,32,'Complex-link filtrations: selected geometry, original objects',37)
text(55,91,'Coordinate and categorical schematic; no singular space is drawn as a disk.',23,'#536a81')
rect(40,145,620,720,'#f7fafc')
rect(650,145,1260,720,'#f7fafc')
rect(1290,145,1860,720,'#f7fafc')
text(65,168,'1. The entire radial end',29)
text(65,216,'ρ is the flow coordinate; dρ(v) = 1.',23)
line([(155,290),(155,575)],'#234e70',5)
levels=[(290,'ε  (H, the exit face)'),(365,'ε − 2η  (χ = 0 above)'),(445,'ε − 3η  (χ = 1 below)'),(575,'ε − 4η  (inner collar)')]
for y,label in levels:
 line([(140,y),(171,y)],'#234e70',3);text(193,y-17,label,23)
arrow(102,305,102,525,'#087d8b')
text(65,617,'Ordinary: retract the end to a core.\nCompact: RΓ(collar, H; F) = 0.',23)

text(675,168,'2. One common complex slice',29)
text(675,224,'h = (π, g),     dim_C h = d + 1\nt has dimension e = r − d − 1\nn is normal to the original R',25)
text(675,356,'Original R:     n = 0\nSelected Y:    h = h(p)\nInduced T:      h = h(p), n = 0',25)
rect(672,495,1237,603,'#e5f4f1','#7ebeb1')
text(687,514,'N_p:  h = h(p), t = 0\nSame normal space and same F in X and Y.',23)
text(675,635,'E07 → NC → HB/HNC\nLocal quotient = N_R,λ(F)[−τ]',24)

text(1315,168,'3. Joint parameters avoid bad lifts',29)
text(1315,228,'Parameter space: (h-fibre level, a)\nReal dimension 2n',24)
text(1315,328,'Original bad conormals B\nReal dimension at most 2n − 2',24)
arrow(1525,404,1525,476)
text(1315,492,'Θ(p, λ) = (h(p), Re λ|Y − dρ|Y)\nImage has measure zero.',22)
text(1315,600,'Equal-dimensional incidence projection\nselects a tangential Morse Hessian.\nBounded multipliers exclude accumulation.',22)

rect(40,750,1860,1050,'#edf3f8')
text(65,773,'4. Actual restriction maps determine the finite derived filtration',29)
text(65,830,'V_j → V_(j−1),     Q_j = fib(V_j → V_(j−1)),     W_j = fib(V_N → V_j)',27)
text(65,888,'0 = W_N → W_(N−1) → ··· → W_0 = V_N       with quotient Q_j',27)
text(65,960,'Ordinary: τ ≤ e.     Compact support: τ′ = 2e − τ ≥ e.     HNC returns both marked objects to the prescribed link.',24)
text(55,1071,'Exact proof locators: CLF3–CLF4 (selection); CLF5–CLF7 (local map); CLF8 (filtration and exit face).',22,'#536a81')
img.resize((1900,1120),Image.Resampling.LANCZOS).save(W/'complex-link-filtration.png')
print(str(W/'complex-link-filtration.png'))

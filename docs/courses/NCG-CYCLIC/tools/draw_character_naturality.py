"""Exact spectral intervals and the oriented one-simplex prism, for N1–N3."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public/assets/character-naturality-mechanism.png"
im = Image.new("RGB", (3200, 1450), "#f7f9fb")
d = ImageDraw.Draw(im)
font_root = Path("C:/Windows/Fonts")
def font(size, bold=False):
    return ImageFont.truetype(str(font_root / ("segoeuib.ttf" if bold else "seguisym.ttf")), size)
def label(x, y, s, size=34, fill="#18394c", bold=False):
    d.text((x,y), s, font=font(size,bold), fill=fill)
def arrow(a,b,color="#18394c",width=7):
    from math import hypot
    d.line((a,b),fill=color,width=width)
    dx,dy=b[0]-a[0],b[1]-a[1]; n=hypot(dx,dy); ux,uy=dx/n,dy/n
    p=(b[0]-26*ux,b[1]-26*uy)
    d.polygon([b,(p[0]-12*uy,p[1]+12*ux),(p[0]+12*uy,p[1]-12*ux)],fill=color)
label(100,55,"Curvature naturality: smoothing and homotopy",68,bold=True)
label(100,155,"Finite-polyhedron bridge N1–N3 • exact bounds and oriented chains",40)
d.rounded_rectangle((80,255,1515,1320),radius=30,fill="white",outline="#cad7e0",width=3)
d.rounded_rectangle((1575,255,3120,1320),radius=30,fill="white",outline="#cad7e0",width=3)
label(135,300,"N1. Keep the spectral gap open",46,bold=True)
label(135,385,"a = Σ_v t_v p(v),  ‖a − p‖ < ε < 1/4",40)
label(135,445,"Illustrated bound: ε = 1/8",36)
x0,x1=220,1380
def sx(v):return x0+(v+0.25)/1.5*(x1-x0)
y=720
arrow((x0,y),(x1,y))
for v,s in [(-.125,"−1/8"),(0,"0"),(.125,"1/8"),(.5,"1/2"),(.875,"7/8"),(1,"1"),(1.125,"9/8")]:
    x=sx(v);d.line((x,y-17,x,y+17),fill="#18394c",width=4)
    w=d.textbbox((0,0),s,font=font(31))[2];label(x-w/2,y+35,s,31)
for lo,hi,c in [(-.125,.125,"#167e95"),(.875,1.125,"#d17731")]:
    d.rounded_rectangle((sx(lo),y-65,sx(hi),y-32),radius=10,fill=c)
d.line((sx(.5),560,sx(.5),865),fill="#84929c",width=4)
label(620,855,"cutoff",32,fill="#617581")
label(160,545,"0-cluster",34,fill="#167e95")
label(1050,545,"1-cluster",34,fill="#af581a")
label(135,970,"Spec(a) ⊂ [−ε, ε] ∪ [1−ε, 1+ε]",38)
label(135,1040,"Riesz projection q keeps the 1-cluster.",35)
label(135,1100,"Same formula on a common face ⇒ compatible q.",33)
label(135,1170,"Intervals are proved bounds, not sampled eigenvalues.",31)

label(1630,300,"N3. The edge prism has its signs",46,bold=True)
label(1630,385,"P[0,1] = [(0,0),(0,1),(1,1)]",34)
label(1825,435,"− [(0,0),(1,0),(1,1)]",34)
A=(1850,1040);B=(2800,1040);C=(1850,610);D=(2800,610)
d.polygon([A,C,D],fill="#dff1f5")
d.polygon([A,B,D],fill="#f9e8d9")
for a,b in [(A,C),(C,D),(A,B),(B,D)]:arrow(a,b)
d.line((A,D),fill="#7794a5",width=5)
for p,s,offset in [(A,"(0,0)",(-65,20)),(B,"(1,0)",(-55,20)),(C,"(0,1)",(-65,-55)),(D,"(1,1)",(-55,-55))]:
    d.ellipse((p[0]-9,p[1]-9,p[0]+9,p[1]+9),fill="#18394c")
    label(p[0]+offset[0],p[1]+offset[1],s,30)
label(2185,680,"+ triangle",33,fill="#167e95")
label(2385,925,"− triangle",33,fill="#af581a")
label(1640,780,"t ↑",34)
label(2320,1100,"x →",34)
label(1630,1180,"∂P = top − bottom − right + left",36)
im.save(OUT)
receipt={"figure":str(OUT.relative_to(ROOT)).replace("\\","/"),"sha256":hashlib.sha256(OUT.read_bytes()).hexdigest(),"pixels":[3200,1450],"spectral_epsilon":"1/8","spectral_intervals":[["-1/8","1/8"],["7/8","9/8"]],"prism_chain":"[(0,0),(0,1),(1,1)]-[(0,0),(1,0),(1,1)]","orientation":"interval first; dt wedge dx","scope":"Exact bounds and oriented chains of N1/N3, not measured eigenvalues."}
(ROOT/"public/assets/character-naturality-figure-receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt))

"""Reproduce the original mathematical figure for Example 6.4 (CC0).

Requires Python and Pillow. Samples are finite exponential sums, not an
approximation asserted to equal the full boundary-divergent series.
"""
from pathlib import Path
from os import environ
from fractions import Fraction
from math import factorial, exp, log
from PIL import Image, ImageDraw, ImageFont

root=Path(__file__).resolve().parents[1]
dest=root/'figures/coefficient-algebra-boundary.png'
dest.parent.mkdir(exist_ok=True)
font_path=Path(environ.get('NCGLI_FIGURE_FONT') or
 (Path(environ.get('WINDIR', ''))/'Fonts'/'segoeui.ttf'))
if not font_path.exists():
 font_path=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
if not font_path.exists():
 raise RuntimeError('Install or select an ordinary sans-serif font to reproduce this plot.')
def font(n): return ImageFont.truetype(str(font_path),n)
im=Image.new('RGB',(1100,1180),'white');d=ImageDraw.Draw(im)
ink='#172a3a';blue='#075f9d';orange='#b64b13';green='#087453';light='#e3e8ec'
def text(x,y,s,size=28,fill=ink): d.text((x,y),s,font=font(size),fill=fill)
text(45,25,'Differential coefficients can hide a boundary',36)
text(45,80,'Example 6.4:  zeta_b(z) = -2 sum over k >= 1 of 2^(-k! z)',27)
text(45,135,'1. Proved nonremovable singularities',31)
text(45,181,'Shown subset: q = a/b, |q| <= 1, b <= 6.',25)
text(45,218,'The full set q in Q is dense.',25)
axisx=755;top=160;bottom=485
def qy(q):return top+(1-float(q))*(bottom-top)/2
d.line((axisx,top,axisx,bottom),fill=ink,width=3)
for q,label in [(Fraction(-1),'-1'),(Fraction(-1,2),'-1/2'),(Fraction(0),'0'),(Fraction(1,2),'1/2'),(Fraction(1),'1')]:
 y=qy(q);d.line((axisx-10,y,axisx+10,y),fill=ink,width=2);text(axisx+24,y-18,label,25)
qs=sorted({Fraction(a,b) for b in range(1,7) for a in range(-b,b+1)})
for q in qs:
 y=qy(q);d.ellipse((axisx-4,y-4,axisx+4,y+4),fill=blue)
selected=qy(Fraction(1,3))
d.ellipse((axisx-9,selected-9,axisx+9,selected+9),outline=orange,width=3)
d.line((455,320,axisx-14,selected),fill=orange,width=3)
text(65,290,'q = 1/3',28,orange)
text(65,332,'For k >= 3:  q k! is an integer.',25)
text(65,373,'On z = x + 2 pi i q / log 2,',25)
text(65,414,'every tail term has phase one.',25)
text(825,318,'Re(z) = 0',25)
text(635,500,'q = Im(z) log(2) / (2 pi)',25)
text(45,552,'2. Arbitrarily long positive tails',31)
text(45,600,'T_N(x) = sum from k = 3 to N of exp(-x k! log 2)',27)
x0,y0,x1,y1=120,680,1020,970
def px(lx):return x0+(lx+9)/9*(x1-x0)
def py(y):return y1-y/7*(y1-y0)
for y in range(8):
 yy=py(y);d.line((x0,yy,x1,yy),fill=light,width=1);text(65,yy-16,str(y),23)
for lx in [-9,-6,-3,0]:
 xx=px(lx);d.line((xx,y0,xx,y1),fill=light,width=1);text(xx-24,y1+12,'10^'+str(lx),23)
d.line((x0,y0,x0,y1,x1,y1),fill=ink,width=3)
for N,col in [(3,blue),(5,orange),(8,green)]:
 points=[]
 for j in range(451):
  lx=-9+9*j/450;x=10**lx
  val=sum(exp(-x*factorial(k)*log(2)) for k in range(3,N+1))
  points.append((px(lx),py(val)))
 d.line(points,fill=col,width=4)
 text(180+(N-3)*145,640,'N = '+str(N),26,col)
text(430,1010,'x = Re(z) > 0  (logarithmic axis)',25)
text(45,1058,'Each finite tail tends to N - 2 as x tends to zero.',26)
text(45,1097,'N is arbitrary; the full tail is unbounded. Plotted curves are finite sums.',24)
text(45,1137,'Proof: Example 6.4. Original figure by GPT-6.1 Sol (OpenAI), Ultra; CC0.',22)
im.save(dest,format='PNG',compress_level=9)
print(dest.name)

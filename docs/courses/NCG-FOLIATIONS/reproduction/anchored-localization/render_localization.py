"""Original exact anchored-localization diagram and finite samples: CC0.

No numeric sample is a substitute for the accompanying analytic proof.
The paired PNG/SVG use the same exact-coordinate drawing instructions.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, base64, html, json, math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument("--output",type=Path,default=ROOT)
args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
FONT=ROOT/"fonts/DejaVuSans.ttf"
NOTICE=(ROOT/"FONT-NOTICE.txt").read_text(encoding="utf-8")
W,H=2600,1990; BLUE="#17638d";RED="#bc4d32";GREEN="#286d49";GRAY="#65737e"
im=Image.new("RGB",(W,H),"#f8fafc");draw=ImageDraw.Draw(im);fonts={}
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Anchored proper-source localization: exact mechanisms and proof chain</title>',
 '<desc>Labelled exact central-parameter and telescope samples, clopen coefficient diagonal, and the whole-base localization theorem.</desc>',
 '<metadata>'+html.escape('Original diagram/generator: CC0.\n'+NOTICE)+'</metadata>',
 '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(FONT.read_bytes()).decode()+')}text{font-family:LocalSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']
def text(x,y,s,size=30,color="#17283c"):
    if size not in fonts:fonts[size]=ImageFont.truetype(str(FONT),size,layout_engine=ImageFont.Layout.BASIC)
    draw.text((x,y),s,font=fonts[size],fill=color,anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def line(x,y,xx,yy,color=GRAY,width=3):
    draw.line((x,y,xx,yy),fill=color,width=width)
    svg.append(f'<path d="M{x:.4f},{y:.4f}L{xx:.4f},{yy:.4f}" stroke="{color}" stroke-width="{width}" fill="none"/>')
def box(x,y,w,h,fill="white",border="#c9d5e3"):
    draw.rectangle((x,y,x+w,y+h),fill=fill,outline=border,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{border}" stroke-width="3"/>')
def arrow(x,y,xx,yy):
    line(x,y,xx,yy,BLUE,4);a=math.atan2(yy-y,xx-x)
    pts=[(xx,yy)]+[(xx-18*math.cos(a+b),yy-18*math.sin(a+b)) for b in [-.45,.45]]
    draw.polygon(pts,fill=BLUE)
    svg.append('<polygon points="'+' '.join(f'{a:.4f},{b:.4f}' for a,b in pts)+f'" fill="{BLUE}"/>')
def axes(x,y,w,h,xticks,yticks,xmax,ymax):
    line(x,y,x,y+h);line(x,y+h,x+w,y+h)
    for t in xticks:
        xx=x+w*t/xmax;line(xx,y,xx,y+h,"#e0e6ea",2);text(xx-14,y+h+15,f"{t:g}",25)
    for v in yticks:
        yy=y+h-h*v/ymax;line(x,yy,x+w,yy,"#e0e6ea",2);text(x-70,yy-14,f"{v:g}",25)
def poly(points,color):
    for (x,y),(xx,yy) in zip(points,points[1:]):line(x,y,xx,yy,color,5)

text(55,35,"Anchored proper-source localization: explicit mechanisms and proof chain",46)
text(55,100,"G is Hausdorff, second-countable, LCH étale. Original anchor R = C₀(T); original E₁ and Q throughout.",29)
for x,y in [(55,160),(1330,160),(55,1070),(1330,1070)]:box(x,y,1215,850)

text(85,188,"1  Open Mayer–Vietoris homotopy  ·  MV.1–MV.6",32)
text(85,241,"Hᵤ(f)(t) = f((1−u)t + uφI)    [exact sample φI = 1/4]",29)
x,y,w,h=145,315,1020,410
axes(x,y,w,h,[0,.25,.5,.75,1],[0,.25,.5,.75,1],1,1)
for u,color in [(0,GRAY),(.5,BLUE),(1,RED)]:
    poly([(x+w*t/200,y+h-h*((1-u)*t/200+u/4)) for t in range(201)],color)
for idx,(u,col) in enumerate([("0",GRAY),("1/2",BLUE),("1",RED)]):
    line(245,352+idx*45,305,352+idx*45,col,5);text(320,337+idx*45,"u = "+u,27,col)
text(485,780,"path variable t",27)
text(85,835,"u = 1 selects f(φI), a constant path in I ∩ J.",29)
text(85,890,"mod I: φI = 0; initial endpoint stays in I.",29)
text(85,945,"mod J: φI = 1; final endpoint stays in J.",29)

text(1360,188,"2  Induction triangle: clopen diagonal  ·  SR.4–SR.8",32)
text(1360,241,"Three-coset sample; proof uses the full continuous bundle C.",28)
gx,gy,cell=1670,330,135
for i in range(3):
    for j in range(3):
        box(gx+j*cell,gy+i*cell,cell-10,cell-10,
            GREEN if i==j else "#e2e7eb","white")
        text(gx+j*cell+27,gy+i*cell+38,"D"+str(i) if i==j else "0",39,
             "white" if i==j else GRAY)
for i in range(3):
    text(gx+i*cell+34,gy+3*cell+16,"c"+str(i),29)
    text(gx-75,gy+i*cell+38,"c"+str(i),29)
text(1630,805,"inner coefficient coset",29)
text(1380,330,"outer",29);text(1380,380,"counting-",29);text(1380,430,"module",29);text(1380,480,"coset",29)
text(1360,865,"C → T is étale: the diagonal in C ×ₜ C is clopen.",28)
text(1360,913,"Diagonal module = Ind D; complement has zero source.",28)
text(1360,962,"Dᵢ is the associated coefficient fibre at coset cᵢ.",26)

text(85,1098,"3  Norm-continuous telescope sample  ·  AT.1–AT.5",32)
text(85,1152,"Exact example P = c₀(ℕ), Pₙ = ℂⁿ; actual theorem uses P.",29)
x,y,w,h=145,1230,1020,355
axes(x,y,w,h,[0,1,2,3,4,5],[0,.125,.25,.375,.5],5,.5)
points=[]
for j in range(1001):
    t=j/200;n=int(math.floor(t));rho=t-n
    error=max((1-rho)*2**(-(n+1)),2**(-(n+2)))
    points.append((x+w*t/5,y+h-h*error/.5))
poly(points,BLUE)
text(520,1645,"telescope variable t",27)
text(85,1710,"aₙ = Σₖ₌₁ⁿ 2⁻ᵏeₖ;  f(n+ρ) = aₙ + ρ 2⁻⁽ⁿ⁺¹⁾eₙ₊₁",28)
text(85,1765,"‖f(n+ρ)−a∞‖ = max{(1−ρ)2⁻⁽ⁿ⁺¹⁾, 2⁻⁽ⁿ⁺²⁾}",28)
text(85,1820,"Two actual anchored sections give the full Milnor sequence.",28)
text(85,1875,"lim and lim¹ vanish here because every stage group is zero.",27)

text(1360,1098,"4  Whole-base lift with original coefficients  ·  PL.1–PL.6",31)
proofboxes=[(1170,"Finite-action restriction","Res_Hj Cq = 0 in KK_Hj   ·   PL.1"),
 (1345,"Slice reciprocity + open Mayer–Vietoris","KK_Gᵏ(Pₙ,Cq) = 0, k = 0,1   ·   PL.2–PL.3"),
 (1520,"Actual anchored telescope + full Milnor sequence","KK_Gᵏ(P,Cq) = 0, k = 0,1   ·   PL.4"),
 (1695,"Puppe exactness","q*: KK_G(P,E₁) ≅ KK_G(P,Q)   ·   PL.5")]
for yy,title,sub in proofboxes:
    box(1370,yy,1135,120,"#edf4f7",BLUE)
    text(1395,yy+18,title,29);text(1395,yy+69,sub,28)
for yy in [1290,1465,1640]:arrow(1935,yy+5,1935,yy+50)
text(1370,1826,"zP = q*⁻¹[i] is the unique actual equivariant lift.",29,GREEN)
text(1370,1878,"For_G D = D₀ holds in KK_T over the whole base.",29,GREEN)

svg.append("</svg>");im.save(args.output/"anchored-localization.png")
(args.output/"anchored-localization.svg").write_text("\n".join(svg),encoding="utf-8")

# Rational checks are exact; the figure's curves merely display these formulas.
vals=[F(j,64) for j in range(65)];checks={}
checks["MV_quotient_endpoint_tests"]=all((1-u)*0+u*0==0 and (1-u)*1+u*1==1 for u in vals)
checks["MV_parameter_range"]=all(0<=(1-u)*t+u*p<=1 for u in vals for t in vals for p in [F(0),F(1,4),F(1,2),F(3,4),F(1)])
checks["MV_taper_cpc_weights"]=all(max(1-2*t,0)+max(2*t-1,0)<=1 for t in vals)
checks["coset_diagonal_identity_three_cosets"]=all(sum(int(i==j) for j in range(3))==1 for i in range(3))
checks["telescope_contraction_stage_inequality"]=all(0<=u*t/(1+(1-u)*t)<=t for u in vals for t in [F(j,2) for j in range(129)])
target=[F(1,2**k) for k in range(1,129)]
checks["telescope_norm_error_formula"]=True
for j in range(257):
    t=F(10*j,256);n=t.numerator//t.denominator;rho=t-n
    sample=[target[k] if k<n else rho*target[k] if k==n else F(0) for k in range(128)]
    direct=max(abs(a-b) for a,b in zip(sample,target))
    formula=max((1-rho)*F(1,2**(n+1)),F(1,2**(n+2)))
    assert direct==formula
assert all(checks.values())
(args.output/"figure-data.json").write_text(json.dumps({
 "schema":"exact-localization-figure-checks/v1", "canvas":[W,H],
 "scope":"Exact rational finite samples; the accompanying analytic texts prove the KK identities",
 "proof_locators":["MV.1–MV.6","SR.4–SR.8","AT.1–AT.5","PL.1–PL.6"],
 "checks":checks},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"output":str(args.output),"checks":checks}))




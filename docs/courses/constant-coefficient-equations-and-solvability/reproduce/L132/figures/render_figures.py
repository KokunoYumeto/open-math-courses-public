"""Original L132 figures with bundled ReportLab graphics. CC0 1.0."""
from pathlib import Path
import json,math
import numpy as np
from reportlab.graphics.shapes import Drawing,Rect,String,Line,Circle
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderSVG,renderPDF
from reportlab.lib.colors import HexColor,white
import pypdfium2 as pdfium
HERE=Path(__file__).resolve().parent
COLORS=["#526580","#007e87","#b06c00","#a63463"]
RADII=[0.0,0.6,0.9,0.98]
def density(t,theta):
 return (1-t*t)/(2*np.pi*(1-2*t*np.cos(theta)+t*t))
def text(d,x,y,s,size=13,anchor="middle",color="#253650"):
 d.add(String(x,y,s,fontName="Helvetica",fontSize=size,textAnchor=anchor,fillColor=HexColor(color)))
def plot(d,x,y,w,h,data,colors,xmin,xmax,ymin,ymax,xsteps,ysteps,xformat=None):
 p=LinePlot();p.x=x;p.y=y;p.width=w;p.height=h;p.data=data
 p.xValueAxis.valueMin=xmin;p.xValueAxis.valueMax=xmax;p.xValueAxis.valueSteps=xsteps
 p.yValueAxis.valueMin=ymin;p.yValueAxis.valueMax=ymax;p.yValueAxis.valueSteps=ysteps
 for a in [p.xValueAxis,p.yValueAxis]:
  a.labels.fontName="Helvetica";a.labels.fontSize=11;a.strokeColor=HexColor("#8a929b")
 if xformat is not None:p.xValueAxis.labelTextFormat=xformat
 for i,c in enumerate(colors):p.lines[i].strokeColor=HexColor(c);p.lines[i].strokeWidth=2
 for yv in ysteps:
  yy=y+(yv-ymin)*h/(ymax-ymin);d.add(Line(x,yy,x+w,yy,strokeColor=HexColor("#e5e8eb"),strokeWidth=.6))
 d.add(p)
 return lambda xx,yy:(x+(xx-xmin)*w/(xmax-xmin),y+(yy-ymin)*h/(ymax-ymin))
def save(d,name):
 renderSVG.drawToFile(d,str(HERE/(name+".svg")))
 out=HERE/(name+".pdf");renderPDF.drawToFile(d,str(out))
 document=pdfium.PdfDocument(str(out));document[0].render(scale=1.7).to_pil().save(HERE/(name+".png"));document.close()

d=Drawing(1200,540);d.add(Rect(0,0,1200,540,fillColor=white,strokeColor=None))
text(d,600,505,"Poisson boundary weights at x = (t, 0) in the unit disk",22)
for x,w,extent,title in [(70,500,np.pi,"Whole circle: integral = 1"),(685,440,.25,"Same densities near the target point")]:
 theta=np.linspace(-extent,extent,12001)
 data=[list(zip(theta.tolist(),density(t,theta).tolist())) for t in RADII]
 steps=[-np.pi,-np.pi/2,0,np.pi/2,np.pi] if extent>1 else [-.25,-.125,0,.125,.25]
 fmt=(lambda v:{-np.pi:"-pi",-np.pi/2:"-pi/2",0:"0",np.pi/2:"pi/2",np.pi:"pi"}.get(v,str(v))) if extent>1 else (lambda v:f"{v:g}")
 plot(d,x,85,w,340,data,COLORS,-extent,extent,-.15,16.5,steps,[0,4,8,12,16],fmt)
 text(d,x+w/2,455,title,17)
 text(d,x,435,"density per radian",12,"start")
 text(d,x+w/2,40,"boundary angle theta (radians)",14)
for i,(t,c) in enumerate(zip(RADII,COLORS)):
 y=399-24*i;d.add(Line(88,y,115,y,strokeColor=HexColor(c),strokeWidth=2));text(d,126,y-4,f"t = {t:g}",13,"start")
text(d,1118,435,"exact t = 0.98 peak: 99/(2 pi)",12,"end",COLORS[-1])
save(d,"poisson-concentration")

d=Drawing(1440,510);d.add(Rect(0,0,1440,510,fillColor=white,strokeColor=None))
text(d,720,475,"An increasing disk family: the finite raw supremum can fail upper semicontinuity",21)
r=np.geomspace(1e-6,1,2401);ks=[1,2,5,10]
data=[list(zip(np.log10(r).tolist(),np.maximum(np.log(r)/k,-1).tolist())) for k in ks]
point=plot(d,70,90,590,300,data,COLORS,-6,0,-1.12,.10,[-6,-4,-2,0],[-1,-.5,0],lambda v:"1" if v==0 else f"10^{int(v)}")
text(d,365,425,"Continuous subharmonic radial sections",17)
text(d,365,43,"positive radius r (log scale)",14)
text(d,70,402,"u_k(r) = max(log(r)/k, -1)",13,"start")
for i,(k,c) in enumerate(zip(ks,COLORS)):
 y=360-24*i;d.add(Line(89,y,115,y,strokeColor=HexColor(c),strokeWidth=2));text(d,126,y-4,f"k = {k}",13,"start")
 xx,yy=point(-k/math.log(10),-1);d.add(Circle(xx,yy,4,fillColor=HexColor(c),strokeColor=None))
raw=plot(d,770,90,270,300,[[(.004,0),(1,0)]],["#253650"],-.08,1.03,-1.12,.10,[0,.5,1],[-1,0],lambda v:f"{v:g}")
text(d,905,425,"Raw supremum",17);text(d,905,43,"radius r",14)
for xx,yy,filled in [(0,0,False),(0,-1,True)]:
 a,b=raw(xx,yy);d.add(Circle(a,b,5,fillColor=HexColor("#253650") if filled else white,strokeColor=HexColor("#253650"),strokeWidth=2))
text(d,822,164,"u(0) = -1",13,"start")
reg=plot(d,1135,90,260,300,[[(0,0),(1,0)]],["#007e87"],-.08,1.03,-1.12,.10,[0,.5,1],[-1,0],lambda v:f"{v:g}")
text(d,1265,425,"Upper semicontinuous regularization",14)
text(d,1265,43,"radius r",14)
a,b=reg(0,0);d.add(Circle(a,b,5,fillColor=HexColor("#007e87"),strokeColor=None))
text(d,1265,285,"u*(r) = 0, including r = 0",12)
save(d,"usc-supremum")

geometry = {
    "schema":"AN02-original-L132-figures/v1", "license":"CC0-1.0",
    "author":"GPT-6.1 Sol (OpenAI)",
    "human_source_credit":"Lars Hörmander, The Analysis of Linear Partial Differential Operators II (1983; second revised printing 1990; reprint 2005), section 16.1, Lemma 16.1.3 and Corollary 16.1.5; original illustrations and disk example",
    "poisson":{
        "dimension":2, "domain":"open unit disk", "boundary":"(cos(theta),sin(theta))",
        "observation_point":"(t,0)", "radii":RADII,
        "exact_density":"(1-t^2)/(2*pi*(1-2*t*cos(theta)+t^2))",
        "exact_peak":"(1+t)/(2*pi*(1-t))", "t098_peak":"99/(2*pi)",
        "full_angle_domain":[-math.pi,math.pi], "zoom_angle_domain":[-0.25,0.25],
        "samples_per_curve":12001, "proved_mass":1,
        "proof_locators":["Theorem P3","P6","P7","P8"],
        "interpretation":"Numerical samples of exact densities; total mass and concentration are proved in the lesson."
    },
    "usc":{
        "dimension":2, "domain":"open unit disk", "section":"radial, not whole-disk",
        "exact_family":"max(log(r)/k,-1); value at r=0 is -1", "k_values":ks,
        "exact_switch_radii":[f"exp(-{k})" for k in ks],
        "switch_radius_samples":[math.exp(-k) for k in ks],
        "raw_supremum":"0 for 0<r<1; -1 at r=0",
        "raw_filled_point":[0,-1], "raw_open_point":[0,0],
        "regularization":"constant0", "regularized_filled_point":[0,0],
        "displayed_radius_one":"boundary limit; r=1 is not in the lesson's open disk",
        "proof_locators":["Theorem S2","S4","S5","Worked example3","Exercise6"]
    }
}
(HERE/"geometry.json").write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Rendered two original PNG/SVG figures and retained exact geometry.")

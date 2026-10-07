"""Original support-function and Liouville illustrations. CC0 1.0."""
from pathlib import Path
import json,math
import numpy as np
from reportlab.graphics.shapes import Drawing,Rect,String,Line,Circle,Polygon
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderSVG,renderPDF
from reportlab.lib.colors import HexColor,white
import pypdfium2 as pdfium
HERE=Path(__file__).resolve().parent
INK='#253650';TEAL='#007e87';PLUM='#a63463';GOLD='#a26600'

def text(d,x,y,value,size=13,anchor='middle',color=INK):
    d.add(String(x,y,value,fontName='Helvetica',fontSize=size,textAnchor=anchor,fillColor=HexColor(color)))
def save(d,name):
    renderSVG.drawToFile(d,str(HERE/(name+'.svg')))
    path=HERE/(name+'.pdf');renderPDF.drawToFile(d,str(path))
    pdf=pdfium.PdfDocument(str(path))
    pdf[0].render(scale=1.7).to_pil().save(HERE/(name+'.png'))
    pdf.close()
def plot(d,x,y,w,h,data,colors,xmin,xmax,ymin,ymax,xsteps,ysteps,xformat=None,dashed=()):
    p=LinePlot();p.x=x;p.y=y;p.width=w;p.height=h;p.data=data
    p.xValueAxis.valueMin=xmin;p.xValueAxis.valueMax=xmax;p.xValueAxis.valueSteps=xsteps
    p.yValueAxis.valueMin=ymin;p.yValueAxis.valueMax=ymax;p.yValueAxis.valueSteps=ysteps
    if xformat:p.xValueAxis.labelTextFormat=xformat
    for axis in [p.xValueAxis,p.yValueAxis]:
        axis.labels.fontName='Helvetica';axis.labels.fontSize=12;axis.strokeColor=HexColor('#8a929b')
    for yy in ysteps:
        ry=y+(yy-ymin)*h/(ymax-ymin)
        d.add(Line(x,ry,x+w,ry,strokeColor=HexColor('#e5e8eb'),strokeWidth=.6))
    for i,c in enumerate(colors):
        p.lines[i].strokeColor=HexColor(c);p.lines[i].strokeWidth=2
        if i in dashed:p.lines[i].strokeDashArray=[6,5]
    d.add(p)
    return lambda xx,yy:(x+(xx-xmin)*w/(xmax-xmin),y+(yy-ymin)*h/(ymax-ymin))

d=Drawing(1480,700);d.add(Rect(0,0,1480,700,fillColor=white,strokeColor=None))
text(d,740,659,'A horizontal envelope has a compact set of slopes',24)
text(d,740,626,'Three exponentials: M(y) = (1/2) log(exp(-2 y1) + exp(2 y1) + exp(4 y2))',15)
text(d,290,593,'Support set in slope coordinates',18)
x0,y0,scale=70,130,110
coord=lambda x,y:(x0+(x+2)*scale,y0+(y+1)*scale)
for xv in [-2,-1,0,1,2]:
    x,y=coord(xv,-1);_,top=coord(xv,3)
    d.add(Line(x,y,x,top,strokeColor=HexColor('#e5e8eb'),strokeWidth=.6));text(d,x,y-20,f'{xv:g}',11)
for yv in [-1,0,1,2,3]:
    x,y=coord(-2,yv);right,_=coord(2,yv)
    d.add(Line(x,y,right,y,strokeColor=HexColor('#e5e8eb'),strokeWidth=.6));text(d,x-15,y-4,f'{yv:g}',11)
origin=coord(0,0)
d.add(Line(*coord(-2,0),*coord(2,0),strokeColor=HexColor('#8a929b'),strokeWidth=.8))
d.add(Line(*coord(0,-1),*coord(0,3),strokeColor=HexColor('#8a929b'),strokeWidth=.8))
vertices=[(-1,0),(1,0),(0,2)]
flat=[value for point in vertices for value in coord(*point)]
d.add(Polygon(flat,fillColor=HexColor('#dceff0'),strokeColor=HexColor(TEAL),strokeWidth=2))
for point,label,dx,dy in [((-1,0),'(-1, 0)',-8,-23),((1,0),'(1, 0)',8,-23),((0,2),'(0, 2)',-35,15)]:
    x,y=coord(*point);d.add(Circle(x,y,4,fillColor=HexColor(TEAL),strokeColor=None));text(d,x+dx,y+dy,label,12)
start=coord(-1,3);end=coord(2,0)
d.add(Line(*start,*end,strokeColor=HexColor(PLUM),strokeWidth=1.5,strokeDashArray=[6,4]))
text(d,432,534,'xi1 + xi2 = 2',13,color=PLUM)
ax,ay=coord(1,1);ox,oy=origin
d.add(Line(ox,oy,ax,ay,strokeColor=HexColor(GOLD),strokeWidth=2))
d.add(Line(ax,ay,ax-15,ay-5,strokeColor=HexColor(GOLD),strokeWidth=2))
d.add(Line(ax,ay,ax-5,ay-15,strokeColor=HexColor(GOLD),strokeWidth=2))
text(d,ax+20,ay-1,'eta = (1, 1)',12,'start',GOLD)
text(d,290,80,'xi1',14);text(d,70,575,'xi2',13,'start')
text(d,290,56,'H(eta) = 2; the support line touches the top vertex',13)

t=np.linspace(-3,3,1601)
envelope=.5*np.log(np.exp(-2*t)+np.exp(2*t)+np.exp(4*t))
support=np.maximum.reduce([-t,t,2*t])
gap=.5*math.log(3)
data=[list(zip(t.tolist(),envelope.tolist())),list(zip(t.tolist(),support.tolist())),list(zip(t.tolist(),(support+gap).tolist()))]
plot(d,730,165,630,370,data,[TEAL,INK,GOLD],-3,3,-.2,6.8,[-3,-2,-1,0,1,2,3],[0,2,4,6],dashed=[2])
text(d,1045,593,'Exact section y = t eta',18)
for xx,label,c,dash in [(748,'M(t eta)',TEAL,False),(945,'H(t eta)',INK,False),(1130,'H(t eta) + log(3)/2',GOLD,True)]:
    d.add(Line(xx,561,xx+24,561,strokeColor=HexColor(c),strokeWidth=2,strokeDashArray=[6,4] if dash else None))
    text(d,xx+32,557,label,13,'start')
text(d,1045,112,'real section parameter t',14)
text(d,1045,78,'0 <= M(y) - H(y) <= log(3)/2',15,color=TEAL)
text(d,740,24,'Left: equal Euclidean coordinate scales. Right: exact sampled functions; the bound and support set are proved in Example C and sections 3-4.',13)
save(d,'support-set-and-envelope')

d=Drawing(1400,650);d.add(Rect(0,0,1400,650,fillColor=white,strokeColor=None))
text(d,700,612,'An expanding annulus proves subharmonic Liouville',24)
text(d,700,580,'The plotted objects are comparison barriers; the observation radius stays fixed at rho = 3',15)
cx,cy,s=330,300,35
d.add(Circle(cx,cy,6*s,fillColor=HexColor('#edf5f5'),strokeColor=HexColor(TEAL),strokeWidth=1.5))
d.add(Circle(cx,cy,s,fillColor=white,strokeColor=HexColor(PLUM),strokeWidth=1.5))
d.add(Line(cx-6*s-12,cy,cx+6*s+12,cy,strokeColor=HexColor('#8a929b'),strokeWidth=.6))
d.add(Line(cx,cy-6*s-12,cx,cy+6*s+12,strokeColor=HexColor('#8a929b'),strokeWidth=.6))
for value in [1,3,6]:
    xx=cx+value*s;d.add(Line(xx,cy-3,xx,cy+3,strokeColor=HexColor(INK),strokeWidth=.8));text(d,xx,cy-23,str(value),11)
d.add(Circle(cx+3*s,cy,5,fillColor=HexColor(GOLD),strokeColor=None))
text(d,330,541,'Annulus at outer radius R = 6',18)
text(d,145,487,'outer circle: C = 1',13,'start',TEAL)
text(d,330,334,'center c = 0',12)
text(d,165,227,'inner circle: delta = 1',12,'start',PLUM)
text(d,165,205,'bound alpha = -1/2',12,'start',PLUM)
text(d,cx+3*s+12,cy+20,'fixed observation point',12,'start',GOLD)
value6=-.5+1.5*math.log(3)/math.log(6)
text(d,330,55,f'At this point: B_6(3) = {value6:.4f}',14)

logrs=np.linspace(math.log10(3.2),8,1601)
values=-.5+1.5*math.log(3)/(logrs*math.log(10))
data=[list(zip(logrs.tolist(),values.tolist())),[(float(logrs[0]),-.5),(8,-.5)]]
plot(d,770,130,550,380,data,[TEAL,PLUM],float(logrs[0]),8,-.6,1.1,[1,2,4,6,8],[-.5,0,.5,1],lambda x:{1:'10',2:'100',4:'10^4',6:'10^6',8:'10^8'}.get(x,str(x)),dashed=[1])
text(d,1045,541,'Barrier at the same fixed radius rho = 3',18)
text(d,770,520,'B_R(3)',13,'start')
text(d,1100,520,'dashed limit: alpha = -1/2',12,color=PLUM)
text(d,1045,74,'outer radius R (logarithmic scale)',14)
text(d,700,24,'Exact formula: B_R(3) = -1/2 + (3/2) log(3)/log(R), R > 3. Lemma C1 proves the fixed-point limit.',13)
save(d,'annulus-liouville')

geometry={'schema':'AN02-original-L139-figures/v1','license':'CC0-1.0','author':'GPT-6.1 Sol (OpenAI)',
 'human_source_credit':'Lars Hörmander, The Analysis of Linear Partial Differential Operators II (1983; second revised printing 1990; reprint 2005), Lemmas16.2.1-16.2.2, printed314-315; original illustrations',
 'support_set_and_envelope':{'dimension':2,'vertices':[list(p) for p in vertices],'intercepts':[0,0,0],
   'support_set':'conv{(-1,0),(1,0),(0,2)}','direction':[1,1],'support_value':2,
   'support_line':'xi1+xi2=2','metric':'equal Euclidean coordinate scales in slope panel',
   'envelope':'0.5*log(exp(-2*y1)+exp(2*y1)+exp(4*y2))',
   'support_function':'max(-y1,y1,2*y2)','section':'y=t*(1,1), -3<=t<=3',
   'section_envelope':'0.5*log(exp(-2*t)+exp(2*t)+exp(4*t))',
   'section_support':'max(-t,t,2*t)','proved_gap_bound':'0<=M(y)-H(y)<=0.5*log(3)',
   'proof_locators':'Theorem E1, sections3-4; Example C, (E28)-(E30)',
   'sampling':'1601 evenly spaced section samples; no numerical inference of theorem'},
 'annulus_liouville':{'dimension':2,'center':[0,0],'inner_radius':1,'outer_radius_geometry':6,
   'alpha':-.5,'C':1,'observation_point':[3,0],'observation_radius':3,
   'barrier':'alpha+(C-alpha)*log(|z-c|/delta)/log(R/delta)',
   'fixed_point_curve':'-0.5+1.5*log(3)/log(R)','R_domain':[3.2,100000000],
   'horizontal_plot_axis':'log10(R)','geometric_panel_metric':'equal Euclidean coordinate scales',
   'fixed_observation_point':True,'object_type':'harmonic comparison barrier, not an unspecified subharmonic function',
   'proved_limit':-.5,'proof_locators':'Lemma C1, (E26); Theorem C2',
   'sampling':'1601 evenly spaced samples in log10(R)'},
 'output':{'svg':'vector illustration','pdf':'original one-page vector illustration','png':'native render from own PDF at scale1.7'}}
(HERE/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figures':2,'section_gap_at_zero':gap,'annulus_value_R6':value6}))

"""Exact quadratic collar graphs and full cotangent labels, with model data."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1]; p=r
f=p/'figures/boundary-normal-window-transfer.svg'
ns='http://www.w3.org/2000/svg';ET.register_namespace('',ns)
svg=ET.Element('{'+ns+'}svg',{'width':'780','height':'440','viewBox':'0 0 780 440',
    'role':'img','aria-labelledby':'title desc'})
def e(tag,a,text=None):
    v=ET.SubElement(svg,'{'+ns+'}'+tag,a)
    if text is not None:v.text=text
    return v
def t(x,y,s,size=14,weight='normal'):
    return e('text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif',
        'font-size':str(size),'fill':'#132238','font-weight':weight},s)
def line(x1,y1,x2,y2,col='#61748c',dash=None):
    a={'x1':str(x1),'y1':str(y1),'x2':str(x2),'y2':str(y2),'stroke':col,'stroke-width':'1.5'}
    if dash:a['stroke-dasharray']=dash
    return e('line',a)
px=lambda y:70+170*y
py=lambda x:306-190*x
e('title',{'id':'title'},'A boundary-fixed collar retains the full time-covector shift')
e('desc',{'id':'desc'},'Exact model at t=1: y=v+x squared over two, with v=0 and v=1 and x between zero and one. Dashed reference lines show the original v levels, solid quadratic curves show their images. These are coordinate lines, not characteristic rays. Full time and compressed normal covector shifts are labeled.')
e('rect',{'width':'780','height':'440','fill':'#f8fafc'})
t(22,29,'A normal form that preserves the boundary wavefront',20,'bold')
t(28,56,'Exact section at t = 1',16,'bold')
line(px(0),py(0),px(1.72),py(0));line(px(0),py(0),px(0),py(1.13))
for x in [.5,1]:
    line(px(0)-4,py(x),px(0)+4,py(x));t(38,py(x)+5,str(x),13)
for y in [0,.5,1,1.5]:
    line(px(y),py(0)-4,px(y),py(0)+4);t(px(y)-8,328,str(y),13)
t(51,93,'x',15,'bold');t(377,311,'y',15,'bold')
curves=[]
for v,col in [(0,'#2563eb'),(1,'#059669')]:
    line(px(v),py(0),px(v),py(1),col,'5 5')
    path=f'M {px(v)} {py(0)} Q {px(v)} {py(.5)} {px(v+.5)} {py(1)}'
    e('path',{'d':path,'fill':'none','stroke':col,'stroke-width':'2.7'})
    e('circle',{'cx':str(px(v)),'cy':str(py(0)),'r':'4','fill':col})
    curves.append({'v':v,'t':1,'x_interval':[0,1],
        'exact_equation':'y=v+x^2/2','bezier_control':[[px(v),py(0)],[px(v),py(.5)],[px(v+.5),py(1)]]})
t(115,103,'y = x²/2',14,'bold');t(270,84,'y = 1 + x²/2',14,'bold')
t(130,353,'Boundary points are fixed.',14,'bold')
e('rect',{'x':'420','y':'47','width':'338','height':'311','rx':'8','fill':'white','stroke':'#6a86a6'})
t(435,72,'Keep every covector component',16,'bold')
t(435,106,'ρ = ξ + xt ζ',16)
t(435,139,'ϑ = τ + x² ζ/2',16,'bold')
t(435,172,'η = ζ',16)
line(435,190,744,190)
t(435,215,'σ̂ = σ + x²t ζ',16)
t(435,247,'R = (ϑ − x²η/2)² − η²',16)
t(435,278,'Time mixing remains in R.',14,'bold')
t(435,305,'x = O(s²) gives an O(s⁴)',14)
t(435,329,'coordinate error. (NC19), (NC23)',14)
e('rect',{'x':'22','y':'373','width':'736','height':'49','rx':'7','fill':'white','stroke':'#6a86a6'})
t(35,394,'Dashed: reference levels. Solid: exact collar images, not characteristic rays.',14)
t(35,414,'Proof: NC2–NC10, NC27–NC29. Primary geometric credit: Melrose–Sjöstrand XV.1.',13)
f.parent.mkdir(parents=True,exist_ok=True);ET.indent(svg);ET.ElementTree(svg).write(f,encoding='utf-8',xml_declaration=True)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
record={'schema':'an04-normal-window-figure/v1','svg':f.relative_to(r).as_posix(),
    'svg_sha256':sha(f),'generator_sha256':sha(Path(__file__)),'width':780,'height':440,
    'proof_locators':['NC2--NC10','NC19','NC23','NC27--NC29'],'exact_model_curves':curves,
    'not_characteristic_rays':True,'unpictured_covectors_fully_labeled':True,
    'human_source_credit':'Melrose and Sjöstrand boundary normal-form route, printed XV.1; Vasy compressed projection framework',
    'new_expression_licence':'CC0-1.0','original_research_claim':False,'actual_render_visually_inspected':False}
(p/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'exact_model_figure':True,'curves':2,'canvas':[780,440]})

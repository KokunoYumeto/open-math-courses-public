"""Exact quadratic support envelopes; reproducible pedagogical phase diagram."""
from pathlib import Path
import hashlib,json,math,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1];p=r;f=p/'figures/smooth-glancing-windows.svg'
ns='http://www.w3.org/2000/svg';ET.register_namespace('',ns)
svg=ET.Element('{'+ns+'}svg',{'width':'780','height':'440','viewBox':'0 0 780 440','role':'img','aria-labelledby':'title desc'})
def e(tag,a,text=None):
    v=ET.SubElement(svg,'{'+ns+'}'+tag,a)
    if text is not None:v.text=text
    return v
def t(x,y,s,size=14,weight='normal'):
    return e('text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'fill':'#132238','font-weight':weight},s)
def line(x1,y1,x2,y2,color='#66788a',dash=None):
    a={'x1':str(x1),'y1':str(y1),'x2':str(x2),'y2':str(y2),'stroke':color,'stroke-width':'1.4'}
    if dash:a['stroke-dasharray']=dash
    return e('line',a)
px=lambda T:54+(T+1.35)*98
py=lambda X:294-108*X
e('title',{'id':'title'},'Nested glancing supports retain one common smooth neighborhood')
e('desc',{'id':'desc'},'Exact support envelopes for beta one, three quarters and the limiting one half, epsilon one quarter and incoming threshold one quarter. Each has T plus X squared at most one plus beta and T at least minus one plus epsilon times threshold minus beta. The common inner rectangle and independently regular compressed normal guard are distinct.')
e('rect',{'width':'780','height':'440','fill':'#f8fafc'})
t(22,28,'One smooth neighborhood from nested glancing estimates',20,'bold')
t(28,54,'Exact support: ε = h* = 1/4',16,'bold')
records=[]
for beta,color,opacity in [(1,'#2563eb','.18'),(.75,'#0891b2','.22'),(.5,'#059669','.25')]:
    lo=-1+.25*(.25-beta);hi=1+beta;X=math.sqrt(hi-lo)
    path=f'M {px(lo)} {py(0)} L {px(lo)} {py(X)} Q {px(hi)} {py(X/2)} {px(hi)} {py(0)} Z'
    e('path',{'d':path,'fill':color,'fill-opacity':opacity,'stroke':color,'stroke-width':'1.6'})
    records.append({'beta':beta,'T_min':lo,'upper_constant':hi,'X_max':X,
        'rendering':'Exact quadratic Bezier parameterized by X'})
e('rect',{'x':str(px(-.25)),'y':str(py(.25)),'width':str(px(.25)-px(-.25)),
    'height':str(py(0)-py(.25)),'fill':'#fef08a','stroke':'#a16207','stroke-width':'1.5'})
line(px(-1.35),py(0),px(2.15),py(0));line(px(-1.35),py(0),px(-1.35),py(1.95))
for T in [-1,0,1,2]:
    line(px(T),py(0)-4,px(T),py(0)+4);t(px(T)-6,312,str(T).replace('-','−'),12)
for X in [1,1.5]:
    line(px(-1.35)-4,py(X),px(-1.35)+4,py(X));t(24,py(X)+4,str(X),12)
t(52,81,'X',14,'bold');t(385,283,'T',14,'bold')
t(187,88,'T + X² ≤ 1 + β',14,'bold')
for yy,beta,col,label in [(188,1,'#2563eb','β = 1'),(211,.75,'#0891b2','β = 3/4'),(234,.5,'#059669','β → 1/2')]:
    line(276,yy-4,297,yy-4,col);t(304,yy,label,13)
t(172,327,'common inner rectangle',13)
e('rect',{'x':'420','y':'47','width':'338','height':'283','rx':'8','fill':'white','stroke':'#6585a7'})
t(435,72,'Supply every lower energy tester',16,'bold')
t(435,101,'new positive support lies inside:',14)
t(447,126,'old positive elliptic set',14,'bold')
t(447,150,'∪ independently smooth normal guard',14)
line(435,165,744,165)
t(435,190,'Guard: |σ|/|τ| > Cσ ω/2',15,'bold')
t(435,214,'The outer χ₂ edge remains here.',14)
t(435,238,'β nesting alone does not remove it.',14)
t(435,265,'stage j: energy output order j/2',14)
t(435,290,'next lower order = (j−1)/2',14)
t(435,314,'(CG7), (CG21)–(CG27)',13)
e('rect',{'x':'22','y':'346','width':'736','height':'76','rx':'8','fill':'white','stroke':'#6585a7'})
t(35,370,'incoming characteristic window → all-order incoming tester → common inner region',15,'bold')
t(35,394,'Source front removed; noncharacteristic points regular. Both clock signs. (CG32)–(CG34)',14)
t(35,414,'Quadratic scale: δ = 2 |h|,  ω = L* δ². Complete arguments in Sections 2–8.',13)
f.parent.mkdir(parents=True,exist_ok=True);ET.indent(svg)
ET.ElementTree(svg).write(f,encoding='utf-8',xml_declaration=True)
record={'schema':'an04-smooth-glancing-figure/v1','svg':f.relative_to(r).as_posix(),
    'svg_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
    'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'width':780,'height':440,'proof_locators':'CG7;CG21--CG27;CG32--CG34',
    'normalized_plot':{'epsilon':.25,'h_star':.25,'envelopes':records,
        'common_rectangle':{'T':[-.25,.25],'X':[0,.25]},
        'limiting_beta_is_not_finite_iteration_step':True},
    'source_credit':'András Vasy freely readable elliptic and nested-cutoff route; new receiving proof/diagram by GPT-6.1 Sol (OpenAI), Ultra',
    'new_expression_licence':'CC0-1.0','pedagogical_estimate_diagram':True,
    'original_research_claim':False,'actual_render_visually_inspected':False}
(p/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'figure_created':True,'exact_quadratic_envelopes':3,'canvas':[780,440]})

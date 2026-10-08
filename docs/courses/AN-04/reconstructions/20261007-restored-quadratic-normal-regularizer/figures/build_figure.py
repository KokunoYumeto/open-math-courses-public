"""Reproducible pedagogical estimate and limit diagram, not a research figure."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1];p=r
f=p/'figures/quadratic-normal-regularizer.svg'
ns='http://www.w3.org/2000/svg';ET.register_namespace('',ns)
svg=ET.Element('{'+ns+'}svg',{'width':'780','height':'440','viewBox':'0 0 780 440','role':'img','aria-labelledby':'title desc'})
def e(tag,attrs,text=None,parent=svg):
    a=ET.SubElement(parent,'{'+ns+'}'+tag,attrs)
    if text is not None:a.text=text
    return a
e('title',{'id':'title'},'Quadratic normal error and removal of a boundary regularizer')
e('desc',{'id':'desc'},'One ordinary normal derivative on each factor. The exact parametrix identity retains three negative corrections. A fixed-width uniform Hilbert norm bound, with distributional convergence, yields the unregularized norm bound.')
e('rect',{'width':'780','height':'440','fill':'#f8fafc'})
def text(x,y,s,size=16,color='#132238',weight='normal'):
    return e('text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'fill':color,'font-weight':weight},s)
def box(x,y,w,h):
    e('rect',{'x':str(x),'y':str(y),'width':str(w),'height':str(h),'rx':'8','fill':'white','stroke':'#6585a7','stroke-width':'1.3'})
def arrow(x,y,x2,y2):
    e('line',{'x1':str(x),'y1':str(y),'x2':str(x2),'y2':str(y2),'stroke':'#34567b','stroke-width':'2'})
    e('path',{'d':f'M {x2-7} {y2-4} L {x2} {y2} L {x2-7} {y2+4}','fill':'none','stroke':'#34567b','stroke-width':'2'})
text(22,30,'Quadratic error: normalize both normal factors',20,weight='bold')
box(22,48,344,72);box(407,48,351,72);arrow(369,84,400,84)
text(35,74,'g = DₓBu,    w = Tg,    T⁻T = I + E')
text(35,99,'e = Eg has residual coefficients (QR2–QR7)',14)
text(420,74,'F = (T⁻)* R T⁻,    ‖f₀‖ ≤ M/ε')
text(420,99,'‖Fw‖ ≤ (2M/ε)‖w‖ + C Xν (QR13)',14)
box(22,137,736,66)
text(35,162,'(Rg,g) = (Fw,w) − (Re,g) − (Rg,e) − (Re,e)',17,weight='bold')
text(35,187,'Every signed tail has a bare energy bound. Only b-coefficient adjoints move. (QR5, QR8)',14)
box(22,220,736,58)
text(35,243,'‖w‖² ≤ C_N ω ‖Bu‖² + K Zν²    ⇒    quadratic leading coefficient 2M C_N ω/ε + γ',15)
text(35,265,'ω ≤ C_w εδ gives 2M C_N C_w δ + γ; all lower/source errors remain. (QR15–QR16)',14)
text(22,311,'Regularizer limit: fix the spatial widths first',20,weight='bold')
box(22,329,344,62);box(407,329,351,62);arrow(369,360,400,360)
text(35,353,'Bᵣ = BΛᵣ,   individual order ν − L ≤ 0',15)
text(35,377,'Bᵣu → Bu in distributions (QR22–QR23)',14)
text(420,353,'supᵣ ‖Bᵣu‖ℋ ≤ C  ⇒  ‖Bu‖ℋ ≤ C',16,weight='bold')
text(420,377,'ℋ = L2 or V, with the same norm (QR24–QR25)',14)
text(22,421,'Both form domains retained. No positive-commutator estimate or uniform shrinking-width bound is asserted.',13)
f.parent.mkdir(parents=True,exist_ok=True);ET.indent(svg);ET.ElementTree(svg).write(f,encoding='utf-8',xml_declaration=True)
record={'schema':'an04-quadratic-normal-regularizer-figure/v1','svg':f.relative_to(r).as_posix(),'svg_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'width':780,'height':440,'proof_locators':'QR2–QR16 and QR20–QR25','source_credit':'András Vasy, free paper PDF37–38/48 and complete correction; new receiving argument and figure by GPT-6.1 Sol (OpenAI), Ultra','new_expression_licence':'CC0-1.0','pedagogical_estimate_diagram':True,'original_research_claim':False,'actual_render_visually_inspected':False,'preserved_original_diagram':True}
(p/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'figure_source_created':True,'canvas':[780,440]})

"""Reproducible exact normalized support envelope and leading-error diagram."""
from pathlib import Path
import hashlib,json,math,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1];p=r;f=p/'figures/compensated-glancing-positive.svg'
ns='http://www.w3.org/2000/svg';ET.register_namespace('',ns)
svg=ET.Element('{'+ns+'}svg',{'width':'780','height':'440','viewBox':'0 0 780 440','role':'img','aria-labelledby':'title desc'})
def e(tag,attrs,text=None):
 a=ET.SubElement(svg,'{'+ns+'}'+tag,attrs)
 if text is not None:a.text=text
 return a
def t(x,y,s,size=14,weight='normal'):
 return e('text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'fill':'#132238','font-weight':weight},s)
def line(x1,y1,x2,y2,color='#66788a',dash=None):
 a={'x1':str(x1),'y1':str(y1),'x2':str(x2),'y2':str(y2),'stroke':color,'stroke-width':'1.4'}
 if dash:a['stroke-dasharray']=dash
 return e('line',a)
px=lambda v:60+(v+1.4)*95
py=lambda v:300-v*108
samples=[(-1.25+3.25*i/160,math.sqrt(3.25-3.25*i/160)) for i in range(161)]
e('title',{'id':'title'},'An exact glancing support envelope and the leading normal errors')
e('desc',{'id':'desc'},'For beta one and epsilon one quarter, the normalized cutoff support is T at least minus five quarters and X squared plus T at most two, with X nonnegative. The incoming transition lies between T minus five quarters and minus one. The compressed normal cutoff shrinks with omega equal to epsilon delta. Zero, linear and quadratic normal errors have different small scales.')
e('rect',{'width':'780','height':'440','fill':'#f8fafc'})
t(22,28,'Cutoff geometry and the positive weak form',20,'bold')
t(30,56,'Exact envelope: β = 1, ε = 1/4',16,'bold')
A=math.sqrt(3.25);B=math.sqrt(3)
# X is affine in the Bezier parameter; T=2-X^2 is quadratic.
# These paths represent the exact parabola rather than polyline interpolation.
envelope=f'M {px(-1.25)} {py(0)} L {px(-1.25)} {py(A)} Q {px(2)} {py(A/2)} {px(2)} {py(0)} Z'
e('path',{'d':envelope,'fill':'#dbeafe','stroke':'#2563eb','stroke-width':'1.5'})
strip=f'M {px(-1.25)} {py(0)} L {px(-1.25)} {py(A)} Q {px(2-A*B)} {py((A+B)/2)} {px(-1)} {py(B)} L {px(-1)} {py(0)} Z'
e('path',{'d':strip,'fill':'#fed7aa','fill-opacity':'.8'})
line(px(-1.4),py(0),px(2.2),py(0));line(px(-1.4),py(0),px(-1.4),py(1.95))
line(px(-1),py(0),px(-1),py(math.sqrt(3)),'#c2410c','4 3')
line(px(-1.25),py(0),px(-1.25),py(math.sqrt(3.25)),'#c2410c','4 3')
for a,label in [(-1.25,'−5/4'),(-1,'−1'),(0,'0'),(1,'1'),(2,'2')]:
 line(px(a),py(0)-4,px(a),py(0)+4);t(px(a)-(24 if a==-1.25 else 11),318,label,12)
for b in [1,1.5]:
 line(px(-1.4)-4,py(b),px(-1.4)+4,py(b));t(31,py(b)+4,str(b),12)
t(58,82,'X',14,'bold');t(368,288,'T',14,'bold')
t(207,133,'T + X² = 2',14,'bold')
t(125,246,'χ₁ = 1 for T ≥ −1',14)
t(66,101,'incoming',12);t(66,116,'strip',12)
e('rect',{'x':'424','y':'47','width':'334','height':'268','rx':'8','fill':'white','stroke':'#6585a7'})
t(438,72,'Full support and leading scales',16,'bold')
t(438,100,'ω = εδ;  |σ|/|τ| ≤ 2 Cσ ω',16)
t(438,124,'normal energy:  ‖T DₓBᵣu‖²',15)
t(438,146,'≤ C′N ω ‖Bᵣu‖² + lower/source',14)
line(438,161,744,161)
t(438,186,'zero error:     δ + δ/ε',15)
t(438,213,'linear error:   √(δ/ε)',15)
t(438,240,'quadratic:      δ',15)
t(438,268,'weight derivative:  δ/A₀',15)
t(438,293,'(PC18), (PC33)–(PC34), (PC44)',13)
e('rect',{'x':'22','y':'337','width':'736','height':'84','rx':'8','fill':'white','stroke':'#6585a7'})
t(35,361,'Cᵣ = 4 ‖Bᵣu‖² + zero + linear + quadratic + incoming + elliptic + lower',16,'bold')
t(35,386,'The full source and complex lower form remain in Cᵣ. (PC26), (PC35)',14)
t(35,408,'Choose ε = L* δ; then L* large, δ small and A₀ large. Both weak form domains.',14)
f.parent.mkdir(parents=True,exist_ok=True);ET.indent(svg);ET.ElementTree(svg).write(f,encoding='utf-8',xml_declaration=True)
record={'schema':'an04-compensated-glancing-figure/v1','svg':f.relative_to(r).as_posix(),'svg_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'width':780,'height':440,
 'proof_locators':'PC16--PC28,PC33--PC44','normalized_plot':{'beta':1,'epsilon':.25,'T_min':-1.25,'T_max':2,'X_min':0,'envelope':'T+X^2<=2','incoming_strip':[-1.25,-1],'curve_samples':samples,'curve_rendering':'Exact quadratic Bezier in the coordinate X; samples are supplementary exact-coordinate points.'},
 'source_credit':'András Vasy freely readable paper complete PDF35--42/44--48 and two-page correction; new receiving proof and figure by GPT-6.1 Sol (OpenAI), Ultra',
 'new_expression_licence':'CC0-1.0','pedagogical_estimate_diagram':True,'original_research_claim':False,'actual_render_visually_inspected':False,'preserved_original_diagram':True}
(p/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'figure_created':True,'exact_envelope_samples':len(samples),'canvas':[780,440]})

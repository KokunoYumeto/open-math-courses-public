"""Smooth compact inverse, exact normal form and distinct domain conditions: CC0."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, base64, hashlib, html, io, json, math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=ROOT/'out')
parser.add_argument('--resources',type=Path,default=ROOT.parent/'labelled-geometric-kernel')
args=parser.parse_args(); OUTPUT=args.output_dir; OUTPUT.mkdir(parents=True,exist_ok=True)
font_bytes=(args.resources/'fonts/DejaVuSans.ttf').read_bytes()
notice=(args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
W,H=2500,1810
INK,BLUE,GREEN,RED,GRAY='#17283c','#17638d','#286d49','#b64932','#65737e'
im=Image.new('RGB',(W,H),'#f8fafc'); d=ImageDraw.Draw(im); fonts={}; overflow=[]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<title>Smooth compact inverse and completed normal forms</title>',
     '<desc>Actual inverse-field construction and infinitesimal positive-order bound; exact real rotating-block example separates form control, one-sided operator estimates and transport-domain preservation.</desc>',
     '<metadata>'+html.escape('Original drawing: CC0.\n'+notice)+'</metadata>',
     '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font_bytes).decode()+')}text{font-family:LocalSans}</style>',
     f'<rect width="{W}" height="{H}" fill="#f8fafc"/>']

def text(x,y,s,size=31,col=INK):
    if size not in fonts: fonts[size]=ImageFont.truetype(io.BytesIO(font_bytes),size,layout_engine=ImageFont.Layout.BASIC)
    bounds=d.textbbox((x,y),s,font=fonts[size],anchor='lt')
    if bounds[0]<0 or bounds[1]<0 or bounds[2]>W or bounds[3]>H: overflow.append([s,list(bounds)])
    d.text((x,y),s,font=fonts[size],fill=col,anchor='lt')
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def box(x,y,w,h,fill='white',col='#c9d5e3'):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=col,width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{col}" stroke-width="3"/>')

def arrow(x,y,xx,yy,col=BLUE):
    d.line((x,y,xx,yy),fill=col,width=4)
    svg.append(f'<path d="M{x},{y}L{xx},{yy}" fill="none" stroke="{col}" stroke-width="4"/>')
    a=math.atan2(yy-y,xx-x); points=[(xx,yy)]+[(xx-17*math.cos(a+b),yy-17*math.sin(a+b)) for b in [-.45,.45]]
    d.polygon(points,fill=col)
    svg.append('<polygon points="'+' '.join(f'{px:.5f},{py:.5f}' for px,py in points)+f'" fill="{col}"/>')

text(45,25,'Smooth compact inverse → completed normal form; transport domains need their own proof',39)
text(45,87,'CW.1–CW.9 on the actual intrinsic jet field; the real circle blocks below illustrate precisely the supplied estimates.',29)
box(45,145,2410,423)
text(77,175,'Actual construction over YH, then the free compact-frame quotient over the original units',34)
box(80,238,595,120,'#e9f3f8',BLUE)
text(106,259,'Real jet columns S, S′v',33,BLUE)
text(106,312,'K average: h=SS*, ‖S′v‖≤ε',29,BLUE)
arrow(698,295,868,295)
box(892,238,635,120,'#e3f2e9',GREEN)
text(918,259,'Θ=h⁻¹, Dom Θ=Ran h',33,GREEN)
text(918,312,'h compact, dense range; Θ≥ε⁻²',28,GREEN)
arrow(1545,295,1714,295,GREEN)
box(1740,238,675,120,'#e3f2e9',GREEN)
text(1766,259,'Compact norm-smooth resolvents',29,GREEN)
text(1766,312,'∂vR±=(1±ih)⁻¹(∂vh)(1±ih)⁻¹',27,GREEN)
text(80,389,'Exact completed form: qv(u,w)=−⟨Θu,(∂vh)Θw⟩ on Dom Θ; Θ is never applied to ∇vw.',30)
text(80,444,'For every a>0:  ±qv(u,u) ≤ a⟨Θu,Θu⟩ + (2 Cv⁴/a³)⟨u,u⟩,   Cv=‖S′v‖≤ε.',32,GREEN)
text(80,501,'The K quotient restricts to one representative fibre.  The full inverse Spinᶜ coefficient and right Clifford order stay intact.',27)

box(45,610,2410,649)
text(77,641,'Exact noncommuting real block at x=0: n=2,  h=diag(¼,1/256),  Θ=diag(4,256)',34)
text(80,704,'Normal derivative Θ′',31,BLUE)
box(80,754,495,158,'#e9f3f8',BLUE)
text(118,781,'[   0       −252  ]',37,BLUE)
text(118,843,'[ −252       0   ]',37,BLUE)
arrow(597,825,806,825,GREEN)
text(607,763,'both sides h',26,GREEN)
box(834,754,690,158,'#e3f2e9',GREEN)
text(861,782,'h Θ′ h: off-diagonal −63/256',31,GREEN)
text(861,845,'norm = 63/256; form control',29,GREEN)
text(1799,704,'Separate: right Θ⁻²',27,RED)
box(1774,754,644,158,'#fff3ee',RED)
text(1799,782,'Θ′Θ⁻²: lower entry −63/4',31,RED)
text(1799,845,'norm = 63/4; different bound',28,RED)
text(80,955,'All n≥2:  ‖h Θ′ h‖ = 2⁻ⁿ−2⁻ⁿ³ → 0,    but  ‖Θ′Θ⁻²‖ = 2^(n³−2n)−2⁻ⁿ → ∞.',32)
text(80,1018,'The one-sided expression is unbounded on the finite-block core.  Small normal forms do not imply this operator estimate.',27,RED)
text(80,1085,'Positive-order sample: C=½, a=¼ gives 2 C⁴/a³=8 exactly.',31,GREEN)
text(80,1143,'¼ Θ² + 8 I ∓ Θ′ = [12, ±252; ±252, 16392],  determinant 133200 > 0; both signs are positive.',29,GREEN)
text(80,1200,'The full inequality is CW.9. This finite block checks its constants; it does not replace the completed module proof.',27)

box(45,1298,2410,386)
text(77,1328,'Completed section-domain example: smooth C₂ coefficient action by the constant swap P',34)
box(82,1395,965,150,'#e9f3f8',BLUE)
text(109,1422,'u(x)=U(x)(2⁻ⁿ/n,0)n;  Θu=U(x)(1/n,0)n',31,BLUE)
text(109,1484,'‖Θu‖²=Σn≥2 1/n²≤1;  u belongs to Ran h.',29,BLUE)
arrow(1069,1470,1343,1470,RED)
text(1112,1409,'swap at x=0',27,RED)
box(1370,1395,1045,150,'#fff3ee',RED)
text(1398,1422,'‖(ΘPu)n‖ = 2^(n³−n)/n ≥ 2ⁿ',32,RED)
text(1398,1484,'Pu(0) is outside Dom Θ(0); Pu is outside Ran h.',28,RED)
text(80,1590,'This is an auxiliary Hilbert-field example, not a foliation counterexample.  Actual G transport and displacement control remain required.',27)
text(45,1728,'Original CC0 diagram.  Exact proofs: CW.1–CW.12; intrinsic field and quotient: IJ.1–IJ.7.',27,GRAY)
text(45,1770,'The physical graph sum, differentiable inverse-module passage and original +1 comparison remain unproved.',27,RED)

def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))] for i in range(len(a))]
def diag(a,b): return [[a,Q(0)],[Q(0),b]]
def transpose(a): return list(map(list,zip(*a)))
def minus(a,b): return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
J=[[Q(0),Q(-1)],[Q(1),Q(0)]]
exact=[]
for n in range(2,7):
    a,b=Q(1,2**n),Q(1,2**(n**3)); A,B=1/a,1/b
    delta=[[Q(0),A-B],[A-B,Q(0)]]
    assert minus(mm(J,diag(A,B)),mm(diag(A,B),J))==delta
    two=mm(mm(diag(a,b),delta),diag(a,b)); one=mm(delta,diag(a*a,b*b))
    assert two==minus([[Q(0),Q(0)],[Q(0),Q(0)]],minus(mm(J,diag(a,b)),mm(diag(a,b),J)))
    assert abs(two[0][1])==a-b and abs(one[1][0])==B/(A*A)-1/A
    exact.append(dict(n=n,two_sided_norm=str(a-b),one_sided_norm=str(B/(A*A)-1/A)))
A,B=Q(4),Q(256); C,a=Q(1,2),Q(1,4); constant=2*C**4/a**3
lo,hi=a*A*A+constant,a*B*B+constant
det=lo*hi-(B-A)**2
assert constant==8 and lo==12 and hi==16392 and det==133200
assert det>0 and lo>0 and hi>0 and transpose(J)==[[Q(0),Q(1)],[Q(-1),Q(0)]]
assert not overflow
im.save(OUTPUT/'normal-form-weight.png'); svg.append('</svg>')
(OUTPUT/'normal-form-weight.svg').write_text('\n'.join(svg),encoding='utf-8')
data=dict(schema='normal-form-weight-figure/v1',license='CC0',real_coefficient_example=True,
          block_checks=exact,order_sample=dict(C=str(C),a=str(a),remainder=str(constant),diagonal=[str(lo),str(hi)],determinant=str(det),both_signs_positive=True),
          finite_exact_matrix_cases=len(exact),derivative_and_inverse_identity_checked=True,normalizations_are_separate=True,text_canvas_overflows=overflow,
          font_sha256=hashlib.sha256(font_bytes).hexdigest(),font_dependency='Shared unchanged DejaVuSans.ttf; complete font and notice embedded in SVG',
          proof_locators=['CW.1–CW.9','CW.10–CW.12','IJ.1–IJ.7'],
          human_source_context='Connes, A survey of foliations and operator algebras (1982), end of Section8; the normal-form and real block proofs are original CW.1–CW.12',
          completed_section_domain_example_proved=True,actual_G_weight_transport_domain_proved=False,physical_graph_operator_proved=False)
(OUTPUT/'NORMAL-FORM-CHECKS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exact_matrix_cases=len(exact),positive_order_determinant=str(det),canvas_overflows=len(overflow))))

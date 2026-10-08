"""Exact pedagogical identity and dual-map diagram."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1];p=r;f=p/'figures/weak-commutator-dual-limit.svg'
ns='http://www.w3.org/2000/svg';ET.register_namespace('',ns)
svg=ET.Element('{'+ns+'}svg',{'width':'780','height':'440','viewBox':'0 0 780 440','role':'img','aria-labelledby':'title desc'})
def e(tag,attrs,text=None,parent=svg):
    a=ET.SubElement(parent,'{'+ns+'}'+tag,attrs)
    if text is not None:a.text=text
    return a
e('title',{'id':'title'},'The principal weak commutator and the natural-dual regularizer limit')
e('desc',{'id':'desc'},'The real principal commutator equals minus twice the imaginary weak source plus twice the imaginary lower form minus twice the imaginary lower defect. The full regularizer commutator maps the energy space to its antidual and converges to the cutoff commutator for a fixed input.')
e('rect',{'width':'780','height':'440','fill':'#f8fafc'})
def text(x,y,s,size=16,weight='normal'):
    e('text',{'x':str(x),'y':str(y),'font-family':'Arial, sans-serif','font-size':str(size),'fill':'#132238','font-weight':weight},s)
def box(x,y,w,h):
    e('rect',{'x':str(x),'y':str(y),'width':str(w),'height':str(h),'rx':'8','fill':'white','stroke':'#6585a7','stroke-width':'1.3'})
text(22,30,'Principal weak commutator: keep all forcing terms',20,'bold')
box(22,48,736,68)
text(35,76,'Cλ = −2 Im ⟨Aλ f, Aλu⟩ + 2 Im q₁(Aλu,Aλu) − 2 Im Δ₁,λ',18,'bold')
text(35,101,'q₀ is Hermitian; q₁ may be complex. The sign uses the linear-first convention. (WC13)',14)
box(22,134,736,65)
text(35,160,'|Δ₁,λ| ≤ C X₋²,    X₋ = ‖u‖V + ‖Q₋u‖V',18)
text(35,185,'order Q₋ = s − 1 = ν − 3/2. One ordinary normal derivative per factor. (WC8–WC12)',14)
text(22,232,'Regularized equation: retain the variable-coefficient error',20,'bold')
box(22,251,736,61)
text(35,277,'PΛᵣu = Λᵣf + Eᵣu,    Eᵣu = [P,Λᵣ]Vu ∈ V*',18,'bold')
text(35,299,'Eᵣ: V → V* is uniformly bounded at fixed supports; the full form is used. (WC16–WC18)',14)
box(22,331,736,68)
text(35,357,'Λᵣf → χf,    Eᵣu → P(χu) − χPu    strongly in V*',18)
text(35,382,'Both form domains. Fixed input and widths. The cutoff error can remain nonzero. (WC19–WC21)',14)
text(22,425,'The positive-symbol factor and the higher-order microlocal regularizer estimate remain to be proved.',14)
f.parent.mkdir(parents=True,exist_ok=True);ET.indent(svg);ET.ElementTree(svg).write(f,encoding='utf-8',xml_declaration=True)
out={'schema':'an04-weak-commutator-figure/v1','svg':f.relative_to(r).as_posix(),'svg_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'width':780,'height':440,'proof_locators':'WC8–WC21','source_credit':'András Vasy free paper Lemma2.8/PDF14–15 and Section6/PDF37–38; new receiving argument and figure by GPT-6.1 Sol (OpenAI), Ultra','new_expression_licence':'CC0-1.0','pedagogical_estimate_diagram':True,'original_research_claim':False,'actual_render_visually_inspected':False,'preserved_original_diagram':True}
(p/'figure-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'figure_source_created':True,'canvas':[780,440]})

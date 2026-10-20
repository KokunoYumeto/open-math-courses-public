from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
def text(x,y,s,size=23,weight='normal',fill='#203c50'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(s)}</text>'
def rect(x,y,w,h,fill):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#c4d3dd"/>'
def arrow(x1,y1,x2,y2):return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="#315c95" stroke-width="2.5" marker-end="url(#arrow)"/>'
def indexed(x,y,base,index):return f'<text x="{x}" y="{y}" font-size="23" fill="#203c50">{escape(base)}<tspan baseline-shift="sub" font-size="16">{escape(index)}</tspan></text>'
def begin(title,desc,height):return ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="'+str(height)+'" viewBox="0 0 1200 '+str(height)+'" role="img" aria-labelledby="title desc">',
    '<title id="title">'+escape(title)+'</title><desc id="desc">'+escape(desc)+'</desc>',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#315c95" stroke-width="1.5"/></marker></defs>',
    '<rect width="1200" height="'+str(height)+'" fill="#fbfcfe"/><g font-family="DejaVu Sans,Arial,sans-serif">']
parts=begin('The finite Cartan identity determines the action',
    'The holonomic pair plane Lambda in the determining-jet and equation-jet fibre product maps by d sigma j to the next equation plane. The inductive point-action formula gives the same plane. Together with the same lower jet, plane injectivity forces equality of the next jets. Full action morphisms, stabilizer schemes and orbit symbols agree, so the one finite-level Lie-Tresse domain applies.',920)
parts += [text(30,43,'A finite Cartan identity determines the actual jet action',27,'bold'),
 rect(25,65,1150,120,'#edf3fb'),
 text(45,104,'Given: σⱼ : Gʲ ×_M Eʲ → Eʲ,  with the specified base M and σ₀.',24,'bold'),
 text(45,145,'Gʲ ⊂ Dʲ(M); finite order, FI, algebraic fixed-point groups.  No action formula prescribed.',21),
 rect(25,205,1150,310,'#f1f8f5'),
 text(45,245,'Finite differential compatibility · (4.116)–(4.117)',24,'bold'),
 text(65,300,'Λ ⊂ T(Gʲ ×_M Eʲ)',24),arrow(360,293,680,293),text(454,279,'dσⱼ',22),
 text(718,300,'L(σⱼ₊₁(g,e))',24),
 text(65,354,'Pair the two holonomic planes by their common source vector.',22),
 text(65,396,'Induction and the transformed-graph chain rule also give L(g⁽ʲ⁺¹⁾e).',22),
 text(65,440,'Same lower jet + same holonomic plane ⇒ same next jet.',24,'bold'),
 text(65,483,'Thus σⱼ(g,e)=g⁽ʲ⁾e at every finite order.  Proof: Theorem 4.45.',23),
 rect(25,535,1150,135,'#fff6eb'),
 text(45,576,'Equality of action morphisms, including every group component',24,'bold'),
 text(45,617,'⇒ full stabilizer schemes, tangent kernels, orbit tangents Δⱼ and symbols ϖⱼ agree.',23),
 text(45,652,'The reduced product point test gives scheme equality, not only infinitesimal equality.',20),
 rect(25,690,1150,155,'#edf3fb'),
 text(45,730,'One finite domain · Theorems 4.28–4.38 and 4.45',24,'bold'),
 text(45,771,'∃ L and invariant U⊂Eᴸ: every point of every complete higher inverse image is covered.',22),
 text(45,810,'A_L = F_L[∇^α f_b : |α|>0]; affine quotients and finite/formal geometric separation.',22),
 text(30,884,'Proof: Theorem 4.45, (4.116)–(4.120).  Context: Kruglikov–Lychagin, arXiv:1111.5480v3.',17),
 text(30,908,'GPT-6.1 Sol (OpenAI). CC0 1.0.',16),'</g></svg>']
cartan_svg='\n'.join(parts)+'\n'

svg=cartan_svg
if __name__=='__main__':
    (OUT/'cartan-finite-jet-action.svg').write_bytes(svg.encode('utf-8'))
